import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Read TempoWordNet data
def read_tempowordnet(file_path):
    columns = ["ID", "Synset_name", "POS", "Synset_gloss", "Prob_of_being_Past", "Prob_of_being_Present", "Prob_of_being_Future", "Prob_of_being_Atemporal"]
    
    df = pd.read_csv(file_path, 
                     sep='\t', 
                     names=columns, 
                     comment='#',
                     encoding='utf-8')
    
    return df

# Load the data
tempowordnet_df = read_tempowordnet('./TempoWordNet/TempoWnL_1.0.txt')

# Create 'Word' column
tempowordnet_df['Word'] = tempowordnet_df['Synset_name'].str.split('.').str[0]

# Convert probability columns to numeric
prob_columns = ["Prob_of_being_Past", "Prob_of_being_Present", "Prob_of_being_Future", "Prob_of_being_Atemporal"]
for col in prob_columns:
    tempowordnet_df[col] = pd.to_numeric(tempowordnet_df[col], errors='coerce')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Preprocess text
def preprocess_text(text):
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    words = [lemmatizer.lemmatize(word.lower()) for word in words if word.lower() not in stop_words]
    return words

# Calculate temporal probabilities
def calculate_temporal_probabilities(words):
    temporal_probs = []
    for word in words:
        try:
            word_probs = tempowordnet_df[tempowordnet_df['Word'].str.lower() == word.lower()].iloc[0]
            probs = (word_probs['Prob_of_being_Past'], word_probs['Prob_of_being_Present'], 
                     word_probs['Prob_of_being_Future'], word_probs['Prob_of_being_Atemporal'])
            temporal_probs.append(probs)
        except IndexError:
            print(f'{word} not found in TWN, hence skipped')
            continue
    
    if temporal_probs:
        avg_probs = np.mean(temporal_probs, axis=0)
        return avg_probs
    else:
        return None

# Process a sentence
def process_sentence(sentence):
    words = preprocess_text(sentence)
    print("Preprocessed words:", words)
    avg_probs = calculate_temporal_probabilities(words)
    return avg_probs

# Test the functions
test_sentence = "Unprocessed lifestyle is the best dead"
avg_temporal_probs = process_sentence(test_sentence)

if avg_temporal_probs is not None:
    print(f"Average Temporal Probabilities:\nPast: {avg_temporal_probs[0]:.4f}, Present: {avg_temporal_probs[1]:.4f}, Future: {avg_temporal_probs[2]:.4f}, Atemporal: {avg_temporal_probs[3]:.4f}")
else:
    print("No valid words found in TempoWordNet.")

# Print DataFrame info for verification
print("\nDataFrame Info:")
print(tempowordnet_df.info())
print("\nFirst few rows of the DataFrame:")
print(tempowordnet_df.head())