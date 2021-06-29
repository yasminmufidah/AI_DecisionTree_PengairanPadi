from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import numpy as np
from numpy import integer, right_shift, rint
from numpy.lib.arraypad import pad
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

class RefiEval:
    def __init__(self):
        master = Tk()
        master.title("Watering Predict")
        master.configure(background='antiquewhite1')
        master.geometry("550x350")
 
       
        heading = Label(master, text='Prediksi Pengairan', font = ('Helvetica', 15, 'bold'), background="antiquewhite1").grid(row=0, column=1, ipady=8, pady=10)
        
         # input
        Label(master, text='Soil Moisture', font = ('Helvetica', 10), background="antiquewhite1").grid(row=3)
        Label(master, text='Temperature', font = ('Helvetica', 10),background="antiquewhite1").grid(row=4)
        Label(master, text='Humidity', font = ('Helvetica', 10),background="antiquewhite1").grid(row=5)
        Label(master, text='Time', font = ('Helvetica', 10),background="antiquewhite1").grid(row=6)
        Label(master, text='Pengairan ?', font = ('Helvetica', 10, 'bold'),background="antiquewhite1").grid(row=10, padx=20, pady=50)

        
        self.d1 = StringVar()
        self.d2 = StringVar()
        self.d3 = StringVar()
        self.d4 = StringVar()
        self.out = StringVar()

        # variable to store input
        e1 = Entry(master, textvariable=self.d1, font=('Helvetica', 10))
        e2 = Entry(master,  textvariable=self.d2, font = ('Helvetica', 10))
        e3 = Entry(master,  textvariable=self.d3, font = ('Helvetica', 10))
        e4 = Entry(master,  textvariable=self.d4, font = ('Helvetica', 10))

        # grid input
        e1.grid(row=3, column=1, sticky=W, ipadx=100, ipady=6)
        e2.grid(row=4, column=1, sticky=W, ipadx=100, ipady=6)
        e3.grid(row=5, column=1, sticky=W, ipadx=100, ipady=6)
        e4.grid(row=6, column=1, sticky=W, ipadx=100, ipady=6)

        # Button
        btn = tk.Button(master, text="Submit",font = ('Helvetica', 10), background="coral1",command=self.submit, justify="left")
        btn.place(x=220, y=220) 
        # btn.grid(ipadx=8, ipady=6, pady=10)
        btn2 = tk.Button(master, text="Reset",font = ('Helvetica', 10), background="coral1",command=self.reset, justify="right") 
        btn2.place(x=275, y=220)
        # btn2.grid(row=9, column=3, ipadx=8, ipady=6, pady=10)
        
        # Output
        output = tk.Label(master, text="Siram ", font = ('Helvetica', 13, 'bold'),background="antiquewhite1", textvariable=self.out).place(x=50, y=280)

        master.mainloop()

    def submit(self):
            data = pd.read_csv('RICE-DATASET.csv')
            data.head(10)

            enc = LabelEncoder()
            data['Status'] = enc.fit_transform(data['Status'].values)
            atr_data = data.drop(columns='Status')
            cls_data = data['Status']

            xtrain, xtest, ytrain, ytest = train_test_split(atr_data, cls_data, test_size=0.2, random_state=50)
            tree_data = DecisionTreeClassifier(random_state=50)
            tree_data.fit(xtrain, ytrain)

            d1 = self.d1.get()
            d2 = self.d2.get()
            d3 = self.d3.get()
            d4 = self.d4.get()
            prediksi = tree_data.predict([[d1, d2, d3, d4]])

            if prediksi == 1:
                self.out.set("Ya")
            else: 
                self.out.set("Tidak")

    def reset(self):
        self.d1.set('')
        self.d2.set('')
        self.d3.set('')
        self.d4.set('')
        self.out.set('')


RefiEval()