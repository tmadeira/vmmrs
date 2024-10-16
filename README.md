Consensus Protocols on Graphs with Agnostic States
==

This repository contains code, data and plots of a paper on consensus protocols
on graphs with agnostic states.

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
clique, cycle, custom edgefile.

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

### Utilities

- `experiments/gen_er_graph.py` generates ER graphs and saves them to .edgelist
  files.
- `experiments/exp1_er.py` and `experiments/exp2_er.py` runs experiments 1
  and 2 on ER graphs.
- `/taskrunner` runs several tasks concurrently (using threads).
- `/gen_subgraph` generates a connected subgraph from a given graph (i/o are
  .edgelist files).

