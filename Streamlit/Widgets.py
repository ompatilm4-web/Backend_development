import streamlit as st
import pandas as pd


st.title("Widgets in Streamlit")
name=st.text_input("Enter Your Name:")

Age = st.slider ("Select Your Age ",0,80,20)


Options  = ['Python','Java','C++','JavaScript']
Choice = st.selectbox("Select your Preffered Language :",Options )


if name :
    st.write(f"Hello {name} !")
    if Age:
        st.write(f"You are {Age} years old.")

st.write(f"You have selected {Choice} as your Preffered Language")

data = pd.DataFrame({
    "Name": ["Om", "Aarav", "Krishna", "Vihaan", "Aditya"],
    "Age": [21, 20, 22, 19, 21],
    "Marks": [85, 90, 78, 88, 95],
    "Study_Hours": [3, 5, 2, 4, 6]
})

st.write("Data Frame:\n",data )

Uploaded=st.file_uploader("Upload a CSV file ",type='csv')
if Uploaded:
    df=pd.read_csv(Uploaded)
    st.write("Uploaded Data Frame:\n",df)
    