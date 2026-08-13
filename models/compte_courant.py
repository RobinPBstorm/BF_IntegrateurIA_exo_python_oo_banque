from models.solde_insuffisant_exception import SoldeInsuffisantException

from models.compte import Compte
from models.personne import Personne

class Courant(Compte):
    def __init__(self, numero: str, titulaire: Personne, ligne_de_credit: float,solde: float = 0):
        super().__init__(numero, titulaire,solde)
        self.__ligne_de_credit = 0
        try:
            self.ligne_de_credit = ligne_de_credit
        except ValueError as error:
            print(error)

    #getter
    @property
    def ligne_de_credit(self):
        return self.__ligne_de_credit

    #setter
    @ligne_de_credit.setter
    def ligne_de_credit(self, valeur):
        if valeur < 0:
            raise ValueError("La ligne de crédit ne peut être négative")
        self.__ligne_de_credit = valeur

    def retrait(self, montant: float) -> None:
        if self.solde - montant < - self.ligne_de_credit:
            raise SoldeInsuffisantException(self.solde)
        super().retrait(montant)


    def __str__(self):
        return f"Le compte courant {self.numero} possédé par {self.titulaire.prenom} avec {self.solde} €"
        

if __name__ == "__main__":
    john_doe = Personne(1, "Doe", "John")
    courant = Courant("BE01", john_doe, 100)
    print(courant)

    courant.retrait(150)
    print(courant)
    courant.depot(50)
    print(courant)
    print(courant + 50)
    print(courant)