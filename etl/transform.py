import pandas as pd
df = pd.DataFrame([data["current"]])
print(df)
print(df.columns)
print(df.dtypes)

df.columns = (df.columns.str.lower().str.strip())
df["time"] = pd.to_datetime(df["time"])
print(df.dtypes)

print(df.isnull().sum())

df = df.drop_duplicates()
print(df.shape)

df = df[
    (df["temperature_2m"] >= -50) &
    (df["temperature_2m"] <= 60)
]
df = df[
    (df["relative_humidity_2m"] >= 0) &
    (df["relative_humidity_2m"] <= 100)
]
df["location_name"] = "Port Harcourt"
df["location_name"] = df["location_name"].str.title()

df["time"] = pd.to_datetime(df["time"])

df["date"] = df["time"].dt.date

df["hour"] = df["time"].dt.hour

df["temperature_f"] = (
    df["temperature_2m"] * 9/5
) + 32

df["day_name"] = df["time"].dt.day_name()

print(df.columns.tolist())
