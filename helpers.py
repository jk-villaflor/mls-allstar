from pymongo import MongoClient
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as vaderSent
from textblob import TextBlob
import datetime

def open_dbcon(i_connection_string):
    return MongoClient(i_connection_string)

def close_dbcon(i_conn):
    i_conn.close()
    pass

def get_players(i_dbname, i_collection, i_conn):
    db = i_conn[i_dbname]
    player_collection = db[i_collection]
    return player_collection.find()

def get_player_query(i_players,i_col_name):
    o_playerQuery = []
    for player in i_players:
        if(',' in player[i_col_name]):
            o_playerQuery.append({'player_name':player[i_col_name],'playerQuery':(player[i_col_name].split()[1] + player[i_col_name].split()[0]).strip(','),'position':player['position']})
        else:
            o_playerQuery.append({'player_name':player[i_col_name],'playerQuery':player[i_col_name],'position':player['position']})
    return o_playerQuery

def get_player_tweets(i_dbname, i_collection, i_conn, i_searchPhrase):
    db = i_conn[i_dbname]
    tweets_collection = db[i_collection]
    return  tweets_collection.find(i_searchPhrase)

def get_player_sentiments(i_playerList, i_dbname, i_collName, i_conn, i_text_col, i_resultColl, i_players, i_flag, i_batch):
    v_vanalyzer = vaderSent() #<- The sith sent me
    v_scores =''
    db = i_conn[i_dbname]

    for player in i_playerList:
        v_pos_ctr = 0
        v_neg_ctr = 0
        v_neutral_ctr = 0
        v_player_tweets = get_player_tweets(i_dbname, i_collName, i_conn, {i_text_col :{'$regex':'.*'+player['playerQuery']+'.*'}})
        
        if(v_player_tweets.count() > 0):
            for tweet in v_player_tweets:
                if(i_flag == 'vader'):
                    v_scores = v_vanalyzer.polarity_scores(tweet[i_text_col])
                    if(v_scores['pos'] > 0.5):
                        v_pos_ctr += 1
                else:
                    v_tanalyze = TextBlob(tweet[i_text_col])
                    if(v_tanalyze.sentiment.polarity > 0.5):
                        v_pos_ctr+=1
            #endif
        if(v_pos_ctr > 0):
            db[i_resultColl].insert_one({'player_name': player['player_name'],'position':player['position'], 'positive_count':v_pos_ctr, 'created_date':datetime.datetime.now(), 'method':i_flag, 'batch':i_batch, 'total_tweets':v_player_tweets.count()})
