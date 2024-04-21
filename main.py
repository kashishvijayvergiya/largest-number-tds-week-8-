import streamlit as st

def large(a,b,c):
  if a>b and a>c:
    return(a)
  elif b>a and b>c:
    return(b)
  else:
    return(c)

st.title("Finding the highest number")
a = st.number_input("Input your first number : ")
b = st.number_input("Input your second number : ")
c = st.number_input("Input your third number : ")

answer = large(a,b,c)
st.write(answer)
