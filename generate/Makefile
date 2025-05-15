.PHONY: all clean

all: asm8080.m4 linker8080.m4

asm8080.m4: generate.py
	./generate.py > ../asm8080.m4

linker8080.m4: generate_linker.py
	./generate_linker.py > ../linker8080.m4

clean:
	rm -f ../asm8080.m4 ../linker8080.m4
