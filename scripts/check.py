import nbformat
import numpy as np


def get_tagged_cell(notebook_path, tag):
    nb = nbformat.read(notebook_path, as_version=4)

    for cell in nb.cells:
        if tag in cell.metadata.get("tags", []):
            return cell.source

    raise ValueError(f"Geen cel gevonden met tag {tag!r}")


source = get_tagged_cell("opdracht.ipynb", "sol_check_1")

namespace = {}
exec(source, namespace)

functie = namespace["som"]

array1 = np.array([-5, 0, 5])
array2 = np.array([-3, 4, 2])

resultaat = functie(array1, array2)

np.testing.assert_array_equal(
    resultaat,
    np.array([-8, 4, 7])
)