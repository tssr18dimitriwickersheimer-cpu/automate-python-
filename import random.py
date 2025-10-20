import random
import string

def generer_code_aleatoire(longueur=10):
    """
    Génère une chaîne de caractères aléatoire (combinaison de lettres
    minuscules, majuscules et de chiffres) de la longueur spécifiée.
    """
    # Définit l'ensemble des caractères possibles
    caracteres = string.ascii_letters + string.digits
    
    # Choisit des caractères au hasard pour construire le code
    code_aleatoire = ''.join(random.choice(caracteres) for i in range(longueur))
    
    return code_aleatoire

# --- Démo ---

# Longueur souhaitée pour le code
longueur_code = 12

# Génération et affichage du code
code_demo = generer_code_aleatoire(longueur_code)

print(f"Longueur du code : {longueur_code}")
print(f"Code aléatoire généré : {code_demo}")