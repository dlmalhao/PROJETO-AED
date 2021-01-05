from tkinter import *

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

        window.mainloop()

    window = Tk()
    window.geometry("800x600")
    window.title("Home Page")

    frame = Frame(window)
    frame.pack()
    
    

    add_new_recipe = Button(frame, text="Add new recipe" , command=recipe_page)
    add_new_recipe.pack(side = TOP)

    window.mainloop()


    


main_page() 