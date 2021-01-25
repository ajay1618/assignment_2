# program to find all occurences of a given characters in a given string

test_str = "lets_upgrade_ourself"
count = 0
for i in test_str:
    if i == 'e':
        count = count + 1

print ("Count of e in lets_upgrade_ourself is : " + str(count))