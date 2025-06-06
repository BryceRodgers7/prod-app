import streamlit as st
from menu import menu_with_redirect
import torch
from torch.hub import load_state_dict_from_url
from fastai.learner import load_learner
from fastai.vision.all import *
from PIL import Image
import sys
from pathlib import Path

menu_with_redirect()

PATH = './.static/models/allfourfinetuned.pkl'
categories = ('Grunt', 'Footman', 'Ghoul', 'Night Elf Archer')

@st.cache_resource
def load_model():
    try:
        # Use fastai's load_learner which handles the custom serialization
        learner = load_learner(PATH, cpu=True)
        return learner
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        st.error("Please ensure the model file exists at the specified path and is a valid fastai model.")
        return None

model = load_model()

if model is None:
    st.error("Failed to load the model. The application cannot continue.")
    st.stop()

st.title('Warcraft Factions')
st.write('This page allows you to upload an image and check which faction it belong to')
st.write('In warcraft, each faction has a basic type of soldier that makes up the bulk of their numbers')
st.subheader('The Roster')


def display_images_side_by_side(image_paths, captions, width=150):  
    # Create columns based on the number of images
    columns = st.columns(len(image_paths))
    
    # Display each image in its respective column, along with caption
    for col, img, caption in zip(columns, image_paths, captions):
        with col:
            st.image(img, caption=caption, use_container_width=False, width=width)

# st.write("The Roster of Warcraft World")
image_paths = ["./.static/footman.jpg", "./.static/grunt.jpg", "./.static/ghoul.jpg", "./.static/nearcher.jpg"]
captions = ["Human Footman", "Orc Grunt", "Undead Ghoul", "Night Elf Archer"]
# Call the function with the images you want to display side-by-side
display_images_side_by_side(image_paths, captions)

uploaded_file = st.file_uploader("Upload an image to determine which warcraft roster it most resembles", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)
    
    # Predict the class of the image
    st.write("Classifying...")
    try:
        pred, pred_idx, probs = model.predict(image)
        # Display the result
        st.write(f"Prediction: {pred}")
        st.write(f"Confidence: {probs[pred_idx]:.4f}")
    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")
else:
    st.write("awaiting uploaded image")