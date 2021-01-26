from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import filedialog
import os
import re


def janelaRegistar():

    def registo ():
        
        emailRegisto=registertxt_username.get()
        passwordRegisto = registertxt_password.get()
        confpassRegisto = registertxt_confpassword.get()
        linha_ficheiro = str(emailRegisto) + ";" + str(passwordRegisto) +"\n"
        
        
        if emailRegisto == "" or passwordRegisto =="" or confpassRegisto=="":
            messagebox.showerror("Campos Inválidos","Preencha todos os campos")
            
        elif  passwordRegisto != confpassRegisto:
            messagebox.showerror("Passwords diferentes","As passwords são diferentes")
        
        elif emailRegisto:
            if re.search(regex,emailRegisto):
                oEmailExiste = False
                with open("Ficheiros\\register.txt", "r") as f:

                    for linha_ficheiro in f.readlines():
                        campos = linha_ficheiro.split(";")
                        if campos[0] == emailRegisto:
                            oEmailExiste = True
                            messagebox.showerror("Erro","Esse utilizador já está registado")
                            break

                if oEmailExiste == False:
                    with open("Ficheiros\\register.txt", "a") as f:
                        f.write(emailRegisto + ";" + passwordRegisto + "\n")
                        messagebox.showinfo("Sucesso", "O registo foi concluído com sucesso")
                        registerWindow.withdraw()
                        main_page()
            else: messagebox.showerror("Email Inválido", "Email Inválido")

        
           
                
        
        


    def voltar ():

        #/-/-/-/-/-/-/-/-/-/-/-
        #Back Button
        #/-/-/-/-/-/-/-/-/-/-/-

        registerWindow.destroy()
        loginwindow.update()
        loginwindow.deiconify()


    def escolhe_imagem():
        global filename
        filename=filedialog.askopenfilename(title="Select file", filetypes=(("jpg files","*.jpg"),("png files","*.png"),("all files","*.*")))
        global img_perfil
        img=ImageTk.PhotoImage(file=filename)   
        canvas.itemconfig(image_id, image=img)

    # Guarda dados no ficheiro perfil.txt
    def guardar_setup():
         #f = open(ficheiro_perfil, "w")
         #linha = filename      # Imagem d eperfil;tema selecionado
         #f.write(linha + "\n") 
         #f.close()
         global img
         # atualiza canvas de imagem de perfil, com imagem guardada em ficheiro
         #img = ImageTk.PhotoImage(file = filename)
         #canvas.itemconfig(image_id, image=img)


    #/-/-/-/-/-/-/-/-/-/-/-
    #Register Window
    #/-/-/-/-/-/-/-/-/-/-/-

    
    registerWindow = Toplevel(loginwindow) 
    registerWindow.title("Register")
    registerWindow.geometry("800x600") 
    
    #wallpaper registo
    wall2=ImageTk.PhotoImage(file="Images/wallpaper6.jpg")
    wallpaper2=Label(registerWindow, image=wall)
    wallpaper2.place(x=0, y=0,relwidth=1, relheight=1) 

    loginwindow.withdraw()

    registerlbl_usernamePerfil = Label(registerWindow, text="Username:", fg="green", font=("Helvetica", 12))
    registerlbl_usernamePerfil.place(x=270, y=140)

    registertxt_usernamePerfil = Entry(registerWindow,  fg="black", font=("Helvetica", 10), width=35, relief="raised")
    registertxt_usernamePerfil.place(x=270, y=180)

    registerlbl_login = Label(registerWindow, text="Register", fg="red", font=("Helvetica", 30) )
    registerlbl_login.place(x=350,y=55)

    registerlbl_username = Label(registerWindow, text="Email:", fg="green", font=("Helvetica", 12) )
    registerlbl_username.place(x=270,y=220)

    registertxt_username = Entry(registerWindow,  fg="black", font=("Helvetica", 10), width=35, relief="raised" )
    registertxt_username.place(x=270,y=260)

    registerlbl_password = Label(registerWindow, text="Password:", fg="green",font=("Helvetica", 12) )
    registerlbl_password.place(x=270,y=300)

    registertxt_password = Entry(registerWindow, fg="black", font=("Helvetica", 10), show="*", width=35, relief="raised" )
    registertxt_password.place(x=270,y=340)

    registerlbl_confpassword = Label(registerWindow, text="Confirm Password:", fg="green",font=("Helvetica", 12) )
    registerlbl_confpassword.place(x=270,y=380)

    registertxt_confpassword = Entry(registerWindow, fg="black", font=("Helvetica", 10), show="*", width=35, relief="raised" )
    registertxt_confpassword.place(x=270,y=420)

    registarButtonRegister= Button(registerWindow, text="Register", width="10", font=("Helvetica", 12), fg="red" , command = registo)
    registarButtonRegister.place(x=420, y= 480)

    menuButton= Button(registerWindow, text="Back", width="10", font=("Helvetica", 12), fg="red", command = voltar)
    menuButton.place(x=270, y= 480)

    canvas = Canvas(registerWindow, width = 120, height = 130, bd = 1, relief = "sunken")
    canvas.place(x=20, y=20)

    button_imagem =Button(registerWindow, text="Selecionar \nFoto de Perfil", width="14", font=("Helvetica", 12), fg="green", command=escolhe_imagem)
    button_imagem.place(x=18, y=230)

    img=ImageTk.PhotoImage(file = "andre.jpeg")

    image_id= canvas.create_image(0,0, anchor='nw', image=img)

