import tkinter as tk
fenetre = tk.Tk()
fenetre.title("Ma première application")
fenetre.geometry("600x400")

etiquette = tk.Label(fenetre, text = "Bonjour les amis !",
font = ("sans-serif", 30))
etiquette.pack()

btn = tk.Button(fenetre, text = "Clic !")
btn.pack()

entree = tk.Entry(fenetre)
entree.pack()

fenetre.mainloop()