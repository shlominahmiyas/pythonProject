from tkinter import *
import re
import group_info_1 as data
# pip install this packages:
import requests
from bs4 import BeautifulSoup

# all the groups and words are imported from group_info_1.py
# make content groups from back cover text (takzir) with tkinter gui
# search in goodreads for genres
# write txt file

# run the program in idle or pycharm etc
# part 1 - user input


def user_input_tk():
    # input from human user with tk, return text, book_name, category
    # calls functions write_file and where_to_run

    category_l = []
    textim = []
    book_name = book_entry.get()
    category = category_entry.get()
    category_l.append(category)
    if category_l[0] == "*":
        for star in data.all_groups_str:
            category_l.append(star)

    text = text_entry.get(1.0, END)
    textim.append(text)

    write_file(book_name, category_l, textim)
    text_results = where_to_run(textim, category_l)

    return book_name, category_l, textim, text_results


def user_input_g():
    # input for searching GENRES in goodreads website
    # robert w. chambers
    # the king in yellow
    book_en = book_en_entry.get()
    # author_en = author_en_entry.get()
    goodreads_list = goodreads(book_en)
    write_file_3(goodreads_list)
    return goodreads_list


def clean():
    output.delete(0.0, END)
    text_entry.delete(0.0, END)
    category_entry.delete(0, 'end')
    book_entry.delete(0, 'end')
    book_en_entry.delete(0, 'end')


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
    # for info2.txt
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

# part 3 goodreads


def goodreads (book_e):
 site = "https://www.goodreads.com/"
 search = "https://www.goodreads.com/search?q="
 # aut_e = aut_e.lower()
 book_e= book_e.lower()
# input_aut_li = aut_e.split()
 input_book_li = book_e.split()
 string = ""
 for wb in input_book_li:
    string += "+" + wb

 url = search+string

 l = requests.get(url)
 soup = BeautifulSoup(l.text, 'html5lib')

 lista = []

 for link in soup.select('.bookTitle'):

    link_book=link.text
    small_book_name = link_book.lower()
    small_book_name=small_book_name.strip()

    if small_book_name == book_e:
     lista.append(small_book_name)

     hrefs = link.get('href')

     new_url = site + hrefs
     ln = requests.get(new_url)
     soup2 = BeautifulSoup(ln.text, 'html5lib')



     for authors in soup2.select('.authorName'):
       au = authors.text
       lista.append(au)
     lista.append(new_url)

     for genre in soup2.select('.elementList'):

          g= genre.text
          g = re.sub(' +', ' ', g)

          lista.append(g.replace("\n", " "))

 return lista


# part 4 - write results to txt file


def write_file(book_name, category, text):
    # basic info -
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
    strings = " "
    if len(final_results) == 0:
        output.insert(END, "לא מצאתי :( \n")

    for found in final_results:
        f.write(found)
        f.write(" ")

        to_print = strings + str(found)
        output.insert(END, to_print)

    f.write("\n")
    f.close()


def write_file_3(final_goodreads):
    # the GENRES who where found in goodreads
    # output GENRES to screen
    f = open("info2.txt", "a")
    strings = " "
    line="\n"
    if len(final_goodreads) == 0:
        output.insert(END, "לא מצאתי :( \n")

    for found in final_goodreads:
        f.write(found)
        f.write("\n")

        to_print = strings + str(found) + line
        output.insert(END, to_print)

    f.write("\n")
    f.close()


# tkinter gui


window = Tk()
window.title("חפש קבוצות")
label_1 = Label(window, text="שם ספר") .grid(row=0, column=1, sticky=E)
book_entry = Entry(window)
book_entry.grid(row=0, column=0, sticky=E)
label_2 = Label(window, text="קטגוריה") .grid(row=1, column=1, sticky=E)
category_entry = Entry(window)
category_entry.grid(row=1, column=0, sticky=E)
label_3 = Label(window, text="תקציר") .grid(row=4, column=1, sticky=E)
text_entry = Text(window, height=14, bg="light gray")
text_entry.grid(row=4, column=0, sticky=E)
button_1 = Button(window, text="חפש", command=user_input_tk) .grid(row=5, column=0,  sticky=E)
button_2 = Button(window, text="נקה", command=clean) .grid(row=7, column=0, sticky=E)
label_4 = Label(window, text="תוצאות") .grid(row=8, column=1, sticky=E)
output = Text(window,  height=18,  bg="light grey")
output.grid(row=8, column=0, sticky=E)
label_5 = Label(window, text="book") .grid(row=2, column=1,  sticky=E)
book_en_entry = Entry(window)
book_en_entry.grid(row=2, column=0, sticky=E)
button_3 = Button(window, text="goodreads", command=user_input_g) .grid(row=6, column=0,  sticky=E)


window.mainloop()
# width=50, padx=7, wrap=WORD,
