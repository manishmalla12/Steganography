
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
from stegano import lsb
secret = ""

def open_tool_window():
    welcome_window.destroy()
    
    root = Tk()
    root.title("Steganography Tool")
    root.geometry("900x700")
    root.resizable(False, False)
    root.configure(bg="skyblue")

    def open_image():
        try:
            global filename
            filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("PNG file", "*.png"), ("JPG File", "*.jpg"), ("All File", "*.txt")))
        
            if not filename:
                return  # No file selected
        
            img = Image.open(filename)
            img = img.resize((250, 250), Image.ANTIALIAS)  # Resizing the image to fit the frame size
            img = ImageTk.PhotoImage(img)
            
            lbl.configure(image=img)
            lbl.image = img 
            
        except Exception as e:
            messagebox.showerror("Error", str(e))

            messagebox.showerror("Error", str(e))
            

    def hide():
        try:
            global secret
            if not 'filename' in globals() or not filename:
                messagebox.showwarning("No Image", "Please open an image first.")
                return

            message = text1.get(1.0, END).strip()  # Get the message and remove leading/trailing whitespace and newlines
            
            if not message:
                messagebox.showwarning("No Data", "Please enter some data to hide.")
                return
            
            secret = lsb.hide(str(filename), message)
            messagebox.showinfo("Success", "Data hidden successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    def show():
        try:
            if not 'filename' in globals() or not filename:
                messagebox.showwarning("No Image", "Please open an image first.")
                return
            
            secret = lsb.reveal(filename)
            if secret:
                text1.delete(1.0, END)
                text1.insert(END, secret)
            else:
                messagebox.showinfo("No Hidden Data", "No hidden data found in the image.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    

    def save():
        try:
            if not 'filename' in globals() or not filename:
                messagebox.showwarning("No Image", "Please open an image first.")
                return

            if not secret:
                messagebox.showwarning("No Data", "Please hide some data first.")
                return
            
            filetypes = (("PNG files", "*.png"), ("All files", "*.*"))
            save_path = filedialog.asksaveasfilename(filetypes=filetypes, defaultextension=".png")
            
            if save_path:
                secret.save(save_path)
                messagebox.showinfo("Success", "Image saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def exit_program():
        root.destroy()
        open_welcome_window()

    root.iconphoto(False, PhotoImage(file="icon.png"))

    logo = PhotoImage(file="logo.png")
    Label(root, image=logo, bg="skyblue").place(x=10, y=5)

    logo1 = PhotoImage(file="logo1.png")
    Label(root, image=logo1, bg="skyblue").place(x=100, y=5)

    logo2 = PhotoImage(file="logo2.png")
    Label(root, image=logo2, bg="skyblue").place(x=700, y=5)

    logo3 = PhotoImage(file="logo3.png")
    Label(root, image=logo3, bg="skyblue").place(x=800, y=5)

    logo4 = PhotoImage(file="logo4.png")
    Label(root, image=logo4, bg="skyblue").place(x=30, y=600)

    logo7 = PhotoImage(file="logo7.png")
    Label(root, image=logo7, bg="skyblue").place(x=800, y=620)

    Label(root, text="Hide Your Data", bg="skyblue", fg="Black", font="arial 25 bold").place(x=250, y=20)

    frame1 = Frame(root, bd=3, bg="lightblue", width=350, height=280, relief=GROOVE)
    frame1.place(x=400, y=85)

    lbl = Label(frame1, bg="lightblue")
    lbl.place(x=40, y=10)

    frame2 = Frame(root, bd=3, width=350, height=280, bg="lightblue", relief=GROOVE)
    frame2.place(x=400, y=380)

    text1 = Text(frame2, font="Robote 20", bg="lightblue", fg="black", relief=GROOVE, wrap=WORD)
    text1.place(x=0, y=0, width=320, height=295)

    Scrollbar1 = Scrollbar(frame2)
    Scrollbar1.place(x=320, y=0, height=300)

    Scrollbar1.configure(command=text1.yview)
    text1.configure(yscrollcommand=Scrollbar1.set)

    frame3 = Frame(root, bd=3, bg="skyblue", width=200, height=100, relief=GROOVE)
    frame3.place(x=150, y=120)
    Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=open_image, bg="lightblue").place(x=25, y=15)

    frame4 = Frame(root, bd=3, bg="skyblue", width=200, height=100, relief=GROOVE)
    frame4.place(x=150, y=210)
    Button(frame4, text="Save Image", width=10, height=2, font="arial 14 bold", command=save, bg="lightblue").place(x=25, y=15)
   
    frame6 = Frame(root, bd=3, bg="skyblue", width=200, height=100, relief=GROOVE)
    frame6.place(x=150, y=450)
    Button(frame6, text="Show Data", width=10, height=2, font="arial 14 bold", command=show, bg="lightblue").place(x=25, y=20)

    frame5 = Frame(root, bd=3, bg="skyblue", width=200, height=100, relief=GROOVE)
    frame5.place(x=150, y=550)
    Button(frame5, text="Hide Data", width=10, height=2, font="arial 14 bold", command=hide, bg="lightblue").place(x=25, y=20)

    # Exit Button
    Button(text="Exit", width=10, height=2, font="arial 14 bold", command=exit_program, bg="lightblue").place(x=180, y=350)






    root.mainloop()


def open_welcome_window():
    global welcome_window
    welcome_window = Tk()
    welcome_window.title("Welcome")
    welcome_window.geometry("800x600")
    welcome_window.resizable(False, False)
    welcome_window.configure(bg="skyblue")
    logo = PhotoImage(file="logo.png")
    Label(welcome_window, image=logo, bg="skyblue").place(x=10, y=5)

    logo1 = PhotoImage(file="logo1.png")
    Label(welcome_window, image=logo1, bg="skyblue").place(x=100, y=5)

    logo2 = PhotoImage(file="logo2.png")
    Label(welcome_window, image=logo2, bg="skyblue").place(x=600, y=5)

    logo3 = PhotoImage(file="logo3.png")
    Label(welcome_window, image=logo3, bg="skyblue").place(x=700, y=5)

    logo4 = PhotoImage(file="logo4.png")
    Label(welcome_window, image=logo4, bg="skyblue").place(x=10, y=500)

    logo5 = PhotoImage(file="logo5.png")
    Label(welcome_window, image=logo5, bg="skyblue").place(x=100, y=500)

    logo6 = PhotoImage(file="logo6.png")
    Label(welcome_window, image=logo6, bg="skyblue").place(x=600, y=500)

    logo7 = PhotoImage(file="logo7.png")
    Label(welcome_window, image=logo7, bg="skyblue").place(x=700, y=500)
 
    logo8 = PhotoImage(file="manishmalla.png")
    Label(welcome_window, image=logo8, bg="skyblue").place(x=300, y=250)

    def exit_program():
        welcome_window.destroy()
   

    Label(welcome_window, text="Welcome to Steganography Tool", bg="skyblue", fg="black", font="arial 20 bold").pack(pady=50)
    Button(welcome_window, text="Open Steganography Tool", width=20, height=2, font="arial 14 bold", command=open_tool_window, bg="lightblue").pack()

    Button(welcome_window, text="Exit", width=10, height=2, font="arial 14 bold", command=exit_program, bg="lightblue").place(x=335, y=200)
    

    
    welcome_window.mainloop()
     

open_welcome_window()

