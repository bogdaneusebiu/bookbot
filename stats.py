def get_num_words(book):
    words = book.split()
    sum = 0
    for word in words:
        sum += 1
    return sum

def get_letter_freq(book):
    book = book.lower()
    freventa={}
    words = book.split()
    for word in words:
        for i in range(0, len(word)):
            if word[i] in freventa:
                freventa[word[i]] += 1
            else: 
                freventa[word[i]] = 1
    return freventa

def sort_on(item):
    return item["num"]

def make_output(char):
    words_list=[]
    for x, y in char.items():
        words_list.append({"name": x, "num": y})

    words_list.sort(reverse=True, key=sort_on)    
    return words_list

