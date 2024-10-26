from asn1_play.generated_code.asn1.GSMA import SGP_22
from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.helper.data import Data
from asn1_play.main.helper.folders import Folders
from asn1_play.main.helper.formats import Formats


class StoreMetaDataBulk(DataTypeMaster):

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
        # RemarksVariable;
        output_file = Folders.in_user(r'bulk\StoreMetadataRequest\$REMARKS')
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
        output_format = Formats.ASN1
        super().set_output_format(output_format)

    def set_input_format(self):
        input_format = Formats.DER
        super().set_input_format(input_format)

    def set_asn1_element(self):
        asn1_element = SGP_22.RSPDefinitions.StoreMetadataRequest
        super().set_asn1_element(asn1_element)

    def set_data_pool(self):
        data_pool = [
            #
            Data(
                remarks='Sample Data 1',
                input_data='BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
            ),
            #
            Data(
                remarks='Sample Data 2',
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
            ),
            #
            Data(
                remarks='Sample Data 3',
                input_data='bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
            )
        ]
        super().set_data_pool(data_pool)
