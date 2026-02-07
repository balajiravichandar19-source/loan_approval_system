import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = {
    "loan_amount": [50000, 100000, 150000, 200000, 300000],
    "interest_rate": [8, 9, 10, 11, 12],
    "time_years": [1, 2, 3, 4, 5],
    "future_interest": [4000, 18000, 45000, 88000, 180000]
}

df = pd.DataFrame(data)

X = df[["loan_amount", "interest_rate", "time_years"]]
y = df["future_interest"]

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open("loan_model.pkl", "wb"))
