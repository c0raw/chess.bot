import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
from ui_game import ChessGUI
from engine.ai import AI_BY_NAME

class MainMenu:
    def __init__(self, root):
        self.root = root
        root.title("Menu - Jeu d'échecs (Terminale NSI)")
        self.frame = tk.Frame(root, padx=30, pady=30)
        self.frame.pack()
        tk.Label(self.frame, text="♔ Jeu d'Échecs ♚", font=("Helvetica",20,"bold")).pack(pady=10)
        tk.Button(self.frame, text="Joueur vs Joueur", width=20, command=self.start_pvp).pack(pady=6)
        tk.Button(self.frame, text="Joueur vs IA", width=20, command=self.start_pvai).pack(pady=6)
        tk.Button(self.frame, text="Quitter", width=20, command=root.quit).pack(pady=12)

    def start_pvp(self):
        self.frame.destroy()
        minutes = simpledialog.askinteger("Temps imparti", "Minutes par joueur (0 = illimité)", minvalue=0, initialvalue=10)
        total_time = minutes * 60 if minutes and minutes > 0 else None
        from ui_game import ChessGUI
        ChessGUI(self.root, vs_ai=False, total_time=total_time)

    def start_pvai(self):
        # Création d'une petite fenêtre de sélection
        win = tk.Toplevel(self.root)
        win.title("Choix de la difficulté IA")
        win.grab_set()  # Rend la fenêtre modale

        tk.Label(win, text="Sélectionne la difficulté de l'IA :", 
                font=("Helvetica", 12)).pack(pady=10)

        # Menu déroulant
        levels = list(AI_BY_NAME.keys())
        difficulty_var = tk.StringVar(value=levels[0])

        combo = ttk.Combobox(win, values=levels, textvariable=difficulty_var, state="readonly")
        combo.pack(pady=5)

        # Temps par joueur
        tk.Label(win, text="Minutes par joueur (0 = illimité) :", font=("Helvetica", 11)).pack(pady=10)
        time_var = tk.IntVar(value=10)
        tk.Entry(win, textvariable=time_var).pack(pady=5)

        def validate():
            level = difficulty_var.get()
            minutes = time_var.get()

            total_time = minutes * 60 if minutes > 0 else None

            win.destroy()
            self.frame.destroy()

            ChessGUI(self.root, vs_ai=True, ai_level=level, total_time=total_time)

        def cancel():
            win.destroy()

        btn_frame = tk.Frame(win)
        btn_frame.pack(pady=15)

        tk.Button(btn_frame, text="Annuler", width=12, command=cancel).grid(row=0, column=0, padx=6)
        tk.Button(btn_frame, text="Valider", width=12, command=validate).grid(row=0, column=1, padx=6)


if __name__ == "__main__":
    root = tk.Tk()
    MainMenu(root)
    root.resizable(False, False)
    root.mainloop()