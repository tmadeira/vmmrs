from math import sqrt
from run_tasks import run_tasks
import matplotlib.pyplot as plt
import numpy as np


def run_exp():
    x = []
    y1 = []
    y2 = []
    for n in range(10, 1000):
        results = run_tasks(100, "clique", n, 0.4, 0.2, True)
        prob_red_consensus = []
        consensus = []
        for result in results:
            prob_red_consensus.append(result["prob_red_consensus"])
            consensus.append(result["consensus"])
        x.append(n)
        y1.append(np.std(prob_red_consensus) / sqrt(len(results)))
        y2.append(np.std(consensus) / sqrt(len(results)))

    plt.plot(x, y1, y2)
    plt.savefig("exp2.png")


if __name__ == "__main__":
    run_exp()
