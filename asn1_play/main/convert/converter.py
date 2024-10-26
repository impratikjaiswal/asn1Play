import copy
import os

from python_helpers.ph_constants import PhConstants
from python_helpers.ph_data_master import PhMasterData, PhMasterDataKeys
from python_helpers.ph_exception_helper import PhExceptionHelper
from python_helpers.ph_file_extensions import PhFileExtensions
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil
from ruamel.yaml.main import YAML
from ruamel.yaml.scalarstring import PreservedScalarString

from asn1_play.generated_code.asn1.GSMA import SGP_22
from asn1_play.generated_code.asn1.GSMA import SGP_32
from asn1_play.generated_code.asn1.GSMA.SGP_22 import version as sgp22_version
from asn1_play.generated_code.asn1.GSMA.SGP_32 import version as sgp32_version
from asn1_play.generated_code.asn1.TCA import eUICC_Profile_Package
from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package import version as epp_version
from asn1_play.generated_code.asn1.asn1 import Asn1
from asn1_play.generated_code.asn1.asn1_versions import Asn1Versions
from asn1_play.main.helper.constants import Constants
from asn1_play.main.helper.data import Data
from asn1_play.main.helper.defaults import Defaults
from asn1_play.main.helper.folders import Folders
from asn1_play.main.helper.formats import Formats
from asn1_play.main.helper.formats_group import FormatsGroup
from asn1_play.main.helper.keywords import KeyWords
from asn1_play.main.helper.mode_operation import OperationModes
from asn1_play.main.helper.util import Util
from asn1_play.main.helper.variables import Variables


