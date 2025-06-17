import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import os

tulemused_file = 'tulemused.txt'


def loe_kaart():
    """Return a random card value between 2 and 11 inclusive."""
    return random.randint(2, 11)

    # Tulemused
def arvuta_tulemus(player_sum, comp_sum):
    """Determine outcome: 'Võit' if player wins, 'Kaotus' if loses."""
    if player_sum > 21:
        return 'Kaotus'
    if comp_sum > 21:
        return 'Võit'
    if abs(21 - player_sum) < abs(21 - comp_sum):
        return 'Võit'
    else:
        return 'Kaotus'


def salvesta_tulemus(name, result, summa):
    """Append game result to file."""
    with open(tulemused_file, 'a', encoding='utf-8') as f:
        f.write(f"{name},{result},{summa}\n")


def näita_ajalugu(root):
    """Display game history in a new window."""
    if not os.path.exists(tulemused_file):
        messagebox.showinfo('Ajalugu', 'Ühtegi tulemust ei leitud.')
        return
    history = tk.Toplevel(root)
    history.title('Mängu ajalugu')
    text = tk.Text(history, width=50, height=20)
    text.pack(fill='both', expand=True)
    with open(tulemused_file, 'r', encoding='utf-8') as f:
        for line in f:
            name, result, summa = line.strip().split(',')
            text.insert('end', f"{name}: {result}, {summa} punkti\n")
    text.config(state='disabled')


def mängi_arvuti():
    """Computer draws cards until sum >=17."""
    sum_comp = 0
    while sum_comp < 17:
        sum_comp += loe_kaart()
    return sum_comp


class Game21App:
    def __init__(self, root):
        self.root = root
        root.title('Mäng 21')
        # Nimi
        tk.Label(root, text='Mängija nimi:').pack(padx=10, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.pack(padx=10)
        # Ekraan
        self.status = tk.Label(root, text='', font=('Arial', 14))
        self.status.pack(pady=10)
        # Nuppud
        frame = tk.Frame(root)
        frame.pack(pady=5)
        self.start_btn = tk.Button(frame, text='Alusta mängu', command=self.start_game)
        self.start_btn.grid(row=0, column=0, padx=5)
        self.draw_btn = tk.Button(frame, text='Võta kaart', command=self.draw_card, state='disabled')
        self.draw_btn.grid(row=0, column=1, padx=5)
        self.stop_btn = tk.Button(frame, text='Peatu', command=self.stop_game, state='disabled')
        self.stop_btn.grid(row=0, column=2, padx=5)
        self.history_btn = tk.Button(frame, text='Vaata ajalugu', command=lambda: näita_ajalugu(self.root))
        self.history_btn.grid(row=0, column=3, padx=5)
        # Holds
        self.player_sum = 0
        self.player_cards = []

    def start_game(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning('Viga', 'Sisesta mängija nimi!')
            return
        # reset
        self.player_cards = []
        self.player_sum = 0
        # initial two cards
        for _ in range(2):
            self.player_sum += loe_kaart()
        self.update_status()
        self.draw_btn.config(state='normal')
        self.stop_btn.config(state='normal')
        self.start_btn.config(state='disabled')

    def draw_card(self):
        self.player_sum += loe_kaart()
        self.update_status()
        if self.player_sum > 21:
            self.end_game('Kaotus')

    def stop_game(self):
        comp_sum = mängi_arvuti()
        result = arvuta_tulemus(self.player_sum, comp_sum)
        self.end_game(result, comp_sum)

    def update_status(self):
        self.status.config(text=f'Summa: {self.player_sum}')
        # Lopp
    def end_game(self, result, comp_sum=None):
        name = self.name_entry.get().strip()
        msg = f'Oma summa: {self.player_sum}'
        if comp_sum is not None:
            msg += f', Arvuti summa: {comp_sum}'
        msg += f'\nTulemus: {result}'
        messagebox.showinfo('Mäng lõppenud', msg)
        salvesta_tulemus(name, result, self.player_sum)

        self.draw_btn.config(state='disabled')
        self.stop_btn.config(state='disabled')
        self.start_btn.config(state='normal')

if __name__ == '__main__':
    root = tk.Tk()
    app = Game21App(root)
    root.mainloop()
