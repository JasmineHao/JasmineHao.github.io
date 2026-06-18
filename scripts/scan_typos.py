import os
import re

root = r'D:\Github\Project-Metis\IndustrialOrganization\2021-2022\Slides'

# Common typos to flag
typos = {
    'teh': 'the',
    'adn': 'and',
    'taht': 'that',
    'wiht': 'with',
    'fo r': 'for',
    'ot ': 'to ',
    'si ': 'is ',
    'it s ': 'its ',
    'it\'s ': 'its ',
    'recieve': 'receive',
    'occured': 'occurred',
    'seperate': 'separate',
    'definately': 'definitely',
    'goverment': 'government',
    'occurence': 'occurrence',
    'accomodate': 'accommodate',
    'refered': 'referred',
    'prefered': 'preferred',
    'equilibirum': 'equilibrium',
    'monopolistic': 'monopolistic', # check spelling
    'compeition': 'competition',
    'comapny': 'company',
    'stratgy': 'strategy',
    'differenciate': 'differentiate',
    'diffrent': 'different',
    'product differentiation': 'product differentiation',
    'Bertrand': 'Bertrand',
    'Cournot': 'Cournot',
    'Stackelberg': 'Stackelberg',
    'oligopol': 'oligopoly',
    'asymetric': 'asymmetric',
    'symetric': 'symmetric',
    'comparision': 'comparison',
    'substitue': 'substitute',
    'substitues': 'substitutes',
    'elasticiy': 'elasticity',
    'elasticities': 'elasticities',
    'margnial': 'marginal',
    'optmization': 'optimization',
    'maxmize': 'maximize',
    'minmize': 'minimize',
    'proffit': 'profit',
    'profts': 'profits',
    'quantitiy': 'quantity',
    'quantites': 'quantities',
    'welfaree': 'welfare',
    'consumer surplus': 'consumer surplus',
    'producer surplus': 'producer surplus',
    'deadweight loss': 'deadweight loss',
    'entry deterrence': 'entry deterrence',
    'predatory pricing': 'predatory pricing',
    'price discrimination': 'price discrimination',
    'vertical integration': 'vertical integration',
    'market power': 'market power',
    'barriers to entry': 'barriers to entry',
    'first order condition': 'first-order condition',
    'first-order condition': 'first-order condition',
    'second order condition': 'second-order condition',
    'second-order condition': 'second-order condition',
}

# We want to find misspellings, so map bad -> good
misspellings = {
    'teh': 'the',
    'adn': 'and',
    'taht': 'that',
    'wiht': 'with',
    'recieve': 'receive',
    'occured': 'occurred',
    'seperate': 'separate',
    'definately': 'definitely',
    'goverment': 'government',
    'occurence': 'occurrence',
    'accomodate': 'accommodate',
    'refered': 'referred',
    'prefered': 'preferred',
    'equilibirum': 'equilibrium',
    'compeition': 'competition',
    'comapny': 'company',
    'stratgy': 'strategy',
    'diffrent': 'different',
    'oligopol ': 'oligopoly ',
    'asymetric': 'asymmetric',
    'symetric': 'symmetric',
    'comparision': 'comparison',
    'substitue ': 'substitute ',
    'substitues': 'substitutes',
    'elasticiy': 'elasticity',
    'margnial': 'marginal',
    'optmization': 'optimization',
    'maxmize': 'maximize',
    'minmize': 'minimize',
    'proffit': 'profit',
    'profts': 'profits',
    'quantitiy': 'quantity',
    'quantites': 'quantities',
    'welfaree': 'welfare',
}

# Extract text-ish lines from tex
findings = []
for dirpath, dirnames, filenames in os.walk(root):
    for fname in filenames:
        if fname.endswith('.tex'):
            path = os.path.join(dirpath, fname)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            for i, line in enumerate(lines, 1):
                # Skip pure command lines
                stripped = line.strip()
                if not stripped or stripped.startswith('%'):
                    continue
                # Check for misspellings
                for bad, good in misspellings.items():
                    if re.search(r'\b' + re.escape(bad) + r'\b', line, re.IGNORECASE):
                        findings.append((path, i, line.strip(), bad, good))

if findings:
    print('Potential typos found:')
    for path, line_no, text, bad, good in findings:
        rel = os.path.relpath(path, root)
        print(f'{rel}:{line_no}  [{bad} -> {good}]  {text[:100]}')
else:
    print('No common misspellings found in slide .tex files.')
