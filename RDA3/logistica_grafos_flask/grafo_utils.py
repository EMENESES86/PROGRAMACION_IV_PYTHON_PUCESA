import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import networkx as nx
import io

# Ciudades costeras
COSTERAS = {'Manta', 'Portoviejo', 'Guayaquil'}

# Construir el grafo dirigido y ponderado
def construir_grafo():
    G = nx.DiGraph()
    aristas = [
        ('Ibarra', 'Quito', 10),
        ('Quito', 'Santo Domingo', 15),
        ('Quito', 'Manta', 30),
        ('Santo Domingo', 'Manta', 12),
        ('Manta', 'Portoviejo', 5),
        ('Portoviejo', 'Guayaquil', 20),
        ('Guayaquil', 'Cuenca', 25),
        ('Cuenca', 'Loja', 18),
        ('Quito', 'Cuenca', 35),
        ('Santo Domingo', 'Guayaquil', 22),
        ('Guayaquil', 'Loja', 40),
    ]

    for origen, destino, costo in aristas:
        G.add_edge(origen, destino, weight=costo)
    
    return G

# Función para renderizar el grafo como imagen
def grafo_a_imagen():
    G = construir_grafo()
    pos = nx.spring_layout(G, seed=85)
    pesos = nx.get_edge_attributes(G, 'weight')

    fig, ax = plt.subplots(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=pesos)
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return buf


def camino_optimo_con_costera(origen='Ibarra', destino='Loja'):
    G = construir_grafo()

    try:
        camino = nx.dijkstra_path(G, origen, destino, weight='weight')
        costo = nx.dijkstra_path_length(G, origen, destino, weight='weight')

        contiene_costera = any(ciudad in COSTERAS for ciudad in camino)
        return {
            "camino": camino,
            "costo": costo,
            "valido": contiene_costera
        }
    except nx.NetworkXNoPath:
        return {
            "camino": [],
            "costo": None,
            "valido": False
        }


def obtener_ciudades():
    return [
        "Ibarra", "Quito", "Santo Domingo", "Manta",
        "Portoviejo", "Guayaquil", "Cuenca", "Loja"
    ]
