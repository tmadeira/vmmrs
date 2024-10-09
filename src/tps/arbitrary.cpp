#include "arbitrary.h"

#include <cstdio>
#include <fstream>
#include <iostream>
#include <sstream>

using namespace std;

pair<int, int> readEdges(vector<vector<int>> &edges, string edgelistFile) {
  ifstream f;
  f.open(edgelistFile);
  if (!f) {
    fprintf(stderr, "Could not open file '%s'.\n", edgelistFile.c_str());
    exit(1);
  }

  int n = 0;
  vector<pair<int, int>> E;
  string line;
  while (getline(f, line)) {
    if (line[0] == '#') {
      continue;
    }
    int from, to;
    sscanf(line.c_str(), "%d %d", &from, &to);
    E.push_back(make_pair(from, to));
    n = max(n, max(from + 1, to + 1));
  }
  int m = E.size();

  edges.resize(n);

  // XXX: We treat all edges as undirected.
  for (pair<int, int> e : E) {
    edges[e.first].push_back(e.second);
    edges[e.second].push_back(e.first);
  }

  return make_pair(n, m);
}

ArbitraryGame::ArbitraryGame(unsigned seed, string edgelistFile)
    : Game(1, seed) {
  pair<int, int> nodesAndEdges = readEdges(edges, edgelistFile);
  n = nodesAndEdges.first;
  edgeCount = nodesAndEdges.second;

  free(color);
  color = (color_t *)malloc(sizeof(color_t) * n);
  if (color == NULL) {
    fprintf(stderr, "Could not allocate memory.\n");
    exit(1);
  }

  old_color = (color_t *)malloc(sizeof(color_t) * n);
  if (old_color == NULL) {
    fprintf(stderr, "Could not allocate memory.\n");
    exit(1);
  }
}

ArbitraryGame::~ArbitraryGame() { free(old_color); }

void ArbitraryGame::step() {
  swap(old_color, color);
  for (int i = 0; i < n; i++) {
    uniform_int_distribution<int> dist(0, edges[i].size() - 1);
    int r = edges[i][dist(generator)];
    color[i] = old_color[r];
    if (color[i] == undecided_c) {
      color[i] = old_color[i];
    }
  }
}

double ArbitraryGame::winProb(color_t c) {
  if (!decided()) {
    fprintf(stderr, "Graph has undecided states.\n");
    exit(1);
  }

  int d = 0;
  for (int i = 0; i < n; i++) {
    if (color[i] == c) {
      d += edges[i].size();
    }
  }

  double p = d / (double)(2.0 * edgeCount);
  return p;
}
