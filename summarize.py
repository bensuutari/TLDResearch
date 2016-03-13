
from nltk import *
import nltk.data



class summtext(object):

	def __init__(self,text):
		self.numwords=50
		self.text=text
		self.tokentext()
		print self.nounsfreq
		self.sentrank()

	def tokentext(self):
		sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
		self.sent=sent_detector.tokenize(self.text.strip())
		word=word_tokenize(self.text)
		self.postoken=pos_tag(word)
		self.nouns=list()
		for i in range(0,len(self.postoken)-1):
			if self.postoken[i][1]=='NN':
				self.nouns.append(self.postoken[i][0])
		self.nounsfreq=FreqDist(self.nouns).most_common(self.numwords)

	def sentrank(self):
		self.nounsfreqlong=list()
		for gg in range(0,self.numwords):
			if len(list(self.nounsfreq[gg][0]))>1:
				self.nounsfreqlong.append(self.nounsfreq[gg])
		freqnouns,freqfreq=zip(*self.nounsfreqlong)
		
		self.sentscore=list()
		for sentence in self.sent:
			sent2word=sentence.split()
			scoredummy=0
			for word in sent2word:
				if (word in freqnouns):
					ind=freqnouns.index(word)
					scoredummy=scoredummy+freqfreq[ind]
			self.sentscore.append((sentence,scoredummy))
				



		#sorted(y, key=lambda yy: yy[1],reverse=True)

