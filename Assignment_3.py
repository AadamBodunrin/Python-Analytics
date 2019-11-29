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


def find(url, word):
	import requests as req
	page = req.get(url)
	pagecode = page.content.decode("utf-8")
	return pagecode.find(word)

print(find(url = "https://en.wikipedia.org/wiki/main_page", word = "Did you know"))
