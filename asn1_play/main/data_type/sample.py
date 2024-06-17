from collections import OrderedDict

from python_helpers.ph_util import PhUtil

from asn1_play.generated_code.asn1.asn1 import Asn1
from asn1_play.generated_code.asn1.asn1_versions import Asn1Versions
from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.helper.data import Data
from asn1_play.main.helper.formats import Formats


class Sample(DataTypeMaster):

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
            #
            Data(
                remarks='StoreMetaData; Der to Asn1; v3_0_0',
                input_data='BF2582031C5A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D6520319301019482029089504E470D0A1A0A0000000D49484452000000400000004008040000000060B9550000000774494D4507E00B091007364C956F97000000097048597300000B1200000B1201D2DD7EFC0000000467414D410000B18F0BFC61050000021F4944415478DAED99CD1583200C803D32000B3004ABB00ECBB0822338578AF559223F49B0A8175F2EC023E1238410DB09A667E5E1E55F80BF00F686060B1E66B80420C02A32550D0E966E8CC6F0128D193460635FA66A3B7D511DB48DD94788B655D7815071BA26E61B9000ACC711841085EB398D84C0CD94F921EBE2DDAB18DB6B5005B055C3BC752B4038745C5339449CD4950248100E1D4528FAC207B228E3101A4BD4AE52BA96A603808B05D44C27ADAB2AF8807A00A6184B228014807566ECA13538E5008AC890BF06BE809E4DBEBE0B808A842A009FFD7B010436AF06B04F034C8D47EA46004703E034E4D95B90A98A447300DC353C9F07A843404D9B2D904BCA84F62480A7013C39351431225B722DE9F6AD591A0047C194E5AE19BD865AFC1A26976F088603C0A7AC9117FCE131F64200BCDFED8E290EE058906C46F2FAD09DAC885AB1550C68D2A8B426DCF69B8E71F76D195B15CD368207463513FD2DEA6648476B2500EB999B6250FA5DC0499E0B88B921F2BBAF782E877588930370724E4D3F0DD01D49DBE7E92CB940423172008F3ED3C6011C03B1396BCE6EC24800C703B862682480A20142250B8C05C081385186CD65009607D059DD772B80AE3CB963010205B054436414808ABB0FF237752480A996FB3702D8334FDA0BF002BC002FC0488053B5F5380005DC0A1703F03FFDFDC433A6FA010CF1EF4165C831E602B40134844C66E67FA4C1000618E5AB8F6008C03FAAB7028C9117E0036BAF44917035AF0E0000000049454E44AE426082B621301F800204F0811974657374736D6470706C7573312E6578616D706C652E636F6DB705800392F91899020640BF220F300D8003883710A1060404C1020304BF230F300D8003883711A106040402020202',
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v3_0_0, 'StoreMetadataRequest'),
            ),
            #
            Data(
                remarks='StoreMetaData; Der to Asn1; v2_4',
                input_data='BF2582031C5A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D6520319301019482029089504E470D0A1A0A0000000D49484452000000400000004008040000000060B9550000000774494D4507E00B091007364C956F97000000097048597300000B1200000B1201D2DD7EFC0000000467414D410000B18F0BFC61050000021F4944415478DAED99CD1583200C803D32000B3004ABB00ECBB0822338578AF559223F49B0A8175F2EC023E1238410DB09A667E5E1E55F80BF00F686060B1E66B80420C02A32550D0E966E8CC6F0128D193460635FA66A3B7D511DB48DD94788B655D7815071BA26E61B9000ACC711841085EB398D84C0CD94F921EBE2DDAB18DB6B5005B055C3BC752B4038745C5339449CD4950248100E1D4528FAC207B228E3101A4BD4AE52BA96A603808B05D44C27ADAB2AF8807A00A6184B228014807566ECA13538E5008AC890BF06BE809E4DBEBE0B808A842A009FFD7B010436AF06B04F034C8D47EA46004703E034E4D95B90A98A447300DC353C9F07A843404D9B2D904BCA84F62480A7013C39351431225B722DE9F6AD591A0047C194E5AE19BD865AFC1A26976F088603C0A7AC9117FCE131F64200BCDFED8E290EE058906C46F2FAD09DAC885AB1550C68D2A8B426DCF69B8E71F76D195B15CD368207463513FD2DEA6648476B2500EB999B6250FA5DC0499E0B88B921F2BBAF782E877588930370724E4D3F0DD01D49DBE7E92CB940423172008F3ED3C6011C03B1396BCE6EC24800C703B862682480A20142250B8C05C081385186CD65009607D059DD772B80AE3CB963010205B054436414808ABB0FF237752480A996FB3702D8334FDA0BF002BC002FC0488053B5F5380005DC0A1703F03FFDFDC433A6FA010CF1EF4165C831E602B40134844C66E67FA4C1000618E5AB8F6008C03FAAB7028C9117E0036BAF44917035AF0E0000000049454E44AE426082B621301F800204F0811974657374736D6470706C7573312E6578616D706C652E636F6DB705800392F91899020640BF220F300D8003883710A1060404C1020304BF230F300D8003883711A106040402020202',
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v2_4, 'StoreMetadataRequest'),
            ),
            #
            Data(
                remarks='SGP22; StoreMetaData; Asn1 to Der',
                input_data="""{
    iccid '989209012143658709F5'H,
    serviceProviderName "SP Name 1",
    profileName "Operational Profile Name 1"
}""",
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v3_0_0, 'StoreMetadataRequest'),
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            #
            Data(
                remarks='SGP22; StoreMetaData; Asn1 to Der; Tlv',
                input_data="""{
    iccid '989209012143658709F5'H,
    serviceProviderName "SP Name 1",
    profileName "Operational Profile Name 1"
}""",
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v3_0_0, 'StoreMetadataRequest'),
                input_format=Formats.ASN1,
                output_format=Formats.DER,
                tlv_parsing_of_output=True,
            ),
            #########
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
                asn1_element=Asn1(Asn1Versions.TCA_EPP_v3_2, 'ProfileHeader'),
                input_format=Formats.ASN1,
                output_format=Formats.DER,
            ),
            #
            Data(
                remarks='PKIX1Explicit88; Der to Asn1; Certificate',
                input_data='308201ff308201a6a0030201020209020000000000000001300a06082a8648ce3d0403023037310b300906035504061302455331153013060355040a0c0c52535020546573742045554d3111300f06035504030c0845554d20546573743020170d3230303430313039343835385a180f37343936303132343039343835385a3064310b300906035504061302455331153013060355040a0c0c52535020546573742045554d312930270603550405132038393034393033323132333435313233343531323334353637383930313233353113301106035504030c0a54657374206555494343305a301406072a8648ce3d020106092b2403030208010107034200043e590c38a9c256315ecff3291416dd335409a666fd41b3b51e5e5114f343abf0a26774c6c26c48753afe283643227bb6608cd261cc972d374a479124ebf27722a36b3069301f0603551d230418301680146fa1e5217363a822bded988a1a0d0ff5d7620db7301d0603551d0e04160414c8a64f343b85b7b0578dc57f8f13586dc804ed84300e0603551d0f0101ff04040302078030170603551d200101ff040d300b3009060767811201020101300a06082a8648ce3d040302034700304402205673c0fe8ff495ae93ae37a13296b2cb1b1017d7697053ed6920e987928699d70220059c7fec056869f24b548ac64757e4cb14d3a08609752c79a5b872a4980e338b',
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v3_0_0, 'Certificate'),
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                remarks='Asn1 Objects Static List; v3_1',
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_22_v3_1, fetch_asn1_objects_list=True),
            ),
            #
            Data(
                remarks='GSMA_SGP_32_v1_0_1; Der to Asn1; EimConfigurationData',
                input_data='301180087465737465696d3182010387020780',
                asn1_element=Asn1(Asn1Versions.GSMA_SGP_32_v1_0_1, 'EimConfigurationData'),
                input_format=Formats.DER,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                remarks='Der to Base 64',
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
                output_format=Formats.ASCII,
            ),
        ]
        super().set_data_pool(data_pool)

    def get_sample_data_pool_for_web(self):
        if not self.data_pool:
            self.set_data_pool()
        sample_data_dic = OrderedDict()
        for data in self.data_pool:
            key, data.data_group = PhUtil.generate_key_and_data_group(data.remarks)
            if key in sample_data_dic:
                raise ValueError(f'Duplicate Sample Remarks: {key}')
            sample_data_dic.update({key: super().to_dic(data)})
        return sample_data_dic
