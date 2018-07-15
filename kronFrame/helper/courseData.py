from bs4 import BeautifulSoup
import requests
from collections import OrderedDict
import requests
import datetime

# url = "http://iiitd.ac.in/academics/m2017"
# r  = requests.get(url)
# data = r.text

"""
Course Data list format
# Course ID # Name # Instructor # Timings+Room # Category # Semester # Year #
"""
def fetch_data():
	soup = BeautifulSoup(open('coursedata_w2018.txt'),'html.parser')
	rows = soup.find_all('tr')	
	course_data = []
	for row in rows:
	    cols = row.find_all('td')
	    cols = [ele.text.strip() for ele in cols]
	    cols.append(cols[0][:3]) # append category
	    cols.append("w2018") # append semester
	    if len(course_data) < 15:
	    	cols.append(2)
	    else:
	    	cols.append(3)
	    course_data.append([ele for ele in cols if ele])

	return course_data
    # print(course_data)

# print(len(course_data))
if __name__ == "__main__":
	c = fetch_data()
	for i in c:
		print(value)
		print(len(i))
		# if len(i) < 4:
		# 	continue
		# else:
		# 	t = i[3].replace("\n","-")
		# 	t = t.replace("-"," ")
		# 	t = t.split(" ")
		# 	t2 = [t1.strip() for t1 in t if len(t1) > 1]
		# 	if(len(t2)%4 > 0):
		# 		print(t2)