def print_data(data=None, meta_data=None, info_data=None, master_data=None):
    if master_data is not None and isinstance(master_data, PhMasterData):
        data = master_data.get_master_data(PhMasterDataKeys.DATA)
        meta_data = master_data.get_master_data(PhMasterDataKeys.META_DATA)
        info_data = master_data.get_master_data(PhMasterDataKeys.INFO_DATA)
    if data.quite_mode:
        return
    input_sep = PhConstants.SEPERATOR_MULTI_LINE if data.input_format in FormatsGroup.TXT_FORMATS else PhConstants.SEPERATOR_ONE_LINE
    output_sep = PhConstants.SEPERATOR_MULTI_LINE if data.output_format in FormatsGroup.TXT_FORMATS or data.tlv_parsing_of_output == True else PhConstants.SEPERATOR_ONE_LINE
    if data.print_info:
        remarks_original = data.get_remarks_as_str(user_original_remarks=True)
        remarks_generated = data.get_remarks_as_str()
        remarks_generated_stripping_needed = True if remarks_generated.endswith(
            PhConstants.DEFAULT_TRIM_STRING) else False
        if remarks_original:
            if remarks_generated_stripping_needed:
                if remarks_generated.strip(PhConstants.DEFAULT_TRIM_STRING) in remarks_original:
                    remarks_generated = ''
            else:
                if remarks_original in remarks_generated:
                    remarks_generated = ''
            meta_data.output_dic.update(
                get_dic_data_and_print(PhKeys.REMARKS, PhConstants.SEPERATOR_ONE_LINE, remarks_original))
        if remarks_generated:
            meta_data.output_dic.update(
                get_dic_data_and_print(PhKeys.REMARKS_GENERATED, PhConstants.SEPERATOR_ONE_LINE,
                                       remarks_generated))
        if info_data is not None:
            info_count = info_data.get_info_count()
            info_msg = info_data.get_info_str()
            if info_msg:
                sep = PhConstants.SEPERATOR_MULTI_LINE_TABBED if info_count > 1 else PhConstants.SEPERATOR_ONE_LINE
                meta_data.output_dic.update(get_dic_data_and_print(PhKeys.INFO_DATA, sep, info_msg))
        asn1_info = data.get_asn1_element_info()
        info = PhConstants.SEPERATOR_MULTI_OBJ.join(filter(None, [
            get_dic_data_and_print(PhKeys.TRANSACTION_ID, PhConstants.SEPERATOR_ONE_LINE, meta_data.transaction_id,
                                   dic_format=False, print_also=False),
            get_dic_data_and_print(PhKeys.MODE, PhConstants.SEPERATOR_ONE_LINE,
                                   get_mode(data.input_format, data.output_format, meta_data.input_mode_key,
                                            data.get_input_modes_hierarchy()), dic_format=False, print_also=False),
            #
            get_dic_data_and_print(PhKeys.ASN1_SCHEMA, PhConstants.SEPERATOR_ONE_LINE,
                                   asn1_info.get(PhKeys.ASN1_SCHEMA), dic_format=False,
                                   print_also=False) if asn1_info.get(PhKeys.ASN1_SCHEMA, None) else None,
            get_dic_data_and_print(PhKeys.ASN1_MODULE, PhConstants.SEPERATOR_ONE_LINE,
                                   asn1_info.get(PhKeys.ASN1_MODULE), dic_format=False,
                                   print_also=False) if asn1_info.get(PhKeys.ASN1_MODULE, None) else None,
            get_dic_data_and_print(PhKeys.ASN1_MODULE_VERSION, PhConstants.SEPERATOR_ONE_LINE,
                                   asn1_info.get(PhKeys.ASN1_MODULE_VERSION), dic_format=False,
                                   print_also=False) if asn1_info.get(PhKeys.ASN1_MODULE_VERSION, None) else None,
            get_dic_data_and_print(PhKeys.ASN1_OBJECT, PhConstants.SEPERATOR_ONE_LINE,
                                   asn1_info.get(PhKeys.ASN1_OBJECT), dic_format=False,
                                   print_also=False) if asn1_info.get(PhKeys.ASN1_OBJECT, None) else None,
            get_dic_data_and_print(PhKeys.ASN1_OBJECT_ALTERNATE, PhConstants.SEPERATOR_ONE_LINE,
                                   asn1_info.get(PhKeys.ASN1_OBJECT_ALTERNATE), dic_format=False,
                                   print_also=False) if asn1_info.get(PhKeys.ASN1_OBJECT_ALTERNATE, None) else None,
            get_dic_data_and_print(PhKeys.FETCH_ASN1_OBJECTS_LIST, PhConstants.SEPERATOR_ONE_LINE,
                                   asn1_info.get(PhKeys.FETCH_ASN1_OBJECTS_LIST), dic_format=False,
                                   print_also=False) if asn1_info.get(PhKeys.FETCH_ASN1_OBJECTS_LIST, None) else None,
            #
            get_dic_data_and_print(PhKeys.INPUT_FORMAT, PhConstants.SEPERATOR_ONE_LINE, data.input_format,
                                   dic_format=False, print_also=False),
            get_dic_data_and_print(PhKeys.OUTPUT_FORMAT, PhConstants.SEPERATOR_ONE_LINE, data.output_format,
                                   dic_format=False, print_also=False),
            get_dic_data_and_print(PhKeys.OUTPUT_FILE, PhConstants.SEPERATOR_ONE_LINE, data.output_file,
                                   dic_format=False, print_also=False) if data.output_file else None,
            get_dic_data_and_print(PhKeys.RE_PARSE_OUTPUT, PhConstants.SEPERATOR_ONE_LINE, data.re_parse_output,
                                   dic_format=False, print_also=False) if data.re_parse_output else None,
            get_dic_data_and_print(PhKeys.TLV_PARSING_OF_OUTPUT, PhConstants.SEPERATOR_ONE_LINE,
                                   data.tlv_parsing_of_output,
                                   dic_format=False, print_also=False) if data.tlv_parsing_of_output else None,
            get_dic_data_and_print(PhKeys.OUTPUT_FILE_NAME_KEYWORD, PhConstants.SEPERATOR_ONE_LINE,
                                   data.output_file_name_keyword,
                                   dic_format=False, print_also=False) if data.output_file_name_keyword else None,
            get_dic_data_and_print(PhKeys.QUITE_MODE, PhConstants.SEPERATOR_ONE_LINE, data.quite_mode,
                                   dic_format=False, print_also=False) if data.quite_mode else None,
        ]))
        meta_data.output_dic.update(get_dic_data_and_print(PhKeys.INFO, PhConstants.SEPERATOR_INFO, info))
        if meta_data.input_mode_key:
            meta_data.output_dic.update(get_dic_data_and_print(meta_data.input_mode_key, PhConstants.SEPERATOR_ONE_LINE,
                                                               meta_data.input_mode_value))
            if len(data.get_input_modes_hierarchy()) > 1:
                meta_data.output_dic.update(
                    get_dic_data_and_print(PhKeys.INPUT_MODES_HIERARCHY, PhConstants.SEPERATOR_ONE_LINE,
                                           data.get_input_modes_hierarchy_as_str()))
        if meta_data.export_mode or (meta_data.parsed_data and meta_data.output_file_path):
            meta_data.output_dic.update(
                get_dic_data_and_print(PhKeys.EXPORT_FILE if meta_data.export_mode else PhKeys.OUTPUT_FILE,
                                       PhConstants.SEPERATOR_ONE_LINE, meta_data.output_file_path))
        if meta_data.re_parsed_data and meta_data.re_output_file_path:
            meta_data.output_dic.update(get_dic_data_and_print(PhKeys.RE_OUTPUT_FILE, PhConstants.SEPERATOR_ONE_LINE,
                                                               meta_data.re_output_file_path))
    if data.print_input:
        meta_data.output_dic.update(get_dic_data_and_print(PhKeys.INPUT_DATA, input_sep, data.input_data))
    bulk_mode = True if len(data.get_input_modes_hierarchy()) >= 1 else False
    output_present = meta_data.parsed_data
    print_output = data.print_output
    if not output_present and (bulk_mode or meta_data.export_mode):
        # in bulk mode, output will not be available
        print_output = False
    if data.print_output and print_output:  # and meta_data.parsed_data:
        meta_data.output_dic.update(get_dic_data_and_print(PhKeys.OUTPUT_DATA, output_sep, meta_data.parsed_data))
    if data.print_output and print_output and data.re_parse_output:
        meta_data.output_dic.update(get_dic_data_and_print(PhKeys.RE_PARSED_DATA, input_sep, meta_data.re_parsed_data))
    PhUtil.print_separator()


