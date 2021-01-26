from tkinter import *
from tkinter import messagebox
import os
import re


def janelaRegistar():

    def registo():

        emailRegisto = str(registertxt_username.get())
        passwordRegisto = str(registertxt_password.get())
        confpassRegisto = registertxt_confpassword.get()
        linha_ficheiro = str(emailRegisto) + ";" + str(passwordRegisto) + "\n"

        if emailRegisto == "" or passwordRegisto == "" or confpassRegisto == "":
            messagebox.showerror("Campos Inválidos",
                                 "Preencha todos os campos")

        elif passwordRegisto != confpassRegisto:
            messagebox.showerror("Passwords diferentes",
                                 "As passwords são diferentes")

        elif emailRegisto:
            if re.search(regex, emailRegisto):
                oEmailExiste = False
                with open("Ficheiros\\register.txt", "a") as f: pass
                with open("Ficheiros\\register.txt", "r") as f:

                    for linha_ficheiro in f.readlines():
                        campos = linha_ficheiro.split(";")
                        if campos[0] == emailRegisto:
                            oEmailExiste = True
                            messagebox.showerror(
                                "Erro", "Esse utilizador já está registado")
                            break

                if oEmailExiste == False:
                    with open("Ficheiros\\register.txt", "a") as g:
                        print(emailRegisto)
                        print(passwordRegisto)
                        g.write(emailRegisto + ";" + passwordRegisto + "\n")

                    messagebox.showinfo("Sucesso", "O registo foi concluído com sucesso")
                    registerWindow.withdraw()
                    main_page()
            else:
                messagebox.showerror("Email Inválido", "Email Inválido")

    def voltar():

        # /-/-/-/-/-/-/-/-/-/-/-
        # Back Button
        # /-/-/-/-/-/-/-/-/-/-/-

        registerWindow.destroy()
        loginwindow.update()
        loginwindow.deiconify()

    # /-/-/-/-/-/-/-/-/-/-/-
    # Register Window
    # /-/-/-/-/-/-/-/-/-/-/-

    registerWindow = Toplevel(loginwindow)
    registerWindow.title("Register")
    registerWindow.geometry("800x600")

    loginwindow.withdraw()

    registerlbl_login = Label(
        registerWindow, text="Register", fg="red", font=("Helvetica", 30))
    registerlbl_login.place(x=330, y=80)

    registerlbl_username = Label(
        registerWindow, text="Email:", fg="red", font=("Helvetica", 12))
    registerlbl_username.place(x=270, y=200)

    registertxt_username = Entry(registerWindow,  fg="black", font=(
        "Helvetica", 10), width=35, relief="raised")
    registertxt_username.place(x=270, y=230)

    registerlbl_password = Label(
        registerWindow, text="Password:", fg="red", font=("Helvetica", 12))
    registerlbl_password.place(x=270, y=270)

    registertxt_password = Entry(registerWindow, fg="black", font=(
        "Helvetica", 10), show="*", width=35, relief="raised")
    registertxt_password.place(x=270, y=300)

    registerlbl_confpassword = Label(
        registerWindow, text="Confirm Password:", fg="red", font=("Helvetica", 12))
    registerlbl_confpassword.place(x=270, y=340)

    registertxt_confpassword = Entry(registerWindow, fg="black", font=(
        "Helvetica", 10), show="*", width=35, relief="raised")
    registertxt_confpassword.place(x=270, y=370)

    registarButtonRegister = Button(registerWindow, text="Register", width="10", font=(
        "Helvetica", 12), fg="red", command=registo)
    registarButtonRegister.place(x=420, y=400)

    menuButton = Button(registerWindow, text="Back", width="10", font=(
        "Helvetica", 12), fg="red", command=voltar)
    menuButton.place(x=270, y=400)


def main_page():

    loginwindow.withdraw()

    window = Toplevel()
    window.geometry("800x600")
    window.title("Home Page")

    # MENU BAR
    barra_Menu = Menu(window)

    categorias_menu = Menu(barra_Menu, tearoff=0)

    barra_Menu.add_cascade(label="Categorias", menu=categorias_menu)
    barra_Menu.add_command(label="Sair", command=window.quit)

    with open("Ficheiros\\categorias.txt", "r") as f:
        for linha_ficheiro in f.readlines():
            campos = linha_ficheiro.strip().split(";")
            categorias_menu.add_command(label=campos[0], command=campos[1])

    window.configure(menu=barra_Menu)

    # CONTAINER

    panel1 = PanedWindow(window, width=200, height=100, bd="2", relief="sunken")
    panel1.pack(fill=Y, side=RIGHT)

    canvas1 = Canvas(panel1, width=150, height=100, bd="2", relief="sunken")
    canvas1.pack(side=TOP)

    

    window.mainloop()


