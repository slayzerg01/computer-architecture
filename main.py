from tkinter import *


def multiplication(a, b):
    Vout = ["0"] * len(b)
    Nout = ["0"] * len(b)
    c = ["0"] * len(b)
    k = 0
    for i in range(len(b)):
        if i == 0:
            c[i] = a * int(b[i])
            Vout[i] = c[i]
        else:
            c[i] = str(c[i - 1]) + "0"
            Vout[i] = c[i]
            length = len(c[i]) + 1
            new = ["0"] * length
            p = len(a) - 1
            if int(b[i]) != 0:
                for j in range(length - 1, -1, -1):
                    if p >= 0:
                        new[j] = str(int(c[i][j - 1]) + int(a[p]) + k)
                    else:
                        new[j] = str(int(c[i][j - 1]) + k)
                    if int(new[j]) == 2:
                        new[j] = "0"
                        k = 1
                    elif int(new[j]) == 3:
                        new[j] = "1"
                        k = 1
                    else:
                        k = 0
                    p -= 1
                c[i] = ''.join(new)
            Nout[i] = c[i]
    otvet = ''
    flag = False
    for i in range(len(c[len(b) - 1])):
        if c[len(b) - 1][i] == '1':
            flag = True
        if flag:
            otvet += c[len(b) - 1][i]

    v = ["A {:0>18}".format(a), "B {:0>18}".format(b), "-" * 20]
    for i in range(len(b) - 1):
        if i < 1:
            v.append("  {:0>18}".format(Vout[i]))
            v.append("  {:0>18} <- Сдвиг влево".format(Vout[i + 1]))
            if int(b[i + 1]) == 1:
                v.append("+ {:0>18}".format(a))
            else:
                v.append("+ {:0>18}".format("0" * len(a)))
        if i >= 1:
            v.append("  {:0>18}".format(Nout[i]))
            v.append("  {:0>18} <- Сдвиг влево".format(Vout[i + 1]))
            if int(b[i + 1]) == 1:
                v.append("+ {:0>18}".format(a))
            else:
                v.append("+ {:0>18}".format("0" * len(a)))
        v.append("-" * 20)
    v.append("  {:0>18}".format(otvet))
    return v


class MainWindow(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Умножение чисел, начиная со страрших разрядов \n множителя и сдвигом СЧП влево "). \
            grid(row=0, column=0, columnspan=2, sticky=W + E, padx=10, pady=10)

        Label(self, text="Число A").grid(row=1, column=0, sticky=W + E, padx=10, pady=10)
        Label(self, text="Число B").grid(row=2, column=0, sticky=W + E, padx=10, pady=10)
        self.A = Entry(self, width=30)
        self.B = Entry(self, width=30)
        self.A.grid(row=1, column=1, padx=10, pady=10)
        self.B.grid(row=2, column=1, padx=10, pady=10)
        Button(self, text="ВЫЧИСЛИТЬ", command=self.calculate, width=20, activebackground="GREY").grid(row=3, column=0,
                                                                                                       columnspan=2,
                                                                                                       sticky=W + E,
                                                                                                       padx=10, pady=10)
        Label(self, text="Процесс умножения").grid(row=4, column=0, columnspan=2, sticky=W + E + S, padx=10)
        self.mult = Text(self, width=41, height=20, wrap=WORD)
        self.mult.configure(state=DISABLED)
        self.mult.grid(row=5, column=0, sticky=W, columnspan=2, padx=10)

        Label(self, text="Результат умножения").grid(row=6, column=0, sticky=W + E, padx=10, pady=10)
        self.answer = Text(self, width=23, height=1, wrap=WORD)
        self.answer.configure(state=DISABLED)
        self.answer.grid(row=6, column=1, sticky=W, padx=10, pady=10)

    def calculate(self):
        if (self.A.get().find('2') == -1 and self.A.get().find('3') == -1 and self.A.get().find('4') == -1 and
                self.A.get().find('5') == -1 and self.A.get().find('6') == -1 and self.A.get().find('7') == -1 and
                self.A.get().find('8') == -1 and self.A.get().find('9') == -1):
            self.answ = multiplication(self.A.get(), self.B.get())
            self.length = len(multiplication(self.A.get(), self.B.get()))
        else:
            self.answ = multiplication(str(bin(int(self.A.get())).replace('0b', '', 1)),
                                       str(bin(int(self.B.get())).replace('0b', '', 1)))
            self.length = len(multiplication(str(bin(int(self.A.get())).replace('0b', '', 1)),
                                             str(bin(int(self.B.get())).replace('0b', '', 1))))
        self.out()

    def out(self):
        self.mult.configure(state=NORMAL)
        self.answer.configure(state=NORMAL)
        self.mult.delete(0.0, END)
        self.answer.delete(0.0, END)
        for i in range(self.length):
            self.mult.insert('end', f'{self.answ[i]} \n')
        self.answer.insert('end', "{0}".format(int(self.answ[self.length - 1])))
        self.mult.configure(state=DISABLED)
        self.answer.configure(state=DISABLED)


root = Tk()
root.title("Умножение чисел")
window = MainWindow(root)
root.resizable(False, False)
root.mainloop()
