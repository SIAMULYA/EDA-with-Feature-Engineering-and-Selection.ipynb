import streamlit as st

st.title("Advanced house price prediction GUI")

st.subheader("Welcome to the sample GUI")
st.sidebar.radio("Select the option",[1,2,3])
st.sidebar.text_input("Enter some value")
st.sidebar.button("Hit me")

st.checkbox("Check this out")
st.time_input("Enter the entry time")
st.file_uploader("Upload the csv file")
st.sidebar.slider("Slide the bar",min_value=0,max_value=10)

st.write("This is a basic GUI for the model")
