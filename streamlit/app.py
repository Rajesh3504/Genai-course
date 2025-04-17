import streamlit as st
import pandas as pd
import numpy as np
import random



## Title of the application
st.title("Hello Streamlit!")
st.subheader("This is a simple Streamlit application.")

## Display a simple text
st.write("this is a simple text")

## Create a simple dataframe

df=pd.DataFrame({

    "Column1": [1, 2, 3],
    "Column2": ["A", "B", "C"]
})

## Display the dataframe
st.write("Here is a simple dataframe")
st.write(df)

#Create a line Chart
chart_data=pd.DataFrame(
    np.random.randn(20, 3),columns=["a","b","c"]
)
st.line_chart(chart_data)