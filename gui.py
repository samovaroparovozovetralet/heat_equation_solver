import tkinter as tk
list_1 = []
list_2 = []
list_3 = []


def show_last():
    r_0 = list_1[7]
    r_gam = list_1[8]
    disc = list_1[9]
    for i in range(int(r_0) * int(disc) + int(r_gam) * int(disc)):
        list_3.append(e_listok[i].get())
    print(list_3)
    master.quit()


def show_again():
    r_0 = list_1[7]
    r_gam = list_1[8]
    disc = list_1[9]
    for i in range(int(r_0) + int(r_gam) + 2 * int(disc)):
        list_2.append(e_list[i].get())
    print(list_2)
    f_third(r_0, r_gam, disc)


def f_third(r_0, r_gam, disc):
    r_0 = int(r_0)
    r_gam = int(r_gam)
    disc = int(disc)
    for i in range(r_0 * disc + r_gam * disc):
        e_listok.append(0)
    third = tk.Tk()
    tk.Label(third,
             text="Введіть праву частину").grid(row=0)
    for i in range(r_0):
        for j in range(disc):
            e_listok[i*j + j] = tk.Entry(third, width=30)
            e_listok[i*j + j].grid(row=i + 1, column=j)
            #list_3.append(e.get())
    tk.Label(third,
             text="Введіть праву чаcтину").grid(row=r_0 + 1)
    for i in range(r_gam):
        for j in range(disc):
            e_listok[r_0*disc + i*j + j] = tk.Entry(third, width=30)
            e_listok[r_0*disc + i*j + j].grid(row=r_0 + i + 2, column=j)
            #list_3.append(e.get())
    tk.Button(third,
              text='Quit',
              command=show_last).grid(row=r_0+r_gam+2,
                                      column=0,
                                      sticky=tk.W,
                                      pady=4)


def f_second(r_0, r_gam, disc):
    second = tk.Tk()
    r_0 = int(r_0)
    r_gam = int(r_gam)
    disc = int(disc)
    for i in range(r_0 + r_gam + 2 * disc):
        e_list.append(0)
    tk.Label(second,
             text="Введіть початкові умови").grid(row=0)
    for i in range(r_0):
        e_list[i] = tk.Entry(second, width=30)
        e_list[i].grid(row=i + 1, column=0)
        #list_2.append(e.get())
    tk.Label(second,
             text="Введіть крайові умови").grid(row=r_0 + 1)
    for i in range(r_gam):
        e_list[r_0 + i] = tk.Entry(second, width=30)
        e_list[r_0 + i].grid(row=r_0 + i + 2, column=0)
        #list_2.append(e.get())
    tk.Label(second,
             text="Введіть точки дискретизації").grid(row=r_0 + r_gam + 2)
    for i in range(disc):
        e_list[i + r_0 + r_gam] = tk.Entry(second, width=30)
        e_list[i + r_0 + r_gam].grid(row=r_0+r_gam + i + 3, column=0)
        #list_2.append(e.get())
    tk.Label(second,
             text="Введіть точки дискретизації граничних умов").grid(row=r_0 + r_gam + disc + 3)
    for i in range(disc):
        e_list[i + r_0 + r_gam + disc] = tk.Entry(second, width=30)
        e_list[i + r_0 + r_gam + disc].grid(row=disc + r_0 + r_gam + i + 4, column=0)
        #list_2.append(e.get())
    tk.Button(second,
              text='Next', command=show_again).grid(row=r_0 + r_gam + 2 * disc + 4,
                                                    column=0,
                                                    sticky=tk.W,
                                                    pady=4)


def show_entry_fields():
    for i in [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]:
        list_1.append(i.get())
    r_0 = e8.get()
    r_gam = e9.get()
    disc = e10.get()
    f_second(r_0, r_gam, disc)


master = tk.Tk()
tk.Label(master,
         text="Введіть оператор").grid(row=0)
tk.Label(master,
         text="Введіть функцію Гріна").grid(row=1)
tk.Label(master,
         text="Введіть a1").grid(row=2)
tk.Label(master,
         text="Введіть a2").grid(row=3)
tk.Label(master,
         text="Введіть b1").grid(row=4)
tk.Label(master,
         text="Введіть b2").grid(row=5)
tk.Label(master,
         text="Введіть часову область T").grid(row=6)
tk.Label(master,
         text="Введіть кількість початкових(r_0)").grid(row=7)
tk.Label(master,
         text="Введіть кількість граничних умови(r_gam)").grid(row=8)
tk.Label(master,
         text="Введіть кількість точок дискретизації(disc)").grid(row=9)

e1 = tk.Entry(master, width=50)
e2 = tk.Entry(master, width=50)
e3 = tk.Entry(master, width=50)
e4 = tk.Entry(master, width=50)
e5 = tk.Entry(master, width=50)
e6 = tk.Entry(master, width=50)
e7 = tk.Entry(master, width=50)
e8 = tk.Entry(master, width=50)
e9 = tk.Entry(master, width=50)
e10 = tk.Entry(master, width=50)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)
e8.grid(row=7, column=1)
e9.grid(row=8, column=1)
e10.grid(row=9, column=1)
e_list = []
e_listok = []

tk.Button(master,
          text='Next', command=show_entry_fields).grid(row=10,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)

tk.mainloop()