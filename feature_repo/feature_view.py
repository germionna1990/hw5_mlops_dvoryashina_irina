from datetime import timedelta
from feast import Entity, FeatureView, FileSource, Field
from feast.types import Float32, Int64

iris_source = FileSource(
    path="../data/feature_repo/iris_features.parquet",
    timestamp_field="event_timestamp",
)

row_id = Entity(
    name="row_id",
    join_keys=["row_id"],
)

iris_features_view = FeatureView(
    name="iris_features",
    entities=[row_id],
    ttl=timedelta(days=3650),
    schema=[
        Field(name="sepal_length", dtype=Float32),
        Field(name="sepal_width", dtype=Float32),
        Field(name="petal_length", dtype=Float32),
        Field(name="petal_width", dtype=Float32),
        Field(name="target", dtype=Int64),
    ],
    source=iris_source,
)