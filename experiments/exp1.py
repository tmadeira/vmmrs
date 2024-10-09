from math import sqrt
from run_tasks import run_tasks
from welford import update_agg, mean_and_variance
import matplotlib.pyplot as plt


def run_exp():
    results = run_tasks(1000, "clique", 1000, 0.4, 0.2, True)
    runs = 0
    agg_formula = (0, 0, 0)
    agg_simulation = (0, 0, 0)

    x = []
    avg1 = []
    avg2 = []
    err1 = []
    err2 = []

    for result in results:
        runs += 1

        # Formula (Experiment 1).
        agg_formula = update_agg(agg_formula, result["prob_red_consensus"])
        (avg_formula, variance_formula) = mean_and_variance(agg_formula)
        stderr_formula = sqrt(variance_formula) / sqrt(runs)

        # Simulation (Experiment 1.2).
        agg_simulation = update_agg(agg_simulation, result["consensus"])
        (avg_simulation, variance_simulation) = mean_and_variance(agg_simulation)
        stderr_simulation = sqrt(variance_simulation) / sqrt(runs)

        x.append(runs)
        avg1.append(avg_formula)
        avg2.append(avg_simulation)
        err1.append(stderr_formula)
        err2.append(stderr_simulation)

    plt.plot(x, avg1, avg2)
    plt.savefig("exp1_1.png")
    plt.plot(x, err1, err2)
    plt.savefig("exp1_2.png")


if __name__ == "__main__":
    run_exp()
