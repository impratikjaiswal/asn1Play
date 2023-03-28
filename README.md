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
<li>Auto Trimming of HEX Data (White Spaces Deletion).
<li>Auto Detection of Base64 & Hex data.
<li>Conversion Mode for HEX, ASCII & Base64.
<li>Support of Individual Mode; Raw/Target Data can be configured Directly or file path (Binary as well as Text File; any extension) can be passed.
<li>Support of Bulk Mode; Raw/Target Data can be configured Directly in List/Array format or Directory Path can be passed (Files with Known extensions will be picked based on Input Format).
<li>For Known File Extensions (".asn1", ".asn", ".base64", ".hex"), Input/Output Format may be modified automatically as per Default Values.
</ul>