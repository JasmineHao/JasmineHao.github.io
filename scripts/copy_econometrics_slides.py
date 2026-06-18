import os, shutil

src_base = r"D:\Dropbox\Apps\Overleaf\HKUCourse\Econometrics\CourseTheory"
dst_base = os.path.join(os.getcwd(), "files", "econometrics", "slides")

slides = [
    ("0_introduction.pdf", "00-introduction.pdf"),
    ("0_logistics.pdf", "00-logistics.pdf"),
    ("1_probability.pdf", "01-probability.pdf"),
    ("2_statistics.pdf", "02-statistics.pdf"),
    ("3_addition.pdf", "03-addition.pdf"),
    ("3_matrix.pdf", "03-matrix.pdf"),
    ("3_regression_with_single_regressor.pdf", "03-regression-single-regressor.pdf"),
    ("4_regression_multiple_regressor.pdf", "04-regression-multiple-regressors.pdf"),
    ("5_nonlinear_regression.pdf", "05-nonlinear-regression.pdf"),
    ("6_extermal_validity.pdf", "06-external-validity.pdf"),
    ("7_binary_regression.pdf", "07-binary-regression.pdf"),
    ("8_panel_regression.pdf", "08-panel-regression.pdf"),
    ("9_IV_regression.pdf", "09-iv-regression.pdf"),
]

os.makedirs(dst_base, exist_ok=True)

for src_name, dst_name in slides:
    src = os.path.join(src_base, src_name)
    dst = os.path.join(dst_base, dst_name)
    if not os.path.exists(src):
        print(f"Missing: {src}")
        continue
    shutil.copy2(src, dst)
    print(f"Copied: {src_name} -> {dst_name}")

print("\nDone.")
