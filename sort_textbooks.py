def sorter(textbooks):
    textbooks.sort(key=lambda x: x.lower()) #Case In-sensitive
    return(textbooks)

