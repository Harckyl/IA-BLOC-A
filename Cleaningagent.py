import threading
import environment as env
class cleaningAgent:
    test = 1

    def __init__(self):
        self.test = 2
        self.position = 0

    def observeEnvironment(self):
        env.environment.getChoice(self.position)

    def testing(self, testingvariable):
        self.test = self.test + testingvariable
        print(self.test)
    




#initialisation matrice coordonnées
    Mamatrice = [[0 for i in range(5)] for i in range(5)]
    profondeur = 5

    Colonne = len(Mamatrice)
    Ligne = len(Mamatrice[0])


    #les coordonnées du tableau font référence à la position en x et en y
    #exemple : matrice[0][1] = 1, matrice[2][1] = 21 ....
    #si on veut partir à droite, il faudra additionner 10
    #si on veut monter, il faut soustraire 1
    for y in range(Colonne):
        for x in range(Ligne):
            Mamatrice[x][y] = int(str(x) + str(y))
            print (Mamatrice[x][y], end = " ")
    print(" ")    
#fin initialisation


cleaningagent = cleaningAgent()
cleaningagent.testing(12)

