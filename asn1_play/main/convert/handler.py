import base64
import re

from binascii import unhexlify
from python_helpers.ph_exception_helper import PhExceptionHelper
from python_helpers.ph_util import PhUtil

from asn1_play.main.helper.defaults import Defaults
from asn1_play.main.helper.formats import Formats
from asn1_play.main.helper.formats_group import FormatsGroup
from asn1_play.main.mapping.asn1_elements import all_mapping
from asn1_play.main.mapping.general import parsing_format_mapping

TAB = '    '
M = None
_debug = False

"""
Enable Flags for Debugging
"""


# _debug = True


def convert_data(raw_data, output_format):
    # Data is converted to Hex
    if output_format in FormatsGroup.INPUT_FORMATS_DER_BASE_64:
        return base64.b64encode(unhexlify(raw_data)).decode()
    if output_format in FormatsGroup.ASCII_FORMATS:
        return PhUtil.hex_str_to_ascii(raw_data)
    if output_format in FormatsGroup.INPUT_FORMATS_DER:
        return raw_data
    if output_format in Formats.BYTE_ARRAY:
        return PhUtil.hex_str_to_dec_list(raw_data)
    if output_format in Formats.BYTE_ARRAY_SIGNED:
        return PhUtil.hex_str_to_dec_list(raw_data, signed_byte_handling=True)
    return None


