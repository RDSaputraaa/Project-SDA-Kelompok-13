import tkinter as tk
from PIL import Image, ImageTk

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Project SDA")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        bg_image = Image.open("A.jpg")
        bg_image = bg_image.resize((800, 600))
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.place(relwidth=1, relheight=1)

        self.welcome_label = tk.Label(
            self.root,
            text="Selamat Datang\n di Project Kelompok 13",
            font=("courier new", 24),
            fg="black",
            bg="sky blue",
            bd=5,
            relief="raised",
            padx=20,
            pady=10
        )
        self.welcome_label.place(relx=0.5, rely=0.15, anchor="center")

        self.enter_button = tk.Button(
            self.root,
            text="MULAI",
            font=("courier new", 18),
            bg="sky blue",
            fg="black",
            padx=20,
            pady=10
        )
        self.enter_button.place(relx=0.5, rely=0.45, anchor="center")

        self.explain_button = tk.Button(
            self.root,
            text="PENJELASAN",
            font=("courier new", 18),
            bg="sky blue",
            fg="black",
            padx=20,
            pady=10,
            command=self.show_info
        )
        self.explain_button.place(relx=0.5, rely=0.55, anchor="center")

    def show_info(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        info_label = tk.Label(
            self.root,
            text="Penjelasan Project Kelompok 13:\n\n"
                 "Pada project ini kami membuat sebuah game MATEMATIKA\n"
                 "Berikut cara bermainnya:\n"
                 "1. Masukkan nama pemain untuk memulai permainan.\n"
                 "2. Setelah masuk ke permainan, kamu akan diberi\n   sebuah soal dengan 4 pilihan jawab.\n"
                 "3. Untuk setiap soal yang benar akan diberi\n   10 POIN, sedangkan Jika Jawaban\n   salah akan diberikan 0 POIN.\n",
            font=("courier new", 18),
            fg="black",
            bg="lightyellow",
            padx=20,
            pady=20,
            justify="left"
        )
        info_label.place(relx=0.5, rely=0.5, anchor="center")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
