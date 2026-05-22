import json, os, sys
from datetime import datetime, timezone

body = os.environ.get('RMS_BODY', '')
if not body:
    sys.exit(1)

d = json.loads(body)['data']
out = {
    "lat": d['latitude'],
    "lon": d['longitude'],
    "satellites": d['satellites'],
    "accuracy": d['accuracy'],
    "altitude": d['altitude'],
    "speed": d['speed'],
    "heading": d['course'],
    "temperature": d['temperature'],
    "signal": d['signal'],
    "operator": d['operator'],
    "timestamp": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
    "source": "rms"
}

with open('gps.json', 'w') as f:
    json.dump(out, f)

print(f"GPS: {d['latitude']}, {d['longitude']}")
