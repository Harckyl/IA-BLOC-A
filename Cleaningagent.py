import threading
import environment as env
import BFS 
import numpy as np
import Astar
import function_create_arbre as create_arbre
import time

class cleaningAgent(threading.Thread):
    def __init__(self,choix):
        super(cleaningAgent, self).__init__()
        self.position = 0
        self.choix = choix
        self.points = 0

    def observeEnvironment(self):
        return environment.getChoice(self.position, rooms)
    
    def action_choice(self, deplacement, etat, rooms):
        if (deplacement == 0 and etat == "v"):
            return 0
        if (etat == "b" or etat == "bp"):
            if(etat == "bp"):
                rooms[int(self.position / 10)][self.position % 10] = "p"
                self.points += 5
                return 1
            rooms[int(self.position / 10)][self.position % 10] = "v"
            self.points += 5
            return 1
        if (etat == "p"):
            rooms[int(self.position / 10)][self.position % 10] = "v"
            self.points += 1
            return 2
        if (deplacement != 0 and etat == "v"):
            self.points -= 1
            return 3

    def run(self):
        while True:
            test = BFS.BFSalgorithm()
            root = create_arbre.Arbre(self.position)
            deplacement = 0
            root.Create_arbre(8)
            if (self.choix == 1):
                #on choisit le BFS
                deplacement = (test.explorer(root,Mamatrice,rooms))
                etat = self.observeEnvironment()
                action = self.action_choice(deplacement, etat, rooms)

            if(self.choix == 2):
                pos_but = environment.cherche_but(environment.rooms)
                if (pos_but) != -11 and pos_but != self.position:    
                    direction = Astar.Astar(rooms, (int(self.position % 10),int(self.position / 10)), (int(pos_but % 10),int(pos_but/ 10)))[1]
                    deplacement += 10 * direction[1]
                    deplacement += 1 * direction[0]
                else:
                    deplacement = 0 
                print(deplacement)
                etat = self.observeEnvironment()
                print(etat)
                action = self.action_choice(deplacement, etat, rooms)

            if(deplacement != None and action == 3):
                self.position = deplacement
                deplacement = None
                print("le robot se déplace")
            if(action == 0):
                print("le robot ne fait rien")
            if(action == 1):
                print("le robot ramasse le bijou")
            if(action == 2):
                print("le robot aspire une poussière")
            print("la position du robot est en x: " + str(self.position % 10) + " et en y : " + str(int(self.position / 10)))
                
            time.sleep(1)
        
		

    

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

rooms = np.full((5,5),"v")
print(rooms)
maxRep = 30
environment = env.roomsThread(maxRep,rooms)
environment.start() # This actually causes the thread to run
agent = cleaningAgent(2)
agent.start()
#print(Astar.Astar(rooms, (0,0), (4,4))[1])
print("DONE")
