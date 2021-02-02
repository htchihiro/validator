FROM python:3.9.0

RUN mkdir /opt/bedtools && \
    cd /opt/bedtools && \
    wget "https://github.com/arq5x/bedtools2/releases/download/v2.30.0/bedtools-2.30.0.tar.gz" && \
    tar -zxvf bedtools-2.30.0.tar.gz && \
    cd bedtools2 && \
    make
ENV PATH $PATH:/opt/bedtools/bedtools2/bin

RUN mkdir /opt/bcftools && \
    cd /opt/bcftools && \
    wget "https://github.com/samtools/bcftools/releases/download/1.11/bcftools-1.11.tar.bz2" && \
    tar -jxvf bcftools-1.11.tar.bz2 && \
    cd bcftools-1.11 && \
    ./configure --prefix=/opt/bcftools/bcftools && \
    make && \
    make install

ENV PATH $PATH:/opt/bcftools/bcftools/bin

RUN mkdir /data
RUN mkdir /log
WORKDIR /app
