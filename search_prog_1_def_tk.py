from tkinter import *
import re
# import sys
import group_info_1 as data

# all the groups and words are imported from group_info_1.py
# make content groups from back cover text (takzir) with tkinter gui
# write txt file

# run the program in idle or pycharm etc
# part 1 - user input


def user_input_tk():
    # input from human user with tk, return text, book_name, category

    category_l = []
    space = " "
    n_line = " \n "
    textim = []
    book_name = book_entry.get()
    category = category_entry.get()
    category_l.append(category)
    text = text_entry.get(1.0, END)
    textim.append(text)
    # print(text)
    # print(textim)
    # printer = str(book_name + space + category_l + n_line + text)

    # output.insert(END,  printer)
    text_results = where_to_run(textim, category_l)
    write_file_2(text_results)
    # print(text_results)
    # print(book_name, category_l, textim, text_results)

    return book_name, category_l, textim, text_results


def clean():
    output.delete(0.0, END)
    text_entry.delete(0.0, END)
    category_entry.delete(0, 'end')
    book_entry.delete(0, 'end')


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
                # print (groupi, data.all_groups_str.index(cat))
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
                        # print(group_to_print, ": ", k_search.group(), " - ", key)

                        text_result.append(group_to_print)
                        text_result.append(k_search.group())
                        text_result.append(key)
                        text_result.append(sign)

                    for valey in val:
                        val_search = re.search(rf"{valey}", line)
                        if val_search:
                            # print(group_to_print, ": ", val_search.group(), " - ", key)

                            text_result.append(group_to_print)
                            text_result.append(val_search.group())
                            text_result.append(key)
                            text_result.append(sign)
    write_file_2(text_result)
    return text_result

# part 3 - write results to txt file


def write_file(text, category, book_name):
    # basic info - this version ignore this
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
    # output words to screen
    f = open("info2.txt", "a")

    for found in final_results:
        f.write(found)
        f.write(" ")
        strings = " "
        strings += str(found)
        output.insert(END, strings)
    f.write("\n")
    f.close()

# tkinter gui


window = Tk()
window.title("חפש קבוצות")
label_1 = Label(window, text="שם ספר") .grid(row=0, column=0)
book_entry = Entry(window)
book_entry.grid(row=1, column=0)
label_2 = Label(window, text="קטגוריה") .grid(row=2, column=0)
category_entry = Entry(window)
category_entry.grid(row=3, column=0)
label_3 = Label(window, text="תקציר") .grid(row=4, column=0)
text_entry = Text(window, bg="light gray")
text_entry.grid(row=5, column=0)
button_1 = Button(window, text="חפש", command=user_input_tk) .grid(row=6, column=0)
button_2 = Button(window, text="נקה", command=clean) .grid(row=7, column=0)
output = Text(window, wrap=WORD,  bg="light grey")
output.grid(row=9, column=0)
window.mainloop()
# width=50,
