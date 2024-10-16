from math import sqrt
from run_tasks import run_tasks
from welford import update_agg, mean_and_variance
import matplotlib.pyplot as plt

n_runs = 401
step = 20

line_styles = ["solid", "dotted", "dashed"]


def tex_plot(x, y):
    print("\\addplot coordinates {")
    for i in range(len(x)):
        print("  (%d, %.6f)" % (x[i], y[i]))
    print("};")


def run_exp():
    x = []

    results = []
    results.append(run_tasks(n_runs, "clique", 1001, 0.05, 0.05, True))
    results.append(run_tasks(n_runs, "cycle", 1001, 0.05, 0.05, True))
    results.append(
        run_tasks(
            n_runs,
            "graphs/soc-pokec-relationships_1001.edgelist",
            1001,
            0.05,
            0.05,
            True,
        )
    )

    agg_formula = []
    agg_simulation = []
    stderr_formula = []
    stderr_simulation = []
    yy = []

    for _ in range(len(results)):
        agg_formula.append((0, 0, 0))
        agg_simulation.append((0, 0, 0))
        stderr_formula.append(0.0)
        stderr_simulation.append(0.0)
        yy.append([])
        yy.append([])

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

            for i in range(len(results)):
                yy[i].append(stderr_formula[i])
            for i in range(len(results)):
                yy[len(results) + i].append(stderr_simulation[i])

    count = 0
    for y in yy:
        plt.plot(x, y, linestyle=line_styles[count % len(results)])
        count += 1

    plt.savefig("exp1.png")

    for i in range(len(results)):
        tex_plot(x, yy[2 * i])
    for i in range(len(results)):
        tex_plot(x, yy[2 * i + 1])


if __name__ == "__main__":
    run_exp()
