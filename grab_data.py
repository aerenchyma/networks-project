from bs4 import BeautifulSoup as bsoup 
import requests

# open html document with categories of featured articles (saved directly from Wikipedia as of 4/4/2014)
cat_f = open("categories_ptag_featwikiarticles.html","r").read() # p tag subset of feat articles page with category id links, manually extracted
sourcepg = open("featured-articles.html","r").read() # full html source of featured articles page

soup = bsoup(cat_f) #bsoup version of the categories file
sp = bsoup(sourcepg) #bsoup version of the whole featured articles source page
#print sp.prettify()

# creates the dictionary with categories as keys and lists of wiki in-category links as values
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

# iterates through the dictionary and writes external links from categories to files named by category
# TODO combine with other loop (this bit takes a VERY long time to run as is)
for k in d:
	f = open("linkfiles/{}.txt".format(k),"w") # originally ran with plain filename, adding path in case we run this again for proper overwriting
	for url in d[k]:
		#f.write("{}\n".format(url))
		resp = requests.get(url).text
		resp_soup = bsoup(resp)
		ext_links = resp_soup.findAll('a',{'class':'external text'})
		for l in ext_links:
			f.write("{}\n".format(l['href'].encode('utf-8')))
f.close()
