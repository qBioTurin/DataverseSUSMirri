from utils.dataverse_controller import DataverseController
import utils.constant as constant

def downloadDataset(args):
	DOI = args.DOI
	outdir = args.outdir

	dataverse_controller = DataverseController(constant.base_url, constant.token)

	dataverse_controller.download_dataset(f'doi:{DOI}', outdir)