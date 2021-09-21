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
      return (T.get_valeur(),affiche(T.get_gauche()),affiche(T.get_droit()))

Mamatrice = [[0 for i in range(5)] for i in range(5)]

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



def Create_arbre(Matrice, depart):
   racine = Arbre(depart)
   if depart + 10 < 44:
       racine.insert_droit(depart + 10)
   if depart - 10 > 0:
       racine.insert_gauche(depart - 10)
   if (depart + 1) % 10 < 5:
       racine.insert_bas(depart + 1)
   if depart % 10 > 0:
       racine.insert_haut(depart - 1)
   




