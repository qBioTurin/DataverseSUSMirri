from utils.dataverse_controller import DataverseController
import utils.constant as constant

def removeDatafileFromDataset(args):
	DOI = args.DOI
	file_name = args.file_name

	dataverse_controller = DataverseController(constant.base_url, constant.token)

	dataverse_controller.remove_datafile_from_dataset(f'doi:{DOI}', file_name)