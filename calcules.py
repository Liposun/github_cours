from math import factorial


class calcul:
    def __init__(self, nombre):
        self.nombre=nombre
    def factorielle(self):
        return factorial(self.nombre)
def listDiviseur(self):
        liste=[]
        for i in range(1, self.nombre+1):
            if self.nombre%i==0:
                liste.append(i)
        return liste
    
mon_calcul=calcul(4)
print("Le facorielle de ce nombre est ", mon_calcul.factorielle())