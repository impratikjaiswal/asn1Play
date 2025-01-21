import base64
import re

from python_helpers.ph_constants import PhConstants
from python_helpers.ph_exception_helper import PhExceptionHelper
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from asn1_play.generated_code.asn1.asn1 import Asn1
from asn1_play.main.helper.constants import Constants
from asn1_play.main.helper.formats import Formats
from asn1_play.main.helper.formats_group import FormatsGroup
from asn1_play.main.helper.methods import Methods

M = None
_debug = False


# Enable Flag for Debugging
# _debug = True


def handle_data(data, meta_data, info_data, flip_output=False):
    """

    :param data:
    :param meta_data:
    :param info_data:
    :param flip_output:
    :return:
    """
    input_data = data.input_data
    input_format = data.input_format
    output_format = data.output_format
    if flip_output is True:
        input_data = meta_data.parsed_data
        input_format = data.output_format
        output_format = data.input_format
    parse_only = True
    asn1_element = data.asn1_element
    res = __handle_data(input_data=input_data, parse_only=parse_only, input_format=input_format,
                        output_format=output_format, asn1_element=asn1_element, info_data=info_data)
    if flip_output is True:
        meta_data.re_parsed_data = res
    else:
        meta_data.parsed_data = res


def __handle_data(input_data, parse_only, input_format, output_format, asn1_element, info_data):
    """
    Ref: https://github.com/P1sec/pycrate/wiki/Using-the-pycrate-asn1-runtime
    :param input_data:
    :param parse_only:
    :param input_format:
    :param output_format:
    :param asn1_element:
    :return:
    """
    func_name = __handle_data.__name__
    exception = None
    print_debug_var_v('input_data', input_data)
    print_debug_var_v('parse_only', parse_only)
    print_debug_var_v('input_format', input_format)
    print_debug_var_v('output_format', output_format)
    print_debug_var_v('asn1_element', asn1_element)
    offset = 0
    if asn1_element and isinstance(asn1_element, Asn1):
        if asn1_element.is_fetch_asn1_objects_list():
            return asn1_element.get_asn1_object_list(str_format=True)
    if not input_data:
        raise ValueError(PhExceptionHelper(msg_key=Constants.INPUT_DATA_MISSING, function_name=func_name))
    if input_format not in FormatsGroup.INPUT_FORMATS_SUPPORTED:
        raise ValueError(
            PhExceptionHelper(msg_key=Constants.UNKNOWN_INPUT_FORMAT, msg_value=input_format, function_name=func_name))
    if output_format not in FormatsGroup.OUTPUT_FORMATS_SUPPORTED:
        raise ValueError(
            PhExceptionHelper(msg_key=Constants.UNKNOWN_OUTPUT_FORMAT, msg_value=output_format,
                              function_name=func_name))
    if isinstance(input_data, bytes):
        input_data = input_data.hex()
    if input_format in FormatsGroup.INPUT_FORMATS_ASCII:
        input_data = PhUtil.ascii_to_hex_str(input_data)
        print_debug_var(Constants.INPUT_DATA_HEX_CONVERSION_IS_DONE, input_data)
    if input_format in FormatsGroup.INPUT_FORMATS_HEX:
        if input_format in FormatsGroup.BYTE_ARRAY_FORMATS:
            input_data = PhUtil.dec_to_hex(input_data)
        # Trim Hex Data
        input_data = PhUtil.trim_and_kill_all_white_spaces(input_data)
        print_debug_var(Constants.INPUT_DATA_TRIMMING_IS_DONE, input_data)
        if not PhUtil.is_hex(input_data) and PhUtil.is_base64(input_data):
            input_data = base64.b64decode(input_data).hex()
            print_debug_var(Constants.INPUT_DATA_BASE_64_CONVERSION_IS_DONE, input_data)
    if input_format in FormatsGroup.NON_TXT_FORMATS and output_format in FormatsGroup.NON_TXT_FORMATS:
        print_debug_var(Constants.ASN1_ELEMENT_IS_NOT_NEEDED)
        output_data = convert_data(input_data, output_format, info_data)
        if output_data:
            return output_data
        additional_msgs_list = PhUtil.get_key_value_pair(PhKeys.INPUT_DATA, input_data)
        raise ValueError(
            PhExceptionHelper(msg_key=Constants.INPUT_DATA_CONVERSION_NOT_POSSIBLE, function_name=func_name,
                              additional_msgs_list=additional_msgs_list))
    if not asn1_element or asn1_element is None:
        raise ValueError(PhExceptionHelper(msg_key=Constants.ASN1_SCHEMA_IS_EMPTY_OR_MISSING, function_name=func_name))
    if isinstance(asn1_element, Asn1):
        # Run Time Versions
        asn1_object = asn1_element.get_asn1_object()
        asn1_object_alternate = asn1_element.get_asn1_object_alternate()
        if (not asn1_object or asn1_object is None) and (not asn1_object_alternate or asn1_object_alternate is None):
            raise ValueError(
                PhExceptionHelper(msg_key=Constants.ASN1_OBJECT_IS_EMPTY_OR_MISSING, function_name=func_name))
        mapping_data = asn1_element.get_asn1_mapping()
        asn1_element_fetched = mapping_data.get(asn1_object, None)
        if not asn1_element_fetched:
            asn1_element_fetched = mapping_data.get(asn1_object_alternate, None)
        print_debug_var(Constants.ASN1_ELEMENT_MAPPING_IS_DONE)
        if asn1_element_fetched is None:
            raise ValueError(
                PhExceptionHelper(msg_key=Constants.UNKNOWN_ASN1_OBJECT, msg_value=asn1_object,
                                  function_name=func_name))
        else:
            print_debug_var(Constants.ASN1_ELEMENT_MAPPING_IS_FAIL)
    else:
        # Compile Time Versions
        # raise ValueError(PhExceptionHelper(msg_key=Constants.UNKNOWN_PARENT_OF_ASN1_OBJECT, msg_value=asn1_element,
        #                                    function_name=func_name))
        asn1_element_fetched = asn1_element

    parsing_data_current = PhConstants.STR_EMPTY
    parsing_data_concatenated = PhConstants.STR_EMPTY
    new_profile = PhConstants.STR_EMPTY
    global M
    M = asn1_element_fetched

    # print(help(M))
    record_count = 0
    print_debug_var('Elements Processing')
    while offset < len(input_data):
        initial_offset = offset
        # TODO: SML-330
        known_data = True
        record_count += 1
        print_debug_var_v('offset', offset)
        print_debug_var_v('len', len)
        temp = PhConstants.STR_EMPTY
        if input_format in FormatsGroup.INPUT_FORMATS_HEX:
            temp = bytes.fromhex(input_data[offset:])
            try:  # Needed For Unknown data / TLV
                M.from_der(temp)
                temp = M.to_der()
            except Exception as e:
                known_data = False
                exception = e
            offset += (len(temp) * 2)
        elif input_format in FormatsGroup.INPUT_FORMATS_ASN:
            temp = input_data[offset:]
            next_offset = find_offset_of_next_block(temp)
            try:  # Needed For Unknown data / TLV
                M.from_asn1(temp)
                temp = M.to_asn1()
            except Exception as e:
                known_data = False
                exception = e
            offset += next_offset
        elif input_format in FormatsGroup.INPUT_FORMATS_JSON:
            # TODO: Can be merged with ASN1 Above
            temp = input_data[offset:]
            next_offset = find_offset_of_next_block(temp)
            try:  # Needed For Unknown data / TLV
                M.from_json(temp)
                temp = M.to_json()
            except Exception as e:
                known_data = False
                exception = e
            offset += next_offset
        print_debug_var_v('temp', temp)
        print_debug_var_v('record_count', record_count)
        print_debug_var_v('offset', offset)
        if parse_only:
            if known_data:
                try:
                    parsing_data_current = parse_data(output_format, record_count)
                except:
                    parsing_data_current = M.to_asn1()
                    parsing_data_current = M.from_asn1()
            else:
                # TODO: SML-450
                print_debug_var_v('known_data', known_data)
                print_debug_var_v('temp', temp)
                if input_format in FormatsGroup.TXT_FORMATS:
                    parsing_data_current = str(temp)
                else:
                    parsing_data_current = temp.hex()
                # TODO: SML-329, SML-330, SML-414
                raise ValueError(
                    PhExceptionHelper(msg_key=Constants.UNKNOWN_INPUT_DATA, msg_value=parsing_data_current,
                                      function_name=func_name, exception=exception))
            print_debug_var('parsing_data_current', parsing_data_current)
            if parsing_data_current:
                # Test cases of asn paring are failing due to 'os.linesep', need to replace same in stored data
                # parsing_data_concatenated = parsing_data_concatenated + os.linesep + parsing_data_current
                sep = PhConstants.SEPERATOR_TWO_LINES if (
                        output_format in FormatsGroup.TXT_FORMATS or not known_data) else PhConstants.STR_EMPTY
                parsing_data_concatenated = sep.join(
                    filter(None, [parsing_data_concatenated,
                                  # TODO: SML-329, SML-330
                                  str(exception) if exception else None,
                                  parsing_data_current]))

            if known_data:
                process_pe(M())

        if not known_data:
            continue
    if parse_only and output_format in FormatsGroup.NON_TXT_FORMATS:
        result = convert_data(parsing_data_concatenated, output_format, info_data)
        if result:
            parsing_data_concatenated = result
    if parse_only:
        return parsing_data_concatenated
    return new_profile


