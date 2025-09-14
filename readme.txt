Questo progetto calcola il percorso ottimale tra città utilizzando l’algoritmo di **Dijkstra**.  
A ogni rotta sono associati **tempo**, **consumo di carburante** e **rischio**, e il programma permette di inserire città di partenza e arrivo per ottenere il percorso migliore in base a una funzione di costo personalizzabile.

Il peso di ciascun percorso viene calcolato come combinazione lineare di tempo, carburante e rischio, con la possibilità di modificare i pesi nel codice per privilegiare velocità, sicurezza o efficienza.  

Il grafo delle città viene costruito da una lista di rotte bidirezionali, e l’algoritmo restituisce sia il **percorso ottimale** sia i **totali di tempo, carburante e rischio**, rendendo immediata la valutazione dei diversi percorsi.

Il progetto è scritto in **Python 3** e utilizza solo la libreria standard `heapq` per la gestione della coda di priorità, quindi non sono necessarie librerie esterne.  
È pensato come esercizio pratico di algoritmi su grafi e ottimizzazione, ma può essere facilmente esteso aggiungendo nuove città, rotte o visualizzazioni interattive.

Esempi di possibili sviluppi includono l’inserimento dei pesi direttamente dall’input, l’importazione di rotte da file esterni o la creazione di un’interfaccia web con **Flask** o **Streamlit** per rendere il progetto più interattivo.