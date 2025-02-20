from math import sqrt
from run_tasks import run_tasks
import matplotlib.pyplot as plt
import numpy as np
from util import line_styles

num_times = 400

min_n = 300
max_n = 3000
delta_n = 100


def run_exp():
    x = []
    yy_prob = []
    yy_error = []
    for n in range(min_n, max_n + 1, delta_n):
        x.append(n)
    for k in [25, 50, 100]:
        y_prob = []
        y_error = []
        for n in range(min_n, max_n + 1, delta_n):
            tp = "graphs/sbm_%d_%d_0.05.edgelist" % (n, k)
            results = run_tasks(num_times, tp, n, 0.05, 0.05)
            prob_red_consensus = []
            for result in results:
                prob_red_consensus.append(result["prob_red_consensus"])
            y_prob.append(np.mean(prob_red_consensus))
            y_error.append(np.std(prob_red_consensus) / sqrt(len(results)))
        yy_prob.append(y_prob)
        yy_error.append(y_error)

    count = 0

    for y in yy_error:
        print("\\addplot coordinates {")
        for i in range(len(x)):
            print("  (%d, %.6f)" % (x[i], y[i]))
        print("};")
        plt.plot(x, y, linestyle=line_styles[count % 3])
        count += 1
    plt.savefig("exp4.png")


if __name__ == "__main__":
    run_exp()
