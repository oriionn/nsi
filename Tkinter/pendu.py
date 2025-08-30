from random import choice
import tkinter as tk

liste_de_mots = ['ANGLE','ARMOIRE','BANC','BUREAU','CABINET','CARREAU','CHAISE','CLASSE',
        'CLEF','COIN','COULOIR','DOSSIER','EAU','ECOLE','ENTRER','ESCALIER','ETAGERE',
        'EXTERIEUR','FENETRE','INTERIEUR','LAVABO','LIT','MARCHE','MATELAS','MATERNELLE']

def tirage(tab : list) -> str:
    """Tire au sort un mot au hasard"""
    return choice(tab)

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
    return "Erreurs : " + str(len(lettres_ratees)) + "/6"

mot = tirage(liste_de_mots)
lettres_trouvees = ["_"]*len(mot)
lettres_ratees = []

main = tk.Tk()
main.title("Pendu")
main.geometry("800x800")

error = tk.Label(main, text=" ".join(lettres_trouvees), font=('sans-serif', 30), justify='center')
error.grid(row=0, column=0)

main.mainloop()