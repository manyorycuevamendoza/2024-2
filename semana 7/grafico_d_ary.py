import matplotlib.pyplot as plt
import networkx as nx

# Crear un gráfico dirigido para representar el heap ternario
G = nx.DiGraph()

# Agregar nodos y relaciones padre-hijo en el heap ternario
# Nodo 1 es el raíz, y cada nodo tiene hasta 3 hijos
nodes = {1: [4, 5, 6], 2: [7, 8, 9], 3: [10, 11, 12]}
for parent, children in nodes.items():
    for child in children:
        G.add_edge(parent, child)

# Dibujar el gráfico
pos = nx.spring_layout(G)
labels = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: '11', 12: '12'}

plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_color='black', labels=labels, arrows=False)
plt.title('Heap Ternario (d=3)')
plt.show()
