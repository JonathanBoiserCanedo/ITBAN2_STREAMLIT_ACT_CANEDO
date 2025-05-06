import streamlit as st

st.title("HELLO, STREAMLIT")
st.header("STREAMLIT APP")
st.write("app demonstration")

# Input fields
email = st.text_input("Enter your email")
pin = st.text_input("Enter your digit PIN")

# Display what the user typed
st.write("📧 Your email is:", email)
st.write("🔢 Your PIN is:", pin)
