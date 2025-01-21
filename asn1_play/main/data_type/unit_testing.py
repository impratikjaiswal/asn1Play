from python_helpers.ph_keys import PhKeys
from python_helpers.ph_variables import PhVariables

from asn1_play.generated_code.asn1.GSMA import SGP_22, SGP_32
from asn1_play.generated_code.asn1.TCA import eUICC_Profile_Package
from asn1_play.generated_code.asn1.asn1 import Asn1
from asn1_play.generated_code.asn1.asn1_versions import Asn1Versions
from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.helper.data import Data
from asn1_play.main.helper.folders import Folders
from asn1_play.main.helper.formats import Formats
from asn1_play.main.helper.formats_group import FormatsGroup
from asn1_play.main.helper.keywords import KeyWords


class UnitTesting(DataTypeMaster):

    def __init__(self):
        super().__init__()

    def set_print_input(self):
        print_input = None
        super().set_print_input(print_input)

    def set_print_output(self):
        print_output = None
        super().set_print_output(print_output)

    def set_print_info(self):
        print_info = None
        super().set_print_info(print_info)

    def set_quiet_mode(self):
        quite_mode = None
        super().set_quiet_mode(quite_mode)

    def set_remarks(self):
        remarks = None
        super().set_remarks(remarks)

    def set_encoding(self):
        encoding = None
        super().set_encoding(encoding)

    def set_encoding_errors(self):
        encoding_errors = None
        super().set_encoding_errors(encoding_errors)

    def set_output_path(self):
        output_path = None
        super().set_output_path(output_path)

    def set_output_file_name_keyword(self):
        output_file_name_keyword = None
        super().set_output_file_name_keyword(output_file_name_keyword)

    def set_archive_output(self):
        archive_output = None
        super().set_archive_output(archive_output)

    def set_archive_output_format(self):
        archive_output_format = None
        super().set_archive_output_format(archive_output_format)

    def set_input_format(self):
        input_format = None
        super().set_input_format(input_format)

    def set_output_format(self):
        output_format = None
        super().set_output_format(output_format)

    def set_asn1_element(self):
        asn1_element = None
        super().set_asn1_element(asn1_element)

    def set_tlv_parsing_of_output(self):
        tlv_parsing_of_output = None
        super().set_tlv_parsing_of_output(tlv_parsing_of_output)

    def set_re_parse_output(self):
        re_parse_output = None
        super().set_re_parse_output(re_parse_output)

    def set_data_pool(self):
        data_pool_positive = [
            #
            Data(  # #YmlInput #ExportKeyword
                input_data=Folders.in_user_gen(r'ASCII\hex_to_ascii_exp.yml'),
            ),
            #
            Data(
                remarks='Input Data with White spaces',
                input_data='bf2a   04 99 02 05 20    ',
                asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks='Input Data with List',
                input_data=[
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
                ],
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1
            ),
        ]

        data_pool_byte_array = [
            # Byte Array with our Remarks
            Data(
                input_data=[10, -68, -46, 85],
                input_format=Formats.DER_BYTE_ARRAY,
                output_format=Formats.DER,
            ),
            # Byte Array with Remarks
            Data(
                remarks='Byte Array with Remarks',
                input_data=[10, -68, -46, 85],
                input_format=Formats.DER_BYTE_ARRAY,
                output_format=Formats.DER,
            ),
            #
            Data(
                input_data=[10, 188, 210, 85],
                input_format=Formats.DER_BYTE_ARRAY,
                output_format=Formats.DER_64,
            )
        ]

        data_pool_remarks = [
            Data(
                input_data='Remarks Test Occurred',
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                re_parse_output=True,
                output_file_name_keyword=r'output'
            ),
            Data(
                input_data=['Remarks TEst', 'Remarks Testing'],
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                re_parse_output=True,
                output_file_name_keyword=r'output'
            ),
            Data(
                remarks='Remarks Test Group',
                input_data=['TEst', 'Testing'],
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                re_parse_output=True,
                output_file_name_keyword=r'output'
            ),
            Data(
                remarks=' Remarks Test Group Extra Space Single ',
                input_data='TEst',
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                re_parse_output=True,
            ),
            Data(
                remarks=' Remarks Test Group Extra Space Multi    ',
                input_data=['TEst', 'Testing'],
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                re_parse_output=True,
            ),
            #
            Data(
                remarks=['Remarks semi colon 1;', 'Remarks semi colon 2; '],
                input_data=['TEst', 'Testing'],
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                re_parse_output=True,
            ),
            #
            Data(
                remarks=['Remarks semi colon 1; colon 1;   colon 1;', 'Remarks semi colon 2; '],
                input_data=['TEst', 'Testing'],
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                re_parse_output=True,
            ),
            Data(
                remarks='Remarks StoreMetadataRequest Testing Individual',
                input_data="BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031",
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=r'output',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest
            ),
            Data(
                remarks='Remarks Testing Individual',
                input_data="BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031",
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=r'output',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest
            ),
            Data(
                input_data="BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031",
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=r'output',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest
            ),
            Data(
                remarks='Error ruamel.yaml.representer.RepresenterError: cannot represent an object: <ProfileInfoListResponse (CHOICE)>',
                input_data='bf2a0499020520',
                asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=KeyWords.OUTPUT_FILE_NAME_KEYWORD
            ),
            Data(
                remarks='Remarks StoreMetadataRequest Testing Group',
                input_data=[
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640'
                ],
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=r'output',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest
            ),
            Data(
                remarks='Remarks Testing Group',
                input_data=[
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640'
                ],
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=r'output',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest
            ),
            Data(
                input_data=[
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640'
                ],
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=r'output',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest
            ),
            #
            Data(
                remarks='This is a long remakrs for the testing of Trimming of remarks of individual item of the pool in asn play.',
                input_data='test',
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
            ),
            #
            Data(
                remarks='This is a long remakrssssssssssssssss for the testing of Trimming of remarks of individual item of the pool in asn play.',
                input_data='test',
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
            ),
            #
            Data(
                remarks='This is a long remakrssssssssssssssssssssssssssssssssssss for the testing of Trimming of remarks of individual item of the pool in asn play.',
                input_data='test',
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
            ),
            #
            Data(
                input_data='This is a long dataaaa for the testing of Trimming of remarks of individual item of the pool in asn play.',
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
            ),
            #
            Data(
                input_data='This is a long dataaaaaaaaaaaaaaaaaaa for the testing of Trimming of remarks of individual item of the pool in asn play.',
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
            ),
            #
            Data(
                input_data='This is a long dataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa for the testing of Trimming of remarks of individual item of the pool in asn play.',
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
            ),
            #
            Data(
                remarks='This is a long remakrss for the testing of Trimming of remarks of individual item of the pool in asn play.',
                input_data=['test'] * 100,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
            ),
            #
            Data(
                input_data=[
                               'This is a long dataaaaa for the testing of Trimming of remarks of individual item of the pool in asn play.'
                           ] * 100,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                print_input=False,
                print_output=False,
            ),
            #
            Data(
                input_data=[
                               'This is a long dataaaaaaa for the testing of Trimming of remarks of individual item of the pool in asn play.'
                           ] * 10,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                print_input=False,
                print_output=False,
            ),
            #
            Data(
                input_data=Folders.in_sample_sgp_22(r'v3_0_0\StoreMetadataRequest\StoreMetadataRequest_wo_icon.hex'),
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
            ),
            #
            Data(
                input_data=r'D:\Other\Github_Self\asn1Play\data\sample_data\GSMA\SGP_22\v3_0_0\StoreMetadataRequest\StoreMetadataRequest_wo_icon_wo_serviceSpecific.asn1',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
            ),
        ]

        data_pool_remarks_extend = [
            Data(
                remarks=['Extend Remarks List Sample', 'Extend Remarks List'],
                input_data=[
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
                ],
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1,
                output_path=Folders.in_user_sgp_22(
                    [PhVariables.VERSION, 'StoreMetadataRequest', 'StoreMetadataRequest_wo_icon.base64']),
            ),
            Data(
                remarks=['Extend Remarks List Sample', 'Extend Remarks List'],
                input_data=[
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
                ],
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1,
                output_path=Folders.in_user_sgp_22([PhVariables.VERSION, 'StoreMetadataRequest']),
            ),
        ]

        data_pool_output_file = [
            #
            Data(
                input_data=['Test1', 'Test2', 'Test3'],
                asn1_element=None,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                output_path=Folders.in_user(r'Temp\Pj.txt'),
            ),
            #
            Data(
                remarks=['T1', 'T2', 'T3'],
                input_data=['Test1', 'Test2', 'Test3'],
                asn1_element=None,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                output_path=Folders.in_user(r'Temp\Pj.txt'),
            ),
            #
            Data(
                remarks=['T1', 'T2', 'T3'],
                input_data=['Test1', 'Test2', 'Test3'],
                asn1_element=None,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                output_path=Folders.in_user(fr'Temp\Pj{PhVariables.ITEM_INDEX}.txt'),
            ),
            #
            Data(
                remarks=['T1', 'T2'],
                input_data=['Test1', 'Test2', 'Test3'],
                asn1_element=None,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                output_path=Folders.in_user(r'Temp\Pj.txt'),
            ),
            #
            Data(
                remarks=['test 1'],
                input_data='bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                print_input=False,
                print_output=False,
                output_path=Folders.in_user(r'Bulk_export\.txt'),
            ),
            #
            Data(
                input_data=['Test4', 'Test5', 'Test6'],
                asn1_element=None,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                output_path=Folders.in_user(r'Temp\\'),
            ),
            #
            Data(
                input_data=['Test4', 'Test5', 'Test6'],
                asn1_element=None,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                output_path=Folders.in_user(r'Temp/'),
            ),
            #
            Data(
                input_data=['Test7', 'Test8', 'Test9'],
                asn1_element=None,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                output_path=Folders.in_user(r'Temp'),
            ),
            #
            Data(
                remarks=['test 1', 'test 2', 'test 3'],
                input_data=[
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
                ],
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                print_input=False,
                print_output=False,
                output_path=Folders.in_user(r'Bulk_export\.txt'),
            ),
            #
            Data(
                remarks=['test 1', 'test 2', 'test 3'],
                input_data=[
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
                ],
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                print_input=False,
                print_output=False,
                output_path=Folders.in_user(r'Bulk_export'),
            ),
        ]

        data_pool_asn1_element = [
            #
            Data(
                remarks='SGP_22.RSPDefinitions.StoreMetadataRequest',
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
            ),
            #
            Data(
                remarks="StoreMetadataRequest",
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                asn1_element='StoreMetadataRequest',
            ),
            #
            Data(
                remarks="asn1_element='SGP_22.RSPDefinitions.StoreMetadataRequest'",
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                asn1_element='SGP_22.RSPDefinitions.StoreMetadataRequest',
            ),
            #
            Data(
                remarks='InvalidAsnElement WhiteSpace',
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                asn1_element=' ',
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks='Conversion Needed, AsnElement is whiteSpace',
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                asn1_element=' ',
                input_format=Formats.ASCII,
                output_format=Formats.HEX
            ),
            #
            Data(
                remarks='InvalidAsnElement',
                input_data=Folders.in_user_sgp_22(fr'{PhVariables.VERSION}\InvalidRequest\StoreMetadataReques.yml'),
            ),
            #
            Data(
                remarks='Invalid asn1_element (unknown str)',
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                asn1_element='s1',
            ),
            #
            Data(
                remarks='Invalid asn1_element (unknown str)',
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                asn1_element='StoreMetadataReques',
            ),
            #
            Data(
                remarks='Invalid asn1_element (class name as str)',
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                asn1_element='SGP_22.RSPDefinitions.StoreMetadataRequest',
            ),
            #
            Data(
                input_data=Folders.in_sample_sgp_22(r'v3_0_0\StoreMetadataRequest\StoreMetadataRequest_wo_icon.hex'),
            ),
            #
            Data(
                input_data=Folders.in_sample_sgp_22(
                    r'v3_0_0\StoreMetadataRequest\StoreMetadataRequest_wo_icon_wo_serviceSpecific.asn1'),
            ),
            #
        ]

        data_pool_tlv = [
            #
            Data(
                remarks='DER; tlv_parsing_of_output=True',
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                input_format=Formats.DER,
                output_format=Formats.DER,
                tlv_parsing_of_output=True
            ),
            #
            Data(
                remarks='DER_64; tlv_parsing_of_output=True',
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                input_format=Formats.DER,
                output_format=Formats.DER_64,
                tlv_parsing_of_output=True
            ),
            #
            Data(
                remarks='Ascii; tlv_parsing_of_output=True',
                input_data='57656c636f6d6520546f2041736e506c617920212121',
                input_format=Formats.HEX,
                output_format=Formats.ASCII,
                tlv_parsing_of_output=True
            ),
            #
        ]

        data_pool_output_file_keyword = [
            #
            Data(
                remarks=['test 1', 'test 2', 'test 3'],
                input_data=[
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
                ],
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                print_input=False,
                print_output=False,
                output_file_name_keyword=KeyWords.OUTPUT_FILE_NAME_KEYWORD
            ),
            Data(
                input_data=fr'D:\Other\Github_Self\asn1Play\data\sample_data\GSMA\SGP_22\{PhVariables.VERSION}\UpdateMetadataRequest',
                asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest,
                output_file_name_keyword='output'
            )
        ]

        data_pool_web_requests = [
            #
            {
                PhKeys.REMARKS: 'Web Request; asn1_element;',
                PhKeys.INPUT_DATA: 'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                PhKeys.INPUT_FORMAT: Formats.DER,
                PhKeys.OUTPUT_FORMAT: Formats.ASN1,
                PhKeys.ASN1_ELEMENT: SGP_22.RSPDefinitions.StoreMetadataRequest
            },
            {
                PhKeys.REMARKS: 'Web Request; asn1_schema; asn1_object;',
                PhKeys.INPUT_DATA: 'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                PhKeys.INPUT_FORMAT: Formats.DER,
                PhKeys.OUTPUT_FORMAT: Formats.ASN1,
                PhKeys.ASN1_SCHEMA: 'GSMA_SGP_22_v3_0_0',
                PhKeys.ASN1_OBJECT: 'StoreMetadataRequest',
            },
            {
                PhKeys.REMARKS: 'Web Request; asn1_schema; asn1_object; Extra Quotation',
                PhKeys.INPUT_DATA: '"BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640"',
                PhKeys.INPUT_FORMAT: Formats.DER,
                PhKeys.OUTPUT_FORMAT: Formats.ASN1,
                PhKeys.ASN1_SCHEMA: 'GSMA_SGP_22_v3_0_0',
                PhKeys.ASN1_OBJECT: 'StoreMetadataRequest',
            },
            {
                PhKeys.REMARKS: 'Web Request; asn1_object_alternate;',
                PhKeys.INPUT_DATA: 'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                PhKeys.INPUT_FORMAT: Formats.DER,
                PhKeys.OUTPUT_FORMAT: Formats.ASN1,
                PhKeys.ASN1_SCHEMA: 'GSMA_SGP_22_v3_0_0',
                PhKeys.ASN1_OBJECT_ALTERNATE: 'StoreMetadataRequest'
            },
            {
                PhKeys.REMARKS: 'Web Request; asn1_object; asn1_object_alternate;',
                PhKeys.INPUT_DATA: 'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                PhKeys.INPUT_FORMAT: Formats.DER,
                PhKeys.OUTPUT_FORMAT: Formats.ASN1,
                PhKeys.ASN1_SCHEMA: 'GSMA_SGP_22_v3_0_0',
                PhKeys.ASN1_OBJECT: 'StoreMetadataRequest',
                PhKeys.ASN1_OBJECT_ALTERNATE: 'StoreMetadataRequest'
            },
            {
                PhKeys.REMARKS: 'Web Request; fetch_asn1_objects; True',
                PhKeys.ASN1_SCHEMA: Asn1Versions.GSMA_SGP_22_v3_1.get_name(),
                PhKeys.FETCH_ASN1_OBJECTS_LIST: True,
            },
            {
                PhKeys.REMARKS: 'Web Request; fetch_asn1_objects; False',
                PhKeys.ASN1_SCHEMA: Asn1Versions.GSMA_SGP_22_v3_1.get_name(),
                PhKeys.FETCH_ASN1_OBJECTS_LIST: False,
            },
            {
                PhKeys.REMARKS: 'Web Request; fetch_asn1_objects; True (str)',
                PhKeys.ASN1_SCHEMA: Asn1Versions.GSMA_SGP_22_v3_1.get_name(),
                PhKeys.FETCH_ASN1_OBJECTS_LIST: 'True',
            },
            {
                PhKeys.REMARKS: 'Web Request; fetch_asn1_objects; False (str)',
                PhKeys.ASN1_SCHEMA: Asn1Versions.GSMA_SGP_22_v3_1.get_name(),
                PhKeys.FETCH_ASN1_OBJECTS_LIST: 'False',
            },
            {
                PhKeys.REMARKS: 'Web Request; fetch_asn1_objects; sgp32; True',
                PhKeys.ASN1_SCHEMA: Asn1Versions.GSMA_SGP_32_v1_0.get_name(),
                PhKeys.FETCH_ASN1_OBJECTS_LIST: True,
            },
            {
                PhKeys.REMARKS: 'Web Request; Byte Array',
                PhKeys.INPUT_DATA: '[10, -68, -46, 85]',
                PhKeys.INPUT_FORMAT: Formats.DER_BYTE_ARRAY,
                PhKeys.OUTPUT_FORMAT: Formats.DER,
            },
        ]

        data_pool_asn_element_with_schema = [
            #####
            # DER to ASN1
            #####
            #
            Data(
                input_data=Folders.in_sample_sgp_22(
                    fr'{PhVariables.VERSION}\StoreMetadataRequest\StoreMetadataRequest.hex'),
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v3_0_0, 'StoreMetadataRequest'),
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                input_data=Folders.in_sample_sgp_22(
                    fr'{PhVariables.VERSION}\StoreMetadataRequest\StoreMetadataRequest.hex'),
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v2_4, 'StoreMetadataRequest'),
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                input_data=Folders.in_sample_sgp_22(
                    fr'{PhVariables.VERSION}\StoreMetadataRequest\StoreMetadataRequest.hex'),
                asn1_element='StoreMetadataRequest',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                input_data=Folders.in_sample_sgp_22(
                    fr'{PhVariables.VERSION}\StoreMetadataRequest\StoreMetadataRequest.hex'),
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #####
            # ASN1 to DER
            #####
            #
            Data(
                input_data=Folders.in_sample_sgp_22(
                    fr'{PhVariables.VERSION}\StoreMetadataRequest\StoreMetadataRequest_Mandatory.asn1'),
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v3_0_0, 'StoreMetadataRequest'),
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            #
            Data(
                input_data=Folders.in_sample_sgp_22(
                    fr'{PhVariables.VERSION}\StoreMetadataRequest\StoreMetadataRequest_Mandatory.asn1'),
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v2_4, 'StoreMetadataRequest'),
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            #
            Data(
                input_data=Folders.in_sample_sgp_22(
                    fr'{PhVariables.VERSION}\StoreMetadataRequest\StoreMetadataRequest_Mandatory.asn1'),
                asn1_element='StoreMetadataRequest',
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            #
            Data(
                input_data=Folders.in_sample_sgp_22(
                    fr'{PhVariables.VERSION}\StoreMetadataRequest\StoreMetadataRequest_Mandatory.asn1'),
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            #####
            # ASN1 to DER; eUICC_Profile_Package
            #####
            #
            Data(
                input_data=Folders.in_sample_epp(fr'{PhVariables.VERSION}\PE_End.asn1'),
                asn1_element=Asn1(Asn1Versions.TCA_EPP_v3_1, 'PE_End'),
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            #
            Data(
                input_data=Folders.in_sample_epp(fr'{PhVariables.VERSION}\PE_End.asn1'),
                asn1_element=Asn1(Asn1Versions.TCA_EPP_v3_2, 'PE_End'),
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            # negative scenario
            Data(
                input_data=Folders.in_sample_epp(fr'{PhVariables.VERSION}\PE_End.asn1'),
                asn1_element='PE_End',
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            #
            Data(
                input_data=Folders.in_sample_epp(fr'{PhVariables.VERSION}\PE_End.asn1'),
                asn1_element=eUICC_Profile_Package.PEDefinitions.PE_End,
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            #####
            # Mix Flow
            #####
            #
            Data(
                input_data=Folders.in_sample_sgp_22(
                    fr'{PhVariables.VERSION}\StoreMetadataRequest\StoreMetadataRequest.hex'),
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v3_0_0, 'StoreMetadataRequest'),
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                input_data=Folders.in_sample_sgp_22(
                    fr'{PhVariables.VERSION}\StoreMetadataRequest\StoreMetadataRequest.hex'),
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v2_4, 'StoreMetadataRequest'),
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                input_data=Folders.in_sample_sgp_22(
                    fr'{PhVariables.VERSION}\StoreMetadataRequest\StoreMetadataRequest.hex'),
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                input_data=Folders.in_sample_epp(fr'{PhVariables.VERSION}\PE_End.asn1'),
                asn1_element=eUICC_Profile_Package.PEDefinitions.PE_End,
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
        ]

        data_pool_negative = [
            #
            Data(
                remarks='input_data is empty',
                input_data='',
                asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks='input_data is None',
                input_data=None,
                asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks='InvalidInputFormat',
                input_data=Folders.in_user_sgp_22(
                    fr'{PhVariables.VERSION}\InvalidRequest\StoreMetadataRequest_inp_derr.yml'),
            ),
            #
            Data(
                remarks='InvalidInputFormat',
                input_data=Folders.in_user_sgp_22(
                    fr'{PhVariables.VERSION}\InvalidRequest\StoreMetadataRequest_inp_derr_formats.yml'),
            ),
            #
            Data(
                remarks='InvalidOutputFormat',
                input_data=Folders.in_user_sgp_22(
                    fr'{PhVariables.VERSION}\InvalidRequest\StoreMetadataRequest_op_asn2.yml'),
            ),
            #
            Data(
                remarks='InvalidOutputFormat',
                input_data=Folders.in_user_sgp_22(
                    fr'{PhVariables.VERSION}\InvalidRequest\StoreMetadataRequest_op_asn2_formats.yml'),
            ),
            #
            Data(
                remarks='Invalid File Path',
                input_data=r'D:\Other\Github_Self\asn1Play\sample_data\GSMA\SGP_22\UpdateMetadataRequest\t',
                asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest,
                output_file_name_keyword='output'
            ),
            #
            Data(
                remarks='Invalid input_data (base 64 conversion failure)',
                input_data='testt',
                input_format=Formats.DER,
                output_format=Formats.DER,
            ),
            #
            Data(
                remarks='Invalid input_data (base 64 conversion failure)',
                input_data='testt',
                input_format=Formats.DER,
                output_format=Formats.DER_64,
            ),
            #
            Data(
                remarks='Invalid input_data (base 64 conversion failure)',
                input_data='D:\e\AC\DeleteProfileRequest.he',
            ),
            #
            Data(
                remarks='Invalid input_data (base 64 conversion failure)',
                input_data='D:\e\AC\DeleteProfileRequest.he',
                input_format=Formats.DER,
                output_format=Formats.DER_64
            ),
            #
            Data(
                remarks='Invalid input_data (base 64 conversion failure)',
                input_data='D:\e\AC\DeleteProfileRequest.he',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                asn1_element='StoreMetadataRequest',
            ),
            #
            Data(
                remarks='Invalid input_data (base 64 conversion failure)',
                input_data='D:\e\AC\DeleteProfileRequest.he',
                input_format=Formats.ASN1,
                output_format=Formats.DER,
                asn1_element='StoreMetadataRequest',
            ),
            #
            Data(
                remarks='Invalid input_data (Brackets MisMatch)',
                input_data="""{
  iccid '989209012143658709F5'H,
  serviceProviderName "SP Name 1",
  profileName "Operational Profile Name 1",
  iconType 1 -- png --,
  profileOwner {
    mccMnc '92F918'H
  }
  },
  profilePolicyRules '01'B -- ppr1 --
}""",
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.ASN1,
                output_format=Formats.DER
            ),
            #
            Data(
                remarks='# FileExistsError Error',
                input_data=[
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                ],
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1,
                output_path=Folders.in_user_sgp_22(
                    fr'{PhVariables.VERSION}\\StoreMetadataRequest\\Extend_Remarks_List_Item_3.asn1\\')
            ),
            #
            Data(
                remarks='Requested conversion is not possible...',
                input_data='8929901012345678905F',
                input_format=Formats.HEX,
                output_format=Formats.TXT
            ),
            #
            Data(
                remarks='Unknown Data (bytes buffer not long enough)',
                input_data=r'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031990206',
                asn1_element='StoreMetadataRequest',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
        ]

        data_pool_json = [
            #
            Data(
                input_data=Folders.in_sample_sgp_22(
                    fr'{PhVariables.VERSION}\StoreMetadataRequest\StoreMetadataRequest_Mandatory.asn1'),
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            #
            Data(
                input_data="""{
         "iccid": "989209012143658709f5",
         "profileName": "Operational Profile Name 1",
         "serviceProviderName": "SP Name 1"
        }""",
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v2_4, 'StoreMetadataRequest'),
                input_format=Formats.JSON,
                output_format=Formats.DER,
            ),
            #
            Data(
                input_data="""{
         "iccid": "989209012143658709f5",
         "profileName": "Operational Profile Name 1",
         "serviceProviderName": "SP Name 1"
        }""",
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v2_4, 'StoreMetadataRequest'),
                input_format=Formats.JSON,
                output_format=Formats.ASN1,
            ),
            #
        ]

        data_pool_asn1_to_all_formats = []
        for output_format in FormatsGroup.OUTPUT_FORMATS_SUPPORTED:
            data_pool_asn1_to_all_formats.append(
                Data(
                    remarks=f"Output Format is {output_format}",
                    input_data=Folders.in_sample_sgp_22(
                        fr'{PhVariables.VERSION}\StoreMetadataRequest\StoreMetadataRequest_Mandatory.asn1'),
                    asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                    input_format=Formats.ASN1,
                    output_format=output_format,
                )
            )

        data_pool_reported = [
            #
            Data(
                remarks='Reported; DER to JSON | JSON to DER conversion #3; Json to Der',
                input_data=Folders.in_user_sgp_32(r'v1_0_1\GetEimPackageResponse\GetEimPackageResponse.json'),
                asn1_element=SGP_32.SGP32Definitions.GetEimPackageResponse,
                input_format=Formats.JSON,
                output_format=Formats.DER,
            ),
            #
            Data(
                remarks='Reported; DER to JSON | JSON to DER conversion #3; Json to Asn1',
                input_data=Folders.in_user_sgp_32(r'v1_0_1\GetEimPackageResponse\GetEimPackageResponse.json'),
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_32_v1_0_1, 'GetEimPackageResponse'),
                input_format=Formats.JSON,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                remarks='Reported; DER to JSON | JSON to DER conversion #3; Der to Json',
                input_data=r'bf4f81a2bf51819e3059802445374246384646352d353642462d333838312d384639462d3236454338453633424646375a10730f11567c634e3399fbabd91a9e5726810103a01ca40c5a0a8929901012345678905fa40c5a0a8929901012345678905f5f374080d82b20d657f8956858ca38848c337783a7c5793429b7edcc724d7d490cbc85c38408c4bd39dd756478928ce26624c0d71e8b781ef5e56cf0f1398f494385cb',
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_32_v1_0_1, 'GetEimPackageResponse'),
                input_format=Formats.DER,
                output_format=Formats.JSON,
            ),
            #
            Data(
                remarks='Reported; DER to JSON | JSON to DER conversion #3; Der to asn1',
                input_data=r'bf4f81a2bf51819e3059802445374246384646352d353642462d333838312d384639462d3236454338453633424646375a10730f11567c634e3399fbabd91a9e5726810103a01ca40c5a0a8929901012345678905fa40c5a0a8929901012345678905f5f374080d82b20d657f8956858ca38848c337783a7c5793429b7edcc724d7d490cbc85c38408c4bd39dd756478928ce26624c0d71e8b781ef5e56cf0f1398f494385cb',
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_32_v1_0_1, 'GetEimPackageResponse'),
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                remarks='Reported; Json not getting parsed to Asn1 #6',
                input_data="""{
                "ipaEuiccDataResponse": {
                "ipaEuiccData": {
                "euiccCertificate": "",
                }
                }
                }""",
                input_format=Formats.JSON,
                output_format=Formats.DER,
                asn1_element=SGP_32.SGP32Definitions.IpaEuiccDataResponse,
            ),
            #
            Data(
                remarks='Reported; Json not getting parsed to Asn1 #6; Corrected structure',
                input_data=""" {
         "ipaEuiccData": {
          "euiccCertificate": ""
         }
        }""",
                input_format=Formats.JSON,
                output_format=Formats.DER,
                asn1_element=SGP_32.SGP32Definitions.IpaEuiccDataResponse,
            ),
            #
            Data(
                remarks='Reported; Json not getting parsed to Asn1 #6; Corrected structure',
                input_data="""{
         "ipaEuiccData": {
          "defaultSmdpAddress": "smdp.amenitypj.in"
         }
        }""",
                input_format=Formats.JSON,
                output_format=Formats.DER,
                asn1_element=SGP_32.SGP32Definitions.IpaEuiccDataResponse,
            ),
            #
            Data(
                remarks='Reported; Json not getting parsed to Asn1 #6; Empty ipaEuiccData',
                input_data="""{
                            "ipaEuiccData": {}
                          }
            """,
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_32_v1_0_1, 'IpaEuiccDataResponse'),
                input_format=Formats.JSON,
                output_format=Formats.ASN1,
            ),
        ]

        data_pool_self_correction = [
            # TODO: Need to Handle with Self Fix
            #
            Data(
                remarks='Hex to Ascii; Non Printable Characters (like new line)',
                input_data='500D0A50',
                input_format=Formats.HEX,
                output_format=Formats.ASCII,
            ),
            #
            Data(
                remarks='Hex to Ascii; (Non UTF) input data conversion is not possible; Input Data ',
                input_data='\x85',
                input_format=Formats.HEX,
                output_format=Formats.ASCII,
            ),
            #
            Data(
                remarks='Hex to Ascii; expected str, bytes or os.PathLike object, not int',
                input_data='85',
                input_format=Formats.HEX,
                output_format=Formats.ASCII,
            ),
            {
                PhKeys.REMARKS: 'Web Request; Hex to Ascii; (Non UTF) input data conversion is not possible; Input Data: ',
                PhKeys.INPUT_DATA: '\x85',
                PhKeys.INPUT_FORMAT: Formats.HEX,
                PhKeys.OUTPUT_FORMAT: Formats.ASCII,
            },
            {
                PhKeys.REMARKS: 'Web Request; Hex to Ascii; non-hexadecimal number found in fromhex()',
                PhKeys.INPUT_DATA: '\85',
                PhKeys.INPUT_FORMAT: Formats.HEX,
                PhKeys.OUTPUT_FORMAT: Formats.ASCII,
            },
        ]
        #
        data_pool_type_casting_boolean = [
            #
            Data(
                remarks='print_input is having garbage string',
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                print_input='gkjghkg',
            ),
            #
            Data(
                remarks='print_input is having valid Boolean value (True) as string',
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                print_input='True',
            ),
            #
            Data(
                remarks='print_input is having valid Boolean value (False) as string',
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                print_input='False',
            ),
            #
            Data(
                remarks='print_input is having valid Boolean value (True)',
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                print_input=True,
            ),
            #
            Data(
                remarks='print_input is having valid Boolean value (False)',
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                print_input=False,
            ),
            #
            Data(
                remarks='print_input is having valid Boolean value (faLsE)',
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                print_input='faLsE',
            ),
            #
        ]
        #
        data_pool_type_casting_boolean_web_request = [
            #
            {
                PhKeys.REMARKS: 'dict; print_input is having garbage string',
                PhKeys.INPUT_DATA: 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                PhKeys.ASN1_ELEMENT: 'StoreMetadataRequest',
                PhKeys.INPUT_FORMAT: 'der',
                PhKeys.OUTPUT_FORMAT: 'asn1',
                PhKeys.PRINT_INPUT: 'gkjghkg',
            },
            #
            {
                PhKeys.REMARKS: 'dict; print_input is having valid Boolean value (True) as string',
                PhKeys.INPUT_DATA: 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                PhKeys.ASN1_ELEMENT: 'StoreMetadataRequest',
                PhKeys.INPUT_FORMAT: 'der',
                PhKeys.OUTPUT_FORMAT: 'asn1',
                PhKeys.PRINT_INPUT: 'True',
            },
            #
            {
                PhKeys.REMARKS: 'dict; print_input is having valid Boolean value (False) as string',
                PhKeys.INPUT_DATA: 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                PhKeys.ASN1_ELEMENT: 'StoreMetadataRequest',
                PhKeys.INPUT_FORMAT: 'der',
                PhKeys.OUTPUT_FORMAT: 'asn1',
                PhKeys.PRINT_INPUT: 'False',
            },
            #
            {
                PhKeys.REMARKS: 'dict; print_input is having valid Boolean value (true) as string',
                PhKeys.INPUT_DATA: 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                PhKeys.ASN1_ELEMENT: 'StoreMetadataRequest',
                PhKeys.INPUT_FORMAT: 'der',
                PhKeys.OUTPUT_FORMAT: 'asn1',
                PhKeys.PRINT_INPUT: 'true',
            },
            #
            {
                PhKeys.REMARKS: 'dict; print_input is having valid Boolean value (false) as string',
                PhKeys.INPUT_DATA: 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                PhKeys.ASN1_ELEMENT: 'StoreMetadataRequest',
                PhKeys.INPUT_FORMAT: 'der',
                PhKeys.OUTPUT_FORMAT: 'asn1',
                PhKeys.PRINT_INPUT: 'false',
            },
            #
            {
                PhKeys.REMARKS: 'dict; print_input is having valid Boolean value (faLsE) as string',
                PhKeys.INPUT_DATA: 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                PhKeys.ASN1_ELEMENT: 'StoreMetadataRequest',
                PhKeys.INPUT_FORMAT: 'der',
                PhKeys.OUTPUT_FORMAT: 'asn1',
                PhKeys.PRINT_INPUT: 'faLsE',
            },
            #
        ]
        #
        data_pool_type_casting_string = [
            #
            #
            Data(
                remarks='input_format is having garbage string',
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format='Kuch Bhi',
                output_format=Formats.ASN1,
                print_input=True,
            ),
            #
            Data(
                remarks='input_format is having valid value as string (Capital)',
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format='DER',
                output_format=Formats.ASN1,
                print_input=True,
            ),
            #
            Data(
                remarks='input_format is having valid value as string (Lower)',
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format='der',
                output_format=Formats.ASN1,
                print_input=True,
            ),
            #
            Data(
                remarks='input_format is having valid value as string (Mix case)',
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format='dEr',
                output_format=Formats.ASN1,
                print_input=True,
            ),
        ]
        #
        data_pool_type_casting_string_web_request = [
            #
            {
                PhKeys.REMARKS: 'dict; input_format is having garbage string',
                PhKeys.INPUT_DATA: 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                PhKeys.ASN1_ELEMENT: 'StoreMetadataRequest',
                PhKeys.INPUT_FORMAT: 'Kuch Bhi',
                PhKeys.OUTPUT_FORMAT: 'asn1',
                PhKeys.PRINT_INPUT: 'True',
            },
            #
            {
                PhKeys.REMARKS: 'dict; input_format is having valid value as string (Capital)',
                PhKeys.INPUT_DATA: 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                PhKeys.ASN1_ELEMENT: 'StoreMetadataRequest',
                PhKeys.INPUT_FORMAT: 'DER',
                PhKeys.OUTPUT_FORMAT: 'asn1',
                PhKeys.PRINT_INPUT: 'True',
            },
            #
            {
                PhKeys.REMARKS: 'dict; input_format is having valid value as string (lower)',
                PhKeys.INPUT_DATA: 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                PhKeys.ASN1_ELEMENT: 'StoreMetadataRequest',
                PhKeys.INPUT_FORMAT: 'der',
                PhKeys.OUTPUT_FORMAT: 'asn1',
                PhKeys.PRINT_INPUT: 'True',
            },
            #
            {
                PhKeys.REMARKS: 'dict; input_format is having valid value as string (Mix case)',
                PhKeys.INPUT_DATA: 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                PhKeys.ASN1_ELEMENT: 'StoreMetadataRequest',
                PhKeys.INPUT_FORMAT: 'dEr',
                PhKeys.OUTPUT_FORMAT: 'asn1',
                PhKeys.PRINT_INPUT: 'True',
            },
        ]
        #
        data_pool_dicts = [
            #
            Data(
                remarks='SGP22; StoreMetadataRequest as Dict',
                input_data={
                    'StoreMetadataRequest': 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031'
                },
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            {
                PhKeys.REMARKS: 'SGP22; StoreMetadataRequest as Dict; Web Request',
                PhKeys.INPUT_DATA: {
                    'StoreMetadataRequest': 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031'
                },
                PhKeys.INPUT_FORMAT: Formats.DER,
                PhKeys.OUTPUT_FORMAT: Formats.ASN1,
            },
            #
            Data(
                remarks=f'SGP22; Dict w multiple unrelated keys; {PhVariables.ASN1_ELEMENT};',
                input_data={
                    "EUICCInfo1": "vyBhggMCAQCpLAQU9UFyvfmKldZcvriKOKHBHYAKhcMEFMC8cLo2kp1DtGf/V1cFMOV6uPzYqiwEFPVBcr35ipXWXL64ijihwR2ACoXDBBTAvHC6NpKdQ7Rn/1dXBTDlerj82A==",
                    'StoreMetadataRequest': 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                },
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            {
                PhKeys.REMARKS: f'SGP22; Dict w multiple unrelated keys; {PhVariables.ASN1_ELEMENT}; Web Request;',
                PhKeys.INPUT_DATA: {
                    "EUICCInfo1": "vyBhggMCAQCpLAQU9UFyvfmKldZcvriKOKHBHYAKhcMEFMC8cLo2kp1DtGf/V1cFMOV6uPzYqiwEFPVBcr35ipXWXL64ijihwR2ACoXDBBTAvHC6NpKdQ7Rn/1dXBTDlerj82A==",
                    'StoreMetadataRequest': 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                },
                PhKeys.INPUT_FORMAT: Formats.DER,
                PhKeys.OUTPUT_FORMAT: Formats.ASN1,
            },
            #
            Data(
                remarks=f'SGP22; InitiateAuthentication Dict; {PhVariables.ASN1_ELEMENT};',
                input_data={
                    "EUICCInfo1": "vyBhggMCAQCpLAQU9UFyvfmKldZcvriKOKHBHYAKhcMEFMC8cLo2kp1DtGf/V1cFMOV6uPzYqiwEFPVBcr35ipXWXL64ijihwR2ACoXDBBTAvHC6NpKdQ7Rn/1dXBTDlerj82A==",
                    "euiccChallenge": "DOEKZlP8xS8i7GwFcyEZfQ==",
                    "smdpAddress": "testsmdpplus1.example.com",
                },
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            {
                PhKeys.REMARKS: f'SGP22; InitiateAuthentication Dict; {PhVariables.ASN1_ELEMENT}; Web Request;',
                PhKeys.INPUT_DATA: {
                    "EUICCInfo1": "vyBhggMCAQCpLAQU9UFyvfmKldZcvriKOKHBHYAKhcMEFMC8cLo2kp1DtGf/V1cFMOV6uPzYqiwEFPVBcr35ipXWXL64ijihwR2ACoXDBBTAvHC6NpKdQ7Rn/1dXBTDlerj82A==",
                    "euiccChallenge": "DOEKZlP8xS8i7GwFcyEZfQ==",
                    "smdpAddress": "testsmdpplus1.example.com",
                },
                PhKeys.INPUT_FORMAT: Formats.DER,
                PhKeys.OUTPUT_FORMAT: Formats.ASN1,
            },
        ]
        #
        super().set_data_pool(
            data_pool_positive
            + data_pool_byte_array
            + data_pool_remarks
            + data_pool_remarks_extend
            + data_pool_output_file
            + data_pool_output_file_keyword
            + data_pool_asn1_element
            + data_pool_tlv
            + data_pool_asn_element_with_schema
            + data_pool_web_requests
            + data_pool_negative
            + data_pool_json
            + data_pool_asn1_to_all_formats
            + data_pool_reported
            + data_pool_self_correction
            + data_pool_type_casting_boolean
            + data_pool_type_casting_boolean_web_request
            + data_pool_type_casting_string
            + data_pool_type_casting_string_web_request
            + data_pool_dicts
        )
