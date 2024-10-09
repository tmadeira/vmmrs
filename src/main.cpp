#include <chrono>
#include <cstdio>
#include <cstdlib>
#include <string>

#include "game.h"
#include "tps/arbitrary.h"
#include "tps/clique.h"
#include "tps/cycle.h"

using namespace std;

void panic_usage(char *argv[]) {
  fprintf(stderr,
          "Usage: %s <clique|cycle|path_to_edgelist_file> <n> <red> <blue> "
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

  Game *g;

  if (tp == "clique") {
    g = new CliqueGame(n, seed);
  } else if (tp == "cycle") {
    g = new CycleGame(n, seed);
  } else {
    g = new ArbitraryGame(seed, tp);
  }

  g->reset(red, blue);

  int iterations = 0;
  while (!g->decided()) {
    g->step();
    iterations++;
  }

  printf("time_nodes_active %d\n", iterations);
  printf("prob_red_consensus %.6f\n", g->winProb(red_c));

  if (finish) {
    while (!g->consensus()) {
      g->step();
      iterations++;
    }

    printf("consensus %d\n", g->consensus() == red_c);
    printf("time_consensus %d\n", iterations);
  }

  free(g);

  return 0;
}
