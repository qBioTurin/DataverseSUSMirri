import pandas as pd
from utils.json_parser import parseJson
import os

def check_microorganism(microorganism):
    if isinstance(microorganism['accessionNumber'], str) and microorganism['accessionNumber'] != '':
        return True
    return False


def loadMicroorganisms(params):
    excel = params.excel
    dataverse = params.dataverse
    base_url = params.base_url
    token = params.token
    
    microorganisms = pd.read_excel(excel, sheet_name="MicroOrganisms")
    total_rows = microorganisms.shape[0]

    count = 0
    while count < total_rows:
        microorganism = {
            "accessionNumber": microorganisms.AccessionNumber[count]}
        if check_microorganism(microorganism):
           parseJson(microorganism)
           os.system(
            f'python3 /script/main.py createDataset --dataverse {dataverse} --json /data.json --base_url {base_url} --token {token}')

        
        count += 1
