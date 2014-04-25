import os, re
import urlparse

tpd = open("two_part_domains.txt").readlines()
dms = [x.strip().rstrip() for x in tpd if x != '']
print dms
## below just in case we need dict speed lookup
# dmsdict = {}
# for domain in dms:
# 	if domain not in dmsdict:
#  		dmsdict[domain] = 0

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
				#BELOW IS LOGIC FOR SUBDOMAINS -- introduces more inaccuracies at moment, so it's been temporarily removed.
				#more work could be done to increase drilling down on individual domains; TODO.
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
				## end subdomain logic
				#print finald #debugging
				finald = lp # useless line without above logic, remaining for consistency
				if finald in catdomains:
					catdomains[finald] += 1
				else:
					catdomains[finald] = 1

		final_catdomains = {}
		for k in catdomains:
			if catdomains[k] > 1:
				final_catdomains[k] = catdomains[k]
		fj.write(str(final_catdomains))

