from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil
from python_helpers.ph_variables import PhVariables

from asn1_play.generated_code.asn1.GSMA.SGP_22 import version as sgp22_version
from asn1_play.generated_code.asn1.GSMA.SGP_32 import version as sgp32_version
from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package import version as epp_version
from asn1_play.generated_code.asn1.asn1 import Asn1
from asn1_play.main.helper.formats_group import FormatsGroup
from asn1_play.main.helper.keywords import KeyWords


class Data:
    def __init__(self,
                 # Common Param
                 input_data=None,
                 print_input=None,
                 print_output=None,
                 print_info=None,
                 quite_mode=None,
                 remarks=[],
                 encoding=None,
                 encoding_errors=None,
                 # TODO: Check if output_path (export yml) can be part of common param
                 output_path=None,
                 # TODO: Rename to output_file_name_suffix ?
                 output_file_name_keyword=None,
                 archive_output=None,
                 # TODO: Check if file can be exported, then zip also can be exported
                 archive_output_format=None,
                 # Specific Param
                 # TODO: Could be a common param; with default value as STR (e.g. qr Play)
                 input_format=None,
                 # TODO: Could be a common param;
                 output_format=None,
                 asn1_element=None,
                 tlv_parsing_of_output=None,
                 # TODO: Could be a common param; with default value as STR (e.g. qr Play)
                 re_parse_output=None,
                 # Unknown/System Param
                 **kwargs,
                 ):
        """
        Instantiate the Data Object for further Processing.

        :param input_data: Input Data; String(s), File Path(s), Dir Paths(s)
        :param print_input: Printing of input needed?
        :param print_output: Printing of output needed?
        :param print_info:  Printing of info needed?
        :param quite_mode: Quite mode needed? If yes, no printing at all.
        :param remarks: Remarks for Input Data
        :param encoding: Encoding for Input/Output Data
        :param encoding_errors: Encoding Errors Handling for Input/Output Data
        :param output_path: Output Path
        :param output_file_name_keyword:
        :param archive_output: Archiving of output needed?
        :param archive_output_format: Archive Output Format
        :param input_format: Format of Input Data
        :param output_format: Output Format
        :param asn1_element:
        :param tlv_parsing_of_output:
        :param re_parse_output:
        :param kwargs: To Handle unwanted/deprecated/internal/additional arguments (See Description)
        ----------

        kwargs -- (handled arguments description)
            raw_data -- @Deprecated!!! Use input_data instead \n
            remarks_list -- @Deprecated!!! Use remarks instead \n
            output_file -- @Deprecated!!! Use output_path instead \n
            data_group -- Used for Web App
        ----------
        """
        # Handle Normal Args
        self.input_data = input_data
        self.print_input = print_input
        self.print_output = print_output
        self.print_info = print_info
        self.quite_mode = quite_mode
        self.remarks = remarks
        self.encoding = encoding
        self.encoding_errors = encoding_errors
        self.output_path = output_path
        self.output_file_name_keyword = output_file_name_keyword
        self.archive_output = archive_output
        self.archive_output_format = archive_output_format
        self.input_format = input_format
        self.output_format = output_format
        self.asn1_element = asn1_element
        self.tlv_parsing_of_output = tlv_parsing_of_output
        self.re_parse_output = re_parse_output
        # Handle kwargs
        if self.input_data is None and PhKeys.RAW_DATA in kwargs:
            self.input_data = kwargs[PhKeys.RAW_DATA]
        if self.remarks is None and PhKeys.REMARKS_LIST in kwargs:
            self.remarks = kwargs[PhKeys.REMARKS_LIST]
        if self.output_path is None and PhKeys.OUTPUT_FILE in kwargs:
            self.output_path = kwargs[PhKeys.OUTPUT_FILE]
        self.data_group = kwargs.get(PhKeys.DATA_GROUP, None)
        # Handle Internal args
        self.__input_modes_hierarchy = []
        self.__asn1_schema_name = None
        self.__asn1_element_name = None
        self.__asn1_element_name_alternate = None
        self.__asn1_module_name = None
        self.__asn1_module_version = None
        self.__auto_generated_remarks = None
        self.__one_time_remarks = None
        self.__extended_remarks_needed = None
        #
        self.set_asn1_element_name()
        # Handle Remarks
        self.set_user_remarks(self.remarks)
        # Handle Remarks Variables
        self.__variables_pool = {
            #           _key : (_var_name, _var_value)
            PhKeys.INPUT_FORMAT: (PhVariables.INPUT_FORMAT, self.input_format),
            PhKeys.OUTPUT_FORMAT: (PhVariables.OUTPUT_FORMAT, self.output_format),
            PhKeys.ASN1_ELEMENT: (PhVariables.ASN1_ELEMENT, self.asn1_element),
            PhKeys.TLV_PARSING_OF_OUTPUT: (PhVariables.TLV_PARSING_OF_OUTPUT, self.tlv_parsing_of_output),
            PhKeys.RE_PARSE_OUTPUT: (PhVariables.RE_PARSE_OUTPUT, self.re_parse_output),
        }

    def set_user_remarks(self, remarks):
        self.remarks = PhUtil.to_list(remarks, trim_data=True, all_str=True)
        self.remarks = [
            x.replace(PhVariables.ASN1_ELEMENT, self.get_asn1_element_name()) if self.get_asn1_element_name() else x
            for x in self.remarks]

    def set_user_remarks_expand_variables(self):
        def __set_value(x, var_name, var_value, key_name_needed, key_):
            if var_name in x and var_value is not None:
                var_value = str(var_value)
                y = '_'.join([key_, var_value]) if key_name_needed else var_value
                return x.replace(var_name, y)
            return x

        def __expand_variable(x):
            key_name_needed = True if PhVariables.KEY_NAME in x else False
            if key_name_needed:
                x = x.replace(PhVariables.KEY_NAME, '')
            for key, value in self.__variables_pool.items():
                x = __set_value(x=x, var_name=value[0], var_value=value[1], key_name_needed=key_name_needed, key_=key)
            return x

        self.remarks = [__expand_variable(x) for x in self.remarks]

    def __get_default_remarks(self):
        self.set_asn1_element_name()
        str_input_data = str(
            self.input_data) if self.input_format in FormatsGroup.BYTE_ARRAY_FORMATS else PhUtil.combine_list_items(
            self.input_data)
        return PhUtil.append_remarks(self.__asn1_element_name, str_input_data)

    def reset_auto_generated_remarks(self):
        self.__auto_generated_remarks = None

    def set_auto_generated_remarks_if_needed(self, internal_remarks=None):
        internal_remarks = PhUtil.set_if_none(internal_remarks)
        default_remarks = self.__get_default_remarks()
        if self.remarks and self.remarks[0]:
            # User Remarks is already provided, default remarks are not needed
            default_remarks = None
        # auto generated comments are set
        self.__auto_generated_remarks = PhUtil.append_remarks(internal_remarks,
                                                              self.__auto_generated_remarks if self.__auto_generated_remarks else default_remarks,
                                                              append_mode_post=False)

    def get_remarks_as_str(self, user_original_remarks=False, force_mode=False):
        user_remarks = PhUtil.combine_list_items(self.remarks)
        if user_original_remarks:
            if user_remarks:
                return user_remarks.replace('\n', ' ')
            if not force_mode:
                return ''
        if user_remarks:
            user_remarks = PhUtil.trim_remarks(user_remarks)
        one_time_remarks = PhUtil.append_remarks(self.get_one_time_remarks(), self.__auto_generated_remarks,
                                                 append_mode_post=False)
        return PhUtil.append_remarks(one_time_remarks, user_remarks, append_mode_post=False).replace('\n', ' ')

    def set_extended_remarks_available(self, extended_remarks):
        self.__extended_remarks_needed = extended_remarks

    def get_extended_remarks_available(self):
        return self.__extended_remarks_needed

    def get_one_time_remarks(self):
        temp = self.__one_time_remarks
        self.__one_time_remarks = None
        return temp

    def set_one_time_remarks(self, one_time_remarks):
        self.__one_time_remarks = one_time_remarks

    def set_asn1_element(self, asn1_element):
        self.asn1_element = asn1_element
        self.set_asn1_element_name()

    def set_asn1_element_name(self):
        if not self.asn1_element or self.asn1_element is None:
            self.__asn1_schema_name = None
            self.__asn1_element_name = None
            self.__asn1_element_name_alternate = None
            self.__asn1_module_name = None
            self.__asn1_module_version = None
            return
        if isinstance(self.asn1_element, Asn1):
            self.__asn1_schema_name = self.asn1_element.get_asn1_schema().get_name()
            self.__asn1_element_name = self.asn1_element.get_asn1_object()
            self.__asn1_element_name_alternate = self.asn1_element.get_asn1_object_alternate()
            self.__asn1_module_name = self.asn1_element.get_asn1_schema().get_asn1_class_name()
            self.__asn1_module_version = self.asn1_element.get_asn1_schema().get_asn1_version()
            return
        # Below code is to support legacy functionality
        # Where the direct code is being used with compile Time Versions
        # Either Object is passed or Object Name is passed
        if isinstance(self.asn1_element, str):
            self.__asn1_element_name = self.asn1_element
        else:
            self.__asn1_element_name = self.asn1_element.fullname()
        if self.__asn1_element_name:
            self.set_asn1_element_name_alternate()
            self.__asn1_module_name = None if isinstance(self.asn1_element, str) else self.asn1_element._mod
        if self.__asn1_module_name:
            if self.__asn1_module_name == KeyWords.MODULE_SGP22:
                self.__asn1_module_version = sgp22_version
            if self.__asn1_module_name == KeyWords.MODULE_SGP32:
                self.__asn1_module_version = sgp32_version
            if self.__asn1_module_name == KeyWords.MODULE_EPP:
                self.__asn1_module_version = epp_version

    def get_asn1_element_info(self, verbose=False):
        if not self.asn1_element:
            return {}
        asn1_schema = self.get_asn1_schema_name()
        asn1_data_schema = {
            PhKeys.ASN1_SCHEMA: asn1_schema,
        }
        asn1_data_module = {
            PhKeys.ASN1_MODULE: self.get_asn1_module_name(),
            PhKeys.ASN1_MODULE_VERSION: self.get_asn1_module_version(),
        }
        asn1_data = asn1_data_schema if asn1_schema and not verbose else asn1_data_module
        # PhKeys.ASN1_OBJECT: self.asn1_element.get_asn1_object(),
        asn1_data.update({PhKeys.ASN1_OBJECT: self.get_asn1_element_name()})
        # PhKeys.ASN1_OBJECT_ALTERNATE: self.asn1_element.get_asn1_object_alternate(),
        asn1_data.update({PhKeys.ASN1_OBJECT_ALTERNATE: self.get_asn1_element_name_alternate()})
        if asn1_schema:
            asn1_data.update({PhKeys.FETCH_ASN1_OBJECTS_LIST: self.asn1_element.fetch_asn1_objects_list})
        return asn1_data

    def get_asn1_element_name(self):
        return self.__asn1_element_name

    def get_asn1_element_name_alternate(self):
        return self.__asn1_element_name_alternate

    def set_asn1_element_name_alternate(self):
        temp = self.__asn1_element_name.replace('-', '_')
        if temp != self.__asn1_element_name:
            self.__asn1_element_name_alternate = temp

    def get_asn1_element(self):
        return self.asn1_element

    def get_asn1_schema_name(self):
        return self.__asn1_schema_name

    def get_asn1_module_name(self):
        return self.__asn1_module_name

    def get_asn1_module_version(self):
        return self.__asn1_module_version

    def append_input_modes_hierarchy(self, input_mode_hierarchy):
        self.__input_modes_hierarchy.append(input_mode_hierarchy)

    def get_input_modes_hierarchy_as_str(self):
        return PhConstants.SEPERATOR_MULTI_OBJ.join(self.__input_modes_hierarchy)

    def get_input_modes_hierarchy(self):
        return self.__input_modes_hierarchy

    def validate_if_input_modes_hierarchy(self, input_mode_hierarchy):
        return True if input_mode_hierarchy in self.__input_modes_hierarchy else False
