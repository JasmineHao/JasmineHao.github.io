import json

# Read current notebook
with open("option1_dml_401k.ipynb", "r") as f:
    nb = json.load(f)

# Fix cell 3 (data download cell) - change data.copy() to data.data
for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        source = "".join(cell["source"])
        if "fetch_401K" in source:
            # Fix the data loading
            new_source = source.replace(
                "data = fetch_401K()\ndf = data.copy()",
                "data = fetch_401K()\ndf = data.data  # Get DataFrame from DoubleMLData object"
            )
            cell["source"] = [new_source]
            print("Fixed Option 1 data loading")
            break

# Save back
with open("option1_dml_401k.ipynb", "w") as f:
    json.dump(nb, f, indent=2)

print("Option 1 fixed!")
