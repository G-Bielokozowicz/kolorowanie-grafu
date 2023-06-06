import networkx as nx
import matplotlib.pyplot as plt
import random
import string


# ---- Heurystyczny largest first -------------- #

def largest_first(graph):
    # Sortowanie wierzchołków malejąco według ich stopni
    sorted_vertices = sorted(graph, key=lambda v: len(graph[v]), reverse=True)

    colors = {}  # Słownik przechowujący przypisane kolory

    # Przypisanie kolorów
    for vertex in sorted_vertices:
        used_colors = set()
        for neighbor in graph[vertex]:
            if neighbor in colors:
                used_colors.add(colors[neighbor])

        # Wybór najmniejszego dostępnego koloru
        for color in range(len(graph)):
            if color not in used_colors:
                colors[vertex] = color
                break

    return colors


# ------------------------------------ #


def largest_first_matrix(graph):
    n = len(graph)  # Liczba wierzchołków

    # Tworzenie listy stopni wierzchołków
    degrees = [sum(row) for row in graph]

    # Sortowanie wierzchołków malejąco według ich stopni
    sorted_vertices = sorted(range(n), key=lambda v: degrees[v], reverse=True)

    colors = {}  # Słownik przechowujący przypisane kolory

    # Przypisanie kolorów
    for vertex in sorted_vertices:
        used_colors = set()
        for neighbor in range(n):
            if graph[vertex][neighbor] == 1 and neighbor in colors:
                used_colors.add(colors[neighbor])

        # Wybór najmniejszego dostępnego koloru
        for color in range(n):
            if color not in used_colors:
                colors[vertex] = color
                break

    return colors

# ----- Dokladny -------------------- #
def graph_coloring_exact(graph):
    colors = {}  # Słownik przechowujący przypisane kolory

    # Sprawdza czy sasiadujace wierzcholki maja ten sam kolor
    def is_safe(vertex, color):
        for neighbor in graph[vertex]:
            if neighbor in colors and colors[neighbor] == color:
                return False
        return True

    # Glowna logika kolorowania
    def graph_coloring(vertex):

        # Jezeli nie ma sasiadujacych wierzcholkow to znaczy, ze wszystkie sa pokolorowane
        if vertex not in graph:
            return True

        # Dla kazdego wierzcholka sprawdzane jest czy mozna bezpiecznie pokolorowac ten wierzcholke
        for color in range(0, len(graph)):
            # Jezeli mozna pokolorwac to pokoloruj
            if is_safe(vertex, color):
                colors[vertex] = color
                if graph_coloring(next_vertex()):
                    return True
                del colors[vertex]

        return False

    def next_vertex():
        for v in graph:
            if v not in colors:
                return v
        return None

    if graph_coloring(next_vertex()):
        return colors
    else:
        return None


# ------------------------------------------ #
def graph_coloring_exact_matrix(graph):
    colors = {}  # Słownik przechowujący przypisane kolory

    # Sprawdza czy sąsiednie wierzchołki mają ten sam kolor
    def is_safe(vertex, color):
        for i in range(len(graph)):
            if graph[vertex][i] == 1 and i in colors and colors[i] == color:
                return False
        return True

    # Główna logika kolorowania
    def graph_coloring(vertex):
        # Jeżeli nie ma sąsiednich wierzchołków, to wszystkie są pokolorowane
        if vertex >= len(graph):
            return True

        # Dla każdego koloru sprawdzane jest, czy można bezpiecznie pokolorować wierzchołek
        for color in range(len(graph)):
            if is_safe(vertex, color):
                colors[vertex] = color
                if graph_coloring(vertex + 1):
                    return True
                del colors[vertex]

        return False

    if graph_coloring(0):
        return colors
    else:
        return None


# ------------------------------------------ #

# Funkcja rysująca graf, wraz z kolorami
def draw_colored_graph(graph, colors):
    G = nx.Graph()

    # Dodawanie wierzchołków
    for node in graph:
        G.add_node(node)

    # Dodawanie krawędzi
    for node, neighbors in graph.items():
        if isinstance(neighbors, list):
            for neighbor in neighbors:
                G.add_edge(node, neighbor)
        else:
            G.add_edge(node, neighbors)

    # Rysowanie grafu z uwzględnieniem kolorów
    pos = nx.spring_layout(G)

    node_colors = [colors[node] for node in G.nodes]

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500)
    nx.draw_networkx_edges(G, pos, edge_color='b')
    nx.draw_networkx_labels(G, pos, font_color='w', font_size=12, font_weight='bold')

    # Wyświetlanie grafu
    plt.axis('off')
    plt.show()


# Generowanie losowego grafu
def generate_random_graph(num_vertices, max_edges_per_vertex, is_complete=False):
    graph = {}
    vertices = list(range(1, num_vertices + 1))

    # Dodawanie wierzchołków do grafu
    for vertex in vertices:
        graph[vertex] = []

    if is_complete:
        for vertex in vertices:
            for neighbor in vertices:
                if neighbor != vertex:
                    graph[vertex].append(neighbor)

    # Dodawanie krawędzi
    else:
        for vertex in vertices:
            num_neighbors = random.randint(1, min(num_vertices - 1, max_edges_per_vertex))
            neighbors = random.sample(vertices, num_neighbors)
            neighbors = [n for n in neighbors if n != vertex]

            for neighbor in neighbors:
                if neighbor not in graph[vertex]:
                    graph[vertex].append(neighbor)

                if vertex not in graph[neighbor]:
                    graph[neighbor].append(vertex)

    return graph


# Generowanie losowego grafu w postaci macierzy


def generate_graph_matrix(size, max_edges, is_complete):
    def count_edges(graph, vertex):
        return sum(graph[vertex])

    graph = [[0] * size for _ in range(size)]

    if is_complete:
        for i in range(size):
            for j in range(i + 1, size):
                graph[i][j] = 1
                graph[j][i] = 1
    else:
        for i in range(size):
            for j in range(i + 1, size):
                if count_edges(graph, i) >= max_edges or count_edges(graph, j) >= max_edges:
                    break

                # Generowanie losowej wartości 0 lub 1
                value = random.randint(0, 1)
                graph[i][j] = value
                graph[j][i] = value

    return graph


#
# def generate_graph_matrix(wielkosc, maks_krawedzi, is_compete=False):
#     macierz = [[0] * wielkosc for _ in range(wielkosc)]
#     if is_compete:
#         for i in range(wielkosc):
#             for j in range(i + 1, wielkosc):
#                 macierz[i][j] = 1
#                 macierz[j][i] = 1
#     else:
#         for i in range(wielkosc):
#             ilosc_krawedzi = random.randint(0, maks_krawedzi)
#             sasiedzi = random.sample(range(wielkosc), ilosc_krawedzi)
#             for sasiad in sasiedzi:
#                 macierz[i][sasiad] = 1
#                 macierz[sasiad][i] = 1
#     return macierz

# Funkcja rysująca graf, wraz z kolorami
def draw_colored_graph_matrix(graph, colors):
    G = nx.Graph()

    # Dodawanie wierzchołków
    for node in range(len(graph)):
        G.add_node(node)

        # Dodawanie krawędzi
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] == 1:
                G.add_edge(i, j)

    # Rysowanie grafu z uwzględnieniem kolorów
    pos = nx.spring_layout(G)

    node_colors = [colors[node] for node in G.nodes]

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500)
    nx.draw_networkx_edges(G, pos, edge_color='b')
    nx.draw_networkx_labels(G, pos, font_color='w', font_size=12, font_weight='bold')

    # Wyświetlanie grafu
    plt.axis('off')
    plt.show()
