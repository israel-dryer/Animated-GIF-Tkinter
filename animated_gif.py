"""
    An Animated GIF with Tkinter
    Author: Israel Dryer
    Modified: 2020-05-14
    GIF Image: https://www.behance.net/gallery/51853877/Dancing-Bear-Animated-GIF
"""    
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence


class App:
    """Animated GIF"""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Have a Happy Thursday!!')
        self.root.iconbitmap('sun.ico')
        self.sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('bear.gif'))]
        self.index = 0
        self.title = tk.Label(self.root, text="Happy Thursday!!", font=("Bodoni MT", 40),
            background='#A37A3B', foreground='#FFF', anchor=tk.CENTER)
        self.gif = tk.Label(self.root, image=self.sequence[self.index])

        # arrange objects
        self.title.pack(side=tk.TOP, ipady=15, fill=tk.X, expand=tk.YES)
        self.gif.pack()

        # begin animation
        self.animate()

    def animate(self):
        """Animate the image"""
        if self.index == len(self.sequence):
            self.index = 0
        self.gif.config(image=self.sequence[self.index])
        self.index += 1
        self.root.after(22, self.animate)


if __name__ == '__main__':

    app = App()
    app.root.mainloop()
