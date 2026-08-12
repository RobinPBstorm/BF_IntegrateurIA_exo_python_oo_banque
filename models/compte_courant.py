from compte import Compte
from personne import Personne

class Courant(Compte):
    def __init__(self, numero: str, titulaire: Personne, ligne_de_credit: float,solde: float = 0):
        super().__init__(numero, titulaire,solde)
        self.ligne_de_credit = ligne_de_credit

    def retrait(self, montant: float) -> None:
        if self.solde - montant < - self.ligne_de_credit:
            print("Limite dépassé")
        else:
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