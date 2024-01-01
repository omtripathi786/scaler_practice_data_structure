import ephem
from datetime import datetime

def calculate_planetary_positions(date, time, latitude, longitude):
    observer = ephem.Observer()
    observer.lat = str(latitude)
    observer.lon = str(longitude)
    observer.date = datetime(date.year, date.month, date.day, time.hour, time.minute, time.second)

    sun = ephem.Sun(observer)
    moon = ephem.Moon(observer)
    mercury = ephem.Mercury(observer)
    venus = ephem.Venus(observer)
    mars = ephem.Mars(observer)
    jupiter = ephem.Jupiter(observer)
    saturn = ephem.Saturn(observer)
    rahu = ephem.TrueNode(observer)  # Rahu
    ketu = ephem.TrueNode(observer, use_mean=True)  # Ketu

    planetary_positions = {
        'Sun': sun.ra,
        'Moon': moon.ra,
        'Mercury': mercury.ra,
        'Venus': venus.ra,
        'Mars': mars.ra,
        'Jupiter': jupiter.ra,
        'Saturn': saturn.ra,
        'Rahu': rahu.ra,
        'Ketu': ketu.ra,
    }

    return planetary_positions

# Example usage
date_of_birth = datetime(1990, 1, 1)
time_of_birth = datetime.strptime("12:00:00", "%H:%M:%S")
latitude, longitude = 37.7749, -122.4194  # San Francisco, CA

positions = calculate_planetary_positions(date_of_birth, time_of_birth, latitude, longitude)
print(positions)
