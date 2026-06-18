import os
from PyPDF2 import PdfMerger

src_dir = os.path.join(os.getcwd(), "files", "io", "slides", "2022")

merges = [
    ("01-market-power.pdf", ["01-market-power-intro.pdf", "02-berry-gaynor-morton.pdf"]),
    ("02-competition.pdf", ["03-competition.pdf", "04-firms.pdf"]),
    ("03-differentiated-products.pdf", ["05-differentiation.pdf", "06-logit-and-extension.pdf"]),
    ("04-advertising.pdf", ["07-advertising.pdf"]),
    ("05-price-discrimination.pdf", ["08-price-discrimination.pdf"]),
    ("06-asymmetric-information.pdf", ["09-asymmetric-information.pdf"]),
    ("07-collusion-and-antitrust.pdf", ["10-competition-policy-intro.pdf", "11-collusion.pdf", "12-antitrust.pdf"]),
    ("08-mergers.pdf", ["13-mergers.pdf"]),
    ("09-entry.pdf", ["14-entry.pdf"]),
    ("10-vertical-market.pdf", ["15-vertical-market.pdf"]),
]

for out_name, inputs in merges:
    merger = PdfMerger()
    for inp in inputs:
        path = os.path.join(src_dir, inp)
        if not os.path.exists(path):
            print(f"Missing: {path}")
            continue
        merger.append(path)
    out_path = os.path.join(src_dir, out_name)
    merger.write(out_path)
    merger.close()
    print(f"Merged: {out_name} <- {inputs}")

# Clean up old individual files
old_files = [
    "01-market-power-intro.pdf", "02-berry-gaynor-morton.pdf",
    "03-competition.pdf", "04-firms.pdf",
    "05-differentiation.pdf", "06-logit-and-extension.pdf",
    "07-advertising.pdf", "08-price-discrimination.pdf", "09-asymmetric-information.pdf",
    "10-competition-policy-intro.pdf", "11-collusion.pdf", "12-antitrust.pdf",
    "13-mergers.pdf", "14-entry.pdf", "15-vertical-market.pdf",
]
for f in old_files:
    p = os.path.join(src_dir, f)
    if os.path.exists(p):
        os.remove(p)
        print(f"Removed: {f}")

print("\nDone.")
