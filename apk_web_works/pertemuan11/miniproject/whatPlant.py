import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image

# Load the trained model
try:
    model = keras.models.load_model('model.h5')
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Load the class mapping
try:
    class_mapping = np.load('class_mapping.npy', allow_pickle=True)
    
    # Memastikan class_mapping memiliki format yang benar
    if isinstance(class_mapping, dict):
        class_labels = class_mapping['class_labels']
    elif isinstance(class_mapping, np.ndarray):
        # Jika class_mapping berbentuk array, kita cek strukturnya
        st.write("class_mapping.npy has been loaded as an array.")
        
        # Jika elemen pertama adalah dictionary, ambil elemen tersebut
        if isinstance(class_mapping[()], dict):
            class_labels = class_mapping[()]['class_labels']
        else:
            st.error("The structure of class_mapping.npy is not as expected.")
            st.stop()

except Exception as e:
    st.error(f"Error loading class mapping: {e}")
    st.stop()

# Descriptions dictionary
descriptions = {
    # (Tambahkan deskripsi seperti kode asli)
}

# Streamlit app title
st.title("🌱 Plant/Fruit Classifier")

# Upload image
uploaded_file = st.file_uploader("Upload an image of a plant/fruit", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Display the uploaded image
    try:
        img = image.load_img(uploaded_file, target_size=(244, 244))
        st.image(img, caption='Uploaded Image', use_column_width=True)

        # Prepare the image for prediction
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0  # Rescale

        # Predict the class
        predictions = model.predict(img_array)
        predicted_class_index = np.argmax(predictions[0])

        # Ensure the predicted class label is valid
        if predicted_class_index < len(class_labels):
            predicted_class_label = class_labels[predicted_class_index]
        else:
            st.error("Predicted class index is out of range for class labels.")
            st.stop()

        # Display the prediction
        st.write(f"Prediction: **{predicted_class_label}**")

        # Display the description
        st.write("Description:")
        st.write(descriptions.get(predicted_class_label, "No description available."))

        # Suggest uses
        if predicted_class_label == "Banana":
            st.write("🍌 You can use bananas in smoothies, desserts, or eat them as a snack!")
        elif predicted_class_label == "Aloevera":
            st.write("🌿 Aloevera can be used in skin care products and is also consumed for health benefits.")
        else:
            st.write("No suggestions available for this plant/fruit.")
    except Exception as e:
        st.error(f"Error processing image or making prediction: {e}")
