import streamlit as st
import pandas as pd

st.title("Streamlit text input example")    

name=st.text_input("Enter your name:")

age=st.slider("Select your age:", 0, 100, 25)

options=["Python", "Java", "C++"]
choice=st.selectbox("Select your favorite programming language:", options)



if name:
    st.write(f"Hello {name}! You are {age} years old. Your favorite programming language is {choice}.")

data={
    "Name": ["John","Doe"],
    "Age": [25, 30],
    "Language": ["Python", "Java"]

}

df=pd.DataFrame(data)
df.to_csv("data.csv")
st.write(df)

uploaded_file=st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)