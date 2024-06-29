from asn1_play.generated_code.asn1.GSMA import SGP_22
from asn1_play.generated_code.asn1.TCA import eUICC_Profile_Package
from asn1_play.generated_code.asn1.asn1 import Asn1
from asn1_play.generated_code.asn1.asn1_versions import Asn1Versions
from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.helper.data import Data
from asn1_play.main.helper.formats import Formats


class Dev(DataTypeMaster):

    def set_print_input(self):
        print_input = None
        super().set_print_input(print_input)

    def set_print_output(self):
        print_output = None
        super().set_print_output(print_output)

    def set_print_info(self):
        print_info = None
        super().set_print_info(print_info)

    def set_output_file(self):
        output_file = None
        super().set_output_file(output_file)

    def set_remarks(self):
        remarks = None
        super().set_remarks(remarks)

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
            # Can be deleted
            Data(
                input_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\StoreMetadataRequest_Mandatory.asn1',
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            # Can be deleted
            Data(
                input_data=r'..\..\Data\SampleData\TCA\eUICC_Profile_Package\$VERSION\PE_End.asn1',
                asn1_element=eUICC_Profile_Package.PEDefinitions.PE_End,
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            # Can be deleted
            Data(
                input_data=r'..\..\Data\SampleData\GSMA\SGP_22\$VERSION\StoreMetadataRequest\StoreMetadataRequest.hex',
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v2_4, 'StoreMetadataRequest'),
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            # Needs to Check
            Data(
                input_data="""{
                "ipaEuiccData": {
                  "euiccCertificate": "MIICADCCAaWgAwIBAgIJAgAAAAAAAAABMAoGCCqGSM49BAMCMDcxCzAJBgNVBAYTAkVTMRUwEwYDVQQKDAxSU1AgVGVzdCBFVU0xETAPBgNVBAMMCEVVTSBUZXN0MCAXDTIwMDQwMTA5NDg1OFoYDzc0OTYwMTI0MDk0ODU4WjBkMQswCQYDVQQGEwJFUzEVMBMGA1UECgwMUlNQIFRlc3QgRVVNMSkwJwYDVQQFEyA4OTA0OTAzMjEyMzQ1MTIzNDUxMjM0NTY3ODkwMTIzNTETMBEGA1UEAwwKVGVzdCBlVUlDQzBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABG2z9Trch9wv8Qx7/Nh60TrpcAmvoGWmdX7lcbPy67GPRsHWjz7esOdLLl1UIFHn0n9QlSAoYFr973n+n//QOVmjazBpMB8GA1UdIwQYMBaAFN09ok01DBzF0K8JZfQOw0xe5AnxMB0GA1UdDgQWBBSlJHavXVCqN2Q3zLHaIXLvRfSE8DAOBgNVHQ8BAf8EBAMCB4AwFwYDVR0gAQH/BA0wCzAJBgdngRIBAgEBMAoGCCqGSM49BAMCA0kAMEYCIQDXK0F9FNHwZV6z0OuERGAKhwYfruAzTfwrkO0sVXvviAIhAO9Rwsb+xS6HoTRoVNVebwGP5umD3hEqy7hDWOx88S9T"
                }
            }
            """,
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_32_v1_0_1, 'IpaEuiccDataResponse'),
                input_format=Formats.JSON,
                output_format=Formats.ASN1,
            ),
            # Needs to Check
            Data(
                input_data="""{
                    "ipaEuiccData": {
                      "euiccCertificate": "MIICADCCAaWgAwIBAgIJAgAAAAAAAAABMAoGCCqGSM49BAMCMDcxCzAJBgNVBAYTAkVTMRUwEwYDVQQKDAxSU1AgVGVzdCBFVU0xETAPBgNVBAMMCEVVTSBUZXN0MCAXDTIwMDQwMTA5NDg1OFoYDzc0OTYwMTI0MDk0ODU4WjBkMQswCQYDVQQGEwJFUzEVMBMGA1UECgwMUlNQIFRlc3QgRVVNMSkwJwYDVQQFEyA4OTA0OTAzMjEyMzQ1MTIzNDUxMjM0NTY3ODkwMTIzNTETMBEGA1UEAwwKVGVzdCBlVUlDQzBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABG2z9Trch9wv8Qx7/Nh60TrpcAmvoGWmdX7lcbPy67GPRsHWjz7esOdLLl1UIFHn0n9QlSAoYFr973n+n//QOVmjazBpMB8GA1UdIwQYMBaAFN09ok01DBzF0K8JZfQOw0xe5AnxMB0GA1UdDgQWBBSlJHavXVCqN2Q3zLHaIXLvRfSE8DAOBgNVHQ8BAf8EBAMCB4AwFwYDVR0gAQH/BA0wCzAJBgdngRIBAgEBMAoGCCqGSM49BAMCA0kAMEYCIQDXK0F9FNHwZV6z0OuERGAKhwYfruAzTfwrkO0sVXvviAIhAO9Rwsb+xS6HoTRoVNVebwGP5umD3hEqy7hDWOx88S9T",
                      "ipaCapabilities": {
                        "ipaFeatures": {
                          "directRspServerCommunication": true,
                          "indirectRspServerCommunication": false,
                          "eimDownloadDataHandling": false,
                          "eimCtxParams1Generation": false,
                          "eimProfileMetadataVerification": false,
                          "minimizeESipaBytes": false
                        },
                        "ipaSupportedProtocols": {
                          "ipaRetrieveHttps": false,
                          "ipaRetrieveCoaps": false,
                          "ipaInjectHttps": false,
                          "ipaInjectCoaps": false,
                          "ipaProprietary": false
                      }
                    }
                  }
                }
                """,
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_32_v1_0_1, 'IpaEuiccDataResponse'),
                input_format=Formats.JSON,
                output_format=Formats.ASN1,
            ),
        ]
        super().set_data_pool(data_pool)
