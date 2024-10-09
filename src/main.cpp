#include <chrono>
#include <cstdio>
#include <cstdlib>
#include <string>

#include "taskrunner.h"

using namespace std;

void panic_usage(char *argv[]) {
  fprintf(stderr,
          "Usage: %s <tp|path_to_edgelist_file> <n> <red> <blue> "
          "[<finish> [<seed>]]\n",
          argv[0]);
  exit(1);
}

int main(int argc, char *argv[]) {
  if (argc < 5) {
    panic_usage(argv);
  }

  string tp = argv[1];

  int n = stol(argv[2]);

  double red = stod(argv[3]);
  double blue = stod(argv[4]);

  bool finish = argc > 5 ? stoi(argv[5]) : false;

  unsigned seed = argc > 6
                      ? stoul(argv[6])
                      : chrono::system_clock::now().time_since_epoch().count();

  TaskInput input = {seed, tp, n, red, blue, finish};
  TaskOutput output = runTask(input);
  printf("time_nodes_active %d\n", output.timeNodesActive);
  printf("prob_red_consensus %.6f\n", output.probRedConsensus);
  if (finish) {
    printf("consensus %d\n", output.consensus);
    printf("time_consensus %d\n", output.timeConsensus);
  }

  return 0;
}
