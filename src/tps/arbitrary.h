#ifndef __ARBITRARY_H_INCLUDED__
#define __ARBITRARY_H_INCLUDED__

#include "../game.h"

class ArbitraryGame : public Game {
 private:
  color_t *old_color;
  int edgeCount;
  std::vector<std::vector<int>> edges;

 public:
  ArbitraryGame(unsigned seed, std::string edgelistFile);
  ~ArbitraryGame();
  void step();
  double winProb(color_t color);
};

#endif
