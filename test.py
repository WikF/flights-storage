from google.cloud import bigquery, job

# Construct a BigQuery client object.


def query_bigquery(client: bigquery.Client, query: str) -> bigquery.job.QueryJob:
    query_job = client.query(query)
    return query_job


query_bigquery(client=bigquery.Client())


def print_data(client: bigquery.Client, query: str) -> str:
    query_job = query_bigquery(client, query)
    for row in query_job:
        return "name={}, count={}".format(row[0], row["total_people"])


def add(num1: int, num2: int) -> int:
    return num1+num2
