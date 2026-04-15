import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/raw/data.csv")

train, test = train_test_split(df, test_size=0.2, random_state=42)

Path("data/processed").mkdir(parents=True, exist_ok=True)

train.to_csv("data/processed/train.csv", index=False)
test.to_csv("data/processed/test.csv", index=False)