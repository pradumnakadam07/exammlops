from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Dummy model (for testing)
class DummyModel:
    def predict(self, X):
        return [sum(x) for x in X]

model = DummyModel()

@app.route("/")
def home():
    return "Model is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["input"]
    prediction = model.predict([data])
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)