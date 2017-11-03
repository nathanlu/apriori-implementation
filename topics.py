from collections import Counter
import operator

def get_topic_words():
	with open('result/word-assignments.dat') as f:
		lines = f.readlines()
	#with open('vocab.txt') as v:
		#vocab = v.read().split('\n')

	for i in range(5):
		with open('topic-'+str(i)+'.txt','w') as out:
			count = 0
			for line in lines:
				flag = False
				for word in line.split()[1:]:
					if word[-1] == str(i):
						out.write(word.split(':')[0]+' ')
						flag = True
				if flag:		 
					out.write('\n')
				print 'line'+str(count)
				count += 1
		print 'topic'+str(i)+' finished'

if __name__ == '__main__':
	get_topic_words()