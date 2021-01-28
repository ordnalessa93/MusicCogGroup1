import pronouncing	
# First install the pronouncing library via pip

def count_rhymes(lyrics_string):
	n_rhymes = 0,
	for index in range(1, len(lyrics_string)):
		if lyrics_string[index].split()[-1] in pronouncing.rhymes(lyrics_string[index-1].split()[-1]):
			n_rhymes += 1
	return n_rhymes