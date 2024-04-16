from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions
from couchbase.auth import PasswordAuthenticator

# http://localhost:8091

# Replace with your actual Couchbase credentials and cluster details
cluster = Cluster('couchbase://localhost', ClusterOptions(
  PasswordAuthenticator('Administrator', 'dsci351project')))
bucket = cluster.bucket('interview_questions')
collection = bucket.default_collection()

collection.upsert('key', 'value')
get_res = collection.get("key")
print('Get result - value: {}; CAS: {}'.format(get_res.content_as(), get_res.cas))