def get_dic_data_and_print(key, sep, value, dic_format=True, print_also=True):
    if value is not None and isinstance(value, str) and '\n' in value:
        value = PreservedScalarString(value)
    return PhUtil.get_key_value_pair(key=key, value=value, sep=sep, dic_format=dic_format, print_also=print_also)


def set_includes_excludes_files(data, meta_data):
    """

    :param data:
    :param meta_data:
    """
    # Always exclude output files
    meta_data.excludes = ['*_' + KeyWords.OUTPUT_FILE_NAME_KEYWORD + '.*']
    if data.input_format in FormatsGroup.INPUT_FORMATS_DER:
        meta_data.include_files = FormatsGroup.INPUT_FILE_FORMATS_HEX
    elif data.input_format in FormatsGroup.BASE64_FORMATS:
        meta_data.include_files = FormatsGroup.INPUT_FILE_FORMATS_BASE_64
    elif data.input_format in FormatsGroup.INPUT_FORMATS_ASN:
        meta_data.include_files = FormatsGroup.INPUT_FILE_FORMATS_ASN
    elif data.input_format in FormatsGroup.INPUT_FORMATS_YML:
        meta_data.include_files = FormatsGroup.INPUT_FILE_FORMATS_YML
    else:  # input_format is None or unknown
        meta_data.include_files = FormatsGroup.INPUT_FILE_FORMATS
    meta_data.include_files = [('*' + x) for x in meta_data.include_files]


