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


loginButton= Button(window, text="Login", width="10", font=("Helvetica", 12), fg="red")
loginButton.place(x=420, y= 400)

registarButton= Button(window, text="Register", width="10", font=("Helvetica", 12), fg="red", command = janelaRegistar)
registarButton.place(x=270, y= 400)




window.mainloop() 

    