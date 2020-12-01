from collections import Counter
import operator

# Apriori algo implementation
# tlu 2020-11-30

def has_infrequent_subset(candidate,l_prev):

	for k in range(len(candidate)):
		subset = candidate[:k] + candidate[(k+1):]
		#print subset
		if subset not in l_prev:
			return True

	return False

def apriori_gen(l_prev):
	ret = []
	for i in range(len(l_prev)-1):
		for j in range(i+1,len(l_prev)):
			[item1,item2] = [l_prev[i],l_prev[j]]
			if item1[:-1]==item2[:-1] and item1[-1] < item2[-1]:
				new_item = item1 + (item2[-1],)
				if not has_infrequent_subset(new_item,l_prev):
					ret.append(new_item)

	return ret


def apriori(min_sup):
	with open('vocab.txt') as f:
		vocab = f.read().split('\n')
	
	for i in range(5):
		in_file = 'topic-' + str(i) + '.txt'
		out_file = 'pattern/pattern-' + str(i) + '.txt'
		out_file_map = 'pattern/pattern-' + str(i) + '.txt.phrase'
		patterns = {}

		with open(in_file) as topic:
			lines = topic.readlines()

		all_words = [w for line in lines for w in line.split()]
		L1 = dict(Counter(all_words))

		min_count = int(min_sup*len(lines))
		L1 = dict((k, v) for k, v in L1.items() if v >= min_count)

		keys = [(ele,) for ele in L1.keys()]
		
		L = {}
		for j in range(len(keys)):
			L[keys[j]] = L1.values()[j]
		patterns.update(L)
		
		while len(L) > 0:
			C = apriori_gen(L.keys())
			temp = {}
			for line in lines:
				words = line.split()
				for ele in C:
					if set(ele).issubset(words):
						if ele not in temp.keys():
							temp[ele] = 1
						else:
							temp[ele] += 1

			L = dict((k, v) for k, v in temp.items() if v >= min_count)
			patterns.update(L)

		with open(out_file,'w') as out:
			sorted_dic = sorted(patterns.items(), key=operator.itemgetter(1),reverse=True)
			for pair in sorted_dic:
				(key,value) = pair
				l = str(float(value)/len(lines)) +' '
				for w in key:
					l += w + ' '
				l += '\n'
				out.write(l)

		with open(out_file_map,'w') as out:
			sorted_dic = sorted(patterns.items(), key=operator.itemgetter(1),reverse=True)
			for pair in sorted_dic:
				(key,value) = pair
				l = str(float(value)/len(lines)) +' '
				for w in key:
					l += vocab[int(w)] + ' '
				l += '\n'
				out.write(l)

		print 'writing topic %s'%i


if __name__ == '__main__':
	apriori(0.01)
