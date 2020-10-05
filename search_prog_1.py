import re
import sys
import group_info_1 as f

# make content groups from back cover text (takzir)
# all the groups and words are imported from group_info_1.py

# run the program in idle or pycharm etc
# part 1 - user input
'''
input from user ->
the fastest way to run the program is ->
enter
* enter
copy clean takzir
cmd d or ctrl d
watch the results
'''
book_name=input("book name (optional, enter its ok) ->")
print("-------")
category=[]
x=True
while x:
    app=input("choose category - new category in each line, to end list press / or press * to choose all categories ->")
    # remove white space form start, end of input
    app_inp=app.strip()
    category.append(app_inp)
    if app_inp == "/":
        x=False
    if app_inp=="*":
        category=f.all_groups_str
        x=False
print(category)
print("-------")
print("copy clean takzir here - press cmd d or enter and ctrl d (or ctrl z) after ->")

# multi line stuff
text = sys.stdin.readlines()

print("-------")
print(book_name)
print(text)
print("-------")

# part 2 - find words
# choose on what category to run from all_groups list  ->
# then run over the category group (holder) and find words in keys values with re.search()
print()
# len_all_category=len(category)
len_all_groups_str=len(f.all_groups_str)
for groupi in f.all_groups_str:
 for cat in category:
        #print(cat, groupi)
     if cat==groupi:
        print (groupi, f.all_groups_str.index(cat))
        group_to_print=groupi
        tempr=f.all_groups_str.index(cat)
        holder = f.all_groups[tempr]
        # the actual code - finds the words
        len_holder = len(holder)
        for group in range(len_holder):
            for item in holder[group]:
                # print(item)
                for key, val in item.items():
                    for line in text:

                        k_search = re.search(rf"{key}", line)
                        if k_search:
                            print(group_to_print, ": ", k_search.group(), " - ", key)
                            # print(k_search.group()," - ", key)

                        for valey in val:
                            val_search = re.search(rf"{valey}", line)
                            if val_search:
                                print(group_to_print, ": ", val_search.group(), " - ", key)
                                # print(val_search.group(), " - ", key)









