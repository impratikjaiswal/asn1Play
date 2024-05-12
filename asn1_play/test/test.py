from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_util import PhUtil

from asn1_play.generated_code.asn1.asn1_versions import Asn1Versions
from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.helper.data import Data
from asn1_play.main.helper.formats import Formats


class Test():

    @classmethod
    def test_data(self):
        raw_data = 'Welcome To AsnPlay !!!'
        input_format = Formats.ASCII
        output_format = Formats.HEX

        data_type = DataTypeMaster()
        data_type.set_data_pool(
            data_pool=[Data(raw_data=raw_data, input_format=input_format, output_format=output_format)])
        data_type.parse_safe(PhErrorHandlingModes.CONTINUE_ON_ERROR)
        print(f'raw_data {raw_data}')
        print(f'input_format {input_format}')
        print(f'output_format {output_format}')
        print(f'output_data {data_type.get_output_data()}')
        PhUtil.print_separator()
        data = Asn1Versions._get_list_of_supported_versions()
        PhUtil.print_iter(data, header='All Supported Versions')
