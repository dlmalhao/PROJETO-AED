from tkinter import *


def janelaRegistar():


    def voltar ():

        registerWindow.destroy()
        window.update()
        window.deiconify()

    registerWindow = Toplevel(window) 
    registerWindow.title("Register")
    registerWindow.geometry("800x600") 

    window.withdraw()

    registerlbl_login = Label(registerWindow, text="Register", fg="red", font=("Helvetica", 30) )
    registerlbl_login.place(x=330,y=80)

    registerlbl_username = Label(registerWindow, text="Email:", fg="red", font=("Helvetica", 12) )
    registerlbl_username.place(x=270,y=200)

    registertxt_username = Entry(registerWindow,  fg="black", font=("Helvetica", 10), width=35, relief="raised" )
    registertxt_username.place(x=270,y=230)

    registerlbl_password = Label(registerWindow, text="Password:", fg="red",font=("Helvetica", 12) )
    registerlbl_password.place(x=270,y=270)

    registertxt_password = Entry(registerWindow, fg="black", font=("Helvetica", 10), show="*", width=35, relief="raised" )
    registertxt_password.place(x=270,y=300)

    registerlbl_confpassword = Label(registerWindow, text="Confirm Password:", fg="red",font=("Helvetica", 12) )
    registerlbl_confpassword.place(x=270,y=340)

    registertxt_confpassword = Entry(registerWindow, fg="black", font=("Helvetica", 10), show="*", width=35, relief="raised" )
    registertxt_confpassword.place(x=270,y=370)

    registarButtonRegister= Button(registerWindow, text="Register", width="10", font=("Helvetica", 12), fg="red")
    registarButtonRegister.place(x=420, y= 400)

    menuButton= Button(registerWindow, text="Back", width="10", font=("Helvetica", 12), fg="red", command = voltar)
    menuButton.place(x=270, y= 400)

def main_page ():

    def recipe_page ():

        def back():
            top_window.destroy()
            window.update()
            window.deiconify()
            

        window.withdraw()

        top_window = Toplevel()
        top_window.geometry("800x600")
        top_window.title("Which category ?")



        frame2= Frame(top_window)
       


        #Back button
        back_button = Button(frame2, text="Back", command=back)
        back_button.place(x=750, y=7)

        #Categorias
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

        

    window = Toplevel()
    window.geometry("800x600")
    window.title("Home Page")

    frame = Frame(window)
    frame.pack()
    
    

    add_new_recipe = Button(frame, text="Add new recipe" , command=recipe_page)
    add_new_recipe.pack(side = TOP)
        

window = Tk()  #invoca classe tk, cria a "main window"
window.geometry("800x600")
window.title("Projeto de AED")

original_frame= Frame(window)
window.configure(bg="#DBE2AC")

lbl_login = Label(window, text="Login", fg="red", font=("Helvetica", 30))
lbl_login.place(x=330,y=80)

lbl_username = Label(window, text="Email:", fg="red", font=("Helvetica", 12) )
lbl_username.place(x=270,y=200)

txt_username = Entry(window,  fg="black", font=("Helvetica", 10), width=35, relief="raised" )
txt_username.place(x=270,y=230)

lbl_password = Label(window, text="Password:", fg="red",font=("Helvetica", 12) )
lbl_password.place(x=270,y=270)

txt_password = Entry(window, fg="black", font=("Helvetica", 10), show="*", width=35, relief="raised" )
txt_password.place(x=270,y=300)


loginButton= Button(window, text="Login", width="10", font=("Helvetica", 12), fg="red", command = main_page)
loginButton.place(x=420, y= 400)

registarButton= Button(window, text="Register", width="10", font=("Helvetica", 12), fg="red", command = janelaRegistar)
registarButton.place(x=270, y= 400)

 

window.mainloop()