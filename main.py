import tkinter as tk
from tkinter import ttk, messagebox
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

        self.welcome_label = tk.Label(
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
        self.welcome_label.place(relx=0.5, rely=0.2, anchor="center")

        self.enter_button = tk.Button(
            self.root,
            text="MULAI",
            font=("courier new", 22),
            bg="sky blue",
            relief="raised",
            fg="black",
            padx=50,
            pady=20,
            command=self.show_perkenalan
        )
        self.enter_button.place(relx=0.5, rely=0.43, anchor="center")

        self.explain_button = tk.Button(
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
        self.explain_button.place(relx=0.5, rely=0.56, anchor="center")

        self.exit_button = tk.Button(
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
        self.exit_button.place(relx=0.5, rely=0.69, anchor="center")

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
        perkenalan_label.place(relx=0.5, rely=0.4, anchor="center")

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

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
