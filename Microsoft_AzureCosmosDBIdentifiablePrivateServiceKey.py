from azure.cosmos import CosmosClient

# This is a test key to check secret scanning detection
url = "https://your-account.documents.azure.com:443/"
key = "mongodb+srv://user1:<password>@debil.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"
# this key is not real :)

# Initializing the CosmosDB client
client = CosmosClient(url, key)

# Get database list
databases = list(client.list_databases())
print("Databases:", databases)
