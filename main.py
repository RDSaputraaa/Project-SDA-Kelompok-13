import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from BE import simpan_data

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Project SDA")
        self.root.attributes('-fullscreen', True)

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        bg_image = Image.open("bg.jpg")
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
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        welcome_label = tk.Label(
            self.root,
            text="Selamat Datang\n di Project Kelompok 13",
            font=("courier new", 36),
            fg="lime",
            bg="black",
            bd=5,
            relief="raised",
            padx=50,
            pady=20
        )
        welcome_label.place(relx=0.5, rely=0.3, anchor="center")

        enter_button = tk.Button(
            self.root,
            text="MULAI",
            font=("courier new", 22),
            bg="black",
            fg="cyan",
            relief="raised",
            bd=5,
            padx=150,
            pady=20,
            command=self.show_perkenalan
        )
        enter_button.place(relx=0.5, rely=0.5, anchor="center")

        exit_button = tk.Button(
            self.root,
            text="KELUAR",
            font=("courier new", 22),
            bg="black",
            fg="red",
            relief="raised",
            padx=140,
            bd=5,
            pady=20,
            command=self.root.quit
        )
        exit_button.place(relx=0.5, rely=0.67, anchor="center")

    def show_perkenalan(self):
        self.clear_widgets()
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
            fg="lime",
            bg="black",
            bd=5,
            relief="raised",
            padx=40,
            pady=30,
            justify="left"
        )
        perkenalan_label.place(relx=0.5, rely=0.4, anchor="center")

        next_button = tk.Button(
            self.root,
            text="MULAI",
            font=("courier new", 22),
            bg="black",
            fg="cyan",
            relief="raised",
            bd=5,
            padx=150,
            pady=20,
            command=self.show_question
        )
        next_button.place(relx=0.5, rely=0.65, anchor="center")

        back_button = tk.Button(
            self.root,
            text="Kembali",
            font=("courier new", 22),
            bg="black",
            fg="red",
            relief="raised",
            bd=5,
            padx=140,
            pady=20,
            command=self.show_main_menu
        )
        back_button.place(relx=0.5, rely=0.8, anchor="center")

    def show_question(self):
        self.clear_widgets()
        self.root.configure(bg="black")

        tk.Label(self.root, text="Nama Ao:", font=("Courier New", 20), bg="black", fg="white").place(relx=0.25, rely=0.05, anchor="center")
        self.ao_entry = tk.Entry(self.root, font=("Courier New", 20), justify="center")
        self.ao_entry.place(relx=0.25, rely=0.1, anchor="center", width=300)

        tk.Label(self.root, text="Nama Aka:", font=("Courier New", 20), bg="black", fg="white").place(relx=0.75, rely=0.05, anchor="center")
        self.aka_entry = tk.Entry(self.root, font=("Courier New", 20), justify="center")
        self.aka_entry.place(relx=0.75, rely=0.1, anchor="center", width=300)

        ao_frame = tk.Frame(self.root, bg="blue", bd=5, relief="raised")
        ao_frame.place(relx=0.0, rely=0.2, relwidth=0.5, relheight=0.6)

        self.ao_score = tk.IntVar(value=0)
        tk.Label(ao_frame, text="Ao", font=("Courier New", 28), bg="blue", fg="white").pack()
        tk.Label(ao_frame, textvariable=self.ao_score, font=("Courier New", 150), bg="blue", fg="white").pack()

        ao_button_frame = tk.Frame(ao_frame, bg="blue")
        ao_button_frame.pack(pady=10)

        btn_frame_ao = tk.Frame(ao_button_frame, bg="blue")
        btn_frame_ao.pack()

        tk.Button(btn_frame_ao, text="+1", font=("Courier New", 20), bg="green", fg="white",
                command=lambda: self.ao_score.set(self.ao_score.get() + 1)).pack(side="left", padx=5)
        tk.Button(btn_frame_ao, text="-1", font=("Courier New", 20), bg="red", fg="white",
                command=lambda: self.ao_score.set(self.ao_score.get() - 1)).pack(side="left", padx=5)
        tk.Button(ao_button_frame, text="Shikaku", font=("Courier New", 20), bg="chocolate", fg="white",
                command=lambda: messagebox.showinfo("Shikaku", f"Shikaku Ao: {self.ao_entry.get()}")).pack(pady=5)
        tk.Button(ao_button_frame, text="Kikken", font=("Courier New", 20), bg="chocolate", fg="white",
                command=lambda: messagebox.showinfo("Kikken", f"Kikken Ao: {self.ao_entry.get()}")).pack(pady=5)

        aka_frame = tk.Frame(self.root, bg="red", bd=5, relief="raised")
        aka_frame.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=0.6)

        self.aka_score = tk.IntVar(value=0)
        tk.Label(aka_frame, text="Aka", font=("Courier New", 28), bg="red", fg="white").pack()
        tk.Label(aka_frame, textvariable=self.aka_score, font=("Courier New", 150), bg="red", fg="white").pack()

        aka_button_frame = tk.Frame(aka_frame, bg="red")
        aka_button_frame.pack(pady=10)

        btn_frame_aka = tk.Frame(aka_button_frame, bg="red")
        btn_frame_aka.pack()

        tk.Button(btn_frame_aka, text="+1", font=("Courier New", 20), bg="green", fg="white",
                command=lambda: self.aka_score.set(self.aka_score.get() + 1)).pack(side="left", padx=5)
        tk.Button(btn_frame_aka, text="-1", font=("Courier New", 20), bg="red", fg="white",
                command=lambda: self.aka_score.set(self.aka_score.get() - 1)).pack(side="left", padx=5)
        tk.Button(aka_button_frame, text="Shikaku", font=("Courier New", 20), bg="chocolate", fg="white",
                command=lambda: messagebox.showinfo("Shikaku", f"Shikaku Aka: {self.aka_entry.get()}")).pack(pady=5)
        tk.Button(aka_button_frame, text="Kikken", font=("Courier New", 20), bg="chocolate", fg="white",
                command=lambda: messagebox.showinfo("Kikken", f"Kikken Aka: {self.aka_entry.get()}")).pack(pady=5)
        
        self.time_var = tk.StringVar(value="00:00")
        self.time_left = 0
        self.timer_running = False

        timer_frame = tk.Frame(self.root, bg="black", bd=10, relief="ridge")
        timer_frame.place(relx=0.5, rely=0.85, anchor="center", relwidth=0.3, relheight=0.1)

        timer_label = tk.Label(timer_frame, textvariable=self.time_var,
                               font=("Courier New", 48), bg="black", fg="white")
        timer_label.pack(expand=True, fill="both")

        tk.Button(self.root, text="Start", font=("Courier New", 18), width=8,
                  bg="green", fg="white", command=self.start_timer).place(relx=0.4, rely=0.95, anchor="center")
        tk.Button(self.root, text="Stop", font=("Courier New", 18), width=8,
                  bg="blue", fg="white", command=self.stop_timer).place(relx=0.5, rely=0.95, anchor="center")
        tk.Button(self.root, text="Reset", font=("Courier New", 18), width=8,
                  bg="red", fg="white", command=self.reset_timer).place(relx=0.6, rely=0.95, anchor="center")

        exit_button = tk.Button(
            self.root,
            text="X",
            font=("Courier New", 16, "bold"),
            bg="red",
            fg="white",
            relief="raised",
            command=self.root.quit
        )
        exit_button.place(relx=0.97, rely=0.02, anchor="ne")

    def update_timer(self):
        if self.time_left > 0 and self.timer_running:
            self.time_left -= 1
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            self.time_var.set(f"{minutes:02d}:{seconds:02d}")
            self.root.after(1000, self.update_timer)
        else:
            self.timer_running = False
            if self.time_left == 0:
                simpan_data(
                    ao_name=self.ao_entry.get(),
                    ao_score=self.ao_score.get(),
                    aka_name=self.aka_entry.get(),
                    aka_score=self.aka_score.get()
                )
                messagebox.showinfo("Waktu Habis", "Timer selesai! Skor telah disimpan.")

    def start_timer(self):
        if not self.timer_running:
            self.time_left = 10
            self.timer_running = True
            self.update_timer()

    def stop_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.time_left = 0
        self.time_var.set("00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from BE import simpan_data

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Project SDA")
        self.root.attributes('-fullscreen', True)

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        bg_image = Image.open("bg.jpg")
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
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        welcome_label = tk.Label(
            self.root,
            text="Selamat Datang\n di Project Kelompok 13",
            font=("courier new", 36),
            fg="lime",
            bg="black",
            bd=5,
            relief="raised",
            padx=50,
            pady=20
        )
        welcome_label.place(relx=0.5, rely=0.3, anchor="center")

        enter_button = tk.Button(
            self.root,
            text="MULAI",
            font=("courier new", 22),
            bg="black",
            fg="cyan",
            relief="raised",
            bd=5,
            padx=150,
            pady=20,
            command=self.show_perkenalan
        )
        enter_button.place(relx=0.5, rely=0.5, anchor="center")

        exit_button = tk.Button(
            self.root,
            text="KELUAR",
            font=("courier new", 22),
            bg="black",
            fg="red",
            relief="raised",
            padx=140,
            bd=5,
            pady=20,
            command=self.root.quit
        )
        exit_button.place(relx=0.5, rely=0.67, anchor="center")

    def show_perkenalan(self):
        self.clear_widgets()
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
            fg="lime",
            bg="black",
            bd=5,
            relief="raised",
            padx=40,
            pady=30,
            justify="left"
        )
        perkenalan_label.place(relx=0.5, rely=0.4, anchor="center")

        next_button = tk.Button(
            self.root,
            text="MULAI",
            font=("courier new", 22),
            bg="black",
            fg="cyan",
            relief="raised",
            bd=5,
            padx=150,
            pady=20,
            command=self.show_question
        )
        next_button.place(relx=0.5, rely=0.65, anchor="center")

        back_button = tk.Button(
            self.root,
            text="Kembali",
            font=("courier new", 22),
            bg="black",
            fg="red",
            relief="raised",
            bd=5,
            padx=140,
            pady=20,
            command=self.show_main_menu
        )
        back_button.place(relx=0.5, rely=0.8, anchor="center")

    def show_question(self):
        self.clear_widgets()
        self.root.configure(bg="black")

        tk.Label(self.root, text="Nama Ao:", font=("Courier New", 20), bg="black", fg="white").place(relx=0.25, rely=0.05, anchor="center")
        self.ao_entry = tk.Entry(self.root, font=("Courier New", 20), justify="center")
        self.ao_entry.place(relx=0.25, rely=0.1, anchor="center", width=300)

        tk.Label(self.root, text="Nama Aka:", font=("Courier New", 20), bg="black", fg="white").place(relx=0.75, rely=0.05, anchor="center")
        self.aka_entry = tk.Entry(self.root, font=("Courier New", 20), justify="center")
        self.aka_entry.place(relx=0.75, rely=0.1, anchor="center", width=300)

        ao_frame = tk.Frame(self.root, bg="blue", bd=5, relief="raised")
        ao_frame.place(relx=0.0, rely=0.2, relwidth=0.5, relheight=0.6)

        self.ao_score = tk.IntVar(value=0)
        tk.Label(ao_frame, text="Ao", font=("Courier New", 28), bg="blue", fg="white").pack()
        tk.Label(ao_frame, textvariable=self.ao_score, font=("Courier New", 150), bg="blue", fg="white").pack()

        ao_button_frame = tk.Frame(ao_frame, bg="blue")
        ao_button_frame.pack(pady=10)

        btn_frame_ao = tk.Frame(ao_button_frame, bg="blue")
        btn_frame_ao.pack()

        tk.Button(btn_frame_ao, text="+1", font=("Courier New", 20), bg="green", fg="white",
                command=lambda: self.ao_score.set(self.ao_score.get() + 1)).pack(side="left", padx=5)
        tk.Button(btn_frame_ao, text="-1", font=("Courier New", 20), bg="red", fg="white",
                command=lambda: self.ao_score.set(self.ao_score.get() - 1)).pack(side="left", padx=5)
        tk.Button(ao_button_frame, text="Shikaku", font=("Courier New", 20), bg="chocolate", fg="white",
                command=lambda: messagebox.showinfo("Shikaku", f"Shikaku Ao: {self.ao_entry.get()}")).pack(pady=5)
        tk.Button(ao_button_frame, text="Kikken", font=("Courier New", 20), bg="chocolate", fg="white",
                command=lambda: messagebox.showinfo("Kikken", f"Kikken Ao: {self.ao_entry.get()}")).pack(pady=5)

        aka_frame = tk.Frame(self.root, bg="red", bd=5, relief="raised")
        aka_frame.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=0.6)

        self.aka_score = tk.IntVar(value=0)
        tk.Label(aka_frame, text="Aka", font=("Courier New", 28), bg="red", fg="white").pack()
        tk.Label(aka_frame, textvariable=self.aka_score, font=("Courier New", 150), bg="red", fg="white").pack()

        aka_button_frame = tk.Frame(aka_frame, bg="red")
        aka_button_frame.pack(pady=10)

        btn_frame_aka = tk.Frame(aka_button_frame, bg="red")
        btn_frame_aka.pack()

        tk.Button(btn_frame_aka, text="+1", font=("Courier New", 20), bg="green", fg="white",
                command=lambda: self.aka_score.set(self.aka_score.get() + 1)).pack(side="left", padx=5)
        tk.Button(btn_frame_aka, text="-1", font=("Courier New", 20), bg="red", fg="white",
                command=lambda: self.aka_score.set(self.aka_score.get() - 1)).pack(side="left", padx=5)
        tk.Button(aka_button_frame, text="Shikaku", font=("Courier New", 20), bg="chocolate", fg="white",
                command=lambda: messagebox.showinfo("Shikaku", f"Shikaku Aka: {self.aka_entry.get()}")).pack(pady=5)
        tk.Button(aka_button_frame, text="Kikken", font=("Courier New", 20), bg="chocolate", fg="white",
                command=lambda: messagebox.showinfo("Kikken", f"Kikken Aka: {self.aka_entry.get()}")).pack(pady=5)
        
        self.time_var = tk.StringVar(value="00:00")
        self.time_left = 0
        self.timer_running = False

        timer_frame = tk.Frame(self.root, bg="black", bd=10, relief="ridge")
        timer_frame.place(relx=0.5, rely=0.85, anchor="center", relwidth=0.3, relheight=0.1)

        timer_label = tk.Label(timer_frame, textvariable=self.time_var,
                               font=("Courier New", 48), bg="black", fg="white")
        timer_label.pack(expand=True, fill="both")

        tk.Button(self.root, text="Start", font=("Courier New", 18), width=8,
                  bg="green", fg="white", command=self.start_timer).place(relx=0.4, rely=0.95, anchor="center")
        tk.Button(self.root, text="Stop", font=("Courier New", 18), width=8,
                  bg="blue", fg="white", command=self.stop_timer).place(relx=0.5, rely=0.95, anchor="center")
        tk.Button(self.root, text="Reset", font=("Courier New", 18), width=8,
                  bg="red", fg="white", command=self.reset_timer).place(relx=0.6, rely=0.95, anchor="center")

        exit_button = tk.Button(
            self.root,
            text="X",
            font=("Courier New", 16, "bold"),
            bg="red",
            fg="white",
            relief="raised",
            command=self.root.quit
        )
        exit_button.place(relx=0.97, rely=0.02, anchor="ne")

    def update_timer(self):
        if self.time_left > 0 and self.timer_running:
            self.time_left -= 1
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            self.time_var.set(f"{minutes:02d}:{seconds:02d}")
            self.root.after(1000, self.update_timer)
        else:
            self.timer_running = False
            if self.time_left == 0:
                simpan_data(
                    ao_name=self.ao_entry.get(),
                    ao_score=self.ao_score.get(),
                    aka_name=self.aka_entry.get(),
                    aka_score=self.aka_score.get()
                )
                messagebox.showinfo("Waktu Habis", "Timer selesai! Skor telah disimpan.")

    def start_timer(self):
        if not self.timer_running:
            self.time_left = 10
            self.timer_running = True
            self.update_timer()

    def stop_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.time_left = 0
        self.time_var.set("00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
