from tkinter import *
from tkinter import messagebox
import os
import re


def janelaRegistar():

    def registo():

        emailRegisto = registertxt_username.get()
        passwordRegisto = registertxt_password.get()
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
                with open("Ficheiros\\register.txt", "r") as f:

                    for linha_ficheiro in f.readlines():
                        campos = linha_ficheiro.split(";")
                        if campos[0] == emailRegisto:
                            oEmailExiste = True
                            messagebox.showerror(
                                "Erro", "Esse utilizador já está registado")
                            break

                if oEmailExiste == False:
                    with open("Ficheiros\\register.txt", "a") as f:
                        f.write(emailRegisto + ";" + passwordRegisto + "\n")
                        messagebox.showinfo(
                            "Sucesso", "O registo foi concluído com sucesso")
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

    def recipe_page():

        def back():

            # /-/-/-/-/-/-/-/-/-/-/-
            # Back button
            # /-/-/-/-/-/-/-/-/-/-/-

            top_window.destroy()
            window.update()
            window.deiconify()

        window.withdraw()

        top_window = Toplevel()
        top_window.geometry("800x600")
        top_window.title("Which category ?")

        frame2 = Frame(top_window)

        # /-/-/-/-/-/-/-/-/-/-/-
        # Back button place
        # /-/-/-/-/-/-/-/-/-/-/-

        back_button = Button(top_window, text="Back", command=back)
        back_button.place(x=750, y=7)

        # /-/-/-/-/-/-/-/-/-/-/-
        # Categorias
        # /-/-/-/-/-/-/-/-/-/-/-

        chicken_btn = Button(frame2, text="Chicken", width=10, height=3)
        chicken_btn.grid(padx=15, pady=15)

        fish_btn = Button(frame2, text="Fish", width=10, height=3)
        fish_btn.grid(row=1, padx=15, pady=15)

        soup_btn = Button(frame2, text="Soup", width=10, height=3)
        soup_btn.grid(row=2, padx=15, pady=15)

        salad_btn = Button(frame2, text="Salad", width=10, height=3)
        salad_btn.grid(row=0, column=1, padx=15, pady=15)

        meat_btn = Button(frame2, text="Meat", width=10, height=3)
        meat_btn.grid(row=1, column=1, padx=15, pady=15)

        vegetarian_btn = Button(frame2, text="Vegetarian", width=10, height=3)
        vegetarian_btn.grid(row=2, column=1, padx=15, pady=15)

        snacks_btn = Button(frame2, text="Snacks", width=10, height=3)
        snacks_btn.grid(row=0, column=2, padx=15, pady=15)

        cakes_btn = Button(frame2, text="Cakes", width=10, height=3)
        cakes_btn.grid(row=1, column=2, padx=15, pady=15)

        beverages_btn = Button(frame2, text="Beverages", width=10, height=3)
        beverages_btn.grid(row=2, column=2, padx=15, pady=15)

        sauces_btn = Button(frame2, text="Sauces", width=10, height=3)
        sauces_btn.grid(row=0, column=3, padx=15, pady=15)

        desserts_btn = Button(frame2, text="Desserts", width=10, height=3)
        desserts_btn.grid(row=1, column=3, padx=15, pady=15)

        appetizers_btn = Button(frame2, text="Appetizers", width=10, height=3)
        appetizers_btn.grid(row=2, column=3, padx=15, pady=15)

        pasta_btn = Button(frame2, text="Pasta", width=10, height=3)
        pasta_btn.grid(row=0, column=4, padx=15, pady=15)

        other_btn = Button(frame2, text="Other", width=10, height=3)
        other_btn.grid(row=1, column=4, padx=15, pady=15)

        frame2.place(relx=0.5, rely=0.5, anchor=CENTER)

    loginwindow.withdraw()

    # /-/-/-/-/-/-/-/-/-/-/-
    # Main Page
    # /-/-/-/-/-/-/-/-/-/-/-

    window = Toplevel()
    window.geometry("800x600")
    window.title("Home Page")

    frame = Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    chicken_btn = Button(frame, text="Chicken", width=10, height=3)
    chicken_btn.grid(padx=15, pady=15)

    fish_btn = Button(frame, text="Fish", width=10, height=3)
    fish_btn.grid(row=1, padx=15, pady=15)

    soup_btn = Button(frame, text="Soup", width=10, height=3)
    soup_btn.grid(row=2, padx=15, pady=15)

    salad_btn = Button(frame, text="Salad", width=10, height=3)
    salad_btn.grid(row=0, column=1, padx=15, pady=15)

    meat_btn = Button(frame, text="Meat", width=10, height=3)
    meat_btn.grid(row=1, column=1, padx=15, pady=15)

    vegetarian_btn = Button(frame, text="Vegetarian", width=10, height=3)
    vegetarian_btn.grid(row=2, column=1, padx=15, pady=15)

    snacks_btn = Button(frame, text="Snacks", width=10, height=3)
    snacks_btn.grid(row=0, column=2, padx=15, pady=15)

    cakes_btn = Button(frame, text="Cakes", width=10, height=3)
    cakes_btn.grid(row=1, column=2, padx=15, pady=15)

    beverages_btn = Button(frame, text="Beverages", width=10, height=3)
    beverages_btn.grid(row=2, column=2, padx=15, pady=15)

    sauces_btn = Button(frame, text="Sauces", width=10, height=3)
    sauces_btn.grid(row=0, column=3, padx=15, pady=15)

    desserts_btn = Button(frame, text="Desserts", width=10, height=3)
    desserts_btn.grid(row=1, column=3, padx=15, pady=15)

    appetizers_btn = Button(frame, text="Appetizers", width=10, height=3)
    appetizers_btn.grid(row=2, column=3, padx=15, pady=15)

    pasta_btn = Button(frame, text="Pasta", width=10, height=3)
    pasta_btn.grid(row=0, column=4, padx=15, pady=15)

    other_btn = Button(frame, text="Other", width=10, height=3)
    other_btn.grid(row=1, column=4, padx=15, pady=15)

    add_new_recipe = Button(window, text="Add new recipe", command=recipe_page)
    add_new_recipe.pack(side=TOP, pady=10)


