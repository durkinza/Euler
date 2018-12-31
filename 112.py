# global var
# num will track how far we are in searching for bouncy numbers 
num = 100

def is_increasing_number(num):
	"""
	Will return true if number is a increasing number
	and false otherwise
	"""
	num_list = [int(i) for i in str(num)]
	prev_num = num_list[0]
	for n in num_list:
		if n < prev_num:
			return False
		prev_num = n
	return True
		
def is_decreasing_number(num):
	"""
	Will return true if number is a decreasing number
	and false otherwise
	"""
	num_list = [int(i) for i in str(num)]
	prev_num = num_list[0]
	for n in num_list:
		if n > prev_num:
			return False
		prev_num = n
	return True

def gen_bouncy():
	"""
	Will continuously output bouncy numbers
	"""
	global num
	while True:
		num+=1
		if (not is_increasing_number(num) and not is_decreasing_number(num)):
			yield num

# get a/an (endless) list of bouncy numbers
bouncy = gen_bouncy()
# cound how many bouncy numbers have been found so far
count = 0
# for every new bouncy number, check the current ratio
for n in bouncy:
	count+=1
	# once we reach the desired ration of 99%, print out how far we had to search
	if (float(count) / float(num) >= 0.99):
		print(num)
		break
