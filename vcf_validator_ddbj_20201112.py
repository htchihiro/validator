#!/usr/bin/env python

#検討中ここから
#def parser():
#$usage = "Usage: dbsnp_vcf_sub_validator.pl -file filename.gz -gi_list gi_list_file -skip_dense 1/0 -getseq_path path -genome_fasta path_to_fasta
#             (1 - skip density check
#              0 - check SNP density)
#ここまで

#-getseq_path GetSeqFromFasta.pl は固定にする？
# fastaは指定するようにするか、自由か

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
import re

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
vcf_data = open("vcfflile", "r") or die("Failed to open the VCF file")
a = 0

curr_chr = 0
previous_pos = 0

for line in vcf_data:
#    print(line)
	if line.startswith('##fileformat'): #vcfのバージョンをチェックする
		if re.search('4\.[1-3]$', line):
			a += 1
		else:
			sys.exit("ERROR 1.0.1: Illegal vcf version")
	elif line.startswith('##reference'):
		if line.search('path_to_fasta', line)
			a += 1
		else:
			sys.exit("ERROR 1.0.1: The entered fasta and the used fasta do not match")
	elif line.startswith('##INFO'):
		
	elif line.startswith('##FORMAT'):

	elif line.startswith('##FILTER'):
	
	elif line.startswith('##fileformat'):
	
	elif line.startswith('#header'): #headerが不正でないか確認する
		a += 1
		header_clm = line.split()
		if header_clm[0] == '#CHROM':
		else:
			sys.exit("ERROR 1.0.1: This vcf is not a standard format on #CHROM")
		if header_clm[1] == 'POS':
		else:
			sys.exit("ERROR 1.0.1: This vcf is not a standard format on POS")
		if header_clm[2] == 'ID':
		else:
			sys.exit("ERROR 1.0.1: This vcf is not a standard format on ID")
		if header_clm[3] == 'REF':
		else:
			sys.exit("ERROR 1.0.1: This vcf is not a standard format on REF")
		if header_clm[4] == 'ALT':
		else:
			sys.exit("ERROR 1.0.1: This vcf is not a standard format on ALT")
		if header_clm[5] == 'QUAL':
		else:
			sys.exit("ERROR 1.0.1: This vcf is not a standard format on QUAL")
		if header_clm[6] == 'FILTER':
		else:
			sys.exit("ERROR 1.0.1: This vcf is not a standard format on FILTER")
		if header_clm[7] == 'INFO':
		else:
			sys.exit("ERROR 1.0.1: This vcf is not a standard format on INFO")
	else:
		if a != 7: #body に入るときに項目が揃っているか確認する
			sys.exit("ERROR 1.0.1: Something is missing in ##")
		else:
				fields = line.split()
				chr_number = re.compile('\d+')
				chr = chr_number.findall(fields[0])0
				position = fields[1]
				if chr < curr_chr:
					sys.exit("ERROR 1.0.1: Chromosome position is larger then chromosome size")
				else:
					if not position.isdecimal():
						sys.exit("ERROR 1.0.1: positions should be numbers")
					else:
						pass
					if chr == curr_chr:
						if not position > previous_pos:
							sys.exit("ERROR 1.0.1: Data are not sorted base on positions")
						else:
							previous_pos = fields[1]
					else:
						curr_chr = fields[0]
						previous_pos = fields[1]



#CHRからINFOの前までの硬い部分のチェック

#INFOにしようされているタグが##と一致するか確認する

#実際のファイルとの比較をする

 
vcf_data.close() # 開いたファイルを閉じる
