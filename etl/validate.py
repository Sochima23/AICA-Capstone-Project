def validate_data(df):

    required_columns = [
        "time",
        "temperature_2m",
        "relative_humidity_2m",
        "date"
    ]

    missing = [
        col
        for col in required_columns
        if col not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing columns: {missing}"
        )

    return True
