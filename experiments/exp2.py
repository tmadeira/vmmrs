from math import sqrt
from run_tasks import run_tasks
import matplotlib.pyplot as plt
import numpy as np
from util import line_styles, tex_plot

num_times = 400

min_n = 301
max_n = 3001
delta_n = 100


def run_exp():
    x = []
    yy_prob = []
    yy_error = []
    for n in range(min_n, max_n + 1, delta_n):
        x.append(n)
    for p in [0.025, 0.25]:
        for tp in ["clique", "cycle"]:
            y_prob = []
            y_error = []
            for n in range(min_n, max_n + 1, delta_n):
                results = run_tasks(num_times, tp, n, p, p)
                prob_red_consensus = []
                for result in results:
                    prob_red_consensus.append(result["prob_red_consensus"])
                y_prob.append(np.mean(prob_red_consensus))
                y_error.append(np.std(prob_red_consensus) / sqrt(len(results)))
            yy_prob.append(y_prob)
            yy_error.append(y_error)

    count = 0

    for y in yy_error:
        plt.plot(x, y, linestyle=line_styles[count % 2])
        tex_plot(x, y)
        count += 1
    plt.savefig("exp2.png")


if __name__ == "__main__":
    run_exp()
