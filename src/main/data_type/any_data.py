from src.generated_code.asn1.GSMA import SGP_22
from src.generated_code.asn1.GSMA.SGP_22 import version, Version
from src.generated_code.asn1.TCA import eUICC_Profile_Package
from src.main.helper.convert_data import ConvertData
from src.main.helper.data import Data
from src.main.helper.formats import Formats


class AnyData(ConvertData):

    def set_print_input(self):
        print_input = None
        super().set_print_input(print_input)

    def set_print_info(self):
        print_info = None
        super().set_print_info(print_info)

    def set_re_parse_output(self):
        re_parse_output = None
        super().set_re_parse_output(re_parse_output)

    def set_asn_element(self):
        pass

    def set_data_pool(self):
        data_pool = [
            # Der to ASCII via YAML
            Data(raw_data=r"..\..\SampleData\Generic\ASCII\hex_to_ascii.yaml"),
            # Der to ASCII via YAML, same file
            Data(raw_data=r"..\..\SampleData\Generic\ASCII\hex_to_ascii_op_same_file.yaml"),
            # Der to Base64 via YAML
            Data(raw_data=r"..\..\SampleData\Generic\Base64\der_to_base64.yaml"),
            # Base64 to Der via YAML
            Data(raw_data=r"..\..\SampleData\Generic\Base64\base64_to_der.yaml"),
            # StoreMetadataRequest; Der to ASN via YAML
            Data(
                raw_data=r"..\..\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest\StoreMetadataRequest.hex.yaml" if version == Version.v3_0_0
                else r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest\StoreMetadataRequest.hex.yaml",
            ),
            # StoreMetadataRequest; ASN to Der via YAML
            Data(
                raw_data=r"..\..\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest\StoreMetadataRequest.asn1.yaml" if version == Version.v3_0_0
                else r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest\StoreMetadataRequest.asn1.yaml",
            ),
            # StoreMetadataRequest Mandatory; re_parse_output ASN to Der via YAML
            Data(
                raw_data=r"..\..\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest\StoreMetadataRequest_Mandatory.asn1.yaml" if version == Version.v3_0_0
                else r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest\StoreMetadataRequest_Mandatory.asn1.yaml",
            ),
            # PROFILE_OPERATIONAL1; Der to Der via YAML
            Data(
                raw_data=r"..\..\SampleData\TCA\eUICC_Profile_Package\v3_2\PROFILE_OPERATIONAL1.hex.yaml"
            ),
            # Der to ASCII
            Data(
                raw_data="50726174696B204A61697377616C",
                asn1_element=None,
                input_format=Formats.DER,
                output_format=Formats.ASCII
            ),
            # Hex to ASCII
            Data(
                raw_data="50726174696B204A61697377616C",
                asn1_element=None,
                input_format=Formats.HEX,
                output_format=Formats.ASCII
            ),
            # ASCII to Hex
            Data(
                raw_data="Pratik Jaiswal",
                asn1_element=None,
                input_format=Formats.ASCII,
                output_format=Formats.DER
            ),
            # Hex to Base 64
            Data(
                raw_data="BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640",
                asn1_element=None,
                input_format=Formats.DER,
                output_format=Formats.DER_64
            ),
            # Base 64 to Hex
            Data(
                raw_data="vyU3WgqYkgkBIUNlhwn1kQlTUCBOYW1lIDGSGk9wZXJhdGlvbmFsIFByb2ZpbGUgTmFtZSAxmQIGQA==",
                asn1_element=None,
                input_format=Formats.DER_64,
                output_format=Formats.DER
            ),
            # ASCII to Base 64
            Data(
                raw_data="Pratik Jaiswal",
                asn1_element=None,
                input_format=Formats.ASCII,
                output_format=Formats.DER_64
            ),
            # Base 64 to ASCII
            Data(
                raw_data="UHJhdGlrIEphaXN3YWw=",
                asn1_element=None,
                input_format=Formats.DER_64,
                output_format=Formats.ASCII
            ),
            # Input Data with White spaces
            Data(
                raw_data="bf2a   04 99 02 05 20    ",
                asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            # Input Data From File
            Data(
                raw_data=
                r"..\..\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest\StoreMetadataRequest_wo_icon.base64" if version == Version.v3_0_0
                else r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest\StoreMetadataRequest_wo_icon.base64",
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1
            ),
            # Input Data From Directory (All Known File Extensions)
            Data(
                raw_data=r"..\..\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest" if version == Version.v3_0_0
                else r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest",
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format='',
                output_format=None
            ),
            # Input Data From Directory (Only ASN1 Files)
            Data(
                raw_data=r"..\..\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest" if version == Version.v3_0_0
                else r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest",
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.ASN1,
                output_format=Formats.DER_64
            ),
            # Input Data From Directory (Only Base64 Files)
            Data(
                raw_data=r"..\..\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest" if version == Version.v3_0_0
                else r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest",
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1
            ),
            # Input Data From Directory (Only Hex Files)
            Data(
                raw_data=r"..\..\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest" if version == Version.v3_0_0
                else r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest",
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            # Input Data with List
            Data(
                raw_data=[
                    'BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640',
                    'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
                    'bf25645a0a989209012143658709f591095350204e616d652031921a4f7065726174696f6e616c2050726f66696c65204e616d652031930101b621301f800204f0811974657374736d6470706c7573312e6578616d706c652e636f6db705800392f91899020640',
                ],
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1
            ),
            # HEX to ASN1
            Data(
                raw_data="BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640",
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.HEX,
                output_format=Formats.ASN1
            ),
            # re_parse_output=True
            Data(
                raw_data="BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640",
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1,
                re_parse_output=True
            ),
            # ProfileElement
            Data(
                raw_data="A042800102810101821447534D412050726F66696C65205061636B616765830A8929901012345678905FA506810084008B00A610060667810F010201060667810F010204B08201F8A0058000810101810667810F010201A207A105C60301020AA305A1038B010FA40C830A989209012143658709F5A527A109820442210026800198831A61184F10A0000000871002FF33FF01890000010050045553494DA682019EA10A8204422100258002022B831B8001019000800102A406830101950108800158A40683010A95010882010A8316800101A40683010195010880015AA40683010A95010882010F830B80015BA40683010A95010882011A830A800101900080015A970082011B8316800103A406830101950108800158A40683010A95010882010F8316800111A40683010195010880014AA40683010A95010882010F8321800103A406830101950108800158A40683010A950108840132A4068301019501088201048321800101A406830101950108800102A406830181950108800158A40683010A950108820104831B800101900080011AA406830101950108800140A40683010A95010882010A8310800101900080015AA40683010A95010882011583158001019000800118A40683010A95010880014297008201108310800101A40683010195010880015A97008201158316800113A406830101950108800148A40683010A95010882010F830B80015EA40683010A95010882011A83258001019000800102A010A406830101950108A406830102950108800158A40683010A950108A33FA0058000810102A13630118001018108303030303030303082020099300D800102810831323334353637383012800200818108393239343536373882020088A244A0058000810103A13BA0393013800101810831323334FFFFFFFF8201018301063010800102810830303030FFFFFFFF820102301080010A810835363738FFFFFFFF830101B37CA0058000810104810667810F010204A21DA11B83027FF18410A0000000871002FF33FF018900000100C60301810AA30B8309082999181132547698A406A104C7022F06A80F830D0A2E148CE73204000000000000AD1383110247534D41206555494343FFFFFFFFFFFFAE03830100B20483020040B606830419F1FF01A225A0058000810105A11CA01A301880020081810839323338FFFFFFFF82020081830101840122A43AA0058000810106A131A12F8001018101018210000102030405060708090A0B0C0D0E0F83100102030405060708090A0B0C0D0E0F008603010203A681BBA0058000810107A1444F07A00000015153504F08A0000001515350414F08A000000151000000820382DC0083010FC90A810280008201F08701F0EA11800F0100000100000002011203B2010000A26C302295013882010183010130173015800180861066778899AABBCCDD1122334455EEFF103022950134820102830101301730158001808610112233445566778899AABBCCDDEEFF1030229501C882010383010130173015800180861099AABBCCDDEEFF101122334455667788A681C0A0058000810108A1494F07A00000015153504F08A0000001515350414F10A00000055910100102736456616C7565820380800083010FC907810280008201F0EA11800F01000001000000020112036C756500A26C30229501388201018301013017301580018086101122334455667788112233445566778830229501348201028301013017301580018086101122334455667788112233445566778830229501C882010383010130173015800180861011223344556677881122334455667788A720A00381010B4F09A00000055910100001A0050403B00000810112040100040100A740A00381010C4F09A00000055910100002A0050403B00020810112040100040100301E8010A0000000871002FF33FF018900000100810402000100820402000100AA07A0058000810163",
                asn1_element=eUICC_Profile_Package.PEDefinitions.ProfileElement,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            # UpdateMetadataRequest
            Data(
                raw_data="bf2a0499020520",
                asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            # StoreMetadataRequest
            Data(
                raw_data="BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640",
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
        ]
        super().set_data_pool(data_pool)
