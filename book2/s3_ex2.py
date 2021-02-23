fname = input("Enter file name: ")
fh = open(fname)
cont = total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    num = float(line[line.find(":") + 2 :])
    total = total + num
    cont = cont + 1

print('Average spam confidence:', total/cont)