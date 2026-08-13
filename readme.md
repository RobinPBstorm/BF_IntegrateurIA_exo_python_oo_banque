# Exercice 1

## Créer des Personnes

Attributs:
 - id 
 - nom
 - prenom
 
## Créer de comptes courants

Attributs:
 - numero
 - titulaire: Personne
 - solde

Ajoutez, un constructeur prenant en paramètre : 
 - Le numéro
 - le titulaire 
 - le solde

Comportement:
 - Retrait(somme)
 - Depot(somme)
  
Contrainte:
 - Pas de retrait de somme négative
 - Pas de dépot de somme négative
 - Retrait ne doit amener à un solde négatif

## Exercice 2

1. Surcharger l’opérateur « + » de la classe « Courant » afin qu’il retourne la somme, de type float, des soldes. Cependant, les soldes négatifs ne doivent pas être pris en compte. 

2. Créer une classe « Banque ».

    Attributs:
     - nom
     - comptes: dict<numero, Courant>

3. Ajouter une méthode « AvoirDesComptes » à la classe « Banque » recevant en paramètre le titulaire (Personne) qui calculera les avoirs de tous ses comptes en utilisant l’opérateur « + ».

# Exercice 3

1. Créer une classe « Epargne » permettant la gestion d’un carnet d’épargne qui devra implémenter :
	- Les propriétés publiques : 
		-  Numéro (string) 
		- Solde (float) - Lecture seule 
		- DateDernierRetrait (DateTime) - représentant la date du dernier retrait sur le carnet
		- Titulaire (Personne)
	- Les méthodes publiques : 
		- void Retrait(float Montant)
		- void Depot(float Montant) 

2.  Ajouter à la classe « Courant »:
	- La propriété publique : 
		- Ligne de crédit - représentant la limite négative du compte strictement supérieur ou égale à 0
		
	- Et modifier les méthodes pour intégrer cette nouvelle limite négative du solde 


3. Créer une classe « Compte » avec tous les éléments communs à « Courant » et « Épargne »

4. Si nous ajoutions la « ligne_de_credit » dans « Compte », définir sur papier les modifications qu’il faudrait apporter à nos classes.

# Exercice 4

Dans la classe « Compte » : 
1. Au niveau de la méthode « Depot » et « Retrait », déclenchez une exception de type « ValueError » si le montant n’est pas supérieur à 0 (zéro). 

2. Faites de même au niveau de la méthode « Retrait » et y ajouter le déclenchement d’une exception de type « SoldeInsuffisantException » si le montant ne peut être retiré. 

Au niveau de la classe « Courant » : 
1. Au niveau de la propriété « LigneDeCredit », déclenchez une exception de type « ValueError » si la valeur n’est pas supérieur ou égale à 0 (zéro).

# Exercice 5

1. Définir la classe « Compte » comme étant abstraite. 

2. Ajouter une méthode à la classe « Compte » appelée « CalculInteret »  en sachant que pour un livret d’épargne le taux est toujours de 4.5% tandis que pour le compte courant si le solde est positif le taux sera de 3% sinon de 9.75%. 

3. Ajouter une méthode à la classe « Compte » appelée «AppliquerInteret » qui additionnera le solde avec le retour de la méthode « CalculInteret ».