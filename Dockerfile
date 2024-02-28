
FROM alpine

RUN apk add --no-cache python3

ADD /Limerick-1.txt /home/data/Limerick-1.txt
ADD /IF.txt /home/data/IF.txt
ADD /scripts.py /home/scripts.py
RUN mkdir -p /home/output/
CMD ["/home/scripts.py"]
ENTRYPOINT ["python3"]