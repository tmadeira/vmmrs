#ifndef __GAME_H_INCLUDED__
#define __GAME_H_INCLUDED__

#include <random>

enum color_t { agnostic_c = 0, red_c = 1, blue_c = 2 };

class Game {
 protected:
  color_t *color;
  int n;
  std::minstd_rand generator;

 public:
  Game(int n, unsigned seed);
  ~Game();
  void reset(double red, double blue);
  color_t consensus();
  bool decided();
  void fillCounts(int *count);
  void debug();

  virtual void step() = 0;
  virtual double winProb(color_t color) = 0;
};

#endif
