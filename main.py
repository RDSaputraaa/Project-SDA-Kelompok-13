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
            widget.destroy()

    def show_main_menu(self):
        self.clear_widgets()
        self.root.configure(bg="SystemButtonFace")
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

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
        enter_button.place(relx=0.5, rely=0.5, anchor="center")

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

    def show_perkenalan(self):
        self.clear_widgets()
        self.root.configure(bg="SystemButtonFace")
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        perkenalan_label = tk.Label(
            self.root,
            text="Perkenalan Anggota Kelompok 13:\n\n"
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

        next_button = tk.Button(
            self.root,
            text="Mulai",
            font=("courier new", 22),
            bg="sky blue",
            fg="black",
            relief="raised",
            padx=50,
            pady=20,
            command=self.show_question
        )
        next_button.place(relx=0.5, rely=0.65, anchor="center")

    def show_question(self):
        self.clear_widgets()
        self.root.configure(bg="black")

        ao_entry_label = tk.Label(self.root, text="Nama Ao:", font=("Courier New", 20), bg="black", fg="white")
        ao_entry_label.place(relx=0.25, rely=0.05, anchor="center")
        self.ao_entry = tk.Entry(self.root, font=("Courier New", 20), justify="center")
        self.ao_entry.place(relx=0.25, rely=0.1, anchor="center", width=300)

        aka_entry_label = tk.Label(self.root, text="Nama Aka:", font=("Courier New", 20), bg="black", fg="white")
        aka_entry_label.place(relx=0.75, rely=0.05, anchor="center")
        self.aka_entry = tk.Entry(self.root, font=("Courier New", 20), justify="center")
        self.aka_entry.place(relx=0.75, rely=0.1, anchor="center", width=300)

        ao_frame = tk.Frame(self.root, bg="red", bd=5, relief="raised")
        ao_frame.place(relx=0.0, rely=0.2, relwidth=0.5, relheight=0.6)

        self.ao_score = tk.IntVar(value=0)
        tk.Label(ao_frame, text="Ao", font=("Courier New", 28), bg="red", fg="white").pack()
        tk.Label(ao_frame, textvariable=self.ao_score, font=("Courier New", 72), bg="red", fg="white").pack()
        tk.Button(ao_frame, text="+1", font=("Courier New", 20),
                  command=lambda: self.ao_score.set(self.ao_score.get() + 1)).pack(pady=10)
        tk.Button(ao_frame, text="-1", font=("Courier New", 20),
                  command=lambda: self.ao_score.set(self.ao_score.get() - 1)).pack(pady=10)
        tk.Button(ao_frame, text="Shikaku", font=("Courier New", 20),
                  command=lambda: messagebox.showinfo("Shikaku", f"Shikaku Ao: {self.ao_entry.get()}")).pack(pady=5)
        tk.Button(ao_frame, text="Kikken", font=("Courier New", 20),
                  command=lambda: messagebox.showinfo("Kikken", f"Kikken Ao: {self.ao_entry.get()}")).pack(pady=5)

        aka_frame = tk.Frame(self.root, bg="blue", bd=5, relief="raised")
        aka_frame.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=0.6)

        self.aka_score = tk.IntVar(value=0)
        tk.Label(aka_frame, text="Aka", font=("Courier New", 28), bg="blue", fg="white").pack()
        tk.Label(aka_frame, textvariable=self.aka_score, font=("Courier New", 72), bg="blue", fg="white").pack()
        tk.Button(aka_frame, text="+1", font=("Courier New", 20),
                  command=lambda: self.aka_score.set(self.aka_score.get() + 1)).pack(pady=10)
        tk.Button(aka_frame, text="-1", font=("Courier New", 20),
                  command=lambda: self.aka_score.set(self.aka_score.get() - 1)).pack(pady=10)
        tk.Button(aka_frame, text="Shikaku", font=("Courier New", 20),
                  command=lambda: messagebox.showinfo("Shikaku", f"Shikaku Aka: {self.aka_entry.get()}")).pack(pady=5)
        tk.Button(aka_frame, text="Kikken", font=("Courier New", 20),
                  command=lambda: messagebox.showinfo("Kikken", f"Kikken Aka: {self.aka_entry.get()}")).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
