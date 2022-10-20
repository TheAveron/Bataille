from paquet import *

def check(bt1:list,bt2:list)->bool:
  for i in range(len(bt1)):
    for i2 in range(i+1,len(bt2)):
      if bt1[i]==bt2[i2]:
        raise AttributeError("Une carte est en double")
  return False

class Bataille:
  def __init__(self):
    self.paquet = Paquet()
    self.joueur_1,self.joueur_2=None,None
    self.winer=None
    self.defausse=Paquet()
    self.ind=int()
    self.lengt=int()

    self.paquet.Generate(52)
    self.paquet.Melange()
    self.SetJoueurs()
    check(self.get()[1].GetCartesAttributs(),self.get()[2].GetCartesAttributs())

  def SetJoueurs(self:object)->None:
    self.joueur_1=Paquet()
    self.joueur_2=Paquet()
    self.joueur_1.SetPaquet([self.paquet[i] for i in range(0,self.paquet.len()-1,2)])
    self.joueur_2.SetPaquet([self.paquet[i] for i in range(1,self.paquet.len(),2)])

  def get(self:object)-> tuple:
    return self.paquet,self.joueur_1,self.joueur_2

  def CompaCartes(self,carte1,carte2)->None:
    self.joueur_1.remove(carte1),self.joueur_2.remove(carte2)
    self.defausse.append(carte1)
    self.defausse.append(carte2)
    if carte1.GetValeur()>carte2.GetValeur():
      for i in self.defausse:
        self.joueur_1.append(i)
      self.defausse.clear()
    elif carte2.GetValeur()>carte1.GetValeur():
      for i in self.defausse:
        self.joueur_2.append(i)
      self.defausse.clear()
    elif carte2.GetValeur()==carte1.GetValeur() and self.lengt>3:
      carte1,carte2=self.joueur_1[0],self.joueur_2[0]
      self.joueur_1.remove(carte1)
      self.joueur_2.remove(carte2)
      self.defausse.append(carte1)
      self.defausse.append(carte2)
      self.ind+=1

  def CompaJoueurs(self):
    lenj1=self.joueur_1.len()
    lenj2=self.joueur_2.len()
    if lenj1<lenj2: return lenj1
    else: return lenj2

  def win(self):
    lenj1=self.joueur_1.len()
    lenj2=self.joueur_2.len()
    if lenj1==0:
      self.winer = "Joueur 1"
    elif lenj2==0:
      self.winer = "Joueur 2"

  def Start(self):    
    while not self.winer:
      self.lengt=self.CompaJoueurs()
      self.ind=0
      while self.ind<self.lengt:
        carte1,carte2=self.joueur_1[0],self.joueur_2[0]

        self.CompaCartes(carte1,carte2)
        self.ind+=1

      self.joueur_1.Melange()
      self.joueur_2.Melange()

      self.win()        
    print(self.winer)

test=Bataille()
test.Start()
check(test.get()[1].GetCartesAttributs(),test.get()[2].GetCartesAttributs())
