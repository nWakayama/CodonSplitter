# CodonSplitter

A tiny Python3 script to split a FASTA file into three new FASTA files.
You can use the script to codon separation for a protein coding region. 
Exported files inherit original file name and file extension.
When you designate a file named 'seq.fas', three files named as 'seq_1st.fas', 'seq_2nd.fas' and 'seq_3rd.fas' will be exported.

## Requirement
Python3


## Usage
1. When the script is started, a dialog to specify which file will open.
Multiple files can be selected using the shift key etc.
2. After a FASTA file is designated, three FASTA files are output into the same directory as the designated file.
Each output file contains characters positioned 1,4,7,10..., 2,5,8,11... and 3,6,9,12.... 


#### INPUT FILE:
FASTA format.  
Wrapped FASTA file is automatically unwrapped during the script running.
Any file extension or no extension can be used.

#### OUTPUT FILES:
Three FASTA format (unwrapped) files will be output into the same directory as the designated file.
The three files inherit the file name and extension from the designated file.
Furthermore, the codon position will be added as '_1st', '_2nd' and '_3rd' between original file name and extension.


#### Examples:
* ND4  `<- no file extension` 
    * ND4_1st  
    * ND4_2nd  
    * ND4_3rd    
    
* protein01_COI.txt  
    * protein01_COI_1st.txt
    * protein01_COI_2nd.txt
    * protein01_COI_3rd.txt
    
* ATP8_wrapped.fas
    * ATP8_wrapped_1st.fas
    * ATP8_wrapped_2nd.fas
    * ATP8_wrapped_3rd.fas
    
* wrapped_with_blank_line.FASTA  
    * wrapped_with_blank_line_1st.FASTA
    * wrapped_with_blank_line_2nd.FASTA
    * wrapped_with_blank_line_3rd.FASTA 



# License
This software is released under the MIT License.  
http://opensource.org/licenses/mit-license.php
