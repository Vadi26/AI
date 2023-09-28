import tkinter as tk
import numpy as np

def create_chessboard(canvas, rows, cols, square_size):
    for i in range(rows):
        for j in range(cols):
            x1 = j * square_size
            y1 = i * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size
            canvas.create_rectangle(x1, y1, x2, y2, fill='white')
    for i in range(rows):
        for j in range(cols):
            x1 = j * square_size
            y1 = i * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size
            if (i == 1) and (j == 1):
                canvas.create_rectangle(x1, y1, x2, y2, fill='grey')
            elif (i == 2) and (j == 1):
                canvas.create_rectangle(x1, y1, x2, y2, fill='grey')
            elif (i == 2) and (j == 2):
                canvas.create_rectangle(x1, y1, x2, y2, fill='grey')
            elif (i == 3) and (j == 2):
                canvas.create_rectangle(x1, y1, x2, y2, fill='grey')
            elif (i == 3) and (j == 3):
                canvas.create_rectangle(x1, y1, x2, y2, fill='grey')
            elif (i == 3) and (j == 4):
                canvas.create_rectangle(x1, y1, x2, y2, fill='grey')
            elif (i == 3) and (j == 5):
                canvas.create_rectangle(x1, y1, x2, y2, fill='grey')
            elif (i == 3) and (j == 6):
                canvas.create_rectangle(x1, y1, x2, y2, fill='grey')
            elif (i == 3) and (j == 7):
                canvas.create_rectangle(x1, y1, x2, y2, fill='grey')
            elif (i == 3) and (j == 8):
                canvas.create_rectangle(x1, y1, x2, y2, fill='grey')
            elif (i == 3) and (j == 9):
                canvas.create_rectangle(x1, y1, x2, y2, fill='grey')
            elif (i == 2) and (j == 9):
                canvas.create_rectangle(x1, y1, x2, y2, fill='grey')
            elif (i == 1) and (j == 9):
                canvas.create_rectangle(x1, y1, x2, y2, fill='grey')
            elif (i == 1) and (j == 8):
                canvas.create_rectangle(x1, y1, x2, y2, fill='grey')
            elif (i == 1) and (j == 7):
                canvas.create_rectangle(x1, y1, x2, y2, fill='grey')
            elif (i == 1) and (j == 6):
                canvas.create_rectangle(x1, y1, x2, y2, fill='grey')
            elif (i == 1) and (j == 5):
                canvas.create_rectangle(x1, y1, x2, y2, fill='grey')
            elif (i == 2) and (j == 6):
                canvas.create_rectangle(x1, y1, x2, y2, fill='green')
            elif (i == 3) and (j == 0):
                canvas.create_rectangle(x1, y1, x2, y2, fill='red')

def main():
    root = tk.Tk()
    root.title("Chessboard")

    canvas = tk.Canvas(root, width=400, height=300)  
    canvas.pack()

    rows = 5
    cols = 11

    square_size = min(400 // cols, 300 // rows)

    create_chessboard(canvas, rows, cols, square_size)

    root.mainloop()

# my logic is to create a matrix. Now an element of the matrix will be a list of two numbers. First digit will be the state of the node and the second number will be th cost or the heuristic of that node
def BeFiSe(maze):
    return 0



if __name__ == "__main__":
    main()
