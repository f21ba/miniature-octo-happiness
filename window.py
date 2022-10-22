import tkinter as tk

root = tk.Tk()
root.geometry('600x400')

message = tk.Message(root, text="Hellow World!!",
                     font=("",20), bg="#faaaff")
message.pack()

label = tk.Label(root, text="Hellow World!!",
                 font=("",20), bg="#aafaff")
label.pack(pady=10)

root.mainloop()