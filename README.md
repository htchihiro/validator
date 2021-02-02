# Validator
VCF Validator

## Dependency

### Docker
docker client & docker-compoase

## Setup
### Docker
Generate .env file from template file and edit .env file with the values appropriate for your environment.
```
$ cp template.env .env
```
container build & start
```
$ docker-compose up -d
```

## Usage
### data
Prepare the input file, and place it under the data directory so that it can be accessed by the docker container.
It can be located anywhere under the data directory.
```
$ mkdir data/input_file/
$ cp /your/path/file.vcf data/input_file/
$ cp /your/path/reference.fasta data/input_file/
$ cp /your/path/reference.fasta.fai data/input_file/ # if available
```

### execute
```
$ docker-compose exec ddbj_vcf_validator python vcf_validator_ddbj.py /data/input_files/test1-SNV.vcf /data/input_files/chr9.fa
$ docker-compose exec ddbj_vcf_validator bcftools norm -m -  -o /data/input_files/test1-SNV.vcf.gz -O z --threads 4 /data/input_files/test1-SNV.vcf -f /data/input_files/chr9.fa
```
