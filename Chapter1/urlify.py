def urlify(query,len):
	return query.rstrip().replace(" ", "%20")

print(urlify("Mr John Smith    ", 13))