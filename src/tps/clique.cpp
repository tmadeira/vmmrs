#include "clique.h"

void CliqueGame::step() {
  int count[3];
  fillCounts(count);

  std::uniform_int_distribution<int> dist(0, n - 2);
  for (int i = 0; i < n; i++) {
    color_t old_color = color[i];
    count[old_color]--;
    int r = dist(generator);
    color[i] = r < count[agnostic_c]                  ? old_color
               : r < count[agnostic_c] + count[red_c] ? red_c
                                                      : blue_c;
    count[old_color]++;
  }
}

double CliqueGame::winProb(color_t color) {
  if (!decided()) {
    fprintf(stderr, "Graph has agnostic states.\n");
    exit(1);
  }

  int count[3];
  fillCounts(count);
  return count[color] / (double)n;
}
