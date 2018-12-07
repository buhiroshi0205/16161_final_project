import json

data = json.load(open('data.json','r'))

currentid = 'Start'
while True:
	print(data[currentid]['text'])
	if 'transitions' not in data[currentid]: break
	print()
	for option, details in sorted(data[currentid]['transitions'].items(), key=lambda x:x[0]):
		print('{}: {}'.format(option, details['text']))
	while True:
		print('(Please type your option and press enter.)')
		option = input().strip()
		if option.upper() in data[currentid]['transitions']: option = option.upper()
		if option in data[currentid]['transitions']: break
	currentid = data[currentid]['transitions'][option]['target']
	print("\n")