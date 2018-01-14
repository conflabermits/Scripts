import urllib

def read_text():
    quotes = open("C:\\local\\temp\\movie_quotes.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity alert!!")
        for word in text_to_check.split():
            connection2 = urllib.urlopen("http://wdylike.appspot.com/?q="+word)
            output2 = connection2.read()
            connection2.close()
            if "true" in output2:
                print(word)
    elif "false" in output:
        print ("This document has no curse words!")
    else:
        print("Could not scan the document properly.")


read_text()