def main_page ():

    def recipe_page ():

        def back():

            #/-/-/-/-/-/-/-/-/-/-/-
            #Back button
            #/-/-/-/-/-/-/-/-/-/-/-

            top_window.destroy()
            window.update()
            window.deiconify()
            

        window.withdraw()

        top_window = Toplevel()
        top_window.geometry("800x600")
        top_window.title("Which category ?")



        frame2= Frame(top_window)


        wall3=ImageTk.PhotoImage(file="Images/livro.jpg")
        wallpaper3=Label(frame2, image=wall)
        wallpaper3.place(x=0, y=0,relwidth=1, relheight=1)

       

        #/-/-/-/-/-/-/-/-/-/-/-
        #Back button place
        #/-/-/-/-/-/-/-/-/-/-/-

        back_button = Button(top_window, text="Back", command=back)
        back_button.place(x=750, y=7)


        #/-/-/-/-/-/-/-/-/-/-/-
        #Categorias
        #/-/-/-/-/-/-/-/-/-/-/-


        chicken_btn = Button(frame2, text="Chicken" , width=10 , height = 3)
        chicken_btn.grid(padx=15, pady=15)

        fish_btn = Button(frame2, text="Fish" ,width=10 , height = 3)
        fish_btn.grid(row=1, padx=15, pady=15)

        soup_btn = Button(frame2, text="Soup",width=10 , height = 3 )
        soup_btn.grid(row=2, padx=15, pady=15)

        salad_btn = Button(frame2, text="Salad",width=10 , height = 3)
        salad_btn.grid(row=0,column=1, padx=15, pady=15)

        meat_btn = Button(frame2, text="Meat",width=10 , height = 3 )
        meat_btn.grid(row=1, column=1, padx=15, pady=15)

        vegetarian_btn = Button(frame2, text="Vegetarian",width=10 , height = 3 )
        vegetarian_btn.grid(row=2, column=1, padx=15, pady=15)

        snacks_btn = Button(frame2, text="Snacks",width=10 , height = 3 )
        snacks_btn.grid(row=0, column=2, padx=15, pady=15)

        cakes_btn = Button(frame2, text="Cakes",width=10 , height = 3 )
        cakes_btn.grid(row=1, column=2, padx=15, pady=15)

        beverages_btn = Button(frame2, text="Beverages",width=10 , height = 3 )
        beverages_btn.grid(row=2, column=2, padx=15, pady=15)

        sauces_btn = Button(frame2, text="Sauces",width=10 , height = 3 )
        sauces_btn.grid(row=0, column=3, padx=15, pady=15)

        desserts_btn = Button(frame2, text="Desserts",width=10 , height = 3 )
        desserts_btn.grid(row=1, column=3, padx=15, pady=15)

        appetizers_btn = Button(frame2, text="Appetizers",width=10 , height = 3 )
        appetizers_btn.grid(row=2, column=3, padx=15, pady=15)

        pasta_btn = Button(frame2, text="Pasta",width=10 , height = 3 )
        pasta_btn.grid(row=0, column=4, padx=15, pady=15)

        other_btn = Button(frame2, text="Other",width=10 , height = 3 )
        other_btn.grid(row=1, column=4, padx=15, pady=15)

        frame2.place(relx=0.5, rely=0.5, anchor=CENTER)

        
    loginwindow.withdraw()


    #/-/-/-/-/-/-/-/-/-/-/-
    #Main Page
    #/-/-/-/-/-/-/-/-/-/-/-


    window = Toplevel()
    window.geometry("800x600")
    window.title("Home Page")

   #wallpaper home page
    wall4=ImageTk.PhotoImage(file="Images/wallpaper6.jpg")
    wallpaper4=Label(window, image=wall)
    wallpaper4.place(x=0, y=0,relwidth=1, relheight=1)


    frame = Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    chicken_btn = Button(frame, text="Chicken" , width=10 , height = 3)
    chicken_btn.grid(padx=15, pady=15)

    fish_btn = Button(frame, text="Fish" ,width=10 , height = 3)
    fish_btn.grid(row=1, padx=15, pady=15)

    soup_btn = Button(frame, text="Soup",width=10 , height = 3 )
    soup_btn.grid(row=2, padx=15, pady=15)

    salad_btn = Button(frame, text="Salad",width=10 , height = 3)
    salad_btn.grid(row=0,column=1, padx=15, pady=15)

    meat_btn = Button(frame, text="Meat",width=10 , height = 3 )
    meat_btn.grid(row=1, column=1, padx=15, pady=15)

    vegetarian_btn = Button(frame, text="Vegetarian",width=10 , height = 3 )
    vegetarian_btn.grid(row=2, column=1, padx=15, pady=15)

    snacks_btn = Button(frame, text="Snacks",width=10 , height = 3 )
    snacks_btn.grid(row=0, column=2, padx=15, pady=15)

    cakes_btn = Button(frame, text="Cakes",width=10 , height = 3 )
    cakes_btn.grid(row=1, column=2, padx=15, pady=15)

    beverages_btn = Button(frame, text="Beverages",width=10 , height = 3 )
    beverages_btn.grid(row=2, column=2, padx=15, pady=15)

    sauces_btn = Button(frame, text="Sauces",width=10 , height = 3 )
    sauces_btn.grid(row=0, column=3, padx=15, pady=15)

    desserts_btn = Button(frame, text="Desserts",width=10 , height = 3 )
    desserts_btn.grid(row=1, column=3, padx=15, pady=15)

    appetizers_btn = Button(frame, text="Appetizers",width=10 , height = 3 )
    appetizers_btn.grid(row=2, column=3, padx=15, pady=15)

    pasta_btn = Button(frame, text="Pasta",width=10 , height = 3 )
    pasta_btn.grid(row=0, column=4, padx=15, pady=15)

    other_btn = Button(frame, text="Other",width=10 , height = 3 )
    other_btn.grid(row=1, column=4, padx=15, pady=15)

    add_new_recipe = Button(window, text="Add new recipe" , command=recipe_page)
    add_new_recipe.pack(side = TOP, pady=10)


   #wallpaper home page-2º fundo
    wall5=ImageTk.PhotoImage(file="Images/livro.jpg")
    wallpaper5=Label(frame, image=wall)
    wallpaper5.place(x=0, y=0,relwidth=1, relheight=1)
        


