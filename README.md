Consensus with Agnostic States
==

This repository contains code, data and plots of a paper on consensus with
agnostic states.

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
clique, cycle.

### Experiments

You must have Python. To create a virtual environment and install requirements:

```
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r experiments/requirements.txt
```

To run experiment 1:

```
$ python experiments/exp1.py
```

