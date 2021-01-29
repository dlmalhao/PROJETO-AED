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
                    guardar_setup()
                    main_page()
                    registerWindow.withdraw()

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
            if imagem :
                f.write(imagem)
            
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


def get_back (window1, window2):
    window1.destroy()
    window2.update()
    window2.deiconify()


def main_page():

    def addnewrecipe ():

        def guardar_dados():
            guardar_titulo= str(titulo.get())
            guardar_preparacao= str(preparacao.get("1.0","end"))
            guardar_tempo=str(tempo.get())
            guardar_categorias=str((lbox.get(ACTIVE))) 

            if guardar_titulo=="" or guardar_preparacao=="\n" or guardar_tempo=="" or guardar_categorias=="":
                messagebox.showerror("Erro","Preencha todos os campos")
            else:
                titulo_Receita()
                tempo_Receita()
                categorias_Receita()
                ingredientes_Receita()
                preparacao_Receita()
                messagebox.showinfo("Sucesso", "A receita foi adicionada com sucesso")
                voltar()


        def voltar():
            windowAddRecipe.withdraw()
            window.update()
            window.deiconify()

        def titulo_Receita():
            tituloReceita= str(titulo.get())
            with open("Ficheiros\\tituloReceita.txt", "a", encoding="utf-8") as f:
                f.write(tituloReceita + "\n")
                f.close()
                

        def tempo_Receita():
            tempoReceita= str(tempo.get())
            with open("Ficheiros\\tempoReceita.txt", "a", encoding="utf-8") as f:
                f.write(tempoReceita + "\n")
                f.close()



        def categorias_Receita():
            with open("Ficheiros\\categoriasReceita.txt", "a", encoding="utf-8") as f:
                for i in lbox.get(0,"end"):
                    f.write(i+"\n")

        def ingredientes_Receita():
            with open("Ficheiros\\ingredientesReceita.txt", "w", encoding="utf-8") as f:
                for i in  ingredientes.get("1.0", END):
                    f.write(i)

        def preparacao_Receita():
            with open("Ficheiros\\preparacaoReceita.txt", "w", encoding="utf-8") as f:
                
                for i in  preparacao.get("1.0", END):
                    f.write(i)


        def escolhe_imagem(canvas2):
            with open("Ficheiros//imagemReceita.txt", "w")as f:
            
                imagem=filedialog.askopenfilename(title="Select file", filetypes=(("jpg files",".jpg"),("png files",".png"),("all files",".")))
                if imagem:
                    canvas2.img = ImageTk.PhotoImage(Image.open(imagem).resize((220, 300)))
                    canvas2.create_image(0,0,anchor = "nw", image = canvas2.img)
                    f.write(imagem)

        window.withdraw()

        windowAddRecipe = Toplevel()
        windowAddRecipe.geometry("800x600")
        windowAddRecipe.title("Adicionar receita")
        windowAddRecipe.resizable(False, False)

        windowAddRecipe.configure(bg="#D1BEA6")

        panel1 = PanedWindow(windowAddRecipe, width=400, height = 500, bd="2", relief="sunken")
        panel1.place(x = 60, y = 50)
        
        header = Label(panel1, text="Adicionar receita", fg="black", font=("Microsoft YaHei", 12))
        header.place(x = 140, y = 10)

        titulo = Entry(panel1, width = 40)
        titulo.place(x = 100, y = 100)
        titulo_label = Label(panel1, text="Título", fg="black", font=("Microsoft YaHei", 10))
        titulo_label.place(x=30, y=95)

        preparacao = Text(panel1, width = 30, height = 10, wrap = "word")
        preparacao.place(x = 100, y = 150)
        preparacao_label = Label(panel1, text="Modo \n de \n preparação", fg="black", font=("Microsoft YaHei", 10))
        preparacao_label.place(x=15, y=140)

        tempo = Entry(panel1, width = 40)
        tempo.place(x = 100, y = 340)
        tempo_label = Label(panel1, text="Tempo \n estimado", fg="black", font=("Microsoft YaHei", 10))
        tempo_label.place(x=15, y=330)

        ingredientes = Text(panel1, width = 30, height=5)
        ingredientes.place(x = 100, y = 400)
        ingredientes_label = Label(panel1, text="Ingredientes", fg="black", font=("Microsoft YaHei", 10))
        ingredientes_label.place(x=15, y=400)

        btn_voltar = Button(windowAddRecipe, text = "Voltar",font=("Microsoft YaHei", 10), bg="#D1BEA6", command = voltar)
        btn_voltar.place(x = 10, y = 10)


        #CANVAS PARA FOTO
        canvas2 = Canvas(windowAddRecipe, width = 250, height = 250, bd ="2", relief = "sunken")
        canvas2.place(x = 500, y = 50)

        btn3 = Button(windowAddRecipe, text = "Selecionar imagem", command = partial(escolhe_imagem, canvas2),font=("Microsoft YaHei", 10), bg="#D1BEA6", width=15)
        btn3.place(x =575, y = 330)

        btn4 = Button(windowAddRecipe, text = "Guardar Receita", command = guardar_dados,font=("Microsoft YaHei", 10), bg="#D1BEA6", width=15)
        btn4.place(x =575, y = 550)


        #COMBO BOX
        lista_cb = []
        with open("Ficheiros//categorias.txt","r") as f:
            for i in f.readlines() :
                campos = i.strip().split(";")
                lista_cb.append(campos[0])

        combo_box = Combobox(windowAddRecipe, values = lista_cb)
        combo_box.place(x = 560, y = 390)

        label_cb = Label(windowAddRecipe, text = "Escolher\ncategoria", font=("Microsoft YaHei", 10), bg="#D1BEA6")
        label_cb.place(x = 485, y = 380)


        #LIST BOX   
        lbox = Listbox(windowAddRecipe, height = 4, width = 30)
        lbox.place(x = 550, y = 470 )


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

            
                
        lbox_btn = Button(windowAddRecipe, text = "Adicionar", font=("Microsoft YaHei", 10), bg="#D1BEA6", command = lbox_add, width=15)
        lbox_btn.place(x = 575, y = 430)


        windowAddRecipe.mainloop()




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

    def detalhesPage():        
    
                
        def ler_titulo_receita():
            f=open("Ficheiros\\tituloReceita.txt","r", encoding="utf-8")
            lista=f.readlines()
            
            f.close()
            for linha in lista:
                print(linha)
                detalhes_titulo.set(linha)

        def ler_tempo_receita():
            f=open("Ficheiros\\tempoReceita.txt","r", encoding="utf-8")
            lista=f.readlines()
            
            f.close()
            for linha in lista:
                
                detalhes_tempo.set(linha)


        def ler_categorias_receita():
            
            f=open("Ficheiros\\categoriasReceita.txt","r", encoding="utf-8")

            
            for linha in f.readlines():
                
                detalhes_categorialbox.insert("end",linha)
                
                
            f.close()
        
        def ler_ingredientes_receita():
            
            f=open("Ficheiros\\ingredientesReceita.txt","r", encoding="utf-8")

            
            for linha in f.readlines():
                print(linha)
                detalhes_ingredientestxt.insert(END,linha)
                detalhes_ingredientestxt["state"]=DISABLED
                
            f.close()

        def ler_preparacao_receita():
            
            f=open("Ficheiros\\preparacaoReceita.txt","r", encoding="utf-8")

            
            for linha in f.readlines():
                print(linha)
                detalhes_modotxt.insert(END,linha)
                detalhes_modotxt["state"]=DISABLED
                
            f.close()


        
            
            

        def voltar():

            # /-/-/-/-/-/-/-/-/-/-/-
            # Back Button
            # /-/-/-/-/-/-/-/-/-/-/-

            detalhesPage.destroy()
            window.update()
            window.deiconify()

        detalhesPage = Toplevel()
        detalhesPage.geometry("800x600")
        detalhesPage.title("Detalhes da receita")
        detalhesPage.resizable(False, False)
        detalhesPage.configure(bg="#D1BEA6")

        detalhes_receitalbl = Label(detalhesPage, text="Dados da receita", fg="black",bg = "#D1BEA6", font=("Microsoft YaHei", 20))
        detalhes_receitalbl.place(x=300, y=30)

        detalhes_titulo=StringVar()
        detalhes_titulolbl = Label(detalhesPage, text="Nome da Receita:", fg="black",bg = "#D1BEA6", font=("Microsoft YaHei", 12))
        detalhes_titulolbl.place(x=40, y=100)
        detalhes_titulotxt = Entry(detalhesPage, text="Dados da receita", fg="black",bg = "#D1BEA6", font=("Microsoft YaHei", 12), state="disabled", width=31,textvariable = detalhes_titulo)
        detalhes_titulotxt.place(x=200, y=100)

        detalhes_modolbl = Label(detalhesPage, text="Como preparar:", fg="black",bg = "#D1BEA6", font=("Microsoft YaHei", 12))
        detalhes_modolbl.place(x=40, y=150)
        detalhes_modotxt = Text(detalhesPage, width=35, height = 10)
        detalhes_modotxt.place(x=200, y=150)

        detalhes_tempo=StringVar()
        detalhes_tempolbl = Label(detalhesPage, text="Tempo de duração\nestimado:", fg="black",bg = "#D1BEA6", font=("Microsoft YaHei", 12))
        detalhes_tempolbl.place(x=40, y=340)
        detalhes_tempotxt = Entry(detalhesPage, text="Dados da receita", fg="black",bg = "#D1BEA6", font=("Microsoft YaHei", 12), state="disabled", width=31,textvariable = detalhes_tempo)
        detalhes_tempotxt.place(x=200, y=350)

        detalhes_categoria=StringVar()
        detalhes_categorialbl = Label(detalhesPage, text="Categorias da Receita:", fg="black",bg = "#D1BEA6", font=("Microsoft YaHei", 12))
        detalhes_categorialbl.place(x=25, y=400)
        detalhes_categorialbox = Listbox(detalhesPage, width=20, height = 8)
        detalhes_categorialbox.place(x=200, y=400)

        detalhes_ingredienteslbl = Label(detalhesPage, text="Ingredientes:", fg="black",bg = "#D1BEA6", font=("Microsoft YaHei", 12))
        detalhes_ingredienteslbl.place(x=400, y=400)
        detalhes_ingredientestxt = Text(detalhesPage, width=20, height = 8)
        detalhes_ingredientestxt.place(x=520, y=400)

        canvas1 = Canvas(detalhesPage, width=250, height=200, bd="2", relief="sunken")
        canvas1.place(x = 550, y = 100)

        
        

        voltarButton= Button(detalhesPage, text="Voltar", fg="black",bg = "#D1BEA6", font=("Microsoft YaHei", 12), command= voltar)
        voltarButton.place(x=10,y=10)

        with open("Ficheiros\\imagemReceita.txt", "r")as f:
            campos2 = f.readline()
        img10 = campos2.replace("/", "//")
        img = ImageTk.PhotoImage(Image.open(img10).resize((220, 300)))
        img_id = canvas1.create_image(0, 0, anchor="nw", image=img)

        ler_preparacao_receita()
        ler_ingredientes_receita()
        ler_categorias_receita()
        ler_titulo_receita()
        ler_tempo_receita()
        detalhesPage.mainloop()

    def cakes():
 
        windowcakes= Toplevel()
        windowcakes.geometry("800x600")
        windowcakes.title("Cakes Page")

        windowcakes.focus_force()
        windowcakes.grab_set() 

        windowcakes.mainloop()

    def chicken():
 
        windowchicken= Toplevel()
        windowchicken.geometry("800x600")
        windowchicken.title("Chicken Page")

        windowchicken.focus_force()
        windowchicken.grab_set() 

        windowchicken.mainloop()

    def fish():
    
        windowfish= Toplevel()
        windowfish.geometry("800x600")
        windowfish.title("Fish Page")

        windowfish.focus_force()
        windowfish.grab_set() 

        windowfish.mainloop()    

    def meat():
    
        windowmeat= Toplevel()
        windowmeat.geometry("800x600")
        windowmeat.title("Meat Page")

        windowmeat.focus_force()
        windowmeat.grab_set() 

        windowmeat.mainloop()      

    def pasta():
    
        windowpasta= Toplevel()
        windowpasta.geometry("800x600")
        windowpasta.title("Pasta Page")

        windowpasta.focus_force()
        windowpasta.grab_set() 

        windowpasta.mainloop()   

    def salad():
    
        windowsalad= Toplevel()
        windowsalad.geometry("800x600")
        windowsalad.title("Salad Page")

        windowsalad.focus_force()
        windowsalad.grab_set() 

        windowsalad.mainloop() 

    def snacks():
    
        windowsnacks= Toplevel()
        windowsnacks.geometry("800x600")
        windowsnacks.title("Snacks Page")

        windowsnacks.focus_force()
        windowsnacks.grab_set() 

        windowsnacks.mainloop()              

    def soup():
    
        windowsoup= Toplevel()
        windowsoup.geometry("800x600")
        windowsoup.title("Soup Page")

        windowsoup.focus_force()
        windowsoup.grab_set() 

        windowsoup.mainloop()   


    def selec(tipo):
        if tipo=="Cakes":
            cakes()
        elif tipo=="Chicken":
            chicken()
        elif tipo=="Fish":
            fish()
        elif tipo=="Meat":
            meat()
        elif tipo=="Pasta":
            pasta()
        elif tipo=="Salad":
            salad()
        elif tipo=="Snacks":
            snacks()
        else:
            soup()            




    # MENU BAR
    barra_Menu = Menu(window)

    categorias_menu = Menu(barra_Menu)

    barra_Menu.add_cascade(label="Categorias", menu=categorias_menu)
    barra_Menu.add_command(label="Sair", command=window.destroy)



    with open("Ficheiros\\categorias.txt", "r") as f:
        for linha_ficheiro in f.readlines():
            campos = linha_ficheiro.strip().split(";")
            categorias_menu.add_command(label=campos[0], command=partial(selec,campos[0]))



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
    
    btn_perfil = Button(panel1, text="Perfil", font=("Microsoft YaHei", 10), width = 8)
    btn_perfil.place (x = 15, y = 115)

    # BUTTON ADD NEW RECIPE

    btn_header = Label(panel2, text="Adicionar receita",
                       fg="black", font=("Microsoft YaHei", 12))
    btn_header.place(x=140, y=10)

    btn_add_new_recipe = Button(
        panel2, text="+", width=4, height=1, font=("Microsoft YaHei", 20), command=addnewrecipe)
    btn_add_new_recipe.place(x=160, y=50)

    btn_ver_receita = Button(panel2, text = "Ver receitas", font=("Microsoft YaHei", 12), command=detalhesPage)
    btn_ver_receita.place (x = 145, y = 140)

    with open("Ficheiros\\perfil.txt", "r")as f:
        campos2 = f.readline()
    img10 = campos2.replace("/", "//")
    img = ImageTk.PhotoImage(file=img10)
    img_id = canvas1.create_image(0, 0, anchor="nw", image=img)

    

    window.mainloop()




