import random

global tailleX
tailleX = 9
tailleY = 3
grandeDonnee = [[31, 242, 392, 208, 48, 135, 232, 37, 1255, 32, 7, 663, 350, 1378, 17, 412, 44, 905, 409, 613, 599, 301, 2, 6, 69, 12],
         [158, 2, 1, 2, 130, 1, 2, 0, 132, 4, 10, 181, 1, 1, 146, 1, 3, 187, 29, 16, 44, 3, 0, 0, 4, 0],
         [312, 0, 73, 19, 765, 2, 2, 411, 209, 3, 5, 124, 5, 1, 677, 11, 7, 100, 14, 142, 132, 2, 0, 0, 11, 0],
         [427, 1, 8, 24, 2409, 2, 5, 25, 378, 3, 0, 14, 21, 5, 231, 4, 6, 134, 64, 3, 406, 4, 1, 0, 5, 0],
         [616, 176, 917, 998, 782, 258, 209, 67, 179, 96, 8, 1382, 1056, 2121, 136, 699, 190, 1514, 3318, 1307, 761, 258, 11, 125, 15, 60],
         [181, 1, 1, 8, 180, 118, 1, 1, 190, 0, 0, 43, 1, 1, 213, 1, 2, 106, 12, 1, 61, 0, 0, 0, 1, 0],
         [135, 1, 10, 9, 408, 4, 63, 3, 69, 6, 4, 74, 10, 103, 47, 5, 1, 197, 12, 23, 81, 1, 0, 0, 2, 0],
         [267, 5, 4, 1, 285, 0, 0, 0, 149, 3, 0, 3, 4, 17, 107, 0, 3, 18, 5, 0, 42, 0, 1, 0, 7, 0],
         [176, 85, 203, 172, 1030, 114, 115, 6, 49, 14, 0, 798, 181, 797, 524, 75, 215, 400, 897, 1243, 11, 190, 1, 40, 0, 4],
         [76, 0, 0, 0, 100, 0, 0, 0, 2, 0, 0, 0, 0, 0, 91, 0, 0, 0, 0, 0, 42, 0, 0, 0, 2, 0],
         [8, 0, 0, 0, 6, 0, 3, 0, 6, 0, 0, 0, 10, 3, 9, 0, 0, 5, 1, 0, 0, 0, 0, 0, 3, 0],
         [1270, 14, 22, 58, 2366, 25, 14, 39, 512, 4, 1, 647, 18, 41, 281, 69, 47, 16, 126, 42, 369, 14, 0, 0, 15, 1],
         [510, 152, 11, 11, 1099, 0, 1, 1, 302, 0, 0, 7, 243, 4, 334, 201, 2, 10, 10, 8, 52, 1, 0, 0, 3, 0],
         [405, 30, 438, 785, 985, 124, 222, 24, 316, 17, 7, 89, 68, 249, 303, 130, 82, 55, 846, 1694, 114, 109, 0, 1, 19, 20],
         [6, 83, 88, 101, 46, 32, 115, 7, 452, 14, 3, 184, 391, 1646, 8, 175, 19, 491, 126, 109, 1086, 28, 9, 4, 62, 4],
         [671, 1, 3, 21, 441, 5, 1, 136, 119, 0, 0, 377, 2, 4, 505, 125, 1, 363, 31, 65, 140, 1, 0, 0, 1, 0],
         [2, 0, 3, 0, 1, 0, 0, 1, 0, 0, 0, 1, 3, 0, 0, 1, 0, 1, 0, 0, 975, 0, 0, 0, 0, 0],
         [896, 53, 168, 302, 1885, 46, 96, 5, 583, 11, 3, 292, 181, 88, 520, 82, 51, 176, 386, 445, 183, 77, 1, 1, 21, 5],
         [896, 53, 168, 302, 1885, 46, 96, 5, 583, 11, 3, 292, 181, 88, 520, 82, 51, 176, 386, 445, 183, 77, 1, 1, 21, 5],
         [809, 85, 306, 735, 1377, 151, 73, 83, 565, 36, 0, 453, 192, 107, 521, 496, 191, 137, 702, 578, 343, 92, 1, 6, 30, 10],
         [881, 25, 166, 515, 1484, 52, 19, 64, 984, 28, 3, 331, 70, 40, 363, 268, 96, 668, 404, 269, 270, 41, 4, 6, 18, 3],
         [168, 87, 165, 162, 781, 40, 83, 4, 534, 41, 3, 302, 128, 516, 19, 184, 15, 980, 591, 469, 14, 177, 1, 264, 8, 4],
         [277, 0, 1, 0, 502, 0, 0, 0, 288, 0, 0, 1, 0, 0, 167, 0, 0, 81, 0, 0, 11, 0, 0, 0, 0, 0],
         [11, 1, 1, 0, 3, 0, 0, 2, 8, 0, 0, 0, 0, 0, 3, 0, 1, 0, 4, 0, 0, 0, 0, 0, 2, 0],
         [35, 14, 37, 36, 68, 8, 7, 5, 57, 0, 0, 21, 15, 3, 7, 56, 11, 3, 15, 35, 2, 18, 0, 4, 0, 0],
         [63, 0, 7, 7, 59, 3, 4, 0, 0, 0, 0, 13, 8, 5, 15, 14, 0, 10, 75, 9, 2, 4, 0, 0, 0, 0],
         [8, 0, 2, 6, 49, 3, 1, 0, 1, 1, 0, 11, 4, 2, 15, 4, 1, 0, 3, 1, 0, 7, 4, 0, 0, 2]
]
## Donné réduite pour pouvoir faire des testes rapides
petiteDonnee = [
    [31, 242, 392, 208],
    [158, 2, 1, 2],
    [312, 0, 73, 19],
    [427, 1, 8, 24]
]
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
petit_clavier = [[0 for j in range(3)] for i in range(2)]

