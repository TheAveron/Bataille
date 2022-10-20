from math import *

class Carte:
  def __init__(self,couleur:str,valeur:int)-> None:
    """
    IN : couleur la couleur de la carte (trefle, carreau, pique, coeur), valeur la valeur de la carte (entre 1 et 14)
    OUT: défini les caracteristiques de la carte
    """
    if (valeur > 14 or valeur < 2):
      raise ValueError(valeur)
    elif (couleur not in ["trefle","coeur","pique","carreau"]):
      raise ValueError(couleur)
    else:
      self.valeur=valeur
      self.couleur=couleur

  def GetAttributs(self:object)-> tuple:
    """
    OUT: renvoie la couleur et la valeur de la carte
    """
    return self.couleur,self.valeur

  def GetValeur(self:object)->int:
    """
    OUT: renvoie la valeur de la carte
    """
    return self.valeur
  
  def GetCouleur(self:object)->str:
    """
    OUT: renvoie la couleur de la carte
    """
    return self.couleur