def prepare_config_data(data):
    data_dic = dict()
    config_data = data.__dict__
    for k, v in config_data.items():
        if str(k).startswith('_'):
            # Private variable
            continue
        if not v:
            continue
        if k in [PhKeys.ASN1_ELEMENT]:
            asn1_element_info = data.get_asn1_element_info(verbose=True)
            value = asn1_element_info.get(PhKeys.ASN1_OBJECT)
            value_alternate = asn1_element_info.get(PhKeys.ASN1_OBJECT_ALTERNATE)
            module_name = asn1_element_info.get(PhKeys.ASN1_MODULE)
            class_obj = None
            module_path = None
            # Legacy Code
            if module_name == KeyWords.MODULE_SGP22:
                class_obj = SGP_22.RSPDefinitions
                module_path = KeyWords.PATH_SGP22
            if module_name == KeyWords.MODULE_SGP32:
                class_obj = SGP_32.SGP32Definitions
                module_path = KeyWords.PATH_SGP32
            if module_name == KeyWords.MODULE_EPP:
                class_obj = eUICC_Profile_Package.PEDefinitions
                module_path = KeyWords.PATH_EPP
            if class_obj:
                try:
                    obj = type(getattr(class_obj, value))
                except:
                    obj = type(getattr(class_obj, value_alternate))
                if obj:
                    data_dic[k] = '.'.join([module_path, value])
                continue

        if k in [PhKeys.INPUT_FORMAT, PhKeys.OUTPUT_FORMAT]:
            pass
        if k in [PhKeys.OUTPUT_FILE_NAME_KEYWORD]:
            # Here we need to be ready for further usage of exported file
            data_dic[k] = KeyWords.OUTPUT_FILE_NAME_KEYWORD
            continue
        data_dic[k] = v
    file_dic = dict()
    file_dic[PhKeys.INPUT] = data_dic
    return file_dic


def clear_quotation_marks(v):
    if isinstance(v, str):
        if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")) or (
                v.startswith('"""') and v.endswith('"""')):
            v = v[1:-1]
    return v


def parse_config(config_data):
    asn1_schema = None
    asn1_object = None
    asn1_object_alternate = None
    fetch_asn1_objects_list = None
    # PhUtil.print_iter(config_data, 'config_data initial', verbose=True)
    for k, v in config_data.items():
        if not v:
            continue
        if isinstance(v, str):
            # Trim Garbage data
            v = PhUtil.trim_white_spaces_in_str(v)
            v = clear_quotation_marks(v)
            v_lower_case = v.lower()
            v_eval = None
            try:
                v_eval = eval(v)
                if isinstance(v_eval, str):
                    # Everything was already str
                    v_eval = None
            except:
                pass
            if v_lower_case in ['none']:
                v = None
                config_data[k] = v
            if v_lower_case in ['true']:
                v = True
                config_data[k] = v
            if v_lower_case in ['false']:
                v = False
                config_data[k] = v
        if not v:
            continue
        if v in [PhConstants.STR_SELECT_OPTION]:
            v = None
            config_data[k] = v
        if k in [PhKeys.INPUT_DATA]:
            if v_eval is not None:
                v = v_eval
        if k in [PhKeys.ASN1_SCHEMA]:
            asn1_schema = Asn1Versions._get_asn1_version(v)
            continue
        if k in [PhKeys.ASN1_OBJECT]:
            asn1_object = v
            continue
        if k in [PhKeys.ASN1_OBJECT_ALTERNATE]:
            asn1_object_alternate = v
            continue
        if k in [PhKeys.FETCH_ASN1_OBJECTS_LIST]:
            fetch_asn1_objects_list = v
            continue
        if k in [PhKeys.ASN1_ELEMENT]:
            temp = str(v).split('.')
            value = temp[-1]
            value_alternate = value.replace('-', '_')
            # Legacy Code
            class_obj = None
            if temp[0] == KeyWords.CLASS_SGP22:
                class_obj = SGP_22.RSPDefinitions
            if temp[0] == KeyWords.CLASS_SGP32:
                class_obj = SGP_32.SGP32Definitions
            if temp[0] == KeyWords.CLASS_EPP:
                class_obj = eUICC_Profile_Package.PEDefinitions
            if class_obj:
                try:
                    obj = getattr(class_obj, value)
                except:
                    obj = getattr(class_obj, value_alternate)
                if obj:
                    config_data[k] = obj
            continue
        if k in [PhKeys.INPUT_FORMAT, PhKeys.OUTPUT_FORMAT, PhKeys.OUTPUT_FILE_NAME_KEYWORD]:
            temp = str(v).split('.')
            value = temp[-1]
            if temp[0] == KeyWords.CLASS_FORMATS:
                config_data[k] = getattr(Formats, value)
            if temp[0] == KeyWords.CLASS_KEYWORDS:
                config_data[k] = getattr(KeyWords, value)
            continue
        config_data[k] = v
    if asn1_schema or asn1_object or asn1_object_alternate or fetch_asn1_objects_list:
        config_data[PhKeys.ASN1_ELEMENT] = Asn1(asn1_schema, asn1_object, asn1_object_alternate,
                                                fetch_asn1_objects_list=fetch_asn1_objects_list)
    # PhUtil.print_iter(config_data, 'config_data before cleaning', verbose=True, depth_level=1)
    if PhKeys.ASN1_SCHEMA in config_data:
        config_data.pop(PhKeys.ASN1_SCHEMA)
    if PhKeys.ASN1_OBJECT in config_data:
        config_data.pop(PhKeys.ASN1_OBJECT)
    if PhKeys.ASN1_OBJECT_ALTERNATE in config_data:
        config_data.pop(PhKeys.ASN1_OBJECT_ALTERNATE)
    if PhKeys.FETCH_ASN1_OBJECTS_LIST in config_data:
        config_data.pop(PhKeys.FETCH_ASN1_OBJECTS_LIST)
    # PhUtil.print_iter(config_data, 'config_data processed', verbose=True, depth_level=1)
    return config_data


