#!/usr/bin/env python

#def parser():
#$usage = "Usage: dbsnp_vcf_sub_validator.pl -file filename.gz -gi_list gi_list_file -skip_dense 1/0 -getseq_path path -genome_fasta path_to_fasta
#(1 - skip density check 0 - check SNP density)

#-getseq_path GetSeqFromFasta.pl

import argparse

parser = argparse.ArgumentParser(description='Validation tool for human genome vcffile') #Make parser

parser.add_argument('vcffile', help='Imput vcf file which you want to validate')
parser.add_argument('gi_list_file', help='Imput gi list file')
parser.add_argument('skip_dense', help='Enter 0 or 1')
parser.add_argument('fasta_for_validation', help='Imput fasta')

arge = parser.parse_args()

print('vcffile='+arge.vcffile)
print('gi_list_file='+arge.gi_list_file)
print('skip_dense='+arge.skip_dense)
print('fasta_for_validation='+arge.path_to_fasta)

vcffile = arge.vcffile
gi_list_file = arge.gi_list_file
skip_dense = arge.skip_dense
fasta_for_validation = arge.fasta_for_validation

#Exist check of imput files or path

import os
import sys
import re

vcf_exist = os.path.isfile(vcffile)
if vcf_exist:
	line_cnt = sum([1 for _ in open(vcffile)])
	if line_cnt == 1:
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

path_fasta_exist = os.path.isfile(fasta_for_validation)
if path_fasta_exist:
	pass
else:
	sys.exit("ERROR 1.0.1: fasta file is blank or not a file")

#Cheking a imput score of skip_dense

if int(skip_dense) in [0,1] :
	pass
else:
	sys.exit("ERROR 1.0.1: skip_dense can be 0 or 1")

#Checking fasta
fasta_file = open(fasta_for_validation) or die("Failed to open the fasta file")

#for bcftools same as TogoVar

path_to_bcftools=/path/to/bcftools/

${path_to_bcftools}bcftools norm -m - -o ${vcffile}.gz -O z --threads 32 ${vcffile} -f ${fasta_for_validation}

normalized_vcf=${vcffile}.gz

#for validation

#Open vcfflile on read only
vcf_data = open(normalized_vcf) or die("Failed to open the normalized-VCF file")

a = 0
b = 0

curr_chr = 0
previous_pos = 0

#Open fasta on read only and storing
fasta_data = open(fasta_for_validation) or die("Failed to open the fasta") #染色体ごとに格納するようにするhedder名の変数に次の行の配列を格納したい$[data_$[hedder]][seqence]

fasta_line = [""]

for f in fasta_data:
	if f.startswith('>'):
		fasta_line.append($f)
		next #次の行を読み込む処理を入れる
		fasta_line.appned($next_f)

#偶数はヘッダー、奇数は塩基配列となるはず？？

