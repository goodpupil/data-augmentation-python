#-------------------------------------------------------------------------------
# Sherif Sarhan.
# This is a program for data augmentation.
#-------------------------------------------------------------------------------

def is_even(x):
	#Checks if even if remainder is 0.
	if x%2 == 0:
		return True
	#If it's not even then it's False.
	else:
		return False
def remove_evens(xs):
	#Iterates over the length of the list backwards so no error.
	for eachx in range(len(xs)-1,-1,-1):
		#Checks if the current index of list is even.
		if xs[eachx]%2 == 0:
			#Deletes the value from the list.
			del xs[eachx]
	#returns new list.
	return xs
	
def minval(xs):
	#Creates initial comparison index value.
	xzero = xs[0]
	#Loops over list.
	for eachx in xs:
		#Checks if initial comparison is less than or equal to next.
		if xzero <= eachx:
			#If it is, set it as new comparison value.
			xzero = xzero
		#If it's not then set current value as the new comparison.
		else:
			xzero = eachx
	#Returns the minval.
	return xzero

def min_index(xs):
	#Loops over length of list starting at 0.
	for x in range(0,len(xs)):
		#Checks if each index value in list is equal to minval.
		if xs[x] == minval(xs):
			return x
	
def remove_value_once(val,xs):
	#Loops over length of list starting at 0.
	for x in range(0,len(xs)):
		#Checks if the value to be removed is equal to each index.
		if val == xs[x]:
			#If it is, delete the index value.
			del xs[x]
			#Returns True successful remove.
			return True
	#False meaning no remove.
	return False

def min_sorted(xs):
	#Makes copy of xs so it doesn't modify it.
	xscopy = xs
	#Makes new results list.
	results = []
	
	#Loops while the length of the copy is greater than 0.
	while len(xscopy) > 0:
		#Appends the current minval to the results list.
		results.append(minval(xscopy))
		#Removes the mival from the list, len(xscopy) decreases.
		remove_value_once(minval(xscopy),xscopy)
	
	return results

def min_sort(xs):	
	#Makes new list.
	results = []
	#Loops while length of xs is greater than 0.
	while len(xs) > 0:
		#Appends the minval of xs to results list.
		results.append(minval(xs))
		#Removes minval from xs.
		remove_value_once(minval(xs),xs)
	
	#Loops through eachval in list.
	for eachVal in results:
		#Appends eachval to xs list.
		xs.append(eachVal)
	
	return xs

def median(xs):
	#Sorts the xs list through min_sort function.
	min_sort(xs)
	#New variable = to length of xs list.
	xslen = len(xs)	
	#New variable to get median index value. 
	med = xslen // 2
	
	#The med-1 makes it so if there is a tie, the leftmost is chosen.
	return xs[med-1]

def kth(k,xs):
	#Sorts the xs list through min_sort.
	min_sort(xs)
	
	#Returns the kth index of xs list.
	return xs[k]

def zip(xs,ys):
	#Creates new list with xs and ys lengths.
	findmin = [len(xs),len(ys)]
	#Finds the lesser of the two lengths.
	minlen = minval(findmin)
	#Creates a new list for the zipping to be done in.
	ziplist = []
	#Loops through the lesser length range(so no out of range error).
	for eachIndex in range(minlen):
		#Creates a new tuple with each index of xs and ys.
		tup = (xs[eachIndex],ys[eachIndex])
		#Appends each tuple to the ziplist.
		ziplist.append(tup)
	
	return ziplist


#Extra function for finding the lesser length of two lists.	
def minlen_list(xs,ys):
	#Creates a new list with the lenghts of xs and ys.
	findmin = [len(xs),len(ys)]
	#Finds the minval of the list.
	minlen = minval(findmin)
	
	return minlen

def pairwise_multiply(xs,ys):
	#Finds the lesser length of the two lists.
	minlen = minlen_list(xs,ys)
	#Creates a new list for parwise.
	pairwise_list = []
	#Loops over the range of the lesser length of the two lists.
	for eachIndex in range(minlen):
		#Appends the product of xs and ys at the current index.
		pairwise_list.append(xs[eachIndex]*ys[eachIndex])

	return pairwise_list

