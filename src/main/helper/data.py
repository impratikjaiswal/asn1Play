from python_helpers.ph_constants import PhConstants
from python_helpers.ph_util import PhUtil

from src.generated_code.asn1.GSMA.SGP_22 import version as sgp22_version
from src.generated_code.asn1.TCA.eUICC_Profile_Package import version as epp_version
from src.main.helper.keywords import KeyWords
from src.main.helper.variables import Variables


class Data:
    def __init__(self,
                 raw_data,
                 asn1_element=None,
                 input_format=None,
                 output_format=None,
                 print_input=None,
                 print_output=None,
                 print_info=None,
                 re_parse_output=None,
                 output_file=None,
                 output_file_name_keyword=None,
                 remarks_list=[],
                 ):
        self.raw_data = raw_data
        self.asn1_element = asn1_element
        self.input_format = input_format
        self.output_format = output_format
        self.print_input = print_input
        self.print_output = print_output
        self.print_info = print_info
        self.re_parse_output = re_parse_output
        self.output_file = output_file
        self.output_file_name_keyword = output_file_name_keyword
        self.remarks_list = None
        #
        self.__asn1_element_name = None
        self.__asn1_module_name = None
        self.__asn1_module_version = None
        self.__auto_generated_remarks = None
        self.__input_modes_hierarchy = []
        self.__one_time_remarks = None
        self.__extended_remarks_needed = None
        #
        self.set_asn1_element_name()
        self.set_user_remarks(remarks_list)

    def set_user_remarks(self, remarks_list):
        self.remarks_list = PhUtil.cast_to_list(remarks_list, trim_data=True, all_str=True)
        self.remarks_list = [
            x.replace(Variables.ASN_ELEMENT, self.get_asn1_element_name()) if self.get_asn1_element_name() else x for x
            in self.remarks_list]

    def __get_default_remarks(self):
        self.set_asn1_element_name()
        str_raw_data = PhUtil.combine_list_items(self.raw_data)
        return PhUtil.append_remarks(self.__asn1_element_name, str_raw_data)

    def reset_auto_generated_remarks(self):
        self.__auto_generated_remarks = None

    def set_auto_generated_remarks_if_needed(self, internal_remarks=None):
        internal_remarks = PhUtil.set_if_not_none(internal_remarks)
        default_remarks = self.__get_default_remarks()
        if self.remarks_list and self.remarks_list[0]:
            # User Remarks is already provided, default remarks are not needed
            default_remarks = None
        # auto generated comments are set
        self.__auto_generated_remarks = PhUtil.append_remarks(internal_remarks,
                                                              self.__auto_generated_remarks if self.__auto_generated_remarks else default_remarks,
                                                              append_mode_post=False)

    def get_remarks_as_str(self, user_original_remarks=False, force_mode=False):
        user_remarks = PhUtil.combine_list_items(self.remarks_list)
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

    def set_asn1_element_name(self):
        self.__asn1_element_name = (
            self.asn1_element if isinstance(self.asn1_element,
                                            str) else self.asn1_element.fullname()) if self.asn1_element else None
        if self.__asn1_element_name:
            self.__asn1_element_name = self.__asn1_element_name.replace('-', '_')
            self.__asn1_module_name = None if isinstance(self.asn1_element, str) else self.asn1_element._mod
        if self.__asn1_module_name:
            if self.__asn1_module_name == KeyWords.MODULE_SGP22:
                self.__asn1_module_version = sgp22_version
            if self.__asn1_module_name == KeyWords.MODULE_EPP:
                self.__asn1_module_version = epp_version

    def get_asn1_element_name(self):
        return self.__asn1_element_name

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
