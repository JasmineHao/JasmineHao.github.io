import os
import re

root = r'D:\Github\Project-Metis\IndustrialOrganization\2021-2022\Slides'

replacements = [
    (r'\\setmainfont\{Palatino\}', r'\\setmainfont{Palatino Linotype}'),
    (r'\\setsansfont\{Palatino\}', r'\\setsansfont{Palatino Linotype}'),
    (r'\\setmainfont\{Helvetica\}', r'\\setmainfont{Arial}'),
    (r'\\setsansfont\{Helvetica\}', r'\\setsansfont{Arial}'),
    (r'\\setmonofont\{Courier Std\}', r'\\setmonofont{Courier New}'),
]

count = 0
for dirpath, dirnames, filenames in os.walk(root):
    for fname in filenames:
        if fname.endswith('.tex'):
            path = os.path.join(dirpath, fname)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            original = content
            for pat, repl in replacements:
                content = re.sub(pat, repl, content)
            if content != original:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f'Patched: {path}')
                count += 1

print(f'Done. Patched {count} files.')
