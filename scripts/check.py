from pathlib import Path
import html
import numpy as np

results = []


def check(name, func):
    try:
        func()
        results.append((name, True, ""))
        print(f"PASS: {name}")
    except Exception as exc:
        results.append((name, False, str(exc)))
        print(f"FAIL: {name}: {exc}")

array1 = np.array([-5, 0, 5])
array2 = np.array([-3, 4, 2])

# Voorbeeld
def check_sol_1(array1 , array2):
  
    # hier jouw bestaande controle
    assert result.tolist() == [-8, 4, 7]


check("sol_check_1", check_sol_1)


# HTML genereren
output = Path("_checks/checks.html")
output.parent.mkdir(parents=True, exist_ok=True)

rows = []

for name, passed, message in results:
    status = "✅ PASS" if passed else "❌ FAIL"

    rows.append(f"""
        <tr>
            <td>{html.escape(name)}</td>
            <td>{status}</td>
            <td>{html.escape(message)}</td>
        </tr>
    """)

output.write_text(
    f"""<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="utf-8">
    <title>Notebook checks</title>
    <style>
        body {{
            font-family: system-ui, sans-serif;
            max-width: 1000px;
            margin: 40px auto;
            padding: 0 20px;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
        }}
        th, td {{
            text-align: left;
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }}
    </style>
</head>
<body>
    <h1>Notebook checks</h1>
    <table>
        <thead>
            <tr>
                <th>Check</th>
                <th>Status</th>
                <th>Details</th>
            </tr>
        </thead>
        <tbody>
            {''.join(rows)}
        </tbody>
    </table>
</body>
</html>
""",
    encoding="utf-8",
)