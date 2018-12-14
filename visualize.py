from graphviz import Digraph
import json

plot = Digraph()
obj = json.load(open('data.json', 'r'))
for i in obj:
	plot.node(i)
for i in obj:
	if 'transitions' in obj[i]:
		for j,k in obj[i]['transitions'].items():
			name = k['target']
			if name in obj:
				plot.edge(i, name)
			else:
				plot.edge(i, name+"\n(not yet implemented)")
print(plot.source)
plot.render(view=True, cleanup=True, format='svg')