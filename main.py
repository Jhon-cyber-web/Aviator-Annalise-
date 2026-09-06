import tkinter as tk
from tkinter import messagebox

def analyser():
    texte = entree.get().replace(",", " ")
    
    try:
        valeurs = [float(x) for x in texte.split() if float(x) > 0]
    except:
        messagebox.showerror("Erreur", "Ampidiro isa toy ny: 1.25 2.10 3.50")
        return

    if not valeurs:
        messagebox.showerror("Erreur", "Ampidiro résultats aloha.")
        return

    moyenne = sum(valeurs) / len(valeurs)
    maximum = max(valeurs)
    minimum = min(valeurs)

    if moyenne < 2:
        tendance = "Tendance basse"
    elif moyenne < 5:
        tendance = "Tendance moyenne"
    else:
        tendance = "Tendance haute"

    resultat.config(
        text=f"Résultats analysés : {len(valeurs)}\n"
             f"Moyenne : {moyenne:.2f}x\n"
             f"Minimum : {minimum:.2f}x\n"
             f"Maximum : {maximum:.2f}x\n\n"
             f"{tendance}"
    )

fenetre = tk.Tk()
fenetre.title("AVIATOR ANALYSE")
fenetre.geometry("400x500")

tk.Label(
    fenetre,
    text="AVIATOR ANALYSE",
    font=("Arial", 24, "bold")
).pack(pady=25)

tk.Label(
    fenetre,
    text="Ampidiro les résultats précédents :"
).pack()

entree = tk.Entry(fenetre, width=40)
entree.pack(pady=15)

tk.Button(
    fenetre,
    text="ANALYSER",
    font=("Arial", 16, "bold"),
    command=analyser
).pack(pady=15)

resultat = tk.Label(
    fenetre,
    text="Miandry analyse...",
    font=("Arial", 14),
    justify="left"
)
resultat.pack(pady=30)

fenetre.mainloop()
