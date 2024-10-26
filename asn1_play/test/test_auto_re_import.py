import os

import sys
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from asn1_play.test.test_data import TestData

"""
Ref: 
TODO: Run Time import needed

https://pyunit.sourceforge.net/notes/reloading.html
https://web.archive.org/web/20080926094551/http://mail.python.org/pipermail/python-list/2003-December/241654.html
https://stackoverflow.com/questions/437589/how-do-i-unload-reload-a-python-module/61617169#61617169

"""

package_name = 'asn1_play.main'
module_name = 'asn1_play.main.asn1play'


def reload_module(full_module_name):
    """
        Assuming the folder `full_module_name` is a folder inside some
        folder on the python sys.path, for example, sys.path as `C:/`, and
        you are inside the folder `C:/Path With Spaces` on the file
        `C:/Path With Spaces/main.py` and want to re-import some files on
        the folder `C:/Path With Spaces/tests`

        @param full_module_name   the relative full path to the module file
                                  you want to reload from a folder on the
                                  python `sys.path`
    """
    import imp
    import sys
    import importlib
    PhUtil.print_heading('Before')
    PhUtil.print_modules(depth_level=1)
    if full_module_name in sys.modules:
        module_object = sys.modules[full_module_name]
        module_object = imp.reload(module_object)
    else:
        importlib.import_module(full_module_name)
    PhUtil.print_heading('After')
    PhUtil.print_modules(depth_level=1)


class TestAutoReImport:
    module_imported = None

    @classmethod
    def test(cls, **kwargs):
        """

        :param kwargs:
        :return:
        """
        # global module_imported
        # Save the original stdout
        original_stdout = sys.stdout

        #

        # # PhUtil.print_iter(sys.modules, depth_level=1, header='before')
        # reimport_needed = False
        # if TestBatch.module_imported is not None:
        #     reimport_needed = True
        # TestBatch.module_imported = importlib.import_module('.asn1play', package_name)
        #
        # full_module_name = f'{package_name}.asn1play'
        # if reimport_needed:
        #     if full_module_name in sys.modules:
        #         module_object = sys.modules[full_module_name]
        #         module_object = importlib.reload(module_object)
        #     else:
        #         importlib.import_module(full_module_name)
        # TestBatch.module_imported.set_configurations()
        # TestBatch.module_imported.print_configurations()

        # dreload(TestBatch.module_imported)
        # importlib.reload(TestBatch.module_imported)

        # for mod in sys.modules.keys():
        #     if isinstance(mod, str):
        #         continue
        #     # print(f'mod: {mod.__name__}')
        #     importlib.reload(mod)

        # PhUtil.print_iter(sys.modules, depth_level=1, header='after')
        # ref = sys.getrefcount(TestBatch.module_imported)

        # print(f'ref are {ref}')
        # try:
        #     del sys.modules['asn1_play']
        #     setattr(TestBatch.module_imported, ".asn1play", None)
        #     # del TestBatch.module_imported
        # except KeyError:
        #     pass
        # ref = sys.getrefcount(TestBatch.module_imported)
        # print(f'ref are {ref}')
        # for item in sys.modules.keys():
        #     if item.startswith('asn1_play'):
        #         del sys.modules[item]
        #     pass

        try:
            #     if 'sgp_22_version' in kwargs:
            #         # import importlib
            #         # importlib.reload(package)
            #         package = None
            #         _version = kwargs.get('sgp_22_version')
            #         file_path = r'D:\Other\Github_Self\asn1Play\asn1_play\generated_code\asn1\GSMA\SGP_22\compile_time_version.py'
            #         with open(file_path, 'w') as f:
            #             f.write(sgp_22_data.replace('XXX', _version))
            #     # from asn1_play.generated_code.asn1.GSMA import SGP_22 as package_sgp_22
            #     # package = package_sgp_22
            #     # package.set_version(_version)
            #     # sgp22Version = _version
            #     # print(f'version: {sgp22Version} ')
            #     # obj.sgp_22_version = kwargs.get('sgp_22_version')
            #     # Asn1(Asn1Versions.GSMA_SGP_22_v2_4)
            import asn1_play.main.asn1play
            obj = asn1_play.main.asn1play
            #     importlib.import_module(asn1_play.main.asn1play)
            file_name = kwargs.get('file_name') if 'file_name' in kwargs else f'{obj.ConfigConst.TOOL_NAME}.log'
            file_path = os.sep.join([PhUtil.path_default_log_folder, file_name])
            PhUtil.make_dirs(file_path=file_path)
            PhUtil.print_separator(main_text=f'{file_path}')
            with open(file_path, 'w') as f:
                sys.stdout = f
                PhUtil.print_separator(main_text=f'{file_path}')
                obj.set_configurations()
                if 'execution_mode' in kwargs:
                    obj.execution_mode = kwargs.get('execution_mode')
                if 'error_handling_mode' in kwargs:
                    obj.error_handling_mode = kwargs.get('error_handling_mode')
                if 'sgp_22_version' in kwargs:
                    obj.sgp_22_version = kwargs.get('sgp_22_version')
                    # Asn1(Asn1Versions.GSMA_SGP_22_v2_4)
                    # obj.set_configurations()
                if 'sgp_32_version' in kwargs:
                    obj.sgp_32_version = kwargs.get('sgp_32_version')
                if 'epp_version' in kwargs:
                    obj.epp_version = kwargs.get('epp_version')
                obj.print_configurations()
                obj.process_data()
                # Restore the original stdout
                sys.stdout = original_stdout
        except Exception as e:
            # Restore the original stdout
            sys.stdout = original_stdout
        reload_module('asn1_play')
        from asn1_play.main import asn1play
        asn1play.set_configurations()
        asn1play.print_configurations()

    @classmethod
    def test_all(cls):
        """

        :return:
        """
        test_cases_data_pool = [
            # Unit Testing Sequences
            TestData.get_test_data('sgp22_v3_1__epp_v3_3_1__sgp32_v1_1'),
            TestData.get_test_data('sgp22_v2_4__epp_v3_2__sgp32_v1_0_1'),
            TestData.get_test_data('sgp22_v3_0_0__epp_v3_1__sgp32_v1_0_1'),
            TestData.get_test_data('sgp22_v3_0_0__epp_v3_2__sgp32_v1_1'),
            TestData.get_test_data('user'),
        ]
        for test_case_data in test_cases_data_pool:
            """
            """
            PhUtil.print_iter(test_case_data, header=test_case_data.get(PhKeys.TEST_CASE_ID))
            cls.test(test_case_data)


def main():
    TestAutoReImport.test_all()


if __name__ == '__main__':
    main()
