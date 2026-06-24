import sqlite3
import logging
try:
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()

    print("Database connected")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fact_weather (
        weather_id INTEGER PRIMARY KEY AUTOINCREMENT,
        weather_date TEXT,
        temperature REAL,
        humidity REAL,
        location_name TEXT
    )
    """)

    cursor.execute("""
    INSERT INTO fact_weather
    (weather_date, temperature, humidity, location_name)
    VALUES ("2026-06-22", 24.7, 93, "Port Harcourt" )
    """)

    conn.commit()

    cursor.execute("SELECT * FROM fact_weather")

    rows = cursor.fetchall()

    for row in rows:
        print(row)
    conn.commit()

    logging.info("Data loaded successfully")

except sqlite3.Error as e:
    logging.error(f"Database error: {e}")
    print(e)

finally:
    conn.close()
