from math import factorial


class calcul:
    def __init__(self, nombre):
        self.nombre=nombre
    def factorielle(self):
        return factorial(self.nombre)
    
mon_calcul=calcul(4)
print("Le facorielle de ce nombre est ", mon_calcul.factorielle())