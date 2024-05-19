import argparse
import mainOperations.create_dataverse as create_dataverse
import mainOperations.create_dataset as create_dataset
import mainOperations.download_dataset as download_dataset
import sys

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
    
    args = parser.parse_args(params)
    create_dataset.createDataset(args)
    
def downloadDataset(params):
	parser = argparse.ArgumentParser(description="Download a dataset from a dataverse instance.")
	parser.add_argument('--DOI', required=True, help='DOI of the dataset')
	parser.add_argument('--outdir', required=True, help='Datafile directory')
	
	args = parser.parse_args(params)
	download_dataset.downloadDataset(args)
	

if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else "help"
    params = sys.argv[2:]

    if command == "createDataverse":
        createDataverse(params)
    elif command == "createDataset":
        createDataset(params)
    elif command == "downloadDataset":
        downloadDataset(params)
    else:
        print("Command not found")
