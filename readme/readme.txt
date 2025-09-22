# 🚗 Optimal Route Finder #

Questo progetto calcola il percorso ottimale tra città utilizzando l’algoritmo di **Dijkstra**.  
A ogni rotta sono associati **tempo**, **consumo di carburante** e **rischio**, e il programma permette di inserire città di partenza e arrivo per ottenere il percorso migliore in base a una funzione di costo personalizzabile.

Il peso di ciascun percorso viene calcolato come combinazione lineare di tempo, carburante e rischio, con la possibilità di modificare i pesi nel codice per privilegiare velocità, sicurezza o efficienza.  

Il grafo delle città viene costruito da una lista di rotte bidirezionali, e l’algoritmo restituisce sia il **percorso ottimale** sia i **totali di tempo, carburante e rischio**, rendendo immediata la valutazione dei diversi percorsi.

Il progetto è scritto in **Python 3** e utilizza solo la libreria standard `heapq` per la gestione della coda di priorità, quindi non sono necessarie librerie esterne.  
È pensato come esercizio pratico di algoritmi su grafi e ottimizzazione, ma può essere facilmente esteso aggiungendo nuove città, rotte o visualizzazioni interattive.

Esempi di possibili sviluppi includono l’inserimento dei pesi direttamente dall’input, l’importazione di rotte da file esterni o la creazione di un’interfaccia web con **Flask** o **Streamlit** per rendere il progetto più interattivo.

----------------------------------------------------------------------------------------------------

This project calculates the optimal route between cities using Dijkstra’s algorithm.
Each route is associated with time, fuel consumption, and risk, and the program allows users to input a starting and ending city to obtain the best path based on a customizable cost function.

The weight of each path is calculated as a linear combination of time, fuel, and risk, with the ability to adjust the weights in the code to prioritize speed, safety, or efficiency.

The city graph is built from a list of bidirectional routes, and the algorithm returns both the optimal path and the total time, fuel, and risk, allowing for immediate evaluation of different routes.

The project is written in Python 3 and only uses the standard heapq library for priority queue management, so no external libraries are required.
It is designed as a practical exercise in graph algorithms and optimization, but it can be easily extended by adding new cities, routes, or interactive visualizations.

Potential future developments include allowing weight input directly from the user, importing routes from external files, or creating a web interface with Flask or Streamlit to make the project more interactive.