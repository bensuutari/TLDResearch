
from nltk import *



class summtext(object):

	def __init__(self,text):
		self.text=text
		self.tokentext()
		print self.nounsfreq

	def tokentext(self):
		self.sent=sent_tokenize(self.text)
		word=word_tokenize(self.text)
		self.postoken=pos_tag(word)
		self.nouns=list()
		for i in range(0,len(self.postoken)-1):
			if self.postoken[i][1]=='NN':
				self.nouns.append(self.postoken[i][0])
		self.nounsfreq=FreqDist(self.nouns).most_common(50)



		