def validate_config_data(config_data):
    config_data = dict(config_data).get(PhKeys.INPUT, None)
    if not config_data:
        raise ValueError(PhExceptionHelper(msg_key=Constants.CONFIG_INPUT_MISSING))
    return parse_config(config_data)


def set_input_output_format(data):
    """

    :param data:
    :return:
    """
    input_format_temp = None
    output_format_temp = None
    file_ext = PhUtil.get_file_name_and_extn(file_path=data.input_data, only_extn=True)
    if file_ext in FormatsGroup.INPUT_FILE_FORMATS_HEX:
        input_format_temp = Formats.DER
        output_format_temp = Formats.ASN1
    if file_ext in FormatsGroup.INPUT_FILE_FORMATS_BASE_64:
        input_format_temp = Formats.DER_64
        output_format_temp = Formats.ASN1
    if file_ext in FormatsGroup.INPUT_FILE_FORMATS_ASN:
        input_format_temp = Formats.ASN1
        output_format_temp = Formats.DER
    if data.output_format is None or not data.output_format:
        data.output_format = output_format_temp
    if data.input_format is None or not data.input_format:
        data.input_format = input_format_temp


def set_defaults_for_printing(data):
    if data.quite_mode is None:
        data.quite_mode = Defaults.QUITE_MODE
    if data.print_input is None:
        data.print_input = Defaults.PRINT_INPUT
    if data.print_output is None:
        data.print_output = Defaults.PRINT_OUTPUT
    if data.print_info is None:
        data.print_info = Defaults.PRINT_INFO


