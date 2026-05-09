#!/usr/bin/env python3
from calculator_adapter import run

# Checks that the program outputs "7" for an input of "3 + 4"
assert run("3 + 4").output == "7"
# Checks that the program outputs "7" for an input of "10 - 3"
assert run("10 - 3").output == "7"

print("All tests passed!")
