import pandas as pd
from datetime import datetime, timezone

df = pd.read_csv("data/raw/data.csv").copy()

df["row_id"] = range(len(df))
df["event_timestamp"] = datetime.now(timezone.utc)

df = df.rename(columns={
    "sepal length (cm)": "sepal_length",
    "sepal width (cm)": "sepal_width",
    "petal length (cm)": "petal_length",
    "petal width (cm)": "petal_width",
})

cols = [
    "row_id",
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "target",
    "event_timestamp",
]

df[cols].to_parquet("data/feature_repo/iris_features.parquet", index=False)

print("Saved feature data to data/feature_repo/iris_features.parquet")