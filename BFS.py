import function_create_arbre as createarbre

class BFSalgorithm:
    def __init__(self):
        print("donothing")
    
    def explorer(self, StartingNode,matrixcoordonnee,matrixpoussiere):
        bfsqueue = []
        explored = [StartingNode]
        bfsqueue.insert(0,StartingNode)
        while bfsqueue != []:
            openednode = bfsqueue.pop()
            print("valeur is ",openednode.get_valeur())

            if self.verification(openednode.get_valeur(),matrixpoussiere):
                print("found")
                print(openednode.get_valeur())
                return self.get_deplacement(openednode)
            
            if openednode.enfant_gauche.get_valeur() != None:
                bfsqueue.insert(0,openednode.get_gauche())
           
            if openednode.enfant_droit.get_valeur() != None:
                bfsqueue.insert(0,openednode.get_droit())
            
            if openednode.enfant_bas.get_valeur() != None:
                bfsqueue.insert(0,openednode.get_bas())
            
            if openednode.enfant_haut.get_valeur() != None:
                bfsqueue.insert(0,openednode.get_haut())

    def get_deplacement(self,node):
        while node.get_parent() != None:
            node = node.get_parent()
        print(node.get_valeur())
        return node


    def verification(self,coordonnees,matrixpoussiere):
        xobject = int(int(coordonnees)/10)
        yobject = int(coordonnees)%10
        strobject = matrixpoussiere[xobject][yobject]
        if strobject == "b" or strobject == "p" or strobject == "bp":
            return True
        else:
            return False

        

Mamatrice = [[0 for i in range(5)] for i in range(5)]
Colonne = len(Mamatrice)
Ligne = len(Mamatrice[0])
for y in range(Colonne):
   for x in range(Ligne):
       Mamatrice[x][y] = int(str(x) + str(y))
       #print (Mamatrice[x][y], end = " ")
   #print(" ")

poussmatrice = [[0 for i in range(5)] for i in range(5)]
poussmatrice[1][2] = "b"
poussmatrice[0][0] = "p"
root = createarbre.Arbre(Mamatrice[3][4])

root.Create_arbre(8)
BFS = BFSalgorithm()
#print(root.getvaleur())
BFS.explorer(root,Mamatrice,poussmatrice)