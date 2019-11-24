""" write a function named word_distribution that takes a string as an input and returns a dictionary 
containing the frequency of each word in the text. Your function should convert all words to lower case and 
should remove punctuation that occurs at the end of a word. 

For example if the argument to the function is: 
 
text_string = “Hello. How are you? Please say hello if you don’t love me!”

your function should return: {‘hello’: 2, ‘how’:1, ‘are’:1, ‘you’:2, ’please’:1, “don’t”: 1, 'say':1, 'if':1, 'love':1,'me':1} """

def word_distribution(text_string):     #Define the function
    words_list = text_string.split(" ")        #Split the word by space
    words_list = [words_list[i].lower() for i in range(len(words_list))] #Convert each word to lower case
    for i in range(len(words_list)): 
        if not words_list[i].isalpha(): #Check if word is an alphabet
            word = words_list[i]
            for j in word:
                if j != "\'" and j != "’" and not j.isalpha():
                    idx = word.find(j)
                    words_list[i] = word.replace(word[idx],"") #use replace to remove anything that is not an alphabet
                    
    words_dict = {} #Create an empty dictionary
    for word in words_list:
        if word in words_dict: #for every word, add that word and 1  to word_dict
            words_dict[word] += 1
        else:
            words_dict[word] = 1 
    result = words_dict
    return result 

x = "Hello. How are you? Please say hello if you don’t love me!"
print(word_distribution(x))


"""Question Two
__2. Sorting the frequency of Words__

After you finish writing your fucntion, sort the result in descending or asecenind order by the frequency of words.

Your fucntion signature should look like this. It receiveds two arguments - The text to count and the sort order

word_distribution(text_string, "asc")

word_distribution(text_string, "desc")

It should receive the text_string and the sort order.

If the text_string is: "Hello. How are you? Please say hello (John's sister) if you don’t me love me, me!"
And you want to sort the dictinary in asc order

word_distribution(text_string1, "asc") would return something similar to this output. Your structure may be different, but must be sorted by the values of the dictionary and should retunr the entire dictionary sorted.

[("john's", 1),
 ('are', 1),
 ('sister', 1),
 ('don’t', 1),
 ('please', 1),
 ('say', 1),
 ('how', 1),
 ('love', 1),
 ('if', 1),
 ('you', 2),
 ('hello', 2),
 ('me', 3)] """

def word_distribution(text_string, order):     #Define the function
	words_list = text_string.split(" ")        #Split the word by space
	words_list = [words_list[i].lower() for i in range(len(words_list))] #Convert each word to lower case
	for i in range(len(words_list)): 
		if not words_list[i].isalpha():
			word = words_list[i]
			for j in word:
				if j != "\'" and j != "’" and not j.isalpha():
					idx = word.find(j)
					words_list[i] = word.replace(word[idx],"") #use replace to remove anything that is not an alphabet
                    
	words_dict = {} #Create an empty dictionary
	for word in words_list:
		if word in words_dict: #for every word, add that word and 1  to word_dict
			words_dict[word] += 1
		else:
			words_dict[word] = 1 
	result = words_dict

	if order == "asc": #To answer the second command
		x = sorted(result.items(), key = lambda x: x[1]) #Convert the dictionary to a list and use the frequency as the key value for ordering in ascending order
		return (x, dict(x)) #print the list and also show it as a dictionary
	elif order == "desc":
		x = sorted(result.items(), key = lambda x: x[1], reverse = True)  #Convert the dictionary to a list and use the frequency as the key value for ordering in descending order
		return (x, dict(x))
	else:
		return ("Kindly specify an order, either 'asc' or 'desc' ")
	
x = "Hello. How are you? Please say hello (John's sister) if you don’t me love me, me!"
print(word_distribution(x,  "desc"))
