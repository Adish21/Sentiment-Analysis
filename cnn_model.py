import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Load model and tokenizer
model = tf.keras.models.load_model("model/text_cnn_model.h5")

with open("model/tokenizer.pkl", "rb") as handle:
    tokenizer = pickle.load(handle)

MAX_LEN = 300  # same as used during training

def predict_sentiment(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=MAX_LEN, padding='post')
    pred = model.predict(padded)[0]
    sentiment = ['Negative', 'Neutral', 'Positive'][pred.argmax()]
    return sentiment
