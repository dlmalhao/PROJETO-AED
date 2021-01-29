from tkinter import *
from tkinter import messagebox
import os
import re
from tkinter import filedialog
from PIL import ImageTk, Image
import tkinter.font as font
from functools import partial
from tkinter.ttk import Combobox


def janelaRegistar():
    global imagem

    def registo():
        usernameRegisto = str(registertxt_usernamePerfil.get())
        emailRegisto = str(registertxt_username.get())
        passwordRegisto = str(registertxt_password.get())
        confpassRegisto = str(registertxt_confpassword.get())
        linha_ficheiro = usernameRegisto + ";" + \
            emailRegisto + ";" + passwordRegisto + "\n"

        if emailRegisto == "" or passwordRegisto == "" or confpassRegisto == "" or usernameRegisto == "":
            messagebox.showerror("Campos Inválidos",
                                 "Preencha todos os campos")

        elif passwordRegisto != confpassRegisto:
            messagebox.showerror("Passwords diferentes",
                                 "As passwords são diferentes")

        elif emailRegisto:
            if re.search(regex, emailRegisto):
                oEmailExiste = False
                with open("Ficheiros\\register.txt", "a") as f:
                    pass
                with open("Ficheiros\\register.txt", "r") as f:

                    for linha_ficheiro in f.readlines():
                        campos = linha_ficheiro.strip().split(";")
                        if campos[0] == "":
                            break
                        if campos[1] == emailRegisto:
                            oEmailExiste = True
                            messagebox.showerror(
                                "Erro", "Esse utilizador já está registado")
                            break

                if oEmailExiste == False:
                    with open("Ficheiros\\register.txt", "a") as g:
                        g.write(usernameRegisto + ";" + emailRegisto +
                                ";" + passwordRegisto + "\n")

                    messagebox.showinfo(
                        "Sucesso", "O registo foi concluído com sucesso")
                    registerWindow.withdraw()
                    guardar_setup()
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
        loginwindow.resizable(False, False)

    def escolhe_imagem():
        global imagem
        imagem = filedialog.askopenfilename(title="Select file", filetypes=(
            ("jpg files", ".jpg"), ("png files", ".png"), ("all files", ".")))
        global img
        img = ImageTk.PhotoImage(file=imagem)
        canvas1.itemconfig(img_id, image=img)

    # Guarda dados no ficheiro perfil.txt
    def guardar_setup():
        with open("Ficheiros//perfil.txt", "w")as f:
            f.write(imagem)
        global img
        # atualiza canvas de imagem de perfil, com imagem guardada em ficheiro
        img = ImageTk.PhotoImage(file=imagem)
        canvas1.itemconfig(img_id, image=img)

    # /-/-/-/-/-/-/-/-/-/-/-
    # Register Window
    # /-/-/-/-/-/-/-/-/-/-/-

    registerWindow = Toplevel(loginwindow)
    registerWindow.title("Register")
    registerWindow.geometry("800x600")
    registerWindow.resizable(False, False)
    registerWindow.configure(bg="#D1BEA6")

    # wallpaper registo
    # wall2=ImageTk.PhotoImage(file="Images/wallpaper6.jpg")
    #wallpaper2=Label(registerWindow, image=wall)
    #wallpaper2.place(x=0, y=0,relwidth=1, relheight=1)

    loginwindow.withdraw()

    registerlbl_usernamePerfil = Label(
        registerWindow, text="Username:", fg="black", bg="#D1BEA6", font=("Microsoft YaHei", 12))
    registerlbl_usernamePerfil.place(x=270, y=150)

    registertxt_usernamePerfil = Entry(registerWindow,  fg="black", font=(
        "Microsoft YaHei", 10), width=35, relief="raised")
    registertxt_usernamePerfil.place(x=270, y=180)

    registerlbl_login = Label(
        registerWindow, text="Register", fg="black", bg="#D1BEA6", font=("Microsoft YaHei", 30))
    registerlbl_login.place(x=330, y=80)

    registerlbl_username = Label(
        registerWindow, text="Email:", fg="black", bg="#D1BEA6", font=("Microsoft YaHei", 12))
    registerlbl_username.place(x=270, y=220)

    registertxt_username = Entry(registerWindow,  fg="black", font=(
        "Microsoft YaHei", 10), width=35, relief="raised")
    registertxt_username.place(x=270, y=250)

    registerlbl_password = Label(
        registerWindow, text="Password:", fg="black", bg="#D1BEA6", font=("Microsoft YaHei", 12))
    registerlbl_password.place(x=270, y=290)

    registertxt_password = Entry(registerWindow, fg="black", font=(
        "Microsoft YaHei", 10), show="*", width=35, relief="raised")
    registertxt_password.place(x=270, y=320)

    registerlbl_confpassword = Label(
        registerWindow, text="Confirm Password:", fg="black", bg="#D1BEA6", font=("Microsoft YaHei", 12))
    registerlbl_confpassword.place(x=270, y=360)

    registertxt_confpassword = Entry(registerWindow, fg="black", font=(
        "Microsoft YaHei", 10), show="*", width=35, relief="raised")
    registertxt_confpassword.place(x=270, y=390)

    registarButtonRegister = Button(registerWindow, text="Register", width="10", font=(
        "Microsoft YaHei", 12), fg="black", command=registo)
    registarButtonRegister.place(x=430, y=440)

    menuButton = Button(registerWindow, text="Back", width="10", font=(
        "Microsoft YaHei", 12), fg="black", command=voltar)
    menuButton.place(x=280, y=440)

    canvas1 = Canvas(registerWindow, width=100,
                     height=100, bd="2", relief="sunken")
    canvas1.place(x=20, y=20)

    img = ImageTk.PhotoImage(file="avatar0.jpg")
    img_id = canvas1.create_image(0, 0, anchor="nw", image=img)

    button_imagem = Button(registerWindow, text="Selecionar \nFoto de Perfil", width="14", font=(
        "Helvetica", 12), fg="black", command=escolhe_imagem)
    button_imagem.place(x=18, y=230)





