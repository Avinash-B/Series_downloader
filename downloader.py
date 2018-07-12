import webbrowser
import time
import sys


quality=sys.argv[1]
pre=sys.argv[2]
r = open("webpage.html","r+")
string="href"
url=[]
print "Searching url's for required quality........."
for line in r.readlines():
	if string in line and quality in line:
		numbers=[]
		for j in range(len(line)):
			if line[j]=='"':
				numbers.append(j)
		new=line[numbers[0]+1:numbers[1]]
		new=pre+new
		url.append(new)
for each in url:
	webbrowser.open_new_tab(each)
	time.sleep(10)