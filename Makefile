CXX=g++
CPPFLAGS=-O4

OBJS=src/game.o src/tps/cycle.o src/tps/clique.o src/main.o

all: simulator

simulator: $(OBJS)
	$(CXX) -o simulator $(OBJS)

clean:
	rm -rf $(OBJS)

distclean: clean
	rm -rf simulator
