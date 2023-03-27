# asn1play

<BR>ASN1 Encoder &amp; Decoder based on pycrate.
<BR>Currently supporting all versions of (By Default):
<ol>
<li>GSMA SGP.22
<li>TCA eUICC_Profile_Package (SAIP)
</ol>
<BR> However, Tool can be extended to support any ASN1 based conversion.

# How To Install 
<ol>
<li>All Required packages are listed in requirements.txt
<li>Few Basic Scripts are also present under <i>scripts</i> folder.
<ol>
<li>Currently Scripts are targeting virtual environment with folder name as <i>.venv</i> (Present in parallel of <i>scripts</i> folder)

However, same can be modified as per user choice. 
</ol>
<li>Note: installing tool in virtual environment is optional but preferred.
</ol>

# Few Features 
<ul>
<li>Auto Trimming of HEX Data (White Spaces Deletion) 
<li>Auto Detection of Base64 & its conversion
<li>Conversion Mode for HEX, ASCII & Base 64
<li>Input Data can be provided in file (Binary as well as Text; any extension) OR List OR inline.
<li>If input file extension is ".asn1", then default input/output formats will be used (if not defined).
</ul>

".asn1"