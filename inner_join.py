'''
Written by: Mohdhar Noor
Note that this was written in Python 2 (for backwards compatibility)
Implements a convential SQL inner join in O(nlogn) time, due to sorting,
the acutal query takes O(n+m) time for two tables of size n and m
'''
import urllib, json, sys

def count_total(name):
	'''
		Returns the order total for specified customer
	
		name: Name of customer
	'''
	total = 0
	for row in result:
		if row["name"] == name:
			total += row["price"]
	return total

if len(sys.argv) < 5:
	print "format: python inner_join.py ", "<file1>.json <file2>.json key1 key2"
	sys.exit()

file1 = sys.argv[1]
file2 = sys.argv[2]
key1 = sys.argv[3]
key2 = sys.argv[4]

t1 = json.loads(open(file1).read())
t2 = json.loads(open(file2).read())

n = len(t1)
m = len(t2)

#assign the left and right tables
#conventionally, the left table would contain the primary key
#and the left table the foreign key
if n <= m:
	left = t1
	right = t2
	lkey = key1
	rkey = key2
else:
	left = t2
	right = t1
	lkey = key2
	rkey = key1
#this python implementation of sort runs in O(nlogn)/O(mlogm)
left.sort(key=lambda x: x["cid"])
right.sort(key=lambda x: x["customer_id"])

result = []
i = 0
j = 0

#O(n+m) worst case complexity
while (i < n) and (j < m):
	if left[i][lkey] == right[j][rkey]:
		#these are all constant time operations
		x = left[i].copy()
		del x[lkey]
		y = right[j].copy()
		del y[rkey]
		x.update(y)
		
		result.append(x)
		j += 1
	elif left[i][lkey] < right[j][rkey]:
		i += 1
	else:
		j += 1

shopify_file1 = (sys.argv[1] == "orders.json") or (sys.argv[1] == "customers.json")
shopify_file2 = (sys.argv[2] == "orders.json") or (sys.argv[2] == "customers.json")

if shopify_file1 and shopify_file2:
	print "length of result is ", len(result)
	print "The total for orders placed by Barry is ", count_total("Barry")
	print "The total for orders placed by Steve is ", count_total("Steve")
else:
	print result
