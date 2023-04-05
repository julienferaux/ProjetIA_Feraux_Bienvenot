
from colorama import init, Fore, Back, Style

global taille

taille =7

class GameState:
    """initialise le plateau à vide , si other != null alors le nouveau plateau est copier sur other"""
    def __init__(self, other=None):
        if other is None:
            self.board = [[0 for _ in range(7)] for _ in range(7)]
        else:
            self.board = [row.copy() for row in other.board]

    def __str__(self):
        board_str = '\n'.join([' '.join([str(cell) for cell in row]) for row in self.board])
        return f"{board_str}"

    def set_cell(self, row, col, value):
        self.board[row][col] = value

    def set_board(self, board_str):
        rows = board_str.strip().split('\n')
        for i, row in enumerate(rows):
            cells = row.split()
            for j, cell in enumerate(cells):
                self.set_cell(i, j, int(cell))

    def print_board(self):
        for row in range(taille):
            for col in range(taille):
                if self.board[row][col] == 0:
                    print( " ", end=' ')
                elif self.board[row][col] == 1:
                    print(Fore.RED + "1", end=' ')
                elif self.board[row][col] == 2:
                    print(Fore.BLUE + Style.DIM + "2", end=' ')
                else:
                    print(Fore.BLUE + "3", end=' ')
            print(Style.RESET_ALL)
        print("")


    def move_piece(self, start_row, start_col, end_row, end_col):
        """ move_piece : déplace une piece si c'est possible"""
        if (self.board[start_row][start_col] != 1) &\
                (self.board[start_row][start_col] != 2 )&\
                    (self.board[start_row][start_col] != 3 ):
            raise ValueError("There is no piece to move in the starting position :" + str(self.board[start_row][start_col]))
        if self.board[end_row][end_col] != 0:
            raise ValueError("The destination position is not empty")

        value  = self.board[start_row][start_col]

        if start_row == end_row:
            if start_col < end_col:
                step = 1
            else:
                step = -1
            for col in range(start_col + step, end_col+1, step):

                if self.board[start_row][col] != 0:
                    raise ValueError("The piece cannot move through occupied positions")
        elif start_col == end_col:

            if start_row < end_row:
                step = 1
            else:
                step = -1
            for row in range(start_row + step, end_row, step):
                if self.board[row][start_col] != 0:
                    raise ValueError("The piece cannot move through occupied positions")
        else:
            raise ValueError("The piece can only move horizontally or vertically")

        self.set_cell(start_row, start_col, 0)
        self.set_cell(end_row, end_col, value)
        self.capture_opponents2((end_row,end_col))

    """is_valid_position vérifie si la position existe"""
    def is_valid_position(pos):
        """
        Vérifie si une position donnée est valide dans le contexte du jeu Ard Ri.
        Retourne True si c'est le cas, False sinon.
        """

        row, col = pos
        return 0 <= row < taille and 0 <= col < taille

    def is_valid_move(self, start_pos, end_pos):
        """
        Vérifie si le déplacement du pion de la position de départ à la position finale est valide.
        Retourne True si c'est le cas, False sinon.
        """
        pion = self.board[start_pos[0]][start_pos[1]]
        # Vérifie que les positions de départ et d'arrivée sont valides
        if not self.is_valid_position(start_pos) or not self.is_valid_position(end_pos):
            return False

        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Vérifie que la case de départ contient un pion
        if self.board[start_row][start_col] == 0:
            return False

        # Vérifie que le déplacement se fait sur une ligne ou une colonne, pas en diagonale
        if start_row != end_row and start_col != end_col:
            return False
        # Vérifie que toutes les cases empruntées sont vides
        if start_row == end_row:
            step = 1 if start_col < end_col else -1
            for col in range(start_col + step, end_col, step):
                if self.board[start_row][col] != 0:
                    return False
        else:
            step = 1 if start_row < end_row else -1
            for row in range(start_row + step, end_row, step):
                if self.board[row][start_col] != 0:
                    return False

        # Vérifie que le déplacement n'est pas sur une des forteresses ou le roi

        if pion ==1 :
            if end_pos in [(0, 0), (0, taille-1), (taille-1, 0), (taille-1, taille-1),(int(taille/2)+1,int(taille/2)+1)]:
                return False

        return True

    def is_valid_position(self,pos):
        """
        Vérifie si une position donnée est valide dans le contexte du jeu Ard Ri.
        Retourne True si c'est le cas, False sinon.
        """
        row, col = pos
        return 0 <= row < taille and 0 <= col < taille

    def get_possible_move(self, start_pos):
        """
        Retourne tous les états possibles du plateau de jeu après que le pion donné a été déplacé.
        """
        possible_move = []
        # Boucle sur toutes les positions possibles pour le déplacement
        for i in range(-start_pos[0], taille-start_pos[0]):
            end_pos = (start_pos[0] + i, start_pos[1])
            # Vérifie si le déplacement est valide et effectue le déplacement si c'est le cas
            if self.is_valid_move(start_pos, end_pos):

                new_board = GameState(self)
                try:
                    new_board.move_piece(start_pos[0],start_pos[1], end_pos[0],end_pos[1])
                    possible_move.append(end_pos)
                except Exception as e:
                    #print(str(e))
                    a=0;

        for j in range(-start_pos[1], taille-start_pos[1]):

            end_pos = (start_pos[0], start_pos[1] + j)
            # Vérifie si le déplacement est valide et effectue le déplacement si c'est le cas

            if self.is_valid_move(start_pos, end_pos):

                new_board = GameState(self)
                try:
                    new_board.move_piece(start_pos[0],start_pos[1], end_pos[0],end_pos[1])
                    possible_move.append(end_pos)
                except Exception as e:
                    #print(str(e))
                    a=0;

        return possible_move

    def get_pion_joueur(self,estJoueurBlanc):
        positions = []
        for i in range(0,taille):
            for j in range(0,taille):
                if estJoueurBlanc :
                    if (self.board[i][j] == 2 ) | (self.board[i][j] == 3):
                        positions.append((i, j))
                else:
                    if (self.board[i][j] == 1 ):
                        positions.append((i, j))
        return positions

    def capture_opponents2(self, last_move):

        x = last_move[0]
        y = last_move[1]
        maCouleur = 1 if self.board[x][y] == 1 else 2
        voisin = []
        voisin.append(((x-1,y),(x-2,y)))
        voisin.append(((x+1,y),(x+2,y)))
        voisin.append(((x,y-1),(x,y-2)))
        voisin.append(((x,y+1),(x,y+2)))

        for v in voisin :
            vx = v[0][0]
            vy = v[0][1]
            try:
                if(self.board[vx][vy]!= 0):
                    couleurv1 = 1 if self.board[vx][vy] == 1 else 2
                    if couleurv1 != maCouleur :
                        vx2 = v[1][0]
                        vy2 = v[1][1]
                        if(v[1] in [(0, 0), (0, taille-1), (taille-1, 0), (taille-1, taille-1),(int(taille/2)+1,int(taille/2)+1)]):
                            self.board[vx][vy]=0
                        else:
                            couleurv2 = 1 if self.board[vx2][vy2] == 1 else 2
                            if couleurv2 == maCouleur:
                                self.board[vx][vy]=0
            except Exception as e:
                #print(str(e))
                a=0



