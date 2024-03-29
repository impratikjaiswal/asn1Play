from python_helpers.ph_keys import PhKeys

from asn1_play.generated_code.asn1.GSMA import SGP_22
from asn1_play.generated_code.asn1.TCA import eUICC_Profile_Package
from asn1_play.generated_code.asn1.asn1 import Asn1
from asn1_play.generated_code.asn1.asn1_versions import Asn1Versions
from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.helper.data import Data
from asn1_play.main.helper.formats import Formats
from asn1_play.main.helper.keywords import KeyWords


class UnitTesting(DataTypeMaster):

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

    def set_remarks_list(self):
        remarks_list = None
        super().set_remarks_list(remarks_list)

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
        data_pool_positive = [
            #
            Data(  # #YmlInput #ExportKeyword
                raw_data=r'..\..\Data\UserData\Generic\ASCII\hex_to_ascii_exp.yml'
            ),
            #
            Data(
                remarks_list='Input Data with White spaces',
                raw_data='bf2a   04 99 02 05 20    ',
                asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks_list='Input Data with List',
                raw_data=[
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
                raw_data=[10, -68, -46, 85],
                input_format=Formats.BYTE_ARRAY,
                output_format=Formats.DER,
            ),
            # Byte Array with Remarks
            Data(
                remarks_list='Byte Array with Remarks',
                raw_data=[10, -68, -46, 85],
                input_format=Formats.BYTE_ARRAY,
                output_format=Formats.DER,
            ),
            #
            Data(
                raw_data=[10, 188, 210, 85],
                input_format=Formats.BYTE_ARRAY,
                output_format=Formats.DER_64,
            )
        ]

        data_pool_remarks = [
            Data(
                raw_data='Remarks Test Occurred',
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                re_parse_output=True,
                output_file_name_keyword=r'output'
            ),
            Data(
                raw_data=['Remarks TEst', 'Remarks Testing'],
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                re_parse_output=True,
                output_file_name_keyword=r'output'
            ),
            Data(
                remarks_list='Remarks Test Group',
                raw_data=['TEst', 'Testing'],
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                re_parse_output=True,
                output_file_name_keyword=r'output'
            ),
            Data(
                remarks_list=' Remarks Test Group Extra Space Single ',
                raw_data='TEst',
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                re_parse_output=True,
            ),
            Data(
                remarks_list=' Remarks Test Group Extra Space Multi    ',
                raw_data=['TEst', 'Testing'],
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                re_parse_output=True,
            ),
            #
            Data(
                remarks_list=['Remarks semi colon 1;', 'Remarks semi colon 2; '],
                raw_data=['TEst', 'Testing'],
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                re_parse_output=True,
            ),
            #
            Data(
                remarks_list=['Remarks semi colon 1; colon 1;   colon 1;', 'Remarks semi colon 2; '],
                raw_data=['TEst', 'Testing'],
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                re_parse_output=True,
            ),
            Data(
                remarks_list='Remarks StoreMetadataRequest Testing Individual',
                raw_data="BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031",
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=r'output',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest
            ),
            Data(
                remarks_list='Remarks Testing Individual',
                raw_data="BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031",
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=r'output',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest
            ),
            Data(
                raw_data="BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031",
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=r'output',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest
            ),
            Data(
                remarks_list='Error ruamel.yaml.representer.RepresenterError: cannot represent an object: <ProfileInfoListResponse (CHOICE)>',
                raw_data='bf2a0499020520',
                asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=KeyWords.OUTPUT_FILE_NAME_KEYWORD
            ),
            Data(
                remarks_list='Remarks StoreMetadataRequest Testing Group',
                raw_data=[
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640'
                ],
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=r'output',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest
            ),
            Data(
                remarks_list='Remarks Testing Group',
                raw_data=[
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640'
                ],
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                output_file_name_keyword=r'output',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest
            ),
            Data(
                raw_data=[
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
                remarks_list='This is a long remakrs for the testing of Trimming of remarks of individual item of the pool in asn play.',
                raw_data='test',
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
            ),
            #
            Data(
                remarks_list='This is a long remakrssssssssssssssss for the testing of Trimming of remarks of individual item of the pool in asn play.',
                raw_data='test',
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
            ),
            #
            Data(
                remarks_list='This is a long remakrssssssssssssssssssssssssssssssssssss for the testing of Trimming of remarks of individual item of the pool in asn play.',
                raw_data='test',
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
            ),
            #
            Data(
                raw_data='This is a long dataaaa for the testing of Trimming of remarks of individual item of the pool in asn play.',
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
            ),
            #
            Data(
                raw_data='This is a long dataaaaaaaaaaaaaaaaaaa for the testing of Trimming of remarks of individual item of the pool in asn play.',
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
            ),
            #
            Data(
                raw_data='This is a long dataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa for the testing of Trimming of remarks of individual item of the pool in asn play.',
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
            ),
            #
            Data(
                remarks_list='This is a long remakrss for the testing of Trimming of remarks of individual item of the pool in asn play.',
                raw_data=['test'] * 100,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
            ),
            #
            Data(
                raw_data=[
                             'This is a long dataaaaa for the testing of Trimming of remarks of individual item of the pool in asn play.'
                         ] * 100,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                print_input=False,
                print_output=False,
            ),
            #
            Data(
                raw_data=[
                             'This is a long dataaaaaaa for the testing of Trimming of remarks of individual item of the pool in asn play.'
                         ] * 10,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                print_input=False,
                print_output=False,
            ),
            #
            Data(
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest\StoreMetadataRequest_wo_icon.hex',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
            ),
            #
            Data(
                raw_data=r'D:\Other\Github_Self\asn1Play\Data\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest\StoreMetadataRequest_wo_icon_wo_serviceSpecific.asn1',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
            ),
        ]

        data_pool_remarks_extend = [
            Data(
                remarks_list=['Extend Remarks List Sample', 'Extend Remarks List'],
                raw_data=[
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
                ],
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1,
                output_file=r'..\..\Data\UserData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\StoreMetadataRequest_wo_icon.base64',
            ),
            Data(
                remarks_list=['Extend Remarks List Sample', 'Extend Remarks List'],
                raw_data=[
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
                ],
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1,
                output_file=r'..\..\Data\UserData\GSMA\SGP_22\$VERSION\StoreMetadataRequest',
            ),
        ]

        data_pool_output_file = [
            #
            Data(
                raw_data=['Test1', 'Test2', 'Test3'],
                asn1_element=None,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                output_file=r'..\..\Data\UserData\Temp\Pj.txt',
            ),
            #
            Data(
                remarks_list=['T1', 'T2', 'T3'],
                raw_data=['Test1', 'Test2', 'Test3'],
                asn1_element=None,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                output_file=r'..\..\Data\UserData\Temp\Pj.txt',
            ),
            #
            Data(
                remarks_list=['T1', 'T2', 'T3'],
                raw_data=['Test1', 'Test2', 'Test3'],
                asn1_element=None,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                output_file=r'..\..\Data\UserData\Temp\Pj$ITEM_INDEX.txt',
            ),
            #
            Data(
                remarks_list=['T1', 'T2'],
                raw_data=['Test1', 'Test2', 'Test3'],
                asn1_element=None,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                output_file=r'..\..\Data\UserData\Temp\Pj.txt',
            ),
            #
            Data(
                remarks_list=['test 1'],
                raw_data='bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                print_input=False,
                print_output=False,
                output_file=r'..\..\Data\UserData\Bulk_export\.txt'
            ),
            #
            Data(
                raw_data=['Test4', 'Test5', 'Test6'],
                asn1_element=None,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                output_file=r'..\..\Data\UserData\Temp\\',
            ),
            #
            Data(
                raw_data=['Test4', 'Test5', 'Test6'],
                asn1_element=None,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                output_file=r'..\..\Data\UserData\Temp/',
            ),
            #
            Data(
                raw_data=['Test7', 'Test8', 'Test9'],
                asn1_element=None,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
                output_file=r'..\..\Data\UserData\Temp',
            ),
            #
            Data(
                remarks_list=['test 1', 'test 2', 'test 3'],
                raw_data=[
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
                ],
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                print_input=False,
                print_output=False,
                output_file=r'..\..\Data\UserData\Bulk_export\.txt'
            ),
            #
            Data(
                remarks_list=['test 1', 'test 2', 'test 3'],
                raw_data=[
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
                ],
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                print_input=False,
                print_output=False,
                output_file=r'..\..\Data\UserData\Bulk_export'
            ),
        ]

        data_pool_asn1_element = [
            #
            Data(
                remarks_list='SGP_22.RSPDefinitions.StoreMetadataRequest',
                raw_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
            ),
            #
            Data(
                remarks_list="StoreMetadataRequest",
                raw_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                asn1_element='StoreMetadataRequest',
            ),
            #
            Data(
                remarks_list="asn1_element='SGP_22.RSPDefinitions.StoreMetadataRequest'",
                raw_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                asn1_element='SGP_22.RSPDefinitions.StoreMetadataRequest',
            ),
            #
            Data(
                remarks_list='InvalidAsnElement WhiteSpace',
                raw_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                asn1_element=' ',
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks_list='Conversion Needed, AsnElement is whiteSpace',
                raw_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                asn1_element=' ',
                input_format=Formats.ASCII,
                output_format=Formats.HEX
            ),
            #
            Data(
                remarks_list='InvalidAsnElement',
                raw_data=r'..\..\Data\UserData\GSMA\SGP_22\$VERSION\InvalidRequest\StoreMetadataReques.yml'
            ),
            #
            Data(
                remarks_list='Invalid asn1_element (unknown str)',
                raw_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                asn1_element='s1',
            ),
            #
            Data(
                remarks_list='Invalid asn1_element (unknown str)',
                raw_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                asn1_element='StoreMetadataReques',
            ),
            #
            Data(
                remarks_list='Invalid asn1_element (class name as str)',
                raw_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                asn1_element='SGP_22.RSPDefinitions.StoreMetadataRequest',
            ),
            #
            Data(
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest\StoreMetadataRequest_wo_icon.hex',
            ),
            #
            Data(
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest\StoreMetadataRequest_wo_icon_wo_serviceSpecific.asn1',
            ),
            #
        ]

        data_pool_tlv = [
            #
            Data(
                remarks_list='DER; tlv_parsing_of_output=True',
                raw_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                input_format=Formats.DER,
                output_format=Formats.DER,
                tlv_parsing_of_output=True
            ),
            #
            Data(
                remarks_list='DER_64; tlv_parsing_of_output=True',
                raw_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                input_format=Formats.DER,
                output_format=Formats.DER_64,
                tlv_parsing_of_output=True
            ),
            #
            Data(
                remarks_list='Ascii; tlv_parsing_of_output=True',
                raw_data='57656c636f6d6520546f2041736e506c617920212121',
                input_format=Formats.HEX,
                output_format=Formats.ASCII,
                tlv_parsing_of_output=True
            ),
            #
        ]

        data_pool_output_file_keyword = [
            #
            Data(
                remarks_list=['test 1', 'test 2', 'test 3'],
                raw_data=[
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
                raw_data=r'D:\Other\Github_Self\asn1Play\Data\SampleData\GSMA\SGP_22\$VERSION\UpdateMetadataRequest',
                asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest,
                output_file_name_keyword='output'
            )
        ]

        data_pool_web_requests = [
            #
            {
                'remarks_list': 'Web Request; asn1_element;',
                'raw_data': 'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                'input_format': Formats.DER,
                'output_format': Formats.ASN1,
                'asn1_element': SGP_22.RSPDefinitions.StoreMetadataRequest
            },
            {
                'remarks_list': 'Web Request; asn1_object;',
                'raw_data': 'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                'input_format': Formats.DER,
                'output_format': Formats.ASN1,
                'asn1_schema': 'GSMA_SGP_22_v3_0_0',
                'asn1_object': 'StoreMetadataRequest',
            },
            {
                'remarks_list': 'Web Request; asn1_object_alternate;',
                'raw_data': 'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                'input_format': Formats.DER,
                'output_format': Formats.ASN1,
                'asn1_schema': 'GSMA_SGP_22_v3_0_0',
                'asn1_object_alternate': 'StoreMetadataRequest'
            },
            {
                'remarks_list': 'Web Request; asn1_object; asn1_object_alternate;',
                'raw_data': 'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                'input_format': Formats.DER,
                'output_format': Formats.ASN1,
                'asn1_schema': 'GSMA_SGP_22_v3_0_0',
                'asn1_object': 'StoreMetadataRequest',
                'asn1_object_alternate': 'StoreMetadataRequest'
            },
            {
                PhKeys.REMARKS_LIST: 'Web Request; fetch_asn1_objects; True',
                PhKeys.ASN1_SCHEMA: Asn1Versions.GSMA_SGP_22_v3_1.get_name(),
                PhKeys.FETCH_ASN1_OBJECTS_LIST: True,
            },
            {
                PhKeys.REMARKS_LIST: 'Web Request; fetch_asn1_objects; False',
                PhKeys.ASN1_SCHEMA: Asn1Versions.GSMA_SGP_22_v3_1.get_name(),
                PhKeys.FETCH_ASN1_OBJECTS_LIST: False,
            },
            {
                PhKeys.REMARKS_LIST: 'Web Request; fetch_asn1_objects; True (str)',
                PhKeys.ASN1_SCHEMA: Asn1Versions.GSMA_SGP_22_v3_1.get_name(),
                PhKeys.FETCH_ASN1_OBJECTS_LIST: 'True',
            },
            {
                PhKeys.REMARKS_LIST: 'Web Request; fetch_asn1_objects; False (str)',
                PhKeys.ASN1_SCHEMA: Asn1Versions.GSMA_SGP_22_v3_1.get_name(),
                PhKeys.FETCH_ASN1_OBJECTS_LIST: 'False',
            },
            {
                PhKeys.REMARKS_LIST: 'Web Request; fetch_asn1_objects; sgp32; True',
                PhKeys.ASN1_SCHEMA: Asn1Versions.GSMA_SGP_32_v1_0.get_name(),
                PhKeys.FETCH_ASN1_OBJECTS_LIST: True,
            },
        ]

        data_pool_asn_element_with_schema = [
            #####
            # DER to ASN1
            #####
            #
            Data(
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\StoreMetadataRequest.hex',
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v3_0_0, 'StoreMetadataRequest'),
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\StoreMetadataRequest.hex',
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v2_4, 'StoreMetadataRequest'),
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\StoreMetadataRequest.hex',
                asn1_element='StoreMetadataRequest',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\StoreMetadataRequest.hex',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #####
            # ASN1 to DER
            #####
            #
            Data(
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\StoreMetadataRequest_Mandatory.asn1',
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v3_0_0, 'StoreMetadataRequest'),
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            #
            Data(
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\StoreMetadataRequest_Mandatory.asn1',
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v2_4, 'StoreMetadataRequest'),
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            #
            Data(
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\StoreMetadataRequest_Mandatory.asn1',
                asn1_element='StoreMetadataRequest',
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            #
            Data(
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\StoreMetadataRequest_Mandatory.asn1',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            #####
            # ASN1 to DER; eUICC_Profile_Package
            #####
            #
            Data(
                raw_data=r'..\..\Data\SampleData\TCA\eUICC_Profile_Package\$VERSION\PE_End.asn1',
                asn1_element=Asn1(Asn1Versions.TCA_EPP_v3_1, 'PE_End'),
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            #
            Data(
                raw_data=r'..\..\Data\SampleData\TCA\eUICC_Profile_Package\$VERSION\PE_End.asn1',
                asn1_element=Asn1(Asn1Versions.TCA_EPP_v3_2, 'PE_End'),
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            # negative scenario
            Data(
                raw_data=r'..\..\Data\SampleData\TCA\eUICC_Profile_Package\$VERSION\PE_End.asn1',
                asn1_element='PE_End',
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            #
            Data(
                raw_data=r'..\..\Data\SampleData\TCA\eUICC_Profile_Package\$VERSION\PE_End.asn1',
                asn1_element=eUICC_Profile_Package.PEDefinitions.PE_End,
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            #####
            # Mix Flow
            #####
            #
            Data(
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\StoreMetadataRequest.hex',
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v3_0_0, 'StoreMetadataRequest'),
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\StoreMetadataRequest.hex',
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v2_4, 'StoreMetadataRequest'),
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\StoreMetadataRequest.hex',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            # Can be deleted
            Data(
                raw_data=r'..\..\Data\SampleData\TCA\eUICC_Profile_Package\$VERSION\PE_End.asn1',
                asn1_element=eUICC_Profile_Package.PEDefinitions.PE_End,
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
        ]

        data_pool_negative = [
            #
            Data(
                remarks_list='raw_data is empty',
                raw_data='',
                asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks_list='raw_data is None',
                raw_data=None,
                asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks_list='InvalidInputFormat',
                raw_data=r'..\..\Data\UserData\GSMA\SGP_22\$VERSION\InvalidRequest\StoreMetadataRequest_inp_derr.yml'
            ),
            #
            Data(
                remarks_list='InvalidInputFormat',
                raw_data=r'..\..\Data\UserData\GSMA\SGP_22\$VERSION\InvalidRequest\StoreMetadataRequest_inp_derr_formats.yml'
            ),
            #
            Data(
                remarks_list='InvalidOutputFormat',
                raw_data=r'..\..\Data\UserData\GSMA\SGP_22\$VERSION\InvalidRequest\StoreMetadataRequest_op_asn2.yml'
            ),
            #
            Data(
                remarks_list='InvalidOutputFormat',
                raw_data=r'..\..\Data\UserData\GSMA\SGP_22\$VERSION\InvalidRequest\StoreMetadataRequest_op_asn2_formats.yml'
            ),
            #
            Data(
                remarks_list='Invalid File Path',
                raw_data=r'D:\Other\Github_Self\asn1Play\SampleData\GSMA\SGP_22\UpdateMetadataRequest\t',
                asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest,
                output_file_name_keyword='output'
            ),
            #
            Data(
                remarks_list='Invalid raw_data (base 64 conversion failure)',
                raw_data='testt',
                input_format=Formats.DER,
                output_format=Formats.DER,
            ),
            #
            Data(
                remarks_list='Invalid raw_data (base 64 conversion failure)',
                raw_data='testt',
                input_format=Formats.DER,
                output_format=Formats.DER_64,
            ),
            #
            Data(
                remarks_list='Invalid raw_data (base 64 conversion failure)',
                raw_data='D:\e\AC\DeleteProfileRequest.he',
            ),
            #
            Data(
                remarks_list='Invalid raw_data (base 64 conversion failure)',
                raw_data='D:\e\AC\DeleteProfileRequest.he',
                input_format=Formats.DER,
                output_format=Formats.DER_64
            ),
            #
            Data(
                remarks_list='Invalid raw_data (base 64 conversion failure)',
                raw_data='D:\e\AC\DeleteProfileRequest.he',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                asn1_element='StoreMetadataRequest',
            ),
            #
            Data(
                remarks_list='Invalid raw_data (base 64 conversion failure)',
                raw_data='D:\e\AC\DeleteProfileRequest.he',
                input_format=Formats.ASN1,
                output_format=Formats.DER,
                asn1_element='StoreMetadataRequest',
            ),
            #
            Data(
                remarks_list='Invalid raw_data (Brackets MisMatch)',
                raw_data="""{
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
                remarks_list='# FileExistsError Error',
                raw_data=[
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                ],
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1,
                output_file=r'..\\..\\Data\\UserData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\Extend_Remarks_List_Item_3.asn1\\'
            ),
            #
            Data(
                remarks_list='Requested conversion is not possible...',
                raw_data='8929901012345678905F',
                input_format=Formats.HEX,
                output_format=Formats.TXT
            ),
            #
            Data(
                remarks_list='Unknown Data (bytes buffer not long enough)',
                raw_data=r'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031990206',
                asn1_element='StoreMetadataRequest',
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
        ]

        super().set_data_pool(
            data_pool_positive +
            data_pool_byte_array +
            data_pool_remarks +
            data_pool_remarks_extend +
            data_pool_output_file +
            data_pool_output_file_keyword +
            data_pool_asn1_element +
            data_pool_tlv +
            data_pool_asn_element_with_schema +
            data_pool_web_requests +
            data_pool_negative
        )
