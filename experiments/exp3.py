from math import sqrt
from run_tasks import run_tasks
import matplotlib.pyplot as plt
from util import update_agg, mean_and_variance, line_styles, tex_plot
from exp_pokec import CACHE_FILE
import csv

n_runs = 200
step = 20


def run_exp():
    x = []

    results = []
    results.append(run_tasks(n_runs, "clique", 1632803, 0.05, 0.05, False))
    # results.append(run_tasks(n_runs, "cycle", 1632803, 0.05, 0.05, False))

    result = []
    with open(CACHE_FILE) as f:
        r = csv.reader(f, delimiter=" ")
        for row in r:
            prob = float(row[2])
            result.append(
                {
                    "prob_red_consensus": prob,
                }
            )
    results.append(result)

    agg_formula = []
    stderr_formula = []
    yy = []

    for _ in range(len(results)):
        agg_formula.append((0, 0, 0))
        stderr_formula.append(0.0)
        yy.append([])

    for run in range(n_runs):
        for i in range(len(results)):
            result = results[i]

            agg_formula[i] = update_agg(
                agg_formula[i], result[run]["prob_red_consensus"]
            )
            (_avg_formula, variance_formula) = mean_and_variance(agg_formula[i])
            stderr_formula[i] = sqrt(variance_formula) / sqrt(run + 1)

        if run >= 9 and (run + 1) % step == 0:
            x.append(run + 1)

            for i in range(len(results)):
                yy[i].append(stderr_formula[i])

    count = 0
    for y in yy:
        plt.plot(x, y, linestyle=line_styles[count % len(results)])
        count += 1

    plt.savefig("exp1_1.6m.png")

    for i in range(len(results)):
        tex_plot(x, yy[i])


if __name__ == "__main__":
    run_exp()
