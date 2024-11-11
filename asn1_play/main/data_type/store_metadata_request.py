from asn1_play.generated_code.asn1.GSMA import SGP_22
from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.helper.folders import Folders


class StoreMetaData(DataTypeMaster):

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

    def set_archive_output(self):
        archive_output = None
        super().set_archive_output(archive_output)

    def set_archive_output_format(self):
        archive_output_format = None
        super().set_archive_output_format(archive_output_format)

    def set_output_file(self):
        output_file = None
        super().set_output_file(output_file)

    def set_re_parse_output(self):
        re_parse_output = None
        super().set_re_parse_output(re_parse_output)

    def set_output_file_name_keyword(self):
        output_file_name_keyword = None
        super().set_output_file_name_keyword(output_file_name_keyword)

    def set_output_format(self):
        output_format = None
        super().set_output_format(output_format)

    def set_input_format(self):
        input_format = None
        super().set_input_format(input_format)

    def set_asn1_element(self):
        asn1_element = SGP_22.RSPDefinitions.StoreMetadataRequest
        super().set_asn1_element(asn1_element)

    def set_data_pool(self):
        data_pool = [
            #
            'BF2581885A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031930101B621301F800204F0811974657374736D6470706C7573312E6578616D706C652E636F6DB705800392F91899020640BF220F300D8003883710A1060404C1020304BF230F300D8003883711A106040402020202',
            #
            Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest\StoreMetadataRequest.asn1'),
            #
            Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest\StoreMetadataRequest_wo_icon.asn1'),
            #
            Folders.in_sample_sgp_22(
                r'$VERSION\StoreMetadataRequest\StoreMetadataRequest_wo_icon_wo_serviceSpecific.asn1'),
            #
            Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest\StoreMetadataRequest.hex'),
            #
            Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest\StoreMetadataRequest_wo_icon.hex'),
            #
            Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest\StoreMetadataRequest.base64'),
            #
            Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest\StoreMetadataRequest_wo_icon.base64'),
            #
            Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest\StoreMetadataRequest_output.asn1'),
            #
            Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest\StoreMetadataRequest_wo_icon_output.asn1'),
            #
            Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest\StoreMetadataRequest_Mandatory.asn1'),
            #
            Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest\StoreMetadataRequest_ppr.asn1'),
            #
            Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest\StoreMetadataRequest_Mandatory.hex'),
            #
            Folders.in_sample_sgp_22(r'$VERSION\StoreMetadataRequest\StoreMetadataRequest_ppr.hex'),
            #
        ]
        super().set_data_pool(data_pool)
