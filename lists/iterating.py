


#### Practicing Iterating thru lists

def meet_the_cats(cats):
	"""Iterating thru a single list and print the breed of cat"""

	for cat_breed in cats:
		print "This is cat is an {}. Its damn awesome.".format(cat_breed)

meet_the_cats(["Abyssinian","Aegean","American Bobtail","Arabian Mau"])

def big_words(words):
	"""Takes a list of words and appends to new list if word has more than 4 letters"""
	big_words = []
	# letter_count = 0
	for word in words:
		for letter in word:
			letter_count = 0
			letter_count += 1
			print letter_count
			


def similar_words(word):
	"""Compares two lists and prints a new list of words in common. """
	pass


def smallest_number(number):
	"""takes a list of numbers and prints the smallest number  """
	pass

def largest_number(number):
	"""takes a list of numbers and prints the largest number  """
	pass


big_words(['cat','hello'])