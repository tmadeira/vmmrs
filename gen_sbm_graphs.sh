#!/bin/bash

for n in `seq 300 100 3000`; do
  for k in 25 100; do
    python experiments/gen_sbm_graph.py $n $k 0.05
  done
done
