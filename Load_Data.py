import pandas as pd

def chargement(path):
    # Article Embeddings
    article_emb = pd.read_pickle(path + 'articles_embeddings.pickle')

    # Article Metadata
    articles = pd.read_csv(path + 'articles_metadata.csv')

    # All Clicks
    frame = pd.read_csv(path + 'clicks.csv')
    
    return article_emb, articles, frame