# billetterie.py — Module de billetterie FestiApp

# ============================================
# CONFIGURATION
# ============================================
MAX_CAPACITE = 3
billets_vendus = 0

EVENEMENT = {
    "nom": "FestiYaoundé 2026",
    "lieu": "Palais des Sports",
    "categories": {
        "VIP": 25000,
        "Premium": 15000,
        "Standard": 5000,
        "Early Bird": 3000,
    }
}

# ============================================
# 1. GÉNÉRATEUR DE NUMÉROS DE BILLETS (closure)
# ============================================
# À TOI — crée une closure qui génère :
# FEST-0001, FEST-0002, FEST-0003...
def generateur_billet():
    compteur = 0
    def numero_billet():
        nonlocal compteur
        compteur += 1
        return f"FEST-{compteur:04d}"
    return numero_billet

# ============================================
# 2. CAISSE PAR CATÉGORIE (closure)
# ============================================
# À TOI — crée une closure qui mémorise
# le total des ventes par catégorie
def caisse(categorie):
    total_ventes = 0
    def informations(prix):
        nonlocal total_ventes
        total_ventes += prix
        if prix == 0:
            return f"Caisse {categorie} - Total : {total_ventes:,} FCFA"
        return f"Categorie : {categorie} | Prix de vente : {prix:,} | Total des ventes : {total_ventes:,} FCFA"
    return informations

# ============================================
# 3. DÉCORATEUR DE CAPACITÉ
# ============================================
# À TOI — décore les ventes pour bloquer
# quand MAX_CAPACITE est atteinte
def verifier_capacite(fonction):
    def verification(*args):
        global billets_vendus
        print("Verfification d'une place disponible ...")
        if billets_vendus >= MAX_CAPACITE:
            print("Desole - Aucune place n'est disponible")
            return
        print("Place disponible")
        print("Billet Vendu")
        resultat = fonction(*args)
        billets_vendus += 1
        return resultat
    return verification

# ============================================
# 4. AFFICHAGE DU PROGRAMME (**kwargs)
# ============================================
# À TOI — fonction qui affiche les détails
# de l'événement depuis un dictionnaire
def afficher_evenement(details):
    print("Information sur l'evenement :")
    for cle, valeur in details.items():
        print(f"- {cle} : {valeur}")

# ============================================
# 5. FONCTION DE VENTE PRINCIPALE
# ============================================
# À TOI — décore cette fonction avec
# @verifier_capacite et utilise :
# - le générateur de numéros
# - la caisse de la bonne catégorie
# - l'affichage du billet en format propre

# ====================================================
# LISTE DES VARIABLES GLOBALES DE CAISSES DISPONIBLES
# ====================================================
caisse_vip = caisse("VIP")
caisse_premium = caisse("Premium")
caisse_standard = caisse("Standard")
caisse_early_bird  = caisse("Early Bird")

# ===========================================
# VARIABLE DE GENERATION DE NUMERO DE BILLET
# ===========================================
numero_billet = generateur_billet()

@verifier_capacite
def vendre_billet(nom, categorie, prix):

    if categorie == "VIP":
       print(caisse_vip(prix))
    elif categorie == "Premium":
        print(caisse_premium(prix))
    elif categorie == "Standard":
        print(caisse_standard(prix))
    elif categorie == "Early Bird":
        print(caisse_early_bird(prix))

    # Affichage conforme du billet
    print(f"""
    ---------- Information sur le billet vendu ----------
        
        Nom du proprietaire : {nom}
        Numero de billet    : {numero_billet()}
        Categorie du billet : {categorie}
        Prix du billet      : {prix:,}

    """)

# ============================================
# 6. TEST DU SYSTÈME COMPLET
# ============================================
if __name__ == "__main__":
    # Afficher le programme de l'événement
    print()
    afficher_evenement(EVENEMENT)
    print()
    # Vendre 3 billets de catégories différentes
    vendre_billet("Pierre", "VIP", 25000)
    vendre_billet("Jean", "VIP", 5000)
    vendre_billet("Peter", "Early Bird", 3000)
    # Afficher le total des ventes par catégorie
    print(f"""
    ----------- Bilan des ventes -----------
    - {caisse_vip(0)}
    - {caisse_premium(0)}
    - {caisse_standard(0)}
    - {caisse_early_bird(0)}
    """)
    # Essayer de vendre quand c'est complet
    print()
    vendre_billet("Manuel", "VIP", 25000)
    print()
    pass