from python_helpers.ph_constants import PhConstants

from src.main.helper.constants import Constants


def append_remarks(remarks1, remarks2):
    if remarks2 is not None:
        sep = PhConstants.SEPERATOR_MULTI_OBJ
        remarks1 = trim_remarks(remarks1, Constants.DEFAULT_REMARKS_MAX_LENGTH - (len(remarks2) + len(sep)))
        remarks1 = sep.join(filter(None, [remarks1, remarks2]))
    return remarks1


def trim_remarks(user_remarks, max_length):
    if len(user_remarks) > max_length > 0:
        # Trimming is needed
        user_remarks = user_remarks[
                       :max_length - Constants.DEFAULT_TRIM_STRING_LENGTH] + Constants.DEFAULT_TRIM_STRING
    return user_remarks


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
                 input_modes_hierarchy=None,
                 ):
        self.raw_data = raw_data
        self.asn1_element = asn1_element
        self.asn1_element_name = None
        self.set_asn1_element_name()
        self.input_format = input_format
        self.output_format = output_format
        self.print_input = print_input
        self.print_output = print_output
        self.print_info = print_info
        self.re_parse_output = re_parse_output
        self.output_file = output_file
        self.output_file_name_keyword = output_file_name_keyword
        self.remarks_list = None
        self.set_remarks(remarks_list)
        self.internal_remarks = None
        self.input_modes_hierarchy = [input_modes_hierarchy] if input_modes_hierarchy else []

    def set_remarks(self, remarks_list):
        self.remarks_list = remarks_list if isinstance(remarks_list, list) else [remarks_list]

    def __get_default_remarks(self):
        self.set_asn1_element_name()
        str_raw_data = str(self.raw_data)
        return PhConstants.SEPERATOR_MULTI_OBJ.join(
            [self.asn1_element_name, str_raw_data]) if self.asn1_element_name else str_raw_data

    def set_default_remarks_if_not_set(self):
        if not self.remarks_list:
            # Remarks is not already provided
            self.set_remarks(self.__get_default_remarks())

    def set_default_internal_remarks_if_not_set(self, internal_remarks):
        if self.remarks_list:
            self.internal_remarks = internal_remarks
        else:
            self.internal_remarks = append_remarks(self.__get_default_remarks(), internal_remarks)

    def get_remarks_as_str(self):
        user_remarks = PhConstants.SEPERATOR_MULTI_OBJ.join(filter(None, self.remarks_list))
        if user_remarks:
            user_remarks = trim_remarks(user_remarks, Constants.DEFAULT_REMARKS_MAX_LENGTH)
        return append_remarks(user_remarks, self.internal_remarks)

    def set_asn1_element_name(self):
        self.asn1_element_name = self.asn1_element.fullname() if self.asn1_element else None

    def append_input_modes_hierarchy(self, input_mode_hierarchy):
        self.input_modes_hierarchy.append(input_mode_hierarchy)

    def get_input_modes_hierarchy(self):
        return PhConstants.SEPERATOR_MULTI_OBJ.join(self.input_modes_hierarchy)

    def validate_if_input_modes_hierarchy(self, input_mode_hierarchy):
        return True if input_mode_hierarchy in self.input_modes_hierarchy else False
