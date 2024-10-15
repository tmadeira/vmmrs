import networkx as nx
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: %s <n> <p>" % sys.argv[0])
        exit(1)

    n = int(sys.argv[1])
    p = float(sys.argv[2])
    g = nx.erdos_renyi_graph(n, p)
    nx.write_edgelist(g, "er_graph.txt")

