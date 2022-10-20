from math import *

class Carte:
  def __init__(self,couleur:str,valeur:int)-> None:
    if (valeur > 14 or valeur < 2):
      raise ValueError(valeur)
    elif (couleur not in ["trefle","coeur","pique","carreau"]):
      raise ValueError(couleur)
    else:
      self.valeur=valeur
      self.couleur=couleur

  def GetAttributs(self:object)-> tuple:
    return self.couleur,self.valeur

  def GetValeur(self:object)->int:
    return self.valeur
  
  def GetCouleur(self:object)->str:
    return self.couleur