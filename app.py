import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
df = pd.read_csv(url)
include = ['Age', 'Sex', 'Embarked', 'Survived']
df_ = df[include]

# Handle missing values
categoricals = []
for col, col_type in df_.dtypes.items():
    if col_type == 'O':
        categoricals.append(col)
    else:
        df_[col].fillna(0, inplace=True)

df_ohe = pd.get_dummies(df_, columns=categoricals, dummy_na=True)

# Train model
dependent_variable = 'Survived'
X = df_ohe[df_ohe.columns.difference([dependent_variable])]
y = df_ohe[dependent_variable]
lr = LogisticRegression()
lr.fit(X, y)

# Save model
joblib.dump(lr, 'model.pkl')
joblib.dump(list(X.columns), 'model_columns.pkl')

print("Model and columns saved!")
