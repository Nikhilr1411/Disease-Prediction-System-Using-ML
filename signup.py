from tkinter import *
from tkinter import messagebox
from csv import writer
from GUI1 import GUI

def signUp(root):
    root.destroy()
    root1 = Tk()
    root1.title('Signup')
    root1.geometry('500x400')
    fn = StringVar()
    ln = StringVar()
    em = StringVar()
    np = StringVar()
    rp = StringVar()

    label = Label(root1, text="First-name", font=('Helvetica', 14)).place(x=10, y=40)
    label1 = Label(root1, text="Last-name", font=('Helvetica', 14)).place(x=10, y=80)
    label2 = Label(root1, text="Email-id", font=('Helvetica', 14)).place(x=10, y=120)
    label3 = Label(root1, text="Password", font=('Helvetica', 14)).place(x=10, y=160)
    label4 = Label(root1, text="Re-enter Password", font=('Helvetica', 14)).place(x=10, y=200)
    e = Entry(root1, font=('Helvetica', 14), textvar=fn).place(x=210, y=40)
    e1 = Entry(root1, font=('Helvetica', 14), textvar=ln).place(x=210, y=80)
    e2 = Entry(root1, font=('Helvetica', 14), textvar=em).place(x=210, y=120)
    e3 = Entry(root1, font=('Helvetica', 14), textvar=np).place(x=210, y=160)
    e4 = Entry(root1, font=('Helvetica', 14), textvar=rp).place(x=210, y=200)

    def click():
        fna = fn.get()
        lna = ln.get()
        ema = em.get()
        npa = np.get()
        rpa = rp.get()
        if npa != rpa:
            messagebox.showerror("ERROR", "Password Mismatch")
        elif fna == "" or lna == "" or ema == "" or npa == "" or rpa == "":
            messagebox.showerror("ERROR", "Enter all the values")
        elif npa == rpa:

            dt = [fna, lna, ema, npa]
            with open('details.csv', 'a')as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(dt)
                f_object.close()
            messagebox.showinfo("SUCCESS", "Successfully registered")

    b = Button(root1, text="Back", font=('Helvetica', 14), command=GUI).place(x=280, y=320)
    b1 = Button(root1, text="Submit", font=('Helvetica', 14), command=click).place(x=370, y=320)
    root1.mainloop()
