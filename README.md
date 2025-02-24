# Voter Model Meets Rumour Spreading

## A Study of Consensus Protocols on Graphs with Agnostic Nodes

_By Marcelo Matheus Gauy, Anna Abramishvili, Eduardo Colli, Tiago Madeira,
Frederik Mallmann-Trenn, Vinícius Franco Vasconcelos, David Kohan Marzagão._

This repository contains code, data and plots used in an accepted paper that
will be published in the 24th International Conference on Autonomous Agents
and Multi-Agent Systems (AAMAS 2025). To appear.

We also have an extended version of the paper available on ArXiv. It contains 
complete proofs and some additional experiments. It can be accessed here: 
https://arxiv.org/abs/2502.15029

### Usage

To compile:

```
$ make
```

You must have GCC/G++.

To run:

```
$ ./simulator <tp> <n> <red> <blue> [<finish> [<seed>]]
```

where `<tp>` is the network structure (or the path of an edge list file with
an arbitrary structure), `<n>` is the number of nodes, `<red>` (`<blue>`) is
the proportion of red (blue) nodes, `<finish>` is a boolean (1/0) indicating
whether to run the simulation until consensus, and `<seed>` is the random seed.

**Supported network structures:**
clique, cycle, custom edgefile (treated as a undirected graph).

### Experiments

You must have Python and compile the source code in C++ first. Then, to create
a virtual environment and install requirements:

```
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r experiments/requirements.txt
```

To run experiments 1 and 2 (which produce the figures used in the paper):

```
$ python experiments/exp1.py
$ python experiments/exp2.py
```

To run experiments 3 and 4 (which produce the figures used in the appendix):

```
$ python experiments/exp3.py
$ python experiments/exp4.py
```

### Utilities

- `/experiments/gen_er_graph.py` generates Erdos-Renyi (ER) graphs and saves
  them to .edgelist files.
- `/experiments/exp1_er.py` and `/experiments/exp2_er.py` runs experiments 1
  and 2 on ER graphs.
- `/experiments/gen_sbm_graph.py` generates stochastic block models and saves
  them to .edgelist files (and `/gen_sbm_graphs.sh` generates all SBM graphs
  that were used in Experiment 4).
- `/taskrunner` runs several tasks concurrently (using threads).
- `/gen_subgraph` generates a connected subgraph from a given graph (i/o are
  .edgelist files).
