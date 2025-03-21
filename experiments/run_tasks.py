from pathlib import Path
import os

task_runner_bin = str(Path(__file__).parent.parent.absolute()) + "/taskrunner"


def run_tasks(runs, tp, n, red, blue, finish=False):
    stream = os.popen(
        "%s %d %s %d %f %f %d" % (task_runner_bin, runs, tp, n, red, blue, finish)
    )
    results = []
    lines = stream.read().strip().split("\n")
    for line in lines:
        [seed, time_nodes_active, prob_red_consensus, consensus, time_consensus] = (
            line.split(",")
        )
        results.append(
            {
                "seed": seed,
                "time_nodes_active": int(time_nodes_active),
                "prob_red_consensus": float(prob_red_consensus),
                "consensus": int(consensus),
                "time_consensus": int(time_consensus),
            }
        )
    results = sorted(results, key=lambda x: x["seed"])
    return results
