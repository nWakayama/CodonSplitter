#!/usr/bin/python3

'''
Copyright (c) 2020 WAKAYAMA_Norio
This software is released under the MIT License.
http://opensource.org/licenses/mit-license.php
'''

import os, tkinter, tkinter.filedialog

def main():
        imported_files=open_files()
        for each_filename in imported_files:
                file_content=clean_fasta(each_filename)[0]
                file_content=file_content.split('\n')#change type str to list
                write_file(each_filename,file_content,'1st')
                write_file(each_filename,file_content,'2nd')
                write_file(each_filename,file_content,'3rd')

        
#open_files opens file selection dialog (python3)
def open_files():
        root=tkinter.Tk()
        root.withdraw()
        idir=os.path.expanduser('~')
        filenames=tkinter.filedialog.askopenfilenames(initialdir=idir)
        return filenames


#clean_fasta removes blank lines and make the data unwrapped
def clean_fasta(fasta_filename):
    fasta_content=''
    OTU_number=0
    with open(fasta_filename,'r') as f:
        for line in f:
            line=line.strip()
            if '>' in line:
                fasta_content=fasta_content+'\n'+line+'\n'
                OTU_number=OTU_number+1
            else:
                fasta_content=fasta_content+line#no use of '\n' allow connecting sequences 
    fasta_content=fasta_content.lstrip()#remove extra '\n' placed above the first OTU
    return fasta_content,OTU_number


#write_file exports 1/3 of the designated list data into FASTA file
def write_file(filename,content,codon):
       filenamecodon=os.path.splitext(os.path.basename(filename))[0],'_',codon,os.path.splitext(os.path.basename(filename))[1]
       startposition=int(codon[:-2])-1
       with open(''.join(filenamecodon),'w') as f:
              for line in content:
                     if '>' in line:
                            f.write(line+'\n')
                     else:
                            f.write(line[startposition::3]+'\n')


if __name__=='__main__':
        main()
        
