  
import boto3
from botocore.client import Config
import shutil
import os

ACCESS_KEY_ID = ''
ACCESS_SECRET_KEY = ''
BUCKET_NAME = ''

archivos = os.listdir()
for file in archivos:
    filee = file.split('.')
    if(len(filee) > 1):
        if(filee[1] == 'csv'):
            data = open(file, 'rb')
            try:
                sizefile = os.stat(file).st_size
                if(sizefile < 5368709120):
                    s3 = boto3.resource(
                        's3',
                        aws_access_key_id=ACCESS_KEY_ID,
                        aws_secret_access_key=ACCESS_SECRET_KEY,
                        config=Config(signature_version='s3v4')
                    )
                    s3.Bucket(BUCKET_NAME).put_object(Key=file, Body=data)
            except ValueError as err:
                print(err)
                print('error al cargar: '+file)
            finally:
                print('Archivo cargado '+file)
                """ ubication = './done/'+file
                shutil.move(file,ubication) """