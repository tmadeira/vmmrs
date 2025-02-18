import csv
from math import sqrt
from run_tasks import run_tasks
import matplotlib.pyplot as plt
from pathlib import Path
from util import update_agg, mean_and_variance, line_styles, tex_plot

CACHE_FILE = "exp_pokec.txt"

n_runs = 200
step = 20


def run_exp():
    if not Path(CACHE_FILE).exists():
        results = run_tasks(
            200, "graphs/soc-pokec-relationships.edgelist", 0, 0.05, 0.05, False
        )
        for result in results:
            print(
                result["seed"],
                result["time_nodes_active"],
                result["prob_red_consensus"],
            )
    else:
        agg = (0, 0, 0)
        run = 0
        x = []
        y = []
        with open(CACHE_FILE) as f:
            r = csv.reader(f, delimiter=" ")
            for row in r:
                run += 1
                prob = float(row[2])
                agg = update_agg(agg, prob)

                if run % step == 0:
                    x.append(run)

                    (_avg, variance) = mean_and_variance(agg)
                    stderr = sqrt(variance) / sqrt(run)
                    y.append(stderr)

        plt.plot(x, y)
        plt.show()


if __name__ == "__main__":
    run_exp()
