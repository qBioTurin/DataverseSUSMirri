import argparse
import mainOperations.create_dataverse as create_dataverse
import mainOperations.create_dataset as create_dataset
import mainOperations.download_dataset as download_dataset
import mainOperations.add_datafile_dataset as add_datafile_dataset
import mainOperations.remove_datafile_dataset as remove_datafile_dataset
import sys

def getDataverseInformation(parser):
    parser.add_argument('--token', required=False, help='Token for API access')
    parser.add_argument('--base_url', required=False, help='Base url of dataverse istance')
    return parser

def createDataverse(params):
    parser = argparse.ArgumentParser(description="Create a dataverse in a dataverse instance.")
    parser.add_argument('--dataverse', required=True, help='Dataverse Json file')
    
    args = parser.parse_args(params)
    create_dataverse.createDataverse(args)

def createDataset(params):
    parser = argparse.ArgumentParser(description="Extract data from a json file and create a dataset in a dataverse instance.")
    parser.add_argument('--json', required=True, help='Json file')
    parser.add_argument('--datafile_dir', required=False, help='Datafile directory')
    parser.add_argument('--dataverse', required=True, help='Dataverse name')
    parser = getDataverseInformation(parser)
    
    args = parser.parse_args(params)
    create_dataset.createDataset(args)
    
def downloadDataset(params):
	parser = argparse.ArgumentParser(description="Download a dataset from a dataverse instance.")
	parser.add_argument('--DOI', required=True, help='DOI of the dataset')
	parser.add_argument('--outdir', required=True, help='Datafile directory')
	
	args = parser.parse_args(params)
	download_dataset.downloadDataset(args)
    
def addDatafileToDataset(params):
	parser = argparse.ArgumentParser(description="Add file to a dataset.")
	parser.add_argument('--DOI', required=True, help='DOI of the dataset')
	parser.add_argument('--datafile_dir', required=True, help='Datafile directory')
	
	args = parser.parse_args(params)
	add_datafile_dataset.addDatafileToDataset(args)
     
def removeDatafileFromDataset(params):
	parser = argparse.ArgumentParser(description="Remove a file from a dataset.")
	parser.add_argument('--DOI', required=True, help='DOI of the dataset')
	parser.add_argument('--file_name', required=True, help='File name')
	
	args = parser.parse_args(params)
	remove_datafile_dataset.removeDatafileFromDataset(args)
	
if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else "help"
    params = sys.argv[2:]

    if command == "createDataverse":
        createDataverse(params)
    elif command == "createDataset":
        createDataset(params)
    elif command == "downloadDataset":
        downloadDataset(params)
    elif command == "addDatafileToDataset":
        addDatafileToDataset(params)
    elif command == "removeDatafileFromDataset":
        removeDatafileFromDataset(params)
    else:
        print("Command not found")
