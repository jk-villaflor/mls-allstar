

# Database values
MONGO_USER = "cluster-user-1"
MONGO_P = "clusteradmin123"
MONGO_URI = "mongodb://"+MONGO_USER+":"+MONGO_P+"@cluster0-shard-00-00-a6fk9.mongodb.net:27017,cluster0-shard-00-01-a6fk9.mongodb.net:27017,cluster0-shard-00-02-a6fk9.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true"
MONGO_DATABASE = "MLS"


#collections
MDB_players = "mls_players_stg"
MDB_tweets = "mls-tweets"
#MDB_players = "mls_players_stg1"
#MDB_tweets = "mls-tweets-stg"
MDB_allstars = 'mls_allstar_stg'


#column_names
MDB_tweets_coltext = 'text'
MDB_player_name_col = 'player_name'
