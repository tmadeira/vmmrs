#include "game.h"

#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <random>

Game::Game(int n, unsigned seed) : n(n), generator(seed) {
  color = (color_t *)malloc(sizeof(color_t) * n);
  if (color == NULL) {
    fprintf(stderr, "Could not allocate memory.\n");
    exit(1);
  }
}

Game::~Game() {
  free(color);
  color = NULL;
}

void Game::reset(double red, double blue) {
  int red_count = red * n;
  int blue_count = blue * n;
  int undecided_count = n - red_count - blue_count;
  for (int i = 0; i < red_count; i++) {
    color[i] = red_c;
  }
  for (int i = red_count; i < red_count + blue_count; i++) {
    color[i] = blue_c;
  }
  for (int i = red_count + blue_count; i < n; i++) {
    color[i] = undecided_c;
  }
  shuffle(color, color + n, generator);
}

color_t Game::consensus() {
  for (int i = 0; i < n; i++) {
    if (color[i] != color[0]) {
      return undecided_c;
    }
  }
  return color[0];
}

bool Game::decided() {
  for (int i = 0; i < n; i++) {
    if (color[i] == undecided_c) {
      return false;
    }
  }
  return true;
}

void Game::fillCounts(int *count) {
  count[0] = count[1] = count[2] = 0;
  for (int i = 0; i < n; i++) {
    count[color[i]]++;
  }
}

void Game::debug() {
  printf("n = %d\n", n);
  int count[3];
  fillCounts(count);
  printf("- und: %d\n", count[undecided_c]);
  printf("- red: %d\n", count[red_c]);
  printf("- blu: %d\n", count[blue_c]);
  printf("\n");
}
