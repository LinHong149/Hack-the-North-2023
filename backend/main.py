import customtkinter as ctk

# Create the Custom Tkinter Window
ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.geometry("1920x1080")

# Create the sidebar housing main functionalities
sidebar = ctk.CTkFrame(master=root, width=610, height=1080, border_width=1, border_color='white')
sidebar.place(relx=0.125, rely=0.5, anchor='center')

root.mainloop()