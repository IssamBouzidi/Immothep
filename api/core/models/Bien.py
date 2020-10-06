from pydantic import BaseModel

class Bien:
    
    def __init__(self, metre_carre, nb_pieces, terrain, code_postal):
        self.metre_carre = metre_carre
        self.nb_pieces = nb_pieces
        self.terrain = terrain
        self.code_postal = code_postal
        self.estimation = 0

    def calcul_estimation(self):
        self.estimation = self.metre_carre + self.nb_pieces + self.terrain
        #return self.estimation