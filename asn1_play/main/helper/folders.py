import os

from python_helpers.ph_util import PhUtil

from asn1_play import PACKAGE_NAME


class Folders:
    top_folder_path = [os.pardir, os.pardir]

    DIR_DATA = 1

    DIR_USER_DATA = 2
    DIR_USER_DATA_SGP22 = 21
    DIR_USER_DATA_SGP32 = 22
    DIR_USER_DATA_EPP = 23
    DIR_USER_DATA_GENERIC = 24

    DIR_SAMPLE_DATA = 3
    DIR_SAMPLE_DATA_SGP22 = 31
    DIR_SAMPLE_DATA_SGP32 = 32
    DIR_SAMPLE_DATA_EPP = 33
    DIR_SAMPLE_DATA_GENERIC = 34

    DIR_RES = 8
    DIR_RES_IMAGES = 81

    DIR_TEST = 9
    DIR_TEST_LOGS = 91

    LOCATIONS_MAPPING = {
        #
        DIR_RES: [PACKAGE_NAME, 'res'],
        DIR_RES_IMAGES: [PACKAGE_NAME, 'res', 'images'],
        #
        DIR_DATA: ['data'],
        #
        DIR_SAMPLE_DATA: ['data', 'sample_data'],
        DIR_SAMPLE_DATA_SGP22: ['data', 'sample_data', 'GSMA', 'SGP_22'],
        DIR_SAMPLE_DATA_SGP32: ['data', 'sample_data', 'GSMA', 'SGP_32'],
        DIR_SAMPLE_DATA_EPP: ['data', 'sample_data', 'TCA', 'eUICC_Profile_Package'],
        DIR_SAMPLE_DATA_GENERIC: ['data', 'sample_data', 'Generic'],
        #
        DIR_USER_DATA: ['data', 'user_data'],
        DIR_USER_DATA_SGP22: ['data', 'user_data', 'GSMA', 'SGP_22'],
        DIR_USER_DATA_SGP32: ['data', 'user_data', 'GSMA', 'SGP_32'],
        DIR_USER_DATA_EPP: ['data', 'user_data', 'TCA', 'eUICC_Profile_Package'],
        DIR_USER_DATA_GENERIC: ['data', 'user_data', 'Generic'],
        #
        DIR_TEST: [PACKAGE_NAME, 'test'],
        DIR_TEST_LOGS: [PACKAGE_NAME, 'test', 'logs'],
    }

    @classmethod
    def in_res_images(cls, relative_path=''):
        return cls.__get_path(Folders.DIR_RES_IMAGES, relative_path)

    @classmethod
    def in_test(cls, relative_path=''):
        return cls.__get_path(Folders.DIR_TEST, relative_path)

    @classmethod
    def in_test_logs(cls, relative_path=''):
        return cls.__get_path(Folders.DIR_TEST_LOGS, relative_path)

    @classmethod
    def in_sample(cls, relative_path=''):
        return cls.__get_path(Folders.DIR_SAMPLE_DATA, relative_path)

    @classmethod
    def in_sample_sgp_22(cls, relative_path=''):
        return cls.__get_path(Folders.DIR_SAMPLE_DATA_SGP22, relative_path)

    @classmethod
    def in_sample_sgp_32(cls, relative_path=''):
        return cls.__get_path(Folders.DIR_SAMPLE_DATA_SGP32, relative_path)

    @classmethod
    def in_sample_epp(cls, relative_path=''):
        return cls.__get_path(Folders.DIR_SAMPLE_DATA_EPP, relative_path)

    @classmethod
    def in_sample_gen(cls, relative_path=''):
        return cls.__get_path(Folders.DIR_SAMPLE_DATA_GENERIC, relative_path)

    @classmethod
    def in_user(cls, relative_path=''):
        return cls.__get_path(Folders.DIR_USER_DATA, relative_path)

    @classmethod
    def in_user_sgp_22(cls, relative_path=''):
        return cls.__get_path(Folders.DIR_USER_DATA_SGP22, relative_path)

    @classmethod
    def in_user_sgp_32(cls, relative_path=''):
        return cls.__get_path(Folders.DIR_USER_DATA_SGP32, relative_path)

    @classmethod
    def in_user_epp(cls, relative_path=''):
        return cls.__get_path(Folders.DIR_USER_DATA_EPP, relative_path)

    @classmethod
    def in_user_gen(cls, relative_path=''):
        return cls.__get_path(Folders.DIR_USER_DATA_GENERIC, relative_path)

    @classmethod
    def __get_path(cls, folder_name, relative_path):
        """

        :param folder_name:
        :param relative_path: str or list
        :return:
        """
        if folder_name not in cls.LOCATIONS_MAPPING:
            raise ValueError('Unknown Folder name')
        # if isinstance(relative_path, list):
        #     relative_path = os.sep.join(filter(None, relative_path))
        return os.sep.join(
            filter(None, PhUtil.normalise_list(
                [Folders.top_folder_path, cls.LOCATIONS_MAPPING.get(folder_name), relative_path])))
