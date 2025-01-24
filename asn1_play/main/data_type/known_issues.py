from python_helpers.ph_keys import PhKeys

from asn1_play.generated_code.asn1.asn1 import Asn1
from asn1_play.generated_code.asn1.asn1_versions import Asn1Versions
from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.helper.data import Data
from asn1_play.main.helper.formats import Formats


class KnownIssues(DataTypeMaster):

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
        asn1_element = None
        super().set_asn1_element(asn1_element)

    def set_tlv_parsing_of_output(self):
        tlv_parsing_of_output = None
        super().set_tlv_parsing_of_output(tlv_parsing_of_output)

    def set_re_parse_output(self):
        re_parse_output = None
        super().set_re_parse_output(re_parse_output)

    def set_data_pool(self):
        data_pool_high_priority = [
            # Needs to Fix
            # ***************************** Web Request; ASN1 to Der; StoreMetadataRequest; List; Item 1 *****************************
            # Remarks: Web Request; ASN1 to Der; StoreMetadataRequest; List
            # Info => Transaction Id: prii8duqjn73; Mode: List_Decoding_Mode; Asn1 Schema: GSMA_SGP_22_v3_1; Asn1 Object: StoreMetadataRequest; Input Format: asn1; Output Format: der; Encoding: utf-8; Encoding Errors: replace; Archive Output: True; Archive Output Format: .zip
            # Input List: ['\n{\n    iccid \'989209012143658709F5\'H,\n    serviceProviderName "SP Name 1",\n    profileName "Operational Profile Name 1"\n}\n', '                                    \n{\n    iccid \'989209012143658709F5\'H,\n    serviceProviderName "SP Name 1",\n    profileName "Operational Profile Name 1"\n}', '\n{\n    iccid \'989209012143658709F5\'H,\n    serviceProviderName "SP Name 1",\n    profileName "Operational Profile Name 1"\n}\n']
            # Input Data:
            # ['\n{\n    iccid \'989209012143658709F5\'H,\n    serviceProviderName "SP Name 1",\n    profileName "Operational Profile Name 1"\n}\n', '                                    \n{\n    iccid \'989209012143658709F5\'H,\n    serviceProviderName "SP Name 1",\n    profileName "Operational Profile Name 1"\n}', '\n{\n    iccid \'989209012143658709F5\'H,\n    serviceProviderName "SP Name 1",\n    profileName "Operational Profile Name 1"\n}\n']
            # Input Data Length: 436
            # --------------------------------------------------------------------------------
            # Known Exception Occurred At Function: __handle_data; Summary: Check all your Inputs; Details: StoreMetadataRequest: invalid text, '\n{\n iccid \'989209012143658709F5\'H,\n serviceProviderName "SP Name 1",\n profileName "Operational Profile Name 1"\n}\n'; Unknown Input Data:
            # {
            #
            Data(
                remarks='Web Request; ASN1 to Der; StoreMetadataRequest; List',
                input_data=["""
{
    iccid '989209012143658709F5'H,
    serviceProviderName "SP Name 1",
    profileName "Operational Profile Name 1"
}
""", """                                    
{
    iccid '989209012143658709F5'H,
    serviceProviderName "SP Name 1",
    profileName "Operational Profile Name 1"
}""", """
{
    iccid '989209012143658709F5'H,
    serviceProviderName "SP Name 1",
    profileName "Operational Profile Name 1"
}
"""],
                input_format=Formats.ASN1,
                output_format=Formats.DER,
                asn1_element='StoreMetadataRequest',
            ),
            #
            # Needs to Fix
            # --------------------------------------------------------------------------------
            # Known Exception Occurred At Function: __handle_data; Summary: Check all your Inputs; Details: StoreMetadataRequest: invalid text, '[\n {\n iccid \'989209012143658709F5\'H,\n serviceProviderName "SP Name 1",\n profileName "Operational Profile Name 1"\n }\n ,\n {\n iccid \'989209012143658709F5\'H,\n serviceProviderName "SP Name 1",\n profileName "Operational Profile Name 1"\n }\n ,\n {\n iccid \'989209012143658709F5\'H,\n serviceProviderName "SP Name 1",\n profileName "Operational Profile Name 1"\n }\n]'; Unknown Input Data: [
            #   {
            #
            {
                PhKeys.REMARKS: 'Web Request; ASN1 to Der; StoreMetadataRequest; List; Web Request',
                PhKeys.INPUT_DATA: """[
  {
    iccid '989209012143658709F5'H,
    serviceProviderName "SP Name 1",
    profileName "Operational Profile Name 1"
  }
  ,
  {
    iccid '989209012143658709F5'H,
    serviceProviderName "SP Name 1",
    profileName "Operational Profile Name 1"
  }
  ,
  {
    iccid '989209012143658709F5'H,
    serviceProviderName "SP Name 1",
    profileName "Operational Profile Name 1"
  }
]""",
                PhKeys.INPUT_FORMAT: Formats.ASN1,
                PhKeys.OUTPUT_FORMAT: Formats.DER,
                PhKeys.ASN1_ELEMENT: 'StoreMetadataRequest'
            },
            #
            # Needs to Fix:
            # Known Exception Occurred At Function: __handle_data; Summary: Check all your Inputs; Details: IpaEuiccDataResponse.ipaEuiccData.euiccCertificate: invalid json value, 'MIICADCCAaWgAwIBAgIJAgAAAAAAAAABMAoGCCqGSM49BAMCMDcxCzAJBgNVBAYTAkVTMRUwEwYDVQQKDAxSU1AgVGVzdCBFVU0xETAPBgNVBAMMCEVVTSBUZXN0MCAXDTIwMDQwMTA5NDg1OFoYDzc0OTYwMTI0MDk0ODU4WjBkMQswCQYDVQQGEwJFUzEVMBMGA1UECgwMUlNQIFRlc3QgRVVNMSkwJwYDVQQFEyA4OTA0OTAzMjEyMzQ1MTIzNDUxMjM0NTY3ODkwMTIzNTETMBEGA1UEAwwKVGVzdCBlVUlDQzBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABG2z9Trch9wv8Qx7/Nh60TrpcAmvoGWmdX7lcbPy67GPRsHWjz7esOdLLl1UIFHn0n9QlSAoYFr973n+n//QOVmjazBpMB8GA1UdIwQYMBaAFN09ok01DBzF0K8JZfQOw0xe5AnxMB0GA1UdDgQWBBSlJHavXVCqN2Q3zLHaIXLvRfSE8DAOBgNVHQ8BAf8EBAMCB4AwFwYDVR0gAQH/BA0wCzAJBgdngRIBAgEBMAoGCCqGSM49BAMCA0kAMEYCIQDXK0F9FNHwZV6z0OuERGAKhwYfruAzTfwrkO0sVXvviAIhAO9Rwsb+xS6HoTRoVNVebwGP5umD3hEqy7hDWOx88S9T'; Unknown Input Data: {
            #    "ipaEuiccData": {
            #
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

            # Needs to Fix
            # Known Exception Occurred At Function: __handle_data; Summary: Check all your Inputs; Details: IpaEuiccDataResponse.ipaEuiccData.euiccCertificate: invalid json value, 'MIICADCCAaWgAwIBAgIJAgAAAAAAAAABMAoGCCqGSM49BAMCMDcxCzAJBgNVBAYTAkVTMRUwEwYDVQQKDAxSU1AgVGVzdCBFVU0xETAPBgNVBAMMCEVVTSBUZXN0MCAXDTIwMDQwMTA5NDg1OFoYDzc0OTYwMTI0MDk0ODU4WjBkMQswCQYDVQQGEwJFUzEVMBMGA1UECgwMUlNQIFRlc3QgRVVNMSkwJwYDVQQFEyA4OTA0OTAzMjEyMzQ1MTIzNDUxMjM0NTY3ODkwMTIzNTETMBEGA1UEAwwKVGVzdCBlVUlDQzBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABG2z9Trch9wv8Qx7/Nh60TrpcAmvoGWmdX7lcbPy67GPRsHWjz7esOdLLl1UIFHn0n9QlSAoYFr973n+n//QOVmjazBpMB8GA1UdIwQYMBaAFN09ok01DBzF0K8JZfQOw0xe5AnxMB0GA1UdDgQWBBSlJHavXVCqN2Q3zLHaIXLvRfSE8DAOBgNVHQ8BAf8EBAMCB4AwFwYDVR0gAQH/BA0wCzAJBgdngRIBAgEBMAoGCCqGSM49BAMCA0kAMEYCIQDXK0F9FNHwZV6z0OuERGAKhwYfruAzTfwrkO0sVXvviAIhAO9Rwsb+xS6HoTRoVNVebwGP5umD3hEqy7hDWOx88S9T'; Unknown Input Data: {
            #                     "ipaEuiccData": {
            #
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
            #
        ]

        data_pool_low_priority = [
            #
            # (Should be considered as feature request)
            {
                PhKeys.REMARKS: 'Hex to Ascii; TypeError: expected string or bytes-like object',
                PhKeys.INPUT_DATA: 85,
                PhKeys.INPUT_FORMAT: Formats.HEX,
                PhKeys.OUTPUT_FORMAT: Formats.ASCII,
            },
            #
            # (Should be considered as feature request)
            {
                PhKeys.REMARKS: 'Hex to Ascii; TypeError: expected string or bytes-like object',
                PhKeys.INPUT_DATA: 61,
                PhKeys.INPUT_FORMAT: Formats.HEX,
                PhKeys.OUTPUT_FORMAT: Formats.ASCII,
            },
            # Needs to Fix the error msg:
            # Through some graceful Error: Reason for failure or something else
            #
            # --------------------------------------------------------------------------------
            # Known Exception Occurred At Function: __handle_data; Summary: Check all your Inputs; Details: input data conversion is not possible; Input Data:
            #
            {
                PhKeys.REMARKS: 'Web Request; Hex to Ascii; (Non UTF) input data conversion is not possible; Input Data: ',
                PhKeys.INPUT_DATA: '\x85',
                PhKeys.INPUT_FORMAT: Formats.HEX,
                PhKeys.OUTPUT_FORMAT: Formats.ASCII,
            },
        ]
        super().set_data_pool(
            data_pool_high_priority
            + data_pool_low_priority
        )
