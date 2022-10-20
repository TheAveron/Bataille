from carte import *
from random import *

class Paquet:
  def __init__(self)->None:
    self.paquet=list()

  def __getitem__(self,indice)->object:
    return self.paquet[indice]

  def append(self:object,carte:object)->None:
    self.paquet.append(carte)

  def remove(self:object,carte:object)->None:
    self.paquet.remove(carte)

  def clear(self):
    self.paquet.clear()

  def Generate(self,taille:int)->None:
    if taille in [32,52]:
      for couleur in ["trefle","coeur","pique","carreau"]:
        for valeur in range((15-(taille/4)),15):
          self.append(Carte(couleur,int(valeur)))
    else:
      raise ValueError(("taille",taille))
  
  def GetCartesAttributs(self:object)->list:
    return [i.GetAttributs() for i in self.paquet]

  def GetCartes(self:object)->object:
    return self.paquet
  
  def SetPaquet(self:object,paquet:list)->None:
    self.paquet=paquet
  
  def len(self:object)->int:
    return len(self.paquet)

  def GetRandCard(self:object)-> object:
    return choice(self.paquet)
  
  def Melange(self:object)->None:
    paquet_m=list()
    for i in range(len(self.paquet)):
      paquet_m.append(choice(self.paquet))
      self.paquet.remove(paquet_m[i])
    self.paquet=paquet_m