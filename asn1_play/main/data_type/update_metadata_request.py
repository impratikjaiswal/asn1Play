from python_helpers.ph_variables import PhVariables

from asn1_play.generated_code.asn1.GSMA import SGP_22
from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.helper.data import Data
from asn1_play.main.helper.folders import Folders
from asn1_play.main.helper.formats import Formats


class UpdateMetadataRequest(DataTypeMaster):

    def __init__(self):
        super().__init__()

    def set_print_input(self):
        print_input = None
        super().set_print_input(print_input)

    def set_print_output(self):
        print_output = None
        super().set_print_output(print_output)

    def set_print_info(self):
        print_info = None
        super().set_print_info(print_info)

    def set_quiet_mode(self):
        quite_mode = None
        super().set_quiet_mode(quite_mode)

    def set_remarks(self):
        remarks = None
        super().set_remarks(remarks)

    def set_encoding(self):
        encoding = None
        super().set_encoding(encoding)

    def set_encoding_errors(self):
        encoding_errors = None
        super().set_encoding_errors(encoding_errors)

    def set_output_path(self):
        output_path = None
        super().set_output_path(output_path)

    def set_output_file_name_keyword(self):
        output_file_name_keyword = None
        super().set_output_file_name_keyword(output_file_name_keyword)

    def set_archive_output(self):
        archive_output = None
        super().set_archive_output(archive_output)

    def set_archive_output_format(self):
        archive_output_format = None
        super().set_archive_output_format(archive_output_format)

    def set_input_format(self):
        input_format = None
        super().set_input_format(input_format)

    def set_output_format(self):
        output_format = None
        super().set_output_format(output_format)

    def set_asn1_element(self):
        asn1_element = SGP_22.RSPDefinitions.UpdateMetadataRequest
        super().set_asn1_element(asn1_element)

    def set_tlv_parsing_of_output(self):
        tlv_parsing_of_output = None
        super().set_tlv_parsing_of_output(tlv_parsing_of_output)

    def set_re_parse_output(self):
        re_parse_output = None
        super().set_re_parse_output(re_parse_output)

    def set_data_pool(self):
        data_pool = [
            #
            Data(
                input_data='bf2a0499020520'
            ),
            #
            Data(
                input_data="""{
                profilePolicyRules {ppr2}
                }""",
                input_format=Formats.ASN1,
                output_format=Formats.DER
            ),
            #
            Data(
                input_data=Folders.in_sample_sgp_22(
                    fr'{PhVariables.VERSION}\UpdateMetadataRequest\UpdateMetadataRequest.asn1')
            ),
            #
            Data(
                input_data=Folders.in_sample_sgp_22(
                    fr'{PhVariables.VERSION}\UpdateMetadataRequest\UpdateMetadataRequest_ppr0_no_ppr.asn1')
            ),
            #
            Data(
                input_data=Folders.in_sample_sgp_22(
                    fr'{PhVariables.VERSION}\UpdateMetadataRequest\UpdateMetadataRequest_ppr1_pp2.asn1')
            ),
            #
            Data(
                input_data=Folders.in_sample_sgp_22(
                    fr'{PhVariables.VERSION}\UpdateMetadataRequest\UpdateMetadataRequest_ppr2_ppr1.asn1')
            ),
            #
            Data(
                input_data=Folders.in_sample_sgp_22(
                    fr'{PhVariables.VERSION}\UpdateMetadataRequest\UpdateMetadataRequest_ppr3_ppr1_ppr2.asn1')
            ),
            #
            Data(
                input_data=Folders.in_sample_sgp_22(
                    fr'{PhVariables.VERSION}\UpdateMetadataRequest\UpdateMetadataRequest.hex')
            ),
        ]
        super().set_data_pool(data_pool)
