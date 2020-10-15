import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Codigos.pre_processamento_text import pre_processamento_texto

corpus_texto = open('estatuto_uespi.txt','r',encoding='utf8')
corpus = []
for i in corpus_texto:
    corpus.append(i)
corpus_join = ''.join(corpus)
corpus_split = corpus_join.split()
corpus_replace = corpus_join.replace('\n','')

lista_sentencas = nltk.sent_tokenize(corpus_replace)
lista_sentencas_pre_processadas = []


for frases in lista_sentencas:
    lista_sentencas_pre_processadas.append(pre_processamento_texto(frases))


# calcular similariedade do cosseno + TF-IDF
def similaridade_sentencas(sentenca):
    lista_similaridade = []
    # recebe a sentença para se analisar é ja faz o pré-processamento
    sentenca_entrada = pre_processamento_texto(sentenca)
    # adicionar a sentenca de entrada no conjunto do regimento
    lista_sentencas.append(sentenca)
    lista_sentencas_pre_processadas.append(sentenca_entrada)

    # convertendo base de dados para tf-idf
    tfidf = TfidfVectorizer()
    palavras_vetorizadas = tfidf.fit_transform(lista_sentencas_pre_processadas)

    # calculo da similariedade
    # pega a ultima frase que foi adicionada que no caso e nossa 'sentenca_entrada'
    similaridade = cosine_similarity(palavras_vetorizadas[-1], palavras_vetorizadas)

    # ordena por ordem decrescente cada indice
    similaridade.argsort()

    # 5 maiores resultados de similariedade
    n1 = similaridade.argsort()[0][-2]


    lista_similaridade.append(str(lista_sentencas[n1]))


    # remove a sentenca adicionada
    del (lista_sentencas[-1])
    del (lista_sentencas_pre_processadas[-1])

    return str(lista_similaridade)

