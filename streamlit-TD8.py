import streamlit as st
st.write("""
# Largest Number
""")


def user_input_features():
  Number1=st.number_input("Enter the first Number")
  Number2=st.number_input("Enter the second Number")
  Number3=st.number_input("Enter the third Number")
  return (max(Number1,Number2,Number3))

a=user_input_features()

st.subheader("The largest number of the above is")
st.write(a)
