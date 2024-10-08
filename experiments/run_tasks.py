import csv
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
import os
import sys


threads = multiprocessing.cpu_count()


def run_task(seed, tp, n, red, blue):
    stream = os.popen("./simulator %s %d %f %f %d" % (tp, n, red, blue, seed))
    results = stream.read().strip().split("\n")
    for line in results:
        if line.startswith("time_nodes_active"):
            time_nodes_active = line.split(" ")[1]
        if line.startswith("prob_red_consensus"):
            prob_red_consensus = line.split(" ")[1]
        if line.startswith("consensus"):
            consensus = line.split(" ")[1]
        if line.startswith("time_consensus"):
            time_consensus = line.split(" ")[1]
    return {
        "seed": seed,
        "time_nodes_active": int(time_nodes_active),
        "prob_red_consensus": float(prob_red_consensus),
        "consensus": int(consensus),
        "time_consensus": int(time_consensus),
    }


def run_tasks(runs, tp, n, red, blue):
    tasks = []
    with ThreadPoolExecutor(max_workers=threads) as e:
        for seed in range(1, runs):
            tasks.append(e.submit(run_task, seed, tp, n, red, blue))
    results = []
    for task in tasks:
        results.append(task.result())
    return results


def panic_usage():
    print("Usage: run_tasks.py <runs> <tp> <n> <red> <blue>")
    print("Example: run_tasks.py 500 clique 1000 0.3333 0.3333")
    exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 6:
        panic_usage()
    runs = int(sys.argv[1])
    tp = sys.argv[2]
    n = int(sys.argv[3])
    red = float(sys.argv[4])
    blue = float(sys.argv[5])
    header = [
        "seed",
        "time_nodes_active",
        "prob_red_consensus",
        "consensus",
        "time_consensus",
    ]
    results = run_tasks(runs, tp, n, red, blue)
    writer = csv.writer(sys.stdout)
    writer.writerow(header)
    for result in results:
        writer.writerow(
            [
                result["seed"],
                result["time_nodes_active"],
                result["prob_red_consensus"],
                result["consensus"],
                result["time_consensus"],
            ]
        )
