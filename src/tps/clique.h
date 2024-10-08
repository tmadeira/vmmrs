#ifndef __CLIQUE_H_INCLUDED__
#define __CLIQUE_H_INCLUDED__

#include "../game.h"

class CliqueGame : public Game {
  using Game::Game;

 public:
  void step();
  double winProb(color_t color);
};

#endif