def decode_encode_asn(raw_data='', parse_only=True, input_format=Defaults.FORMAT_INPUT,
                      output_format=Defaults.FORMAT_OUTPUT, asn1_element=None):
    """
    Ref: https://github.com/P1sec/pycrate/wiki/Using-the-pycrate-asn1-runtime
    :param raw_data:
    :param parse_only:
    :param input_format:
    :param output_format:
    :param asn1_element:
    :return:
    """
    func_name = decode_encode_asn.__name__
    exception = None
    print_debug_var('raw_data', raw_data)
    print_debug_var('parse_only', parse_only)
    print_debug_var('input_format', input_format)
    print_debug_var('output_format', output_format)
    print_debug_var('asn1_element', asn1_element)
    offset = 0
    if not raw_data:
        raise ValueError(PhExceptionHelper(msg=f'Mandatory raw data is missing.', function_name=func_name))
    if input_format not in FormatsGroup.INPUT_FORMATS:
        raise ValueError(PhExceptionHelper(msg=f'Unknown input format {input_format}', function_name=func_name))
    if output_format not in FormatsGroup.ALL_FORMATS:
        raise ValueError(PhExceptionHelper(msg=f'Unknown output format {output_format}', function_name=func_name))
    if isinstance(asn1_element, str):
        asn1_element_str = asn1_element  # Str is provided, check the mapping
        asn1_element = asn1_element.strip()
        if asn1_element:
            asn1_element = all_mapping.get(asn1_element, None)
            print_debug('asn1_element mapping conversion is needed ' + (
                'but not available' if asn1_element is None else 'and done'))
            if asn1_element is None:
                raise ValueError(
                    PhExceptionHelper(msg=f'Unknown asn1_element {asn1_element_str}', function_name=func_name))
    if isinstance(raw_data, bytes):
        raw_data = raw_data.hex()
    if input_format in FormatsGroup.INPUT_FORMATS_ASCII:
        raw_data = PhUtil.ascii_to_hex_str(raw_data)
        print_debug('base_profile hex conversion done, data is {0}'.format(raw_data))
    if input_format in FormatsGroup.INPUT_FORMATS_HEX:
        if input_format in FormatsGroup.INPUT_FORMATS_BYTE_ARRAY:
            raw_data = PhUtil.dec_to_hex(raw_data)
        # Trim Hex Data
        raw_data = PhUtil.trim_and_kill_all_white_spaces(raw_data)
        print_debug('base_profile Trimming done, data is {0}'.format(raw_data))
        if not PhUtil.is_hex(raw_data):
            raw_data = base64.b64decode(raw_data).hex()
            print_debug('base_profile hex conversion done, data is {0}'.format(raw_data))
    if not asn1_element:
        print_debug('asn1_element is not provided; Only Conversion can be performed')
        if input_format in FormatsGroup.INPUT_FORMATS_NON_TXT and output_format in FormatsGroup.INPUT_FORMATS_NON_TXT:
            output_data = convert_data(raw_data, output_format)
            if output_data:
                return output_data
            raise ValueError(f'Please check your inputs. Requested conversion is not possible for {raw_data}.')
        raise ValueError('asn1_element is either empty or not provided')

    parsing_data_current = ''
    parsing_data_concatenated = ''
    new_profile = ''
    global M
    M = asn1_element

    # print(help(M))
    record_count = 0
    print_debug('Elements Processing')
    while offset < len(raw_data):
        initial_offset = offset
        # TODO: SML-330
        known_data = True
        record_count += 1
        print_debug_var('offset', offset)
        print_debug_var('len', len)
        temp = ''
        if input_format in FormatsGroup.INPUT_FORMATS_HEX:
            temp = bytes.fromhex(raw_data[offset:])
            try:  # Needed For Unknown data / TLV
                M.from_der(temp)
                temp = M.to_der()
            except Exception as e:
                known_data = False
                exception = e
            offset += (len(temp) * 2)
        if input_format in FormatsGroup.INPUT_FORMATS_ASN:
            temp = raw_data[offset:]
            next_offset = find_offset_of_section(temp, '{', '}') + 1
            print_debug_var('next_offset', next_offset)
            # There could be n white spaces (\n, \r , or both)
            next_offset = find_offset_of_next_non_white_space_char(temp, next_offset)
            print_debug_var('next_offset', next_offset)
            try:  # Needed For Unknown data / TLV
                M.from_asn1(temp)
                temp = M.to_asn1()
            except Exception as e:
                known_data = False
                exception = e
            offset += next_offset
        print_debug_var('temp', temp)
        print_debug_var('record_count', record_count)
        print_debug_var('offset', offset)
        if parse_only:
            if known_data:
                try:
                    parsing_data_current = parse_data(output_format, record_count)
                except:
                    parsing_data_current = M.to_asn1()
                    parsing_data_current = M.from_asn1()
            else:
                if input_format in FormatsGroup.TXT_FORMATS:
                    parsing_data_current = str(temp)
                else:
                    parsing_data_current = temp.hex()
                # TODO: SML-329, SML-330
                raise ValueError(
                    PhExceptionHelper(msg=f'Unknown raw data {parsing_data_current}', function_name=func_name,
                                      exception=exception))
            print_debug('parsing_data_current', parsing_data_current)
            if parsing_data_current:
                # Test cases of asn paring are failing due to 'os.linesep', need to replace same in stored data
                # parsing_data_concatenated = parsing_data_concatenated + os.linesep + parsing_data_current
                sep = '\n' if (output_format in FormatsGroup.TXT_FORMATS or not known_data) else ''
                parsing_data_concatenated = sep.join(
                    filter(None, [parsing_data_concatenated,
                                  # TODO: SML-329, SML-330
                                  str(exception) if exception else None,
                                  parsing_data_current]))
            if known_data:
                process_pe(M())

        if not known_data:
            continue

    if parse_only and output_format in FormatsGroup.BASE64_FORMATS:
        parsing_data_concatenated = base64.b64encode(unhexlify(parsing_data_concatenated)).decode()
    if parse_only:
        return parsing_data_concatenated
    return new_profile


