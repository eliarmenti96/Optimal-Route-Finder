import gpxpy
import gpxpy.gpx

gpx_file1 = open('paths/biroto_RT00000111_1f.gpx', 'r')
gpx_file2 = open('paths/biroto_RT00000238_1f.gpx', 'r')
gpx_file3 = open('paths/biroto_RT00000260_1f.gpx', 'r')
gpx_file4 = open('paths/biroto_RT00000018_1f.gpx', 'r')

gpx1 = gpxpy.parse(gpx_file1)
gpx2 = gpxpy.parse(gpx_file2)
gpx3 = gpxpy.parse(gpx_file3)
gpx4 = gpxpy.parse(gpx_file4)

for track in gpx1.tracks:
    for segment in track.segments:
        for point in segment.points:
            print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))

for track in gpx2.tracks:
    for segment in track.segments:
        for point in segment.points:
            print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))

for track in gpx3.tracks:
    for segment in track.segments:
        for point in segment.points:
            print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))

for track in gpx4.tracks:
    for segment in track.segments:
        for point in segment.points:
            print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))

# 1. creazione lista dei gpx
gpx_list = [gpx1, gpx2, gpx3, gpx4]

# 2. creazione lista delle routes
routes = []

# Funzione per identificare i nodi chiave (inizio, fine o punti importanti)

def get_key_nodes(segment):
    # Filtra punti non validi (None o senza coordinate)
    valid_points = [p for p in segment.points if p and p.latitude is not None and p.longitude is not None]
    if len(valid_points) < 2:
        return []  # Nessun nodo chiave se meno di 2 punti validi
    # Prendi inizio e fine (puoi aggiungere altri criteri)
    return [valid_points[0], valid_points[-1]]


def calculate_time(from_node, to_node):
    # calcola tempo stimato tra due punti
    return 5  

def calculate_safety(from_node, to_node):
    # calcola un punteggio di sicurezza
    return 1  

def calculate_height_difference(from_node, to_node):
    if from_node.elevation is None or to_node.elevation is None:
        return 0
    return abs(from_node.elevation - to_node.elevation)

# 3. Itera su ciascun file GPX e crea le routes
routes = []

""" for gpx in gpx_list:
    for track in gpx.tracks:
        for segment in track.segments:
            key_nodes = get_key_nodes(segment)
            if len(key_nodes) < 2:
                continue  # Salta segmenti vuoti o con nodi invalidi
            for from_node, to_node in zip(key_nodes, key_nodes[1:]):
                # Controlla ancora che i nodi non siano None
                if from_node is None or to_node is None:
                    continue
                route = {
                    'from': from_node,
                    'to': to_node,
                    'time': calculate_time(from_node, to_node),
                    'safety': calculate_safety(from_node, to_node),
                    'height_difference': calculate_height_difference(from_node, to_node)
                }
                routes.append(route) """

for gpx in gpx_list:
    for track in gpx.tracks:
        for segment in track.segments:
            key_nodes = get_key_nodes(segment)
            if not key_nodes:
                continue
            for from_node, to_node in zip(key_nodes, key_nodes[1:]):
                route = {
                    'from': from_node,
                    'to': to_node,
                    'time': calculate_time(from_node, to_node),
                    'safety': calculate_safety(from_node, to_node),
                    'height_difference': calculate_height_difference(from_node, to_node)
                }
                routes.append(route)

print(f"Routes generate: {len(routes)}")

# 4. Stampa le routes per verifica
for route in routes:
    print(route)