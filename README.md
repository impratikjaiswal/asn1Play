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
<li>Currently Scripts are targeting virtual environment with folder name as <i>venv</i> (Present in parallel of <i>scripts</i> folder)

However, same can be modified as per user choice. 
</ol>
<li>Note: installing tool in virtual environment is optional but preferred.
</ol>

# Few Features 
<ul>
<li>Auto Trimming of HEX Data (White Spaces Deletion).
<li>Auto Detection of Base64 & Hex data.
<li>Conversion Mode for HEX, ASCII & Base64.
<li>Support of "Individual Mode"; Raw/Target Data can be configured Directly or file path (Binary as well as Text File; any extension) can be passed.
<li>Support of "Bulk Mode"; Raw/Target Data can be configured Directly in List/Array format or Directory Path can be passed (Files with Known extensions will be picked based on Input Format).
<li>Support of "Config Mode"; Raw/Target Data (along with all needed config) can be configured Directly in Yaml Files (".yaml" or ".yml" extensions), and same cane be passed in "Individual Mode" or "Bulk Mode".
<li>For Known File Extensions (".asn1", ".asn", ".base64", ".hex"), Input/Output Format may be modified automatically as per Default Values.
</ul>

# Sampledata Folder (\asn1Play\SampleData)
<ul>
<li>Sample Data folder contains version specific files.
<li>"$VERSION" keyword can be used to generate file path on run time. (Refer: "\asn1Play\src\main\data_type\store_metadata_request.py")
</ul>

# Important Points
<ul>
<li>For output_file, Both "directory path" and "file path" (identified based on any extension) are supported, Hence a path without extension will be considered as directory. 
<li>For input/output via files/directory, always enclosed path with r''. Here "r" denotes raw string and avoid escape sequences.
</ul>

# Reserve Keywords
<ul>
<li>$VERSION
<ul>
<li>Used for input_path, when version of asn specification needs to be considered in path.
</ul>
<li>$REMARKS
<ul>
<li>Used for output_path, when Remarks needs to be considered in output path.
</ul>
<li>output
<ul>
<li>Used for output in file.
</ul>
<li>export
<ul>
<li>Used for export mode. Export of configuration in .yml file.
</ul>
</ul>
