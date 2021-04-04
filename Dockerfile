FROM python:alpine

LABEL author=joez

RUN python3 -m pip install xlsxwriter

COPY schulte-table.py /usr/bin
RUN chmod a+x /usr/bin/schulte-table.py

RUN mkdir -p -m 777 /work
VOLUME ["/work"]
WORKDIR /work

ENTRYPOINT ["schulte-table.py"]