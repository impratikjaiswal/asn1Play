from src.main.helper.convert_data import ConvertData
from src.main.helper.data import Data
from src.main.helper.formats import Formats


class UserData(ConvertData):

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

    def set_asn_element(self):
        pass

    def set_data_pool(self):
        data_pool = [
            # Hex to ASCII
            # Data(
            #     raw_data='48444643',
            #     asn1_element=None,
            #     input_format=Formats.HEX,
            #     output_format=Formats.ASCII
            # ),
            # ASCII to Hex
            Data(
                raw_data='SBI',
                asn1_element=None,
                input_format=Formats.ASCII,
                output_format=Formats.HEX
            ),
        ]
        super().set_data_pool(data_pool)
