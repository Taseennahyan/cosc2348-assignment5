import subprocess
import pytest

def run_calculator(*args):
    result = subprocess.run(
        ["./calculator"] + list(args),
        capture_output=True,
        text=True
    )
    return result.stdout.strip(), result.returncode

def test_addition():
    """Test that the calculator correctly adds two numbers."""
    stdout, returncode = run_calculator("+", "3", "4")
    assert returncode == 0, "Calculator exited with non-zero return code"
    assert "7" in stdout, f"Expected '7' in output, got: '{stdout}'"

def test_subtraction():
    """Test that the calculator correctly subtracts two numbers."""
    stdout, returncode = run_calculator("-", "10", "3")
    assert returncode == 0, "Calculator exited with non-zero return code"
    assert "7" in stdout, f"Expected '7' in output, got: '{stdout}'"
