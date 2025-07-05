import sys
import subprocess

PASS = 0
FAIL = 1

def main() -> int:
    """Run `xmake format` on the project"""
    exit_code = FAIL
    try:
        result = subprocess.run(["xmake", "format"], stdout=subprocess.PIPE,
                                text=True)
        if "format ok!" in result.stdout:
            exit_code = PASS
    except Exception:
        exit_code = FAIL

    return exit_code

if __name__ == "__main__":
    raise SystemExit(main())
