import networkx as nx
import sys
import random

def gen_sbm_graph(n, k, p, seed):
    random.seed(seed)
    g = nx.Graph()

    s = n // k
    
    # Create `s` cliques of size `k`
    for i in range(s):
        clique = nx.complete_graph(k)
        mapping = {node: node + i * k for node in clique.nodes()}
        clique = nx.relabel_nodes(clique, mapping)
        g = nx.compose(g, clique)
    
    # Connect pairs of nodes in distinct subgraphs with probability `p`
    for i in range(s):
        for j in range(i + 1, s):
            for u in range(i * k, (i + 1) * k):
                for v in range(j * k, (j + 1) * k):
                    if random.random() < p:
                        g.add_edge(u, v)
    
    return g

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: %s <n> <k> <p>   # generate (n/k)K(k) subgraphs, connect pair of nodes in different subgraphs with probability p" % sys.argv[0])
        exit(1)

    n = int(sys.argv[1])
    k = int(sys.argv[2])
    p = float(sys.argv[3])

    if n % k != 0:
        print("Error: n must be divisible by k")
        exit(1)

    g = gen_sbm_graph(n, k, p, n)
    nx.write_edgelist(g, "sbm_%d_%d_%.2f.edgelist" % (n, k, p))
