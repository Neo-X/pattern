import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from pattern.en import sentiment, polarity, subjectivity, positive
from pattern.db  import Datasheet, pprint, pd

# Sentiment analysis (or opinion mining) attempts to determine if
# a text is objective or subjective, positive or negative.
# The sentiment analysis lexicon bundled in Pattern focuses on adjectives.
# It contains adjectives that occur frequently in customer reviews,
# hand-tagged with values for polarity and subjectivity.

# The polarity() function measures positive vs. negative, as a number between -1.0 and +1.0.
# The subjectivity() function measures objective vs. subjective, as a number between 0.0 and 1.0.
# The sentiment() function returns an averaged (polarity, subjectivity)-tuple for a given string.
for word in ("amazing", "horrible", "public"):
    print word, sentiment(word)

text = "The movie attempts to be surreal by incorporating time travel and various time paradoxes, but it's presented in such a ridiculous way it's seriously boring."
print
print sentiment(text) 
print 
print polarity(text)
print 
print subjectivity(text)

# The input string can be:
# - a string, 
# - a Synset (see pattern.en.wordnet), 
# - a parsed Sentence, Text, Chunk or Word (see pattern.en),
# - a Document (see pattern.vector).

# The positive() function returns True if the string's polarity >= threshold.
# The threshold can be lowered or raised, 
# but overall for strings with multiple words +0.1 yields the best results.
print
print "good:", positive("good", threshold=0.1)
print " bad:", positive("bad")
print

# You can also do sentiment analysis in Dutch or French, 
# it works exactly the same:

#from pattern.nl import sentiment as sentiment_nl
#print "In Dutch:"
#print sentiment_nl("Een onwijs spannend goed boek!")

# You can also use Pattern with SentiWordNet.
# You can get SentiWordNet at: http://sentiwordnet.isti.cnr.it/
# Put the file "SentiWordNet*.txt" in pattern/en/wordnet/
# You can then use Synset.weight() and wordnet.sentiwordnet:

#from pattern.en import wordnet, ADJECTIVE
#print wordnet.synsets("horrible", pos=ADJECTIVE)[0].weight # Yields a (polarity, subjectivity)-tuple.
#print wordnet.sentiwordnet["horrible"]

# For fine-grained analysis, 
# the return value of sentiment() has a special "assessments" property.
# Each assessment is a (chunk, polarity, subjectivity, label)-tuple,
# where chunk is a list of words (e.g., "not very good").

# The label offers additional meta-information.
# For example, its value is MOOD for emoticons:
try:
    table = Datasheet.load(pd("../../valentines.csv"))
    index = set(table.columns[0])
except Exception as e:
    print e
    sys.exit()

for i in range(len(table)):
    text = table[i][1]
    sent = sentiment(text)
    
    print sent[0], sent[1], text
    table[i].append(sent[0])
    table[i].append(sent[1])
    

table.save(pd("cool.csv"))

