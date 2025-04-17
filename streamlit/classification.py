# Example of ML App with streamlit

import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


@st.cache_data

def load_data():
    """Load the iris dataset."""
    iris = load_iris()
    df = pd.DataFrame(iris.data,columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names
    

df,target_names = load_data()

model=RandomForestClassifier()
model.fit(df.iloc[:,:-1],df['species'])
st.title("Iris Species Classification")
st.write("This app classifies iris species using Random Forest Classifier.")


sepal_length = st.slider("Sepal Length", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
sepal_width = st.slider("Sepal Width", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
petal_length = st.slider("Petal Length", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petal_width = st.slider("Petal Width", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

st.write("Input Features:")
st.write(f"Sepal Length: {sepal_length}")
st.write(f"Sepal Width: {sepal_width}")
st.write(f"Petal Length: {petal_length}")
st.write(f"Petal Width: {petal_width}")


input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(input_data)
predicted_species = target_names[prediction][0]


st.write("Prediction")
st.write(f"The predicted species is: {predicted_species}")