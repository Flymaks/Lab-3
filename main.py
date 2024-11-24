import tkinter as tk
from tkinter import messagebox
import random


def windows():
    def password():  # Generating a random key
        block1 = ""
        block2 = ""
        block3 = ""
        for i in range(5):
            list1 = []
            for i in range(48, 58):
                list1.append(int(i))
            for i in range(65, 91):
                list1.append(int(i))
            a = random.choice(list1)
            block1 += chr(a)
        for i in range(5):
            s = ord(f"{block1[i]}")
            s = upper(s)
            block2 += chr(s)
        for i in range(5):
            s = ord(f"{block1[i]}")
            s = lower(s)
            block3 += chr(s)
        password = block1 + "-" + block2 + "-" + block3
        return password

    def upper(s):  # key for the second block
        s += 3
        if s > 90:
            s -= 91 - 48
        elif s > 57 and s < 65:
            s += 65 - 58
        return s

    def lower(s):  # key for the third block
        s -= 5
        if s < 48:
            s += 91 - 48
        elif s > 57 and s < 65:
            s -= 65 - 58
        return s

    def close():
        window.destroy()

    def some_callback(event): 
        input1.delete(0, "end")
        return None

    def key():
        input1.delete(0, "end")
        password1 = password()
        input1.insert(0, f"{password1}")
        return None

    def enter():
        res = 1
        n = input1.get()
        if len(n) != 17 or n[5] != "-" or n[11] != "-":
            res = 0
        else:
            for i in range(5):
                if not (47 < ord(n[i]) < 58 or  64 < ord(n[i]) < 91):
                    res = 0
                if upper(ord(n[i])) != ord(n[i + 6]) or lower(ord(n[i])) != ord(n[i + 12]):
                    res = 0
        if res == 0:
            tk.messagebox.showwarning('Неверный ключ!', 'Попробуйте ещё раз')
            return None
        else:
            lbl_bg = tk.Label(window, image=img)
            lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
            frame1 = tk.Frame(window)
            frame1.place(relx=0.5, rely=0.5, anchor='center')

            lbl_heading = tk.Label(frame1, text="Добро пожаловать", font=('Arial', 30))
            lbl_heading.grid(column=1, row=0, padx=10, pady=15)

            btn_exit = tk.Button(frame1, text='Cancel', command=close)
            btn_exit.grid(column=0, row=3, padx=10, pady=15)
            btn_ret = tk.Button(frame1, text='Return', command=main)
            btn_ret.grid(column=2, row=3, padx=10, pady=15)
            return None

    window = tk.Tk()
    window.geometry('576x360')
    img = tk.PhotoImage(file='gradient.png')
    bg_img = tk.PhotoImage(file='bg_pic.png')

    def main():
        lbl_bg = tk.Label(window, image=bg_img)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        global input1
        frame = tk.Frame(window)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        heading = tk.Label(frame, text='Введите ключ доступа:', font=('Arial', 30))
        heading.grid(column=1, row=0, padx=10, pady=15)

        input1 = tk.Entry(frame, width=30)
        input1.insert(0, 'XXXXX-XXXXX-XXXXX')
        input1.bind("<Button-1>", some_callback)
        input1.grid(column=1, row=1, padx=10, pady=15)

        lbl_text = tk.Button(frame, text='Сгенерировать ключ', command=key)
        lbl_text.grid(column=1, row=2)

        btn_ent = tk.Button(frame, text='Войти', command=enter)
        btn_ent.grid(column=2, row=3, padx=10, pady=15)
        btn_exit = tk.Button(frame, text='Cancel', command=close)
        btn_exit.grid(column=0, row=3, padx=10, pady=15)

        window.mainloop()
        return None

    main()


if __name__ == "__main__":
    windows()