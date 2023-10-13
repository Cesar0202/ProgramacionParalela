import nltk
from nltk.corpus import twitter_samples
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# conjunto de datos de Twitter
nltk.download("twitter_samples")

tweets_positivos = twitter_samples.strings("positive_tweets.json")
tweets_negativos = twitter_samples.strings("negative_tweets.json")


def extraer_caracteristicas(tweet):
    palabras = word_tokenize(tweet)
    return ' '.join(palabras)


caracteristicas_positivas = [extraer_caracteristicas(
    tweet) for tweet in tweets_positivos]
caracteristicas_negativas = [extraer_caracteristicas(
    tweet) for tweet in tweets_negativos]
todas_caracteristicas = caracteristicas_positivas + caracteristicas_negativas
etiquetas = ['positivo'] * len(caracteristicas_positivas) + \
    ['negativo'] * len(caracteristicas_negativas)

vectorizador = TfidfVectorizer(max_features=5000)
matriz_caracteristicas = vectorizador.fit_transform(todas_caracteristicas)

clasificador = SVC(kernel='linear')
clasificador.fit(matriz_caracteristicas, etiquetas)
while True:
    print("\n")
    texto_analizar = input(
        "Ingresa el texto a analizar (o escribe 'salir' para salir): ")
    if texto_analizar.lower() == 'salir':
        break

    texto_analizar = extraer_caracteristicas(texto_analizar)
    vector_texto = vectorizador.transform([texto_analizar])
    sentimiento = clasificador.predict(vector_texto)
    print("Sentimiento del texto:", sentimiento[0])