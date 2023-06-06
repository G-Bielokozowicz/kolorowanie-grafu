from graph import largest_first
from graph import generate_random_graph
from graph import graph_coloring_exact
from graph import graph_coloring_exact_matrix
from graph import draw_colored_graph
from graph import generate_graph_matrix
from graph import draw_colored_graph_matrix
from graph import largest_first_matrix
import time
import sys


def exact(graph, should_print=False):
    print("Kolorowanie algorytmem dokładnym")
    # Pokoloruj graf
    start_time = time.time()
    exact_coloring = graph_coloring_exact_matrix(graph)
    end_time = time.time()

    # Oblicz czas
    execution_time = end_time - start_time
    # print(execution_time)

    # Wyświetlenie przypisanych kolorów
    if should_print:
        if exact_coloring is not None:
            for vertex, color in exact_coloring.items():
                print(f"Wierzchołek {vertex}: Kolor {color}")
            draw_colored_graph_matrix(graph, exact_coloring)
        else:
            print("Nie udało się znaleźć poprawnego kolorowania.")

    return exact_coloring, execution_time


def heuristic(graph, should_print=False):
    print("Kolorowanie algorytmem heurtystycznym")
    # Pokoloruj graf
    start_time = time.time()
    heuristic_coloring = largest_first_matrix(graph)
    end_time = time.time()
    # Oblicz czas
    execution_time = end_time - start_time
    # print(execution_time)

    # Wyświetlenie przypisanych kolorów
    if should_print:
        for vertex, color in heuristic_coloring.items():
            print(f"Wierzchołek {vertex}: Kolor {color}")
        draw_colored_graph_matrix(graph, heuristic_coloring)
    return heuristic_coloring, execution_time






if __name__ == "__main__":
    # Ustawienie limitu rekurencji
    #sys.setrecursionlimit(15000)

    # Generowanie grafu
    liczba_wierzcholkow = 20
    liczba_krawedzi = 10
    czy_graf_pelny = False
    graph = generate_random_graph(liczba_wierzcholkow, liczba_krawedzi, czy_graf_pelny)
    graph_matrix = generate_graph_matrix(liczba_wierzcholkow,liczba_krawedzi,czy_graf_pelny)

    # Wypisanie grafu w postaci slownika
    # for key, value in graph.items():
    #     print(f'{key}: {value}')


    # Kolorowanie grafu
    exact_coloring, exact_execution_time = exact(graph_matrix, True)
    heuristic_coloring, heuristic_execution_time = heuristic(graph_matrix, True)

    liczba_kolorow_dokladny = len(set(exact_coloring.values()))
    liczba_kolorow_heurystyczny = len(set(heuristic_coloring.values()))


    print("Liczba wierzchołków w grafie: {}".format(liczba_wierzcholkow))
    print("Maksymalna liczba krawędzi wychodzących od wierzchołka: {}".format(liczba_krawedzi))
    print("Graf pelny: {}".format(czy_graf_pelny))

    print("Objętość pamięciowa grafu: {} bajtów".format(sys.getsizeof(graph)))
    print("Objętość pamięciowa grafu: {} bajtów".format(sys.getsizeof(graph_matrix)))
    print("Objętość pamięciowa kolorowania dokładnego: {} bajtów".format(sys.getsizeof(exact_coloring)))
    print("Objętość pamięciowa kolorowania heurystycznego: {} bajtów".format(sys.getsizeof(heuristic_coloring)))

    print("Czas kolorowania algorytmem dokładnym: {} sekund".format(exact_execution_time))
    print("Czas kolorowania algorytmem heurystycznym: {} sekund".format(heuristic_execution_time))

    print("Liczba kolorów wykorzystana w algorytmie dokładnym: {}".format(liczba_kolorow_dokladny))
    print("Liczba kolorów wykorzystana w algorytmie heurystycznym: {}".format(liczba_kolorow_heurystyczny))