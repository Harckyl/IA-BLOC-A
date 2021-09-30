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
        self.test = 2
        self.position = 0
        self.choix = choix

    def observeEnvironment(self):
        env.environment.getChoice(self.position)
    
    def run(self):
        while True:
            if(self.choix == 1):
                test = BFS.BFSalgorithm()
                root = create_arbre.Arbre(self.position)
                root.Create_arbre(8)
                print(test.explorer(root,Mamatrice,rooms))
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
agent = cleaningAgent(1)
agent.start()
#test = threading.Thread(target=env.roomsThread.run, args=[rooms])
#test.start()
print(Astar.Astar(rooms, (0,0), (4,4))[1])
print("DONE")
