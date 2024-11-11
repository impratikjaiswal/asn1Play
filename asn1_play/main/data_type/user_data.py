from asn1_play.generated_code.asn1.GSMA import SGP_22
from asn1_play.generated_code.asn1.TCA import eUICC_Profile_Package
from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.helper.data import Data
from asn1_play.main.helper.formats import Formats


class UserData(DataTypeMaster):

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
        asn1_element = None
        super().set_asn1_element(asn1_element)

    def set_data_pool(self):
        data_pool = [
            #
            Data(
                remarks='SGP22; Der to Asn1',
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                remarks='SGP22; Asn1 to Der; Tlv',
                input_data="""{
    iccid '989209012143658709F5'H,
    serviceProviderName "SP Name 1",
    profileName "Operational Profile Name 1"
}""",
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.ASN1,
                output_format=Formats.DER,
                tlv_parsing_of_output=True,
            ),
            #
            Data(
                remarks='TCA; Asn1 to Der',
                input_data="""{
    major-version 2,
    minor-version 1,
    profileType "GSMA Profile Package",
    iccid '8929901012345678905F'H,
    eUICC-Mandatory-services {
        usim NULL
    },
    eUICC-Mandatory-GFSTEList {
        {2 23 143 1 2 1}
    }
}""",
                asn1_element=eUICC_Profile_Package.PEDefinitions.ProfileHeader,
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            #
            Data(
                remarks='Der(Hex) to Base 64',
                input_data='BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                input_format=Formats.DER,
                output_format=Formats.DER_64,
            ),
            #
            Data(
                remarks='Ascii to Hex',
                input_data='Welcome To AsnPlay !!!',
                input_format=Formats.ASCII,
                output_format=Formats.HEX,
            ),
            #
            Data(
                remarks='Hex to ASCII',
                input_data='57656c636f6d6520546f2041736e506c617920212121',
                input_format=Formats.HEX,
                output_format=Formats.ASCII
            ),
            #
        ]
        super().set_data_pool(data_pool)