def convert_data(input_data, output_format, info_data):
    # Data is converted to Hex
    if output_format in FormatsGroup.BASE64_FORMATS:
        return PhUtil.decode_to_base64_if_hex(input_data)
    if output_format in FormatsGroup.ASCII_FORMATS:
        decoding_format = PhConstants.CHAR_ENCODING_UTF8
        if info_data is not None:
            info_data.set_info(f'Trying with {decoding_format}')
        return PhUtil.hex_str_to_ascii(input_data, only_if_printable=False, encoding=decoding_format)
    if output_format in FormatsGroup.INPUT_FORMATS_DER:
        return input_data
    if output_format in Formats.DER_BYTE_ARRAY:
        return PhUtil.hex_str_to_dec_list(input_data)
    if output_format in Formats.DER_BYTE_ARRAY_SIGNED:
        return PhUtil.hex_str_to_dec_list(input_data, signed_byte_handling=True)
    return None


def process_pe(profile_element, level=1, data_to_update=PhConstants.STR_EMPTY):
    """

    :param profile_element:
    :param level:
    :param data_to_update:
    :return:
    """
    space = level * PhConstants.STR_TAB
    if isinstance(profile_element, tuple):
        level = level + 1
        if all(isinstance(v, int) for v in profile_element):
            print_debug_var(space + 'tuple with all Int')
            return
        print_debug_var(space + 'tuple')
        for elements in profile_element:
            # TODO: Temp Experiments
            #            profile_element_der = pe.from_asn1(profile_element)
            print_debug_var_v(space + 'pe', str(elements))
            process_pe(elements, level, data_to_update)

    elif isinstance(profile_element, dict):
        level = level + 1
        print_debug_var(space + 'dict')
        for elements in profile_element:
            print_debug_var_v(space + 'pe element', f'{elements} -> {profile_element[elements]}')
            if data_to_update:  # Data Provided
                if elements in data_to_update.keys():
                    print_debug_var('Target Element Found', elements)
            process_pe(profile_element[elements], level, data_to_update)
    elif isinstance(profile_element, list):
        level = level + 1
        print_debug_var(space + 'list')
        for elements in profile_element:
            print_debug_var_v(space + 'pe', str(elements))
            process_pe(elements, level, data_to_update)
    elif isinstance(profile_element, str):
        print_debug_var(space + 'str')
    elif isinstance(profile_element, int):
        print_debug_var(space + 'int')
    elif isinstance(profile_element, bytes):
        print_debug_var(space + 'bytes')
    else:
        print_debug_var(space + 'unknown', str(type(profile_element)))


