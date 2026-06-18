import os, subprocess, shutil

tectonic = os.path.join(os.getcwd(), "tools", "tectonic.exe")
src_base = r"D:\Dropbox\Apps\Overleaf\ECON 6083 Slides"
dst_base = os.path.join(os.getcwd(), "econ6083", "slides", "2023")

slides = [
    ("0_introduction.tex", "00-introduction.pdf"),
    ("1_1_lasso.tex", "01-lasso.pdf"),
    ("1_2_belloni_2014_jep_new.tex", "02-belloni-2014-jep.pdf"),
    ("1_3_hansen_konbor_lasso_iv.tex", "03-hansen-kozbur-lasso-iv.pdf"),
    ("1_4_Lasso_Application.tex", "04-lasso-application.pdf"),
    ("2_1_tree_based_method.tex", "05-tree-based-methods.pdf"),
    ("2_2_hetorogeneous_treatment_tree.tex", "06-heterogeneous-treatment-tree.pdf"),
    ("2_3_narayanan_kalyanam_2020.tex", "07-narayanan-kalyanam-2020.pdf"),
    ("3_0_forest_for_inference.tex", "08-forest-for-inference.pdf"),
    ("3_1_wagner_athey_2018.tex", "09-wager-athey-2018.pdf"),
    ("3_2_athay_tibshirani_wagner_2019.tex", "10-athey-tibshirani-wager-2019.pdf"),
    ("4_1_gentzkow_taddy_kelly_jep.tex", "11-gentzkow-taddy-kelly-jep.pdf"),
    ("4_2_Grimmer_Stewart_2013.tex", "12-grimmer-stewart-2013.pdf"),
    ("5_1_FiniteMixture.tex", "13-finite-mixture.pdf"),
    ("5_2_Clustering.tex", "14-clustering.pdf"),
]

os.makedirs(dst_base, exist_ok=True)

for tex_name, dst_name in slides:
    tex_path = os.path.join(src_base, tex_name)
    pdf_name = tex_name.replace(".tex", ".pdf")
    src_pdf = os.path.join(src_base, pdf_name)
    dst_pdf = os.path.join(dst_base, dst_name)

    print(f"\n=== Compiling {tex_name} ===")
    log_path = os.path.join(os.getcwd(), "tools", f"tectonic_2023_{dst_name}.log")
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
