"""
In this assignment, you will write a function named reverse(sentence, reverse_word) that takes two strings as an input and returns a new string where the first occurrence of replace_word has been reverted (i.e. spelled backwards).
For example- 
reverse("Python improves my mood very much", "mood") should return "Python improves my doom very much"

"""
#Option 1

def count_overlapping_substrings(haystack, needle):
    count = 0
    i = -1
    while True:
        i = haystack.find(needle, i+1)
        if i == -1:
            return count
        count += 1

def reverse(sentence, reverse_word):
	count = count_overlapping_substrings(sentence, reverse_word)
	for i in range(count):
		sentence = sentence[0:sentence.find(reverse_word)] + reverse_word[::-1] \
		+  sentence[sentence.find(reverse_word)+len(reverse_word):]
	transformed_string = sentence
	return transformed_string

print(reverse("Python improves my mood very much.", "mood"))


#option 2
def reverse2(sentence, reverse_word):
	return sentence.replace(reverse_word, reverse_word[::-1])

print(reverse2("Python improves my mood very much.", "mood"))


#option 3
def reverse3(sentence, reverse_word):
	if reverse_word in sentence:
		return sentence.replace(reverse_word, reverse_word[::-1])
	else:
		return ("The item you highlighted is not in the sentence.")
		
print(reverse3("Python programming is great for Data Science, Web development and buidling games.", "mood"))

