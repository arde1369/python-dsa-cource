"""
Scenario:
You are monitoring a stream of temperature readings from multiple sensors. Each reading is a dictionary:

{
    "sensor_id": str,
    "temp": float
}


Some readings may be invalid (temp < -40 or temp > 85).

Requirements:

Ignore invalid readings.

For each sensor, detect if it has 3 consecutive valid readings above 70°C.

When this happens, yield a tuple (sensor_id, [last three temps]).

Must work on real-time streams (i.e., use a generator; don’t store all readings in memory).

Example input:

readings = [
    {"sensor_id": "S1", "temp": 68},
    {"sensor_id": "S1", "temp": 72},
    {"sensor_id": "S1", "temp": 73},
    {"sensor_id": "S1", "temp": 75},
    {"sensor_id": "S2", "temp": 71},
    {"sensor_id": "S2", "temp": 72},
    {"sensor_id": "S2", "temp": 69},
    {"sensor_id": "S2", "temp": 74},
    {"sensor_id": "S2", "temp": 76},
    {"sensor_id": "S2", "temp": 77},
]


Expected generator output:

("S1", [72, 73, 75])
("S2", [74, 76, 77])

"""

def alert(readings):
    tracker = {}
    for reading in readings:
        if reading["sensor_id"] not in tracker:
            tracker[reading["sensor_id"]] = []

        #invalid (temp < -40 or temp > 85).
        if reading["temp"] < -40 or reading["temp"] > 85:
            continue

        #valid readings above 70°C.
        if reading["temp"] > 70:
            tracker[reading["sensor_id"]].append(reading["temp"])
        #If not consecutive, reset readings in tracker
        else:
            tracker[reading["sensor_id"]] = []
        #detect if it has 3 consecutive 
        if len(tracker[reading["sensor_id"]]) >= 3:
            #Yield readings
            yield (reading["sensor_id"], tracker[reading["sensor_id"]])
            #reset readings in tracker after yield
            tracker[reading["sensor_id"]] = []

readings = [
    {"sensor_id": "S1", "temp": 68},
    {"sensor_id": "S1", "temp": 72},
    {"sensor_id": "S1", "temp": 73},
    {"sensor_id": "S1", "temp": 75},
    {"sensor_id": "S2", "temp": 71},
    {"sensor_id": "S2", "temp": 72},
    {"sensor_id": "S2", "temp": 69},
    {"sensor_id": "S2", "temp": 74},
    {"sensor_id": "S2", "temp": 76},
    {"sensor_id": "S2", "temp": 77},
]

for alert_event in alert(readings):
    print(alert_event)