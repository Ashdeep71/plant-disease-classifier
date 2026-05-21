import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image


model= tf.keras.models.load_model("model/plant_disease_mobilenet_model.keras")

class_names= ["Potato Early Blight", "Potato Late Blight", "Potato Healthy"]


st.title("Plant Disease Classifier")

st.write("Upload an image of a plant leaf to classify its disease.")

uploaded_file= st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])


if uploaded_file is not None:
    img= Image.open(uploaded_file)
    st.image(img, caption= "Uploaded Image", use_container_width=True)
    img= img.resize((224, 224))
    img_array= np.array(img)
    img_array= np.expand_dims(img_array, axis=0)
    predictions= model.predict(img_array)
    confidence= np.max(predictions)*100
    predicted_class= class_names[np.argmax(predictions)]
    
    for i in range(len(class_names)):
        st.write(f"{class_names[i]} confidence: {predictions[0][i]*100:.2f}")
    
    # st.subheader("Prediction Results")
    # st.write(f"Predicted Class: {predicted_class}")
    # st.write(f"Confidence: {confidence:.2f}%")

