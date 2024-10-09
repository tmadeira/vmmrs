#include <boost/asio/post.hpp>
#include <boost/asio/thread_pool.hpp>
#include <cstdio>
#include <cstdlib>
#include <future>
#include <string>

#include "taskrunner.h"

using namespace std;

void panic_usage(char *argv[]) {
  fprintf(stderr, "Usage: %s <runs> <tp> <n> <red> <blue> <finish>\n", argv[0]);
  fprintf(stderr, "Example: %s 500 clique 1000 0.1 0.1 0\n", argv[0]);
  exit(1);
}

int main(int argc, char *argv[]) {
  if (argc != 7) {
    panic_usage(argv);
  }

  int runs = stoi(argv[1]);
  string tp = argv[2];
  int n = stoi(argv[3]);
  double red = stof(argv[4]);
  double blue = stof(argv[5]);
  bool finish = stoi(argv[6]);

  boost::asio::thread_pool pool;
  for (unsigned run = 0; run < runs; run++) {
    TaskInput input = {run + 1, tp, n, red, blue, finish};
    boost::asio::post(pool, [input]() {
      TaskOutput output = runTask(input);
      printf("%u,%d,%.6f,%d,%d\n", input.seed, output.timeNodesActive,
             output.probRedConsensus, output.consensus, output.timeConsensus);
    });
  }
  pool.join();

  return 0;
}
