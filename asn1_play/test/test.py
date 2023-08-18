from python_helpers.ph_modes_error_handling import PhErrorHandlingModes

from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.helper.data import Data

raw_data = 'Welcome To AsnPlay !!!'
input_format = 'ascii'
output_format = 'hex'

data_type = DataTypeMaster()
data_type.set_data_pool(data_pool=[Data(raw_data=raw_data, input_format=input_format, output_format=output_format)])
data_type.parse_safe(PhErrorHandlingModes.CONTINUE_ON_ERROR)
print(f'raw_data {raw_data}')
print(f'input_format {input_format}')
print(f'output_format {output_format}')
print(f'output_data {data_type.meta_data_pool[0]}')