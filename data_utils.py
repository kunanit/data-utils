import pandas as pd
from sqlalchemy import create_engine
from datetime import date
from s3fs import S3FileSystem


def create_db_engine(database=None,user=None,password=None,host=None,port=5432):
    """
    Create sqlalchemy postgres engine from settings
    """
    engine_string = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format(
        user = user,
        password = password,
        host = host,
        port = port,
        database = database,
    )
    return create_engine(engine_string)


def create_db_engine_from_settings_dict(database_settings):
    """
    Create sqlalchemy postgres engine from django db settings dict
    """
    return create_db_engine(
        database = database_settings['NAME'],
        user = database_settings['USER'],
        password = database_settings['PASSWORD'],
        host = database_settings['HOST'],
    )


def write_df_to_s3(df, s3_bucket, s3_key, encoding='utf-8', index=False, **kwargs):
    """
    Writes a pandas dataframe to a file on AWS S3 
    Utilizes s3fs pandas integration
    Passes some alternate kwarg defaults for DataFrame.to_csv()
    
    Arguments:
        df (pd.DataFrame): dataframe to write
        s3_bucket (str): s3 bucket name, e.g. "my-bucket"
        s3_key (str): s3 bucket key to write file as, e.g. "data/myfile.csv"
        kwargs: keyword arguments to pass to pd.DataFrame.to_csv()
    """
    s3 = S3FileSystem(anon=False)
    s3file = s3.open("{}/{}".format(s3_bucket, s3_key), mode='wb')
    df.to_csv(s3file, encoding=encoding, index=index, **kwargs)
