import subprocess

def run_calculator(*args):
    result = subprocess.run(
        ["./calculator"] + list(args),
        capture_output=True,
        text=True
    )
    return result.stdout.strip(), result.returncode

def test_addition():
    stdout, returncode = run_calculator("+", "3", "4")
    assert returncode == 0
    assert "7" in stdout
    print("TEST RUN: test_addition passed")

def test_subtraction():
    stdout, returncode = run_calculator("-", "10", "3")
    assert returncode == 0
    assert "7" in stdout
    print("TEST RUN: test_subtraction passed")

if __name__ == "__main__":
    test_addition()
    test_subtraction()
    print("All tests passed!")
