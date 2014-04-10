from bs4 import BeautifulSoup as bsoup 
import requests

# open html document with categories of featured articles (saved directly from Wikipedia as of 4/4/2014)
cat_f = open("categories_ptag_featwikiarticles.html","r").read() # p tag subset of feat articles page with category id links, manually extracted
sourcepg = open("featured-articles.html","r").read() # full html source of featured articles page

soup = bsoup(cat_f) #bsoup version of the categories file
sp = bsoup(sourcepg) #bsoup version of the whole featured articles source page
#print sp.prettify()

catlinks = soup.findAll('a')
d = {}
i = 0
for c in catlinks:
	idt = c['href'][1:].strip() 
	txt = c.text
	#print idt, txt
	d[idt] = [] # creates empty list for each key
	# get place in full source
	allh3s = sp.findAll('span', {"class":'mw-headline'})
	#print allh3s
	imp_p = allh3s[i].find_next("p")
	#print first_imp_p.prettify()
	categ_wikilinks = imp_p.findAll('a')
	for l in categ_wikilinks: 
		d[idt].append("http://en.wikipedia.org{}".format(l['href']))
	i += 1


for k in d:
	f = open("{}.txt".format(k),"w")
	for url in d[k]:
		#f.write("{}\n".format(url))
		resp = requests.get(url).text
		resp_soup = bsoup(resp)
		ext_links = resp_soup.findAll('a',{'class':'external text'})
		for l in ext_links:
			f.write("{}\n".format(l['href'].encode('utf-8')))
f.close()






## well, this works:
# headers = sp.findAll(text=d.keys()[1])
# print headers

#for k in d:



# for each text of link in p tag (that's a dictionary key)
# AND go to the full html page with the featured source page

# find all h2s and h3s
# if the text in the span inside the h3 or h2 matches the key we're looking articles
# get all the hrefs of the links
# add each of those to en.wikipedia.org and we have the links of all the articles
# for each of those add to the list value of the key in the dictionary
# (save this or write it to a json file) ---- STOP NUMBER ONE

# for each key in the dictionary
# the name of each article is (for each value in the list v) -- v[6:].strip()
# using the name we can find the url

# compose each url in the list
# use requests to grab the source of each url

# for each article, save file whose name is category + "-" + the article name



