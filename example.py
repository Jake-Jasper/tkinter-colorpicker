import tkinter as tk
from tkinter import Button, Scale, Canvas


class color_picker:
    def rgbtohex(self, r,g,b):
        return f'#{r:02x}{g:02x}{b:02x}'

    # Function to update the color of the canvas
    def update_col(self, val):
        self.display_box.configure(bg = self.rgbtohex(self.R_scale.get(),self.G_scale.get(),self.B_scale.get()))

    # Close the window and print chosen value
    def close_dialog(self):
        print(self.rgbtohex(self.R_scale.get(),self.G_scale.get(),self.B_scale.get()))
        self.window.destroy()
    
    # Gui for the color chooser
    def color_chooser(self):
        # Create window
        self.window = tk.Tk()
        self.window.title('Choose a color')
        self.window.geometry("356x200")

        # Slider widgets
        self.R_scale = Scale(master = self.window, length = 256, orient='horizontal', from_=0, to=255)
        self.R_scale.grid(row = 0, column = 0)
        self.G_scale = Scale(master = self.window, length = 256, orient='horizontal', from_=0, to=255)
        self.G_scale.grid(row = 1, column = 0)
        self.B_scale = Scale(master = self.window, length = 256, orient='horizontal', from_=0, to=255)
        self.B_scale.grid(row = 2, column = 0)

        # Bindings for mouse interactions
        self.R_scale.bind("<Motion>", self.update_col)
        self.G_scale.bind("<Motion>", self.update_col)
        self.B_scale.bind("<Motion>", self.update_col)

        # Canvas to display color
        self.display_box = Canvas(master = self.window, width =90, height = 125, bg = self.rgbtohex(self.R_scale.get(),self.G_scale.get(),self.B_scale.get()))
        self.display_box.grid(row = 0, rowspan =3, column = 1)

        # Buttons to exit the dialog
        self.Ok_button = Button(master = self.window, text = 'Okay', command = self.close_dialog)
        self.Ok_button.grid(row = 3, column = 0)
        self.close_button = Button(master = self.window, text = 'Close', command = self.window.destroy)
        self.close_button.grid(row = 3, column = 1)

# Main loop
def main():
    # create window
    root = tk.Tk()
    root.geometry("500x500")
    new_var_button = Button(master = root, text = 'test color picker', command = color_picker().color_chooser)
    new_var_button.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
