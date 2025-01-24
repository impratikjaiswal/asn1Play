from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_modes_execution import PhExecutionModes
from python_helpers.ph_util import PhUtil

from asn1_play.generated_code.asn1.GSMA.SGP_22.versions import Versions as sgp_22_versions
from asn1_play.generated_code.asn1.GSMA.SGP_32.versions import Versions as sgp_32_versions
from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.versions import Versions as epp_versions


class TestData:
    # Unit Testing Sequences
    dynamic_data = {
        PhExecutionModes.UNIT_TESTING:
            {
                PhKeys.VAR_EXECUTION_MODE: 'UNIT_TESTING',
            },
        PhExecutionModes.USER:
            {
                PhKeys.VAR_EXECUTION_MODE: 'USER',
            },
        PhExecutionModes.SAMPLES_LIST:
            {
                PhKeys.VAR_EXECUTION_MODE: 'SAMPLES_LIST',
            },
        PhExecutionModes.DEV:
            {
                PhKeys.VAR_EXECUTION_MODE: 'DEV',
            },
        PhExecutionModes.KNOWN_ISSUES:
            {
                PhKeys.VAR_EXECUTION_MODE: 'KNOWN_ISSUES',
            },
        PhExecutionModes.UNIT_TESTING_EXTERNAL:
            {
                PhKeys.VAR_EXECUTION_MODE: 'UNIT_TESTING_EXTERNAL',
            },
        PhExecutionModes.ALL:
            {
                PhKeys.VAR_EXECUTION_MODE: 'ALL',
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

    #
    dynamic_data_cli = {
        'no_param':
            {
                PhKeys.BATCH_PARAMS: '',
            },
        '--help':
            {
                PhKeys.BATCH_PARAMS: '--help',
            },
    }

    read_me_cli_pool = [
    ]

    @classmethod
    def get_test_data(cls, key):
        dynamic_data = cls.dynamic_data.get(key, PhConstants.DICT_EMPTY)
        key_name = PhExecutionModes.get_key_name(key) if key in PhExecutionModes.KEYS_NAME else key
        for temp_key in cls.default_data:
            if temp_key not in dynamic_data:
                dynamic_data[temp_key] = cls.default_data[temp_key]
        static_data = {
            PhKeys.TEST_CASE_ID: key_name,
            PhKeys.TEST_CASE_NAME: key_name,
            PhKeys.TEST_CASE_FILE_NAME: f'{key_name}.log'
        }
        return PhUtil.dict_merge(static_data, dynamic_data)

    @classmethod
    def get_test_data_cli(cls, key):
        key_name = 'cli_' + key
        dynamic_data = cls.dynamic_data_cli.get(key, PhConstants.DICT_EMPTY)
        static_data = {
            PhKeys.TEST_CASE_ID: key_name,
            PhKeys.TEST_CASE_NAME: key_name,
            PhKeys.TEST_CASE_FILE_NAME: f'{key_name}.log'
        }
        return PhUtil.dict_merge(static_data, dynamic_data)

    @classmethod
    def generate_dynamic_cli_from_read_me(cls):
        for index, batch_param in enumerate(TestData.read_me_cli_pool):
            TestData.dynamic_data_cli.update({f'read_me_{index}': {PhKeys.BATCH_PARAMS: f'"{batch_param}"'}})