def parse_data(parsing_format, record_count):
    print_debug_var('all_mapping', Methods.ALL_MAPPING)
    mapping = Methods.ALL_MAPPING.get(parsing_format)
    if not mapping:
        raise ValueError(f'Method Mapping not found for {parsing_format}')
    method = mapping[Methods.INDEX_TO] if isinstance(mapping, tuple) else mapping
    parsing_data_current = getattr(M, method)()
    print_debug_var('parsing_data_current', parsing_data_current)
    if parsing_format == Formats.GET_PROTO and record_count > 1:
        # Whole data parsing is returned in first iteration
        return None
    print_debug_var('parsing_data_current', parsing_data_current)
    print_debug_var('profile_element_record_count', record_count)
    if isinstance(parsing_data_current, bytes):
        parsing_data_current = parsing_data_current.hex()
    # Few Function returns tuple, list, dict
    print_debug_var('parsing_data_current', parsing_data_current)
    return str(parsing_data_current)


def find_offset_of_next_block(temp, start_char=PhConstants.STR_CURLY_BRACE_START,
                              end_char=PhConstants.STR_CURLY_BRACE_END):
    next_offset = find_offset_of_block(temp, start_char, end_char) + 1
    print_debug_var_v('next_offset', next_offset)
    # There could be n white spaces (\n, \r , or both)
    next_offset = find_offset_of_next_non_white_space_char(temp, next_offset)
    print_debug_var_v('next_offset', next_offset)
    return next_offset


def find_offset_of_block(data, char_to_find, corresponding_char_to_find):
    """
    Considering Ideal Scenario: Any target char is not present as a comment
    Data Pattern is correct, target characters are available in pairs

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
                additional_data = [
                    f'Corresponding character "{corresponding_char_to_find}" (Total Count {start_char_list_len}) for "{char_to_find}" (Total Count {end_char_list_len}) is not found.',
                    PhUtil.get_key_value_pair('data', data)
                ]
                raise ValueError(PhExceptionHelper(msg_key=Constants.INPUT_DATA_ASN1_FORMATION_ISSUE,
                                                   additional_msgs_list=additional_data,
                                                   function_name='find_offset_of_section'))
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


def print_debug_var(param_name, param_value=None):
    if _debug:
        print(PhConstants.SEPERATOR_KEY_VALUE.join(filter(None, [param_name, str(param_value)])))
    pass


def print_debug_var_v(param_name, param_value=None):
    """
    verbose mode
    :param param_name:
    :param param_value:
    :return:
    """
    if param_value is None:
        print_debug_var(param_name, param_value)
    else:
        print_debug_var(
            f'{param_name}, type: {type(param_value)}, length: {len(str(param_value))}, value: {str(param_value)}')
