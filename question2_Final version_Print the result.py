import os
import csv
from collections import defaultdict

# Directory where all yearly CSV data files are stored
temperature_data_dir = '/Users/ketianhui/Documents/workplace/homework/HIT137/assignment-2/HIT137 Assignment 2 S1 2025/temperature_data'

# Define seasons based on Australian month groupings
season_month_map = {
    'Summer': ['December', 'January', 'February'],
    'Autumn': ['March', 'April', 'May'],
    'Winter': ['June', 'July', 'August'],
    'Spring': ['September', 'October', 'November']
}

# Store cumulative temperature and count for each season
season_temp_sum = defaultdict(float)
season_temp_count = defaultdict(int)

# For each station, store a list of temperatures per month
station_month_temps = defaultdict(lambda: defaultdict(list))

# Load all CSV files and extract temperature data
for file_name in os.listdir(temperature_data_dir):
    if file_name.endswith(".csv"):
        file_path = os.path.join(temperature_data_dir, file_name)
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                station_id = row['STATION_NAME']
                for month in sum(season_month_map.values(), []):
                    try:
                        temperature = float(row[month])
                        station_month_temps[station_id][month].append(temperature)
                        # Add to seasonal totals if month matches
                        for season, season_months in season_month_map.items():
                            if month in season_months:
                                season_temp_sum[season] += temperature
                                season_temp_count[season] += 1
                    except:
                        continue  # Skip rows with missing or invalid data

# Calculate and write average seasonal temperatures
with open("average_temp.txt", "w") as f:
    f.write("Average Seasonal Temperatures (°C):\n")
    for season in season_month_map:
        if season_temp_count[season] > 0:
            average = season_temp_sum[season] / season_temp_count[season]
            f.write(f"{season}: {average:.2f}°C\n")
        else:
            f.write(f"{season}: No data\n")

# Determine station(s) with the largest temperature range
max_temp_range = -1
stations_with_max_range = []

for station_id, monthly_data in station_month_temps.items():
    combined_temps = []
    for temp_list in monthly_data.values():
        combined_temps.extend(temp_list)
    if combined_temps:
        range_val = max(combined_temps) - min(combined_temps)
        if range_val > max_temp_range:
            max_temp_range = range_val
            stations_with_max_range = [station_id]
        elif range_val == max_temp_range:
            stations_with_max_range.append(station_id)

# Write result for station(s) with the largest range
with open("largest_temp_range_station.txt", "w") as f:
    f.write(f"Largest temperature range: {max_temp_range:.2f} °C\n")
    f.write("Station(s):\n")
    for station_id in stations_with_max_range:
        f.write(station_id + "\n")

# Compute average temperature for each station
station_avg_temp_map = {}

for station_id, monthly_data in station_month_temps.items():
    all_temps = []
    for temp_list in monthly_data.values():
        all_temps.extend(temp_list)
    if all_temps:
        avg_temp = sum(all_temps) / len(all_temps)
        station_avg_temp_map[station_id] = avg_temp

# Identify warmest and coolest stations
warmest_temp = max(station_avg_temp_map.values(), default=None)
coolest_temp = min(station_avg_temp_map.values(), default=None)

warmest_stations = [sid for sid, t in station_avg_temp_map.items() if t == warmest_temp]
coolest_stations = [sid for sid, t in station_avg_temp_map.items() if t == coolest_temp]

# Write warmest and coolest station information
with open("warmest_and_coolest_station.txt", "w") as f:
    if warmest_temp is not None:
        f.write(f"Warmest average temperature: {warmest_temp:.2f} °C\n")
        f.write("Warmest station(s):\n")
        for sid in warmest_stations:
            f.write(sid + "\n")
    if coolest_temp is not None:
        f.write(f"\nCoolest average temperature: {coolest_temp:.2f} °C\n")
        f.write("Coolest station(s):\n")
        for sid in coolest_stations:
            f.write(sid + "\n")
