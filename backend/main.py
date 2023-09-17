from tkinter import PhotoImage
import customtkinter as ctk
from PIL import Image, ImageTk

# Create the Custom Tkinter Window
ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.geometry("1920x1080")

# page = ctk.CTkLabel(master=root, font=('Ariel', 18))
# page.pack()  

def nav1_clicked():
    background = ctk.CTkFrame(master=root, width=950, height=1080, fg_color='#242424')
    background.place(relx=0.667, rely=0.5, anchor="center")
    income = ctk.CTkFrame(master=root, width=390, height=250)
    income.place(relx=0.5+0.025, rely=0.1, anchor='n')
    global current_income
    def edit_income():
        global current_income
        current_income.configure(text='$'+str(income_input.get()))
    income_title = ctk.CTkLabel(master=income, text="Income", font=('Ariel', 18))
    income_title.place(relx=0.5, rely=0.1, anchor='n')
    current_income = ctk.CTkLabel(master=income, width=200, height=50, text='$0', font=("Ariel", 25))
    current_income.place(relx=0.5, rely=0.25, anchor='n')
    income_input = ctk.CTkEntry(master=income, width=200, height=40)
    income_input.place(relx=0.5, rely=0.65, anchor='s')
    income_button = ctk.CTkButton(master=income, width=200, height=40, text="Change Income", command=edit_income, font=('Ariel', 14))
    income_button.place(relx=0.5, rely=0.9, anchor='s')

    goals = ctk.CTkFrame(master=root, width=390, height=250)
    goals.place(relx=0.833-0.025, rely=0.1, anchor='n')
    global current_goals
    def edit_goals():
        global current_goals
        current_goals.configure(text=goals_input.get())
    goals_title = ctk.CTkLabel(master=goals, text="Goal", font=('Ariel', 18))
    goals_title.place(relx=0.5, rely=0.1, anchor='n')
    current_goals = ctk.CTkLabel(master=goals, width=200, height=50, text='No current goals', font=("Ariel", 25))
    current_goals.place(relx=0.5, rely=0.25, anchor='n')
    goals_input = ctk.CTkEntry(master=goals, width=200, height=40)
    goals_input.place(relx=0.5, rely=0.65, anchor='s')
    goals_button = ctk.CTkButton(master=goals, width=200, height=40, text="Change Goal", command=edit_goals, font=('Ariel', 14))
    goals_button.place(relx=0.5, rely=0.9, anchor='s')

    spending = ctk.CTkFrame(master=root, width=800, height=60)
    spending.place(relx=0.6667, rely=0.4, anchor='n')
    spending_text = ctk.CTkLabel(master=spending, text="Spending Charts", height=60, font=("Arial", 16))
    spending_text.place(relx=0.1, rely=0.5, anchor='center')
def nav2_clicked():
    background = ctk.CTkFrame(master=root, width=950, height=1080, fg_color='#242424')
    background.place(relx=0.667, rely=0.5, anchor="center")
    test = ctk.CTkLabel(master=root, text="insight")
    test.place(relx=0.667, rely=0.5, anchor='center')
def nav3_clicked():
    background = ctk.CTkFrame(master=root, width=950, height=1080, fg_color='#242424')
    background.place(relx=0.667, rely=0.5, anchor="center")
    test = ctk.CTkLabel(master=root, text="my vision")
    test.place(relx=0.667, rely=0.5, anchor='center')



# if page1:
#     income = ctk.CTkFrame(master=root, width=390, height=250)
#     income.place(relx=0.5+0.025, rely=0.1, anchor='n')
#     global current_income
#     def edit_income():
#         global current_income
#         current_income.configure(text='$'+str(income_input.get()))
#     income_title = ctk.CTkLabel(master=income, text="Income", font=('Ariel', 18))
#     income_title.place(relx=0.5, rely=0.1, anchor='n')
#     current_income = ctk.CTkLabel(master=income, width=200, height=50, text='$0', font=("Ariel", 25))
#     current_income.place(relx=0.5, rely=0.25, anchor='n')
#     income_input = ctk.CTkEntry(master=income, width=200, height=40)
#     income_input.place(relx=0.5, rely=0.65, anchor='s')
#     income_button = ctk.CTkButton(master=income, width=200, height=40, text="Change Income", command=edit_income, font=('Ariel', 14))
#     income_button.place(relx=0.5, rely=0.9, anchor='s')

#     goals = ctk.CTkFrame(master=root, width=390, height=250)
#     goals.place(relx=0.833-0.025, rely=0.1, anchor='n')
#     global current_goals
#     def edit_goals():
#         global current_goals
#         current_goals.configure(text=goals_input.get())
#     goals_title = ctk.CTkLabel(master=goals, text="Goal", font=('Ariel', 18))
#     goals_title.place(relx=0.5, rely=0.1, anchor='n')
#     current_goals = ctk.CTkLabel(master=goals, width=200, height=50, text='No current goals', font=("Ariel", 25))
#     current_goals.place(relx=0.5, rely=0.25, anchor='n')
#     goals_input = ctk.CTkEntry(master=goals, width=200, height=40)
#     goals_input.place(relx=0.5, rely=0.65, anchor='s')
#     goals_button = ctk.CTkButton(master=goals, width=200, height=40, text="Change Goal", command=edit_goals, font=('Ariel', 14))
#     goals_button.place(relx=0.5, rely=0.9, anchor='s')

#     spending = ctk.CTkFrame(master=root, width=800, height=60)
#     spending.place(relx=0.6667, rely=0.4, anchor='n')
#     spending_text = ctk.CTkLabel(master=spending, text="Spending Charts", height=60, font=("Arial", 16))
#     spending_text.place(relx=0.1, rely=0.5, anchor='center')
# elif page2:
#     #show second page
#     spending_text = ctk.CTkLabel(master=root, text="ss Charts", height=60, font=("Arial", 16))
#     spending_text.place(relx=0.1, rely=0.8, anchor='center')
#     test = ctk.CTkLabel(master=root, text="insight")
#     test.place(relx=0.667, rely=0.5, anchor='center')
# elif page3:
#     #show vision page
#     test = ctk.CTkLabel(master=root, text="my vision")
#     test.place(relx=0.667, rely=0.5, anchor='center')



# Create the sidebar housing main functionalities
sidebar = ctk.CTkFrame(master=root, width=610, height=1080, border_width=1, border_color='white')
sidebar.place(relx=0.125, rely=0.5, anchor='center')

# Nav Logo
logo = Image.open("./public/logo192.png")
resize_logo = logo.resize((300,100))
img = ImageTk.PhotoImage(resize_logo)
nav_logo = ctk.CTkButton(master=root, width=300, height=50, image=img, hover=False, text=None, command=nav1_clicked)
nav_logo.place(relx=0.1666, rely=0.1, anchor='center')

# Nav Buttons
nav_button1 = ctk.CTkButton(master=root, width=400, height=50, text="Home", command=nav1_clicked)
nav_button1.place(relx=0.1666, rely=0.18, anchor='center')
nav_button2 = ctk.CTkButton(master=root, width=400, height=50, text="Insight", command=nav2_clicked)
nav_button2.place(relx=0.1666, rely=0.26, anchor='center')
nav_button3 = ctk.CTkButton(master=root, width=400, height=50, text="My Vision", command=nav3_clicked)
nav_button3.place(relx=0.1666, rely=0.34, anchor='center')

root.attributes('-fullscreen', True)
root.mainloop()