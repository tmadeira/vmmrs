from math import sqrt
from run_tasks import run_tasks
from util import update_agg, mean_and_variance
import matplotlib.pyplot as plt

n_runs = 405
step = 20


def tex_plot(x, y):
    print("\\addplot coordinates {")
    for i in range(len(x)):
        print("  (%d, %.6f)" % (x[i], y[i]))
    print("};")


def run_exp():
    results = []
    results.append(run_tasks(n_runs, "clique", 1001, 0.05, 0.05, True))
    results.append(
        run_tasks(n_runs, "graphs/er_1001_0.05.edgelist", 1001, 0.05, 0.05, True)
    )

    agg_formula = [(0, 0, 0), (0, 0, 0)]
    agg_simulation = [(0, 0, 0), (0, 0, 0)]
    stderr_formula = [0.0, 0.0]
    stderr_simulation = [0.0, 0.0]

    x = []
    yy = [[], [], [], []]

    for run in range(n_runs):
        for i in range(len(results)):
            result = results[i]

            agg_formula[i] = update_agg(
                agg_formula[i], result[run]["prob_red_consensus"]
            )
            (avg_formula, variance_formula) = mean_and_variance(agg_formula[i])
            stderr_formula[i] = sqrt(variance_formula) / sqrt(run + 1)

            agg_simulation[i] = update_agg(agg_simulation[i], result[run]["consensus"])
            (avg_simulation, variance_simulation) = mean_and_variance(agg_simulation[i])
            stderr_simulation[i] = sqrt(variance_simulation) / sqrt(run + 1)

        if run >= 9 and (run + 1) % step == 0:
            x.append(run + 1)
            yy[0].append(stderr_formula[0])
            yy[1].append(stderr_formula[1])
            yy[2].append(stderr_simulation[0])
            yy[3].append(stderr_simulation[1])

    plt.plot(x, yy[0])
    plt.plot(x, yy[2])
    plt.plot(x, yy[1], linestyle="dotted")
    plt.plot(x, yy[3], linestyle="dotted")
    plt.savefig("exp1.png")

    tex_plot(x, yy[0])
    tex_plot(x, yy[1])
    tex_plot(x, yy[2])
    tex_plot(x, yy[3])


if __name__ == "__main__":
    run_exp()
