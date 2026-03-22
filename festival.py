# festival.py - jour 1 : fonctions avancees
print("")

# fonction classique - parametres fixes
def creer_evenement(nom, date):
    return f"Evenement : {nom} le {date}"

# *args - plusieurs artistes d'un coup
def ajouter_artistes(*artistes):
    print(f"{len(artistes)} artiste(s) ajoute(s) :")
    for artiste in artistes:
        print(f" - {artiste}")

ajouter_artistes("Locko", "Charlotte Dipanda", "Tenor")

# **kwargs - details flexibles d'un evenement
def afficher_evenement(**details):
    print("\nFiche evenement :")
    for cle, valeur in details.items():
        print(f" {cle} : {valeur}")

afficher_evenement(
    nom="Kmer Otaku Festival 2026",
    lieu="Musee National",
    capacite=5000,
    prix_billet="2000 FCFA",
    date="12/06/26"
)

afficher_evenement(
    nom="Yafe",
    lieu="Palais des Congres",
    capacite=100000,
    prix_billet="500 FCFA",
    date="22/12/26"
)

# Tri des categories de billets par prix
billets = [
    {"categorie" : "VIP", "prix": 25000},
    {"categorie" : "Standard", "prix": 5000},
    {"categorie" : "Early Bird", "prix": 3000},
    {"categorie" : "Premium", "prix": 15000},
]

# Trier du moins cher au plus cher
billets_tries = sorted(billets, key=lambda b: b["prix"])

print("\nBillets du moins cher au plus cher :")
for billet in billets_tries:
    print(f" {billet['categorie']} : {billet['prix']} FCFA")

# Trier du plus cher au moins cher
billets_tries_desc = sorted(billets, key=lambda b: b["prix"], reverse=True)

print("\nBillets du plus cher au moins cher :")
for billet in billets_tries_desc:
    print(f" {billet['categorie']} : {billet['prix']} FCFA")

# Trier par nom de categorie
billets_tries_nom = sorted(billets, key= lambda b: b['categorie'])
print("\n Trier a partir du nom des categories")

for billet in billets_tries_nom:
    print(f" {billet['categorie']} : {billet['prix']} FCFA")

# Creer les billets
def creer_billet(**infos_acheteur):
    print(f""" 
    ------ Confirmation d'achat ------
    Nom       : {infos_acheteur['nom']}
    Email     : {infos_acheteur['email']}
    Categorie : {infos_acheteur['categorie']}
    """)

creer_billet (
    nom="Feryl",
    email="pierreferyl@gmail.com",
    categorie="V-VIP"
)

def creer_guichet(): # fonction exterieure - cree le guichet
    compteur = 0     # la memoire du guichet 

    def vendre_billet(): # fonction interieure - l'action du guichetier
        nonlocal compteur # "Je vais modifier la memoire du guichet"
        compteur += 1
        return f"Billet-{compteur:03d}" #001, 002, 003...
    
    return vendre_billet # On retourne le guichetier, pas le resultat

# Creer un guichet 
kmer_otaku_festival = creer_guichet()
yafe = creer_guichet()

# Vendre des billets du guichet 0
print(kmer_otaku_festival()) # Billet-001

# vendre des billets du guichet 1
print(yafe()) # Billet-001

# Compter le nombre d'entrees validee
def creer_compteur_entree(porte):
    compteur = 0

    def compte_entree():
        nonlocal compteur
        compteur += 1
        return f"Porte {porte} - {compteur} entrees validees"
    
    return compte_entree

porte_a = creer_compteur_entree("A")

print(porte_a())
print(porte_a())
print(porte_a())
print(porte_a())

liste_noire = ["Jean-Pierre", "Marcel"]

# Le decorateur - le videur
def verifier_billet(fonction):
    def videur(*args, **kwargs):
        nom = args[0] # recupere le premier argument
        if nom in liste_noire:
            print(f"{nom} - acces refuses.")
            return # stoppe ici, n'appelle pas la fonction
        print("Verification OK ...")
        resultat = fonction(*args, **kwargs)
        print("Entree enregistree.")
        return resultat
    return videur

# La fonction decoree - l'entree VIP
@verifier_billet
def entrer_vip(nom):
    print(f"{nom} entre dans la zone VIP.")

# Test
entrer_vip("Locko")
entrer_vip("Jean-Pierre")
entrer_vip("Charlotte")

# afficher le programme 
def affircher_programme(*evenements):
    print("Programme du festival :")
    for numero, evenement in enumerate(evenements, start=1):
        print(f"  {numero:02d}. {evenement}")
    
#Test
liste_programme = [
    "Concert Locko - Scene principale",
    "DJ Set Charlotte - scene secondaire",
    "Stand-up Marcel - Chapiteau"
 ]

affircher_programme("Concert Locko - Scene principale","DJ Set Charlotte - scene secondaire","Stand-up Marcel - Chapiteau")

# creer les caisses
def creer_caisse(categorie):
    total_vente = 0

    def vendre(prix):
        nonlocal total_vente
        total_vente += prix
        return f"Caisse {categorie} - vente enregistree : {prix:,} | Total : {total_vente:,} FCFA"
    return vendre

#Test
caisse_vip = creer_caisse("VIP")
caisse_standard = creer_caisse("Standard")

print(caisse_vip(25000))
print(caisse_vip(25000))
print(caisse_vip(25000))
print(caisse_vip(25000))
print(caisse_standard(5000))

MAX_PLACE = 3
billets_vendus = 0

# decorateur @verifier_capacite
def verifier_capacite(fonction):
    def verificateur(*args):
        global billets_vendus
        print("Verification du nombre de place disponible ...")
        if billets_vendus >= MAX_PLACE:
            print("Desole - evenement complet.")
            return
        print("Billet disponible")
        resultat = fonction(*args)
        billets_vendus += 1
        print(f"Places restantes : {MAX_PLACE - billets_vendus}")
        return resultat
    return verificateur


@verifier_capacite
def vendre_billet(nom, categorie):
    print(f"Billet vendu a {nom} - categorie {categorie}")

#Test

vendre_billet("locko", "VIP")
vendre_billet("locko", "VIP")
vendre_billet("locko", "VIP")
vendre_billet("locko", "VIP")

billets = [
    {"nom": "Alice", "categorie": "VIP", "prix": 25000},
    {"nom": "Bob", "categorie": "Standard", "prix": 5000},
    {"nom": "Claire", "categorie": "Early Bird", "prix": 3000},
    {"nom": "David", "categorie": "Premium", "prix": 15000},
    {"nom": "Eve", "categorie": "VIP", "prix": 25000},
]

# Afficher la liste du plus cher au moins cher

billets_trier = sorted(billets, key= lambda b : b["prix"], reverse=True)
print("------- Liste trier du plus cher au moins cher ------")
for numero, billet in enumerate(billets_trier, start=1):
    print(f"""
    {numero:02d}. Nom         : {billet['nom']}
        Categorie   : {billet['categorie']}
        Prix        : {billet['prix']:,}
    """)

billet_plus_cher = max(billets, key= lambda b : b['prix'])
print(f"Plus cher : {billet_plus_cher['nom']} — {billet_plus_cher['categorie']} — {billet_plus_cher['prix']:,} FCFA")

billet_moins_cher = min(billets, key= lambda b : b['prix'])
print(f"Moins cher : {billet_moins_cher['nom']} — {billet_moins_cher['categorie']} — {billet_moins_cher['prix']:,} FCFA")

print()