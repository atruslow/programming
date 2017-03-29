
def has_unique_characters(string:str) -> bool:
	"""
	>>> has_unique_characters('aaa')
	False
	>>> has_unique_characters('aba')
	False
	>>> has_unique_characters('aAa')
	False
	>>> has_unique_characters('12345678')
	True
	>>> has_unique_characters('abcedftz')
	True
	"""
	unique_chars = {i for i in string}
	return len(unique_chars) == len(string)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
