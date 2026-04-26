import contextlib
import io
from pathlib import Path

import matplotlib
import nbformat


matplotlib.use("Agg")


def main() -> None:
    notebook_path = Path("HW01.ipynb")
    nb = nbformat.read(notebook_path, as_version=4)

    shared_globals = {"__name__": "__main__"}

    for idx, cell in enumerate(nb.cells, start=1):
        if cell.cell_type != "code":
            continue

        print(f"\n=== Executing code cell {idx} ===")
        buffer = io.StringIO()
        try:
            with contextlib.redirect_stdout(buffer), contextlib.redirect_stderr(buffer):
                exec(cell.source, shared_globals)
        except Exception:
            output = buffer.getvalue()
            if output:
                print(output.rstrip())
            raise

        output = buffer.getvalue()
        if output:
            print(output.rstrip())

    print("\nHW01.ipynb executed successfully.")


if __name__ == "__main__":
    main()
