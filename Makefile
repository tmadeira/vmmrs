CXX=g++
CPPFLAGS=-O4

OBJS=src/game.o src/tps/arbitrary.o src/tps/cycle.o src/tps/clique.o src/taskrunner.o

all: simulator taskrunner

simulator: $(OBJS) src/main_simulator.o
	$(CXX) -o simulator $(OBJS) src/main_simulator.o

taskrunner: $(OBJS) src/main_taskrunner.o
	$(CXX) -o taskrunner $(OBJS) src/main_taskrunner.o

clean:
	rm -rf $(OBJS) src/main_simulator.o src/main_taskrunner.o

distclean: clean
	rm -rf simulator taskrunner
