import os, re, glob

src_base = r"D:\Github\Project-Metis\IndustrialOrganization\2021-2022\Slides"

tex_files = glob.glob(os.path.join(src_base, "**", "*.tex"), recursive=True)

fixed_count = 0

for tex_path in tex_files:
    with open(tex_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    original = content

    # 1) Fix \setsansfont fallback: in the FiraSans else branch, \setmainfont{...} -> \setsansfont{Segoe UI}
    content = re.sub(
        r"(\\IfFontExistsTF\{FiraSans-Regular\.otf\}\{.*?)(\\setmainfont\{[^}]+\}\s*\})",
        r"\1\\setsansfont{Segoe UI}}",
        content,
        flags=re.DOTALL,
    )

    # 2) Fix frametitle fallback: empty { } after the Minion-Pro frametitle line
    # Match the Minion-Pro frametitle line, then any whitespace/newline, then { }
    content = re.sub(
        r"(\\setbeamerfont\{frametitle\}\{family=\{\\fontspec\{Minion Pro\}\}, size=\\LARGE,series=\\bfseries\} %series=\\bfseries\s+% font title\s+%Georgia)\s*(\{\s*\})",
        r"\1\n\t\t{ \\setbeamerfont{frametitle}{family={\\fontspec{Segoe UI}}, size=\\LARGE,series=\\bfseries} }",
        content,
        flags=re.DOTALL,
    )

    # 3) Standardize \setmainfont fallback in Minion-Pro block (Palatino -> Arial)
    content = re.sub(
        r"(\\IfFontExistsTF\{Minion Pro\}\{.*?\\setmainfont\[Mapping=tex-text\]\{Minion Pro\}.*?% MinionPro-Medium\.otf\s*\n.*?\}\{ )\\setmainfont\{Palatino Linotype\}( \})",
        r"\1\\setmainfont{Arial}\2",
        content,
        flags=re.DOTALL,
    )

    if content != original:
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed: {os.path.relpath(tex_path, src_base)}")
        fixed_count += 1

print(f"\nTotal fixed: {fixed_count}")
