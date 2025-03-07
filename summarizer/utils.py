from transformers import pipeline
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords



length_settings = {
        1: (30, 60),
        2: (80, 150),
        3: (200, 300)
    }

def summary(text,depth):
    pipe = pipeline("summarization", model="facebook/bart-large-cnn",
                    max_length=length_settings[depth][1],
                    min_length=length_settings[depth][0],
                    do_sample=False
                    )

    res = pipe(text)
    return res


def keywords(text):

    words = word_tokenize(text)

    filtered_words = [
        word.lower()
        for word in words
        if word.lower() not in stopwords.words('english')
           and word.isalpha()
    ]
    return  filtered_words