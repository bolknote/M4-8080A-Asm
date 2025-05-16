# i8080A Assembler in m4

This project is an assembler for the Intel 8080A processor, implemented entirely in **m4**. It translates a simplified assembly language into machine code suitable for execution on the 8080A or its Soviet analogs (such as those used in the Radio-86RK computer).

## Features

* Full support for the i8080A instruction set.

## Syntax

Some key differences from traditional assemblers:

* All numbers must be specified in hexadecimal with the `h` prefix (e.g., `hFF`).
* The start address is specified with `ORG(address)`.
* Labels are declared with `LABEL(name)`, and their addresses are obtained via `ADDR(name)`.
* Arbitrary byte sequences are inserted using `BYTE(...)`.
* Comments are added using the `COM(...)` construct.

### Example

```asm
ORG(h1100)
COM(This program prints "HELLO WORLD")
LXI H, ADDR(TEXT)
CALL hF818
JMP hF86C

LABEL(TEXT)
BYTE(h48, h45, h4C, h4C, h4F, h20, h57, h4F, h52, h4C, h44, hD, hA, h0)
```

## How to Use

To assemble a program, use the provided `asm` script:

* **Generate a binary file:**

  ```
  asm helloworld.m4 helloworld.bin
  ```

  This command generates a binary file from the source.

* **Output codes in human-readable form:**

  ```
  asm helloworld.m4 /dev/stdout
  ```

  This command prints the machine code to the console.

## Requirements

* **m4** macro processor
* **Python 3** (for code generation scripts)