# classe de l'état du clavier de 4 * 10
class grandClavier:
    # other pour inicialisé un nouvel etat a partir d'un autre ( genre le parent )
    def __init__(self, other=None):
        if other is None:
            self.tableau = [[' '] * 10 for _ in range(4)]
        else:
            self.tableau = [row.copy() for row in other.tableau]

    #fonction qui renvoie un paire de paire de coordonnées aléatoire dans le tableau
    def afficher(self):
        for i in range(4):
            print(' '.join(self.tableau[i]))

    def set(self, i, j, value):
        self.tableau[i][j] = value

    def get(self, i, j):
        return self.tableau[i][j]

    def permuter(self, mouve):
        lettre1 = self.get(mouve[0][0],mouve[0][1])
        lettre2 = self.get(mouve[1][0],mouve[1][1])
        self.set(mouve[0][0],mouve[0][1],lettre2)
        self.set(mouve[1][0],mouve[1][1],lettre1)

    def evaluer_etat(christant):  # christant le clavier
        matBool = matriceBooleen()
        for i in range(0, 4):
            for j in range(0, 10):
                case = christant.get(i, j)
                if case != ' ':
                    positionLettre1 = alphabet.index(case)
                    if i < 2:
                        case2 = christant.get(i + 1, j)
                        if case2 != ' ':
                            positionLettre2 = alphabet.index(case2)
                            matBool.set(positionLettre1, positionLettre2, 1)
                            matBool.set(positionLettre2, positionLettre1, 1)
                    if i > 0:
                        case3 = christant.get(i - 1, j)
                        if case3 != ' ':
                            positionLettre3 = alphabet.index(case3)
                            matBool.set(positionLettre1, positionLettre3, 1)
                            matBool.set(positionLettre3, positionLettre1, 1)
                    if j < 9:
                        case4 = christant.get(i, j + 1)
                        if case4 != ' ':
                            positionLettre4 = alphabet.index(case4)
                            matBool.set(positionLettre1, positionLettre4, 1)
                            matBool.set(positionLettre4, positionLettre1, 1)
                    if j > 0:
                        case5 = christant.get(i, j - 1)
                        if case5 != ' ':
                            positionLettre5 = alphabet.index(case5)
                            matBool.set(positionLettre1, positionLettre5, 1)
                            matBool.set(positionLettre5, positionLettre1, 1)
        res = 0
        for i in range(0, 26):
            for j in range(0, 26):
                res += matBool.get(i, j) * grandeDonnee[i][j]

        #matBool.afficher()
        return res

# matrice de booleen pour evaluer un etat
class matriceBooleen:
    def __init__(self):
        self.matrice = [[0] * 26 for _ in range(26)]

    def set(self, i, j, value):
        self.matrice[i][j] = value

    def get(self, i, j):
        return self.matrice[i][j]

    def afficher(self):
        for i in range(26):
            for j in range(26):
                print(self.matrice[i][j], end="")
            print()

def get_random_coordonnee():
    i1, j1 = random.randint(0, 3), random.randint(0, 9)
    i2, j2 = random.randint(0, 3), random.randint(0, 9)
    return ((i1,j1),(i2,(j2)))

def get_max_paire(listeMouvement):
    max_value = float('-inf')
    max_pair = None
    for pair in listeMouvement:
        if pair[1] > max_value:
            max_value = pair[1]
            max_pair = pair
    return max_pair

clavier = grandClavier()
clavier.tableau =   [[' ', 'C', ' ', ' ', 'R', 'K', 'W', ' ', ' ', 'I'],
                    ['T', 'O', 'U', 'B', 'P', 'A', 'M', ' ', 'J', ' '],
                    ['Q', 'S', 'V', ' ', 'N', 'L', 'H', ' ', 'X', 'G'],
                    [' ', ' ', 'E', 'Z', 'D', 'F', 'Y', ' ', ' ', ' ']]

tabu_size = 10  #Taille du tabou
nbMouvementTester = 100
tabou = []       #liste du tabou

clavier.afficher()
print(clavier.evaluer_etat())
print()
i=0
listeMouvement = []
while( i < 1000):
    if (i%100 == 0):
        print(int(i/100),"%fi")
    listeMouvement = []
    for j in range(nbMouvementTester):
        mouve = get_random_coordonnee()
        fils = grandClavier(clavier)
        fils.permuter(mouve)
        listeMouvement.append((mouve,fils.evaluer_etat() ))

    max_pair = get_max_paire(listeMouvement)
    if (len(tabou) > tabu_size):
        tabou.pop(0)
    while 1 :
        max_pair = get_max_paire(listeMouvement)
        if (max_pair[0] in tabou) :
            listeMouvement.pop(listeMouvement.index(max_pair))
        else:
            break
    clavier.permuter(max_pair[0])
    tabou.append(max_pair[0])
    i+=1




clavier.afficher()
print(clavier.evaluer_etat())
"""
  F Q   Y P Z      
M O U D T A R G    
K B L E N C H J    
  W I S V X        
34537
"""