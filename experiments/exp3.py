from math import sqrt
from run_tasks import run_tasks
import matplotlib.pyplot as plt
import numpy as np


def run_exp2():
    x = []
    for n in range(101, 1001, 2):
        x.append(n)
    for p in [0.01, 0.05, 0.1, 0.2, 0.3]:
        y = []
        for n in range(101, 1001, 2):
            results = run_tasks(200, "cycle", n, p, p)
            prob_red_consensus = []
            for result in results:
                prob_red_consensus.append(result["prob_red_consensus"])
            y.append(np.std(prob_red_consensus) / sqrt(len(results)))
        plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    run_exp2()
