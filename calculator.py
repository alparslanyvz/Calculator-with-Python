# Calculator with Python. | github.com/alparslanyvz 
#---------------------------------------------------------------------
# Modules
import customtkinter as ctk 
from customtkinter import *
import tkinter as tk 
from tkinter import *

class Calculator():
    def __init__(self) -> None:
        self.window1_geomerty = "270x425+400+200"
        self.window1_title = "Calculator"

        self.number = None
        self.process = None
        self.entryBoxFontSize = 28       
        self.main_frame()
    #binds
    def on_kp0(self,event=None):
        self.b0_d()
    def on_kp1(self,event=None):
        self.b1_d()
    def on_kp2(self,event=None):
        self.b2_d()
    def on_kp3(self,event=None):
        self.b3_d()
    def on_kp4(self,event=None):
        self.b4_d()
    def on_kp5(self,event=None):
        self.b5_d()
    def on_kp6(self,event=None):
        self.b6_d()
    def on_kp7(self,event=None):
        self.b7_d()
    def on_kp8(self,event=None):
        self.b8_d()
    def on_kp9(self,event=None):
        self.b1_d()
    def on_kpComma(self,event=None):
        self.Comma()
    def on_kpAddition(self,event=None):
        self.Addition()
    def on_kpSubtraction(self,event=None):
        self.Subtraction()
    def on_kpMultiplication(self,event=None):
        self.Multiplication()
    def on_kpDivision(self,event=None):
        self.Division()
    def on_kpEqual(self,event=None):
        self.Equal()
    def on_kpDelete(self,event=None):
        self.delete()

    def main_frame(self):
        ctk.set_appearance_mode("dark") # Dark Theme
        self.window1 = ctk.CTk()
        self.window1.geometry(self.window1_geomerty)
        self.window1.title(self.window1_title)
        self.window1.configure(fg_color="black")
        self.window1.resizable(False,False)

        #TextBox
        self.numberBox = CTkEntry(master=self.window1,width=230,height=50,justify="right",font=CTkFont(family="Arial",size=self.entryBoxFontSize),border_color="#cd853f",border_width=1,fg_color="black",text_color="white")
        self.numberBox.place(x=20,y=45)
        #Process Label
        self.processLabel = CTkLabel(master=self.window1,text="",fg_color="black",text_color="gray",font=CTkFont(family="Arial",size=16),justify="right")
        self.processLabel.place(x=20,y=10)

        #numbers
        self.b0 = CTkButton(master=self.window1,text="0",font=CTkFont(family="Arial",size=28),width=110,height=50,fg_color="#363636",hover_color="gray",corner_radius=0,command=self.b0_d) #  0
        self.b0.place(x=20,y=350)
        self.bComma = CTkButton(master=self.window1,text=",",font=CTkFont(family="Arial",size=28),width=50,height=50,fg_color="#363636",hover_color="gray",corner_radius=0,command=self.Comma) # ,
        self.bComma.place(x=140,y=350)
        self.b1 = CTkButton(master=self.window1,text="1",font=CTkFont(family="Arial",size=28),width=50,height=50,fg_color="#363636",hover_color="gray",corner_radius=0,command=self.b1_d) # 1
        self.b1.place(x=20,y=290)
        self.b2 = CTkButton(master=self.window1,text="2",font=CTkFont(family="Arial",size=28),width=50,height=50,fg_color="#363636",hover_color="gray",corner_radius=0,command=self.b2_d) # 2
        self.b2.place(x=80,y=290)
        self.b3 = CTkButton(master=self.window1,text="3",font=CTkFont(family="Arial",size=28),width=50,height=50,fg_color="#363636",hover_color="gray",corner_radius=0,command=self.b3_d) # 3
        self.b3.place(x=140,y=290)
        self.b4 = CTkButton(master=self.window1,text="4",font=CTkFont(family="Arial",size=28),width=50,height=50,fg_color="#363636",hover_color="gray",corner_radius=0,command=self.b4_d) # 4
        self.b4.place(x=20,y=230)
        self.b5 = CTkButton(master=self.window1,text="5",font=CTkFont(family="Arial",size=28),width=50,height=50,fg_color="#363636",hover_color="gray",corner_radius=0,command=self.b5_d) # 5
        self.b5.place(x=80,y=230)
        self.b6 = CTkButton(master=self.window1,text="6",font=CTkFont(family="Arial",size=28),width=50,height=50,fg_color="#363636",hover_color="gray",corner_radius=0,command=self.b6_d) # 6
        self.b6.place(x=140,y=230)
        self.b7 = CTkButton(master=self.window1,text="7",font=CTkFont(family="Arial",size=28),width=50,height=50,fg_color="#363636",hover_color="gray",corner_radius=0,command=self.b7_d) # 7
        self.b7.place(x=20,y=170)
        self.b8 = CTkButton(master=self.window1,text="8",font=CTkFont(family="Arial",size=28),width=50,height=50,fg_color="#363636",hover_color="gray",corner_radius=0,command=self.b8_d) # 8
        self.b8.place(x=80,y=170)
        self.b9 = CTkButton(master=self.window1,text="9",font=CTkFont(family="Arial",size=28),width=50,height=50,fg_color="#363636",hover_color="gray",corner_radius=0,command=self.b9_d) # 9
        self.b9.place(x=140,y=170)
        # action buttons
        self.bEqual = CTkButton(master=self.window1,text="=",font=CTkFont(family="Arial",size=28),width=50,height=50,fg_color="#cd853f",hover_color="orange",corner_radius=0,command=self.Equal) # = 
        self.bEqual.place(x=200,y=350)
        self.bAddition = CTkButton(master=self.window1,text="+",font=CTkFont(family="Arial",size=28),width=50,height=50,fg_color="#cd853f",hover_color="orange",corner_radius=0,command=self.Addition) # +
        self.bAddition.place(x=200,y=290)
        self.bSubtraction = CTkButton(master=self.window1,text="-",font=CTkFont(family="Arial",size=28),width=50,height=50,fg_color="#cd853f",hover_color="orange",corner_radius=0,command=self.Subtraction) # -
        self.bSubtraction.place(x=200,y=230)
        self.bMultiplication = CTkButton(master=self.window1,text="x",font=CTkFont(family="Arial",size=28),width=50,height=50,fg_color="#cd853f",hover_color="orange",corner_radius=0,command=self.Multiplication) # x
        self.bMultiplication.place(x=200,y=170)
        self.bDivision = CTkButton(master=self.window1,text="/",font=CTkFont(family="Arial",size=28),width=50,height=50,fg_color="#cd853f",hover_color="orange",corner_radius=0,command=self.Division) # /
        self.bDivision.place(x=200,y=110)
        self.b10 = CTkButton(master=self.window1,text="Del",font=CTkFont(family="Arial",size=28),width=50,height=50,fg_color="#9c9c9c",hover_color="gray",corner_radius=0,command=self.delete) # delete
        self.b10.place(x=140,y=110)
        self.b11 = CTkButton(master=self.window1,text=" ",font=CTkFont(family="Arial",size=28),width=50,height=50,fg_color="#9c9c9c",hover_color="gray",corner_radius=0) # 
        self.b11.place(x=80,y=110)
        self.b12 = CTkButton(master=self.window1,text="AC",font=CTkFont(family="Arial",size=28),width=50,height=50,fg_color="#9c9c9c",hover_color="gray",corner_radius=0,command=self.ac) # AC
        self.b12.place(x=20,y=110)
        # binds
        self.window1.bind("<Key-0>",self.on_kp0)
        self.window1.bind("<Key-1>",self.on_kp1)
        self.window1.bind("<Key-2>",self.on_kp2)
        self.window1.bind("<Key-3>",self.on_kp3)
        self.window1.bind("<Key-4>",self.on_kp4)
        self.window1.bind("<Key-5>",self.on_kp5)
        self.window1.bind("<Key-6>",self.on_kp6)
        self.window1.bind("<Key-7>",self.on_kp7)
        self.window1.bind("<Key-8>",self.on_kp8)
        self.window1.bind("<Key-9>",self.on_kp9)
        self.window1.bind("<comma>",self.on_kpComma)
        self.window1.bind("<plus>",self.on_kpAddition)
        self.window1.bind("<minus>",self.on_kpSubtraction)
        self.window1.bind("<asterisk>",self.on_kpMultiplication)
        self.window1.bind("<slash>",self.on_kpDivision)
        self.window1.bind("<Return>",self.on_kpEqual)
        self.window1.bind("<BackSpace>",self.on_kpDelete)
        self.window1.mainloop()

    #Actions
    #=
    def Equal(self):
        if self.numberBox.get().endswith("+" or "-" or "/" or "*"):
            pass
        else:
            self.lastProcess =  eval(self.numberBox.get())
            self.numberBox.delete(0,END)
            self.numberBox.insert(tk.END,f"{self.lastProcess}")
        try:
            self.processLabel.destroy()
        except:
            pass
        self.processLabel = CTkLabel(master=self.window1,text=f"{self.numberBox.get()}",fg_color="black",text_color="gray",font=CTkFont(family="Arial",size=16),justify="right")
        self.processLabel.place(x=20,y=10)
        
    #+    
    def Addition(self):
        if self.numberBox.get().endswith("+" or "-" or "/" or "*"):
            pass
        else: 
            if len(self.numberBox.get()) < 1:
                self.numberBox.insert(tk.END,"+")
            else:
                if self.numberBox.get().startswith("0") and ',' not in self.numberBox.get():
                    self.numberBox.delete(0,END)
                    self.numberBox.insert(tk.END,"+")
                else:
                    self.numberBox.insert(tk.END,"+")
    #-
    def Subtraction(self):
        if self.numberBox.get().endswith("+" or "-" or "/" or "*"):
            pass
        else:
            if len(self.numberBox.get()) < 1:
                self.numberBox.insert(tk.END,"-")
            else:
                if self.numberBox.get().startswith("0") and ',' not in self.numberBox.get():
                    self.numberBox.delete(0,END)
                    self.numberBox.insert(tk.END,"-")
                else:
                    self.numberBox.insert(tk.END,"-")
    #x
    def Multiplication(self):
        if self.numberBox.get().endswith("+" or "-" or "/" or "*"):
            pass
        else:
            if len(self.numberBox.get()) < 1:
                self.numberBox.insert(tk.END,"*")
            else:
                if self.numberBox.get().startswith("0") and ',' not in self.numberBox.get():
                    self.numberBox.delete(0,END)
                    self.numberBox.insert(tk.END,"*")
                else:
                    self.numberBox.insert(tk.END,"*")
    #/
    def Division(self):
        if self.numberBox.get().endswith("+" or "-" or "/" or "*"):
            pass
        else:
            if len(self.numberBox.get()) < 1:
                self.numberBox.insert(tk.END,"/")
            else:
                if self.numberBox.get().startswith("0") and '.' not in self.numberBox.get():
                    self.numberBox.delete(0,END)
                    self.numberBox.insert(tk.END,"/")
                else:
                    self.numberBox.insert(tk.END,"/")


    def b0_d(self):
        if len(self.numberBox.get()) < 1:
            self.numberBox.insert(tk.END,"0")
        else:
            if self.numberBox.get().startswith("0") and '.' not in self.numberBox.get():
                self.numberBox.delete(0,END)
                self.numberBox.insert(tk.END,"0")
            else:
                self.numberBox.insert(tk.END,"0")
    
    def b1_d(self):
        if len(self.numberBox.get()) < 1:
            self.numberBox.insert(tk.END,"1")
        else:
            if self.numberBox.get().startswith("0") and '.' not in self.numberBox.get():
                self.numberBox.delete(0,END)
                self.numberBox.insert(tk.END,"1")
            else:
                self.numberBox.insert(tk.END,"1")
    
    def b2_d(self):
        if len(self.numberBox.get()) < 1:
            self.numberBox.insert(tk.END,"2")
        else:
            if self.numberBox.get().startswith("0") and '.' not in self.numberBox.get():
                self.numberBox.delete(0,END)
                self.numberBox.insert(tk.END,"2")
            else:
                self.numberBox.insert(tk.END,"2")
    
    def b3_d(self):
        if len(self.numberBox.get()) < 1:
            self.numberBox.insert(tk.END,"3")
        else:
            if self.numberBox.get().startswith("0") and '.' not in self.numberBox.get():
                self.numberBox.delete(0,END)
                self.numberBox.insert(tk.END,"3")
            else:
                self.numberBox.insert(tk.END,"3")
    
    def b4_d(self):
        if len(self.numberBox.get()) < 1:
            self.numberBox.insert(tk.END,"4")
        else:
            if self.numberBox.get().startswith("0") and '.' not in self.numberBox.get():
                self.numberBox.delete(0,END)
                self.numberBox.insert(tk.END,"4")
            else:
                self.numberBox.insert(tk.END,"4")
    
    def b5_d(self):
        if len(self.numberBox.get()) < 1:
            self.numberBox.insert(tk.END,"5")
        else:
            if self.numberBox.get().startswith("0") and '.' not in self.numberBox.get():
                self.numberBox.delete(0,END)
                self.numberBox.insert(tk.END,"5")
            else:
                self.numberBox.insert(tk.END,"5")

    def b6_d(self):
        if len(self.numberBox.get()) < 1:
            self.numberBox.insert(tk.END,"6")
        else:
            if self.numberBox.get().startswith("0") and '.' not in self.numberBox.get():
                self.numberBox.delete(0,END)
                self.numberBox.insert(tk.END,"6")
            else:
                self.numberBox.insert(tk.END,"6")

    def b7_d(self):
        if len(self.numberBox.get()) < 1:
            self.numberBox.insert(tk.END,"7")
        else:
            if self.numberBox.get().startswith("0") and '.' not in self.numberBox.get():
                self.numberBox.delete(0,END)
                self.numberBox.insert(tk.END,"7")
            else:
                self.numberBox.insert(tk.END,"7")

    def b8_d(self):
        if len(self.numberBox.get()) < 1:
            self.numberBox.insert(tk.END,"8")
        else:
            if self.numberBox.get().startswith("0") and '.' not in self.numberBox.get():
                self.numberBox.delete(0,END)
                self.numberBox.insert(tk.END,"8")
            else:
                self.numberBox.insert(tk.END,"8")

    def b9_d(self):
        if len(self.numberBox.get()) < 1:
            self.numberBox.insert(tk.END,"9")
        else:
            if self.numberBox.get().startswith("0") and '.' not in self.numberBox.get():
                self.numberBox.delete(0,END)
                self.numberBox.insert(tk.END,"9")
            else:
                self.numberBox.insert(tk.END,"9")
        
    def Comma(self):
        if len(self.numberBox.get()) < 1:
            pass
        else:
            if self.numberBox.get().count(".") < 1:
                self.numberBox.insert(tk.END,".")
            else:
                if self.numberBox.get().count("+"or"-"or"*"or"/") >= 1:
                    if self.numberBox.get().endswith(".") or self.numberBox.get().endswith("+" or "-" or "/" or "*"):
                        pass
                    else:
                        self.numberBox.insert(tk.END,".")
                else:
                    pass

    def delete(self): # To delete the last character
        del_1 = self.numberBox.get()[:-1]
        self.numberBox.delete(0,END)
        self.numberBox.insert(tk.END,del_1)

    def ac(self): # To clear the numberBox
        self.numberBox.delete(0,END)
        try:
            self.processLabel.destroy()
        except:
            pass
app_exe = Calculator()