def set_defaults(data, meta_data):
    """
    Set Default Values if nothing is set
    :param data:
    :param meta_data:
    :return:
    """
    if data.input_format is None:
        data.input_format = Defaults.FORMAT_INPUT
    if data.output_format is None:
        data.output_format = Defaults.FORMAT_OUTPUT
    if data.re_parse_output is None:
        data.re_parse_output = Defaults.RE_PARSE_OUTPUT
    if meta_data is None:
        return
    data.set_asn1_element_name()
    if data.asn1_element:
        meta_data.operation_mode = OperationModes.ENCODE_DECODE
    else:
        meta_data.operation_mode = OperationModes.CONVERSION
    default_output_file_mapping = {
        Formats.ASN1: PhFileExtensions.ASN1,
        Formats.DER: PhFileExtensions.HEX,
        Formats.DER_64: PhFileExtensions.BASE_64,
        Formats.JSON: PhFileExtensions.JSON,
        Formats.YML: PhFileExtensions.YML,
    }
    meta_data.export_mode = True if data.output_file_name_keyword == KeyWords.EXPORT_FILE_NAME_KEYWORD else False
    meta_data.output_file_ext_default = default_output_file_mapping.get(
        Formats.YML if (meta_data.export_mode or meta_data.input_mode_key == PhKeys.INPUT_YML) else data.output_format,
        PhFileExtensions.TXT)
    meta_data.output_file_location_default = Folders.in_user()


def read_yaml(input_file):
    yaml_object = YAML()
    file_dic = yaml_object.load(input_file)
    config_data = validate_config_data(copy.deepcopy(file_dic))
    return file_dic, Data(**config_data)


def read_web_request(request_form):
    return Data(**parse_config(request_form))


def write_yml_file(output_file_path, file_dic, output_dic=None, output_versions_dic=None):
    Util.make_dirs(file_path=output_file_path)
    with open(output_file_path, 'w') as file:
        if output_dic:
            file_dic[PhKeys.OUTPUT] = dict(output_dic)
        if output_versions_dic:
            file_dic[PhKeys.OUTPUT_VERSION] = dict(output_versions_dic)
        yaml_object = YAML()
        yaml_object.width = 1000
        yaml_object.indent(mapping=4)
        yaml_object.dump(file_dic, file)


def set_output_file_path(data, meta_data):
    """

    :param data:
    :param meta_data:
    """
    file_mode = False
    remarks_needed = False
    remarks_with_indexes = False
    sample_file_name_from_input_file = False
    sample_file_name = ''
    name_as_per_remarks = ''
    if not (meta_data.input_mode_key == PhKeys.INPUT_YML or data.output_file or data.output_file_name_keyword):
        return
    output_file = data.output_file
    output_file_location = meta_data.output_file_location_default
    input_file_name = ''
    if meta_data.input_mode_key == PhKeys.INPUT_YML or meta_data.input_mode_key == PhKeys.INPUT_FILE:
        # YML File writing is mandatory, But output_file is not Provided, so Dest File will be source File only
        # File writing is needed, But output_file is not Provided,so Dest File will be prepared from source File only
        input_file_name = meta_data.input_data_org
        file_mode = True
        if not output_file:
            output_file = input_file_name
    if output_file:
        sample_file_ext = PhUtil.get_file_name_and_extn(output_file, only_extn=True)
        sample_file_folder = PhUtil.get_file_name_and_extn(output_file, only_path=True)
        sample_file_name = PhUtil.get_file_name_and_extn(output_file)
        if Variables.ITEM_INDEX in sample_file_name:
            remarks_with_indexes = True
            sample_file_name = sample_file_name.replace(Variables.ITEM_INDEX, '')
        if sample_file_name == Variables.REMARKS:
            # Only Target Directory is provided; Remarks usage is explicitly mentioned
            remarks_needed = True
            sample_file_name = sample_file_name.replace(Variables.REMARKS, '')
            output_file_location = sample_file_folder
            pass
        elif sample_file_ext:
            # Target File Provided
            output_file_name = sample_file_name
            output_file_location = sample_file_folder
        else:
            # Only Target Directory is provided
            output_file_location = os.sep.join([sample_file_folder, sample_file_name])
            if input_file_name and meta_data.input_mode_key != PhKeys.INPUT_YML:
                remarks_needed = False
                sample_file_name = PhUtil.get_file_name_and_extn(input_file_name)
                sample_file_name_from_input_file = True
            else:
                # Remarks usage is implicit
                remarks_needed = True
                sample_file_name = ''
    if data.validate_if_input_modes_hierarchy(PhKeys.INPUT_LIST) and not file_mode:
        # unique name needed
        remarks_needed = True
    if not output_file and meta_data.export_mode:
        remarks_needed = True
    if data.output_file_name_keyword and not output_file:
        remarks_needed = True
    if remarks_needed or data.output_file_name_keyword or sample_file_name_from_input_file:
        if remarks_needed:
            if data.get_extended_remarks_available():
                remarks_with_indexes = True
            name_as_per_remarks = PhUtil.get_python_friendly_name(
                data.get_remarks_as_str(user_original_remarks=not remarks_with_indexes,
                                        force_mode=True), case_sensitive=False)
        output_file_name = PhUtil.append_in_file_name(str_file_path=sample_file_name,
                                                      str_append=[name_as_per_remarks,
                                                                  data.output_file_name_keyword],
                                                      new_ext=meta_data.output_file_ext_default)
    meta_data.output_file_path = os.sep.join([output_file_location, output_file_name])