game = GameState()
"""
board_str = '0 0 1 1 1 0 0\n' \
            '0 0 0 1 0 0 0\n' \
            '1 0 2 2 2 0 1\n' \
            '1 1 2 3 2 1 1\n' \
            '1 0 2 2 2 0 1\n' \
            '0 0 0 1 0 0 0\n' \
            '0 0 1 1 1 0 0\n'
"""
board_str = '0 0 1 1 1 0 0\n' \
            '0 0 0 1 0 0 0\n' \
            '1 0 2 2 2 0 1\n' \
            '1 1 2 3 2 1 1\n' \
            '1 0 2 2 2 0 1\n' \
            '0 0 0 1 0 0 0\n' \
            '0 0 1 1 1 0 0\n'

game.set_board(board_str)
game.print_board()




"""
"""
ii=0
for pion in game.get_pion_joueur(True) :

    for move in game.get_possible_move(pion):
        new_board = GameState(game)
        new_board.move_piece(pion[0], pion[1], move[0], move[1])
        new_board.print_board()
        print("-------------------------------------------------")
        for pion2 in new_board.get_pion_joueur(False):
            for move2 in new_board.get_possible_move(pion2):
                new_board2 = GameState(new_board)
                new_board2.move_piece(pion2[0], pion2[1], move2[0], move2[1])
                new_board2.print_board()

#game.move_piece(6,2,6,0)
#game.print_board()
