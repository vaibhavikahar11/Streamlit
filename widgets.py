import streamlit as st
import pandas as pd

st.title("Streamlit Text input")
name=st.text_input("Enter the name:")


age=st.slider("Select your age:",1,100,25)
st.write(f"Your age is {age}.")

options=['Python','Java','C++','Javascript']
choice=st.selectbox("choose your avourite language:",options)
st.write(f"you selcted {choice}")
if name:
    st.write(f"HELLO ,{name}")
    

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice Johnson", "Bob Smith", "Charlie Lee", "Diana Prince", "Ethan Wright"],
    "Age": [20, 21, 19, 22, 20],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Grade": ["A", "B", "A", "C", "B"],
    "Major": ["Computer Science", "Mechanical Eng.", "Physics", "History", "Economics"]
}    
    
df=pd.DataFrame(data)  
df.to_csv("sampledata.csv")  
st.write(df)

uploaded_files=st.file_uploader("choose  a csv file",type="csv")
if uploaded_files is not None:
    df=pd.read_csv(uploaded_files)
    st.write(df)
    
    