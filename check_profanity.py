import urllib

def read_text():
    quotes = open("/Users/macbook/Documents/Udacity/Python_foundation/text.txt")
    contents = quotes.read()
    ##print(contents)
    quotes.close()
    print
    check_profanity(contents)
    

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    ##print(output)
    if output == "false":
        print("There is no curse word")
    else:
        print("Watch Out! Curse word is detected!!")
    connection.close()
    

read_text()