for line in vcf_data:
#    print(line)
	if line.startswith('##fileformat'): #Checking VCF version
		if re.search('4\.[1-3]$', line):
			a += 1
			print("pass ##fileformat")
		else:
			print("WARNING 1.0.1: Illegal vcf version")
	elif line.startswith('##fileDate'):
		import datetime
		tomorrow = str(datetime.date.today() + datetime.timedelta(days=1))
		filedate = str(re.sub("\\D", "", line))
		if datetime.datetime.strptime(tomorrow, '%Y-%m-%d').strftime("%Y%m%d") > datetime.datetime.strptime(filedate, '%Y%m%d').strftime("%Y%m%d"): #Future filedate is ellegal
			a += 1
			print("pass ##filedate")
		else:
			print("WARNING 1.0.1: Illegal vcf file date")
	elif line.startswith('##reference'):
		if re.search(path_to_fasta, line):
			a += 1
			print("pass ##reference")
		else:
			print("WARNING 1.0.1: The entered fasta and the used fasta do not match")
	elif line.startswith('##INFO'): #later add
		pass
	elif line.startswith('##FORMAT'): #later add
		pass
	elif line.startswith('##FILTER'): #later add
		pass
	elif re.search('#CHROM',line): #header is illegal or not
		a += 1
		header_clm = line.split()
		print("pass #header")
		if header_clm[0] == '#CHROM':
			b += 1
		else:
			print(header_clm[0])
			print("WARNING 1.0.1: This vcf is not a standard format on CHROM")
		if header_clm[1] == 'POS':
			b += 1
		else:
			print("WARNING 1.0.1: This vcf is not a standard format on POS")
		if header_clm[2] == 'ID':
			b += 1
		else:
			print("WARNING 1.0.1: This vcf is not a standard format on ID")
		if header_clm[3] == 'REF':
			b += 1
		else:
			print("WARNING 1.0.1: This vcf is not a standard format on REF")
		if header_clm[4] == 'ALT':
			b += 1
		else:
			print("WARNING 1.0.1: This vcf is not a standard format on ALT")
		if header_clm[5] == 'QUAL':
			b += 1
		else:
			print("WARNING 1.0.1: This vcf is not a standard format on QUAL")
		if header_clm[6] == 'FILTER':
			b += 1
		else:
			print("WARNING 1.0.1: This vcf is not a standard format on FILTER")
		if header_clm[7] == 'INFO':
			b += 1
		else:
			print("WARNING 1.0.1: This vcf is not a standard format on INFO")
	elif line.startswith('##'):
			pass
	else:
		if a != 4 or b != 8: #Number of header items completery collected or not
			print(a)
			print(b)
			sys.exit("ERROR 1.0.1: Something is missing in header")
		else:
				fields = line.split()
				chr_number = fields[0]
				chr = str(chr_number.replace('chr', ''))
				position = str(fields[1])
				if chr < curr_chr:
					print("WARNING 1.0.1: Chromosome position is larger then chromosome size")
				else:
					if not position.isdigit():
						print("WARNING 1.0.1: positions should be numbers")
					else:
						pass
					if chr == curr_chr:
						if position < previous_pos:
							print (position)
							print (previous_pos)
							print("WARNING 1.0.1: Data are not sorted base on positions")
						else:
							previous_pos = fields[1]
					else:
						curr_chr = chr
						previous_pos = fields[1]
				if fields[3] == fields[4]:
					print("WARNING 1.0.1: Reference allele and alternative alleles are the same")
				if re.search('[^ATGC]', fields[3]): #REF is only allowed for AGCT
					if fields[3] == "\." or fields[3] == "-": #Some submitter use "-" for Insertion
						move_position = 1
						new_position = fields[2] - 1
						fasta_nuc = #fastaから読み込んできた塩基
						fields[3] = fasta_nuc #fastaから取得した-1ポジションの塩基を入れる
						new_alt = fasta_nuc + fields[4] #fastaから取得した-1ポジションの塩基をもともとの塩基の前に追加する必要がある
						fields[4] = new_alt
					else:
						print("WARNING 1.0.1: Illegal characters are used in reference allele")
				elif len(fields[3]) == 0 : #ref allele missing
					print("WARNING 1.0.1: Reference allele missing")
				else:
					pass
				if re.search('[^ATGC]', fields[4]) : #ALT is only allowed for AGCT
					if fields[4] == "\." or fields[4] == "-": #Some submitter use "-" for Deletion
						move_position = 1
						fields[2] = fields[2] - 1
						fasta_nuc =
                                                new_ref = fasta_nuc + fields[3] #fastaから取得した-1ポジションの塩基をもともとの塩基の前に追加する必要がある
                                                fields[3] = new_ref
                                                fields[4] = fasta_nuc #fastaから取得してきた-1ポジションの塩基を入れる
						#hit_line = [fasta_line for fasta_line in fasta_file if fields[2] in fasta_line]
						#split_hit_line = hit_line.split()
						#add_allele = split_hit_line[]
					else:
						print("WARNING 1.0.1: Illegal characters are used in alternative allele")
				elif len(fields[4]) == 0 : #alt allele missing
					print("WARNING 1.0.1: Alternative allele missing")
				else:
					pass
		if move_position = 0
			re.serch(field[0], fasta_line) #対応する染色体番号の配列部分を呼び出したい
			contig[fields[2]]
			if field[4] == fasta_data[field[2]]: #ポジションが一致するか
				pass
			else:
				print( filed[4] "dosen't match reference allele")
		else:
			pass

vcf_data.close()

#candidate of error

#";ERR_LINE_EMPTY=Line is empty"
#";ERR_VRT_NOT_DEFINED=variation type not defined"
#";ERR_CHR_NOT_GROUPED=Data on the same chromosome are not grouped together"
#";ERR_CHR=invalid chromosome name"
#";ERR_VARI_LENGTH_INDEL=Indels with variable length alleles"
#";ERR_DUP_SITES=Duplicated sites"
#";ERR_SPACE_REF=Extra space before/after ref. allele"


#	    if((substr($alleles[$i], 0, 1) ne substr($fields[3], 0, 1)) && (length($fields[3]) > 1 || length($alleles[$i]) > 1)) {
#		$current_line_error = 1;
#		$self->{result}->{ERR}->{ERR_INVALID_INDEL_MNV_FMT}->{counter}++;
#		$line .= ";ERR_INVALID_INDEL_MNV_FMT=Ref and alt alleles don not have common leading base";
#	    }
