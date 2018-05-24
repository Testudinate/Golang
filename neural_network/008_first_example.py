https://sourcedexter.com/tensorflow-text-classification-python/

# a table structure to hold the different punctuation used
tbl = dict.fromkeys(i for i in xrange(sys.maxunicode)
                      if unicodedata.category(unichr(i)).startswith('P'))
 
# method to remove punctuations from sentences.
def remove_punctuation(text):
    return text.translate(tbl)
 
#initialize the stemmer
stemmer = LancasterStemmer()
#variable to hold the Json data read from the file
data = None
 
# read the json file and load the training data
with open('data.json') as json_data:
    data = json.load(json_data)
    print (data)
 
# get a list of all categories to train for
categories = list(data.keys())
words = []
