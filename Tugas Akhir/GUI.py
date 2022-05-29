#Tugas TA PDKP
#Muhammad Fathan Mubiina

#List Modul yang digunakan
#1. Modul 1 : Variable
#2. Modul 2 : if-else
#3. Modul 3 : Perulangan (loop)
#4. Modul 4 : Function & method
#5. Modul 5 : OOP 1 (class, constructor)
#6. Modul 8 : GUI


from tkinter import *
from solve import solve

#inisialisasi gui tkinter
class root():
    
    def __init__(self, root):
        self.root = root
        

root = Tk()
root.title("Fat's Sudoku Solver")
root.geometry("324x550")


#label keterangan program
label = Label(root,text="Fill in the numbers and click solve").grid(row=0, column=1, columnspan=10)

errLabel = Label(root, text="", fg="red")
errLabel.grid(row=15, column=1, columnspan=10, pady=5)

solvedLabel = Label(root, text="", fg="green")
solvedLabel.grid(row=15, column=1, columnspan=10, pady=5)

cells = {}

#validasi panjang angka (satu grid hanya berisi 1 angka)
def ValidateNumber(P):
    
    out = (P.isdigit() or P == "") and len(P) < 2
    return out

reg = root.register(ValidateNumber)

#inisialisasi grid sudoku 3x3
def draw3x3Grid(row, column, bgcolor):
    for i in range(3):
        for j in range(3):
            e = Entry(root, width=5, bg=bgcolor, justify="center", validate="key", validatecommand=(reg, "%P"))
            e.grid(row=row+i+1, column=column+j+1, sticky="nsew", padx=1, pady=1, ipady=5)
            cells[(row+i+1, column+j+1)] = e

#inisialisasi grid sudoku 9x9
def draw9x9Grid():
    color="#D0ffff"
    for rowNo in range(1, 10, 3):
        for colNo in range(0, 9, 3):
            draw3x3Grid(rowNo, colNo, color)
            if color == "#D0ffff":
                color = "#ffffd0"
            else:
                color = "#D0ffff"

#fungsi untuk mereset papan sudoku
def clearValues ():
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2, 11):
        for col in range(1, 10):
            cell = cells[(row, col)]
            cell.delete(0, "end")

#fungsi untuk mem fetch data dari papan
def getValues():
    board = []
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2, 11):
        rows = []
        for col in range(1, 10):
            val = cells[(row, col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))
        
        board.append(rows)
    updateValues(board)

#tombol untuk solve, dan reset papan
btn = Button(root, command=getValues, text="Solve", width=10)
btn.grid(row=20, column=1, columnspan=5, pady=20)

btn = Button(root, command=clearValues, text="Clear", width=10)
btn.grid(row=20, column=5, columnspan=5, pady=20)

#fungsi untuk mengupdate tampilan papan setelah solusi ditemukan
def updateValues(s):
    sol = solve(s)
    if sol != "no":
        for rows in range(2, 11):
            for col in range(1, 10):
                cells[(rows, col)].delete(0, "end")
                cells[(rows, col)].insert(0, sol[rows-2][col-1])
            solvedLabel.configure(text="Sudoku solved!")
    else:
        errLabel.configure(text="No solution exist for this sudoku")

draw9x9Grid()
root.mainloop()

