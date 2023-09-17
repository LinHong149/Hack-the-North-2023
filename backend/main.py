from tkinter import PhotoImage
import customtkinter as ctk
from PIL import Image, ImageTk
import copy

# Create the Custom Tkinter Window
ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.geometry("1920x1080")

showPage = "home"
def nav1_clicked():
    showPage = "home"
def nav2_clicked():
    showPage = "insight"
def nav3_clicked():
    showPage = "my_vision"

# Create the sidebar housing main functionalities
sidebar = ctk.CTkFrame(master=root, width=610, height=1080, border_width=1, border_color='white')
sidebar.place(relx=0.125, rely=0.5, anchor='center')

# Nav Logo
logo = Image.open("./public/logo192.png")
resize_logo = logo.resize((300,100))
img = ImageTk.PhotoImage(resize_logo)
# logo = PhotoImage(file="./public/logo192.png")
# logo = logo.resize((10))
nav_logo = ctk.CTkButton(master=root, width=300, height=50, image=img, hover=False, text=None, command=nav1_clicked)
nav_logo.place(relx=0.1666, rely=0.1, anchor='center')

# Nav Buttons
nav_button1 = ctk.CTkButton(master=root, width=400, height=50, text="Home", command=nav1_clicked)
nav_button1.place(relx=0.1666, rely=0.18, anchor='center')
nav_button2 = ctk.CTkButton(master=root, width=400, height=50, text="Insight", command=nav2_clicked)
nav_button2.place(relx=0.1666, rely=0.26, anchor='center')
nav_button3 = ctk.CTkButton(master=root, width=400, height=50, text="My Vision", command=nav3_clicked)
nav_button3.place(relx=0.1666, rely=0.34, anchor='center')



global current_income
current_income = 0
current_goal = "No current goal"    

# class EditIncome(ctk.CTkFrame):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.income_input = ctk.CTkEntry(self, width=200)
#         self.income_input.grid(row=1, column=0, padx=30, pady=(30, 10))
#         self.income_submit = ctk.CTkButton(self, width=200, text="Submit")
#         self.income_submit.grid(row=2, column=0, padx=30, pady=(10, 30))
        

def edit_income():
    # income_popup = EditIncome(master=root)
    # income_popup.place(relx=0.6667, rely=0.5, anchor='center')
    return current_income + 1

    
class IncomeWidget(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.income_title = ctk.CTkLabel(self, text="Income", width=350)
        self.income_title.grid(row=1, column=0, padx=10, pady=(30, 10))

        self.income_amount = ctk.CTkLabel(self, text="$"+str(current_income))
        self.income_amount.grid(row=2, column=0, padx=10, pady=0)

        self.income_button = ctk.CTkButton(self, text="Edit Income")
        self.income_button.grid(row=3, column=0, padx=10, pady=(10, 30))


class GoalWidget(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.goal_title = ctk.CTkLabel(self, text="Goal", width=350)
        self.goal_title.grid(row=1, column=0, padx=10, pady=(30, 10))
        self.goal_text = ctk.CTkLabel(self, text=current_goal)
        self.goal_text.grid(row=2, column=0, padx=10, pady=0)
        self.goal_button = ctk.CTkButton(self, text="Edit Goal")
        self.goal_button.grid(row=3, column=0, padx=10, pady=(10, 30))

if showPage == "home":
    income = IncomeWidget(master=root)
    income.place(relx=0.5+0.025, rely=0.1, anchor='n')

    goal = GoalWidget(master=root)
    goal.place(relx=0.833-0.025, rely=0.1, anchor='n')

    
    # income_title = ctk.CTkLabel(master=root, text="Income", width=600)
    # income_title.place(relx=0.667, rely=0.1, anchor='nw')
    # income_amount = ctk.CTkLabel(master=root, text=income, width=600)
    # income_amount.place(relx=0.667, rely=0.1, anchor='sw')
    # edit_income = ctk.CTkButton(master=root, width=80, height=40, text="Edit Income")
    # edit_income.place(relx=0.667, rely=0.1, anchor='se')

elif showPage == "insight":
    #show second page
    test = ctk.CTkLabel(master=root, text="insight")
    test.place(relx=0.667, rely=0.5, anchor='center')
elif showPage == "my_vision":
    #show vision page
    test = ctk.CTkLabel(master=root, text="my vision")
    test.place(relx=0.667, rely=0.5, anchor='center')

root.attributes('-fullscreen', True)
root.mainloop()