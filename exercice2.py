import math
class Rectangle:
    def __init__(self, longeur, largeur):
        self.longeur = longeur
        self.largeur = largeur

    def calucul_aire(self):
        return self.longeur * self.largeur

    def afficher_infos(self):
        return print('longeur:', self.longeur, 'largeur:', self.largeur, 'aire:', self.longeur * self.largeur)

Rectangle().afficher_infos()
