import os, shutil
from PyPDF2 import PdfMerger

src_base_2022 = r"D:\Github\Project-Metis\IndustrialOrganization\2021-2022"
src_base_2023 = r"D:\Github\Project-Metis\IndustrialOrganization\2022-2023"
dst_base = os.path.join(os.getcwd(), "files", "io", "slides")

slides_2022 = [
    ("Slides\\1 Market Power\\1 Intro.pdf", "2022/_01-market-power-intro.pdf"),
    ("Slides\\1 Market Power\\Berry Gaynor and Morton 2019.pdf", "2022/_02-berry-gaynor-morton.pdf"),
    ("Slides\\2 Competition\\2 Competition.pdf", "2022/_03-competition.pdf"),
    ("Slides\\2 Competition\\2 Firms.pdf", "2022/_04-firms.pdf"),
    ("Slides\\3 Differentiated Product\\3 Differentiation.pdf", "2022/_05-differentiation.pdf"),
    ("Slides\\3 Differentiated Product\\3 Logit and extension.pdf", "2022/_06-logit-and-extension.pdf"),
    ("Slides\\4 Advertising\\4 Advertising.pdf", "2022/_07-advertising.pdf"),
    ("Slides\\5 Price Discrimination\\5 Price Discrimination.pdf", "2022/_08-price-discrimination.pdf"),
    ("Slides\\6 Asymmetric Information\\6 Asymmetric Information.pdf", "2022/_09-asymmetric-information.pdf"),
    ("Slides\\7 Collusion\\7 IntroCompetitionPolicy.pdf", "2022/_10-competition-policy-intro.pdf"),
    ("Slides\\7 Collusion\\7 Collusion.pdf", "2022/_11-collusion.pdf"),
    ("Slides\\7 Collusion\\7 Antitrust\\7 Antitrust.pdf", "2022/_12-antitrust.pdf"),
    ("Slides\\8 Mergers and MP Firms\\8 Mergers.pdf", "2022/_13-mergers.pdf"),
    ("Slides\\9 Entry\\9 Entry.pdf", "2022/_14-entry.pdf"),
    ("Slides\\10 Vertical Market\\10_vertical_market.pdf", "2022/_15-vertical-market.pdf"),
]

slides_2023 = [
    ("Slides\\Lec1_Introduction_Firms.pdf", "2023/01-introduction-firms.pdf"),
    ("Slides\\Lec2_Competition.pdf", "2023/02-competition.pdf"),
    ("Slides\\Lec3_Cartel.pdf", "2023/03-cartel.pdf"),
    ("Slides\\Lec4_Oligopoly.pdf", "2023/04-oligopoly.pdf"),
    ("Slides\\Lec5_Structure_Performance.pdf", "2023/05-structure-performance.pdf"),
    ("Slides\\Lec6_Price_Discrimination.pdf", "2023/06-price-discrimination.pdf"),
    ("Slides\\Lec7_Strategic_Behavior.pdf", "2023/07-strategic-behavior.pdf"),
    ("Slides\\Lec8_Vertical_Integration_Restrictions.pdf", "2023/08-vertical-integration-restrictions.pdf"),
    ("Slides\\Lec9_Information_Advertising_Disclosure.pdf", "2023/09-information-advertising-disclosure.pdf"),
    ("Slides\\Lec10_Durability.pdf", "2023/10-durability.pdf"),
    ("Slides\\Lec11_Patents_Technological_Change.pdf", "2023/11-patents-technological-change.pdf"),
    ("Slides\\Lec12_GovernmentPolicy.pdf", "2023/12-government-policy.pdf"),
]

def copy_slides(slides, src_base):
    for src_rel, dst_rel in slides:
        src = os.path.join(src_base, src_rel)
        dst = os.path.join(dst_base, dst_rel)
        if not os.path.exists(src):
            print(f"Missing: {src}")
            continue
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        print(f"Copied: {src_rel} -> {dst_rel}")

def merge_2022():
    src_dir = os.path.join(dst_base, "2022")
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
    for out_name, inputs in merges:
        merger = PdfMerger()
        for inp in inputs:
            path = os.path.join(src_dir, inp)
            if not os.path.exists(path):
                print(f"Missing for merge: {path}")
                continue
            merger.append(path)
        out_path = os.path.join(src_dir, out_name)
        merger.write(out_path)
        merger.close()
        print(f"Merged: {out_name}")
    for f in os.listdir(src_dir):
        if f.startswith("_") and f.endswith(".pdf"):
            os.remove(os.path.join(src_dir, f))
            print(f"Removed temp: {f}")

print("=== 2022 Spring ===")
copy_slides(slides_2022, src_base_2022)
merge_2022()
print("\n=== 2023 Spring ===")
copy_slides(slides_2023, src_base_2023)
print("\nDone.")
