CXX=g++
CPPFLAGS=-O3 -std=c++17

OBJS=src/game.o src/tps/arbitrary.o src/tps/cycle.o src/tps/clique.o src/taskrunner.o

all: gen_subgraph simulator taskrunner

gen_subgraph: $(OBJS) src/main_gen_subgraph.o
	$(CXX) -o gen_subgraph $(OBJS) src/main_gen_subgraph.o

simulator: $(OBJS) src/main_simulator.o
	$(CXX) -o simulator $(OBJS) src/main_simulator.o

taskrunner: $(OBJS) src/main_taskrunner.o
	$(CXX) -o taskrunner $(OBJS) src/main_taskrunner.o

clean:
	rm -rf $(OBJS) src/main_gen_subgraph.o src/main_simulator.o src/main_taskrunner.o

distclean: clean
	rm -rf gen_subgraph simulator taskrunner
