import os

from asn1.GSMA import SGP_22
from asn1.TCA import eUICC_Profile_Package
from converter.converter import decode_encode_asn
from helper.data import Data
from helper.options import options
from helper.util import print_done


def parse_or_update_any_data(base_data, input_format='der', output_format='asn1', print_inp=None, re_parse_op=None,
                             asn1_element=None):
    if isinstance(base_data, list):
        parsed_data_list = []
        for data in base_data:
            parsed_data_list.append(
                parse_or_update_any_data(base_data=data, input_format=input_format, output_format=output_format,
                                         print_inp=print_inp, re_parse_op=re_parse_op, asn1_element=asn1_element))
        return parsed_data_list
    if os.path.isfile(base_data):
        # file is provided
        try:
            with open(base_data, 'r') as the_file:
                resp = ''.join(the_file.readlines())
        except UnicodeDecodeError:
            # Binary File
            with open(base_data, 'rb') as the_file:
                resp = the_file.read()
        if os.path.splitext(base_data)[1] == ".asn1":
            input_format = 'asn1'
            if output_format in ['asn1']:
                output_format = 'der'
        base_data = resp

    # Set Default Values if nothing is set
    if print_inp is None: print_inp = False
    if re_parse_op is None: re_parse_op = False
    re_parsed_data = None
    # parse Data
    parsed_data = decode_encode_asn(input_data=base_data, parse_only=True,
                                    input_format=input_format, output_format=output_format,
                                    asn1_element=asn1_element)
    if re_parse_op:
        re_parsed_data = decode_encode_asn(input_data=parsed_data, parse_only=True,
                                           input_format=output_format, output_format=input_format,
                                           asn1_element=asn1_element)
    if print_inp:
        print('\nInput Data is: ')
        print(base_data)
    print('\nOutPut Data is: ')
    print(parsed_data)
    if re_parse_op:
        print('\nRe-parsed Data is: ')
        print(re_parsed_data)
    return parsed_data


