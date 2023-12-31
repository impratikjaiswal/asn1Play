# ASN1 Play

<BR>ASN1 Encoder &amp; Decoder based on [pycrate](https://github.com/P1sec/pycrate).
<BR>Currently supporting various versions of:
1. [GSMA SGP.22](https://www.gsma.com/esim/esim-specification/ "GSMA SGP.22" )
2. [TCA eUICC_Profile_Package (SAIP)](https://trustedconnectivityalliance.org/technology-library-sim-specifications/ "SAIP")

<BR>However, Tool can be extended to support any ASN1 based conversion.

# How To Install

1. All Required packages are listed in requirements.txt
1. Few Basic Scripts are also present under <i>scripts</i> folder.
   - Currently, Scripts are targeting virtual environment with folder name as <i>venv</i> (Present in parallel of <i>scripts</i> folder)
   - However, same can be modified as per user choice.
   
    **Note:** installing tool in virtual environment is optional but preferred.

# How To Use
  - Code can be directly run from <i>asn1Play/asn1_play/main/asn1play.py</i>
<BR>    or alternatively 
  - UI via Local Web server [AmenityPjApp](https://github.com/impratikjaiswal/AmenityPjApp) can alos be used by running <i>/scripts/server_amenity_pj_app_start_debug.bat</i>
 
# Screen Shots

![Sample 1](images\Sample1.png)
![Sample 2](https://github.com/impratikjaiswal/asn1play/tree/ef13a274e666a577e1c381cfc6cb85054147e5d2/images\Sample1.png)

# Few Major Features

  - Auto Trimming of HEX Data (White Spaces Deletion).
  - Auto Detection of Base64 & Hex data.
  - Auto Detection of ByteArraySigned & ByteArrayUnSigned.
  - Conversion Mode for HEX, ASCII, TEXT & Base64.
  - Support of "Individual Mode"; Raw/Target Data can be configured Directly or file path (Binary as well as Text File; any extension) can be passed.
  - Support of "Bulk Mode"; Raw/Target Data can be configured Directly in List/Array format or Directory Path can be passed (Files with Known extensions will be picked based on Input Format).
  - Support of "Yml Mode (Config Mode)"; Raw/Target Data (along with all needed config) can be configured Directly in Yaml Files (".yaml" or ".yml" extensions), and same cane be passed in "Individual Mode" or "Bulk Mode".
  - For Known File Extensions (".asn1", ".asn", ".base64", ".hex"), Input/Output Format may be modified automatically as per sensible out-of-the-box defaults.

# Data Folders

  - <b>\asn1Play\Data\SampleData</b>: Sample Data folder containing various version specific data files.
  - <b>\asn1Play\Data\UserData</b>: User Data folder containing various version specific data files (Default Output Directory).

# Sample Usage References

To Refer Sample usages, search for below keywords in source code (\asn1Play\asn1_play\main\data_type) and/or in data folders.
  - .Asn1Files;
  - .Base64Files;
  - .HexFiles;
  - .YmlFiles;
  - AsciiInput;
  - AsciiOutput;
  - TxtInput;
  - TxtOutput;
  - Asn1Element;
  - Asn1Schema;
  - Asn1ElementString;
  - Asn1ElementVariable;
  - Asn1Input;
  - Asn1Output;
  - Base64Input;
  - Base64Output;
  - BulkMode;
  - ByteArrayInput;
  - ByteArrayOutput;
  - ByteArraySignedInput;
  - ByteArraySignedOutput;
  - Certificate;
  - Der64Input;
  - Der64Output;
  - DerInput;
  - DerOutput;
  - DirectInput;
  - DirectoryInput;
  - DirectoryOutput;
  - ExportKeyword;
  - ExportedInput;
  - ExtendRemarksList;
  - FileInput;
  - HexInput;
  - HexOutput;
  - ItemIndexVariable;
  - ListInput;
  - OutputFile;
  - OutputKeyword;
  - PE_End;
  - ProfileElement;
  - ReParseOutput;
  - RemarksVariable;
  - StoreMetadataRequest;
  - TlvParsing;
  - UpdateMetadataRequest;
  - VersionVariable;
  - YmlInput;
  - YmlOutput;
  - YmlOutputSameFile;

# Reserve Variables

  - $VERSION
    - Used for input_path, when version of asn specification needs to be considered in file path on run time.
  - $REMARKS
    - Used for output_file_path, when Remarks needs to be considered in output path.
  - $ASN1_ELEMENT
    - Used for remarks_list, when Asn Element Name needs to be considered in remarks_list.
  - $ITEM_INDEX
    - Used for output_file_path, when Item Index (For Bulk Mode) needs to be considered in output path.

# Reserve Keywords
  - output
    - Used for output in file.
  - export
    - Used for export mode. Export of configuration in .yml file.

# Important Points

  - For output_file, Both "directory path" and "file path" (identified based on any extension) are supported, Hence a path without extension will be considered as directory. 
  - For input/output via files/directory, always enclosed path with r''. Here "r" denotes raw string and avoid escape sequences, otherwise it might be considered as normal input. 
  - output keyword always utilize comments
  - output file utilize comments in case of directory or if file name is having $REMARKS