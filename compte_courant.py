from personne import Personne

class Courant:
    def __init__(self, numero: str, titulaire: Personne, solde: float = 0):
        self.numero = numero
        self.titulaire = titulaire
        self.solde = solde

    def retrait(self, montant: float) -> None:
        if montant <= 0:
            print("Montant invalide")
        elif self.solde < montant:
            print("Solde insffisant")
        else:
            self.solde -= montant

    def depot(self, montant: float) -> None:
        if montant <= 0:
            print("Montant invalide")
        else:
            self.solde += montant

    # Courant(self) + other
    def __add__(self, other):
        if self.solde < 0:
            return other
        return self.solde + other

    def __str__(self):
        return f"Le compte courant {self.numero} possédé par {self.titulaire.prenom} avec {self.solde} €"
        

if __name__ == "__main__":
    john_doe = Personne(1, "Doe", "John")
    courant = Courant("BE01", john_doe, 100)
    print(courant)

    courant.retrait(25)
    print(courant)
    courant.depot(50)
    print(courant)
    print(courant + 50)
    print(courant)