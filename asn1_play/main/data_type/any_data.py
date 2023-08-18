from asn1_play.generated_code.asn1.GSMA import SGP_22
from asn1_play.generated_code.asn1.TCA import eUICC_Profile_Package
from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.helper.data import Data
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

    def set_re_parse_output(self):
        re_parse_output = None
        super().set_re_parse_output(re_parse_output)

    def set_output_file(self):
        output_file = None
        super().set_output_file(output_file)

    def set_output_file_name_keyword(self):
        output_file_name_keyword = None
        super().set_output_file_name_keyword(output_file_name_keyword)

    def set_remarks_list(self):
        remarks_list = None
        super().set_remarks_list(remarks_list)

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
            Data(  # HexInput; AsciiOutput; YmlInput;
                raw_data=r'..\..\Data\SampleData\Generic\ASCII\hex_to_ascii_op_same_file.yml'
            ),
            #
            Data(  # HexInput; AsciiOutput; YmlInput; OutputKeyword;
                raw_data=r'..\..\Data\SampleData\Generic\ASCII\hex_to_ascii_op.yml'
            ),
            #
            Data(
                remarks_list='HexInput; AsciiOutput; DirectInput;',
                raw_data='50726174696B204A61697377616C',
                asn1_element=None,
                input_format=Formats.HEX,
                output_format=Formats.ASCII
            ),
            #
            Data(
                remarks_list='DerInput; AsciiOutput; DirectInput;',
                raw_data='50726174696B204A61697377616C',
                asn1_element=None,
                input_format=Formats.DER,
                output_format=Formats.ASCII
            ),
            #
            Data(
                remarks_list='HexInput; AsciiOutput; DirectInput; ExportKeyword;',
                raw_data='57656c636f6d6520546f2041736e506c61792021212157656c636f6d6520546f2041736e506c61792021212157656c636f6d6520546f2041736e506c61792021212157656c636f6d6520546f2041736e506c617920212121',
                input_format=Formats.HEX,
                output_format=Formats.ASCII,
                output_file_name_keyword=KeyWords.EXPORT_FILE_NAME_KEYWORD
            ),
            #
            Data(  # 'HexInput; AsciiOutput; YmlInput; ExportedInput;
                raw_data=r'..\..\Data\UserData\HexInput_AsciiOutput_DirectInput_ExportKeyword_export.yml',
            ),
            #
            Data(
                remarks_list='HexInput; AsciiOutput; DirectInput; ExportKeyword; OutputFile;',
                raw_data='57656c636f6d6520546f2041736e506c61792021212157656c636f6d6520546f2041736e506c61792021212157656c636f6d6520546f2041736e506c61792021212157656c636f6d6520546f2041736e506c617920212121',
                input_format=Formats.HEX,
                output_format=Formats.ASCII,
                output_file=r'..\..\Data\SampleData\Generic\ASCII',
                output_file_name_keyword=KeyWords.EXPORT_FILE_NAME_KEYWORD,
            ),
            #
            Data(  # 'HexInput; AsciiOutput; DirectInput; ExportKeyword; OutputFile; YmlInput;
                raw_data=r'..\..\Data\SampleData\Generic\ASCII\HexInput_AsciiOutput_DirectInput_ExportKeyword_OutputFile_export.yml',
            ),
            #
            Data(
                remarks_list='AsciiInput; HexOutput; DirectInput;',
                raw_data='Pratik Jaiswal',
                asn1_element=None,
                input_format=Formats.ASCII,
                output_format=Formats.DER
            ),
            #
            Data(
                remarks_list='AsciiInput; HexOutput; FileInput;',
                raw_data=r'..\..\Data\SampleData\Generic\ASCII\ascii_to_hex_welcome.txt',
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
            ),
            #
            Data(
                remarks_list='HexInput; AsciiOutput; FileInput;',
                raw_data=r'..\..\Data\SampleData\Generic\ASCII\hex_to_ascii_welcome.hex',
                input_format=Formats.HEX,
                output_format=Formats.ASCII,
            ),
            #
            Data(
                remarks_list='ByteArrayInput; ByteArraySignedInput; DerOutput; DirectInput;',
                raw_data=[10, -68, -46, 85],
                input_format=Formats.BYTE_ARRAY,
                output_format=Formats.DER,
            ),
            #
            Data(
                remarks_list='ByteArrayInput; DerOutput; DirectInput;',
                raw_data=[10, 188, 210, 85],
                input_format=Formats.BYTE_ARRAY,
                output_format=Formats.DER,
            ),
            #
            Data(
                remarks_list='DerInput; ByteArrayOutput; DirectInput;',
                raw_data='0ABCD255',
                input_format=Formats.DER,
                output_format=Formats.BYTE_ARRAY,
            ),
            #
            Data(
                remarks_list='DerInput; ByteArraySignedOutput; DirectInput;',
                raw_data='CrzSVQ==',
                input_format=Formats.DER,
                output_format=Formats.BYTE_ARRAY_SIGNED,
            ),
            #
            Data(
                remarks_list='DerInput; Base64Output; DirectInput;',
                raw_data='BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                asn1_element=None,
                input_format=Formats.DER,
                output_format=Formats.DER_64
            ),
            #
            Data(  # DerInput; Base64Output; YmlInput; OutputKeyword;
                raw_data=r'..\..\Data\SampleData\Generic\Base64\der_to_base64.yml'
            ),
            #
            Data(
                remarks_list='# Base64Input; DerOutput; DirectInput;',
                raw_data='vyU3WgqYkgkBIUNlhwn1kQlTUCBOYW1lIDGSGk9wZXJhdGlvbmFsIFByb2ZpbGUgTmFtZSAxmQIGQA==',
                asn1_element=None,
                input_format=Formats.DER_64,
                output_format=Formats.DER
            ),
            #
            Data(  # Base64Input; DerOutput; YmlInput; OutputKeyword;
                raw_data=r'..\..\Data\SampleData\Generic\Base64\base64_to_der.yml'
            ),
            #
            Data(
                remarks_list='# AsciiInput; Der64Output; DirectInput;',
                raw_data='Pratik Jaiswal',
                asn1_element=None,
                input_format=Formats.ASCII,
                output_format=Formats.DER_64
            ),
            #
            Data(
                remarks_list='# Der64Input; AsciiOutput; DirectInput;',
                raw_data='UHJhdGlrIEphaXN3YWw=',
                asn1_element=None,
                input_format=Formats.DER_64,
                output_format=Formats.ASCII
            ),
            #
            Data(
                remarks_list='# DerInput; Asn1Output; DirectInput; Asn1ElementString; StoreMetadataRequest; ',
                raw_data='BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                asn1_element='StoreMetadataRequest',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                remarks_list='# DerInput; Asn1Output; DirectInput; Asn1ElementString; UpdateMetadataRequest;',
                raw_data='bf2a0499020520',
                asn1_element='UpdateMetadataRequest',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                remarks_list='# DerInput; Asn1Output; DirectInput; Asn1Element; StoreMetadataRequest; ',
                raw_data='BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks_list='# HexInput; Asn1Output; DirectInput; Asn1Element; StoreMetadataRequest; ',
                raw_data='BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.HEX,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks_list='# HexInput; Asn1Output; DirectInput; Asn1Element; ReParseOutput; StoreMetadataRequest; ',
                raw_data='BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                re_parse_output=True
            ),
            #
            Data(
                remarks_list='# DerInput; Asn1Output; DirectInput; Asn1ElementString; StoreMetadataRequest; OutputKeyword;',
                raw_data='BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                asn1_element='StoreMetadataRequest',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=KeyWords.OUTPUT_FILE_NAME_KEYWORD
            ),
            #
            Data(
                remarks_list='# DerInput; Asn1Output; DirectInput; Asn1ElementString; UpdateMetadataRequest; OutputKeyword; ',
                raw_data='bf2a0499020520',
                asn1_element='UpdateMetadataRequest',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=KeyWords.OUTPUT_FILE_NAME_KEYWORD,
            ),
            #
            Data(
                remarks_list='# DerInput; Asn1Output; DirectInput; Asn1Element; StoreMetadataRequest; OutputKeyword;',
                raw_data='BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=KeyWords.OUTPUT_FILE_NAME_KEYWORD
            ),
            #
            Data(
                remarks_list='# Der64Input; Asn1Output; FileInput; Asn1Element; StoreMetadataRequest; VersionVariable;',
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\StoreMetadataRequest_wo_icon.base64',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks_list='# Der64Input; Asn1Output; FileInput; Asn1Element; StoreMetadataRequest; VersionVariable; OutputKeyword;',
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\StoreMetadataRequest_wo_icon.base64',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1,
                output_file_name_keyword=KeyWords.OUTPUT_FILE_NAME_KEYWORD
            ),
            #
            Data(
                remarks_list='# DerInput; Asn1Output; FileInput; Asn1Element; StoreMetadataRequest; VersionVariable; OutputKeyword;',
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\StoreMetadataRequest.hex',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=KeyWords.OUTPUT_FILE_NAME_KEYWORD
            ),
            #
            Data(  # DerInput; Asn1Output; YmlInput; Asn1Element; StoreMetadataRequest; VersionVariable; OutputKeyword;
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\StoreMetadataRequest.hex.yml',
            ),
            #
            Data(  # Asn1Input; DerOutput; YmlInput; Asn1Element; StoreMetadataRequest; VersionVariable; OutputKeyword;
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\StoreMetadataRequest.asn1.yml',
            ),
            #
            Data(
                # Asn1Input; DerOutput; YmlInput; Asn1Element; ReParseOutput; StoreMetadataRequest; VersionVariable; OutputKeyword;
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\StoreMetadataRequest_Mandatory.asn1.yml',
            ),
            #
            Data(
                remarks_list='DerInput; Asn1Output; DirectInput; Asn1Element; ProfileElement;',
                raw_data='A042800102810101821447534D412050726F66696C65205061636B616765830A8929901012345678905FA506810084008B00A610060667810F010201060667810F010204B08201F8A0058000810101810667810F010201A207A105C60301020AA305A1038B010FA40C830A989209012143658709F5A527A109820442210026800198831A61184F10A0000000871002FF33FF01890000010050045553494DA682019EA10A8204422100258002022B831B8001019000800102A406830101950108800158A40683010A95010882010A8316800101A40683010195010880015AA40683010A95010882010F830B80015BA40683010A95010882011A830A800101900080015A970082011B8316800103A406830101950108800158A40683010A95010882010F8316800111A40683010195010880014AA40683010A95010882010F8321800103A406830101950108800158A40683010A950108840132A4068301019501088201048321800101A406830101950108800102A406830181950108800158A40683010A950108820104831B800101900080011AA406830101950108800140A40683010A95010882010A8310800101900080015AA40683010A95010882011583158001019000800118A40683010A95010880014297008201108310800101A40683010195010880015A97008201158316800113A406830101950108800148A40683010A95010882010F830B80015EA40683010A95010882011A83258001019000800102A010A406830101950108A406830102950108800158A40683010A950108A33FA0058000810102A13630118001018108303030303030303082020099300D800102810831323334353637383012800200818108393239343536373882020088A244A0058000810103A13BA0393013800101810831323334FFFFFFFF8201018301063010800102810830303030FFFFFFFF820102301080010A810835363738FFFFFFFF830101B37CA0058000810104810667810F010204A21DA11B83027FF18410A0000000871002FF33FF018900000100C60301810AA30B8309082999181132547698A406A104C7022F06A80F830D0A2E148CE73204000000000000AD1383110247534D41206555494343FFFFFFFFFFFFAE03830100B20483020040B606830419F1FF01A225A0058000810105A11CA01A301880020081810839323338FFFFFFFF82020081830101840122A43AA0058000810106A131A12F8001018101018210000102030405060708090A0B0C0D0E0F83100102030405060708090A0B0C0D0E0F008603010203A681BBA0058000810107A1444F07A00000015153504F08A0000001515350414F08A000000151000000820382DC0083010FC90A810280008201F08701F0EA11800F0100000100000002011203B2010000A26C302295013882010183010130173015800180861066778899AABBCCDD1122334455EEFF103022950134820102830101301730158001808610112233445566778899AABBCCDDEEFF1030229501C882010383010130173015800180861099AABBCCDDEEFF101122334455667788A681C0A0058000810108A1494F07A00000015153504F08A0000001515350414F10A00000055910100102736456616C7565820380800083010FC907810280008201F0EA11800F01000001000000020112036C756500A26C30229501388201018301013017301580018086101122334455667788112233445566778830229501348201028301013017301580018086101122334455667788112233445566778830229501C882010383010130173015800180861011223344556677881122334455667788A720A00381010B4F09A00000055910100001A0050403B00000810112040100040100A740A00381010C4F09A00000055910100002A0050403B00020810112040100040100301E8010A0000000871002FF33FF018900000100810402000100820402000100AA07A0058000810163',
                asn1_element=eUICC_Profile_Package.PEDefinitions.ProfileElement,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            #
            Data(  # DerInput; Asn1Output; YmlInput; Asn1Element; ProfileElement; OutputKeyword;
                raw_data=r'..\..\Data\SampleData\TCA\eUICC_Profile_Package\$VERSION\PROFILE_OPERATIONAL1.hex.yml'
            ),
            #
            Data(  # Asn1Input; DerOutput; YmlInput; Asn1Element; ProfileElement; OutputKeyword;
                raw_data=r'..\..\Data\SampleData\TCA\eUICC_Profile_Package\$VERSION\PROFILE_OPERATIONAL1.asn1.yml'
            ),

            #
            Data(
                remarks_list='DerInput; Asn1Output; DirectInput; Asn1Element; UpdateMetadataRequest; ExportKeyword; OutputFile;',
                raw_data='bf2a0499020520',
                asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=KeyWords.EXPORT_FILE_NAME_KEYWORD,
                output_file=r'..\..\Data\UserData\GSMA\SGP_22\$VERSION\UpdateMetadataRequest',
            ),
            #
            Data(  # 'DerInput; Asn1Output; YmlInput; ExportedInput; Asn1Element; UpdateMetadataRequest;',
                raw_data=r'..\..\Data\UserData\GSMA\SGP_22\$VERSION\UpdateMetadataRequest\DerInput_Asn1Output_DirectInput_Asn1Element_UpdateMetadataRequest_ExportKeyword_OutputFile_export.yml',
            ),
            #
            Data(
                remarks_list='DerInput; Asn1Output; DirectInput; Asn1Element; PE_End; ExportKeyword;',
                raw_data='3007a0058000810163',
                asn1_element=eUICC_Profile_Package.PEDefinitions.PE_End,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=KeyWords.EXPORT_FILE_NAME_KEYWORD,
                output_file=r'..\..\Data\UserData\TCA\eUICC_Profile_Package\$VERSION\PE_End',
            ),
            #
            Data(  # 'DerInput; Asn1Output; YmlInput; ExportedInput; Asn1Element; PE_End;',
                raw_data=r'../../Data/UserData/TCA/eUICC_Profile_Package/$VERSION/\PE_End\DerInput_Asn1Output_DirectInput_Asn1Element_PE_End_ExportKeyword_export.yml',
            ),

            #
            Data(
                remarks_list='# DerInput; Asn1Output; DirectInput; Asn1Element; PE_End;',
                raw_data='3007a0058000810163',
                asn1_element=eUICC_Profile_Package.PEDefinitions.PE_End,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks_list='# DerInput; Asn1Output; DirectInput; Asn1Element; UpdateMetadataRequest;',
                raw_data='bf2a0499020520',
                asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks_list='# $ASN1_ELEMENT DerInput; Asn1Output; DirectInput; Asn1Element; Asn1ElementVariable;',
                raw_data='bf2a0499020520',
                asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
        ]
        super().set_data_pool(data_pool)
