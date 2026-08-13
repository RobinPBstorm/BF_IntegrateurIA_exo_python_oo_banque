from models.personne import Personne
from models.compte_courant import Courant
from models.compte_epargne import Epargne
from models.solde_insuffisant_exception import SoldeInsuffisantException

john_doe = Personne(1, "Doe", "John")
courant = Courant("BE01", john_doe, 100,0)
print(courant)

try:
    courant.retrait(50)
except ValueError as error:
    print(error)
except SoldeInsuffisantException as exception:
    print(exception)
print(courant)


try:
    courant.depot(-50)
except ValueError as error:
    print(error)
print(courant)

epargne = Epargne("BE02", john_doe, 100)
print(epargne)

try:
    epargne.retrait(150)
except ValueError as error:
    print(error)
except SoldeInsuffisantException as exception:
    print(exception)
print(epargne)

try:
    epargne.depot(50)
except ValueError as error:
    print(error)
print(epargne)