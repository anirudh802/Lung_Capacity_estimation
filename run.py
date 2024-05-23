import numpy as np
import pandas as pd
import tensorflow as tf
import seaborn as sns
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Dense

model=tf.keras.models.load_model('ltm2.keras')
# df=pd.read_csv(r"lung capacity dataset.csv")

while True:
    age=float(input("enter age in years: "))
    sex=input('enter gender(m/f)').lower()
    if sex=='m':
        sex=1
    else :
        sex=0
    race=input('enter race;(w:white, b:black, h:hispanic, a:asian, o:other)').lower()
    r1,r2,r3,r4,r5=False,False,False,False,False
    if race=='w':
        r1=True
    elif race=='b':
        r2=True
    elif race=='h':
        r3=True
    elif race=='a':
        r4=True
    else :
        r5=True
    height=float(input("enter height in cms: "))
    weight=float(input("enter weight in kgs: "))
    dis=input('enter disease(a:ashtma, f:CF, c:COPD, n:Normal, o:other)').lower()
    d1,d2,d3,d4,d5=False,False,False,False,False
    if dis=='a':
        d1=True
    elif dis=='f':
        d2=True
    elif dis=='c':
        d3=True
    elif dis=='n':
        d4=True
    else :
        d5=True
    nr={'Calculated age (years):': [age], 'Sex:': [sex], 'Race/ethnicity: (choice=White)': [r1], 'Race/ethnicity: (choice=Black / African American)': [r2], 'Race/ethnicity: (choice=Hispanic / Latino)': [r3], 'Race/ethnicity: (choice=Asian)': [r4], 'Race/ethnicity: (choice=Other)': [r5], 'Height (cm):': [height], 'Weight (kg):': [weight], 'Asthma': [d1], 'CF': [d2], 'COPD': [d3], 'Control / healthy / no pulmonary disease': [d4], 'Other': [d5]}
    df=pd.DataFrame(nr)
    print('Your estimated lung tidal volume is ',model.predict(df))
