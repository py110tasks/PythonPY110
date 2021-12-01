import re

lines = [
    '1 + 10 = 11',
    '20 - 12 = 8',
    '7.5 / 2.5 = 3',
    '3 * 0.5 = 1.5',
    '0.05 + 6 = 6.05',
    '0.5 * 8 = 16'
]

pt = re.compile(r'([\d\.]+)\s*([\*\+\/-])\s*([\d\.]+)\s*=\s*([\d\.]+)')
for line in lines:
    prs = pt.findall(line)
    if not prs or prs == [()]:
        print(line, ': ', False)
        continue
    n1 = float(prs[0][0]) if '.' in prs[0][0] else int(prs[0][0])
    n2 = float(prs[0][2])if '.' in prs[0][2] else int(prs[0][2])
    res = float(prs[0][3]) if '.' in prs[0][3] else int(prs[0][3])
    print(line, ': ', end="")
    if prs[0][1] == '+' and n1 + n2 == res:
        print(True)
    elif prs[0][1] == '-' and n1 - n2 == res:
        print(True)
    elif prs[0][1] == '*' and n1 * n2 == res:
        print(True)
    elif prs[0][1] == '/' and n1 / n2 == res:
        print(True)
    else:
        print(False)
