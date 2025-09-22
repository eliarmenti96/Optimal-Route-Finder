""" import heapq

# Lista delle rotte
routes = [
    {"from": "A", "to": "B", "time": 15, "fuel": 1.2, "risk": 3},
    {"from": "A", "to": "C", "time": 10, "fuel": 1.0, "risk": 5},
    {"from": "B", "to": "D", "time": 12, "fuel": 1.1, "risk": 4},
    {"from": "C", "to": "D", "time": 8,  "fuel": 0.9, "risk": 2},
    {"from": "C", "to": "E", "time": 20, "fuel": 1.6, "risk": 6},
    {"from": "D", "to": "E", "time": 6,  "fuel": 0.5, "risk": 3},
    {"from": "E", "to": "F", "time": 9,  "fuel": 0.7, "risk": 4},
    {"from": "B", "to": "F", "time": 30, "fuel": 2.5, "risk": 7},
    {"from": "A", "to": "F", "time": 40, "fuel": 3.0, "risk": 9}
]

# Funzione per costruire il grafo
def build_graph(routes):
    grafo = {}
    for route in routes:
        a, b = route["from"], route["to"]
        time, fuel, risk = route["time"], route["fuel"], route["risk"]
        grafo.setdefault(a, []).append((b, time, fuel, risk))
        grafo.setdefault(b, []).append((a, time, fuel, risk))  # bidirezionale
    return grafo

# Funzione per calcolare il peso personalizzato
def cost(time, fuel, risk, w_time=1, w_fuel=0.7, w_risk=0.8):
    return time * w_time + fuel * w_fuel + risk * w_risk

# Algoritmo di Dijkstra
def dijkstra(grafo, start, cost_function):
    distanze = {nodo: float('inf') for nodo in grafo}
    distanze[start] = 0
    predecessori = {nodo: None for nodo in grafo}
    coda = [(0, start)]

    while coda:
        distanza_corrente, nodo_corrente = heapq.heappop(coda)

        if distanza_corrente > distanze[nodo_corrente]:
            continue

        for vicino, time, fuel, risk in grafo[nodo_corrente]:
            peso = cost_function(time, fuel, risk)
            nuova_distanza = distanza_corrente + peso

            if nuova_distanza < distanze[vicino]:
                distanze[vicino] = nuova_distanza
                predecessori[vicino] = nodo_corrente
                heapq.heappush(coda, (nuova_distanza, vicino))

    return distanze, predecessori

# Funzione per ricostruire il percorso
def ricostruisci_percorso(predecessori, destinazione):
    percorso = []
    while destinazione is not None:
        percorso.append(destinazione)
        destinazione = predecessori[destinazione]
    return list(reversed(percorso))


# MAIN: interazione con l'utente
grafo = build_graph(routes)

start = input("Inserisci città di partenza: ").strip().upper()
end = input("Inserisci città di arrivo: ").strip().upper()

if start not in grafo or end not in grafo:
    print("❌ Città non trovata nel grafo.")
else:
    # posso modificare qui i pesi per personalizzare il tipo di ottimizzazione
    distanze, predecessori = dijkstra(grafo, start, lambda t, f, r: cost(t, f, r, w_time=1, w_fuel=0.6, w_risk=1))

    print(f"\n✅ Distanza ottimizzata da {start} a {end}: {distanze[end]:.2f}")
    percorso = ricostruisci_percorso(predecessori, end)
    print(f"📍 Percorso: {' ➜ '.join(percorso)}")

    tempo_tot = 0
    consumo_tot = 0
    rischio_tot = 0

    for i in range(len(percorso) - 1):
        partenza = percorso[i]
        arrivo = percorso[i + 1]
    
        for route in routes:
            if (route["from"] == partenza and route["to"] == arrivo) or (route["from"] == arrivo and route["to"] == partenza):
                tempo_tot += route["time"]
                consumo_tot += route["fuel"]
                rischio_tot += route["risk"]
                break
    
    print(f"⏱ Tempo totale: {tempo_tot} min")
    print(f"⛽ Consumo totale: {consumo_tot} litri")
    print(f"⚠️ Rischio totale: {rischio_tot}") """