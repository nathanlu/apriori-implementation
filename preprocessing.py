from collections import Counter
import operator

with open('paper.txt') as f:
	lines = f.readlines()


def get_vocab():
	words_list = [line.split('\t')[1].split() for line in lines]
	words = [word for words in words_list for word in words]

	vocab = list(set(words))

	with open('vocab.txt','w') as out:
		for word in vocab:
			out.write(word+'\n')


def get_title():
	with open('vocab.txt') as f:
		vocab = f.read().split('\n')
	
	with open('title.txt','w') as out:
		for line in lines:
			words = line.split('\t')[1].split()
			words = dict(Counter(words))
			N = len(words)
			out.write(str(N))
			for word in words.keys():
				out.write(' '+str(vocab.index(word))+':'+str(words[word]))
			out.write('\n')

if __name__ == '__main__':
	get_vocab()
	get_title()

