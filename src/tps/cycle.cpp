#include "cycle.h"

#include <algorithm>

CycleGame::CycleGame(int n, unsigned seed) : Game(n, seed) {
  if (n % 2 == 0) {
    fprintf(stderr, "CycleGame requires odd `n`.\n");
    exit(1);
  }

  old_color = (color_t *)malloc(sizeof(color_t) * n);
  if (old_color == NULL) {
    fprintf(stderr, "Could not allocate memory.\n");
    exit(1);
  }
}

void CycleGame::step() {
  std::uniform_int_distribution<int> dist(0, 1);
  std::swap(old_color, color);
  for (int i = 0; i < n; i++) {
    int r = dist(generator);
    color[i] = r ? old_color[(i + n - 1) % n] : old_color[(i + 1) % n];
    if (color[i] == undecided_c) {
      color[i] = old_color[i];
    }
  }
}

double CycleGame::winProb(color_t color) {
  if (!decided()) {
    fprintf(stderr, "Graph has undecided states.\n");
    exit(1);
  }

  int count[3];
  fillCounts(count);
  return count[color] / (double)n;
}
