#!/usr/bin/env python

#def parser():
#$usage = "Usage: dbsnp_vcf_sub_validator.pl -file filename.gz -gi_list gi_list_file -skip_dense 1/0 -getseq_path path -genome_fasta path_to_fasta
#(1 - skip density check 0 - check SNP density)

#-getseq_path GetSeqFromFasta.pl

import argparse

parser = argparse.ArgumentParser(description='Validation tool for human genome vcffile') #Make parser

parser.add_argument('vcffile', help='Imput vcf file which you want to validate')
#parser.add_argument('gi_list_file', help='Imput gi list file') #Unnecessary?
#parser.add_argument('skip_dense', help='Enter 0 or 1') #Unnecessary?
parser.add_argument('fasta_for_validation', help='Imput fasta')

arge = parser.parse_args()

print('vcffile='+arge.vcffile)
#print('gi_list_file='+arge.gi_list_file)
#print('skip_dense='+arge.skip_dense)
print('fasta_for_validation='+arge.fasta_for_validation)

vcffile = arge.vcffile
#gi_list_file = arge.gi_list_file
#skip_dense = arge.skip_dense
fasta_for_validation = arge.fasta_for_validation

#Exist check of imput files or path

import os
import sys
import re
import subprocess
import linecache
import gzip
import codecs
import time

start_time = time.time()

vcf_exist = os.path.isfile(vcffile)
if vcf_exist:
	if os.path.getsize(vcffile) == 0:
		sys.exit("ERROR JV_VR0007: vcf file is empty")
	else:
		pass
else:
	sys.exit("ERROR JV_VR0008: vcf file is blank or not a file")

#gi_exist = os.path.isfile(gi_list_file)
#if gi_exist:
#	pass
#else:
#	sys.exit("ERROR 1.0.1: gi_list file is blank or not a file")

path_fasta_exist = os.path.isfile(fasta_for_validation)
if path_fasta_exist:
	pass
else:
	sys.exit("ERROR JV_VR0010: fasta file is blank or not a file")

#Cheking a imput score of skip_dense

#if int(skip_dense) in [0,1] :
#	pass
#else:
#	sys.exit("ERROR 1.0.1: skip_dense can be 0 or 1")

#Checking fasta
fasta_file = open(fasta_for_validation) or die("Failed to open the fasta file")
firstrow = fasta_file.readlines()[0]
if re.search('chr[0-9]+', firstrow):
	chr_marke = 1
else:
	chr_marke = 0

#for bcftools same as TogoVar

#comment out
#path_to_bcftools=/path/to/bcftools/

#${path_to_bcftools}bcftools norm -m - -o ${vcffile}.gz -O z --threads 32 ${vcffile} -f ${fasta_for_validation}

#normalized_vcf=${vcffile}.gz

#for validation

#Open vcfflile on read only
vcf_data = gzip.open(vcffile) or die("Failed to open the normalized-VCF file")
reader = codecs.getreader("utf-8")
vcf_lines = reader(vcf_data)

a = 0
b = 0

curr_chr = "0"
previous_pos = 0

#count of lines
line_numbers = 0

