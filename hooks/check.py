import sys
import subprocess

PASS = 0
FAIL = 1

def main() -> int:
    """Run `xmake check` on the project"""
    checkers = sys.argv[1:]
    if len(checkers) == 0:
        print("must provide at least one checker to `xmake check`")
        return FAIL

    exit_code = PASS
    for checker in checkers:
        try:
            result = subprocess.run(["xmake", "check", checker], stdout=subprocess.PIPE,
                                    text=True)
            if "error" not in result.stdout:
                exit_code = PASS
        except Exception:
            exit_code |= FAIL

    return exit_code

if __name__ == "__main__":
    raise SystemExit(main())
