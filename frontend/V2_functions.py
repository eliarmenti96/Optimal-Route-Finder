import gpxpy
import math

# === 1. Carica i GPX ===
gpx_paths = [
    'paths/biroto_RT00000111_1f.gpx',
    'paths/biroto_RT00000238_1f.gpx',
    'paths/biroto_RT00000260_1f.gpx',
    'paths/biroto_RT00000018_1f.gpx'
]

gpx_list = [gpxpy.parse(open(p, 'r')) for p in gpx_paths]

# === 2. Funzioni di supporto ===
def haversine(lat1, lon1, lat2, lon2):
    """Calcola distanza tra due punti in km."""
    R = 6371.0
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

def calculate_time(path_coords, avg_speed_kmh=20):
    """Tempo stimato in minuti lungo il percorso."""
    total_dist = 0
    for i in range(len(path_coords)-1):
        lat1, lon1, *_ = path_coords[i]
        lat2, lon2, *_ = path_coords[i+1]
        total_dist += haversine(lat1, lon1, lat2, lon2)
    return (total_dist / avg_speed_kmh) * 60

def calculate_height_difference(path_coords):
    """Differenza altimetrica tra primo e ultimo punto."""
    first = path_coords[0][2] if path_coords[0][2] else 0
    last = path_coords[-1][2] if path_coords[-1][2] else 0
    return abs(last - first)

def calculate_safety(path_coords):
    """Simulazione punteggio sicurezza (più alto = meglio)."""
    # Per ora fisso, puoi aggiungere logiche su curve, traffico, urbanità ecc.
    return 1.0

# === 3. Estrae tutti i punti dal GPX ===
def extract_full_path():
    path_coords = []
    for gpx in gpx_list:
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    if point and point.latitude and point.longitude:
                        path_coords.append((point.latitude, point.longitude, point.elevation))
    return path_coords

# === 4. Trova il percorso migliore ===
def find_best_route(start=None, end=None):
    path_coords = extract_full_path()
    if not path_coords:
        return None

    time = calculate_time(path_coords)
    safety = calculate_safety(path_coords)
    height_diff = calculate_height_difference(path_coords)

    return {
        "full_path": [(lat, lon) for lat, lon, _ in path_coords],
        "time_min": round(time, 1),
        "safety": round(safety, 2),
        "height_diff_m": round(height_diff, 1)
    }
