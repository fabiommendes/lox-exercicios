import sys
from pathlib import Path

def main():
    from lox import run_source
    run_source(Path(sys.argv[1]).read_text())