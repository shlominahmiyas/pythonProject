import re
import sys
import group_info_1 as data

# all the groups and words are imported from group_info_1.py
# make content groups from back cover text (takzir)
# write txt file

# run the program in idle or pycharm etc
# part 1 - user input
'''
input from user ->
the fastest way to run the program is ->
enter -> * enter -> copy clean takzir -> cmd d or ctrl d -> watch the results
'''


def user_input():
    # input from human user, return text, book_name, category
    book_name=input("book name (optional, enter its ok) ->")
    category = []
    print("-------")
    flag = True
    while flag:
        app=input("choose category - new category in each line, to end list press / or press * to choose all categories ->")
        # remove white space form start, end of input
        app_inp=app.strip()
        category.append(app_inp)
        if app_inp == "/":
            flag=False
        if app_inp=="*":
            category=data.all_groups_str
            flag=False
    print(category)
    print("-------")
    print("copy clean takzir here - press cmd d or enter and ctrl d (or ctrl z) after ->")

    # multi line stuff
    text = sys.stdin.readlines()

    print("-------")
    print(book_name)
    print(text)
    print("-------")
    return text, book_name, category


print()

# part 2 - find words
# choose on what category to run from all_groups list  ->
# then run over the category group (holder) and find words in keys values with re.search()


def where_to_run(text, category):
    # decide where to run on data.all_groups depending on user category, call search_words method
    final_results=[]
    texti=''
    len_all_groups_str=len(data.all_groups_str)
    for groupi in data.all_groups_str:
        for cat in category:
        #print(cat, groupi)
            if cat==groupi:
                print (groupi, data.all_groups_str.index(cat))
                group_to_print=groupi
                tempr=data.all_groups_str.index(cat)
                holder = data.all_groups[tempr]
                # return holder, group_to_print
                final_results = search_words(text, holder, group_to_print)

    return final_results


def search_words(text, holder, group_to_print):
    # search in text variable, find words from chosen data.all_groups list and dictionary (holder) ->
    # use re.search, take keys values items() as variable to find -> print result and write to a file
    # for info.txt
    text_result = []
    sign = "\n"
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

                        text_result.append(group_to_print)
                        text_result.append(k_search.group())
                        text_result.append(key)
                        text_result.append(sign)

                    for valey in val:
                        val_search = re.search(rf"{valey}", line)
                        if val_search:
                            print(group_to_print, ": ", val_search.group(), " - ", key)

                            text_result.append(group_to_print)
                            text_result.append(val_search.group())
                            text_result.append(key)
                            text_result.append(sign)
    write_file_2(text_result)
    return text_result

# part 3 - write results to txt file


def write_file(text, category, book_name):
    # basic info
    f = open("info2.txt", "a")

    f.write("\n שם הספר: \n")
    f.write(book_name)
    f.write("\n")

    f.write("\n התקציר: \n")
    for lines in text:
      f.write(lines)
    f.write("\n")

    f.write("\n קטגוריות החיפוש: \n")
    for groupa in category:
        f.write(groupa)
        f.write(" ")
    f.write("\n")
    f.write("\n הקבוצות והמילים: \n")
    f.close()


def write_file_2(final_results):
    # the words who where found in text
    f = open("info2.txt", "a")
    for found in final_results:
        f.write(found)
        f.write(" ")
    f.write("\n")
    f.close()


# call functions
n_text, n_book_name, n_category = user_input()
write_file(n_text, n_category, n_book_name)
text_results = where_to_run(n_text, n_category)
write_file_2(text_results)






