import streamlit as st 
import pandas as pd 
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


# Cache the dataset
@st.cache_data
def Load_Data():
    iris = load_iris()

    Data_Frame = pd.DataFrame(
        iris.data,
        columns=iris.feature_names
    )

    Data_Frame['species'] = iris.target

    return Data_Frame, iris


# Load Data
df, iris = Load_Data()


# Title
st.title("Iris Flower Prediction App")


# Display Dataset
st.subheader("Iris Dataset")
st.write(df)


# Sidebar Inputs
st.sidebar.header("Input Features")

sepal_length = st.sidebar.slider(
    "Sepal Length",
    float(df["sepal length (cm)"].min()),
    float(df["sepal length (cm)"].max()),
    5.4
)

sepal_width = st.sidebar.slider(
    "Sepal Width",
    float(df["sepal width (cm)"].min()),
    float(df["sepal width (cm)"].max()),
    3.4
)

petal_length = st.sidebar.slider(
    "Petal Length",
    float(df["petal length (cm)"].min()),
    float(df["petal length (cm)"].max()),
    1.3
)

petal_width = st.sidebar.slider(
    "Petal Width",
    float(df["petal width (cm)"].min()),
    float(df["petal width (cm)"].max()),
    0.2
)


# User Input Data
user_data = [[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]]


# Train Model
model = RandomForestClassifier()

X = df.iloc[:, :-1]
Y = df.iloc[:, -1]

model.fit(X, Y)


# Prediction
prediction = model.predict(user_data)
prediction_name = iris.target_names[prediction][0]


# Output
st.subheader("Prediction")
st.write(f"The predicted flower species is: **{prediction_name}**")


# Probability
st.subheader("Prediction Probability")

probability = model.predict_proba(user_data)

prob_df = pd.DataFrame(
    probability,
    columns=iris.target_names
)

st.write(prob_df)