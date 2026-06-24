from etl.transform import transform_data


def test_temperature_conversion():

    sample = {
        "current": {
            "time": "2026-01-01T10:00",
            "temperature_2m": 25,
            "relative_humidity_2m": 80
        }
    }

    df = transform_data(sample)

    assert "temperature_f" in df.columns
