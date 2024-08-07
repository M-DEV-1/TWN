# TWN_InfoDecay

## Context

Usage of TempoWordNet to perform lemmetization and stemming for Information Decay paper feature.

# Steps

1. study and understand lemmetization, stemming, stop word removal (preprocessing)

2. use NLTK, Gensim, and Spacy (libraries)

3. PANDAS, and NumPy (dataframes)

4. Create a script to convert TempoWordNet.txt to dataframe in Pandas with a quadtuple (past, present, future, atemporal)

5. This is to be done after preprocessing (stemming, lemmatization and stop words removal)

6. The script works such that each sentence is represented as an array of tuples, which returns a new tuple of averages (past_avg, present_avg, etc...)

7. You must use a Python Notebook to do this task.

8. Use try exception to get rid of words which do not exist in TempoWordNet
