from tkinter import*
root=Tk()
root.geometry("500x500")

input_1=Entry(root)
input_1.place(relx=0.5 , rely=0.6 , anchor=CENTER)

def error():
    number = 5
    a=input_1.get()
 
    
    label_2["text"]=a
    
    try:
        print(a + input_1)
        
        
    except(TypeError):
            messagebox.showinfo("error")


label_1=Label(root,text="Errores")
label_1.place(relx=0.5 , rely=0.5 , anchor=CENTER)
label_2=Label(root,text="a")
label_2.place(relx=0.5 , rely=0.4 , anchor=CENTER)
button_1=Button(root,text="Dame click", command=error)
button_1.place(relx=0.5 , rely=0.3 , anchor=CENTER)

root.mainloop()