"""
    An Animated GIF with Tkinter
    Author: Israel Dryer
    Modified: 2020-05-29
    GIF Image: https://www.behance.net/gallery/51853877/Dancing-Bear-Animated-GIF
"""    
import tkinter as tk
from itertools import cycle
from PIL import Image, ImageTk, ImageSequence

class App:
    """Animated GIF"""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Have a Happy Thursday!!')
        self.root.iconbitmap('sun.ico')
        self.sequence = cycle([ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('bear.gif'))])
        self.fps = Image.open('bear.gif').info['duration']
        self.title = tk.Label(self.root, text="Happy Thursday!!", font=("Bodoni MT", 40),
            background='#A37A3B', foreground='#FFF', anchor=tk.CENTER)
        self.gif = tk.Label(self.root, image=next(self.sequence))

        # arrange objects
        self.title.pack(side=tk.TOP, ipady=15, fill=tk.X, expand=tk.YES)
        self.gif.pack()

        # begin animation
        self.animate()

    def animate(self):
        """Animate the image"""
        self.gif.config(image=next(self.sequence))
        self.root.after(self.fps, self.animate)

if __name__ == '__main__':

    app = App()
    app.root.mainloop()