def set_re_output_file_name(data, meta_data):
    if meta_data.output_file_path and data.re_parse_output:
        meta_data.re_output_file_path = PhUtil.append_in_file_name(str_file_path=meta_data.output_file_path,
                                                                   str_append='re_parsed')
    return


def write_output_file(output_file_name, parsed_data):
    with open(output_file_name, 'w') as file:
        file.writelines(parsed_data)


def replace_data(target_data, keyword, new_value):
    if keyword not in target_data:
        return target_data
    if new_value is None:
        return target_data
    return target_data.replace(keyword, new_value)


def replace_version(target_data, data):
    module_version = data.get_asn1_module_version()
    if not module_version:
        # needed when yml file is being read with $VERSION
        # Sample: '..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\StoreMetadataRequest.hex.yml'
        # Set version based on path
        if KeyWords.CLASS_EPP in target_data:
            module_version = epp_version
        elif KeyWords.CLASS_SGP32 in target_data:
            module_version = sgp32_version
        elif KeyWords.CLASS_SGP22 in target_data:
            module_version = sgp22_version
        else:
            # default version is of SGP
            module_version = sgp22_version
    return replace_data(target_data, Variables.VERSION, module_version)


def path_generalisation(data, key):
    if key == PhKeys.INPUT_DATA:
        if isinstance(data.input_data, str):
            data.input_data = replace_version(data.input_data, data)

    if key == PhKeys.OUTPUT_FILE:
        if data.output_file:
            data.output_file = replace_version(data.output_file, data)


def get_mode(input_format, output_format, meta_data_input_mode_key, data_input_mode_hierarchy):
    mode = []
    if input_format and input_format == output_format:
        mode.append(Constants.STR_FORMATTING)
    if meta_data_input_mode_key == PhKeys.INPUT_DIR:
        mode.append(Constants.STR_DIR)
    if meta_data_input_mode_key == PhKeys.INPUT_LIST:
        if data_input_mode_hierarchy and PhKeys.INPUT_DIR in data_input_mode_hierarchy:
            mode.append(Constants.STR_DIR)
        mode.append(Constants.STR_LIST)
    if meta_data_input_mode_key == PhKeys.INPUT_YML:  # or input_format in FormatsGroup.INPUT_FORMATS_YML:
        mode.append(Constants.STR_YML_MODE)
    else:
        if not input_format:
            # Temp assignment to find the mode
            input_format = Defaults.FORMAT_INPUT
        if not output_format:
            # Temp assignment to find the mode
            output_format = Defaults.FORMAT_OUTPUT
    if input_format in FormatsGroup.INPUT_FORMATS_YML:
        mode.append(Constants.STR_YML_MODE)
    elif output_format in FormatsGroup.INPUT_FORMATS_ASN:
        mode.append(Constants.STR_ENCODING_MODE)
    elif input_format in FormatsGroup.INPUT_FORMATS_ASN:
        mode.append(Constants.STR_DECODING_MODE)
    elif input_format != output_format:
        mode.append(Constants.STR_CONVERSION_MODE)
    mode.append(Constants.STR_MODE)
    return '_'.join(filter(None, mode))
