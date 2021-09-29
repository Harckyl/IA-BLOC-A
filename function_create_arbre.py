class Arbre:
   def __init__(self, valeur):
      self.valeur = valeur
      self.enfant_gauche = None
      self.enfant_droit = None
      self.enfant_haut = None
      self.enfant_bas = None
      self.parent = None

   def insert_gauche(self, valeur, parent):
      if self.enfant_gauche == None:
         self.enfant_gauche = Arbre(valeur)
         self.enfant_gauche.parent = Arbre(parent)
      else:
         new_node = Arbre(valeur)
         new_node.parent = Arbre(parent)
         new_node.enfant_gauche = self.enfant_gauche
         self.enfant_gauche = new_node

   def insert_droit(self, valeur, parent):
      if self.enfant_droit == None:
         self.enfant_droit = Arbre(valeur)
         self.enfant_droit.parent = Arbre(parent)
      else:
         new_node = Arbre(valeur)
         new_node.parent = Arbre(parent)
         new_node.enfant_droit = self.enfant_droit
         self.enfant_droit = new_node

   def insert_haut(self, valeur, parent):
      if self.enfant_haut == None:
         self.enfant_haut = Arbre(valeur)
         self.enfant_haut.parent = Arbre(parent)
      else:
         new_node = Arbre(valeur)
         new_node.parent = Arbre(parent)
         new_node.enfant_haut = self.enfant_haut
         self.enfant_haut = new_node

   def insert_bas(self, valeur, parent):
      if self.enfant_bas == None:
         self.enfant_bas = Arbre(valeur)
         self.enfant_bas.parent = Arbre(parent)
      else:
         new_node = Arbre(valeur)
         new_node.parent = Arbre(parent)
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

   def get_parent(self):
      return self.parent

   def Create_arbre(self, profondeur):
    if profondeur > 0:
       #déplacement vers la droite
        if self.get_valeur() + 10 <= 44:
           self.insert_droit(self.get_valeur() + 10, self.get_valeur())
           new_node = self.get_droit()
           new_node.Create_arbre(profondeur - 1)
        else:
         self.insert_droit(None, self.get_valeur())
       #déplacement vers la gauche
        if self.get_valeur() - 10 >= 0:
           self.insert_gauche(self.get_valeur() - 10, self.get_valeur())
           new_node = self.get_gauche()
           new_node.Create_arbre(profondeur - 1)
        else:
         self.insert_gauche(None, self.get_valeur())
       #déplacement vers la bas
        if (self.get_valeur() + 1) % 10 < 5:
           self.insert_bas(self.get_valeur() + 1, self.get_valeur())
           new_node = self.get_bas()
           new_node.Create_arbre(profondeur - 1)
        else:
         self.insert_bas(None, self.get_valeur())
       #déplacement vers la haut
        if self.get_valeur() % 10 > 0:
           self.insert_haut(self.get_valeur() - 1, self.get_valeur())
           new_node = self.get_haut()
           new_node.Create_arbre(profondeur - 1)
        else:
         self.insert_haut(None, self.get_valeur())
   





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
   print(" ")



racine = Arbre(Mamatrice[0][0])


#fonction récursive : on choisi le nombre de récursions avec profondeur
#value = la valeur du node
#node = noeud, au départ, c'est la racine

   
racine.Create_arbre(8)



print(racine.get_bas().get_bas().get_haut().get_parent().get_valeur())