def process_pe(profile_element, level=1, data_to_update=''):
    """

    :param profile_element:
    :param level:
    :param data_to_update:
    :return:
    """
    space = level * TAB
    if isinstance(profile_element, tuple):
        level = level + 1
        if all(isinstance(v, int) for v in profile_element):
            print_debug(space + 'tuple with all Int')
            return
        print_debug(space + 'tuple')
        for elements in profile_element:
            # TODO: Temp Experiments
            #            profile_element_der = pe.from_asn1(profile_element)
            print_debug_var(space + 'pe: ' + str(elements))
            process_pe(elements, level, data_to_update)

    elif isinstance(profile_element, dict):
        level = level + 1
        print_debug(space + 'dict')
        for elements in profile_element:
            print_debug_var(space + 'pe element: {0} -> {1}'.format(elements, profile_element[elements]))
            if data_to_update:  # Data Provided
                if elements in data_to_update.keys():
                    print_debug('Target Element {} Found'.format(elements))
            process_pe(profile_element[elements], level, data_to_update)
    elif isinstance(profile_element, list):
        level = level + 1
        print_debug(space + 'list')
        for elements in profile_element:
            print_debug_var(space + 'pe: ' + str(elements))
            process_pe(elements, level, data_to_update)
    elif isinstance(profile_element, str):
        print_debug(space + 'str')
    elif isinstance(profile_element, int):
        print_debug(space + 'int')
    elif isinstance(profile_element, bytes):
        print_debug(space + 'bytes')
    else:
        print_debug(space + 'unknown' + str(type(profile_element)))


def parse_data(parsing_format, record_count):
    print_debug('parsing_format_mapping', parsing_format_mapping)
    parsing_data_current = getattr(M, parsing_format_mapping.get(parsing_format))()
    print_debug('parsing_data_current', parsing_data_current)
    if parsing_format == 'get_proto' and record_count > 1:
        # Whole data parsing is returned in first iteration
        return None
    if _debug:
        print('profile_element_record_count:', record_count)
    if isinstance(parsing_data_current, bytes):
        parsing_data_current = parsing_data_current.hex()
    # Few Function returns tuple, list, dict
    if _debug:
        PhUtil.print_iter(parsing_data_current)
    return str(parsing_data_current)


def find_offset_of_section(data, char_to_find, corresponding_char_to_find):
    """
    Considering Ideal Scenario: Any target char is not present as a comment
    Data Pattern is correct,target characters are available in pairs

    :param data:
    :param char_to_find:
    :param corresponding_char_to_find:
    :return:
    """
    slack = []
    start_char_list = [m.start() for m in re.finditer(char_to_find, data)]
    end_char_list = [m.start() for m in re.finditer(corresponding_char_to_find, data)]
    start_char_list_len = len(start_char_list)
    end_char_list_len = len(end_char_list)
    # print('start_char_list', start_char_list)
    # print('end_char_list', end_char_list)
    # print('start_char_list_len', start_char_list_len)
    # print('end_char_list_len', end_char_list_len)
    index_start_char = 0
    index_end_char = 0
    count = 0
    end_char = len(data)  # assignment is needed for the wrong case when target chars are not present
    while count < start_char_list_len + end_char_list_len:
        count += 1
        start_char = int(start_char_list[index_start_char]) if index_start_char < start_char_list_len else -1
        end_char = int(end_char_list[index_end_char]) if index_end_char < end_char_list_len else -1
        if start_char < end_char and start_char != -1:
            # print('pushed', start_char)
            index_start_char += 1
            slack.append(start_char)
        else:
            # print('poped', end_char)
            index_end_char += 1
            if len(slack) == 0:
                raise ValueError(
                    f'Corresponding character "{corresponding_char_to_find}" (Total Count {start_char_list_len}) for "{char_to_find}" (Total Count {end_char_list_len}) is not found.\nWhere data is:\n{data}')
            slack.pop()
        if len(slack) == 0:
            # print(corresponding_char_to_find, end_char)
            break;
    return end_char


def find_offset_of_next_non_white_space_char(temp, current_offset):
    new_offset = current_offset
    for a in temp[current_offset:]:
        if not a.isspace():
            break
        new_offset += 1
    return new_offset


def print_debug(param, sep=' ', end='\n'):
    if _debug:
        print(param, sep, end)


def print_debug_var(param_name, param_value=''):
    print_debug('{0},type: {1}, length: {2}, value: {3}'.format(param_name, type(param_value), len(str(param_value)),
                                                                str(param_value)))
