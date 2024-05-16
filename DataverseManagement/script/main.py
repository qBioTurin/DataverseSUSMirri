from dataverse_controller import DataverseController
from json_parser import Json
import json
import constant as constant
import sys

if __name__ == "__main__":
    dataverse = 'Root'
    dataverse_controller = DataverseController(constant.base_url, constant.token)
    
    # print(dataverse_controller.create_dataverse())

    #results_api = api_caller.rest_get('https://susmirri-mbrcapi.di.unito.it/strains')
    json_file = sys.argv[1]
    results_dir = sys.argv[2]

    with open(json_file, 'r') as file:
        values = json.load(file)
        
    # dataverse_controller.download_datafile('doi:10.5072/FK2/BZNQCE', results_dir)

    json = Json(values)
    #json.add_strain(results_api[0])
    json.parsing_dataset()
    #json.save_json(True)
    ds_pid = dataverse_controller.create_dataset(dataverse, json.save_json())
    dataverse_controller.add_datafile_to_dataset(ds_pid, results_dir)
    #dataverse_controller.publish_dataset(ds_pid, 'major')

