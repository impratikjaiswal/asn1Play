# asn1play

<BR>ASN1 Encoder &amp; Decoder based on [pycrate](https://github.com/P1sec/pycrate).
<BR>Currently supporting various versions of:
1. [GSMA SGP.22](https://www.gsma.com/esim/esim-specification/ "GSMA SGP.22" )
2. [TCA eUICC_Profile_Package (SAIP)](https://trustedconnectivityalliance.org/technology-library-sim-specifications/ "SAIP")

<BR>However, Tool can be extended to support any ASN1 based conversion.

# How To Install

<ol>
    <li>All Required packages are listed in requirements.txt
    <li>Few Basic Scripts are also present under <i>scripts</i> folder.
    <ol>
        <li>Currently, Scripts are targeting virtual environment with folder name as <i>venv</i> (Present in parallel of <i>scripts</i> folder)
        However, same can be modified as per user choice.
    </ol>
    <li>Note: installing tool in virtual environment is optional but preferred.
</ol>

# How To Use
<ul>
<li>Web server can be locally started using <i>scripts/flask_server_start.bat</i>
<li>or alternatively code can be used directly from <i>asn1Play/src/main/asn1play.py</i>
</ul>

# Few Major Features

<ul>
    <li>Auto Trimming of HEX Data (White Spaces Deletion).
    <li>Auto Detection of Base64 & Hex data.
    <li>Auto Detection of ByteArraySigned & ByteArrayUnSigned.
    <li>Conversion Mode for HEX, ASCII & Base64.
    <li>Support of "Individual Mode"; Raw/Target Data can be configured Directly or file path (Binary as well as Text File; any extension) can be passed.
    <li>Support of "Bulk Mode"; Raw/Target Data can be configured Directly in List/Array format or Directory Path can be passed (Files with Known extensions will be picked based on Input Format).
    <li>Support of "Yml Mode (Config Mode)"; Raw/Target Data (along with all needed config) can be configured Directly in Yaml Files (".yaml" or ".yml" extensions), and same cane be passed in "Individual Mode" or "Bulk Mode".
    <li>For Known File Extensions (".asn1", ".asn", ".base64", ".hex"), Input/Output Format may be modified automatically as per sensible out-of-the-box defaults.
    <li>Support of flask.
</ul>

# Data Folders

<ul>
    <li><b>\asn1Play\Data\SampleData</b>: Sample Data folder containing various version specific data files.
    <li><b>\asn1Play\Data\UserData</b>: User Data folder containing various version specific data files (Default Output Directory).
</ul>

# Sample Usage References

To Refer Sample usages, search for below keywords in source code (\asn1Play\src\main\data_type) and/or in data folders.
<ul>
    <li>.Asn1Files;
    <li>.Base64Files;
    <li>.HexFiles;
    <li>.YmlFiles;
    <li>AsciiInput;
    <li>AsciiOutput;
    <li>Asn1Element;
    <li>Asn1ElementString;
    <li>Asn1ElementVariable;
    <li>Asn1Input;
    <li>Asn1Output;
    <li>Base64Input;
    <li>Base64Output;
    <li>BulkMode;
    <li>ByteArrayInput;
    <li>ByteArrayOutput;
    <li>ByteArraySignedInput;
    <li>ByteArraySignedOutput;
    <li>Der64Input;
    <li>Der64Output;
    <li>DerInput;
    <li>DerOutput;
    <li>DirectInput;
    <li>DirectoryInput;
    <li>ExportKeyword;
    <li>ExportedInput;
    <li>ExtendRemarksList;
    <li>FileInput;
    <li>HexInput;
    <li>HexOutput;
    <li>ItemIndexVariable;
    <li>ListInput;
    <li>OutputFile;
    <li>OutputKeyword;
    <li>PE_End;
    <li>ProfileElement;
    <li>ReParseOutput;
    <li>RemarksVariable;
    <li>StoreMetadataRequest;
    <li>UpdateMetadataRequest;
    <li>VersionVariable;
    <li>YmlInput;
    <li>YmlOutput;
    <li>YmlOutputSameFile;
</ul>

# Reserve Variables

<ul>
    <li>$VERSION
    <ul>
        <li>Used for input_path, when version of asn specification needs to be considered in file path on run time.
    </ul>
    <li>$REMARKS
    <ul>
        <li>Used for output_file_path, when Remarks needs to be considered in output path.
    </ul>
    <li>$ASN1_ELEMENT
    <ul>
        <li>Used for remarks_list, when Asn Element Name needs to be considered in remarks_list.
    </ul>
    <li>$ITEM_INDEX
    <ul>
        <li>Used for output_file_path, when Item Index (For Bulk Mode) needs to be considered in output path.
    </ul>
</ul>

# Reserve Keywords

<ul>
    <li>output
    <ul>
        <li>Used for output in file.
    </ul>
    <li>export
    <ul>
        <li>Used for export mode. Export of configuration in .yml file.
    </ul>
</ul>

# Important Points

<ul>
    <li>For output_file, Both "directory path" and "file path" (identified based on any extension) are supported, Hence a path without extension will be considered as directory. 
    <li>For input/output via files/directory, always enclosed path with r''. Here "r" denotes raw string and avoid escape sequences.
    <li>output keyword always utilize comments
    <li>output file utilize comments in case of directory or if file name is having $REMARKS
</ul>
