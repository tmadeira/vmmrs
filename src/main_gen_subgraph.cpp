#include <chrono>
#include <cstdio>
#include <cstdlib>
#include <string>

#include "tps/arbitrary.h"

using namespace std;

void panic_usage(char *argv[]) {
  fprintf(stderr, "Usage: %s <path_to_edgelist_file> <n>", argv[0]);
  exit(1);
}

int main(int argc, char *argv[]) {
  if (argc != 3) {
    panic_usage(argv);
  }

  string edgelist = argv[1];
  int n = stol(argv[2]);

  ArbitraryGame G(n, edgelist);
  G.resizeGraph(n);
  vector<pair<int, int>> edges = G.getEdgeList();
  for (pair<int, int> edge : edges) {
    printf("%d %d\n", edge.first, edge.second);
  }

  return 0;
}
