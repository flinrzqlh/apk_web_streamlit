import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import TextBlob  # for sentiment analysis

# Load preprocessed data
df = pd.read_csv('labelNLTKutbk.csv')

# Streamlit App Title with Emoji
st.title("📊 NLP Dashboard")

# Sidebar for user input with Emojis
st.sidebar.title("⚙️ Options")
analysis_type = st.sidebar.selectbox(
    "🔍 Choose Analysis Type", 
    ("🗂️ View Dataset", "📋 Basic Info", "📝 Text Analysis", "😊 Sentiment Distribution", "☁️ Word Cloud", "🔮 Sentiment Analysis")
)

# Option for Viewing the Dataset
if analysis_type == "🗂️ View Dataset":
    st.subheader("🗂️ Preprocessed Dataset")
    st.write("Here is your preprocessed dataset:")
    st.dataframe(df)
    st.write("Dataset columns:")
    st.write(df.columns)

# Option 1: Show basic dataset info
if analysis_type == "📋 Basic Info":
    st.subheader("📋 Basic Information")
    st.write("This section provides general information about the dataset, including its size, data types, and any missing values.")
    
    st.write("Shape of dataset:", df.shape)
    st.write("Data types:")
    st.write(df.dtypes)
    st.write("Missing values in the dataset:")
    st.write(df.isnull().sum())
    
# Option 2: Perform simple text analysis
elif analysis_type == "📝 Text Analysis":
    st.subheader("📝 Text Data Exploration")
    st.write("In this section, we explore the text data by analyzing word lengths, providing insights into the overall text structure.")
    
    if 'steaming_data' in df.columns:
        df['text_length'] = df['steaming_data'].apply(lambda x: len(str(x).split()))
        st.write("Distribution of text lengths:")
        st.write(df['text_length'].describe())
        
        # Plotting text length distribution
        plt.figure(figsize=(10, 5))
        sns.histplot(df['text_length'], kde=True)
        st.pyplot(plt)
    else:
        st.error("Column 'steaming_data' not found in the dataset!")

# Option 3: Sentiment Distribution
elif analysis_type == "😊 Sentiment Distribution":
    st.subheader("😊 Sentiment Distribution")
    st.write("Sentiment distribution shows the frequency of different sentiment categories (e.g., positive, negative, neutral) in the dataset. The graph below illustrates the distribution of sentiments across the dataset.")
    
    if 'sentiment' in df.columns:
        sentiment_counts = df['sentiment'].value_counts()
        st.write(sentiment_counts)

        # Plotting sentiment distribution
        plt.figure(figsize=(10, 5))
        sns.countplot(data=df, x='sentiment')
        st.pyplot(plt)
    else:
        st.error("Column 'sentiment' not found in the dataset!")

# Option 4: Generate Word Cloud
elif analysis_type == "☁️ Word Cloud":
    st.subheader("☁️ Word Cloud")
    st.write("The word cloud provides a visual representation of the most common words in the dataset. The larger the word, the more frequently it appears.")
    
    if 'steaming_data' in df.columns:
        text = " ".join(df['steaming_data'].astype(str))

        # Generate a word cloud
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

        # Display the word cloud
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        st.pyplot(plt)
    else:
        st.error("Column 'steaming_data' not found in the dataset!")

# Option 5: Sentiment Analysis using TextBlob
elif analysis_type == "🔮 Sentiment Analysis":
    st.subheader("🔮 Sentiment Analysis")
    st.write("This section uses TextBlob to calculate the polarity and subjectivity of the text data. Polarity indicates the sentiment (positive or negative), while subjectivity indicates how subjective the text is.")
    
    if 'steaming_data' in df.columns:
        df['polarity'] = df['steaming_data'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
        df['subjectivity'] = df['steaming_data'].apply(lambda x: TextBlob(str(x)).sentiment.subjectivity)

        st.write("Sentiment Analysis Results (Polarity & Subjectivity):")
        st.write(df[['steaming_data', 'polarity', 'subjectivity']])

        # Visualizing sentiment polarity
        plt.figure(figsize=(10, 5))
        sns.histplot(df['polarity'], kde=True, bins=20, color="blue", label="Polarity")
        plt.legend()
        st.pyplot(plt)

        # Visualizing word cloud based on positive sentiment
        positive_text = " ".join(df[df['polarity'] > 0]['steaming_data'].astype(str))
        wordcloud_pos = WordCloud(width=800, height=400, background_color="white").generate(positive_text)
        
        st.write("Positive Sentiment Word Cloud:")
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud_pos, interpolation="bilinear")
        plt.axis("off")
        st.pyplot(plt)
    else:
        st.error("Column 'steaming_data' not found in the dataset!")