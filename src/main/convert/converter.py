import os

from util_helpers import util

from src.main.convert.handler import decode_encode_asn
from src.main.helper.defaults import Defaults
from src.main.helper.formats import Formats
from src.main.helper.formatsGroup import FormatsGroup


def print_data(base_data, input_format, output_format, print_input, print_info, re_parse_output,
               asn1_element, parsed_data, re_parsed_data, mode_key, mode_value):
    one_line_sep = ': '
    multi_line_sep = ':\n'
    multi_obj_sep = '; '
    input_sep = multi_line_sep if input_format in FormatsGroup.TXT_FORMATS else one_line_sep
    output_sep = multi_line_sep if output_format in FormatsGroup.TXT_FORMATS else one_line_sep
    if print_info:
        print(multi_obj_sep.join(filter(None, [
            f'Asn1 Element is{one_line_sep}{asn1_element.fullname()}' if asn1_element else 'Conversion Mode',
            f'Input Format is{one_line_sep}{input_format}',
            f'Output Format is{one_line_sep}{output_format}',
            f'Input {mode_key} is{one_line_sep}{mode_value}' if mode_key else None,
        ])))
    if print_input:
        print(f'Input Data is{input_sep}{base_data}')
    if parsed_data:
        print(f'OutPut Data is{output_sep}{parsed_data}')
    if re_parse_output:
        print(f'Re-parsed Data is{input_sep}{re_parsed_data}')
    util.print_separator()


def files_ext_as_per_input_format(input_format):
    if input_format in FormatsGroup.INPUT_FORMATS_DER:
        include_files = FormatsGroup.INPUT_FILE_FORMATS_HEX
    elif input_format in FormatsGroup.INPUT_FORMATS_DER_BASE_64:
        include_files = FormatsGroup.INPUT_FILE_FORMATS_BASE_64
    elif input_format in FormatsGroup.INPUT_FORMATS_ASN:
        include_files = FormatsGroup.INPUT_FILE_FORMATS_ASN
    else:  # input_format is None or unknown
        include_files = FormatsGroup.INPUT_FILE_FORMATS
    include_files = [('*' + x) for x in include_files]
    return include_files


def input_output_format_as_per_files_ext(base_data, input_format, output_format):
    file_ext = os.path.splitext(base_data)[1]
    if file_ext in FormatsGroup.INPUT_FILE_FORMATS_HEX:
        input_format = Formats.DER
        output_format_temp = Formats.ASN1
    if file_ext in FormatsGroup.INPUT_FILE_FORMATS_BASE_64:
        input_format = Formats.DER_64
        output_format_temp = Formats.ASN1
    if file_ext in FormatsGroup.INPUT_FILE_FORMATS_ASN:
        input_format = Formats.ASN1
        output_format_temp = Formats.DER
    if output_format == input_format:
        output_format = output_format_temp
    return input_format, output_format


def parse_or_update_any_data(base_data, input_format=Defaults.FORMAT_INPUT, output_format=Defaults.FORMAT_OUTPUT,
                             print_input=None, print_info=None, re_parse_output=None, asn1_element=None):
    mode_key = None
    base_data_org = base_data
    if isinstance(base_data, list):
        mode_key = f'List ({len(base_data)} Elements)'
        print_data(base_data=base_data, input_format=input_format, output_format=output_format, print_input=print_input,
                   print_info=print_info, re_parse_output=re_parse_output, asn1_element=asn1_element, parsed_data=None,
                   re_parsed_data=None, mode_key=mode_key, mode_value=base_data_org)
        parsed_data_list = []
        for data in base_data:
            parsed_data_list.append(
                parse_or_update_any_data(base_data=data, input_format=input_format, output_format=output_format,
                                         print_input=print_input, print_info=print_info,
                                         re_parse_output=re_parse_output,
                                         asn1_element=asn1_element))
        return parsed_data_list
    temp_path = os.path.abspath(base_data)
    if os.path.isdir(os.path.abspath(base_data)):
        # dir is provided
        mode_key = 'Dir'
        print_data(base_data=base_data, input_format=input_format, output_format=output_format, print_input=print_input,
                   print_info=print_info, re_parse_output=re_parse_output, asn1_element=asn1_element, parsed_data=None,
                   re_parsed_data=None, mode_key=mode_key, mode_value=base_data_org)
        files_list = util.traverse_it(top=temp_path, traverse_mode='Regex',
                                      include_files=files_ext_as_per_input_format(input_format))
        if files_list:
            return parse_or_update_any_data(base_data=files_list, input_format=input_format,
                                            output_format=output_format,
                                            print_input=print_input, print_info=print_info,
                                            re_parse_output=re_parse_output,
                                            asn1_element=asn1_element)
    if os.path.isfile(base_data):
        # file is provided
        mode_key = 'File'
        try:
            with open(base_data, 'r') as the_file:
                resp = ''.join(the_file.readlines())
        except UnicodeDecodeError:
            # Binary File
            with open(base_data, 'rb') as the_file:
                resp = the_file.read()
        input_format, output_format = input_output_format_as_per_files_ext(base_data, input_format, output_format)
        base_data = resp

    # Set Default Values if nothing is set
    if print_input is None: print_input = False
    if re_parse_output is None: re_parse_output = False
    re_parsed_data = None
    # parse Data
    parsed_data = decode_encode_asn(input_data=base_data, parse_only=True,
                                    input_format=input_format, output_format=output_format,
                                    asn1_element=asn1_element)
    if re_parse_output:
        re_parsed_data = decode_encode_asn(input_data=parsed_data, parse_only=True,
                                           input_format=output_format, output_format=input_format,
                                           asn1_element=asn1_element)
    print_data(base_data=base_data, input_format=input_format, output_format=output_format, print_input=print_input,
               print_info=print_info, re_parse_output=re_parse_output, asn1_element=asn1_element,
               parsed_data=parsed_data, re_parsed_data=re_parsed_data, mode_key=mode_key, mode_value=base_data_org)
    return parsed_data
