import os

from converter.converter import decode_encode_asn
from helper.util import print_separator
from helper.formats import Formats
from mapping.general import txt_formats


def parse_or_update_any_data(base_data, input_format=Formats.DEFAULT_INPUT, output_format=Formats.DEFAULT_OUTPUT,
                             print_inp=None, print_info=None, re_parse_op=None, asn1_element=None):
    if isinstance(base_data, list):
        parsed_data_list = []
        for data in base_data:
            parsed_data_list.append(
                parse_or_update_any_data(base_data=data, input_format=input_format, output_format=output_format,
                                         print_inp=print_inp, print_info=print_info, re_parse_op=re_parse_op,
                                         asn1_element=asn1_element))
        return parsed_data_list
    base_data_org = base_data
    if os.path.isfile(base_data):
        # file is provided
        try:
            with open(base_data, 'r') as the_file:
                resp = ''.join(the_file.readlines())
        except UnicodeDecodeError:
            # Binary File
            with open(base_data, 'rb') as the_file:
                resp = the_file.read()
        if os.path.splitext(base_data)[1] == ".asn1":
            input_format = Formats.ASN1
            if output_format in [Formats.ASN1]:
                output_format = Formats.DER
        base_data = resp

    # Set Default Values if nothing is set
    if print_inp is None: print_inp = False
    if re_parse_op is None: re_parse_op = False
    re_parsed_data = None
    # parse Data
    parsed_data = decode_encode_asn(input_data=base_data, parse_only=True,
                                    input_format=input_format, output_format=output_format,
                                    asn1_element=asn1_element)
    if re_parse_op:
        re_parsed_data = decode_encode_asn(input_data=parsed_data, parse_only=True,
                                           input_format=output_format, output_format=input_format,
                                           asn1_element=asn1_element)

    one_line_sep = ': '
    multi_line_sep = ':\n'
    multi_obj_sep = '; '
    input_sep = multi_line_sep if input_format in txt_formats else one_line_sep
    output_sep = multi_line_sep if output_format in txt_formats else one_line_sep
    if print_info:
        print(multi_obj_sep.join(filter(None, [
            f'Asn1 Element is{one_line_sep}{asn1_element.fullname()}',
            f'Input Format is{one_line_sep}{input_format}',
            f'Output Format is{one_line_sep}{output_format}',
            '' if base_data_org == base_data else f'Input File is{one_line_sep}{base_data_org}'
        ])))
    if print_info:
        print(f'Input Data is{input_sep}{base_data}')
    print(f'OutPut Data is{output_sep}{parsed_data}')
    if re_parse_op:
        print(f'Re-parsed Data is{input_sep}{re_parsed_data}')
    print_separator()
    return parsed_data