def main_page():


    def addnewrecipe ():

        def escolhe_imagem(canvas2):
            
            imagem=filedialog.askopenfilename(title="Select file", filetypes=(("jpg files",".jpg"),("png files",".png"),("all files",".")))
            if imagem:
                canvas2.img = ImageTk.PhotoImage(Image.open(imagem).resize((220, 300)))
                print(canvas2.img)
                canvas2.create_image(0,0,anchor = "nw", image = canvas2.img)

        window.withdraw()
        
        newrecipe_window = Toplevel()
        newrecipe_window.geometry("800x600")
        newrecipe_window.title("Adicionar receita")
        newrecipe_window.resizable(False, False)

        newrecipe_window.configure(bg="#D1BEA6")

        panel1 = PanedWindow(newrecipe_window, width=400, height = 500, bd="2", relief="sunken")
        panel1.place(x = 60, y = 50)
        
        header = Label(panel1, text="Adicionar receita", fg="black", font=("Microsoft YaHei", 12))
        header.place(x = 140, y = 10)

        titulo = Entry(panel1, width = 35)
        titulo.place(x = 100, y = 100)
        titulo_label = Label(panel1, text="Título", fg="black", font=("Microsoft YaHei", 10))
        titulo_label.place(x=30, y=95)

        preparacao = Text(panel1, width = 30, height = 12, wrap = "word")
        preparacao.place(x = 100, y = 150)
        preparacao_label = Label(panel1, text="Modo \n de \n preparação", fg="black", font=("Microsoft YaHei", 10))
        preparacao_label.place(x=15, y=140)

        tempo = Entry(panel1, width = 35)
        tempo.place(x = 100, y = 400)
        tempo_label = Label(panel1, text="Tempo \n estimado", fg="black", font=("Microsoft YaHei", 10))
        tempo_label.place(x=15, y=390)


        #CANVAS PARA FOTO
        canvas2 = Canvas(newrecipe_window, width = 220, height = 300, bd ="2", relief = "sunken")
        canvas2.place(x = 520, y = 50)

        btn3 = Button(newrecipe_window, text = "Selecionar imagem", command = partial(escolhe_imagem, canvas2),font=("Microsoft YaHei", 10), bg="#D1BEA6")
        btn3.place(x =575, y = 370)


        #COMBO BOX
        lista_cb = []
        with open("Ficheiros//categorias.txt","r") as f:
            for i in f.readlines() :
                campos = i.strip().split(";")
                lista_cb.append(campos[0])

        combo_box = Combobox(newrecipe_window, values = lista_cb)
        combo_box.place(x = 560, y = 420)

        label_cb = Label(newrecipe_window, text = "Escolher\ncategoria", font=("Microsoft YaHei", 10), bg="#D1BEA6")
        label_cb.place(x = 485, y = 408)


        #LIST BOX   
        lbox = Listbox(newrecipe_window, height = 4, width = 30)
        lbox.place(x = 530, y = 500 )


        def lbox_add ():
            item = combo_box.get()
            if item:
                if lbox.size() == 0:
                    lbox.insert(END,item)
                else:
                    existemIguais = False
                    for value in lbox.get(0,END):
                        if value == item:
                            existemIguais = True
                            break
                    if existemIguais == False:
                        lbox.insert(END,item)
                    else:
                        messagebox.showerror("Erro","Essa categoria já está inserida")

            
                
        lbox_btn = Button(newrecipe_window, text = "Adicionar", font=("Microsoft YaHei", 10), bg="#D1BEA6", command = lbox_add)
        lbox_btn.place(x = 580, y = 460)


        newrecipe_window.mainloop()



    # def escolhe_imagem():
    #imagem=filedialog.askopenfilename(title="Select file", filetypes=(("jpg files",".jpg"),("png files",".png"),("all files",".")))
    #global img
    #img = ImageTk.PhotoImage(file = imagem)
    #canvas1.itemconfig(img_id, image=img)

    loginwindow.withdraw()

    window = Toplevel()
    window.geometry("800x600")
    window.title("Pagina principal")

    window.resizable(False, False)
    window.configure(bg="#D1BEA6")

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

    panel1 = PanedWindow(window, width=200, height=105,
                         bd="2", relief="sunken")
    panel1.pack(fill=Y, side=RIGHT)

    canvas1 = Canvas(panel1, width=100, height=100, bd="2", relief="sunken")
    canvas1.pack(side=TOP)

    panel2 = PanedWindow(window, width=400, height=500,
                         bd="2", relief="sunken")
    panel2.place(x=100, y=50)
    

    # BUTTON ADD NEW RECIPE

    btn_header = Label(panel2, text="Adicionar receita",
                       fg="black", font=("Microsoft YaHei", 12))
    btn_header.place(x=140, y=10)

    btn_add_new_recipe = Button(
        panel2, text="+", width=4, height=1, font=("Microsoft YaHei", 20), command=addnewrecipe)
    btn_add_new_recipe.place(x=160, y=50)

    with open("Ficheiros\\perfil.txt", "r")as f:
        campos2 = f.readline()
    img10 = campos2.replace("/", "//")
    img = ImageTk.PhotoImage(file=img10)
    img_id = canvas1.create_image(0, 0, anchor="nw", image=img)

    window.mainloop()




