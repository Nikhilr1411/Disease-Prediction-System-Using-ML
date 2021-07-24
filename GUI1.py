from heart import *
from glucose import *
from remaining_disease import *
from tkinter import *
from tkinter import messagebox
from csv import writer

root1 = Tk()


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

    b = Button(root1, text="Back", font=('Helvetica', 14), command=lambda: GUI(root1)).place(x=280, y=320)
    b1 = Button(root1, text="Submit", font=('Helvetica', 14), command=click).place(x=370, y=320)
    root1.mainloop()


def GUI(root1):
    root1.destroy()
    root = Tk()
    root.title("DISEASE PREDICTION SYSTEM")
    root.geometry("400x300")
    root.maxsize(400, 300)
    root.minsize(400, 300)

    email = StringVar()
    password = StringVar()

    email_label = Label(root, text="EMAIL ID", font=('Helvetica', 12)).place(x=60, y=70)

    entry_email = Entry(root, width=30, textvar=email)
    entry_email.place(x=160, y=70)

    password_label = Label(root, text="PASSWORD", font=('Helvetica', 12)).place(x=60, y=120)

    entry_password = Entry(root, show="*", width=30, textvar=password)
    entry_password.place(x=160, y=120)

    def login(root, email1, password1):
        root.destroy()
        flag = 0

        details = pd.read_csv("details.csv")
        em = details['email'].tolist()
        pa = details['password'].tolist()
        password.set("")
        email.set("")
        for i in range(0, len(em)):
            if em[i] == email1 and str(pa[i]) == password1:
                flag = 1
                break

        if flag == 1:

            root2 = Tk()
            root2.title("Disease Prediction System")
            root2.geometry('400x300')
            root2.maxsize(400, 300)
            root2.minsize(400, 300)
            label = Label(root2, text="Select the disease", fg='blue', font=('Helvetica', 20)).place(x=90, y=40)
            var1 = IntVar()
            c1 = Radiobutton(root2, text="Heart", font=('Helvetica', 14), variable=var1, value=1).place(x=130, y=90)
            c2 = Radiobutton(root2, text="Diabetes", font=('Helvetica', 14), variable=var1, value=2).place(x=130, y=130)
            c3 = Radiobutton(root2, text="Other disease", font=('Helvetica', 14), variable=var1, value=3).place(x=130,
                                                                                                                y=170)

            def click1():
                dis = var1.get()
                if dis == 1:
                    heart(root2, email1, password1)
                elif dis == 2:
                    glucose(root2, email1, password1)
                elif dis == 3:
                    otherdisease(root2, email1, password1)
                else:
                    messagebox.showerror("ERROR", "Choose a valid option")

            b = Button(root2, text="Back", font=('Helvetica', 14), command=lambda: GUI(root2)).place(x=100, y=240)
            b2 = Button(root2, text="Submit", command=click1, font=('Helvetica', 14)).place(x=200, y=240)

        else:
            messagebox.showerror("INVALID ENTRY", "Enter a valid email or password")
            email.set("")
            password.set("")
        root2.mainloop()

    def heart(root, email1, password1):
        root.destroy()
        root3 = Tk()
        root3.title('Heart')
        root3.geometry('1000x600')
        root3.maxsize(1000, 600)
        root3.minsize(1000, 600)

        c = IntVar()

        r1 = Radiobutton(root3, text="0", variable=c, value=0).place(x=540, y=100)
        r2 = Radiobutton(root3, text="1", variable=c, value=1).place(x=580, y=100)
        r3 = Radiobutton(root3, text="2", variable=c, value=2).place(x=620, y=100)
        r4 = Radiobutton(root3, text="3", variable=c, value=3).place(x=660, y=100)
        fbs = IntVar()
        r1 = Radiobutton(root3, text="0", variable=fbs, value=0).place(x=540, y=220)
        r2 = Radiobutton(root3, text="1", variable=fbs, value=1).place(x=580, y=220)
        ec = IntVar()
        r1 = Radiobutton(root3, text="0", variable=ec, value=0).place(x=540, y=260)
        r2 = Radiobutton(root3, text="1", variable=ec, value=1).place(x=580, y=260)
        r3 = Radiobutton(root3, text="2", variable=ec, value=2).place(x=620, y=260)
        ea = IntVar()
        r1 = Radiobutton(root3, text="0", variable=ea, value=0).place(x=540, y=340)
        r3 = Radiobutton(root3, text="1", variable=ea, value=1).place(x=580, y=340)
        s = IntVar()
        r3 = Radiobutton(root3, text="0", variable=s, value=0).place(x=540, y=420)
        r3 = Radiobutton(root3, text="1", variable=s, value=1).place(x=580, y=420)
        r3 = Radiobutton(root3, text="2", variable=s, value=2).place(x=620, y=420)

        m = IntVar()
        r1 = Radiobutton(root3, text="Male", variable=m, value=1).place(x=540, y=60)
        r2 = Radiobutton(root3, text="Female", variable=m, value=0).place(x=600, y=60)
        mv = IntVar()
        r1 = Radiobutton(root3, text="0", variable=mv, value=0).place(x=540, y=460)
        r2 = Radiobutton(root3, text="1", variable=mv, value=1).place(x=580, y=460)
        r3 = Radiobutton(root3, text="2", variable=mv, value=2).place(x=620, y=460)
        r4 = Radiobutton(root3, text="3", variable=mv, value=3).place(x=660, y=460)
        r5 = Radiobutton(root3, text="4", variable=mv, value=4).place(x=700, y=460)

        t = IntVar()
        r1 = Radiobutton(root3, text="1", variable=t, value=1).place(x=540, y=500)
        r2 = Radiobutton(root3, text="2", variable=t, value=2).place(x=580, y=500)
        r3 = Radiobutton(root3, text="3", variable=t, value=3).place(x=620, y=500)
        label = Label(root3, text="Age", font=('Helvetica', 14)).place(x=10, y=20)
        label1 = Label(root3, text="Sex", font=('Helvetica', 14)).place(x=10, y=60)
        label2 = Label(root3, text="Chest pain type", font=('Helvetica', 14)).place(x=10, y=100)
        label3 = Label(root3, text="Resting blood pressure", font=('Helvetica', 14)).place(x=10, y=140)
        label4 = Label(root3, text="Serum cholesterol in mg/dl", font=("Helvetica", 14)).place(x=10, y=180)
        label5 = Label(root3, text="Fasting blood sugar > mg//dl", font=('Helvetica', 14)).place(x=10, y=220)
        Label6 = Label(root3, text="Resting electrocardiograph results", font=('Helvetica', 14)).place(x=10, y=260)
        label7 = Label(root3, text="Maximum heart rate achieved", font=('Helvetica', 14)).place(x=10, y=300)
        label8 = Label(root3, text="Exercise induced angina", font=("Helvetica", 14)).place(x=10, y=340)
        label9 = Label(root3, text="Old peak = ST depression induced by exercise relative to rest",
                       font=('Helvetica', 14)).place(x=10, y=380)
        label10 = Label(root3, text="The slope of the peak exercise ST segment", font=('Helvetica', 14)).place(x=10,
                                                                                                               y=420)
        Label11 = Label(root3, text="Number of major vessels colored by fluoroscopy", font=('Helvetica', 14)).place(
            x=10,
            y=460)
        label12 = Label(root3, text="Thal", font=('Helvetica', 14)).place(x=10, y=500)
        hage = IntVar()
        e = Entry(root3, font=('Helvetica', 14), textvar=hage).place(x=540, y=20)
        rbp = IntVar()
        e1 = Entry(root3, font=('Helvetica', 14), textvar=rbp).place(x=540, y=140)
        sc = IntVar()
        e2 = Entry(root3, font=('Helvetica', 14), textvar=sc).place(x=540, y=180)

        mha = IntVar()
        e4 = Entry(root3, font=('Helvetica', 14), textvar=mha).place(x=540, y=300)
        op = DoubleVar()
        e5 = Entry(root3, font=('Helvetica', 14), textvar=op).place(x=540, y=380)

        def heartml():
            iage = 0
            if hage.get() <= 30:
                iage = 0
            elif (hage.get() > 30 and hage.get() <= 50):
                iage = 1
            else:
                iage = 2

            ichol = 0
            if sc.get() <= 180:
                ichol = 0
            elif sc.get() > 180 and sc.get() <= 220:
                ichol = 1
            else:
                ichol = 2
            output = heartop(m.get(), c.get(), rbp.get(), fbs.get(), ec.get(), mha.get(), ea.get(), op.get(), s.get(),
                             mv.get(), t.get(), ichol, iage)
            root6 = Tk()
            root6.geometry("700x400")
            root6.maxsize(700, 400)
            root6.minsize(700, 400)
            root6.title("RESULT")
            root3.destroy()
            if output == 1:
                l = Label(root6, font=('Helvetica', 12), text="YOU HAVE HIGHER PROBABILITY OF HAVING DISEASE RELATED "
                                                              "TO HEART").place(x=100, y=100)
                l2 = Label(root6, font=('Helvetica', 12), text="NOTHING TO WORRY, VISIT THE NEARBY HOSPITAL AT THE "
                                                               "EARLIEST").place(x=100, y=200)
                b1 = Button(root6, text='OK', font=('Helvetica', 14), command=lambda: login(root6,email1,password1)).place(x=300, y=240)

            else:
                l = Label(root6, font=('Helvetica', 12), text="YOU HAVE NO PROBLEMS IN HEART").place(x=200, y=150)
                b1 = Button(root6, text='OK', font=('Helvetica', 14), command=lambda: login(root6,email1,password1)).place(x=340, y=240)

            root6.mainloop()

        b = Button(root3, text='Back', font='Helvetica, 14', command=lambda: login(root3, email1, password1)).place(
            x=700, y=550)
        b1 = Button(root3, text='Submit', font='Helvetica, 14', command=heartml).place(x=800, y=550)

    def glucose(root, email1, password1):
        root.destroy()
        root4 = Tk()
        root4.title('Diabetes')
        root4.geometry('500x400')
        root4.maxsize(500, 400)
        root4.minsize(500, 400)
        l = Label(root4, text='Pregnancies', font=('Helvetica', 14)).place(x=10, y=20)
        p = IntVar()
        e1 = Entry(root4, font=('Helvetica', 14), textvar=p).place(x=250, y=20)
        l1 = Label(root4, text='Glucose', font=('Helvetica', 14)).place(x=10, y=60)
        g = IntVar()
        e3 = Entry(root4, font=('Helvetica', 14), textvar=g).place(x=250, y=60)
        l7 = Label(root4, text='Blood Pressure', font=('Helvetica', 14)).place(x=10, y=100)
        bp = IntVar()
        e7 = Entry(root4, font=('Helvetica', 14), textvar=bp).place(x=250, y=100)
        l8 = Label(root4, text='Skin Thickness', font=('Helvetica', 14)).place(x=10, y=140)
        s = IntVar()
        e8 = Entry(root4, font=('Helvetica', 14), textvar=s).place(x=250, y=140)
        l3 = Label(root4, text='Insulin', font=('Helvetica', 14)).place(x=10, y=180)
        i = IntVar()
        e4 = Entry(root4, font=('Helvetica', 14), textvar=i).place(x=250, y=180)

        l4 = Label(root4, text='BMI', font=('Helvetica', 14)).place(x=10, y=220)
        bmi = DoubleVar()
        e5 = Entry(root4, font=('Helvetica', 14), textvar=bmi).place(x=250, y=220)
        l5 = Label(root4, text='Diabetes Pedigree Function', font=('Helvetica', 14)).place(x=10, y=260)
        dpf = DoubleVar()
        e6 = Entry(root4, font=('Helvetica', 14), textvar=dpf).place(x=250, y=260)

        l6 = Label(root4, text='Age', font=('Helvetica', 14)).place(x=10, y=300)
        a1 = IntVar()
        e7 = Entry(root4, font=('Helvetica', 14), textvar=a1).place(x=250, y=300)

        def diabetes():
            output = glucoseop(p.get(), g.get(), bp.get(), s.get(), i.get(), bmi.get(), dpf.get(), a1.get())
            root4.destroy()
            root6 = Tk()
            root6.geometry("700x400")
            root6.title("RESULT")
            root6.maxsize(700, 400)
            root6.minsize(700, 400)

            if output == 1:
                l = Label(root6, font=('Helvetica', 12), text="YOU HAVE HIGHER PROBABILITY OF HAVING DIABETES").place(x=100, y=100)
                l2 = Label(root6, font=('Helvetica', 12), text="NOTHING TO WORRY, VISIT THE NEARBY HOSPITAL AT THE "
                                                               "EARLIEST").place(x=100, y=200)
                b1 = Button(root6, text='OK', font=('Helvetica', 14), command=lambda: login(root6,email1,password1)).place(x=340, y=240)

            else:
                l = Label(root6, font=('Helvetica', 14), text="YOU HAVE NO DIABETES").place(x=200, y=150)
                b1 = Button(root6, text='OK', font=('Helvetica', 14), command=lambda: login(root6,email1,password1)).place(x=300, y=240)

            root6.mainloop()

        b = Button(root4, text='Back', font=('Helvetica', 14), command=lambda: login(root4, email1, password1)).place(
            x=260, y=340)
        b1 = Button(root4, text='Submit', font=('Helvetica', 14), command=diabetes).place(x=350, y=340)

    def otherdisease(root, email1, password1):
        root.destroy()
        root5 = Tk()
        root5.title('Other Disease')
        root5.geometry('450x400')
        root5.maxsize(450, 400)
        root5.minsize(450, 400)
        options = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills',
                   'joint_pain',
                   'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition',
                   'spotting_ urination', 'fatigue',
                   'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness',
                   'lethargy', 'patches_in_throat',
                   'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
                   'dehydration', 'indigestion',
                   'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
                   'back_pain', 'constipation',
                   'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
                   'acute_liver_failure',
                   'fluid_overload',
                   'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm',
                   'throat_irritation',
                   'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
                   'fast_heart_rate',
                   'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus',
                   'neck_pain',
                   'dizziness', 'cramps',
                   'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes',
                   'enlarged_thyroid', 'brittle_nails',
                   'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
                   'slurred_speech', 'knee_pain', 'hip_joint_pain',
                   'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements',
                   'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
                   'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine',
                   'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
                   'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body',
                   'belly_pain',
                   'abnormal_menstruation', 'dischromic _patches',
                   'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum',
                   'rusty_sputum', 'lack_of_concentration', 'visual_disturbances',
                   'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding',
                   'distention_of_abdomen', 'history_of_alcohol_consumption',
                   'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking',
                   'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
                   'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister',
                   'red_sore_around_nose',
                   'yellow_crust_ooze']
        options = sorted(options)

        clicked1 = StringVar()
        clicked1.set('Choose')
        clicked2 = StringVar()
        clicked2.set('Choose')
        clicked3 = StringVar()
        clicked3.set('Choose')
        clicked4 = StringVar()
        clicked4.set('Choose')
        clicked5 = StringVar()
        clicked5.set('Choose')
        d1 = OptionMenu(root5, clicked1, *options).place(x=280, y=20)
        l11 = Label(root5, text='Enter the Symptoms 1', font=('Helvetica', 14)).place(x=10, y=20)
        d2 = OptionMenu(root5, clicked2, *options).place(x=280, y=60)
        l2 = Label(root5, text='Enter the Symptoms 2', font=('Helvetica', 14)).place(x=10, y=60)
        d3 = OptionMenu(root5, clicked3, *options).place(x=280, y=100)
        l3 = Label(root5, text='Enter the Symptoms 3', font=('Helvetica', 14)).place(x=10, y=100)
        d4 = OptionMenu(root5, clicked4, *options).place(x=280, y=140)
        l4 = Label(root5, text='Enter the Symptoms 4', font=('Helvetica', 14)).place(x=10, y=140)
        d5 = OptionMenu(root5, clicked5, *options).place(x=280, y=180)
        l5 = Label(root5, text='Enter the Symptoms 5', font=('Helvetica', 14)).place(x=10, y=180)

        def otherdis():

            if clicked1.get() == "Choose" or clicked2.get() == "Choose" or clicked3.get() == "Choose" or clicked4.get() == "Choose" or clicked5.get() == "Choose":
                messagebox.showerror("ERROR", "Select all the options")
            else:
                output = remdis(clicked1.get(), clicked2.get(), clicked3.get(), clicked4.get(), clicked5.get())
                root5.destroy()
                root6 = Tk()
                root6.geometry("800x400")
                root6.maxsize(800, 400)
                root6.minsize(800, 400)
                root6.title("RESULT")
                l = Label(root6, font=('Helvetica', 12), text="YOU HAVE HIGHER PROBABILITY OF HAVING " + output.upper()).place(x=100, y=100)
                l2 = Label(root6, font=('Helvetica', 12), text="NOTHING TO WORRY, VISIT THE NEARBY HOSPITAL AT THE "
                                                               "EARLIEST").place(x=100, y=200)
                b1 = Button(root6, text='OK', font=('Helvetica', 14), command=lambda: login(root6,email1,password1)).place(x=340, y=240)
                root6.mainloop()

        b = Button(root5, text='Back', font=('Helvetica', 14), command=lambda: login(root5, email1, password1)).place(x=200, y=240)
        b1 = Button(root5, text='Submit', font=('Helvetica', 14), command=otherdis).place(x=290, y=240)

    login_button = Button(root, text="Login", command=lambda: login(root, email.get(), password.get()),
                          font=('Helvetica', 14)).place(x=100, y=200)
    signup_button = Button(root, text="Sign Up", command=lambda: signUp(root), font=('Helvetica', 14)).place(x=200,
                                                                                                             y=200)

    root.mainloop()


GUI(root1)
