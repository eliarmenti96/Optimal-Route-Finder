import gpxpy
import gpxpy.gpx
import math

# === 1. Lettura file GPX ===
gpx_paths = [
    'paths/biroto_RT00000111_1f.gpx',
    'paths/biroto_RT00000238_1f.gpx',
    'paths/biroto_RT00000260_1f.gpx',
    'paths/biroto_RT00000018_1f.gpx'
]

gpx_list = [gpxpy.parse(open(path, 'r')) for path in gpx_paths]

# === 2. Funzioni di supporto ===

def haversine(lat1, lon1, lat2, lon2):
    """Calcola la distanza tra due punti in km."""
    R = 6371.0
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

def get_key_nodes(segment):
    """Estrae punti validi (inizio e fine)."""
    valid_points = [p for p in segment.points if p and p.latitude and p.longitude]
    if len(valid_points) < 2:
        return []
    return [valid_points[0], valid_points[-1]]

def calculate_time(from_node, to_node, avg_speed_kmh=20):
    """Tempo stimato in minuti."""
    dist_km = haversine(from_node.latitude, from_node.longitude, to_node.latitude, to_node.longitude)
    return (dist_km / avg_speed_kmh) * 60

def calculate_safety(from_node, to_node):
    """Simulazione punteggio sicurezza (più alto = meglio)."""
    # puoi aggiungere logiche reali (es. altitudine, urbanità, curve, ecc.)
    return 1.0

def calculate_height_difference(from_node, to_node):
    """Differenza altimetrica assoluta in metri."""
    if from_node.elevation is None or to_node.elevation is None:
        return 0
    return abs(from_node.elevation - to_node.elevation)

def calculate_score(time, safety, height_diff, w_time=0.6, w_safety=0.3, w_height=0.1):
    """Formula di valutazione combinata."""
    # Più basso = meglio
    return (w_time * time) + (w_height * (height_diff / 10)) + (w_safety * (1 / safety))

# === 3. Creazione routes ===
routes = []

for gpx in gpx_list:
    for track in gpx.tracks:
        for segment in track.segments:
            key_nodes = get_key_nodes(segment)
            if not key_nodes:
                continue
            for from_node, to_node in zip(key_nodes, key_nodes[1:]):
                time = calculate_time(from_node, to_node)
                safety = calculate_safety(from_node, to_node)
                height_diff = calculate_height_difference(from_node, to_node)
                score = calculate_score(time, safety, height_diff)
                route = {
                    'from': (from_node.latitude, from_node.longitude),
                    'to': (to_node.latitude, to_node.longitude),
                    'time_min': time,
                    'safety': safety,
                    'height_diff_m': height_diff,
                    'score': score
                }
                routes.append(route)

print(f"Totale routes generate: {len(routes)}")

# === 4. Trova la migliore ===
if routes:
    best_route = min(routes, key=lambda r: r['score'])
    print("\n📍 Percorso migliore:")
    print(f"Da: {best_route['from']}")
    print(f"A: {best_route['to']}")
    print(f"Tempo stimato: {best_route['time_min']:.2f} min")
    print(f"Dislivello: {best_route['height_diff_m']:.1f} m")
    print(f"Sicurezza: {best_route['safety']}")
    print(f"Punteggio totale: {best_route['score']:.3f}")
else:
    print("Nessuna route valida trovata.")
