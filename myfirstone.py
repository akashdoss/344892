import streamlit as st

# Title of the app
st.title("My First Streamlit App")

# Add a text input
name = st.text_input("Enter your name:")

# Add a button
if st.button("Greet"):
    st.write(f"Hello, {name}!")
