#ifndef __ARBITRARY_H_INCLUDED__
#define __ARBITRARY_H_INCLUDED__

#include <map>

#include "../game.h"

using namespace std;

class ArbitraryGame : public Game {
 private:
  color_t *old_color;
  int edgeCount;
  vector<vector<int>> edges;
  void resizeHelper(map<int, int> &M, int u);

 public:
  ArbitraryGame(unsigned seed, string edgelistFile);
  ~ArbitraryGame();
  void reset(double red, double blue) override;
  void step() override;
  double winProb(color_t color) override;
  void resizeGraph(int n);
  vector<pair<int, int>> getEdgeList();
};

#endif
