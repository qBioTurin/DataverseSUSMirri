# DataverseSUSMirri

## Metadata Customisation
Copy the metadatablock file that you want to add in your Dataverse installation into the data/metadablock directory of Dataverse. Here use the following command:
```
curl http://localhost:8080/api/admin/datasetfield/load -H "Content-type: text
tab-separated-values" -X POST --upload-file $FILE_NAME
```
Then update the Solr schema.xml file stored in the Dataverse root directory:
```
curl "http://localhost:8080/api/admin/index/solr/schema" | bash update-fields.sh schema.xml
```

In the machine which has solr installed:
```
scp $DATAVERSE_MACHINE:/dataverse/dvinstall/schema.xml /dataverseDB/solr/solr-9.3.0/server/solr/collection1/conf/schema.xml 
curl "http://localhost:8983/solr/admin/cores?action=RELOAD&core=collection1" | jq
```