from asn1_play.generated_code.asn1.GSMA import SGP_22
from asn1_play.generated_code.asn1.GSMA.SGP_22.v0_0.python_gen.sgp22.sgp22 import PKIX1Explicit88
from asn1_play.generated_code.asn1.TCA import eUICC_Profile_Package
from asn1_play.generated_code.asn1.asn1 import Asn1
from asn1_play.generated_code.asn1.asn1_versions import Asn1Versions
from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.helper.data import Data
from asn1_play.main.helper.folders import Folders
from asn1_play.main.helper.formats import Formats
from asn1_play.main.helper.keywords import KeyWords


class AnyData(DataTypeMaster):

    def set_print_input(self):
        print_input = None
        super().set_print_input(print_input)

    def set_print_output(self):
        print_output = None
        super().set_print_output(print_output)

    def set_print_info(self):
        print_info = None
        super().set_print_info(print_info)

    def set_output_file(self):
        output_file = None
        super().set_output_file(output_file)

    def set_remarks(self):
        remarks = None
        super().set_remarks(remarks)

    def set_re_parse_output(self):
        re_parse_output = None
        super().set_re_parse_output(re_parse_output)

    def set_output_file_name_keyword(self):
        output_file_name_keyword = None
        super().set_output_file_name_keyword(output_file_name_keyword)

    def set_output_format(self):
        output_format = None
        super().set_output_format(output_format)

    def set_input_format(self):
        input_format = None
        super().set_input_format(input_format)

    def set_asn1_element(self):
        asn1_element = None
        super().set_asn1_element(asn1_element)

    def set_data_pool(self):
        data_pool = [
            #
            Data(
                remarks='# DerInput; Asn1Output; FileInput; Asn1Schema; Asn1Element; StoreMetadataRequest; VersionVariable; GSMA_SGP_22_v3_0_0;',
                input_data=Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest\StoreMetadataRequest.hex'),
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v3_0_0, 'StoreMetadataRequest'),
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                remarks='# DerInput; Asn1Output; FileInput; Asn1Schema; Asn1Element; StoreMetadataRequest; VersionVariable; GSMA_SGP_22_v2_4;',
                input_data=Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest\StoreMetadataRequest.hex'),
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v2_4, 'StoreMetadataRequest'),
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                remarks='# DerInput; Asn1Output; FileInput; Asn1Schema; Asn1Element; EimConfigurationData; VersionVariable;',
                input_data=Folders.in_sample_sgp_32(r'$VERSION\EimConfigurationData\EimConfigurationData.asn1'),
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_32_v1_0_1, 'EimConfigurationData'),
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            #
            Data(
                remarks='# DerInput; Asn1Output; Asn1Schema; Asn1Element; EimConfigurationData;',
                input_data='301180087465737465696d3182010387020780',
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_32_v1_0_1, 'EimConfigurationData'),
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(  # HexInput; AsciiOutput; YmlInput;
                input_data=Folders.in_sample_gen(r'ASCII\hex_to_ascii_op_same_file.yml')
            ),
            #
            Data(  # HexInput; AsciiOutput; YmlInput; OutputKeyword;
                input_data=Folders.in_sample_gen(r'ASCII\hex_to_ascii_op.yml')
            ),
            #
            Data(
                remarks='HexInput; AsciiOutput; DirectInput;',
                input_data='50726174696B204A61697377616C',
                asn1_element=None,
                input_format=Formats.HEX,
                output_format=Formats.ASCII
            ),
            #
            Data(
                remarks='DerInput; AsciiOutput; DirectInput;',
                input_data='50726174696B204A61697377616C',
                asn1_element=None,
                input_format=Formats.DER,
                output_format=Formats.ASCII
            ),
            #
            Data(
                remarks='HexInput; AsciiOutput; DirectInput; ExportKeyword;',
                input_data='57656c636f6d6520546f2041736e506c61792021212157656c636f6d6520546f2041736e506c61792021212157656c636f6d6520546f2041736e506c61792021212157656c636f6d6520546f2041736e506c617920212121',
                input_format=Formats.HEX,
                output_format=Formats.ASCII,
                output_file_name_keyword=KeyWords.EXPORT_FILE_NAME_KEYWORD
            ),
            #
            Data(  # 'HexInput; AsciiOutput; YmlInput; ExportedInput;
                input_data=Folders.in_user(r'HexInput_AsciiOutput_DirectInput_ExportKeyword_export.yml'),
            ),
            #
            Data(
                remarks='HexInput; AsciiOutput; DirectInput; ExportKeyword; OutputFile;',
                input_data='57656c636f6d6520546f2041736e506c61792021212157656c636f6d6520546f2041736e506c61792021212157656c636f6d6520546f2041736e506c61792021212157656c636f6d6520546f2041736e506c617920212121',
                input_format=Formats.HEX,
                output_format=Formats.ASCII,
                output_file=Folders.in_sample_gen(r'ASCII'),
                output_file_name_keyword=KeyWords.EXPORT_FILE_NAME_KEYWORD,
            ),
            #
            Data(  # 'HexInput; AsciiOutput; DirectInput; ExportKeyword; OutputFile; YmlInput;
                input_data=Folders.in_sample_gen(
                    r'ASCII\HexInput_AsciiOutput_DirectInput_ExportKeyword_OutputFile_export.yml'),
            ),
            #
            Data(
                remarks='AsciiInput; HexOutput; DirectInput;',
                input_data='Pratik Jaiswal',
                input_format=Formats.ASCII,
                output_format=Formats.HEX
            ),
            #
            Data(
                remarks='TxtInput; HexOutput; DirectInput;',
                input_data='8929901012345678905F',
                input_format=Formats.TXT,
                output_format=Formats.HEX
            ),
            #
            Data(
                remarks='TxtOutput; HexInput; DirectInput;',
                input_data='3839323939303130313233343536373839303546',
                input_format=Formats.HEX,
                output_format=Formats.TXT
            ),
            #
            Data(
                remarks='AsciiInput; HexOutput; FileInput;',
                input_data=Folders.in_sample_gen(r'ASCII\ascii_to_hex_welcome.txt'),
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
            ),
            #
            Data(
                remarks='HexInput; AsciiOutput; FileInput;',
                input_data=Folders.in_sample_gen(r'ASCII\hex_to_ascii_welcome.hex'),
                input_format=Formats.HEX,
                output_format=Formats.ASCII,
            ),
            #
            Data(
                remarks='ByteArrayInput; ByteArraySignedInput; DerOutput; DirectInput;',
                input_data=[10, -68, -46, 85],
                input_format=Formats.DER_BYTE_ARRAY,
                output_format=Formats.DER,
            ),
            #
            Data(
                remarks='ByteArrayInput; DerOutput; DirectInput;',
                input_data=[10, 188, 210, 85],
                input_format=Formats.DER_BYTE_ARRAY,
                output_format=Formats.DER,
            ),
            #
            Data(
                remarks='DerInput; ByteArrayOutput; DirectInput;',
                input_data='0ABCD255',
                input_format=Formats.DER,
                output_format=Formats.DER_BYTE_ARRAY,
            ),
            #
            Data(
                remarks='DerInput; ByteArraySignedOutput; DirectInput;',
                input_data='CrzSVQ==',
                input_format=Formats.DER,
                output_format=Formats.DER_BYTE_ARRAY_SIGNED,
            ),
            #
            Data(
                remarks='DerInput; Base64Output; DirectInput;',
                input_data='BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                asn1_element=None,
                input_format=Formats.DER,
                output_format=Formats.DER_64
            ),
            #
            Data(  # DerInput; Base64Output; YmlInput; OutputKeyword;
                input_data=Folders.in_sample_gen(r'Base64\der_to_base64.yml')
            ),
            #
            Data(
                remarks='# Base64Input; DerOutput; DirectInput;',
                input_data='vyU3WgqYkgkBIUNlhwn1kQlTUCBOYW1lIDGSGk9wZXJhdGlvbmFsIFByb2ZpbGUgTmFtZSAxmQIGQA==',
                asn1_element=None,
                input_format=Formats.DER_64,
                output_format=Formats.DER
            ),
            #
            Data(  # Base64Input; DerOutput; YmlInput; OutputKeyword;
                input_data=Folders.in_sample_gen(r'Base64\base64_to_der.yml')
            ),
            #
            Data(
                remarks='# AsciiInput; Der64Output; DirectInput;',
                input_data='Pratik Jaiswal',
                asn1_element=None,
                input_format=Formats.ASCII,
                output_format=Formats.DER_64
            ),
            #
            Data(
                remarks='# Der64Input; AsciiOutput; DirectInput;',
                input_data='UHJhdGlrIEphaXN3YWw=',
                asn1_element=None,
                input_format=Formats.DER_64,
                output_format=Formats.ASCII
            ),
            #
            Data(
                remarks='# DerInput; Asn1Output; DirectInput; Asn1ElementString; StoreMetadataRequest; ',
                input_data='BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                asn1_element='StoreMetadataRequest',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                remarks='# DerInput; Asn1Output; DirectInput; Asn1ElementString; UpdateMetadataRequest;',
                input_data='bf2a0499020520',
                asn1_element='UpdateMetadataRequest',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                remarks='# DerInput; Asn1Output; DirectInput; Asn1Element; StoreMetadataRequest; ',
                input_data='BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks='# HexInput; Asn1Output; DirectInput; Asn1Element; StoreMetadataRequest; ',
                input_data='BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.HEX,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks='# HexInput; Asn1Output; DirectInput; Asn1Element; ReParseOutput; StoreMetadataRequest; ',
                input_data='BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                re_parse_output=True
            ),
            #
            Data(
                remarks='# Asn1Input; DerOutput; FileInput; Asn1Element; TlvParsing; StoreMetadataRequest; ',
                input_data=Folders.in_sample_sgp_22(
                    r'$VERSION\StoreMetadataRequest\StoreMetadataRequest_Mandatory.asn1'),
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.ASN1,
                output_format=Formats.DER,
                tlv_parsing_of_output=True,
            ),
            #
            Data(
                remarks='# DerInput; Asn1Output; DirectInput; Asn1ElementString; StoreMetadataRequest; OutputKeyword;',
                input_data='BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                asn1_element='StoreMetadataRequest',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=KeyWords.OUTPUT_FILE_NAME_KEYWORD
            ),
            #
            Data(
                remarks='# DerInput; Asn1Output; DirectInput; Asn1ElementString; UpdateMetadataRequest; OutputKeyword; ',
                input_data='bf2a0499020520',
                asn1_element='UpdateMetadataRequest',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=KeyWords.OUTPUT_FILE_NAME_KEYWORD,
            ),
            #
            Data(
                remarks='# DerInput; Asn1Output; DirectInput; Asn1Element; StoreMetadataRequest; OutputKeyword;',
                input_data='BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=KeyWords.OUTPUT_FILE_NAME_KEYWORD
            ),
            #
            Data(
                remarks='# Der64Input; Asn1Output; FileInput; Asn1Element; StoreMetadataRequest; VersionVariable;',
                input_data=Folders.in_sample_sgp_22(
                    r'$VERSION\StoreMetadataRequest\StoreMetadataRequest_wo_icon.base64'),
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks='# Der64Input; Asn1Output; FileInput; Asn1Element; StoreMetadataRequest; VersionVariable; OutputKeyword;',
                input_data=Folders.in_sample_sgp_22(
                    r'$VERSION\StoreMetadataRequest\StoreMetadataRequest_wo_icon.base64'),
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1,
                output_file_name_keyword=KeyWords.OUTPUT_FILE_NAME_KEYWORD
            ),
            #
            Data(
                remarks='# DerInput; Asn1Output; FileInput; Asn1Element; StoreMetadataRequest; VersionVariable; OutputKeyword;',
                input_data=Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest\StoreMetadataRequest.hex'),
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=KeyWords.OUTPUT_FILE_NAME_KEYWORD
            ),
            #
            Data(  # DerInput; Asn1Output; YmlInput; Asn1Element; StoreMetadataRequest; VersionVariable; OutputKeyword;
                input_data=Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest\StoreMetadataRequest.hex.yml'),
            ),
            #
            Data(  # Asn1Input; DerOutput; YmlInput; Asn1Element; StoreMetadataRequest; VersionVariable; OutputKeyword;
                input_data=Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest\StoreMetadataRequest.asn1.yml'),
            ),
            #
            Data(
                # Asn1Input; DerOutput; YmlInput; Asn1Element; ReParseOutput; StoreMetadataRequest; VersionVariable; OutputKeyword;
                input_data=Folders.in_sample_sgp_22(
                    r'$VERSION\StoreMetadataRequest\StoreMetadataRequest_Mandatory.asn1.yml'),
            ),
            #
            Data(
                remarks='DerInput; Asn1Output; DirectInput; Asn1Element; ProfileElement;',
                input_data='A042800102810101821447534D412050726F66696C65205061636B616765830A8929901012345678905FA506810084008B00A610060667810F010201060667810F010204B08201F8A0058000810101810667810F010201A207A105C60301020AA305A1038B010FA40C830A989209012143658709F5A527A109820442210026800198831A61184F10A0000000871002FF33FF01890000010050045553494DA682019EA10A8204422100258002022B831B8001019000800102A406830101950108800158A40683010A95010882010A8316800101A40683010195010880015AA40683010A95010882010F830B80015BA40683010A95010882011A830A800101900080015A970082011B8316800103A406830101950108800158A40683010A95010882010F8316800111A40683010195010880014AA40683010A95010882010F8321800103A406830101950108800158A40683010A950108840132A4068301019501088201048321800101A406830101950108800102A406830181950108800158A40683010A950108820104831B800101900080011AA406830101950108800140A40683010A95010882010A8310800101900080015AA40683010A95010882011583158001019000800118A40683010A95010880014297008201108310800101A40683010195010880015A97008201158316800113A406830101950108800148A40683010A95010882010F830B80015EA40683010A95010882011A83258001019000800102A010A406830101950108A406830102950108800158A40683010A950108A33FA0058000810102A13630118001018108303030303030303082020099300D800102810831323334353637383012800200818108393239343536373882020088A244A0058000810103A13BA0393013800101810831323334FFFFFFFF8201018301063010800102810830303030FFFFFFFF820102301080010A810835363738FFFFFFFF830101B37CA0058000810104810667810F010204A21DA11B83027FF18410A0000000871002FF33FF018900000100C60301810AA30B8309082999181132547698A406A104C7022F06A80F830D0A2E148CE73204000000000000AD1383110247534D41206555494343FFFFFFFFFFFFAE03830100B20483020040B606830419F1FF01A225A0058000810105A11CA01A301880020081810839323338FFFFFFFF82020081830101840122A43AA0058000810106A131A12F8001018101018210000102030405060708090A0B0C0D0E0F83100102030405060708090A0B0C0D0E0F008603010203A681BBA0058000810107A1444F07A00000015153504F08A0000001515350414F08A000000151000000820382DC0083010FC90A810280008201F08701F0EA11800F0100000100000002011203B2010000A26C302295013882010183010130173015800180861066778899AABBCCDD1122334455EEFF103022950134820102830101301730158001808610112233445566778899AABBCCDDEEFF1030229501C882010383010130173015800180861099AABBCCDDEEFF101122334455667788A681C0A0058000810108A1494F07A00000015153504F08A0000001515350414F10A00000055910100102736456616C7565820380800083010FC907810280008201F0EA11800F01000001000000020112036C756500A26C30229501388201018301013017301580018086101122334455667788112233445566778830229501348201028301013017301580018086101122334455667788112233445566778830229501C882010383010130173015800180861011223344556677881122334455667788A720A00381010B4F09A00000055910100001A0050403B00000810112040100040100A740A00381010C4F09A00000055910100002A0050403B00020810112040100040100301E8010A0000000871002FF33FF018900000100810402000100820402000100AA07A0058000810163',
                asn1_element=eUICC_Profile_Package.PEDefinitions.ProfileElement,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            #
            Data(  # DerInput; Asn1Output; YmlInput; Asn1Element; ProfileElement; OutputKeyword;
                input_data=Folders.in_sample_epp(r'$VERSION\PROFILE_OPERATIONAL1.hex.yml')
            ),
            #
            Data(  # Asn1Input; DerOutput; YmlInput; Asn1Element; ProfileElement; OutputKeyword;
                input_data=Folders.in_sample_epp(r'$VERSION\PROFILE_OPERATIONAL1.asn1.yml')
            ),
            #
            Data(
                remarks='DerInput; Asn1Output; DirectInput; Asn1Element; UpdateMetadataRequest; ExportKeyword; OutputFile;',
                input_data='bf2a0499020520',
                asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=KeyWords.EXPORT_FILE_NAME_KEYWORD,
                output_file=Folders.in_user_sgp_22(r'$VERSION\UpdateMetadataRequest'),
            ),
            #
            Data(  # 'DerInput; Asn1Output; YmlInput; ExportedInput; Asn1Element; UpdateMetadataRequest;',
                input_data=Folders.in_user_sgp_22(
                    r'$VERSION\UpdateMetadataRequest\DerInput_Asn1Output_DirectInput_Asn1Element_UpdateMetadataRequest_ExportKeyword_OutputFile_export.yml'),
            ),
            #
            Data(
                remarks='DerInput; Asn1Output; DirectInput; Asn1Element; PE_End; ExportKeyword;',
                input_data='3007a0058000810163',
                asn1_element=eUICC_Profile_Package.PEDefinitions.PE_End,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=KeyWords.EXPORT_FILE_NAME_KEYWORD,
                output_file=Folders.in_user_epp(r'$VERSION\PE_End'),
            ),
            #
            Data(  # 'DerInput; Asn1Output; YmlInput; ExportedInput; Asn1Element; PE_End;',
                input_data=Folders.in_user_epp(
                    r'$VERSION/\PE_End\DerInput_Asn1Output_DirectInput_Asn1Element_PE_End_ExportKeyword_export.yml'),
            ),
            #
            Data(
                remarks='# DerInput; Asn1Output; DirectInput; Asn1Element; PE_End;',
                input_data='3007a0058000810163',
                asn1_element=eUICC_Profile_Package.PEDefinitions.PE_End,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks='# DerInput; Asn1Output; DirectInput; Asn1Element; UpdateMetadataRequest;',
                input_data='bf2a0499020520',
                asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks='# $ASN1_ELEMENT DerInput; Asn1Output; DirectInput; Asn1Element; Asn1ElementVariable;',
                input_data='bf2a0499020520',
                asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks='# DerInput; Asn1Output; DirectInput; Asn1Element; Certificate;',
                input_data='308201ff308201a6a0030201020209020000000000000001300a06082a8648ce3d0403023037310b300906035504061302455331153013060355040a0c0c52535020546573742045554d3111300f06035504030c0845554d20546573743020170d3230303430313039343835385a180f37343936303132343039343835385a3064310b300906035504061302455331153013060355040a0c0c52535020546573742045554d312930270603550405132038393034393033323132333435313233343531323334353637383930313233353113301106035504030c0a54657374206555494343305a301406072a8648ce3d020106092b2403030208010107034200043e590c38a9c256315ecff3291416dd335409a666fd41b3b51e5e5114f343abf0a26774c6c26c48753afe283643227bb6608cd261cc972d374a479124ebf27722a36b3069301f0603551d230418301680146fa1e5217363a822bded988a1a0d0ff5d7620db7301d0603551d0e04160414c8a64f343b85b7b0578dc57f8f13586dc804ed84300e0603551d0f0101ff04040302078030170603551d200101ff040d300b3009060767811201020101300a06082a8648ce3d040302034700304402205673c0fe8ff495ae93ae37a13296b2cb1b1017d7697053ed6920e987928699d70220059c7fec056869f24b548ac64757e4cb14d3a08609752c79a5b872a4980e338b',
                asn1_element=PKIX1Explicit88.Certificate,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                remarks='# BulkMode; DirectoryInput; YmlInput; .YmlFiles;',
                input_data=Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest'),
                input_format=Formats.YML,
                output_format=''
            ),
            #
            Data(
                remarks='# BulkMode; DirectoryInput; DerInput; Asn1Output; .HexFiles;',
                input_data=Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest'),
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks='# BulkMode; DirectoryInput; Base64Input; Asn1Output; .Base64Files;',
                input_data=Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest'),
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks='# BulkMode; DirectoryInput; Asn1Input; Der64Output; .Asn1Files;',
                input_data=Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest'),
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.ASN1,
                output_format=Formats.DER_64
            ),
            #
            Data(
                remarks='# BulkMode; DirectoryInput; .YmlFiles; .HexFiles; .Base64Files; .Asn1Files; ',
                input_data=Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest'),
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format='',
            ),
            #
            Data(
                remarks='# BulkMode; DirectoryInput; Asn1Input; Der64Output; DirectoryOutput; .Asn1Files;',
                input_data=Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest'),
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.ASN1,
                output_format=Formats.DER,
                output_file=Folders.in_user_sgp_22(r'$VERSION\StoreMetadataRequest\hex'),
            ),
            #
            Data(
                remarks='# BulkMode; ListInput; Der64Input; Asn1Output; Asn1Element; StoreMetadataRequest;',
                input_data=[
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
                ],
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks='# BulkMode; ListInput; Der64Input; Asn1Output; Asn1Element; StoreMetadataRequest; ItemIndexVariable; ',
                input_data=[
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
                ],
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1,
                output_file=Folders.in_user(r'Temp\$ITEM_INDEX'),
            ),
            #
            Data(
                # BulkMode; ListInput; Der64Input; Asn1Output; Asn1Element; StoreMetadataRequest; ExtendRemarksList;
                remarks=['ExtendRemarksList; Sample', 'ExtendRemarksList;'],
                input_data=[
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
                ],
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                remarks='# BulkMode; ListInput; Der64Input; Asn1Output; Asn1Element; StoreMetadataRequest; RemarksVariable;',
                input_data=[
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
                ],
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1,
                output_file=Folders.in_user_sgp_22(r'$VERSION\StoreMetadataRequest\$REMARKS'),
            ),
            #
            Data(  # DerInput; Asn1Output; YmlInput; Asn1Element; EUICCInfo2; VersionVariable; OutputKeyword;
                input_data=Folders.in_sample_sgp_22(r'$VERSION\EUICCInfo2\EUICCInfo2.hex.yml'),
            ),
            #
            Data(  # DerInput; Asn1Output; YmlInput; Asn1Element; EUICCInfo2; VersionVariable; OutputKeyword;
                input_data=Folders.in_sample_sgp_32(r'$VERSION\EUICCInfo2\EUICCInfo2.hex.yml'),
            ),
        ]
        super().set_data_pool(data_pool)
