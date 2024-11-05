import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Carregar os dados
data = pd.read_csv('data.csv')

# Separar as características e o rótulo
X = data['opinion']
y = data['label']

# Dividir o conjunto de dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vetorizar as opiniões
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)

# Treinar o modelo
model = MultinomialNB()
model.fit(X_train_vectorized, y_train)

# Salvar o modelo e o vetorizer
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

print("Modelo treinado e salvo com sucesso!")