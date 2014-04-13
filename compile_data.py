import os, re
import urlparse

domains = {}
for x in os.listdir("linkfiles"): 
	if x[-4:] == ".txt":
		fj = open('linkfiles/{}.json'.format(x[:-4]),'w')
		catdomains = {}
		f = open(x,"r").readlines() # f is list of url strings
		for l in f:
			fd = urlparse.urlparse(l)
			if fd[1]:
				# currently getting full domain name i.e. books.google.com
				# TODO write code here to get just "google" from that or w/e
				lp = fd[1].strip().lower()
				if lp in domains:
					catdomains[lp] += 1
				else:
					catdomains[lp] = 1
		fj.write(str(catdomains))

