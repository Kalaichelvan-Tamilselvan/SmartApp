import string
from textblob import Word, TextBlob
import wikipedia
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

'''Remove Punctuations'''
# a_string = input("Enter a string: ")
# remove_whitespace = (" ".join(a_string.split()))
# remove_punctuation = remove_whitespace.translate(str.maketrans('', '', string.punctuation))
#
# print(remove_punctuation)


'''Upper case'''
# a_string = input("Enter a string: ")
# Upper_case = a_string.upper()
#
# print(Upper_case)


'''Lower case'''
# a_string = input("Enter a string: ")
# Lower_case = a_string.lower()
#
# print(Lower_case)


'''Remove New lines'''
# a_string = "Enter\n a\n string:"
# Remove_newline = ''.join(a_string.splitlines())
#
# print(Remove_newline)


'''Count characters'''
# a_string = input("Enter a string: ")
# count = len(a_string) - a_string.count(" ")
# print(count)


'''Text Spellchecker'''
# def text_spellchecker(text):
#     text = TextBlob(text)
#
#     result = text.correct()
#
#     print(result)
#
#
# text_spellchecker(input("Enter a text: "))


''' Generate summary of word '''
# word = input('Enter the Word: ')
# print(wikipedia.summary(word))


'''Remove stop words from text'''
# example_sent = """This is a sample sentence,showing off the stop words filtration."""
#
# stop_words = set(stopwords.words('english'))
#
# word_tokens = word_tokenize(example_sent)
#
# filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
#
# filtered_sentence = []
#
# for w in word_tokens:
#     if w not in stop_words:
#         filtered_sentence.append(w)
#
# print(word_tokens)
# print(filtered_sentence)
