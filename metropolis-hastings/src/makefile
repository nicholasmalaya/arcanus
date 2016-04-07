# choose compiler
#CC=g++  # gnu (asus laptop)
CC=icpc # taccs lonestar

# optimize
CFLAGS  = -O3

# debug
LDFLAGS = 
SOURCES = $(wildcard *.cpp)

## building object list ##
#
# I prefer the following... over patsubstring
#OBJECTS = $(addsuffix .o,$(basename $(SOURCES)))
#
OBJECTS = $(patsubst %.cpp,%.o,$(SOURCES))

## append include and library paths -- choose what is being used here ##
INCLUDE=
LIBS=-openmp

# one rule to rule them all..
#
all: metropolis-normal metropolis-beta metropolis-openmp regression_tests 

## link the executable ##
regression_tests: regression.o distributions.o
	$(CC) $(CFLAGS) $(LDFLAGS) regression.o distributions.o -o $@ $(LIBS) 

metropolis-normal: mh.o distributions.o
	$(CC) $(CFLAGS) $(LDFLAGS) mh.o distributions.o -o $@ $(LIBS)

metropolis-openmp: mh-omp.o distributions.o
	$(CC) $(CFLAGS) $(LDFLAGS) mh-omp.o distributions.o -o $@ $(LIBS) #-fopenmp -lpthread 

metropolis-beta: mh-beta.o distributions.o
	$(CC) $(CFLAGS) $(LDFLAGS) mh-beta.o distributions.o -o $@ $(LIBS) 

# build cpp object files
%.o: %.cpp
	@echo building $< 
	$(CC) -openmp -c $(CFLAGS) $(INCLUDE) $< -o $@

# build c object files
%.o: %.c
	@echo building $<
	$(CC) -c $(CFLAGS) $(INCLUDE) $< -o $@

# run directive: run the program and print error
run: 
	@echo 'running execs...'
	../bin/regression_tests
	../bin/metropolis-normal
	../bin/metropolis-beta
	../bin/metropolis-openmp


# install directive
install:
	@echo 'installing your routines to bin/'
	mv metropolis-normal metropolis-beta metropolis-openmp regression_tests ../bin/

# regression test suite
check: 
	@echo 'running make check...'
	../bin/regression_tests

# clean directive 'make clean'
clean:
	- /bin/rm $(EXEC) *.o *.mod *~ \#* ../bin/metropolis-normal ../bin/metropolis-beta ../bin/regression_tests ../bin/metropolis-openmp metropolis-normal metropolis-beta regression_tests metropolis-openmp
	@echo 'files cleaned'
