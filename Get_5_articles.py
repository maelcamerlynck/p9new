import pandas as pd
import numpy as np
from scipy.spatial import distance

def get5Articles(article_emb, userid, frame):
    print(userid)
    #get all articles read by user
    var= frame.loc[frame['user_id'] == int(userid)]['click_article_id'].tolist()
    #print(frame.shape)
    #print(len(var))
    #we choose the last element of the list
    value = var[-1]
    print(value)

    #get 5 articles the most similar to the selected one
    distances = distance.cdist([article_emb[value]],article_emb, "cosine")[0]
    #find indexes except the one selected
    result = np.argsort(distances)[1:6]
    #similarity value between selected article and 5 top proposed articles (the smaller the better!)
    similarite = distance.cdist([article_emb[value]],article_emb[result], "cosine")[0]
    print(result)
    print(similarite)
 
        
    return result.tolist()