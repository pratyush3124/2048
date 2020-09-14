from tkinter import *
import random


class Main(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.canvas = Game(self)
        self.canvas.pack()


class Game(Canvas):
    def __init__(self, parent):
        Canvas.__init__(self, parent, height=452, width=452, bg="#BBADA0")

        self.colors = {
            "bg": "#BBADA0",
            "empty": "#CFC1B5",
            "2": "#EDE4D7",
            "4": "#EDE4D7",
            "8": "#EFB27B",
        }

        self.numbers = [[0 for i in range(4)] for i in range(4)]

        self.positions = [[0 for i in range(4)] for i in range(4)]
        for i in range(4):
            for j in range(4):
                self.positions[i][j] = (
                    j * 111 + 11,
                    i * 111 + 11,
                    (j + 1) * 100 + j * 11 + 11,
                    (i + 1) * 100 + i * 11 + 11,
                )

        for i in range(4):
            for j in range(4):
                a = self.positions[i][j]
                self.create_rectangle(
                    a[0],
                    a[1],
                    a[2],
                    a[3],
                    fill=self.colors["empty"],
                    outline=self.colors["empty"],
                )

        self.create_num()

        self.focus_set()
        self.bind("<Key>", lambda event: self.move(event.char))
        self.bind("<Left>", lambda event: self.move("a"))
        self.bind("<Right>", lambda event: self.move("d"))
        self.bind("<Up>", lambda event: self.move("w"))
        self.bind("<Down>", lambda event: self.move("s"))

    def create_num(self):
        fl = True
        while fl:
            a = random.randint(0, 3)
            b = random.randint(0, 3)
            c = 8
            if self.numbers[a][b] == 0:
                self.numbers[a][b] = c
                fl = False

        self.refresh()

    def refresh(self):
        for i in range(4):
            for j in range(4):
                if self.numbers[i][j] != 0:
                    a = self.positions[i][j]
                    self.create_rectangle(a[0], a[1], a[2], a[3], fill=self.colors[str(
                        self.numbers[i][j])], outline=self.colors[str(self.numbers[i][j])])
                else:
                    a = self.positions[i][j]
                    self.create_rectangle(a[0], a[1], a[2], a[3], fill=self.colors['empty'],
                        outline=self.colors['empty'])

    def move(self, d):
        if d == "w":
            for i in range(4):
                for j in range(4):
                    if self.numbers[i][j] != 0:
                        for x in range(i,0,-1):
                            self.numbers[x][j], self.numbers[x - 1][j] = 0 , self.numbers[x][j]

        if d == "a":
            for i in range(4):
                for j in range(4):
                    if self.numbers[i][j] != 0:
                        for x in range(j,0,-1):
                            self.numbers[i][x], self.numbers[i][x-1] = (
                                0,
                                self.numbers[i][x],
                            )
        if d == "s":
            for i in range(4):
                for j in range(4):
                    if self.numbers[i][j] != 0:
                        for x in range(i,3):
                            self.numbers[x][j], self.numbers[x + 1][j] = (
                                0,
                                self.numbers[x][j],
                            )
        if d == "d":
            for i in range(4):
                for j in range(4):
                    if self.numbers[i][j] != 0:
                        for x in range(j,3):
                            self.numbers[i][x], self.numbers[i][x+1] = (
                                0,
                                self.numbers[i][x],
                            )
        self.refresh()
        self.create_num()


if __name__ == "__main__":
    a = Main()
    a.mainloop()
