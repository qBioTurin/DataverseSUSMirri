from utils.dataverse_controller import DataverseController
import utils.constant as constant

def createDataverse(args):
	dv_filename = args.dataverse
	dataverse_controller = DataverseController(constant.base_url, constant.token)

	dataverse_controller.create_dataverse(dv_filename)