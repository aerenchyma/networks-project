import os
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import numpy as np
np.seterr(divide='ignore', invalid='ignore')

# calculating info for weights n stuff
cfiles = os.listdir("combfiles")
total_shared = []
for x in cfiles:
	f = open("combfiles/{}".format(x),'r')
	for line in f:
		total_shared.append(line.strip())

ts = set(total_shared)
total_shared_links = len(ts) # 1103
#print ts
#print len(ts) 

# create dictionary of shared links
shared_domains = {}
for y in cfiles:
	shared_domains[(tuple(y[:-4].split("--")))] = len(open("combfiles/{}".format(y)).readlines())# split the name of the combined file on the --, taking off the extension

#print shared_domains
perc_shared_domains = {}
for k in shared_domains:
	perc_shared_domains[k] = (shared_domains[k]/float(total_shared_links))*100 # these are percentages
# print perc_shared_domains
# print shared_domains

weight_dist = np.array(perc_shared_domains.values())
sortedwts = sorted(weight_dist, reverse=True)

fs = open("sorted_weight_dist.csv","w")
for w in sortedwts:
	fs.write("{}\n".format(w))
fs.close()

import powerlaw
data = sortedwts #data can be list or Numpy array
results = powerlaw.Fit(data,method="KS")
print results.power_law.alpha
print results.power_law.xmin
R, p = results.distribution_compare('power_law', 'lognormal')
print R,p

# print "max",max([x[1] for x in shared_domains.items()])
# print "min",min([x[1] for x in shared_domains.items()])

# min_pairs = [k for k,v in shared_domains.items() if v == 2]
# # for p in min_pairs:
# # 	print 
# print len(min_pairs)

# BUILDING NETWORK FTW

cats = [x[:-4] for x in os.listdir("linkfiles") if x.endswith(".txt")] # all category namestrings

G = nx.Graph() 
for categ in cats:
	G.add_node(categ)
#print G.nodes()


for key in perc_shared_domains:
	if shared_domains[key] == 0:
		print key
	else:
		G.add_edge(key[0],key[1],weight=perc_shared_domains[key]*100)#{'weight':perc_shared_domains[key]*100})


values = [int(10*(G[n[0]][n[1]]['weight'])) for n in G.edges()] # ?????
jet = cm = plt.get_cmap('jet') 
cNorm  = colors.Normalize(vmin=0, vmax=values[-1])
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)


colorList = []
for i in range(len([int(G[n[0]][n[1]]['weight']) for n in G.edges()])):
      colorVal = scalarMap.to_rgba(values[i])
      colorList.append(colorVal)


nx.draw_random(G,edge_color=colorList,font_size="18")
plt.show()

#pos = nx.random_layout(G)
#elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5]
# esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5]


# nx.draw_random(G,edge_color='g',font_size=18)
# plt.show()

#pos = nx.spring_layout(G)
# nx.draw_networkx_edges(G,pos,width=) #


# layout = nx.spring_layout(G)  # or whatever layout you wish   
# nx.draw_spring(G)   # draw the graph, must be consistent with layout above
# edgeLabels = {}  # dictionary of node tuples to edge labels: {(nodeX, nodeY): aString}
# for a, b in G.edges():     # loop over all the edges
#     edgeLabels[(a, b)] = str(G.get_edge_data(a, b, {"weight":0})["weight"])   # retrieve the edge data dictionary
     
# nx.draw_networkx_edge_labels(G,pos=layout, edge_labels=edgeLabels) # draw the edge labels
# plt.show()   # show the plotting window


# elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5]
# esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5]
# pos = nx.spring_layout(G)
# nx.draw_networkx_edges(G,pos,edgelist=elarge, width=6)
# nx.draw_networkx_edges(G,pos,edgelist=esmall, width=6,alpha=0.5,edge_color='b',style='dashed')

# # for e in G.edges(): 
# # 	print e
# # 	print G[e[0]][e[1]]['weight']

# #nx.draw(G,nx.spectral_layout(G))
# # nx.draw_spring(G)
# plt.show()