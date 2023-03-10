import pandas as pd
import numpy as np
import streamlit as st
import pickle


st.title("Diamonds Dancing- Diamond Price Calculator")
st.write("Enter the characteristics of a diamond to predict its price")

with open("../models/randomforest_bestparams_model.pickle", "rb") as file:
	model = pickle.load(file)

with open("../scalers/standard_scaler.pickle", "rb") as file:
	scaler = pickle.load(file)

carat = None
cut = None
color = None
clarity = None
depth = None
table = None
x = None
y = None
z = None 

try:
    carat = float(st.text_input("Enter carat value of the diamond: "))
    cut = int(st.text_input("Enter the corresponding numerical value for the cut of the diamond ('Ideal': 5, 'Premium': 4, 'Very Good': 3, 'Good': 2, 'Fair': 1): "))
    color = int(st.text_input("Enter the corresponding numerical value for the color of the diamond ('D': 7, 'E': 6, 'F': 5, 'G': 4, 'H': 3, 'I': 2, 'J': 1): "))
    clarity = int(st.text_input("Enter the corresponding numerical value for the clarity of the diamond ('IF': 5, 'VVS1': 4, 'VVS2': 4, 'VS1': 3, 'VS2': 3, 'SI1': 2, 'SI2': 2, 'I1': 1): "))
    depth = float(st.text_input("Enter the total depth percentage of the diamond: "))
    table = float(st.text_input("Enter the table of the diamond: "))
    x = float(st.text_input("Enter the length of the diamond in milimetres: "))
    y = float(st.text_input("Enter the width of the diamond in millimetres: "))
    z = float(st.text_input("Enter the depth of the diamond in millimetres: "))
except ValueError:
    if carat is None or cut is None or color is None or clarity is None or depth is None or table is None or x is None or y is None or z is None:
        st.write("Please enter a valid value")
    else:
        st.write("Invalid input! Check your input and enter a valid value")

if carat is not None and cut is not None and color is not None and clarity is not None and depth is not None and table is not None and x is not None and y is not None and z is not None:
    d = {
        "carat" : [carat],
        "cut" : [cut],
        "color" : [color],
        "clarity" : [clarity],
        "depth" : [depth],
        "table" : [table],
        "x" : [x],
        "y" : [y],
        "z" : [z]
    }

    X = pd.DataFrame(d)

    X_scaled = scaler.transform(X)

    y_pred = model.predict(X_scaled)

    st.write("The predicted price of the diamond is:", round(y_pred[0], 2))







