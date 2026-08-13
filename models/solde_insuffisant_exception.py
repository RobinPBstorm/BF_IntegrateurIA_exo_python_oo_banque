class SoldeInsuffisantException(Exception):
    def __init__(self, solde):
        super().__init__(f"Solde de {solde} € est insuffisant pour l'opération")