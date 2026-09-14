CC ?= cc
CFLAGS ?= -std=c89 -Wall -Wextra -Werror -pedantic

.PHONY: all check check-m0 clean

all: build/test_backend

build/test_backend: tests/test_backend.c src/backend.c include/amistudio/backend.h
	mkdir -p build
	$(CC) $(CFLAGS) -Iinclude -o $@ tests/test_backend.c src/backend.c

check: check-m0 build/test_backend
	./build/test_backend

check-m0:
	python3 scripts/check_m0.py

clean:
	rm -rf build
