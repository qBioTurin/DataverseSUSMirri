from dataverse_controller import DataverseController
import constant as constant
import sys

dataverse_controller = DataverseController(constant.base_url, constant.token)

DOI = sys.argv[1]
results_dir = sys.argv[2]
#'doi:10.5072/FK2/BZNQCE'
dataverse_controller.download_datafile(f'doi:{DOI}', results_dir)