from nltk.tokenize import sent_tokenize, word_tokenize
#tokenizing - word tokenzers... sentence tokenizers
#lexicon and corpora
#corpora - body of text--ex:medical journals,english language
#lexicon-words and meanings LIKE A DICTIONARY(ambigous)

example_text ="Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
token=word_tokenize(example_text)
print(token)

token2=sent_tokenize(example_text)
print(token2)