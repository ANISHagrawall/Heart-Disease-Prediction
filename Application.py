import pandas as pd
import numpy as np
from tkinter import *

from random_forest import RandomForest

def mod():
    def heart_disease(new_input):
        df = pd.read_csv("dataset.csv", delimiter=",")
        data = df.to_numpy()
        n_samples, n_features = data.shape
        n_features -= 1
        X = data[:, 0:n_features]
        y = data[:, n_features]
        clf = RandomForest(n_trees=20, max_depth=10)
        clf.fit(X, y)
        y_pred = clf.predict(new_input)
        return y_pred

    window = Tk()
    window.title("Heart-Disease-Prediction")
    window.geometry('550x400')

    lbl = Label(window, text="Enter the following parameters", font=("Arial Bold", 10))
    lbl.grid(column=2, row=0)

    lbl = Label(window, text="Age")
    lbl.grid(column=1, row=1)
    age = Entry(window,width=20)
    age.grid(column=2, row=1)
    age.focus()

    lbl = Label(window, text="Sex (Male=1,Female=0)")
    lbl.grid(column=1, row=2)
    sex = Entry(window,width=20)
    sex.grid(column=2, row=2)
    sex.focus()

    lbl = Label(window, text="Chest pain level (0-3)")
    lbl.grid(column=1, row=3)
    cp = Entry(window,width=20)
    cp.grid(column=2, row=3)
    cp.focus()

    lbl = Label(window, text="Blood Pressure(mmHg)")
    lbl.grid(column=1, row=4)
    bps = Entry(window,width=20)
    bps.grid(column=2, row=4)
    bps.focus()

    lbl = Label(window, text="Cholesterol(mg/dl) (Normal<200)")
    lbl.grid(column=1, row=5)
    chol = Entry(window,width=20)
    chol.grid(column=2, row=5)
    chol.focus()

    lbl = Label(window, text="Fasting Blood Sugar > 120 mg/dl (1 = true, 0 = false)")
    lbl.grid(column=1, row=6)
    fbs = Entry(window,width=20)
    fbs.grid(column=2, row=6)
    fbs.focus()

    lbl = Label(window, text="ECG > 100 (true=1, false=0)")
    lbl.grid(column=1, row=7)
    ecg = Entry(window,width=20)
    ecg.grid(column=2, row=7)
    ecg.focus()

    lbl = Label(window, text="Maximum Heart Rate Achieved")
    lbl.grid(column=1, row=8)
    mhr = Entry(window,width=20)
    mhr.grid(column=2, row=8)
    mhr.focus()

    lbl = Label(window, text="Exercise induced Angina (1 = yes, 0 = no)")
    lbl.grid(column=1, row=9)
    eia = Entry(window, width=20)
    eia.grid(column=2, row=9)
    eia.focus()

    lbl = Label(window, text="Exercise induced Ischaemia (1 = yes, 0 = no)")
    lbl.grid(column=1, row=11)
    slope = Entry(window, width=20)
    slope.grid(column=2, row=11)
    slope.focus()

    lbl = Label(window, text="Number of major vessels (0-3) colored by flouroscopy")
    lbl.grid(column=1, row=12)
    ca = Entry(window, width=20)
    ca.grid(column=2, row=12)
    ca.focus()

    lbl = Label(window, text="Thalassemia disorder level (1-3)")
    lbl.grid(column=1, row=13)
    thal = Entry(window, width=20)
    thal.grid(column=2, row=13)
    thal.focus()

    def clicked():
        new_input = list(map(int, [age.get(), sex.get(), cp.get(), bps.get(), chol.get(), fbs.get(), ecg.get(), mhr.get(), eia.get(), slope.get(), ca.get(), thal.get()]))
        new_input = np.reshape(new_input, (1, -1))
        output = heart_disease(new_input)

        if (output == 1):
            s = 'You have a Heart Disease'
        else:
            s = "You are in Perfect Health"
        ot.configure(text="Result: " + s)

    btn = Button(window, text="Submit", command=clicked)
    btn.grid(column=2, row=18)

    ot = Label(window, text="", font=("Arial Bold", 10))
    ot.grid(column=1, row=20)

    window.mainloop()


mod()
