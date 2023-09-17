from tkinter import PhotoImage
import customtkinter as ctk
from PIL import Image, ImageTk

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
nav_button2 = ctk.CTkButton(master=root, width=400, height=50, text="insight", command=nav2_clicked)
nav_button2.place(relx=0.1666, rely=0.26, anchor='center')
nav_button3 = ctk.CTkButton(master=root, width=400, height=50, text="My Vision", command=nav3_clicked)
nav_button3.place(relx=0.1666, rely=0.34, anchor='center')


if showPage == "home":
    #show home
    test = ctk.CTkLabel(master=root, text="home")
    test.place(relx=0.667, rely=0.5, anchor='center')
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