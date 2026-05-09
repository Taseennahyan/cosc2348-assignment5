# Compiler and flags
CC = gcc
CFLAGS = -Wall -Wextra

# Target executable
TARGET = calculator

# Object files
OBJS = main.o addition.o subtraction.o multiplication.o division.o

# Default rule: build the calculator executable
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

# Compile each .c file into a .o file
main.o: main.c operations.h
	$(CC) $(CFLAGS) -c main.c

addition.o: addition.c operations.h
	$(CC) $(CFLAGS) -c addition.c

subtraction.o: subtraction.c operations.h
	$(CC) $(CFLAGS) -c subtraction.c

multiplication.o: multiplication.c operations.h
	$(CC) $(CFLAGS) -c multiplication.c

division.o: division.c operations.h
	$(CC) $(CFLAGS) -c division.c

# Clean rule: remove binaries and object files
clean:
	rm -f $(OBJS) $(TARGET)
