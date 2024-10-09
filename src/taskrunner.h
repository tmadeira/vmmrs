#ifndef __TASKRUNNER_H_INCLUDED__
#define __TASKRUNNER_H_INCLUDED__

#include <string>

struct TaskInput {
  unsigned seed;
  std::string tp;
  int n;
  double red;
  double blue;
  bool finish;
};

struct TaskOutput {
  int timeNodesActive;
  int timeConsensus;
  double probRedConsensus;
  int consensus;
};

TaskOutput runTask(TaskInput &input);
#endif
