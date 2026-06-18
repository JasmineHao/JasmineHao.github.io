import os, re, glob

src_base = r"D:\Github\Project-Metis\IndustrialOrganization\2021-2022\Slides"
tex_files = glob.glob(os.path.join(src_base, "**", "*.tex"), recursive=True)

fixed_count = 0

for tex_path in tex_files:
    with open(tex_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    original = content

    # Fix frametitle fallback: empty third argument of \IfFontExistsTF{Minion Pro} -> use Segoe UI
    content = re.sub(
        r"(\\setbeamerfont\{frametitle\}\{family=\{\\fontspec\{Minion Pro\}\}, size=\\LARGE,series=\\bfseries\} %series=\\bfseries\s+% font title\s+%Georgia)(\s*\n\s*\}\s*\{)\s*(\})",
        r"\1\2 \\setbeamerfont{frametitle}{family={\\fontspec{Segoe UI}}, size=\\LARGE,series=\\bfseries} \3",
        content,
        flags=re.DOTALL,
    )

    if content != original:
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed: {os.path.relpath(tex_path, src_base)}")
        fixed_count += 1

print(f"\nTotal fixed: {fixed_count}")
