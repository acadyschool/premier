CC = gcc
CFLAGS = -std=c99 -Wall -Wextra -Werror -fPIC
LDFLAGS = -Wl,-rpath,./lib -L./lib
RM = rm -f
SHARED = -shared
INCLUDE = --include
SRC = src
OBJ = obj
INC = include
LIB = lib

EXEC = main
MY_TRACK = $(SRC)/myTrack.c
LIB_MYTRACK = $(LIB)/libmyTrack.so
INCLUDE_MYTRACK_H = include/myTrack.h
L_MYTRACK = -lmyTrack
FICHIER_TEST = $(SRC)/main.c
.PHONY: all clean distclean

all: $(LIB_MYTRACK) $(EXEC)


$(OBJ)/mytrack.o: $(SRC)/myTrack.c | $(OBJ)
	$(CC) -c $< $(CFLAGS) -o $@


$(LIB_MYTRACK): $(OBJ)/mytrack.o | $(LIB)
	$(CC) $(CFLAGS) $(SHARED) $< -o $@

$(OBJ)/main.o: $(FICHIER_TEST) $(INCLUDE_MYTRACK_H) | $(OBJ)
	$(CC) $(INCLUDE) $(INCLUDE_MYTRACK_H) -c $< -o $@


$(EXEC): $(OBJ)/main.o $(LIB_MYTRACK)
	$(CC) $(LDFLAGS) $< $(L_MYTRACK) -o $@



clean:
	$(RM) $(OBJ)/*.o

distclean: clean
	$(RM) $(LIB_MYTRACK) $(EXEC)
