from flask import Flask, render_template, request, url_for
import folium
import gpxpy

app = Flask(__name__)

# funzione dummy per calcolo percorso migliore
def find_best_route(start, end):
    best_time = 15.3
    best_safety = 0.95
    best_heigth = 200
    lat_start, lon_start = start
    lat_end, lon_end = end

    # crea mappa centrata tra i due punti
    map = folium.Map(location=[(lat_start + lat_end) / 2, (lon_start + lon_end) / 2], zoom_start = 12)

    # aggiungi il marker
    folium.Marker([lat_start, lon_start], popup="Partenza").add_to(m)
    folium.Marker([lat_end, lon_end], popup="Arrivo").add_to(map)

    # aggiungi polyline
    folium.PolyLine([[lat_start, lon_start], [lat_end, lon_end]], color="blue", weight=5).add_to(map)

    # salva la mappa
    map.save("static/map.html")

    return {
        "time_min": best_time,
        "safety": best_safety,
        "height_diff_m": best_heigth
    }

# funzione per ottenere le coordinate dall'input
def get_coordinates(location_str):
    try:
        lat, lon = map(float, location_str.split(','))
        return (lat, lon)
    except:
        return None


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        start_input = request.form["start"]
        end_input = request.form["end"]
        
        start_coords = get_coordinates(start_input)
        end_coords = get_coordinates(end_input)
        
        if not start_coords or not end_coords:
            return "Errore: Inserisci coordinate valide nel formato lat,lon"
        
        best_route = find_best_route(start_coords, end_coords)
        return render_template("result.html", best_route=best_route)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)