for line in vcf_lines:
#    print(line)
	line_numbers += 1
	if line.startswith('##fileformat'): #Checking VCF version
		if re.search('4\.[1-3]$', line):
			a += 1
			print("pass ##fileformat")
		else:
			print(str(line_numbers) + " WARNING JV_VR0012: Illegal vcf version")
	elif line.startswith('##fileDate'):
		#import datetime
		#tomorrow = str(datetime.date.today() + datetime.timedelta(days=1))
		#filedate = str(re.sub("\\D", "", line))
		#if datetime.datetime.strptime(tomorrow, '%Y-%m-%d').strftime("%Y%m%d") > datetime.datetime.strptime(filedate, '%Y%m%d').strftime("%Y%m%d"): #Future filedate is ellegal
			a += 1
			print("pass ##fileDate")
		#else:
		#	print("WARNING 1.0.1: Illegal vcf file date")
	elif line.startswith('##reference'):
		fasta_name=os.path.basename(fasta_for_validation)
		if re.search(fasta_name, line):
			a += 1
			print("pass ##reference")
		else:
			print(str(line_numbers) + " WARNING JV_VR0014: The entered fasta and the used fasta do not match")
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
			print(str(line_numbers) + " WARNING JV_VR0015: This vcf is not a standard format on CHROM")
		if header_clm[1] == 'POS':
			b += 1
		else:
			print(str(line_numbers) + " WARNING JV_VR0016: This vcf is not a standard format on POS")
		if header_clm[2] == 'ID':
			b += 1
		else:
			print(str(line_numbers) + " WARNING JV_VR0017: This vcf is not a standard format on ID")
		if header_clm[3] == 'REF':
			b += 1
		else:
			print(str(line_numbers) + " WARNING JV_VR0018: This vcf is not a standard format on REF")
		if header_clm[4] == 'ALT':
			b += 1
		else:
			print(str(line_numbers) + " WARNING JV_VR0019: This vcf is not a standard format on ALT")
		if header_clm[5] == 'QUAL':
			b += 1
		else:
			print(str(line_numbers) + " WARNING JV_VR0020: This vcf is not a standard format on QUAL")
		if header_clm[6] == 'FILTER':
			b += 1
		else:
			print(str(line_numbers) + " WARNING JV_VR0021: This vcf is not a standard format on FILTER")
		if header_clm[7] == 'INFO':
			b += 1
		else:
			print(str(line_numbers) + " WARNING JV_VR0022: This vcf is not a standard format on INFO")
	elif line.startswith('##'):
			pass
	else:
		if a != 4 or b != 8: #Number of header items completery collected or not
			print(a)
			print(b)
			sys.exit(str(line_numbers) + "ERROR JV_VR0023: Something is missing in header")
		else:
				fields = line.split()
				chr_number = fields[0]
				chr = str(chr_number.replace('chr', ''))
				if not re.match("(\d+|X|Y)", chr):
						print(str(line_numbers) + " WARNING JV_VR00XX: Chromosome numbers should be UCSC format ('chr' + number or 'chrX' or 'chrY') or Ensembl format (number or 'X' or 'Y')")
				if chr.isdigit() and curr_chr.isdigit():
					if int(chr) < int(curr_chr):
						print(str(line_numbers) + " WARNING JV_VR0025: Chromosome numbers were not sorted")
				elif chr < curr_chr:
						print(str(line_numbers) + " WARNING JV_VR0025: Chromosome numbers were not sorted")
				position = str(fields[1])
				if not position.isdigit():
						print(str(line_numbers) + " WARNING JV_VR0024: positions should be numbers")
				if chr == curr_chr:
					if str(position).isdigit() and str(previous_pos).isdigit() and (int(position) < int(previous_pos)):
						print ("previous:" + position)
						print ("now:" + previous_pos)
						print(str(line_numbers) + " WARNING JV_VR0026: Data are not sorted base on positions")
					else:
						previous_pos = fields[1]
				curr_chr = chr
				previous_pos = fields[1]
				if fields[3] == fields[4]:
					print(str(line_numbers) + " WARNING JV_VR0027: Reference allele and alternative alleles are the same")
				if re.search('[^ATGC]', fields[3]): #REF is only allowed for AGCT
					if re.search('[MRWSYKVHDBN]', fields[3]) :
						print(str(line_numbers) + " WARNING JV_VR0028: No non-ATGC nucleotide or iupac ambiguity codes (ie. R, Y, etc.) are in either reference alleles")
					elif fields[3] == "\." or fields[3] == "-": #Some submitter use "-" for Insertion
						print(str(line_numbers) + " WARNING JV_VR0029: This vcf file uses - or . for reference colum")
					else:
						print(str(line_numbers) + " WARNING JV_VR0030: Illegal characters are used in reference allele")
					if len(fields[4]) > 50:
						print(str(line_numbers) + " WARNING JV_VR0031: Insertion size is over 50bp")
					else:
						pass
						#move_position = 1 #If we need to fix vcf files for standerd, add correction steps
						#new_position = fields[2] - 1
						#ref_bed = print ( chr"\t"new_position-1"\t"new_position)
						#bedtools getfasta -fi $fasta_file -bed $ref_bed -fo ref_out
						#output_bedtools = open( ref_out ) or die("Failed to open the output file of bedtools")
						#for fasta_nuc in output_bedtools:
						#	if line.startswith('>'): #skip headder
						#		pass
						#	else:
						#		fields[3] = fasta_nuc
						#		new_alt = fasta_nuc + fields[4]
						#		fields[4] = new_alt
						#ref_out.close()
						#rm ref_out					
				elif len(fields[3]) == 0 : #ref allele missing
					print(str(line_numbers) + " WARNING JV_VR0032: Reference allele missing")
				else:
					if len(fields[3]) > len(fields[4]): #For deletion cases
						back_one = int(fields[1]) + int(len(fields[3])) - 1
					else:
						back_one = int(fields[1])
					prev_one = int(fields[1]) - 1
					ref_bed = open('ref_bed.bed','w')
					if chr_marke == 1 :
						ref_bed.write("chr"+str(chr)+"\t"+str(prev_one)+"\t"+str(back_one))
					else:
						ref_bed.write(str(chr)+"\t"+str(prev_one)+"\t"+str(back_one))
					ref_bed.close()
					cmd = "bedtools getfasta -fi "+str(fasta_for_validation)+" -bed ref_bed.bed -fo ref_out.bed"
					subprocess.call(cmd.split())
					output_bedtools = open( "ref_out.bed" ) or die("Failed to open the output file of bedtools")
					for fasta_nuc in output_bedtools:
						if re.search('>', fasta_nuc): #skip headder
							pass
						else:
							fn_search = re.search(r'([ATGC]+)', fasta_nuc)
							fn_ex = fn_search.group()
							if str(fields[3]) != str(fn_ex):
								print(str(line_numbers) + "_vcf:" +str(fields[3]) + "_ref:" +str(fn_ex) + " WARNING JV_VR0033: Dosen't match reference allele")
					ref_bed = ""
				if re.search('[^ATGC]', fields[4]) : #ALT is only allowed for AGCT
					if re.search('[MRWSYKVHDBN]', fields[4]) :
						print(str(line_numbers) + " WARNING JV_VR0034: No non-ATGC nucleotide or iupac ambiguity codes (ie. R, Y, etc.) are in alternative alleles")
					elif fields[4] == "\." or fields[4] == "-": #Some submitter use "-" for Deletion
						print(str(line_numbers) + " WARNING JV_VR0035: This vcf file uses - or . for alternative colum")
					if re.search(',', fields[4]) : #For multi-allelic
						print(str(line_numbers) + " WARNING JV_VR0036: Please sepalate the multi-allelic")
					else:
						print(str(line_numbers) + " WARNING JV_VR0037: Illegal characters are used in alternative allele")
					if len(fields[3]) > 50:
						print(str(line_numbers) + " WARNING JV_VR0038: Deletion size is over 50bp")
                        #move_position = 1 #If we need to fix vcf files for standerd, add correction steps
						#new_position = fields[2] - 1
						#ref_bed = print ( chr"\t"new_position-1"\t"new_position)
						#bedtools getfasta -fi $fasta_file -bed $ref_bed -fo ref_out
						#output_bedtools = open( ref_out ) or die("Failed to open the output file of bedtools")
						#for fasta_nuc in output_bedtools:
						#	if line.startswith('>'): #skip headder
						#		pass
						#	else:
						#		fields[4] = fasta_nuc
						#		new_ref = fasta_nuc + fields[3]
						#		fields[3] = new_ref
						#ref_out.close()
						#rm ref_out
				if len(fields[4]) == 0 : #alt allele missing
					print(str(line_numbers) + " WARNING JV_VR0039: Alternative allele missing")
else:
	print (str(line_numbers) + " All lines of vcf were validated! Please check errors and/or warnings in the log file")

elapsed_time = time.time() - start_time
print (f'elapsed_time: {int(elapsed_time)} sec')
vcf_data.close()