def admin_mode():

    def addnewrecipe ():

        def escolhe_imagem(canvas2):
            
            imagem=filedialog.askopenfilename(title="Select file", filetypes=(("jpg files",".jpg"),("png files",".png"),("all files",".")))
            if imagem:
                canvas2.img = ImageTk.PhotoImage(Image.open(imagem).resize((220, 300)))
                print(canvas2.img)
                canvas2.create_image(0,0,anchor = "nw", image = canvas2.img)

        window.withdraw()
        
        newrecipe_window = Toplevel()
        newrecipe_window.geometry("800x600")
        newrecipe_window.title("Adicionar receita")
        newrecipe_window.resizable(False, False)

        newrecipe_window.configure(bg="#D1BEA6")

        panel1 = PanedWindow(newrecipe_window, width=400, height = 500, bd="2", relief="sunken")
        panel1.place(x = 60, y = 50)
        
        header = Label(panel1, text="Adicionar receita", fg="black", font=("Microsoft YaHei", 12))
        header.place(x = 140, y = 10)

        titulo = Entry(panel1, width = 35)
        titulo.place(x = 100, y = 100)
        titulo_label = Label(panel1, text="Título", fg="black", font=("Microsoft YaHei", 10))
        titulo_label.place(x=30, y=95)

        preparacao = Text(panel1, width = 30, height = 12, wrap = "word")
        preparacao.place(x = 100, y = 150)
        preparacao_label = Label(panel1, text="Modo \n de \n preparação", fg="black", font=("Microsoft YaHei", 10))
        preparacao_label.place(x=15, y=140)

        tempo = Entry(panel1, width = 35)
        tempo.place(x = 100, y = 400)
        tempo_label = Label(panel1, text="Tempo \n estimado", fg="black", font=("Microsoft YaHei", 10))
        tempo_label.place(x=15, y=390)


        #CANVAS PARA FOTO
        canvas2 = Canvas(newrecipe_window, width = 220, height = 300, bd ="2", relief = "sunken")
        canvas2.place(x = 520, y = 50)

        btn3 = Button(newrecipe_window, text = "Selecionar imagem", command = partial(escolhe_imagem, canvas2),font=("Microsoft YaHei", 10), bg="#D1BEA6")
        btn3.place(x =575, y = 370)


        #COMBO BOX
        lista_cb = []
        with open("Ficheiros//categorias.txt","r") as f:
            for i in f.readlines() :
                campos = i.strip().split(";")
                lista_cb.append(campos[0])

        combo_box = Combobox(newrecipe_window, values = lista_cb)
        combo_box.place(x = 560, y = 420)

        label_cb = Label(newrecipe_window, text = "Escolher\ncategoria", font=("Microsoft YaHei", 10), bg="#D1BEA6")
        label_cb.place(x = 485, y = 408)


        #LIST BOX   
        lbox = Listbox(newrecipe_window, height = 4, width = 30)
        lbox.place(x = 530, y = 500 )


        def lbox_add ():
            item = combo_box.get()
            if item:
                if lbox.size() == 0:
                    lbox.insert(END,item)
                else:
                    existemIguais = False
                    for value in lbox.get(0,END):
                        if value == item:
                            existemIguais = True
                            break
                    if existemIguais == False:
                        lbox.insert(END,item)
                    else:
                        messagebox.showerror("Erro","Essa categoria já está inserida")

            
                
        lbox_btn = Button(newrecipe_window, text = "Adicionar", font=("Microsoft YaHei", 10), bg="#D1BEA6", command = lbox_add)
        lbox_btn.place(x = 580, y = 460)


        newrecipe_window.mainloop()


    def janela_adicionar_categoria():

        def adicionar_categoria():

            categoriaExiste = True
            input_categoria = str(entry_titulo.get())
            with open("Ficheiros\\register.txt", "a") as f:
                pass
            with open("Ficheiros\\categorias.txt","r") as f:
                for item in f.readlines():
                    campos = item.strip().split(";")
                    if not campos[0] == input_categoria:
                        categoriaExiste = False
                        break
                if categoriaExiste == False:
                    f.write(input_categoria + ";" + input_categoria + "()" + "\n")
                    messagebox.showinfo("Receita","Receita adicionada com sucesso")
                else:
                    messagebox.showerror("Erro","A categoria já existe")
        

        miniwindow = Toplevel()
        miniwindow.geometry("400x300")
        miniwindow.title("Adicionar categoria")
        miniwindow.resizable(False, False)
        miniwindow.configure(bg="#D1BEA6")
        
        label_titulo = Label(miniwindow, text = "Categoria", font=("Microsoft YaHei", 12), bg="#D1BEA6")
        label_titulo.place(x = 160, y = 50)

        entry_titulo = Entry(miniwindow, font=("Microsoft YaHei", 10))
        entry_titulo.place(x = 115, y = 90)

        btn_titulo = Button(miniwindow, text = "Adicionar", font=("Microsoft YaHei", 12), bg="#D1BEA6", command = adicionar_categoria)
        btn_titulo.place(x = 155, y = 130)

        miniwindow.mainloop()


    # def escolhe_imagem():
    #imagem=filedialog.askopenfilename(title="Select file", filetypes=(("jpg files",".jpg"),("png files",".png"),("all files",".")))
    #global img
    #img = ImageTk.PhotoImage(file = imagem)
    #canvas1.itemconfig(img_id, image=img)

    loginwindow.withdraw()

    window = Toplevel()
    window.geometry("800x600")
    window.title("Pagina principal")

    window.resizable(False, False)
    window.configure(bg="#D1BEA6")

    # MENU BAR
    barra_Menu = Menu(window)

    categorias_menu = Menu(barra_Menu, tearoff=0)

    barra_Menu.add_cascade(label="Categorias", menu=categorias_menu)
    barra_Menu.add_command(label="Sair", command=window.quit)

    with open("Ficheiros\\categorias.txt", "r") as f:
        for linha_ficheiro in f.readlines():
            campos = linha_ficheiro.strip().split(";")
            categorias_menu.add_command(label=campos[0])

    window.configure(menu=barra_Menu)

    # CONTAINER

    panel1 = PanedWindow(window, width=200, height=105,
                         bd="2", relief="sunken")
    panel1.pack(fill=Y, side=RIGHT)

    canvas1 = Canvas(panel1, width=100, height=100, bd="2", relief="sunken")
    canvas1.pack(side=TOP)

    admin = Label(panel1, text = "ADMIN",font=("Microsoft YaHei", 10), fg = "red")
    admin.place(x = 30, y = 115)

    btn_adicionar_categorias = Button(panel1, text = "Adicionar\ncategoria", font=("Microsoft YaHei", 10), command = janela_adicionar_categoria)
    btn_adicionar_categorias.place(x = 20, y = 140)

    panel2 = PanedWindow(window, width=400, height=500,
                         bd="2", relief="sunken")
    panel2.place(x=100, y=50)
    

    # BUTTON ADD NEW RECIPE

    btn_header = Label(panel2, text="Adicionar receita",
                       fg="black", font=("Microsoft YaHei", 12))
    btn_header.place(x=140, y=10)

    btn_add_new_recipe = Button(
        panel2, text="+", width=4, height=1, font=("Microsoft YaHei", 20), command=addnewrecipe)
    btn_add_new_recipe.place(x=160, y=50)

    with open("Ficheiros\\perfil.txt", "r")as f:
        campos2 = f.readline()
    img10 = campos2.replace("/", "//")
    img = ImageTk.PhotoImage(file=img10)
    img_id = canvas1.create_image(0, 0, anchor="nw", image=img)

    window.mainloop()


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
        user.title("Página utilizador")

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
    window.title("Página principal")
    window.resizable(False, False)

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

                    if campos[1] == user:
                        isUserRegisted = True

                    if campos[2] == password:
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
loginwindow.title("Login")
loginwindow.resizable(False, False)
loginwindow.configure(bg="#D1BEA6")

