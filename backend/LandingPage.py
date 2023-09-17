import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import PhotoImage

# Create the Custom Tkinter Window
ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.geometry('1920x1080')

logo = Image.open('./assets/LogoWhite.png')
resize_logo = logo.resize((600,600))
img = ImageTk.PhotoImage(resize_logo)

frame = ctk.CTkFrame(master=root, width=1920, height=1080)
frame.place(relx=0.5, rely=0.5, anchor='center')

main_scr_label = ctk.CTkLabel(master=frame, width=1920, height=1080, image=img, text='', fg_color='#4831D4')
main_scr_label.pack()

main_screen_btn = ctk.CTkButton(master=frame, font=('Courier New', 24, 'bold'), width=300, height=50, text="CONTINUE", fg_color='#4831D4', hover_color='dark blue', corner_radius=0)
main_screen_btn.place(relx=0.5, rely=0.9, anchor='center')

header_btn = ctk.CTkButton(master=frame, width=400, height=100, text="Wallet Wise", fg_color='#4831D4', border_color='#4831D4', font=('Courier New', 52, 'bold'), corner_radius=0)
header_btn.place(relx=0.5, rely=0.1, anchor='center')

root.attributes('-fullscreen', True)
root.mainloop()
