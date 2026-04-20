import pandas as pd
from feast import FeatureStore

store = FeatureStore(repo_path="feature_repo")

entity_df = pd.DataFrame({
    "row_id": [0, 1, 2],
    "event_timestamp": pd.to_datetime([
        "2026-04-20 17:20:00+00:00",
        "2026-04-20 17:20:00+00:00",
        "2026-04-20 17:20:00+00:00",
    ], utc=True),
})

features = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "iris_features:sepal_length",
        "iris_features:sepal_width",
        "iris_features:petal_length",
        "iris_features:petal_width",
        "iris_features:target",
    ],
).to_df()

print(features)