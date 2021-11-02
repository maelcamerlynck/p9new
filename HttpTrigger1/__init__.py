import logging
import azure.functions as func
import os
import json
import pandas as pd
import numpy as np
from scipy.spatial import distance
from Load_Data import *
from Get_5_articles import *

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Nouvelle requête HTTP en cours...')

    userid = req.params.get('userid')
    if not userid:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            userid = req_body.get('userId')

    if userid:
        # Load data
        logging.info('Load data in progress ...')
        path = os.getcwd() + '\\Data_globocom\\'
        article_emb, articles, frame = chargement(path)
        logging.info('Load data ok')
        
        # Recommandation du top5
        logging.info('Recommandation des 5 articles en cours ....')
        record5 = get5Articles(article_emb, userid, frame)  
    
        # Retour des 5 articles recommandés
        return func.HttpResponse(json.dumps(record5), status_code=200)
    else:
        return func.HttpResponse(
             "Pass a userId in the query string or in the request body for a personalized response.",
             status_code=200
        )