#/-/-/-/-/-/-/-/-/-/-/-#
#Login Page
#/-/-/-/-/-/-/-/-/-/-/-#

def loginvazio():



    isUserRegisted = False
    user = str (txt_username.get())
    password= str(txt_password.get())
    with open("Ficheiros\\register.txt", "r") as f:
        for linha in f.readlines():
            campos = linha.split(";")
    print(campos)

    if user == "" or password =="":
        messagebox.showerror("Campos inválidos","Preencha todos os campos")

    elif not campos[0] == user:
        messagebox.showerror("Erro","O Utilizador inserido não está registado")
            

    elif not campos[1] == password:
        messagebox.showerror("Erro","Password inválida, tente novamente")

    else:
        isUserRegisted = True
        if isUserRegisted == True:
            messagebox.showinfo("Sucesso","O login foi concludo com sucesso")
            main_page()

        

loginwindow = Tk()  #invoca classe tk, cria a "main window"
loginwindow.geometry("800x600")
loginwindow.title("Projeto de AED")


#criar wallpaper
wall=ImageTk.PhotoImage(file="Images/wallpaper6.jpg")
wallpaper=Label(loginwindow, image=wall)
wallpaper.place(x=0, y=0,relwidth=1, relheight=1)

original_frame= Frame(loginwindow)
loginwindow.configure(bg="#DBE2AC")

lbl_login = Label(loginwindow, text="Login", fg="red", font=("Helvetica", 30))
lbl_login.place(x=350,y=75)

lbl_username = Label(loginwindow, text="Email:", fg="green", font=("Helvetica", 12) )
lbl_username.place(x=250,y=200)

txt_username = Entry(loginwindow,  fg="black", font=("Helvetica", 10), width=35, relief="raised" )
txt_username.place(x=250,y=250)

lbl_password = Label(loginwindow, text="Password:", fg="green",font=("Helvetica", 12) )
lbl_password.place(x=250,y=300)

txt_password = Entry(loginwindow, fg="black", font=("Helvetica", 10), show="*", width=35, relief="raised" )
txt_password.place(x=250,y=350)


loginButton= Button(loginwindow, text="Login", width="10", font=("Helvetica", 12), fg="red", command = loginvazio)
loginButton.place(x=395, y= 420)

registarButton= Button(loginwindow, text="Register", width="10", font=("Helvetica", 12), fg="red", command = janelaRegistar)
registarButton.place(x=245, y= 420)


regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

loginwindow.mainloop()

