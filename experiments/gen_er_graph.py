import networkx as nx
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("Usage (1): %s <n> <p>   # generate G(n, p)" % sys.argv[0])
        print(
            "Usage (2): %s <p>       # generate G(n, p) for n in range(301, 3002, 100)"
            % sys.argv[0]
        )
        exit(1)

    if len(sys.argv) == 2:
        p = float(sys.argv[1])
        for n in range(301, 3002, 100):
            g = nx.erdos_renyi_graph(n, p, seed=n)
            nx.write_edgelist(g, "er_%d_%.2f.edgelist" % (n, p))
    else:
        n = int(sys.argv[1])
        p = float(sys.argv[2])
        g = nx.erdos_renyi_graph(n, p, seed=n)
        nx.write_edgelist(g, "er_%d_%.2f.edgelist" % (n, p))
