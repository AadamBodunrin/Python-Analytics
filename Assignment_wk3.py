"""Practice using the requests library by visiting https://en.wikipedia.org/wiki/main_page and searching for the string "Did you know" on that page. You need to do the following steps:
1. Open https://en.wikipedia.org/wiki/main_page using the requests library
2. Check the status code. Did your request work?
3. Get the content. Decode it. Then search the page for the string “Did you know” using the str find function
4. If your find function returned a positive number - Great!
5. If it returned -1 (that means it was not found), you’ve done something wrong. Try figuring out what went wrong """


"""import requests as req     #Use Request Library 
wiki = req.get("https://en.wikipedia.org/wiki/main_page")  #Label the url
print(type(wiki)) #Find the class type
print(wiki.status_code) #Check if the command was suucessful
print(wiki.content.decode("utf-8")) #Print the content"""

#Option 1
def find(url, word):
	import requests as req
	page = req.get(url)
	pagecode = page.content.decode("utf-8")
	return pagecode.find(word)

print(find(url = "https://en.wikipedia.org/wiki/main_page", word = "Did you know"))

#Option 2
def find2(url, word):
	import requests as req
	page = req.get(url)
	if page.status_code == 200:
		pagecode = page.content.decode("utf-8")
		return pagecode.find(word)
	else:
		return "Your action wasn't successful, check the url again"

print(find2(url = "https://en.wikipedia.org/wiki/main_page", word = "Did you know"))
