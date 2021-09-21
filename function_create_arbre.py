class Arbre:
   def __init__(self, valeur):
      self.valeur = valeur
      self.enfant_gauche = None
      self.enfant_droit = None
      self.enfant_haut = None
      self.enfant_bas = None

   def insert_gauche(self, valeur):
      if self.enfant_gauche == None:
         self.enfant_gauche = Arbre(valeur)
      else:
         new_node = Arbre(valeur)
         new_node.enfant_gauche = self.enfant_gauche
         self.enfant_gauche = new_node

   def insert_droit(self, valeur):
      if self.enfant_droit == None:
         self.enfant_droit = Arbre(valeur)
      else:
         new_node = Arbre(valeur)
         new_node.enfant_droit = self.enfant_droit
         self.enfant_droit = new_node

   def insert_haut(self, valeur):
      if self.enfant_haut == None:
         self.enfant_haut = Arbre(valeur)
      else:
         new_node = Arbre(valeur)
         new_node.enfant_haut = self.enfant_haut
         self.enfant_haut = new_node

   def insert_bas(self, valeur):
      if self.enfant_bas == None:
         self.enfant_bas = Arbre(valeur)
      else:
         new_node = Arbre(valeur)
         new_node.enfant_bas = self.enfant_bas
         self.enfant_bas = new_node

   def get_valeur(self):
      return self.valeur

   def get_gauche(self):
      return self.enfant_gauche

   def get_droit(self):
      return self.enfant_droit

   def get_haut(self):
      return self.enfant_haut

   def get_bas(self):
      return self.enfant_bas



def affiche(T):
   if T != None:
      return (T.get_valeur(),affiche(T.get_gauche()),affiche(T.get_droit()),affiche(T.get_haut()),affiche(T.get_bas()))

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
   print()




racine = Arbre(Mamatrice[0][0])


#fonction récursive : on choisi le nombre de récursions avec profondeur
#value = la valeur du node
#node = noeud, au départ, c'est la racine
def Create_arbre(value, profondeur, node):
    if profondeur > 0:
       #déplacement vers la droite
        if value + 10 < 44:
           node.insert_droit(value + 10)
           new_node = node.get_droit()
           Create_arbre(value + 10, profondeur - 1, new_node)
       #déplacement vers la gauche
        if value - 10 >= 0:
           node.insert_gauche(value - 10)
           new_node = node.get_gauche()
           Create_arbre(value - 10, profondeur - 1, new_node)
       #déplacement vers la bas
        if (value + 1) % 10 < 5:
           node.insert_bas(value + 1)
           new_node = node.get_bas()
           Create_arbre(value + 1, profondeur - 1, new_node)
       #déplacement vers la haut
        if value % 10 > 0:
           node.insert_haut(value - 1)
           new_node = node.get_haut()
           Create_arbre(value - 1, profondeur - 1, new_node)
   
Create_arbre(Mamatrice[0][0], 3, racine)

print(racine.get_droit().get_gauche().get_valeur())




