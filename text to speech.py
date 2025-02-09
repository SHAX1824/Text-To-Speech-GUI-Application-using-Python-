import tkinter as tk
from tkinter import *
import pyttsx3

engine=pyttsx3.init()
def speaknow():
    engine.setProperty('rate', 120)
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()
root = Tk()
textv=StringVar()

obj=LabelFrame(root,text="Text to Speech by Shashank M Aradhya",font=20,bd=1,bg="grey",fg="white")
obj.pack(fill="both",expand="yes",padx=10,pady=10)
lbl=Label(obj,text="Enter Text",font=20,bg="black",fg="white")
lbl.pack(side=tk.LEFT,padx=5)

text=Entry(obj,textvariable=textv,font=30,width=25,bd=5)
text.pack(side=tk.LEFT,padx=10)

btn=Button(obj,text="Speak",font=20,bg="white",fg="black",command=speaknow)
btn.pack(side=tk.LEFT,padx=10)

root.title("Text to Speech")
root.iconbitmap("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.shutterstock.com%2Fsearch%2Fconversational-ai-icon%3Fimage_type%3Dvector&psig=AOvVaw0lkF_ZRz0c6MvHGnQ6Ldv3&ust=1739170588117000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCPi5pbuBtosDFQAAAAAdAAAAABAE")
root.geometry("600x300")
root.resizable(False, False)
root.mainloop()







