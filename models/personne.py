class Personne:
    def __init__(self, id: int, nom: str, prenom: str):
        self.id = id
        self.nom = nom
        self.prenom = prenom

    def nom_comlet2(self):
        return f"{self.prenom} {self.nom}"

    @property
    def nom_complet(self):
        return f"{self.prenom} {self.nom}"

if __name__ == "__main__":
    john_doe = Personne(1, "Doe", "John")
    print(john_doe.prenom)
    print(john_doe.nom_complet)
    # n'est pas possible car pas de setter
    #john_doe.nom_complet = "Jane Doe"
    print(john_doe.nom_comlet2())