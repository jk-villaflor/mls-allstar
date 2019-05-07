import settings
import helpers


v_playerNames = []
v_sentiVader = 'vader'
v_sentiTextblob = 'textblob'
v_batch = 2
#   fetch data from database
v_conn = helpers.open_dbcon(settings.MONGO_URI)
v_players = helpers.get_players(settings.MONGO_DATABASE, settings.MDB_players, v_conn)

#sanitize player_name
v_playerNames = helpers.get_player_query(v_players, settings.MDB_player_name_col)

#   perform sentiment analysis and quantify player tweets
helpers.get_player_sentiments(v_playerNames, settings.MONGO_DATABASE, settings.MDB_tweets, v_conn, settings.MDB_tweets_coltext, settings.MDB_allstars, v_players, v_sentiVader, v_batch)
helpers.get_player_sentiments(v_playerNames, settings.MONGO_DATABASE, settings.MDB_tweets, v_conn, settings.MDB_tweets_coltext, settings.MDB_allstars, v_players, v_sentiTextblob, v_batch)

#   save results into database
helpers.close_dbcon(v_conn)

