import string
from textblob import TextBlob
import wikipedia
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def punctuation_removal(text):
    for character in text:
        if character in string.punctuation:
            text = text.replace(character, "")
    return text


def text_upper(text):
    return text.upper()


def text_lower(text):
    return text.lower()


def remove_newline(text):
    text = " ".join(text.split())
    return text


def extra_space_remove(text):
    extra_space = "  "
    while extra_space in text:
        text = text.replace(extra_space, " ")
    return text.strip()


def count_characters(text):
    text = len(text) - text.count(" ")
    return str(text)


def text_spellchecker(text):
    text = TextBlob(text.casefold())
    result = text.correct()
    return str(result)


def summary_generate(text):
    try:
        return wikipedia.summary(text, auto_suggest=False)
    except wikipedia.exceptions.PageError:
        return f'Summary for "{text}" is not found! Please try again with another word.'
    except wikipedia.exceptions.DisambiguationError as e:
        return f'Summary for "{text}" is not found! {e.options}'
    except KeyError:
        return f'Summary for "{text}" is not found! Please try again with another word.'


def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(str(text))
    filtered_sentence = str([w for w in word_tokens if not w.lower() in stop_words])
    remove_whitespace = (" ".join(filtered_sentence.split()))
    remove_punctuation = remove_whitespace.translate(str.maketrans('', '', string.punctuation))
    if 'Summary' in text:
        return f' Not found! Try again.'
    else:
        return remove_punctuation
