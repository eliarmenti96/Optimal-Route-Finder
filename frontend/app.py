from flask import Flask, render_template, request
import folium
from V2_functions import find_best_route

app = Flask(__name__)

# Genera mappa con percorso completo
def generate_map(best_route):
    coords = best_route['full_path']
    map_center = [(coords[0][0]+coords[-1][0])/2, (coords[0][1]+coords[-1][1])/2]
    m = folium.Map(location=map_center, zoom_start=13)
    folium.PolyLine(coords, color="blue", weight=5).add_to(m)
    folium.Marker(coords[0], popup="Partenza").add_to(m)
    folium.Marker(coords[-1], popup="Arrivo").add_to(m)
    m.save("static/map.html")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        best_route = find_best_route()
        if best_route:
            generate_map(best_route)
            return render_template("result.html", best_route=best_route)
        else:
            return "Nessuna route valida trovata."
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
