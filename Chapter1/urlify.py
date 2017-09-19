##strip white spaces from end of string, replace white spaces with $20
def urlify(query,len):
	return query.rstrip().replace(" ", "%20")

print(urlify("Mr John Smith    ", 13))