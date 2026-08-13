import datetime

from models.compte import Compte
from models.personne import Personne
from models.solde_insuffisant_exception import SoldeInsuffisantException

class Epargne(Compte):
    def __init__(self, numero: str, titulaire: Personne, solde: float = 0, 
                 date_dernier_retait: datetime = None):
        super().__init__(numero, titulaire,solde)
        if date_dernier_retait is None:
             date_dernier_retait = datetime.datetime.now
        self.date_dernier_retait = date_dernier_retait

    def retrait(self, montant: float) -> None:
            if self.solde < montant:
                raise SoldeInsuffisantException(self.solde)
            super().retrait(montant)
            self.date_dernier_retait = datetime.datetime.now

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