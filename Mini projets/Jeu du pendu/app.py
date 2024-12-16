import pyxel
from random import choice

pyxel.init(160, 100, title="Jeu du Pendu")

mots = ['ANGLE','ARMOIRE','BANC','BUREAU','CABINET','CARREAU','CHAISE','CLASSE',
        'CLEF','COIN','COULOIR','DOSSIER','EAU','ECOLE','ENTRER','ESCALIER','ETAGERE',
        'EXTERIEUR','FENETRE','INTERIEUR','LAVABO','LIT','MARCHE','MATELAS','MATERNELLE']

def tirage(tab : list) -> str:
    """Tire au sort un mot au hasard"""
    return choice(tab)        

mot = tirage(mots)
max_erreurs = 6
################ à compléter ##########################################
lettres_trouvees = ["_"]*len(mot)
lettres_ratees = []
game_over = False

def tab_to_string(tab : list, separateur : str) -> str :
    joined = ""
    for i in range(len(tab)):
        if i != len(tab) - 1:
            joined += tab[i] + separateur 
        else:
            joined += tab[i]
    return joined

def verifier_lettre(lettre : str, mot : str) :
    """
        Vérifie si la lettre fait partie du mot, 
        si oui, on remplace tout les occurences de la lettre dans lettres_trouvees[i] 
        si non, on ajoute la lettres à lettres_ratees, si elle n'y est pas.
    """
    lettre = lettre.upper()
    if lettre in mot:
        for i in range(len(mot)):
            if mot[i] == lettre:
                lettres_trouvees[i] = lettre
    else:
        if lettre not in lettres_ratees:
            lettres_ratees.append(lettre)

def affiche_erreurs() -> str :
    """Retourne le nombre d'erreurs de l'utilisateur"""
    return "Erreurs : " + str(len(lettres_ratees)) + "/" + str(max_erreurs)



################ fin de la zone à compléter ###########################
    
def update():
    if pyxel.btnp(pyxel.KEY_ESCAPE) or len(lettres_ratees) >= max_erreurs:
        pyxel.quit()
    # une boucle qui permet de tester toutes les touches de lettres possibles...
    for lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        touche = "KEY_" + lettre
        if pyxel.btnp(getattr(pyxel, touche)):
            verifier_lettre(lettre, mot)
def draw():
    pyxel.cls(0)
    if len(lettres_ratees) >= max_erreurs:
        pyxel.text(60, 50, "GAME OVER", 8)
    else:
        pyxel.text(10, 10, "Mot: " + tab_to_string(lettres_trouvees, ' '), 7)
        pyxel.text(10, 30, "Ratees: " + tab_to_string(lettres_ratees, ', '), 8)
        pyxel.text(10, 50, affiche_erreurs(), 8)
    


pyxel.run(update, draw)

