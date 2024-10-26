from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from asn1_play.generated_code.asn1.GSMA.SGP_22.versions import Versions as sgp_22_versions
from asn1_play.generated_code.asn1.GSMA.SGP_32.versions import Versions as sgp_32_versions
from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.versions import Versions as epp_versions


class TestData:
    dynamic_data = {
        'user':
            {
                PhKeys.VAR_EXECUTION_MODE: 'USER',
            },
        'sample_list':
            {
                PhKeys.VAR_EXECUTION_MODE: 'SAMPLES_LIST',
            },
        'dev':
            {
                PhKeys.VAR_EXECUTION_MODE: 'DEV',
            },
        'unit_testing_external':
            {
                PhKeys.VAR_EXECUTION_MODE: 'UNIT_TESTING_EXTERNAL',
            },
        'sgp22_v2_4__epp_v3_2__sgp32_v1_0_1':
            {
                PhKeys.SGP22: sgp_22_versions.v2_4,
                PhKeys.EUICC_PROFILE_PACKAGE: epp_versions.v3_2,
                PhKeys.SGP32: sgp_32_versions.v1_0_1,
            },

        'sgp22_v3_0_0__epp_v3_1__sgp32_v1_0_1':
            {
                PhKeys.SGP22: sgp_22_versions.v3_0_0,
                PhKeys.EUICC_PROFILE_PACKAGE: epp_versions.v3_1,
                PhKeys.SGP32: sgp_32_versions.v1_0_1,
            },
        'sgp22_v3_0_0__epp_v3_2__sgp32_v1_1':
            {
                PhKeys.SGP22: sgp_22_versions.v3_0_0,
                PhKeys.EUICC_PROFILE_PACKAGE: epp_versions.v3_2,
                PhKeys.SGP32: sgp_32_versions.v1_1,
            },
        'sgp22_v3_1__epp_v3_3_1__sgp32_v1_1':
            {
                PhKeys.SGP22: sgp_22_versions.v3_1,
                PhKeys.EUICC_PROFILE_PACKAGE: epp_versions.v3_3_1,
                PhKeys.SGP32: sgp_32_versions.v1_1,
            },
    }

    default_data = {
        PhKeys.VAR_EXECUTION_MODE: 'ALL',
        PhKeys.VAR_ERROR_HANDLING_MODE: 'CONTINUE_ON_ERROR',
        PhKeys.VAR_TOP_FOLDER_PATH: '[]',
    }

    @classmethod
    def get_test_data(cls, key):
        dynamic_data = cls.dynamic_data.get(key, PhConstants.DICT_EMPTY)
        for temp_key in cls.default_data:
            if temp_key not in dynamic_data:
                dynamic_data[temp_key] = cls.default_data[temp_key]
        static_data = {
            PhKeys.TEST_CASE_ID: key,
            PhKeys.TEST_CASE_NAME: key,
            PhKeys.TEST_CASE_FILE_NAME: f'{key}.log'
        }
        return PhUtil.dict_merge(static_data, dynamic_data)
