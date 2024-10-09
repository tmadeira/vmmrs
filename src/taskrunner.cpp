#include "taskrunner.h"

#include <cstdio>
#include <string>

#include "game.h"
#include "tps/arbitrary.h"
#include "tps/clique.h"
#include "tps/cycle.h"

TaskOutput runTask(TaskInput &input) {
  TaskOutput output;

  Game *g;
  if (input.tp == "clique") {
    g = new CliqueGame(input.n, input.seed);
  } else if (input.tp == "cycle") {
    g = new CycleGame(input.n, input.seed);
  } else {
    g = new ArbitraryGame(input.seed, input.tp);
  }

  g->reset(input.red, input.blue);

  int iterations = 0;
  while (!g->decided()) {
    g->step();
    iterations++;
  }

  output.timeNodesActive = iterations;
  output.probRedConsensus = g->winProb(red_c);

  if (input.finish) {
    while (!g->consensus()) {
      g->step();
      iterations++;
    }

    output.consensus = g->consensus() == red_c;
    output.timeConsensus = iterations;
  }

  free(g);
  return output;
}
