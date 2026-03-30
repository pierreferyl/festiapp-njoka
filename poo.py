# Classe parent - ce qui est commun a tous les billets
class Billet:
    # Compteur partage par TOUS les billets
    nombre_billets_crees = 0

    def __init__(self, nom, categorie, prix):
        Billet.nombre_billets_crees += 1
        self.numero = Billet.nombre_billets_crees
        self.proprietaire = nom
        self.categorie = categorie
        self.prix = prix
        self.valide = True

    # @classmethod - connait la classe, pas l'objet
    @classmethod
    def creer_vip(cls, nom):
        return cls(nom, "VIP", 25000)
    
    @classmethod
    def creer_standard(cls, nom):
        return cls(nom, "Standard", 5000)
    
    # @staticmethod - utilitaire pur, pas besion de self ni cls
    @staticmethod
    def categorie_valide(categorie):
        categories = ["VIP", "Premium", "Standard", "Early Bird"]
        return categorie in categories
    
    # @propety - attribut calcule, appele sans parentheses
    @property
    def status(self):
        if self.valide:
            return "Valide"
        return "invalide"
    
    @property
    def prix_avec_frais(self):
        return self.prix * 1.05 # 5% de frais de service
    
    def __str__(self):
        return f"Billet FEST-{self.numero:04d} - {self.proprietaire} - {self.categorie} - {self.status}"

    def afficher(self):
        print(f"""
    Numero       : FEST-{self.numero:04d}
    Proprietaire : {self.proprietaire}
    Categorie    : {self.categorie}
    Prix         : {self.prix:,} FCFA
    Valide       : {self.valide}
        """)

    def invalider(self):
        self.valide = False
        print(f"Billet FEST-{self.numero:04d} invalide")

    """ def __str__(self):
        return f"Billet FEST-{self.numero:04d} - {self.proprietaire} - {self.categorie}" """
    
    def __repr__(self):
        return f"Billet(numero={self.numero}, proprietaire='{self.proprietaire}')"
    
    def __len__(self):
        return self.prix
    

# Test
billet1 = Billet.creer_vip("Pierre")    # @classmethod
billet2 = Billet.creer_standard("Jean") # @classmethod
billet3 = Billet("Alice", "Premium", 15000)

print(billet1)
print(billet2)
print(billet3)

print(f"\nBillet crees :")
            
# Classe enfant - herite de tout Billet + ajoute ses propres attributs
class BilletVIP(Billet):
    def __init__(self, nom, numero, prix):
        super().__init__(nom, numero, "VIP", prix) # appelle __init__ du parent
        self.acces_backstage = True
        self.repas_inclus = True

    def afficher_avantages(self):
        print(f"""
    Avantage VIP :
    - Acces backstage : {self.acces_backstage}
    - Repas inclus    : {self.repas_inclus}    
        """)

# Classe enfant - herite de tout Billet + acces simple
class BilletStandard(Billet):
    def __init__(self, nom, numero, prix):
        super().__init__(nom, numero, "Standard", prix)
        self.acces_backstage = False

""" # Test
billet_vip = BilletVIP("Pierre", 1, 25000)
billet_std = BilletStandard("Jean", 2, 5000)

billet_vip.afficher()           # methode heritee du parent
billet_vip.afficher_avantages() # methode propre a BilletVIP
billet_std.afficher()           # methode heritee du parent
billet_vip.invalider()          # methode heritee du parent
billet_vip.afficher()           # valide devient False

# Creer deux billets
billet1 = Billet("Pierre", 1,"VIP", 25000)
billet2 = Billet("Jean", 2, "Standard", 5000)

print(billet1)          # utilise __str__
print(repr(billet1))    # utilise __repr__
print(len(billet1))     # utilise __len__

billet1.afficher()
billet2.afficher() """

class Evenement:

    def __init__(self, nom, lieu, capacite_max):
        self.nom = nom
        self.lieu = lieu
        self.capacite_max = capacite_max
        self.billets = []

    def ajouter_billet(self, billet):
        if len(self.billets) >= self.capacite_max:
            print("Evenement complet")
            return
        self.billets.append(billet)
    
    def afficher_billets(self):
        print(f"------ Billets : {self.nom} --------")
        for numero, billet in enumerate(self.billets, start = 1):
            print(f"{numero}.")
            billet.afficher()

    def places_restantes(self):
        return self.capacite_max - len(self.billets)
    
""" festival = Evenement("FestiYaoundé 2026", "Palais des Sports", 3)
festival.ajouter_billet(billet1)
festival.ajouter_billet(billet2)
festival.ajouter_billet(billet2)
festival.ajouter_billet(billet2)
festival.afficher_billets()
print(f"Places restantes : {festival.places_restantes()}") """