# remove empty list in a list
names = ['ajay', 'rohit', [], 'mayank']
for m in names:
    if len(m) == 0:
        at_ind = names.index(m)
        del names[at_ind]
    else:
        pass
print(names)