#Extra function for finding sum of a list.
def listsum(xs):
	#Counter variable.
	listsum = 0
	#Loops through list.
	for eachVal in xs:
		#Adds each list value to the counter variable.
		listsum += eachVal
	
	return listsum
	
def dot_product(xs,ys):
	#First gets the pairwise of the two lists.
	pairwise = pairwise_multiply(xs,ys)
	#Finds the sum of the list.
	pairwiseList_sum = listsum(pairwise)
	
	return pairwiseList_sum

def repeat(val,n):
	#Converts the val into string. Repeats it n number of times.
	return str(val)*n

def interleave(xs,ys):
	#Creates a new list with xs and ys zipped.
	zippedlist = zip(xs,ys)
	#New list for interleave.
	interleave_list = []
	#Loops for all tuples in zipped list.
	for eachTup in zippedlist:
		#Loops for all values in all tuples.
		for eachVal in eachTup:
			#Appends each value to interleave list.
			interleave_list.append(eachVal)
	#Checks if length of xs greater than length of ys.
	if len(xs)>len(ys):
		#If it is, then the extra values(difference) need to be
		#accounted for and added later on.
		#Lendiff accounts for extra values.
		lendiff = len(xs)-len(ys)
		#Loops over all values in length of xs without extra values.
		for eachVal in range(len(xs)-lendiff,len(xs)):
			#Appends each value in xs to interleave list.
			interleave_list.append(xs[eachVal])
	#If length of ys is greater than that of xs.
	else:
		#Lendiff to account for extra values in ys not in xs.
		lendiff = len(ys)-len(xs)
		#Loops over all values in range ys without the extra values.
		for eachVal in range(len(ys)-lendiff,len(ys)):
			#Appends each value in ys to interleave list.
			interleave_list.append(ys[eachVal])
	
	return interleave_list

def shuffle(xs,n=1):
	#Checks if shuffle value less than or equal to 0.
	if n <= 0:
		return None
	#If not.
	else:
		#Creates counter variable.
		x = 0
		#Makes a copy of xs.
		shuffled = xs[:]
		#Loops while counter variable is less than shuffle value.
		while x != n:
			#Creates two halve of the list.
			halve_one = []
			halve_two = []
			#Loops over all values in first halve of shuffled list.
			for eachVal in range(len(shuffled)//2):
				#Appends all 1st halve values of shuffled to halve_one.
				halve_one.append(shuffled[eachVal])
			#Loops over second halve. Uses full length as stop value.
			for eachVal in range(len(shuffled)//2,len(shuffled)):
				#Appends all 2nd halve values of shuffled to halve_two.
				halve_two.append(shuffled[eachVal])
			
			#New list that combines the two halves.
			shuffled = interleave(halve_one,halve_two)
			#Increments counter variable by one.
			x += 1
		
		#Slice updates xs from shuffled.
		xs[:] = shuffled
		

		return None

def all_pairs(xs,ys):
	#Creates new list.
	bigList = []
	#Loops over len xs.
	for eachX in range(len(xs)):
		#Double nested loop for len ys.
		for eachY in range(len(ys)):
			#New tuple with eachX and eachY.
			tup = (xs[eachX],ys[eachY])
			#Appends each tup to list.
			bigList.append(tup)

	return bigList

def stringify_pairs(pairs):	
	#New list.
	stringified = []
	#Loops over len pairs.
	for eachTup in range(len(pairs)):
		#New variable converts each index of each tuple to string.
		str_val = str(pairs[eachTup][0]) + str(pairs[eachTup][1])		
		#Appends the str_val to list.
		stringified.append(str_val)
	
	return stringified

def new_deck(card_vals,suits):
	#New variable of all different combinations.
	allpairs = all_pairs(card_vals,suits)
	#Converts variable to string.
	str_allpairs = stringify_pairs(allpairs)
	
	return str_allpairs

def flatten(xss):
	#New list.
	flatlist = []
	#Loops over each list in xss list.
	for eachList in xss:
		#Double nested loop for each value in each list in xss list.
		for moreList in eachList:
			#Appends each of the lists to a list.
			flatlist.append(moreList)
	return flatlist
