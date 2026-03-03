import json
f = open('stops.txt')
content = f.read()

stops = []
lines = []

for line in content.strip().split('\n'):
    lineContent = line.split(',')

    stops.append({
        "name": lineContent[2],
        "coordinates": [float(lineContent[4]), float(lineContent[5])]
    })

print(stops)

with open("wfile.json", "w") as file:
    file.write(json.dumps(stops))