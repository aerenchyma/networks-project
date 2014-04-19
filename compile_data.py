import os, re
import urlparse

tpd = open("two_part_domains.txt").readlines()
dms = [x.strip().rstrip() for x in tpd if x != '']
print dms
# just in case we need dict speed lookup... (below, dmsdict)
dmsdict = {}
for domain in dms:
	if domain not in dmsdict:
 		dmsdict[domain] = 0

# #domains = {}
for x in os.listdir("linkfiles"): 
	if x[-4:] == ".txt":
		fj = open('linkfiles/{}-ORIGV.json'.format(x[:-4]),'w')
		catdomains = {}
		f = open(x,"r").readlines() # f is list of url strings
		for l in f:
			fd = urlparse.urlparse(l)
			if fd[1]:
				dm = fd[1].replace("www.","")
				# 
				lp = dm.strip().lower()
				#BELOW IS LOGIC FOR SUBDOMAINS
				# for d in dms:
					
				# 	if lp.endswith(d):
				# 		if len(lp.split(".")) > 4:
				# 			finald = ".".join(lp.split(".")[1:]).strip()
				# 		else:
				# 			finald = lp.strip()
				# 	else:
				# 		if len(lp.split(".")) >= 3:
				# 			finald = ".".join(lp.split(".")[1:]).strip()
				# 		else:
				# 			finald = lp.strip()
				
				#print finald
				finald = lp



				if finald in catdomains:
					catdomains[finald] += 1
				else:
					catdomains[finald] = 1


		final_catdomains = {}
		for k in catdomains:
			if catdomains[k] > 1:
				final_catdomains[k] = catdomains[k]
		fj.write(str(final_catdomains))

