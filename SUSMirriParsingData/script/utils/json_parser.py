import json


def parseJson(microorganism):
    data = {"dataset_title": f"{microorganism['accessionNumber']}", "author_name": "SUS-MIRRI.IT", "author_affiliation": "Dept. Computer Science", "dataset_contact_name": "SUS-MIRRI.IT", "dataset_contact_email": "email@email.com", "dataset_description": f"{microorganism['accessionNumber']}", "subject": ["Medicine, Health and Life Sciences"],
            "metadatablocks": [
        {
            "display_name": "UNITO Metadata",
            "name": "unito",
            "fields": [
                {
                    "typeName": "ERC",
                    "value": "SH1_1 Macroeconomics; monetary economics; economic growth",
                    "multiple": False,
                    "typeClass": "controlledVocabulary"
                }
            ]
        },
        {
            "display_name": "UNITO Projects Metadata",
            "name": "unitoProjects",
            "fields": [
                {
                    "typeName": "susmirri",
                    "multiple": False,
                    "typeClass": "compound",
                    "value": {
                        "accessionNumberSUSMirri": {
                            "typeName": "accessionNumberSUSMirri",
                            "multiple": False,
                            "typeClass": "primitive",
                            "value": f"{microorganism['accessionNumber']}"
                        }
                    }
                }
            ]
        }
    ]}
    
    with open(f'/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
