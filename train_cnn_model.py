import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Conv1D, GlobalMaxPooling1D, Dense, Dropout

# Load dataset
df = pd.read_csv('data/news_data.csv')

# Combine headline and article
df['text'] = df['headline'].fillna('') + " " + df['article'].fillna('')

# Encode target labels
label_encoder = LabelEncoder()
df['encoded_label'] = label_encoder.fit_transform(df['label'])  # ['Negative', 'Neutral', 'Positive']

# Save label encoder (optional if needed later)
with open('model/label_encoder.pkl', 'wb') as le_file:
    pickle.dump(label_encoder, le_file)

# Tokenization
tokenizer = Tokenizer(num_words=5000, oov_token="<OOV>")
tokenizer.fit_on_texts(df['text'])
sequences = tokenizer.texts_to_sequences(df['text'])

# Padding
X = pad_sequences(sequences, maxlen=300)
y = to_categorical(df['encoded_label'], num_classes=3)

# Save tokenizer
with open('model/tokenizer.pkl', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

# Build the Text CNN model
model = Sequential([
    Embedding(input_dim=5000, output_dim=128, input_length=300),
    Conv1D(filters=128, kernel_size=5, activation='relu'),
    GlobalMaxPooling1D(),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(3, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

# Train model
model.fit(X, y, epochs=5, batch_size=32, validation_split=0.2)

# Save model
model.save('model/text_cnn_model.h5')
print("Model and tokenizer saved successfully.")
