import streamlit as st
import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# Fungsi untuk memuat dan menggabungkan semua dataset CSV
@st.cache_data
def load_data_from_folder(folder_path):
    all_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    df_list = []
    
    # Membaca setiap file CSV dan menyesuaikan kolomnya
    for file in all_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        
        # Ubah nama kolom agar sesuai dengan yang diharapkan
        if 'Instagram Comment Text' in df.columns and 'Sentiment' in df.columns:
            df = df.rename(columns={'Instagram Comment Text': 'text', 'Sentiment': 'label'})
            df_list.append(df[['text', 'label']])
    
    # Menggabungkan semua DataFrame menjadi satu
    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df

# Training model
@st.cache_resource
def train_model(data):
    X = data['text']
    y = data['label']
    
    # Split data menjadi training dan testing set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Membuat pipeline dengan TF-IDF vectorizer dan model Naive Bayes
    model = Pipeline([
        ('vectorizer', TfidfVectorizer(ngram_range=(1, 2))),
        ('classifier', MultinomialNB())
    ])
    
    # Melatih model
    model.fit(X_train, y_train)
    # Menghitung akurasi
    accuracy = accuracy_score(y_test, model.predict(X_test))
    return model, accuracy

def main():
    st.title("Sentiment Analysis NLP App")
    st.subheader("Streamlit Projects")
    
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    # Ganti 'folder_path' dengan path ke folder tempat semua file CSV disimpan
    folder_path = "./Dataset-Sentimen-Analisis-Bahasa-Indonesia"
    data = load_data_from_folder(folder_path)
    model, accuracy = train_model(data)

    if choice == "Home":
        st.subheader("Home")
        st.write(f"Model Accuracy: {accuracy:.2f}")
        with st.form("nlpForm"):
            raw_text = st.text_area("Enter Indonesian Text Here")
            submit_button = st.form_submit_button(label='Analyze')
        
        # Layout
        col1, col2 = st.columns(2)
        if submit_button:
            with col1:
                st.info("Results")
                # Memprediksi sentimen
                prediction = model.predict([raw_text])[0]
                st.write(f"Sentiment: {prediction}")
 
    else:
        st.subheader("About")
        st.write("This application uses a machine learning model trained on an Indonesian sentiment analysis dataset.")

if __name__ == '__main__':
    main()