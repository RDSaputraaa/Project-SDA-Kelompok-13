import tkinter as tk
from PIL import Image, ImageTk

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Utama Tkinter")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        bg_image = Image.open("2.png")
        bg_image = bg_image.resize((800, 600))
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.place(relwidth=1, relheight=1)

        self.main_frame = tk.Frame(self.root, bg="white", bd=10, relief="raised")
        self.main_frame.place(relx=0.5, rely=0.2, anchor="center")

        self.show_welcome_page()

    def show_welcome_page(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        welcome_label = tk.Label(
            self.main_frame, 
            text="Selamat Datang", 
            font=("courier new", 24), 
            bg="white",
            fg="black"
        )
        welcome_label.pack(padx=10, pady=10, expand=True, )

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()