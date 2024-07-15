# SUSMirri Parsing Data

This software parses data from SUSMirri Excel file to the json needed by Dataverses. To use the tool build the docker image with the following command:
```
docker build . -t susmirriparsingdata
```

### Load Microorganisms
To load all the microorganisms in an excel file you should use the following command:
```
docker run -v /path/to/excel:/data susmirriparsingdata loadMicroorganisms --excel /data/EXCEL_NAME --dataverse DATAVERSE_COLLECTION --base_url BASE_URL_DATAVERSE_INSTANCE --token TOKEN_API
```