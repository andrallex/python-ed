import spacy


# Lemmatize the list of words
def lemmatize_words(list_of_words_prepared: list) -> list:

    nlp = spacy.load("ru_core_news_sm")

    text = " ".join(list_of_words_prepared)
    doc = nlp(text)
      
    list_of_lemmatized_words = []
    for token in doc:
        list_of_lemmatized_words.append(token.lemma_)

    return list_of_lemmatized_words