# criar wallpaper
#wall = ImageTk.PhotoImage(file="Images/wallpaper6.jpg")
#wallpaper = Label(loginwindow, image=wall)
#wallpaper.place(x=0, y=0, relwidth=1, relheight=1)


original_frame = Frame(loginwindow)
loginwindow.configure(bg="#D1BEA6")


lbl_login = Label(loginwindow, text="Login", font=("Microsoft YaHei", 20), bg="#D1BEA6")
lbl_login.place(x=350, y=90)


lbl_username = Label(loginwindow, text="Email:",
                     font=("Microsoft YaHei", 12), bg="#D1BEA6")
lbl_username.place(x=250, y=200)


txt_username = Entry(loginwindow,  fg="black", font=("Microsoft YaHei", 12), width=35, relief="raised")
txt_username.place(x=250, y=230)


lbl_password = Label(loginwindow, text="Password:", font=("Microsoft YaHei", 12),bg="#D1BEA6")
lbl_password.place(x=250, y=280)


txt_password = Entry(loginwindow, fg="black", font=("Microsoft YaHei", 12), show="*", width=35, relief="raised")
txt_password.place(x=250, y=310)


loginButton = Button(loginwindow, text="Login", width="10",
                     font=("Microsoft YaHei", 12), command=login,bg="#D1BEA6")
loginButton.place(x=450, y=400)


registarButton = Button(loginwindow, text="Register", width="10", font=("Microsoft YaHei", 12), command=janelaRegistar, bg="#D1BEA6")
registarButton.place(x=250, y=400)


regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

loginwindow.mainloop()
