import os, subprocess, shutil
from PyPDF2 import PdfMerger

tectonic = os.path.join(os.getcwd(), "tools", "tectonic.exe")
src_base = r"D:\Github\Project-Metis\IndustrialOrganization\2021-2022\Slides"
dst_base = os.path.join(os.getcwd(), "files", "io", "slides", "2022")

tex_files = [
    ("1 Market Power\\1 Intro.tex", "_01-market-power-intro.pdf"),
    ("1 Market Power\\Berry Gaynor and Morton 2019.tex", "_02-berry-gaynor-morton.pdf"),
    ("2 Competition\\2 Competition.tex", "_03-competition.pdf"),
    ("2 Competition\\2 Firms.tex", "_04-firms.pdf"),
    ("3 Differentiated Product\\3 Differentiation.tex", "_05-differentiation.pdf"),
    ("3 Differentiated Product\\3 Logit and extension.tex", "_06-logit-and-extension.pdf"),
    ("4 Advertising\\4 Advertising.tex", "_07-advertising.pdf"),
    ("5 Price Discrimination\\5 Price Discrimination.tex", "_08-price-discrimination.pdf"),
    ("6 Asymmetric Information\\6 Asymmetric Information.tex", "_09-asymmetric-information.pdf"),
    ("7 Collusion\\7 IntroCompetitionPolicy.tex", "_10-competition-policy-intro.pdf"),
    ("7 Collusion\\7 Collusion.tex", "_11-collusion.pdf"),
    ("7 Collusion\\7 Antitrust\\7 Antitrust.tex", "_12-antitrust.pdf"),
    ("8 Mergers and MP Firms\\8 Mergers.tex", "_13-mergers.pdf"),
    ("9 Entry\\9 Entry.tex", "_14-entry.pdf"),
    ("10 Vertical Market\\10_vertical_market.tex", "_15-vertical-market.pdf"),
]

os.makedirs(dst_base, exist_ok=True)

for tex_rel, dst_name in tex_files:
    tex_path = os.path.join(src_base, tex_rel)
    tex_dir = os.path.dirname(tex_path)
    tex_name = os.path.basename(tex_path)
    pdf_name = tex_name.replace(".tex", ".pdf")
    src_pdf = os.path.join(tex_dir, pdf_name)
    dst_pdf = os.path.join(dst_base, dst_name)

    print(f"\n=== Compiling {tex_rel} ===")
    log_path = os.path.join(os.getcwd(), "tools", f"tectonic_{dst_name}.log")
    with open(log_path, "w", encoding="utf-8") as logfile:
        result = subprocess.run(
            [tectonic, "-X", "compile", tex_name],
            cwd=tex_dir,
            stdout=logfile,
            stderr=subprocess.STDOUT,
            encoding="utf-8",
            errors="replace",
        )

    if result.returncode != 0:
        print(f"FAILED: {tex_rel} (see {log_path})")
        continue

    if not os.path.exists(src_pdf):
        print(f"PDF not found after compile: {src_pdf}")
        continue

    shutil.copy2(src_pdf, dst_pdf)
    print(f"OK -> {dst_name}")

# Merge
merges = [
    ("01-market-power.pdf", ["_01-market-power-intro.pdf", "_02-berry-gaynor-morton.pdf"]),
    ("02-competition.pdf", ["_03-competition.pdf", "_04-firms.pdf"]),
    ("03-differentiated-products.pdf", ["_05-differentiation.pdf", "_06-logit-and-extension.pdf"]),
    ("04-advertising.pdf", ["_07-advertising.pdf"]),
    ("05-price-discrimination.pdf", ["_08-price-discrimination.pdf"]),
    ("06-asymmetric-information.pdf", ["_09-asymmetric-information.pdf"]),
    ("07-collusion-and-antitrust.pdf", ["_10-competition-policy-intro.pdf", "_11-collusion.pdf", "_12-antitrust.pdf"]),
    ("08-mergers.pdf", ["_13-mergers.pdf"]),
    ("09-entry.pdf", ["_14-entry.pdf"]),
    ("10-vertical-market.pdf", ["_15-vertical-market.pdf"]),
]

print("\n=== Merging ===")
for out_name, inputs in merges:
    merger = PdfMerger()
    for inp in inputs:
        path = os.path.join(dst_base, inp)
        if not os.path.exists(path):
            print(f"Missing for merge: {path}")
            continue
        merger.append(path)
    out_path = os.path.join(dst_base, out_name)
    merger.write(out_path)
    merger.close()
    print(f"Merged: {out_name}")

for f in os.listdir(dst_base):
    if f.startswith("_") and f.endswith(".pdf"):
        os.remove(os.path.join(dst_base, f))
        print(f"Removed temp: {f}")

print("\nAll done.")
