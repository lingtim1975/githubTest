import pandas as pd

mqtt_data = {
    "device": "CC8480A4AE30",
    "time": "2023-09-27 10:10:24.698089",
    "src": 0,
    "wifi": 13,
    "latitude": 1.35575521,
    "longitude": 103.8452142,
    "accuracy": 26,
    "battery": 3599,
    "battPercentage": 46,
    "temperature": 400
}

# Create a DataFrame from the MQTT data
df = pd.DataFrame([mqtt_data])

# Define the desired CSV file name
csv_file_name = "mqtt_data.csv"

# Save the DataFrame to a CSV file
df.to_csv(csv_file_name, index=False)

print(f"Data has been saved to {csv_file_name}")
