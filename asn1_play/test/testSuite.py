import importlib
import os

import sys
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_modes_execution import PhExecutionModes
from python_helpers.ph_util import PhUtil

from asn1_play.generated_code.asn1.GSMA.SGP_22 import CompileTimeVersion as sgp22Version
from asn1_play.generated_code.asn1.GSMA.SGP_32 import CompileTimeVersion as sgp32Version
from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package import CompileTimeVersion as eppVersion


class TestSuite:

    @classmethod
    def _test(cls, **kwargs):
        """

        :param kwargs:
        :return:
        """
        # Save the original stdout
        original_stdout = sys.stdout
        try:
            import asn1_play.main.asn1play
            obj = asn1_play.main.asn1play
            file_name = kwargs.get('file_name') if 'file_name' in kwargs else f'{obj.ConfigConst.TOOL_NAME}.log'
            file_path = os.sep.join([PhUtil.path_default_log_folder, file_name])
            PhUtil.makedirs(PhUtil.get_file_name_and_extn(file_path=file_path, only_path=True))
            with open(file_path, 'w') as f:
                sys.stdout = f
                obj.set_configurations()
                if 'execution_mode' in kwargs:
                    obj.execution_mode = kwargs.get('execution_mode')
                if 'error_handling_mode' in kwargs:
                    obj.error_handling_mode = kwargs.get('error_handling_mode')
                if 'sgp_22_version' in kwargs:
                    obj.sgp_22_version = kwargs.get('sgp_22_version')
                if 'sgp_32_version' in kwargs:
                    obj.sgp_32_version = kwargs.get('sgp_32_version')
                if 'epp_version' in kwargs:
                    obj.epp_version = kwargs.get('epp_version')
                obj.print_configurations()
                obj2 = importlib.reload('asn1_play.generated_code.asn1.GSMA.SGP_22')
                obj.process_data()
        except:
            pass
        # Restore the original stdout
        sys.stdout = original_stdout

    @classmethod
    def sgp22_v2_4__epp_v3_2__sgp32_v1_0_1(cls):
        execution_mode = PhExecutionModes.ALL
        error_handling_mode = PhErrorHandlingModes.CONTINUE_ON_ERROR
        sgp_22_version = 'v2_4'
        epp_version = 'v3_2'
        sgp_32_version = 'v1_0_1'
        cls._test(
            file_name=f'{PhUtil.get_current_func_name()}.log',
            execution_mode=execution_mode, error_handling_mode=error_handling_mode,
            sgp_22_version=sgp_22_version, sgp_32_version=sgp_32_version, epp_version=epp_version
        )
    #
    # @classmethod
    # def sgp22_v3_0_0__epp_v3_1__sgp32_v1_0_1(cls):
    #     execution_mode = PhExecutionModes.ALL
    #     error_handling_mode = PhErrorHandlingModes.CONTINUE_ON_ERROR
    #     sgp_22_version = sgp22Version.v3_0_0
    #     epp_version = eppVersion.v3_1
    #     sgp_32_version = sgp32Version.v1_0_1
    #     cls._test(
    #         file_name=f'{PhUtil.get_current_func_name()}.log',
    #         execution_mode=execution_mode, error_handling_mode=error_handling_mode,
    #         sgp_22_version=sgp_22_version, sgp_32_version=sgp_32_version, epp_version=epp_version
    #     )
    #
    # @classmethod
    # def sgp22_v3_0_0__epp_v3_2__sgp32_v1_1(cls):
    #     execution_mode = PhExecutionModes.ALL
    #     error_handling_mode = PhErrorHandlingModes.CONTINUE_ON_ERROR
    #     sgp_22_version = sgp22Version.v3_0_0
    #     epp_version = eppVersion.v3_2
    #     sgp_32_version = sgp32Version.v1_1
    #     cls._test(
    #         file_name=f'{PhUtil.get_current_func_name()}.log',
    #         execution_mode=execution_mode, error_handling_mode=error_handling_mode,
    #         sgp_22_version=sgp_22_version, sgp_32_version=sgp_32_version, epp_version=epp_version
    #     )

    @classmethod
    def user(cls):
        cls._test()

    @classmethod
    def test_all(cls):
        cls.sgp22_v2_4__epp_v3_2__sgp32_v1_0_1()
        # cls.sgp22_v3_0_0__epp_v3_1__sgp32_v1_0_1()
        # cls.sgp22_v3_0_0__epp_v3_2__sgp32_v1_1()
        # cls.user()


def main():
    TestSuite.test_all()


if __name__ == '__main__':
    main()
