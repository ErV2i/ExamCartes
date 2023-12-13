class Mage:
    nombreJoueur=0
    #connaitre le nombre de joeur si on veux connaitre le nombre de tours a faire plus tard
    def __init__ (self, srtNom, pv, valeurMana, maxMana, main, defausse):
        Mage.nombreJoueur+=1
        #ajouter 1 a chaque fois qu'un mage(Joueur) est crée
        self.__srtnom=srtNom
        self.__pv=pv
        self.__valeurMana=valeurMana
        self.__maxMana=maxMana
        self.__main=main
        self.__defausse=defausse

    def getNom (self):
        return self.__srtnom
    def getpv (self):
            return self.__pv
    def getVmana (self):
            return self.__valeurMana
    def getMmana (self):
            return self.__maxMana
    def getMain (self):
            return self.__main
    def getdefausse (self):
            return self.__defausse
    
    def jouerCarte (self,):
          self.__valeurmana-=Carte.getCmanaCarte
          return self.__valeurMana
          #quand on joue une carte on retir le prix de la carte au mana du joueur
    
    def getMana (self):
          if tour == %2:
                self.__valeurMana+=10
                #si le tour est paire (les 2 mage récupere 10 de mana)
    def atkMage (self):
          

class Carte:
    def __init__ (self, srtNom, coutMana, srtDescription):
        self.__srtNom=srtNom
        self.__coutMana=coutMana
        self.__srtDescription=srtDescription
    def getNomCarte (self):
            return self.__srtNom
    def getCmanaCarte(self):
            return self.__coutMana
    def getDesc (self):
            return self.__srtDescription
    
    def joueCarte (self,):
        #Quand on joue une carte on la perd mais j'ai aucune idée de comment supprimer une class :/
        print(f"Vous avez jouer la carte {self.__srtNom}, vous avez {self.__srtDescription}")

class Blast(Carte):
    def __init__ (self, srtNom, pv, atkScore):
        self.__srtNom=srtNom
        self.__pv=pv
        self.__atkScore=atkScore
    def getNomBlast (self):
          return self.__srtNom
    def getPvBlast (self):
          return self.__pv
    def getAtkBlast (self):
          return self.__atkScore
    
class Cristal(Carte):
    def __init__ (self, coutMana):
        self.__coutMana=coutMana
    def getCoMana (self):
        return self.__coutMana
    
class Creature(Carte):
    def __init__(self, srtNom, pv, atkScore):
            self.__srtNom=srtNom
            self.__pv=pv
            self.__atkScore=atkScore
    def getNomCrea (self):
          return self.__srtNom
    def getPvCrea (self):
          return self.__pv
    def getAtkCrea (self):
          return self.__atkScore


mage1 = Mage("Maître Gloutfou", 100, 30, 3, 0)

mage2 = Mage("Maître Gloutfraude", 130, 50, 3, 0)

tour = 0

while mage2.getpv<0 or mage1.getpv<0:
    #temps qu'aucuns mage est mort la partie continue
      tour+=1
      print(f"vous entamez le tour {tour}\n")
      print(f"{mage1.getNom} possède {mage1.getpv} pv et {mage1.getVmana} de mana/{mage1.getMmana}")
      print(f"{mage2.getNom} possède {mage2.getpv} pv et {mage2.getVmana} de mana/{mage2.getMmana}")
      #indique a chaque début de tours le tour actuel et le nombre de mana et de pv de chaque joueur

