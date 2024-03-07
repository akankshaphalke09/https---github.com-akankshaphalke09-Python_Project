import tkinter as tk
class demo:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("application")
        self.root.geometry("800x600")
        self.canvas=tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.ui()
    def ui(self):
        self.label1 = tk.Label(self.root, text="Full Name:", anchor="w")
        self.label1.place(x=50, y=10, width=100, height=30)

        self.entry1 = tk.Entry(self.root)
        self.entry1.place(x=180, y=10, width=200, height=30)

        self.label2 = tk.Label(self.root, text="Age:", anchor="w")
        self.label2.place(x=50, y=60, width=100, height=30)

        self.entry2 = tk.Entry(self.root)
        self.entry2.place(x=180, y=60, width=200, height=30)

        self.label3 = tk.Label(self.root, text="Email:", anchor="w")
        self.label3.place(x=50, y=110, width=100, height=30)

        self.entry3 = tk.Entry(self.root)
        self.entry3.place(x=180, y=110, width=200, height=30)


        self.checkbox_var = tk.BooleanVar()
        self.checkbox_var.set(False)

        self.checkbox = tk.Checkbutton(self.root, text="Enable Feature", variable=self.checkbox_var, command=self.on_tick)
        self.checkbox.place(x=0, y=170, width=200, height=30,anchor="w")

        self.label6 = tk.Label(self.root, text="", anchor="w")
        self.label6.place(x=50, y=420, width=100, height=30)




      

    def on_tick(self):
        
        self.label4 = tk.Label(self.root, text="Company Name:", anchor="w")
        self.label4.place(x=50, y=230, width=100, height=30)

        self.entry4 = tk.Entry(self.root)
        self.entry4.place(x=180, y=230, width=200, height=30)

        self.label5 = tk.Label(self.root, text="Package:", anchor="w")
        self.label5.place(x=50, y=290, width=100, height=30)

        self.entry5 = tk.Entry(self.root)
        self.entry5.place(x=180, y=290, width=200, height=30)

        self.btn=tk.Button(self.root,text="Generate Card",bg="green",command=self.card)
        self.btn.place(x=50, y=360, width=330, height=30,anchor="w")
    def card(self):
        self.canvas.create_rectangle(10, 400, 790, 570, outline="black", fill="white")
        multiline_text = "Full Name : {}\nAge : {}\nEmail : {}\nCompany Name : {}\nPackage : {} ".format(self.entry1.get(),self.entry2.get(),self.entry3.get(),self.entry4.get(),self.entry5.get())
        self.label = tk.Label(self.root, text=multiline_text, justify="left", padx=10, pady=10, fg="white" ,bg="green")
        self.label.place(x=20, y=430)

   

    

    def run(self):
        self.root.mainloop()
if __name__=="__main__":
    app=demo()
    app.run()