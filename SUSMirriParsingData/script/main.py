import sys
import argparse
import mainOperations.load_microorganisms as load_microorganisms

def loadMicroorganisms(params):
	parser = argparse.ArgumentParser(description="Load microorganisms from an excel file.")
	parser.add_argument('--excel', required=True, help='Excel file')
	parser.add_argument('--dataverse', required=True, help='Dataverse name')
	parser.add_argument('--base_url', required=True, help='Base URL')
	parser.add_argument('--token', required=True, help='Token')

	args = parser.parse_args(params)
	load_microorganisms.loadMicroorganisms(args)

if __name__ == "__main__":
	command = sys.argv[1] if len(sys.argv) > 1 else "help"
	params = sys.argv[2:]

	if command == "loadMicroorganisms":
		loadMicroorganisms(params)
	else:
		print('Command not found')