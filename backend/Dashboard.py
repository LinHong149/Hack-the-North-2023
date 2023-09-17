import customtkinter as ctk

# Create the Custom Tkinter Window
ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.geometry('1920x1080')

mainframe = ctk.CTkFrame(master=root, width=1920, height=1080, border_width=2, fg_color='#4831D4')
mainframe.place(relx=0.5, rely=0.5, anchor='center')

info_frame = ctk.CTkFrame(master=mainframe, width=1500, height=600, fg_color='#4831D4', border_color='#4831D4', border_width=0, corner_radius=20)
info_frame.place(relx=0.5, rely=0.6, anchor='center')

header_frame = ctk.CTkFrame(master=mainframe, width=1920, height=180, fg_color='#4831D4', border_color='#4831D4', border_width=0)
header_frame.place(relx=0.5, rely=0.075, anchor='center')

top_info_frame = ctk.CTkFrame(master=info_frame, width=1500, height=150, fg_color='#4831D4', border_color='#4831D4', border_width=0, corner_radius=0)
top_info_frame.place(relx=0.5, rely=0.125, anchor='center')

bot_info_frame = ctk.CTkFrame(master=info_frame, width=1500, height=450, fg_color='#4831D4', border_color='#4831D4', border_width=0, corner_radius=0)
bot_info_frame.place(relx=0.5, rely=0.625, anchor='center')

home_btn = ctk.CTkButton(master=header_frame, text = "Home", width=480, height=150, text_color='white', fg_color='transparent', corner_radius=0, font=('Courier New', 24, 'bold'), hover_color='dark blue')
home_btn.place(relx=0.25, rely=0.55, anchor='center')

budget_btn = ctk.CTkButton(master=header_frame, text = "Budget", width=480, height=150, text_color='white', fg_color='transparent', corner_radius=0, font=('Courier New', 24, 'bold'), hover_color='dark blue')
budget_btn.place(relx=0.5, rely=0.55, anchor='center')

vision_btn = ctk.CTkButton(master=header_frame, text = "My Vision", width=480, height=150, text_color='white', fg_color='transparent', corner_radius=0, font=('Courier New', 24, 'bold'), hover_color='dark blue')
vision_btn.place(relx=0.75, rely=0.55, anchor='center')

root.attributes('-fullscreen', True)
root.mainloop()

