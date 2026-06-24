from etl.validate import validate_data
import pandas as pd


def test_validation():

    df = pd.DataFrame({
        "time": ["2026-01-01"],
        "temperature_2m": [25],
        "relative_humidity_2m": [80],
        "date": ["2026-01-01"]
    })

    assert validate_data(df)
