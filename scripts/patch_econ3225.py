import os, glob

base = r"D:\Dropbox\Apps\Overleaf\ECON 3225 Slides"
tex_files = sorted(glob.glob(os.path.join(base, "*.tex")))

for tex_path in tex_files:
    with open(tex_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    original = content
    content = content.replace("\\usepackage[latin9]{inputenc}", "\\usepackage[utf8]{inputenc}")
    content = content.replace("\\usepackage{bbm}", "\\newcommand{\\mathbbm}[1]{\\mathbb{#1}}")

    if content != original:
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Patched: {os.path.basename(tex_path)}")
    else:
        print(f"No change: {os.path.basename(tex_path)}")

print("\nDone.")
