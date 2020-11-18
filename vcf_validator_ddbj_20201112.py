#!/usr/bin/env python

#検討中ここから
#import sys

#def parser():
#$usage = "Usage: dbsnp_vcf_sub_validator.pl -file filename.gz -gi_list gi_list_file -skip_dense 1/0 -getseq_path path -genome_fasta path_to_fasta
#             (1 - skip density check
#              0 - check SNP density)
#ここまで

#-getseq_path GetSeqFromFasta.pl は固定する

import argparse #Import argparse

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

vcf_exist = os.path.isfile(vcffile)
if vcf_exist:
	pass
else:
	sys.exit("vcf file is empty or not a file")

gi_exist = os.path.isfile(gi_list_file)
if gi_exist:
	pass
else:
	sys.exit("gi list file is empty or not a file")

path_fasta_exist = os.path.isdir(path_to_fasta)
if path_fasta_exist:
	pass
else:
	sys.exit("path is empty or not a directory")

#Cheking a imput score of skip_dense

if skip_dense = 0 or skip_dense = 1:
	pass
else:
	print("skip_dense can be 0 or 1")

# Open vcfflile on read only
vcf_data = open("vcfflile", "r")

for line in vcf_data:
#    print(line)
	if line.startswith('##'): #vcfの##を取得して保管する
		if line.startswith('##fileformat'): #vcfのバージョンをチェックする
			if re.search('4\.[1-3]$', line):
				pass
			else:
				sys.exit("Illegal vcf version")

	elif line.startswith('#header'):

#headerが不正でないか確認する

#CHRからINFOの前までの硬い部分のチェック

#INFOにしようされているタグが##と一致するか確認する

#実際のファイルとの比較をする








 
# 読み込んだテキストファイルを１行ずつ表示

 
# 開いたファイルを閉じる
file_data.close()