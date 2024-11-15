import streamlit as st
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

st.title("About Me")
st.image("./.static/me.jpg")
st.write(f"Hi there, my name is Bryce Rodgers and I've been a software developer for over 15 years.\nIn that time I've been a system architect, data scientist, and full-stack developer.")
# st.write(f"In that time I've been a system architect, data scientist, and full-stack developer.")
st.write(f"I have a Patent for my work creating the Support Vector Machine for a novel Android app back in 2013. (US9299264B2) ")
st.write(f"The following year, I built a standardized test score-predictor which used a KNN model at its core.")
st.write(f"In college I took every grad-level Machine Learning course offered. Since then I've continued my AI-education, completing Andrej Karpathy's lectures and Jeremy Howard's course 'Practical Deep Learning for Coders 2022'.")

# st.write(f"Since then I have continued my AI-education, completing Andrej Karpathy's lectures, and Jeremy Howard's course 'Practical Deep Learning for Coders 2022'!")
st.write(f"Please browse around my website and explore the various functionalities I've made through Machine Learning & Data Science!")
