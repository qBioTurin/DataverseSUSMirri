from pyDataverse.api import NativeApi, DataAccessApi
from pyDataverse.models import Datafile, Dataverse
from pyDataverse.utils import read_file
import os
from utils.json_parser import json_to_file


# This class is a controller for Dataverse
# 1. __init__(self, base_url, token): initialize the object using a base_url of dataverse implementation
#   and a dataverse api token (e.g. base_url='https://mirri-dataverse.di.unito.it')
# 2. create_dataverse(self): TODO
# 3. create_dataset(self, dataverse, json): create a dataset from the json in the dataverse parameter
class DataverseController:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.api = NativeApi(self.base_url, self.token)
        self.data_api = DataAccessApi(self.base_url, self.token)  # Init a Data Access to the API

    # def create_dataverse(self):
    #     dv = Dataverse()
    #     dv_filename = "./dataverse.json"
    #     dv.from_json(read_file(dv_filename))
    #     resp = self.api.create_dataverse(":root", dv.json())
    #     resp = self.api.publish_dataverse("pyDataverse_user-guide")
    #     resp = self.api.get_dataverse("pyDataverse_user-guide")
        
    #     return resp.json()
    
    def create_dataverse(self, dv_filename):
        dv = Dataverse()
        # dv_filename = "./dataverse.json"
        dv.from_json(read_file(dv_filename))
        #TODO check where to create the dataverse
        resp = self.api.create_dataverse(":root", dv.json())
        # resp = self.api.publish_dataverse("pyDataverse_user-guide")
        # resp = self.api.get_dataverse("pyDataverse_user-guide")
        
        return resp.json()

    def create_dataset(self, dataverse, json):
        resp = self.api.get_dataverse(dataverse)

        if resp.json()['status'] != 'OK':
            return 'ERROR dataverse'

        resp = self.api.create_dataset(dataverse, json)

        if resp.json()['status'] != 'OK':
            return resp.json()

        return resp.json()["data"]["persistentId"]  # TODO create a human readable string
        
    def get_dataset(self, DOI):
        #TODO crea un file json con i dati del dataset
        print(self.api.get_dataset(DOI).json())
        return self.api.get_dataset(DOI)
        
    def download_dataset(self, DOI, results_dir):
        resp = self.api.get_dataset(DOI)
        if resp.json()['status'] != 'OK':
            print(resp.json()['message'])
            return
        json_to_file(resp.json()['data']['latestVersion'], f'dataverse_metadata.json')
        os.system(f'mv dataverse_metadata.json {results_dir}')
        if (resp.json()['data']['latestVersion']['files'] != []):
            os.system(f'curl -L -O -J -H "X-Dataverse-key:{self.token}" {self.base_url}/api/access/dataset/:persistentId/?persistentId={DOI}')
            os.system(f'mv dataverse_files.zip {results_dir}')
    
    def publish_dataset(self, DOI, release_type='major'):
        return self.api.publish_dataset(DOI, release_type=release_type)

    def add_datafile_to_dataset(self, DOI, results_dir):
        for file in os.listdir(results_dir):
            df = Datafile()
            df_filename = f'{results_dir}/{file}' 
            df.set({"pid": DOI, "filename": df_filename})
            resp = self.api.upload_datafile(DOI, df_filename, df.json())

        #TODO change return

        return resp.json()

