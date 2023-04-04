from src.main.helper.convert_data import ConvertData
from src.main.helper.data import Data


class Dev(ConvertData):

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
        data_pool_experiment = [
            Data(
            ),
        ]
        super().set_data_pool(data_pool_experiment)
