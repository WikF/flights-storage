markdict={"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73}


marklist = sorted(markdict)
#                  .items(), key = lambda x:x[0])
#print(marklist)
l = []
for i in markdict:
    l.append(markdict[i])

sorted_list = sorted(l)
final_list = []
j=0
for i in sorted_list:
    for j in markdict:
        if i==markdict[j]:
            final_list.append((markdict[j], j))

print(final_list)

