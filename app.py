from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Carregar o modelo e o vetorizer
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analisar', methods=['POST'])
def analisar():
    data = request.json
    opinion = data['opinion']
    opinion_vectorized = vectorizer.transform([opinion])
    prediction = model.predict(opinion_vectorized)[0]
    return jsonify({'label': prediction})

if __name__ == '__main__':
    app.run(debug=True)