from compte import Compte
from personne import Personne


class Epargne(Compte):
    def __init__(self, numero: str, titulaire: Personne, solde: float = 0):
        super().__init__(numero, titulaire,solde)

    def retrait(self, montant: float) -> None:
            if self.solde < montant:
                print("Solde insffisant")
            else:
                super().retrait(montant)

    def __str__(self):
        return f"Le compte épargne {self.numero} possédé par {self.titulaire.prenom} avec {self.solde} €"
        

if __name__ == "__main__":
    john_doe = Personne(1, "Doe", "John")
    epargne = Epargne("BE01", john_doe, 100)
    print(epargne)

    epargne.retrait(150)
    print(epargne)
    epargne.depot(50)
    print(epargne)
    print(epargne + 50)
    print(epargne)