import tkinter as tk
import tkinter.simpledialog
from Swiat import Swiat
from Organizm import Kierunek
from Komentator import Komentator
from tkinter import font

class GUI:

    class Oznaczenia(tk.Frame):
        def __init__(self, main_panel):
            super().__init__(main_panel, bg="#08a999", width=100,
                             height=600, relief=tk.RAISED, bd=10)

            self.labels = []
            self.create_legend_labels()

            for label in self.labels:
                label.pack(pady=5)

        def create_legend_labels(self):
            self.labels.append(tk.Label(self, text="Legenda", font=("Arial", 14, "bold"), bg="#08a999"))
            self.labels.append(tk.Label(self, text="Barszcz Sosnowskiego", bg="purple"))
            self.labels.append(tk.Label(self, text="Guarana", bg="#808000"))
            self.labels.append(tk.Label(self, text="Mlecz", bg="gold"))
            self.labels.append(tk.Label(self, text="Trawa", bg="#00ff00"))
            self.labels.append(tk.Label(self, text="Wilcze jagody", bg="dark red"))
            self.labels.append(tk.Label(self, text="Antylopa", bg="dark cyan"))
            self.labels.append(tk.Label(self, text="Czlowiek", bg="blue"))
            self.labels.append(tk.Label(self, text="Lis", bg="orange"))
            self.labels.append(tk.Label(self, text="Owca", bg="saddle brown"))
            self.labels.append(tk.Label(self, text="Wilk", bg="turquoise"))
            self.labels.append(tk.Label(self, text="Zolw", bg="dark green"))
            self.labels.append(tk.Label(self, text="Cyber owca", bg="black"))
    class KomentarzeLayout(tk.Frame):
        def __init__(self, main_panel, grafika_planszy):
            super().__init__(main_panel, bg="gray", width=300,
                             height=600, relief=tk.RAISED, bd=16)
            self.grafika_planszy = grafika_planszy

            self.tekst = ""
            self.instruction = "Autor: Hubert Szymczak\n"

            self.text_area = tk.Text(self, bg="gray", fg="white")
            self.text_area.configure(state='disabled')
            self.text_area.tag_configure("center", justify='center')
            self.text_area.insert(tk.END, self.instruction)
            self.text_area.insert(tk.END, self.tekst)
            self.text_area.tag_add("center", "1.0", "end")
            self.text_area.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

        def odswiezKomentarze(self):
            self.tekst = self.instruction + Komentator.getTekst()
            self.text_area.configure(state='normal')
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, self.tekst)
            self.text_area.tag_add("center", "1.0", "end")
            self.text_area.configure(state='disabled')
    def __init__(self, title):
        def on_enter(event):
            event.widget.config(bg="#03544c")  # Zmiana koloru tła na najechanie myszą

        def on_leave(event):
            event.widget.config(bg="#08a999")
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("1300x700")
        self.root.configure(bg="gray")
        button_frame = tk.Frame(self.root, bg="gray")
        button_frame.pack(side=tk.TOP, fill=tk.X)
        font_style = font.Font(family="Helvetica", weight="bold")
        new_game_button = tk.Button(button_frame, bg="#08a999", text="Nowa gra", command=self.show_dimensions_window,
                                    width=20, height=3, font=font_style, relief=tk.RAISED, bd=10)
        new_game_button.pack(side=tk.LEFT)
        new_game_button.bind("<Enter>", on_enter)  # Powiązanie zdarzenia "<Enter>" z funkcją on_enter
        new_game_button.bind("<Leave>", on_leave)
        load_button = tk.Button(button_frame,bg="#08a999", text="Wczytaj", command=self.load,width=20, height=3, font=font_style, relief=tk.RAISED, bd=10)
        load_button.pack(side=tk.LEFT)
        load_button.bind("<Enter>", on_enter)  # Powiązanie zdarzenia "<Enter>" z funkcją on_enter
        load_button.bind("<Leave>", on_leave)
        save_button = tk.Button(button_frame,bg="#08a999", text="Zapisz", command=self.save,width=20, height=3, font=font_style, relief=tk.RAISED, bd=10)
        save_button.pack(side=tk.LEFT)
        save_button.bind("<Enter>", on_enter)  # Powiązanie zdarzenia "<Enter>" z funkcją on_enter
        save_button.bind("<Leave>", on_leave)

        exit_button = tk.Button(button_frame,bg="#08a999", text="Wyjscie", command=self.exit,width=20, height=3, font=font_style, relief=tk.RAISED, bd=10)
        exit_button.pack(side=tk.LEFT)
        exit_button.bind("<Enter>", on_enter)  # Powiązanie zdarzenia "<Enter>" z funkcją on_enter
        exit_button.bind("<Leave>", on_leave)

        self.map_section = tk.Frame(self.root, bg="grey", width=300, height=600)
        self.map_section.pack(side=tk.LEFT)
        self.comment_section = tk.Frame(self.root, bg="light yellow", width=300, height=600)
        self.comment_section.pack(side=tk.LEFT)
        self.komentarze_layout = self.KomentarzeLayout(self.comment_section, self)
        self.komentarze_layout.pack(side=tk.LEFT)
        self.legend_section = tk.Frame(self.root, bg="black", width=100, height=600)
        self.legend_section.pack(side=tk.LEFT, fill=tk.X)
        self.legend = self.Oznaczenia(self.legend_section)
        self.legend.pack()

        self.root.bind("<Key>", self.key_pressed)

        self.root.mainloop()

    def odswiezSwiat(self):
        self.odswiez_plansze()
        self.komentarze_layout.odswiezKomentarze()
        self.root.update()
        self.root.focus_force()
    def key_pressed(self, event):
        if self.swiat is not None and self.swiat.isPauza():
            keycode = event.keycode
            if keycode == 13:  # KeyCode dla klawisza Enter
                pass  # Tutaj dodaj logikę dla naciśnięcia klawisza Enter
            elif self.swiat.getCzyCzlowiekZyje():
                if keycode == 38:  # KeyCode dla strzałki w górę
                    self.swiat.getCzlowiek().setKierunekRuchu(Kierunek.GORA)
                elif keycode == 40:  # KeyCode dla strzałki w dół
                    self.swiat.getCzlowiek().setKierunekRuchu(Kierunek.DOL)
                elif keycode == 37:  # KeyCode dla strzałki w lewo
                    self.swiat.getCzlowiek().setKierunekRuchu(Kierunek.LEWO)
                elif keycode == 39:  # KeyCode dla strzałki w prawo
                    self.swiat.getCzlowiek().setKierunekRuchu(Kierunek.PRAWO)
                elif keycode == 80:  # KeyCode dla klawisza P
                    tmpUmiejetnosc = self.swiat.getCzlowiek().getUmiejetnosc()
                    if tmpUmiejetnosc.getCzyMoznaAktywowac():
                        tmpUmiejetnosc.Aktywuj()
                        self.swiat.getCzlowiek().setSila(10)
                        Komentator.DodajKomentarz(
                            "Umiejetnosc zwiekaszania sily aktywowana (Pozostaly" + " czas trwania wynosi " + str(tmpUmiejetnosc.getCzasTrwania()) + " tur)")
                    elif tmpUmiejetnosc.getCzyJestAktywna():
                        Komentator.DodajKomentarz(
                            "Umiejetnosc juz zostala aktywowana " + "(Pozostaly" + " czas trwania wynosi " + str(tmpUmiejetnosc.getCzasTrwania()) + " tur)")
                        self.komentarze_layout.odswiezKomentarze()

                        return
                    else:
                        Komentator.DodajKomentarz(
                            "Umiejetnosc mozna wlaczyc tylko po " + str(tmpUmiejetnosc.getCooldown()) + " turach")
                        self.komentarze_layout.odswiezKomentarze()

                        return
                else:
                    Komentator.DodajKomentarz("\nNieoznaczony symbol, sprobuj ponownie")
                    self.komentarze_layout.odswiezKomentarze()

                    return
            elif not self.swiat.getCzyCzlowiekZyje() and (
                    keycode == 38 or keycode == 40 or keycode == 37 or keycode == 39 or keycode == 80):
                Komentator.DodajKomentarz("Czlowiek umarl, nie mozesz im wiecej sterowac")
                self.komentarze_layout.odswiezKomentarze()

                return
            else:
                Komentator.DodajKomentarz("\nNieoznaczony symbol, sprobuj ponownie")
                self.komentarze_layout.odswiezKomentarze()

                return

            Komentator.CzyszczenieKomentarzy()
            self.swiat.setPauza(False)
            self.swiat.WykonajTure()
            self.odswiezSwiat()
            self.swiat.setPauza(True)
    def show_dimensions_window(self):
        Komentator.CzyszczenieKomentarzy()
        self.dim_window = tk.Toplevel(self.root)
        self.dim_window.title("Wymiary planszy")

        self.width_label = tk.Label(self.dim_window, text="Szerokość:")
        self.width_label.pack()
        self.width_entry = tk.Entry(self.dim_window)
        self.width_entry.pack()

        self.height_label = tk.Label(self.dim_window, text="Wysokość:")
        self.height_label.pack()
        self.height_entry = tk.Entry(self.dim_window)
        self.height_entry.pack()

        self.zapelnienie_swiata = tk.Label(self.dim_window, text="Zapelnienie Swiata:")
        self.zapelnienie_swiata.pack()
        self.zapelnienie_entry = tk.Entry(self.dim_window)
        self.zapelnienie_entry.pack()

        self.ok_button = tk.Button(self.dim_window, text="OK", command=self.generate_buttons)
        self.ok_button.pack()

    def odswiez_plansze(self):

        for i in range(self.swiat.getSizeY()):
            for j in range(self.swiat.getSizeX()):
                tmp_organizm = self.swiat.getPlansza()[i][j]
                if tmp_organizm is not None:
                    color = self.swiat.getPlansza()[i][j].getKolor()
                else:
                    color = "white"

                button = self.buttons[i][j]  # Pobranie referencji do istniejącego przycisku
                image = self.images[i][j]  # Pobranie referencji do istniejącego obrazka
                button.configure(bg=color)  # Ustawienie koloru tła przycisku

        self.dim_window.destroy()
    def generate_buttons(self):
        self.swiat = Swiat(int(self.width_entry.get()), int(self.height_entry.get()), self)
        self.swiat.GenerujSwiat(float(self.zapelnienie_entry.get()))

        width = self.swiat.getSizeX()
        height = self.swiat.getSizeY()

        button_width = int(700 / 11)
        button_height = int(600 / 11)

        self.buttons = []  # Lista przechowująca referencje do przycisków
        self.images = []  # Lista przechowująca referencje do obrazków

        for i in range(height):
            row_buttons = []  # Lista przycisków w danym wierszu
            row_images = []  # Lista obrazków w danym wierszu
            for j in range(width):
                if self.swiat.getPlansza()[i][j] is None:
                    color = "white"
                else:
                    color = self.swiat.getPlansza()[i][j].getKolor()
                pixel = tk.PhotoImage(width=1, height=1)
                button = tk.Button(self.map_section, image=pixel, bg=color,
                                   width=300 // width, height=400 // height)
                button.grid(row=i, column=j, padx=0, pady=0)
                row_buttons.append(button)  # Dodanie przycisku do listy przycisków w wierszu
                row_images.append(pixel)  # Dodanie obrazka do listy obrazków w wierszu
            self.buttons.append(row_buttons)  # Dodanie listy przycisków do listy przycisków
            self.images.append(row_images)  # Dodanie listy obrazków do listy obrazków

        self.dim_window.destroy()

    def generate_color(self):
        # Generowanie losowego koloru w formacie RGB
        import random
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return f"#{r:02x}{g:02x}{b:02x}"

    def load(self):
        Komentator.CzyszczenieKomentarzy()
        name_of_file = tkinter.simpledialog.askstring("Wczytaj", "podaj nazwe pliku",initialvalue="zapis1")
        self.swiat = Swiat.WczytajSwiat(name_of_file)
        self.swiat.setSwiatGUI(self)
        width = self.swiat.getSizeX()
        height = self.swiat.getSizeY()

        self.dim_window = tk.Toplevel(self.root)


        self.buttons = []  # Lista przechowująca referencje do przycisków
        self.images = []  # Lista przechowująca referencje do obrazków

        for i in range(height):
            row_buttons = []  # Lista przycisków w danym wierszu
            row_images = []  # Lista obrazków w danym wierszu
            for j in range(width):
                if self.swiat.getPlansza()[i][j] is None:
                    color = "white"
                else:
                    color = self.swiat.getPlansza()[i][j].getKolor()
                pixel = tk.PhotoImage(width=1, height=1)
                button = tk.Button(self.map_section, image=pixel, bg=color,
                                   width=300 // width, height=400 // height)
                button.grid(row=i, column=j, padx=0, pady=0)
                row_buttons.append(button)  # Dodanie przycisku do listy przycisków w wierszu
                row_images.append(pixel)  # Dodanie obrazka do listy obrazków w wierszu
            self.buttons.append(row_buttons)  # Dodanie listy przycisków do listy przycisków
            self.images.append(row_images)  # Dodanie listy obrazków do listy obrazków
        self.odswiezSwiat()
        self.dim_window.destroy()



    def save(self):
        name_of_file_s = tk.simpledialog.askstring("Zapisz", "Podaj nazwę pliku", parent=self.root,
                                                   initialvalue="zapis1")

        self.swiat.ZapiszSwiat(name_of_file_s)
        Komentator.DodajKomentarz("Zapisano świat")
        self.komentarze_layout.odswiezKomentarze()

    def exit(self):
        self.root.quit()



