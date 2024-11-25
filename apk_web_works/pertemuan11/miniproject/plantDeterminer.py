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

# Define class labels directly
class_labels = [
    "Aloevera", "Banana", "Bilimbi", "Cantaloupe", "Cassava",
    "Coconut", "Corn", "Cucumber", "Curcuma", "Eggplant",
    "Galangal", "Ginger", "Guava", "Kale", "Longbeans",
    "Mango", "Melon", "Orange", "Paddy", "Papaya",
    "Peperchili", "Pineapple", "Pomelo", "Shallot", "Soybeans",
    "Spinach", "Sweetpotatoes", "Tobacco", "Waterapple", "Watermelon"
]

# Descriptions dictionary
descriptions = {
    "Aloevera": "Aloe vera is widely used in skincare products due to its soothing and healing properties.",
    "Banana": "Bananas are a popular fruit known for their sweet taste and high potassium content.",
    "Bilimbi": "Bilimbi is often used to add sourness to dishes and is rich in vitamin C.",
    "Cantaloupe": "Cantaloupe is a sweet, orange-fleshed melon that is high in vitamins A and C.",
    "Cassava": "Cassava is a starchy root vegetable that is a staple food in many tropical regions.",
    "Coconut": "Coconuts provide refreshing water and nutritious meat, used in various culinary dishes.",
    "Corn": "Corn is a versatile grain that can be eaten fresh, popped, or ground into flour.",
    "Cucumber": "Cucumbers are hydrating vegetables often used in salads and sandwiches.",
    "Curcuma": "Curcuma, or turmeric, is known for its anti-inflammatory properties and is used as a spice.",
    "Eggplant": "Eggplants are commonly used in Mediterranean and Asian dishes and are rich in fiber.",
    "Galangal": "Galangal is a root used in Thai cooking, known for its distinct flavor.",
    "Ginger": "Ginger is a popular spice with a spicy flavor and is often used in cooking and teas.",
    "Guava": "Guava is a tropical fruit high in vitamin C and can be eaten raw or in juices.",
    "Kale": "Kale is a nutrient-rich leafy green, often used in salads and smoothies.",
    "Longbeans": "Longbeans are used in stir-fries and are a good source of protein.",
    "Mango": "Mangoes are sweet tropical fruits known for their juicy flesh.",
    "Melon": "Melons are sweet fruits with high water content, perfect for refreshing snacks.",
    "Orange": "Oranges are citrus fruits rich in vitamin C and are often eaten fresh or juiced.",
    "Paddy": "Paddy refers to rice in its growing state and is a staple food for many cultures.",
    "Papaya": "Papayas are tropical fruits high in vitamins A and C, often used in smoothies.",
    "Peperchili": "Peperchili adds heat and flavor to dishes and is rich in vitamins.",
    "Pineapple": "Pineapples are sweet tropical fruits that can be eaten fresh or juiced.",
    "Pomelo": "Pomelo is a large citrus fruit with a sweet and tangy flavor.",
    "Shallot": "Shallots are a type of onion known for their sweet flavor, used in many dishes.",
    "Soybeans": "Soybeans are high in protein and used to make various products like tofu and soy milk.",
    "Spinach": "Spinach is a nutrient-dense leafy green often used in salads and cooking.",
    "Sweetpotatoes": "Sweet potatoes are starchy root vegetables rich in vitamins and fiber.",
    "Tobacco": "Tobacco is a plant whose leaves are processed for smoking and other uses.",
    "Waterapple": "Waterapples are tropical fruits that are crunchy and juicy, often eaten fresh.",
    "Watermelon": "Watermelons are refreshing fruits with high water content, perfect for hot days."
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
            st.write("🌿 Aloevera can be used in skincare products and is also consumed for health benefits.")
        # Add more suggestions as needed for other plants
        else:
            st.write("No suggestions available for this plant/fruit.")
    except Exception as e:
        st.error(f"Error processing image or making prediction: {e}")
