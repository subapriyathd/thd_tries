from google.cloud import bigquery
import google.auth
import pandas as pd
#db_dtypes

credentials, project_id = google.auth.default()
print('project:', project_id)
print(credentials)

client = bigquery.Client(project=project_id, credentials=credentials)
print('client executed successfully')
print('fetching query')
query = 'SELECT * FROM `sunny-airfoil-452214-v9.ck_data_tech.sales_orders` LIMIT 1'
print('query:',query)
query_job = client.query(query)
print('query_job:',query_job)
results = query_job.to_dataframe()
print(results)

