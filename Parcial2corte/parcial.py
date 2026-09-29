import networkx as nx
import matplotlib.pyplot as plt

# Creamos el grafo
G = nx.Graph()

# Yo soy el centro de la red
yo = "Sebastián"
# Los grupos de personas
familia = ["Mamá", "Papá", "Hermano", "Abuela", "Tío Carlos"]
barrio = ["Juan", "Camilo", "Andrés", "Felipe"]
universidad = ["Laura", "Daniela", "Nicolás", "Sofía"]

# Conexiones de yo con cada persona
for persona in familia:
    G.add_edge(yo, persona)
for persona in barrio:
    G.add_edge(yo, persona)
for persona in universidad:
    G.add_edge(yo, persona)
    # Conexiones entre los integrantes de la familia
G.add_edge("Mamá", "Papá")
G.add_edge("Mamá", "Hermano")
G.add_edge("Papá", "Hermano")
G.add_edge("Mamá", "Abuela")
G.add_edge("Abuela", "Tío Carlos")

# Conexiones entre los amigos del barrio
G.add_edge("Juan", "Camilo")
G.add_edge("Camilo", "Andrés")
G.add_edge("Andrés", "Felipe")
G.add_edge("Juan", "Felipe")

# Conexiones entre los compañeros de la universidad
G.add_edge("Laura", "Daniela")
G.add_edge("Daniela", "Nicolás")
G.add_edge("Nicolás", "Sofía")
G.add_edge("Laura", "Sofía")
# Colores: cada grupo tiene un color diferente
colores = []
for nodo in G.nodes():
    if nodo == yo:
        colores.append("red")
    elif nodo in familia:
        colores.append("orange")
    elif nodo in barrio:
        colores.append("lightgreen")
    else:
        colores.append("skyblue")

# Dibujamos el grafo
plt.figure(figsize=(10, 8))
posicion = nx.spring_layout(G, seed=5)
nx.draw(G, posicion, with_labels=True, node_color=colores,
        node_size=1800, font_size=9, edge_color="gray")
plt.title("Mi red social personal")
plt.savefig("red_social.png")
plt.show()