import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




# title of the Webpage
st.title("My First Streamlit App")



# Data Frame
Data=pd.DataFrame({
    "First" :[1,2,3,4],
    "Second":[10,20,30,40]
    
})


# Displaying the Data Frame 
st.write("Displaying the Data Frame using st.write()")
st.write(Data)



# Line graph of the Data Frame 
DATA=pd.DataFrame(
    np.random.randn(20,3), columns=["a","b","c"]
)

st.write("Relationship Between First and Second ") 
st.line_chart(DATA)

        # st.write(graph)



