from asn1_play.generated_code.asn1.GSMA import SGP_22
from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.helper.data import Data
from asn1_play.main.helper.formats import Formats


class AnyDataBulk(DataTypeMaster):

    def set_print_input(self):
        print_input = None
        super().set_print_input(print_input)

    def set_print_output(self):
        print_output = None
        super().set_print_output(print_output)

    def set_print_info(self):
        print_info = None
        super().set_print_info(print_info)

    def set_re_parse_output(self):
        re_parse_output = None
        super().set_re_parse_output(re_parse_output)

    def set_output_file(self):
        output_file = None
        super().set_output_file(output_file)

    def set_output_file_name_keyword(self):
        output_file_name_keyword = None
        super().set_output_file_name_keyword(output_file_name_keyword)

    def set_remarks_list(self):
        remarks_list = None
        super().set_remarks_list(remarks_list)

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
                remarks_list='# BulkMode; DirectoryInput; YmlInput; .YmlFiles;',
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest',
                input_format=Formats.YML,
                output_format=''
            ),
            #
            Data(
                remarks_list='# BulkMode; DirectoryInput; DerInput; Asn1Output; .HexFiles;',
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks_list='# BulkMode; DirectoryInput; Base64Input; Asn1Output; .Base64Files;',
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks_list='# BulkMode; DirectoryInput; Asn1Input; Der64Output; .Asn1Files;',
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.ASN1,
                output_format=Formats.DER_64
            ),
            #
            Data(
                remarks_list='# BulkMode; DirectoryInput; .YmlFiles; .HexFiles; .Base64Files; .Asn1Files; ',
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format='',
            ),
            #
            Data(
                remarks_list='# BulkMode; DirectoryInput; Asn1Input; Der64Output; DirectoryOutput; .Asn1Files;',
                raw_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.ASN1,
                output_format=Formats.DER,
                output_file=r'..\..\Data\UserData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\hex',
            ),
            #
            Data(
                remarks_list='# BulkMode; ListInput; Der64Input; Asn1Output; Asn1Element; StoreMetadataRequest;',
                raw_data=[
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
                ],
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1
            ),
            #
            Data(
                remarks_list='# BulkMode; ListInput; Der64Input; Asn1Output; Asn1Element; StoreMetadataRequest; ItemIndexVariable; ',
                raw_data=[
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
                ],
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1,
                output_file=r'..\..\Data\UserData\Temp\$ITEM_INDEX',
            ),
            #
            Data(
                # BulkMode; ListInput; Der64Input; Asn1Output; Asn1Element; StoreMetadataRequest; ExtendRemarksList;
                remarks_list=['ExtendRemarksList; Sample', 'ExtendRemarksList;'],
                raw_data=[
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
                ],
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                remarks_list='# BulkMode; ListInput; Der64Input; Asn1Output; Asn1Element; StoreMetadataRequest; RemarksVariable;',
                raw_data=[
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
                ],
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1,
                output_file=r'..\..\Data\UserData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\$REMARKS'
            ),
            #
        ]
        super().set_data_pool(data_pool)
