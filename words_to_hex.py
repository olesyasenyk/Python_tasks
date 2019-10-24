'''Convert the words that make up a string into hexadecimal values that will be read as colour values.
A word is defined as a sequence of ASCII characters between two white spaces or the first or last word.
Each word will represent a hexadecimal value by taking the first three letters of each word 
and find the ASCII character code for each character. 
This will then give you one hexadecimal value that represents the colours red, green or blue. 
You will then combine these values into one readable RGB hexadecimal value, ie, #ffffff.
If your word consists of less than 3 letters, you should use the hexidecimal value '00', 
ie "It" would return a value #497400.
Your answer should be an array of hexadecimal values that correspond to each word 
that made up your original string.
Example:
"Hello, my name is Gary and I like cheese."
['#48656c', '#6d7900', '#6e616d','#697300','#476172','#616e64','#490000','#6c696b','#636865']'''

def wordsToHex (words):
    li = words.split()
    colors=['#'+ '{0:x}'.format(ord(e[0])) + '{0:x}'.format(ord(e[1])) + '{0:x}'.format(ord(e[2])) 
    if len(e)>=3 else '#'+ '{0:x}'.format(ord(e[0])) + '{0:x}'.format(ord(e[1])) + '00' for e in li]
    return colors
print (wordsToHex('hello to baby'))
