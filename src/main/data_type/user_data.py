from src.main.data_type.data_type_master import DataTypeMaster
from src.main.helper.data import Data
from src.main.helper.formats import Formats


class UserData(DataTypeMaster):

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
            # ASCII to Hex
            Data(
                raw_data='Welcome To AsnPlay !!!',
                input_format=Formats.ASCII,
                output_format=Formats.HEX
            ),
            # Hex to ASCII
            Data(
                raw_data='57656c636f6d6520546f2041736e506c617920212121',
                input_format=Formats.HEX,
                output_format=Formats.ASCII
            ),
        ]
        super().set_data_pool(data_pool)
