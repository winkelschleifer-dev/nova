# Nova

Nova is an experimental programming language designed to be easy to read and understand while keeping a path toward typed, more capable programs. The original idea was: "What if C++, Java and Rust were more human-readable?"

> **Status:** early development. The language design and interpreter are changing quickly.

## Current interpreter

The repository contains `nova.py`, a prototype interpreter written in Python.

At the moment, it can:

- read a `.nova` source file selected in the terminal;
- skip empty lines and comments beginning with `$`;
- parse declarations using `make <type> <name> = <value>`;
- store declared variables together with their declared type and raw value;
- validate the basic syntax of `set` statements;
- print the text following `say`.

The following features are part of the design, but are not fully implemented yet: type conversion and validation, changing values with `set`, variable output and string interpolation, expressions, control flow, functions, lists, and OOP.

## Proposed syntax

```nova
$ A comment

make int x = 1
make str message = "Value of x:"

set x += 1
say message + x
say "Value of x is {x}"
```

## Running the prototype

1. Install Python 3.
2. Run:

```bash
python nova.py
```

3. Enter the name of a Nova source file without its `.nova` extension.

## Goal

Nova aims for a small, consistent syntax that reads naturally:

- `make` declares a variable;
- `set` changes an existing variable;
- `say` writes output;
- `$` starts a comment.

## Contributing

Nova is a personal project in its early stages. Feedback and ideas are welcome, but the syntax and implementation may change without notice.
