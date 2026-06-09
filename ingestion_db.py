import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename="logs/ingestion_db.log", 
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s", 
    filemode="a"  
)
engine = create_engine('sqlite:///inventory.db')
CHUNK_SIZE = 10000  # rows per chunk

def ingest_db(df, table_name, engine):
    '''Ingest a single dataframe chunk into the database table'''
    df.to_sql(table_name, con=engine, if_exists='append', index=False)

def load_raw_data():
    '''Load CSVs in chunks and ingest into db'''
    start = time.time()

    for file in os.listdir('data'):
        if '.csv' in file:
            table_name = file[:-4]
            file_path = os.path.join('data', file)
            logging.info(f'Starting ingestion of {file}')

            first_chunk = True
            for chunk in pd.read_csv(file_path, chunksize=CHUNK_SIZE):
                if first_chunk:
                    chunk.to_sql(table_name, con=engine, if_exists='replace', index=False)
                    first_chunk = False
                else:
                    chunk.to_sql(table_name, con=engine, if_exists='append', index=False)

            logging.info(f'Finished ingesting {file}')  # ← aligned with 'first_chunk = True'

    end = time.time()
    total_time = (end - start) / 60
    logging.info('--------------Ingestion Complete------------')
    logging.info(f'Total Time Taken: {total_time:.2f} minutes')