# Machine Learning API with Flask

## Screenshot
### Folder structures
![image](https://github.com/user-attachments/assets/147cac48-6c38-4cb3-9f19-98d925ab1851)

### Start serving ML Model as API using Flasks
![image](https://github.com/user-attachments/assets/843a3743-69c8-418e-83b2-a6a0cef169f7)

### Testing API in Postman
![image](https://github.com/user-attachments/assets/4ad0cfe1-c86c-4ff7-b77e-9f9beaf14914)

## Prerequisites
Ensure you have Python installed along with the following dependencies:

```bash
pip install flask pandas numpy scikit-learn joblib
```

## Step 1: Train and Save the Machine Learning Model
Run `app.py` to preprocess data, train the model, and save it:

```bash
python app.py
```

## Step 2: Start the Flask API
Run `api.py` to launch the API server:

```bash
python api.py
```

By default, the API runs on `http://127.0.0.1:5000/`.

## Step 3: Test the API
You can test the API using **Postman** or **cURL**.

### Using Postman:
1. Open Postman.
2. Set the request type to `POST`.
3. Use the URL `http://127.0.0.1:5000/predict`.
4. Select the **Body** tab → Choose **raw** → Set format to **JSON**.
5. Paste the following JSON input:

```json
[
    {"Age": 85, "Sex": "male", "Embarked": "S"},
    {"Age": 24, "Sex": "female", "Embarked": "C"}
]
```

6. Click **Send** and check the response.

### Using cURL:
```bash
curl -X POST "http://127.0.0.1:12345/predict" -H "Content-Type: application/json" -d '[
    {"Age": 85, "Sex": "male", "Embarked": "S"},
    {"Age": 24, "Sex": "female", "Embarked": "C"},
]'
```

## Expected Output
```json
{"prediction": [0, 1]}
```
Where `0` means **Not Survived** and `1` means **Survived**.