def admin_mode():

    def recipe_page():

        def back():

            # /-/-/-/-/-/-/-/-/-/-/-
            # Back button
            # /-/-/-/-/-/-/-/-/-/-/-

            top_window.destroy()
            window.update()
            window.deiconify()

        top_window = Toplevel()
        top_window.geometry("800x600")
        top_window.title("Which category ?")

        frame2 = Frame(top_window)

        # /-/-/-/-/-/-/-/-/-/-/-
        # Back button place
        # /-/-/-/-/-/-/-/-/-/-/-

        back_button = Button(top_window, text="Back", command=back)
        back_button.place(x=750, y=7)

        frame2.place(relx=0.5, rely=0.5, anchor=CENTER)

    def user():

        window.withdraw()

        def back():

            # /-/-/-/-/-/-/-/-/-/-/-
            # Back button
            # /-/-/-/-/-/-/-/-/-/-/-

            user.destroy()
            window.update()
            window.deiconify()

        window.withdraw()

        user = Toplevel()
        user.geometry("800x600")
        user.title("User Page")

        canvas1 = Canvas(user, width=200, height=200, bd="3", relief="sunken")
        canvas1.place(x=330, y=150)

        panel1 = PanedWindow(user, width=100, height=100,
                             bd="3", relief="sunken")
        panel1.pack(fill=X, side=TOP)

        back_button = Button(panel1, text="Back", command=back)
        back_button.pack(side=LEFT, padx=10, pady=10)

        user.mainloop()

    loginwindow.withdraw()

    window = Toplevel()
    window.geometry("800x600")
    window.title("Home Page")

    panel1 = PanedWindow(window, width=100, height=100,
                         bd="3", relief="sunken")
    panel1.pack(fill=X, side=TOP)

    user_button = Button(panel1, text="Profile",
                         width=6, height=2, command=user)
    user_button.pack(side=RIGHT, padx=10, pady=10)

    window.mainloop()


def login():

    isUserRegisted = False
    isPassCorrect = False

    user = str(txt_username.get())
    password = str(txt_password.get())

    if user == "admin@gmail.com" and password == "admin123":
        admin_mode()

    else:
        if user == "" or password == "":
            messagebox.showerror("Campos inválidos",
                                 "Preencha todos os campos")
        elif re.search(regex, user):
            with open("Ficheiros\\register.txt", "r") as f:
                for linha_ficheiro in f.readlines():
                    campos = linha_ficheiro.strip().split(";")

                    if campos[0] == user:
                        isUserRegisted = True

                    if campos[1] == password:
                        isPassCorrect = True

                if isUserRegisted == False:
                    messagebox.showerror("Erro", "Utilizador não registado")
                elif isPassCorrect == False:
                    messagebox.showerror(
                        "Erro", "Password incorreta, tente novamente")
                elif isUserRegisted == True and isPassCorrect == True:
                    main_page()
                    loginwindow.withdraw()

        else:
            messagebox.showerror("Email Inválido", "Email Inválido")


loginwindow = Tk()  # invoca classe tk, cria a "main window"
loginwindow.geometry("800x600")
loginwindow.title("Projeto de AED")

original_frame = Frame(loginwindow)
loginwindow.configure(bg="#DBE2AC")

lbl_login = Label(loginwindow, text="Login", fg="red", font=("Helvetica", 30))
lbl_login.place(x=330, y=80)

lbl_username = Label(loginwindow, text="Email:",
                     fg="red", font=("Helvetica", 12))
lbl_username.place(x=270, y=200)

txt_username = Entry(loginwindow,  fg="black", font=(
    "Helvetica", 10), width=35, relief="raised")
txt_username.place(x=270, y=230)

lbl_password = Label(loginwindow, text="Password:",
                     fg="red", font=("Helvetica", 12))
lbl_password.place(x=270, y=270)

txt_password = Entry(loginwindow, fg="black", font=(
    "Helvetica", 10), show="*", width=35, relief="raised")
txt_password.place(x=270, y=300)


loginButton = Button(loginwindow, text="Login", width="10",
                     font=("Helvetica", 12), fg="red", command=login)
loginButton.place(x=420, y=400)

registarButton = Button(loginwindow, text="Register", width="10", font=(
    "Helvetica", 12), fg="red", command=janelaRegistar)
registarButton.place(x=270, y=400)

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

loginwindow.mainloop()