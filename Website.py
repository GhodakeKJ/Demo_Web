import streamlit as st
import pandas as pd
st.title("Welcome To GFCCT ")
fname=st.text_input("Enter Your First Name :")
lname=st.text_input("Enter Your Last Name :")
adr=st.text_area("Enter Your Address :")
course=st.selectbox("Choose Your Course :",("C Language","HTML CSS","Javascript","PHP","Python","Java","Oracle"))

button=st.button("Done")
if button:
    st.markdown(f"""
    fname:{fname}
    lname:{lname}
    address:{adr}
    crs:{course}""")
