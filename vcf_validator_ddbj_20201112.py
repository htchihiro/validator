#!/usr/bin/env python

#検討中ここから
#def parser():
#$usage = "Usage: dbsnp_vcf_sub_validator.pl -file filename.gz -gi_list gi_list_file -skip_dense 1/0 -getseq_path path -genome_fasta path_to_fasta
#             (1 - skip density check
#              0 - check SNP density)
#ここまで

#-getseq_path GetSeqFromFasta.pl は固定にする？

import argparse

parser = argparse.ArgumentParser(description='Validation tool for human genome vcffile') #Make parser

parser.add_argument('vcffile', help='Imput vcf file which you want to validate')
parser.add_argument('gi_list_file', help='Imput gi list file')
parser.add_argument('skip_dense', help='Enter 0 or 1')
parser.add_argument('path_to_fasta', help='Write down the path to fasta')

arge = parser.parse_args()

print('vcffile='+args.vcffile)
print('gi_list_file='+args.gi_list_file)
print('skip_dense='+args.skip_dense)
print('path_to_fasta='+args.path_to_fasta)

#Exist check of imput files or path

import os
import sys

vcf_exist = os.path.isfile(vcffile)
if vcf_exist:
	line_cnt = sum([1 for _ in open('sample.txt')])
	if $line_cnt == 1:
		sys.exit("ERROR 1.0.1: vcf file is empty")
	else:
		pass
else:
	sys.exit("ERROR 1.0.1: vcf file is blank or not a file")

gi_exist = os.path.isfile(gi_list_file)
if gi_exist:
	pass
else:
	sys.exit("ERROR 1.0.1: gi_list file is blank or not a file")

path_fasta_exist = os.path.isfile(path_to_fasta)
if path_fasta_exist:
	pass
else:
	sys.exit("ERROR 1.0.1: fasta file is blank or not a file")

#Cheking a imput score of skip_dense

if skip_dense = (0|1) :
	pass
else:
	sys.exit("ERROR 1.0.1: skip_dense can be 0 or 1")

# Open vcfflile on read only
vcf_data = open("vcfflile", "r")

for line in vcf_data:
#    print(line)
	if line.startswith('##fileformat'): #vcfのバージョンをチェックする
		if re.search('4\.[1-3]$', line):
			pass
		else:
			sys.exit("ERROR 1.0.1: Illegal vcf version")
	if line.startswith('##reference'):
		if line.search('path_to_fasta', line)
			pass
		else:
			sys.exit("ERROR 1.0.1: The entered fasta and the used fasta do not match")
	if line.startswith('##INFO'):
		
	if line.startswith('##FORMAT'):

	if line.startswith('##FILTER'):
	
	if line.startswith('##fileformat'):
	
	if line.startswith('#header'): #headerが不正でないか確認する
		header_clm = line.split()
		if header_clm[0] == '#CHROM':
			pass
		else:
			sys.exit("ERROR 1.0.1: This vcf is not a standard format on #CHROM")
		if header_clm[1] == 'POS':
			pass
		else:
			sys.exit("ERROR 1.0.1: This vcf is not a standard format on POS")
		if header_clm[2] == 'ID':
			pass
		else:
			sys.exit("ERROR 1.0.1: This vcf is not a standard format on ID")
		if header_clm[3] == 'REF':
			pass
		else:
			sys.exit("ERROR 1.0.1: This vcf is not a standard format on REF")
		if header_clm[4] == 'ALT':
			pass
		else:
			sys.exit("ERROR 1.0.1: This vcf is not a standard format on ALT")
		if header_clm[5] == 'QUAL':
			pass
		else:
			sys.exit("ERROR 1.0.1: This vcf is not a standard format on QUAL")
		if header_clm[6] == 'FILTER':
			pass
		else:
			sys.exit("ERROR 1.0.1: This vcf is not a standard format on FILTER")
		if header_clm[7] == 'INFO':
			pass
		else:
			sys.exit("ERROR 1.0.1: This vcf is not a standard format on INFO")
		if header_clm[8] == 'FORMAT':
			pass
		else:
			sys.exit("ERROR 1.0.1: This vcf is not a standard format on FORMAT")

#body
#CHRからINFOの前までの硬い部分のチェック

#INFOにしようされているタグが##と一致するか確認する

#実際のファイルとの比較をする

 
vcf_data.close() # 開いたファイルを閉じる
