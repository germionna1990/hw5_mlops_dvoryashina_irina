import pandas as pd
import pickle
import yaml
from sklearn.ensemble import RandomForestClassifier

with open("params.yaml", "r") as f:
    params = yaml.safe_load(f)

train = pd.read_csv("data/processed/train.csv")

X = train.drop("target", axis=1)
y = train["target"]

model = RandomForestClassifier(
    n_estimators=params["n_estimators"],
    random_state=params["random_state"]
)
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved to model.pkl")