def process_data(option):
    print_ip = False
    parse_op = False
    asn1_element = None

    if option == options.parse_store_meta_data_pool_console_output:
        asn1_element = SGP_22.RSPDefinitions.StoreMetadataRequest
        #
        data_pool = [
            "BF2581885A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031930101B621301F800204F0811974657374736D6470706C7573312E6578616D706C652E636F6DB705800392F91899020640BF220F300D8003883710A1060404C1020304BF230F300D8003883711A106040402020202",
            r"..\SampleData\FULL_METADATA.asn1",
            r"..\SampleData\FULL_METADATA_wo_icon.asn1",
            r"..\SampleData\FULL_METADATA.hex",
            r"..\SampleData\FULL_METADATA_wo_icon.hex",
            r"..\SampleData\FULL_METADATA.base64",
            r"..\SampleData\FULL_METADATA_wo_icon.base64",
            r"..\SampleData\FULL_METADATA_Generated.asn1",
            r"..\SampleData\FULL_METADATA_wo_icon_Generated.asn1",
        ]
        for data in data_pool:
            parse_or_update_any_data(data, print_inp=print_ip, re_parse_op=parse_op, asn1_element=asn1_element)

    if option == options.parse_profile_element_data_pool_console_output:
        asn1_element = eUICC_Profile_Package.PEDefinitions.ProfileElement
        #
        data_pool = [
            r'..\SampleData\PROFILE_OPERATIONAL1.asn1',
            "A042800102810101821447534D412050726F66696C65205061636B616765830A8929901012345678905FA506810084008B00A610060667810F010201060667810F010204B08201F8A0058000810101810667810F010201A207A105C60301020AA305A1038B010FA40C830A989209012143658709F5A527A109820442210026800198831A61184F10A0000000871002FF33FF01890000010050045553494DA682019EA10A8204422100258002022B831B8001019000800102A406830101950108800158A40683010A95010882010A8316800101A40683010195010880015AA40683010A95010882010F830B80015BA40683010A95010882011A830A800101900080015A970082011B8316800103A406830101950108800158A40683010A95010882010F8316800111A40683010195010880014AA40683010A95010882010F8321800103A406830101950108800158A40683010A950108840132A4068301019501088201048321800101A406830101950108800102A406830181950108800158A40683010A950108820104831B800101900080011AA406830101950108800140A40683010A95010882010A8310800101900080015AA40683010A95010882011583158001019000800118A40683010A95010880014297008201108310800101A40683010195010880015A97008201158316800113A406830101950108800148A40683010A95010882010F830B80015EA40683010A95010882011A83258001019000800102A010A406830101950108A406830102950108800158A40683010A950108A33FA0058000810102A13630118001018108303030303030303082020099300D800102810831323334353637383012800200818108393239343536373882020088A244A0058000810103A13BA0393013800101810831323334FFFFFFFF8201018301063010800102810830303030FFFFFFFF820102301080010A810835363738FFFFFFFF830101B37CA0058000810104810667810F010204A21DA11B83027FF18410A0000000871002FF33FF018900000100C60301810AA30B8309082999181132547698A406A104C7022F06A80F830D0A2E148CE73204000000000000AD1383110247534D41206555494343FFFFFFFFFFFFAE03830100B20483020040B606830419F1FF01A225A0058000810105A11CA01A301880020081810839323338FFFFFFFF82020081830101840122A43AA0058000810106A131A12F8001018101018210000102030405060708090A0B0C0D0E0F83100102030405060708090A0B0C0D0E0F008603010203A681BBA0058000810107A1444F07A00000015153504F08A0000001515350414F08A000000151000000820382DC0083010FC90A810280008201F08701F0EA11800F0100000100000002011203B2010000A26C302295013882010183010130173015800180861066778899AABBCCDD1122334455EEFF103022950134820102830101301730158001808610112233445566778899AABBCCDDEEFF1030229501C882010383010130173015800180861099AABBCCDDEEFF101122334455667788A681C0A0058000810108A1494F07A00000015153504F08A0000001515350414F10A00000055910100102736456616C7565820380800083010FC907810280008201F0EA11800F01000001000000020112036C756500A26C30229501388201018301013017301580018086101122334455667788112233445566778830229501348201028301013017301580018086101122334455667788112233445566778830229501C882010383010130173015800180861011223344556677881122334455667788A720A00381010B4F09A00000055910100001A0050403B00000810112040100040100A740A00381010C4F09A00000055910100002A0050403B00020810112040100040100301E8010A0000000871002FF33FF018900000100810402000100820402000100AA07A0058000810163",
        ]
        for data in data_pool:
            parse_or_update_any_data(data, print_inp=print_ip, re_parse_op=parse_op, asn1_element=asn1_element)

    if option == options.parse_any_data_pool_console_output:
        data_pool = [
            #
            Data
            (raw_data="""{
            profilePolicyRules {ppr2}
        }""",
             input_format='asn1', output_format='der', asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest
             ),
            #
            Data(raw_data='bf2a0499020520', asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest),
            #
            Data(raw_data=r'..\SampleData\UpdateMetadataRequest.txt',
                 asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest),
        ]
        for data in data_pool:
            parse_or_update_any_data(data.raw_data, print_inp=print_ip, re_parse_op=parse_op,
                                     asn1_element=data.asn1_element, input_format=data.input_format,
                                     output_format=data.output_format)

    if option == options.parse_any_data_console_output:
        input_format = 'der'
        output_format = 'asn1'
        data = 'bf2a0499020520'
        asn1_element = SGP_22.RSPDefinitions.UpdateMetadataRequest
        parse_or_update_any_data(data, print_inp=print_ip, re_parse_op=parse_op, asn1_element=asn1_element,
                                 input_format=input_format, output_format=output_format)
        #


def main():
    """

    :return:
    """
    data_processing_options = [
        options.parse_store_meta_data_pool_console_output,
        options.parse_profile_element_data_pool_console_output,
        options.parse_any_data_pool_console_output,
        options.parse_any_data_console_output,
    ]
    for data_processing_option in data_processing_options:
        process_data(data_processing_option)
    print_done()


if __name__ == '__main__':
    main()
