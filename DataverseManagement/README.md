# Dataverse Management

This software help admin users to manage harvard dataverse installation. To use the tool build the docker image with the following command:
```
docker build . -t dataversemanagement
```

### Create dataverse collection

To create a new dataverse collection you need to save a json file as dataverse.json with the following keys:
```
{
  "alias": "test",
  "name": "Test",
  "dataverseContacts": [{ "contactEmail": "test@info.com" }]
}
```

Subsequently, run the following command sharing a volume with this file with the container:
```
docker run -v path/to/json/dir:/data dataversemanagement createDataverse --dataverse /data/dataverse.json
```

### Create dataset

To create and upload a dataset its metadata json is needed. The format is as follow:
```
{
	"dataset_title": "title",
	"author_name": "author",
	"author_affiliation": "affilitation",
	"dataset_contact_name": "contact_name",
	"dataset_contact_email": "email@email.com",
	"dataset_description": "description",
	"subject": ["Medicine, Health and Life Sciences"]
}
```

Then use the following command:
```
docker run -v path/to/json/dir:/data dataversemanagement createDataset --dataverse DATAVERSE_NAME --json /data/metadata.json
```

If you need to upload files within the dataset, use the `--datafile_dir` parameter to specify the directory containing the files.

### Download datafile from dataset

To download metadata and any files associated with a dataset, use the following command:
```
docker run -v path/to/output/dir:/output dataversemanagement downloadDataset --DOI DOI --outdir /output
```

### Add datafile to dataset

To add a file from a dataset, place all your files in a directory and use the command:
```
docker run -v path/to/file/dir:/files dataversemanagement addDatafileToDataset --DOI DOI --datafile_dir /files
```

### Remove datafile from dataset

To remove a file from a dataset use the following command:
```
docker run dataversemanagement removeDatafileFromDataset --DOI DOI --file_name FILENAME
```