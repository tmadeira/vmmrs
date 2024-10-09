Consensus with Inactive States
==

This repository contains code, data and plots of a paper on consensus with
inactive states.

### Usage

To compile:

```
$ make
```

You must have GCC/G++.

To run:

```
$ ./simulator <tp> <n> <red> <blue> [<seed>]
```

where `<tp>` is the network structure, `<n>` is the number of nodes, `<red>`
(`<blue>`) is the proportion of red (blue) nodes, `<seed>` is the random
seed.

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