def admin_mode():

    def addnewrecipe ():

        def guardar_dados():
            guardar_titulo= str(titulo.get())
            guardar_preparacao= str(preparacao.get("1.0","end"))
            guardar_tempo=str(tempo.get())
            guardar_categorias=str((lbox.get(ACTIVE))) 

            if guardar_titulo=="" or guardar_preparacao=="\n" or guardar_tempo=="" or guardar_categorias=="":
                messagebox.showerror("Erro","Preencha todos os campos")
            else:
                titulo_Receita()
                tempo_Receita()
                categorias_Receita()
                ingredientes_Receita()
                preparacao_Receita()
                messagebox.showinfo("Sucesso", "A receita foi adicionada com sucesso")
                voltar()


        def voltar():
            windowAddRecipe.withdraw()
            window.update()
            window.deiconify()

        def titulo_Receita():
            tituloReceita= str(titulo.get())
            with open("Ficheiros\\tituloReceita.txt", "a", encoding="utf-8") as f:
                f.write(tituloReceita + "\n")
                f.close()
                

        def tempo_Receita():
            tempoReceita= str(tempo.get())
            with open("Ficheiros\\tempoReceita.txt", "a", encoding="utf-8") as f:
                f.write(tempoReceita + "\n")
                f.close()



        def categorias_Receita():
            with open("Ficheiros\\categoriasReceita.txt", "a", encoding="utf-8") as f:
                for i in lbox.get(0,"end"):
                    f.write(i+"\n")

        def ingredientes_Receita():
            with open("Ficheiros\\ingredientesReceita.txt", "w", encoding="utf-8") as f:
                for i in ingredientes.get("1.0", END):
                    f.write(i)

        def preparacao_Receita():
            with open("Ficheiros\\preparacaoReceita.txt", "w", encoding="utf-8") as f:
                
                for i in  preparacao.get("1.0", END):
                    f.write(i)


        def escolhe_imagem(canvas2):
            with open("Ficheiros//imagemReceita.txt", "w")as f:
            
                imagem=filedialog.askopenfilename(title="Select file", filetypes=(("jpg files",".jpg"),("png files",".png"),("all files",".")))
                if imagem:
                    canvas2.img = ImageTk.PhotoImage(Image.open(imagem).resize((220, 300)))
                    canvas2.create_image(0,0,anchor = "nw", image = canvas2.img)
                    f.write(imagem)

        window.withdraw()

        windowAddRecipe = Toplevel()
        windowAddRecipe.geometry("800x600")
        windowAddRecipe.title("Adicionar receita")
        windowAddRecipe.resizable(False, False)

        windowAddRecipe.configure(bg="#D1BEA6")

        panel1 = PanedWindow(windowAddRecipe, width=400, height = 500, bd="2", relief="sunken")
        panel1.place(x = 60, y = 50)
        
        header = Label(panel1, text="Adicionar receita", fg="black", font=("Microsoft YaHei", 12))
        header.place(x = 140, y = 10)

        titulo = Entry(panel1, width = 40)
        titulo.place(x = 100, y = 100)
        titulo_label = Label(panel1, text="Título", fg="black", font=("Microsoft YaHei", 10))
        titulo_label.place(x=30, y=95)

        preparacao = Text(panel1, width = 30, height = 10, wrap = "word")
        preparacao.place(x = 100, y = 150)
        preparacao_label = Label(panel1, text="Modo \n de \n preparação", fg="black", font=("Microsoft YaHei", 10))
        preparacao_label.place(x=15, y=140)

        tempo = Entry(panel1, width = 40)
        tempo.place(x = 100, y = 340)
        tempo_label = Label(panel1, text="Tempo \n estimado", fg="black", font=("Microsoft YaHei", 10))
        tempo_label.place(x=15, y=330)

        ingredientes = Text(panel1, width = 30, height=5)
        ingredientes.place(x = 100, y = 400)
        ingredientes_label = Label(panel1, text="Ingredientes", fg="black", font=("Microsoft YaHei", 10))
        ingredientes_label.place(x=15, y=400)

        btn_voltar = Button(windowAddRecipe, text = "Voltar",font=("Microsoft YaHei", 10), bg="#D1BEA6", command = voltar)
        btn_voltar.place(x = 10, y = 10)


        #CANVAS PARA FOTO
        canvas2 = Canvas(windowAddRecipe, width = 250, height = 250, bd ="2", relief = "sunken")
        canvas2.place(x = 500, y = 50)

        btn3 = Button(windowAddRecipe, text = "Selecionar imagem", command = partial(escolhe_imagem, canvas2),font=("Microsoft YaHei", 10), bg="#D1BEA6", width=15)
        btn3.place(x =575, y = 330)

        btn4 = Button(windowAddRecipe, text = "Guardar Receita", command = guardar_dados,font=("Microsoft YaHei", 10), bg="#D1BEA6", width=15)
        btn4.place(x =575, y = 550)


        #COMBO BOX
        lista_cb = []
        with open("Ficheiros//categorias.txt","r") as f:
            for i in f.readlines() :
                campos = i.strip().split(";")
                lista_cb.append(campos[0])

        combo_box = Combobox(windowAddRecipe, values = lista_cb)
        combo_box.place(x = 560, y = 390)

        label_cb = Label(windowAddRecipe, text = "Escolher\ncategoria", font=("Microsoft YaHei", 10), bg="#D1BEA6")
        label_cb.place(x = 485, y = 380)


        #LIST BOX   
        lbox = Listbox(windowAddRecipe, height = 4, width = 30)
        lbox.place(x = 550, y = 470 )


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

            
                
        lbox_btn = Button(windowAddRecipe, text = "Adicionar", font=("Microsoft YaHei", 10), bg="#D1BEA6", command = lbox_add, width=15)
        lbox_btn.place(x = 575, y = 430)


        


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

    def detalhesPage():        
    
                
        def ler_titulo_receita():
            f=open("Ficheiros\\tituloReceita.txt","r", encoding="utf-8")
            lista=f.readlines()
            
            f.close()
            for linha in lista:
                print(linha)
                detalhes_titulo.set(linha)

        def ler_tempo_receita():
            f=open("Ficheiros\\tempoReceita.txt","r", encoding="utf-8")
            lista=f.readlines()
            
            f.close()
            for linha in lista:
                
                detalhes_tempo.set(linha)


        def ler_categorias_receita():
            
            f=open("Ficheiros\\categoriasReceita.txt","r", encoding="utf-8")

            
            for linha in f.readlines():
                
                detalhes_categorialbox.insert("end",linha)
                
                
            f.close()
        
        def ler_ingredientes_receita():
            
            f=open("Ficheiros\\ingredientesReceita.txt","r", encoding="utf-8")

            
            for linha in f.readlines():
                print(linha)
                detalhes_ingredientestxt.insert(END,linha)
                detalhes_ingredientestxt["state"]=DISABLED
                
            f.close()

        def ler_preparacao_receita():
            
            f=open("Ficheiros\\preparacaoReceita.txt","r", encoding="utf-8")

            
            for linha in f.readlines():
                print(linha)
                detalhes_modotxt.insert(END,linha)
                detalhes_modotxt["state"]=DISABLED
                
            f.close()


        def adicionar_categoria():
            input_value = entry_titulo.get()
            with open("Ficheiros\\categorias.txt","a")as f:
                if input_value:
                    f.write(input_value)
            

        def voltar():

            # /-/-/-/-/-/-/-/-/-/-/-
            # Back Button
            # /-/-/-/-/-/-/-/-/-/-/-

            detalhesPage.destroy()
            window.update()
            window.deiconify()

        detalhesPage = Toplevel()
        detalhesPage.geometry("800x600")
        detalhesPage.title("Detalhes da receita")
        detalhesPage.resizable(False, False)
        detalhesPage.configure(bg="#D1BEA6")

        detalhes_receitalbl = Label(detalhesPage, text="Dados da receita", fg="black",bg = "#D1BEA6", font=("Microsoft YaHei", 20))
        detalhes_receitalbl.place(x=300, y=30)

        detalhes_titulo=StringVar()
        detalhes_titulolbl = Label(detalhesPage, text="Nome da Receita:", fg="black",bg = "#D1BEA6", font=("Microsoft YaHei", 12))
        detalhes_titulolbl.place(x=40, y=100)
        detalhes_titulotxt = Entry(detalhesPage, text="Dados da receita", fg="black",bg = "#D1BEA6", font=("Microsoft YaHei", 12), state="disabled", width=31,textvariable = detalhes_titulo)
        detalhes_titulotxt.place(x=200, y=100)

        detalhes_modolbl = Label(detalhesPage, text="Como preparar:", fg="black",bg = "#D1BEA6", font=("Microsoft YaHei", 12))
        detalhes_modolbl.place(x=40, y=150)
        detalhes_modotxt = Text(detalhesPage, width=35, height = 10)
        detalhes_modotxt.place(x=200, y=150)

        detalhes_tempo=StringVar()
        detalhes_tempolbl = Label(detalhesPage, text="Tempo de duração\nestimado:", fg="black",bg = "#D1BEA6", font=("Microsoft YaHei", 12))
        detalhes_tempolbl.place(x=40, y=340)
        detalhes_tempotxt = Entry(detalhesPage, text="Dados da receita", fg="black",bg = "#D1BEA6", font=("Microsoft YaHei", 12), state="disabled", width=31,textvariable = detalhes_tempo)
        detalhes_tempotxt.place(x=200, y=350)

        detalhes_categoria=StringVar()
        detalhes_categorialbl = Label(detalhesPage, text="Categorias da Receita:", fg="black",bg = "#D1BEA6", font=("Microsoft YaHei", 12))
        detalhes_categorialbl.place(x=25, y=400)
        detalhes_categorialbox = Listbox(detalhesPage, width=20, height = 8)
        detalhes_categorialbox.place(x=200, y=400)

        detalhes_ingredienteslbl = Label(detalhesPage, text="Ingredientes:", fg="black",bg = "#D1BEA6", font=("Microsoft YaHei", 12))
        detalhes_ingredienteslbl.place(x=400, y=400)
        detalhes_ingredientestxt = Text(detalhesPage, width=20, height = 8)
        detalhes_ingredientestxt.place(x=520, y=400)

        canvas1 = Canvas(detalhesPage, width=250, height=200, bd="2", relief="sunken")
        canvas1.place(x = 550, y = 100)

        
        

        voltarButton= Button(detalhesPage, text="Voltar", fg="black",bg = "#D1BEA6", font=("Microsoft YaHei", 12), command= voltar)
        voltarButton.place(x=10,y=10)

        with open("Ficheiros\\imagemReceita.txt", "r")as f:
            campos2 = f.readline()
        img10 = campos2.replace("/", "//")
        img = ImageTk.PhotoImage(Image.open(img10).resize((220, 300)))
        img_id = canvas1.create_image(0, 0, anchor="nw", image=img)

        ler_preparacao_receita()
        ler_ingredientes_receita()
        ler_categorias_receita()
        ler_titulo_receita()
        ler_tempo_receita()
        detalhesPage.mainloop()
                
        def cancelar():
            miniwindow.destroy()

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

        button_cancelar = Button(miniwindow, text = "Cancelar", font=("Microsoft YaHei", 12), bg="#D1BEA6", command = cancelar)
        button_cancelar.place( x = 158, y = 180)

        miniwindow.mainloop()

    def cakes():
 
        windowcakes= Toplevel()
        windowcakes.geometry("800x600")
        windowcakes.title("Cakes Page")

        windowcakes.focus_force()
        windowcakes.grab_set() 

        windowcakes.mainloop()

    def chicken():
 
        windowchicken= Toplevel()
        windowchicken.geometry("800x600")
        windowchicken.title("Chicken Page")

        windowchicken.focus_force()
        windowchicken.grab_set() 

        windowchicken.mainloop()

    def fish():
    
        windowfish= Toplevel()
        windowfish.geometry("800x600")
        windowfish.title("Fish Page")

        windowfish.focus_force()
        windowfish.grab_set() 

        windowfish.mainloop()    

    def meat():
    
        windowmeat= Toplevel()
        windowmeat.geometry("800x600")
        windowmeat.title("Meat Page")

        windowmeat.focus_force()
        windowmeat.grab_set() 

        windowmeat.mainloop()      

    def pasta():
    
        windowpasta= Toplevel()
        windowpasta.geometry("800x600")
        windowpasta.title("Pasta Page")

        windowpasta.focus_force()
        windowpasta.grab_set() 

        windowpasta.mainloop()   

    def salad():
    
        windowsalad= Toplevel()
        windowsalad.geometry("800x600")
        windowsalad.title("Salad Page")

        windowsalad.focus_force()
        windowsalad.grab_set() 

        windowsalad.mainloop() 

    def snacks():
    
        windowsnacks= Toplevel()
        windowsnacks.geometry("800x600")
        windowsnacks.title("Snacks Page")

        windowsnacks.focus_force()
        windowsnacks.grab_set() 

        windowsnacks.mainloop()              

    def soup():
    
        windowsoup= Toplevel()
        windowsoup.geometry("800x600")
        windowsoup.title("Soup Page")

        windowsoup.focus_force()
        windowsoup.grab_set() 

        windowsoup.mainloop()   


    def selec(tipo):
        if tipo=="Cakes":
            cakes()
        elif tipo=="Chicken":
            chicken()
        elif tipo=="Fish":
            fish()
        elif tipo=="Meat":
            meat()
        elif tipo=="Pasta":
            pasta()
        elif tipo=="Salad":
            salad()
        elif tipo=="Snacks":
            snacks()
        else:
            soup()            


    # MENU BAR
    barra_Menu = Menu(window)

    categorias_menu = Menu(barra_Menu, tearoff=0)

    barra_Menu.add_cascade(label="Categorias", menu=categorias_menu)
    barra_Menu.add_command(label="Sair", command=window.destroy)

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

    panel2 = PanedWindow(window, width=400, height=500,
                         bd="2", relief="sunken")
    panel2.place(x=100, y=50)
    
    btn_perfil = Button(panel1, text="Perfil", font=("Microsoft YaHei", 10), width = 8)
    btn_perfil.place(x = 15, y = 115)

    # BUTTON ADD NEW RECIPE

    btn_header = Label(panel2, text="Adicionar receita",
                       fg="black", font=("Microsoft YaHei", 12))
    btn_header.place(x=140, y=10)

    btn_add_new_recipe = Button(
        panel2, text="+", width=4, height=1, font=("Microsoft YaHei", 20), command=addnewrecipe)
    btn_add_new_recipe.place(x=160, y=50)

    btn_ver_receita = Button(panel2, text = "Ver receitas", font=("Microsoft YaHei", 12), command=detalhesPage)
    btn_ver_receita.place (x = 145, y = 140)

    with open("Ficheiros\\perfil.txt", "r")as f:
        campos2 = f.readline()
    img10 = campos2.replace("/", "//")
    img = ImageTk.PhotoImage(file=img10)
    img_id = canvas1.create_image(0, 0, anchor="nw", image=img)

    

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
