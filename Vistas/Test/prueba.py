import customtkinter as ctk

app = ctk.CTk()
frame = ctk.CTkFrame(app, corner_radius=20, fg_color="red")
frame.pack(fill="both", expand=True, padx=20, pady=20)

app.mainloop()
