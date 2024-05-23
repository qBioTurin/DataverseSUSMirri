from utils.dataverse_controller import DataverseController
import utils.constant as constant

def addDatafileToDataset(args):
	DOI = args.DOI
	datafile_dir = args.datafile_dir

	dataverse_controller = DataverseController(constant.base_url, constant.token)

	dataverse_controller.add_datafile_to_dataset(f'doi:{DOI}', datafile_dir)