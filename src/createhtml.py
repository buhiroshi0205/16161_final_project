import os, shutil, json


shutil.rmtree("html", ignore_errors=True)
os.mkdir("html")
index = '''<html>
  <head>
    <title>AI & Humanity (Fall 2018) Individual Futuring Project</title>
  </head>
  <body>
    <a href="Start.html">Play!</a>
    <p>
      Details for this project can be found on github:
      <a href="https://github.com/buhiroshi0205/16161_final_project">https://github.com/buhiroshi0205/16161_final_project</a>.
    </p>
  </body>
</html>'''
open("html/index.html", "w").write(index)


data = json.load(open("data.json","r"))

for name, details in data.items():
	file = open("html/"+name+".html", "w")
	file.write(details["text"].replace("\n", "<br/>\n"))
	file.write("\n<br/><br/>\n")
	if "transitions" in details:
		for idx, option in sorted(details["transitions"].items(), key=lambda x: x[0]):
			file.write(idx + ': <a href="' + option["target"] + '.html">' + option["text"] + "</a><br/>\n")
	file.close()