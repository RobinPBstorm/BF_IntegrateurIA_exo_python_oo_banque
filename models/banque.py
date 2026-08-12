from compte import Compte
from compte_courant import Courant
from compte_epargne import Epargne
from personne import Personne

class Banque:
    def __init__(self, nom, comptes = dict()):
        self.nom = nom
        self.comptes = comptes

    def ajouter_compte(self, compte:Compte):
        if not isinstance(compte,Compte):
            print("Ce n'est pas un compte valide qe vous tentez d'ajouter à la banque!")
            return
        
        self.comptes[compte.numero] = compte

    # def __add__(self, other):
    #     self.ajouter_compte(other)

    def retirer_compte(self, compte):
        self.comptes.pop(compte.numero)

    def avoir_des_comptes(self, titulaire):
        total = 0
        for compte in self.comptes.values():
            if compte.titulaire == titulaire:
                total = compte + total
        return total

    
if __name__ == "__main__":
    titulaire1 = Personne("01", "Doe", "John")
    compte1 = Courant("BE01", titulaire1, 100, -50)
    compte2 = Courant("BE02", Personne("02", "Doe", "Jane"), 50)
    compte3 = Epargne("BE03", titulaire1, 250)

    banque = Banque("NeoBanque")
    try:
        banque.ajouter_compte("mon grand compte courant")
        banque.ajouter_compte(compte1)
        banque.ajouter_compte(compte2)
        banque.ajouter_compte(compte3)
    except Exception as exception:
        print(exception)

    print(banque.avoir_des_comptes(titulaire1))
    # for numero in banque.comptes:
    #     compte = banque.comptes[numero]
    #     print(f"{numero} : {compte.titulaire.nom}-{compte.titulaire.prenom} {compte.solde} €")