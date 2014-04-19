import json
import os

cats = [x[:-4] for x in os.listdir("linkfiles") if x.endswith(".txt")]


done_already = []

for x in os.listdir("linkfiles"): 
	if x.endswith("-ORIGV.json"):
		for c in [b for b in cats if b != x[:-11]]: # all -11s were -5s otherwise, when not using -ORIGV files
			if (c,x[:-11]) not in done_already and (x[:-11],c) not in done_already:
				done_already.append((c,x[:-11]))
				f = open("combfiles/{}--{}.txt".format(x[:-11],c),"w")
			
				filedata = open("linkfiles/{}".format(x),'r')
				nd = json.loads(filedata.read().replace("\'", '"'))
				compd = json.loads(open("linkfiles/{}.json".format(c)).read().replace("\'", '"'))
				both = [k for k in nd.keys() if k in compd]
				for i in both:
				# 	print i
					f.write(i+"\n")
			else:
				continue












