import pandas as pd
import json

def get_column_names(schemas, ds_name, sorting_key='column_position'):
    column_details = schemas[ds_name]
    columns = sorted(column_details, key=lambda col: col[sorting_key])
    return [col['column_name'] for col in columns]

def files_to_database_load():
    schemas = json.load(open('data/retail_db/schemas.json'))
    columns = get_column_names(schemas, 'orders')
    df = pd.read_csv(
        'data/retail_db/orders/part-00000',
     names=columns
    )
    conn_uri = 'postgresql://itversity_retail_user:itversity@localhost:5432/itversity_retail_db'
    help(df.to_sql)
    df.to_sql(
        'orders',
        conn_uri,
        if_exists='replace',
        index=False
    )
    pd.read_sql('orders', conn_uri)