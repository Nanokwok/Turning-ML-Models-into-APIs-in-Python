from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and column names
lr = joblib.load("model.pkl")
model_columns = joblib.load("model_columns.pkl")


@app.route('/predict', methods=['POST'])
def predict():
    try:
        json_ = request.json
        query = pd.DataFrame(json_)
        query = pd.get_dummies(query)
        query = query.reindex(columns=model_columns, fill_value=0)

        prediction = lr.predict(query).tolist()
        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(port=12345, debug=True)
