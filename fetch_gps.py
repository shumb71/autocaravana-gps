import json, os, sys
from datetime import datetime, timezone

body = os.environ.get('RMS_BODY', '')
if not body:
    print("Error: RMS_BODY vacio")
    sys.exit(1)

data = json.loads(body)['data']

out = {
    "lat": data['latitude'],
    "lon": data['longitude'],
    "satellites": data['satellites'],
    "accuracy": data['accuracy'],
    "altitude": data['altitude'],
    "speed": data['speed'],
    "heading": data['course'],
    "temperature": data['temperature'],
    "signal": data['signal'],
    "operator": data['operator'],
    "timestamp": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
    "source": "rms"
}

with open('gps.json', 'w') as f:
    json.dump(out, f)

print(f"GPS guardado: {out['lat']}, {out['lon']}")
