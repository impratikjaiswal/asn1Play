from src.generated_code.asn1.GSMA import SGP_22
from src.main.helper.convert_data import ConvertData
from src.main.helper.data import Data
from src.main.helper.formats import Formats


class UnitTesting(ConvertData):

    def set_print_input(self):
        print_input = None
        super().set_print_input(print_input)

    def set_print_info(self):
        print_info = None
        super().set_print_info(print_info)

    def set_re_parse_output(self):
        re_parse_output = None
        super().set_re_parse_output(re_parse_output)

    def set_asn_element(self):
        pass

    def set_data_pool(self):
        data_pool_positive = [
            #
            Data(
                remarks_list='Der to ASCII via YAML',
                raw_data=r'..\..\SampleData\Generic\ASCII\hex_to_ascii.yaml'
            ),
            #
            Data(
                remarks_list='Der to ASCII via YAML, same file',
                raw_data=r'..\..\SampleData\Generic\ASCII\hex_to_ascii_op_same_file.yaml'
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
            Data(
                remarks_list='This is a long remakrs for the testing of Trimming of remarks of individual item of the pool in asn play.',
                raw_data=['test'] * 100,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
            ),
            Data(
                raw_data=['This is a long dataaaa for the testing of Trimming of remarks of individual item of the pool in asn play.'] * 100,
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
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
        ]
        super().set_data_pool(data_pool_positive + data_pool_remarks + data_pool_negative)
