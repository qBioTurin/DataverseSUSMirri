FROM qbioturin/dataversemanagement:dev

RUN pip3 install pandas
RUN pip3 install openpyxl

WORKDIR /

# copy data
COPY script /script_susmirriparsing

ENTRYPOINT ["python3", "/script_susmirriparsing/main.py"]