#/-/-/-/-/-/-/-/-/-/-/-#
# Login Page
#/-/-/-/-/-/-/-/-/-/-/-#



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

        # /-/-/-/-/-/-/-/-/-/-/-
        # Categorias
        # /-/-/-/-/-/-/-/-/-/-/-

        chicken_btn = Button(frame2, text="Chicken", width=10, height=3)
        chicken_btn.grid(padx=15, pady=15)

        fish_btn = Button(frame2, text="Fish", width=10, height=3)
        fish_btn.grid(row=1, padx=15, pady=15)

        soup_btn = Button(frame2, text="Soup", width=10, height=3)
        soup_btn.grid(row=2, padx=15, pady=15)

        salad_btn = Button(frame2, text="Salad", width=10, height=3)
        salad_btn.grid(row=0, column=1, padx=15, pady=15)

        meat_btn = Button(frame2, text="Meat", width=10, height=3)
        meat_btn.grid(row=1, column=1, padx=15, pady=15)

        vegetarian_btn = Button(frame2, text="Vegetarian", width=10, height=3)
        vegetarian_btn.grid(row=2, column=1, padx=15, pady=15)

        snacks_btn = Button(frame2, text="Snacks", width=10, height=3)
        snacks_btn.grid(row=0, column=2, padx=15, pady=15)

        cakes_btn = Button(frame2, text="Cakes", width=10, height=3)
        cakes_btn.grid(row=1, column=2, padx=15, pady=15)

        beverages_btn = Button(frame2, text="Beverages", width=10, height=3)
        beverages_btn.grid(row=2, column=2, padx=15, pady=15)

        sauces_btn = Button(frame2, text="Sauces", width=10, height=3)
        sauces_btn.grid(row=0, column=3, padx=15, pady=15)

        desserts_btn = Button(frame2, text="Desserts", width=10, height=3)
        desserts_btn.grid(row=1, column=3, padx=15, pady=15)

        appetizers_btn = Button(frame2, text="Appetizers", width=10, height=3)
        appetizers_btn.grid(row=2, column=3, padx=15, pady=15)

        pasta_btn = Button(frame2, text="Pasta", width=10, height=3)
        pasta_btn.grid(row=0, column=4, padx=15, pady=15)

        other_btn = Button(frame2, text="Other", width=10, height=3)
        other_btn.grid(row=1, column=4, padx=15, pady=15)

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

        canvas1 = Canvas(user, width= 200, height=200, bd="3", relief="sunken")
        canvas1.place(x = 330, y = 150)

        panel1 = PanedWindow(user, width=100, height=100, bd="3", relief="sunken")
        panel1.pack( fill= X, side=TOP)

        back_button = Button(panel1, text="Back", command=back)
        back_button.pack(side=LEFT,padx= 10, pady= 10)


        user.mainloop()


    

    
    loginwindow.withdraw()

    window = Toplevel()
    window.geometry("800x600")
    window.title("Home Page")


    panel1 = PanedWindow(window, width=100, height=100, bd="3", relief="sunken")
    panel1.pack( fill= X, side=TOP)

    user_button = Button(panel1, text="Profile",width=6, height=2 , command= user)
    user_button.pack(side=RIGHT,padx= 10, pady= 10)

    frame = Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    chicken_btn = Button(frame, text="Chicken", width=10, height=3)
    chicken_btn.grid(padx=15, pady=15)

    fish_btn = Button(frame, text="Fish", width=10, height=3)
    fish_btn.grid(row=1, padx=15, pady=15)

    soup_btn = Button(frame, text="Soup", width=10, height=3)
    soup_btn.grid(row=2, padx=15, pady=15)

    salad_btn = Button(frame, text="Salad", width=10, height=3)
    salad_btn.grid(row=0, column=1, padx=15, pady=15)

    meat_btn = Button(frame, text="Meat", width=10, height=3)
    meat_btn.grid(row=1, column=1, padx=15, pady=15)

    vegetarian_btn = Button(frame, text="Vegetarian", width=10, height=3)
    vegetarian_btn.grid(row=2, column=1, padx=15, pady=15)

    snacks_btn = Button(frame, text="Snacks", width=10, height=3)
    snacks_btn.grid(row=0, column=2, padx=15, pady=15)

    cakes_btn = Button(frame, text="Cakes", width=10, height=3)
    cakes_btn.grid(row=1, column=2, padx=15, pady=15)

    beverages_btn = Button(frame, text="Beverages", width=10, height=3)
    beverages_btn.grid(row=2, column=2, padx=15, pady=15)

    sauces_btn = Button(frame, text="Sauces", width=10, height=3)
    sauces_btn.grid(row=0, column=3, padx=15, pady=15)

    desserts_btn = Button(frame, text="Desserts", width=10, height=3)
    desserts_btn.grid(row=1, column=3, padx=15, pady=15)

    appetizers_btn = Button(frame, text="Appetizers", width=10, height=3)
    appetizers_btn.grid(row=2, column=3, padx=15, pady=15)

    pasta_btn = Button(frame, text="Pasta", width=10, height=3)
    pasta_btn.grid(row=0, column=4, padx=15, pady=15)

    other_btn = Button(frame, text="Other", width=10, height=3)
    other_btn.grid(row=1, column=4, padx=15, pady=15)

    add_new_recipe = Button(window, text="Add new recipe", command=recipe_page)
    add_new_recipe.pack(side=TOP, pady=10)

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
            messagebox.showerror("Campos inválidos","Preencha todos os campos")
        elif re.search(regex, user):
            with open("Ficheiros\\register.txt", "r") as f:
                for linha_ficheiro in f.readlines():
                    campos = linha_ficheiro.strip().split(";")
                    
                    if campos[0] == user:
                        isUserRegisted = True

                    if campos[1] == password:
                        isPassCorrect = True

                if isUserRegisted == False:
                    messagebox.showerror("Erro","Utilizador não registado")
                elif isPassCorrect == False:
                    messagebox.showerror("Erro","Password incorreta, tente novamente")
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

lbl_username = Label(loginwindow, text="Email:",fg="red", font=("Helvetica", 12))
lbl_username.place(x=270, y=200)

txt_username = Entry(loginwindow,  fg="black", font=("Helvetica", 10), width=35, relief="raised")
txt_username.place(x=270, y=230)

lbl_password = Label(loginwindow, text="Password:",fg="red", font=("Helvetica", 12))
lbl_password.place(x=270, y=270)

txt_password = Entry(loginwindow, fg="black", font=("Helvetica", 10), show="*", width=35, relief="raised")
txt_password.place(x=270, y=300)


loginButton = Button(loginwindow, text="Login", width="10",font=("Helvetica", 12), fg="red", command=login)
loginButton.place(x=420, y=400)

registarButton = Button(loginwindow, text="Register", width="10", font=("Helvetica", 12), fg="red", command=janelaRegistar)
registarButton.place(x=270, y=400)

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

loginwindow.mainloop()


