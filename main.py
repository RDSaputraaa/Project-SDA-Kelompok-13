import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Project SDA")
        self.root.attributes('-fullscreen', True)

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        bg_image = Image.open("A.jpg")
        bg_image = bg_image.resize((self.screen_width, self.screen_height))
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        self.show_main_menu()

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            if widget != self.bg_label:
                widget.destroy()

    def show_main_menu(self):
        self.clear_widgets()

        welcome_label = tk.Label(
            self.root,
            text="Selamat Datang\n di Project Kelompok 13",
            font=("courier new", 36),
            fg="black",
            bg="sky blue",
            bd=5,
            relief="raised",
            padx=50,
            pady=20
        )
        welcome_label.place(relx=0.5, rely=0.2, anchor="center")

        enter_button = tk.Button(
            self.root,
            text="MULAI",
            font=("courier new", 22),
            bg="sky blue",
            fg="black",
            relief="raised",
            padx=50,
            pady=20,
            command=self.show_perkenalan
        )
        enter_button.place(relx=0.5, rely=0.43, anchor="center")

        explain_button = tk.Button(
            self.root,
            text="PENJELASAN",
            font=("courier new", 22),
            bg="sky blue",
            fg="black",
            relief="raised",
            padx=50,
            pady=20,
            command=self.show_info
        )
        explain_button.place(relx=0.5, rely=0.56, anchor="center")

        exit_button = tk.Button(
            self.root,
            text="KELUAR",
            font=("courier new", 22),
            bg="sky blue",
            fg="black",
            relief="raised",
            padx=50,
            pady=20,
            command=self.root.quit
        )
        exit_button.place(relx=0.5, rely=0.69, anchor="center")

    def show_info(self):
        self.clear_widgets()

        info_label = tk.Label(
            self.root,
            text="📝Penjelasan Project Kelompok 13:\n\n"
                 "Pada project ini kami membuat sebuah game MATEMATIKA\n"
                 "Berikut cara bermainnya:\n"
                 "1. Masukkan nama pemain untuk memulai permainan.\n"
                 "2. Setelah itu akan diberikan 4 soal. \n"
                 "3. Untuk setiap soal yang benar akan diberikan 25 POIN. \n" 
                 "4. Jika Jawaban salah akan diberikan 0 POIN.",
            font=("courier new", 22),
            fg="black",
            bg="sky blue",
            bd=5,
            relief="raised",
            padx=50,
            pady=20,
            justify="left"
        )
        info_label.place(relx=0.5, rely=0.4, anchor="center")

        back_button = tk.Button(
            self.root,
            text="KEMBALI",
            font=("courier new", 22),
            bg="sky blue",
            fg="black",
            relief="raised",
            padx=50,
            pady=20,
            command=self.show_main_menu
        )
        back_button.place(relx=0.5, rely=0.75, anchor="center")

    def show_perkenalan(self):
        self.clear_widgets()

        perkenalan_label = tk.Label(
            self.root,
            text="👥 Perkenalan Anggota Kelompok 13:\n\n"
                 "1. Rizky Dwi Saputra (2417051009)\n"
                 "2. Meidina Aulia (2417051038)\n"
                 "3. Naura Azura Grahyta M (2417051005)\n"
                 "4. Alfin Lambok Kristiano Silitonga (2417053001)",
            font=("courier new", 24),
            fg="black",
            bg="sky blue",
            bd=5,
            relief="raised",
            padx=40,
            pady=30,
            justify="left"
        )
        perkenalan_label.place(relx=0.5, rely=0.35, anchor="center")

        next_button = tk.Button(
            self.root,
            text="Mulai",
            font=("courier new", 22),
            bg="sky blue",
            fg="black",
            relief="raised",
            padx=50,
            pady=20,
            command=self.start_game
        )
        next_button.place(relx=0.5, rely=0.65, anchor="center")

    def start_game(self):
        self.player_name = None
        self.ask_name()

    def ask_name(self):
        self.clear_widgets()

        frame = tk.Frame(
            self.root,
            bg="sky blue",
            bd=5,
            relief="raised",
            padx=50,
            pady=30
        )
        frame.place(relx=0.5, rely=0.5, anchor="center")

        title_label = tk.Label(
            frame,
            text="Masukkan Nama:",
            font=("courier new", 24),
            bg="sky blue",
            fg="black"
        )
        title_label.pack(pady=(0, 20))

        name_label = tk.Label(
            frame,
            text="Nama:",
            font=("courier new", 24),
            bg="sky blue",
            fg="black"
        )
        name_label.pack(anchor="w")

        self.name_entry = tk.Entry(
            frame,
            font=("courier new", 20),
            width=30,
            relief="raised"
        )
        self.name_entry.pack(pady=5)

        start_btn = tk.Button(
            frame,
            text="MULAI GAME",
            font=("courier new", 20),
            bg="sky blue",
            fg="black",
            relief="raised",
        )
        start_btn.pack(pady=(20, 0))

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
