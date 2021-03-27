import tkinter as tk
from tkinter import Button, Scale, Canvas


class color_picker:
    def rgbtohex(self, r,g,b):
        return f'#{r:02x}{g:02x}{b:02x}'


    def update_col(self, val):
        self.display_box.configure(bg = self.rgbtohex(self.R_scale.get(),self.G_scale.get(),self.B_scale.get()))

    def color_chooser(self):
        window = tk.Tk()
        window.geometry("200x200")

        self.R_scale = Scale(master = window, orient='horizontal', from_=0, to=255)
        self.R_scale.grid(row = 0, column = 0)
        self.G_scale = Scale(master = window, orient='horizontal', from_=0, to=255)
        self.G_scale.grid(row = 1, column = 0)
        self.B_scale = Scale(master = window, orient='horizontal', from_=0, to=255)
        self.B_scale.grid(row = 2, column = 0)

        self.R_scale.bind("<ButtonRelease-1>", self.update_col)
        self.G_scale.bind("<ButtonRelease-1>", self.update_col)
        self.B_scale.bind("<ButtonRelease-1>", self.update_col)


        self.display_box = Canvas(master = window, width =90, height = 125, bg = self.rgbtohex(self.R_scale.get(),self.G_scale.get(),self.B_scale.get()))
        self.display_box.grid(row = 0, rowspan =3, column = 1)


        self.Ok_button = Button(master = window, text = 'Okay', command = None).grid(row = 3, column = 0)
        self.close_button = Button(master = window, text = 'Close', command = window.destroy).grid(row = 3, column = 1)


def main():
    # create window
    root = tk.Tk()
    root.geometry("500x500")
    new_var_button = Button(master = root, text = 'Add new variable', command = color_picker().color_chooser).pack()
    root.mainloop()

if __name__ == "__main__":
    main()
