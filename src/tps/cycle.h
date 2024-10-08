#ifndef __CYCLE_H_INCLUDED__
#define __CYCLE_H_INCLUDED__

#include "../game.h"

class CycleGame : public Game {
 private:
  color_t *old_color;

 public:
  CycleGame(int n, unsigned seed);
  void step();
  double winProb(color_t color);
};

#endif
