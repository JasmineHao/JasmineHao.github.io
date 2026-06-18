import os
import subprocess
import sys

root = r'D:\Github\Project-Metis\IndustrialOrganization\2021-2022\Slides'
tectonic = r'D:\GitHub\JasmineHao.github.io\tools\tectonic.exe'
log_dir = r'D:\GitHub\JasmineHao.github.io\tectonic_logs'
os.makedirs(log_dir, exist_ok=True)

results = []
for dirpath, dirnames, filenames in os.walk(root):
    for fname in filenames:
        if fname.endswith('.tex'):
            path = os.path.join(dirpath, fname)
            log_name = fname.replace('.tex', '.log')
            log_path = os.path.join(log_dir, log_name)
            print(f'Compiling: {fname} ...')
            with open(log_path, 'w', encoding='utf-8', errors='replace') as logf:
                result = subprocess.run([tectonic, fname], cwd=dirpath, stdout=logf, stderr=subprocess.STDOUT)
            pdf_name = fname.replace('.tex', '.pdf')
            pdf_path = os.path.join(dirpath, pdf_name)
            success = result.returncode == 0 and os.path.exists(pdf_path)
            results.append((fname, success, result.returncode))
            print(f'  {"OK" if success else "FAILED"} (exit {result.returncode})')

print('\n=== Summary ===')
for fname, success, code in results:
    print(f'{"OK" if success else "FAIL"}: {fname}')
