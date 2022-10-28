TARGET_EXEC := check_permutations
CC = gcc -std=gnu99

DEBUG_LEVEL := -g
EXTRA_CFLAGS := -Wall
CXXFLAGS := $(DEBUG_LEVEL) $(EXTRA_CCFLAGS)
CFLAGS := $(CXXFLAGS)

INC_DIR := include
SRC_DIR := src

SRCS := $(wildcard $(SRC_DIR)/*.c)


$(TARGET_EXEC): 
	$(CC) -o $(TARGET_EXEC) $(SRCS) -I $(INC_DIR) $(CFLAGS)

.PHONY: run
run: $(TARGET_EXEC) test 
	$(TARGET_EXEC) tests/cp1252.csv 


.PHONY: clean
clean:
	-rm $(TARGET_EXEC)


.PHONY: test 
test:
	mkdir -p tests


