import os, subprocess, shutil

tectonic = os.path.join(os.getcwd(), "tools", "tectonic.exe")
src_base = r"D:\Dropbox\Apps\Overleaf\ECON 3225 Slides"
dst_base = os.path.join(os.getcwd(), "files", "econ3225", "slides")

slides = [
    ("Lect6_moving_beyond_linearity.tex", "06-moving-beyond-linearity.pdf"),
    ("Lect7_tree_based_method.tex", "07-tree-based-methods.pdf"),
    ("Lect8_support_vector_machine.tex", "08-support-vector-machine.pdf"),
    ("Lect9_deep_learning.tex", "09-deep-learning.pdf"),
]

os.makedirs(dst_base, exist_ok=True)

for tex_name, dst_name in slides:
    tex_path = os.path.join(src_base, tex_name)
    pdf_name = tex_name.replace(".tex", ".pdf")
    src_pdf = os.path.join(src_base, pdf_name)
    dst_pdf = os.path.join(dst_base, dst_name)

    print(f"\n=== Compiling {tex_name} ===")
    log_path = os.path.join(os.getcwd(), "tools", f"tectonic_3225_{dst_name}.log")
    with open(log_path, "w", encoding="utf-8") as logfile:
        result = subprocess.run(
            [tectonic, "-X", "compile", tex_name],
            cwd=src_base,
            stdout=logfile,
            stderr=subprocess.STDOUT,
            encoding="utf-8",
            errors="replace",
        )

    if result.returncode != 0:
        print(f"FAILED: {tex_name} (see {log_path})")
        continue

    if not os.path.exists(src_pdf):
        print(f"PDF not found after compile: {src_pdf}")
        continue

    shutil.copy2(src_pdf, dst_pdf)
    print(f"OK -> {dst_name}")

print("\nAll done.")
