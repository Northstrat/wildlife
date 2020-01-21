import wikipedia
import json

b = {}
with open('birds') as f:
    lines = f.readlines()
    l1 = ""
    l2 = ""
    l3 = ""
    l4 = ""
    cl = 0
    for l in lines:
        print(l2)
        if l.startswith("            "):
            l4 = l.strip()
            cl = 4
        elif l.startswith("        "):
            l3 = l.strip()
            cl = 3
        elif l.startswith("    "):
            l2 = l.strip()
            cl = 2
        else:
            l1 = l.strip()
            cl = 1
        if cl == 4:
            if l1 not in b:
                b[l1] = {}
            if l2 not in b[l1]:
                b[l1][l2] = {}
            if l3 not in b[l1][l2]:
                b[l1][l2][l3] = []
            b[l1][l2][l3] += [{"name":l4}]
    print(b)
        