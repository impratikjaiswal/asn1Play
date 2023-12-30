import importlib

from asn1_play.generated_code.asn1.GSMA.SGP_22.v3_0_0.python_gen.sgp22.sgp22 import PKIX1Explicit88, PKIX1Implicit88

# from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_4.python_gen.sgp22.sgp22 import RSPDefinitions
# from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_4.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

OFFSET_CLASSES = 0
OFFSET_MAPPING_CLASSES = 1

__module_name = '.sgp22'
__module_mapping_name = '.sgp22_mapping'
__class_name = 'RSPDefinitions'
__class_name_mapping = 'sgp_22_mapping'
__package_name_pre = 'asn1_play.generated_code.asn1.GSMA.SGP_22'
__package_name_post = 'python_gen.sgp22'

version = None
asn1_mapping = None
RSPDefinitions = None


def __set_asn1_classes(param):
    global RSPDefinitions
    RSPDefinitions = param


def __set_asn1_mapping(param):
    pkix_mapping = {
        'Certificate': PKIX1Explicit88.Certificate,
        'CertificateList': PKIX1Explicit88.CertificateList,
        'Time': PKIX1Explicit88.Time,
        'SubjectKeyIdentifier': PKIX1Implicit88.SubjectKeyIdentifier,
    }
    # TODO: SML-332
    all_mapping = {
        **param,
        **pkix_mapping
    }
    global asn1_mapping
    asn1_mapping = all_mapping


def is_valid_state():
    return False if version is None else True


def get_version():
    return version


def set_version(version_user):
    def __set_version_duck_typing(version_user_local):
        try:
            package_name = '.'.join([__package_name_pre, version_user_local, __package_name_post])

            module_imported = importlib.import_module(__module_name, package_name)
            class_imported = getattr(module_imported, __class_name)

            module_mapping_imported = importlib.import_module(__module_mapping_name, package_name)
            class_mapping_imported = getattr(module_mapping_imported, __class_name_mapping)
        except Exception:
            return None
            # raise AttributeError(
            #     PhExceptionHelper(msg=f'Unknown version {version}', function_name=set_version))
        # PhUtil.print_modules(filter_string=package_name)
        # PhUtil.get_classes_list(module_to_explore=module_imported, print_also=True)
        return [class_imported], [class_mapping_imported]

    imported_objects = __set_version_duck_typing(version_user)
    if imported_objects is None:
        return None
    __set_version(version_user)
    __set_asn1_classes(imported_objects[OFFSET_CLASSES][0])
    __set_asn1_mapping(imported_objects[OFFSET_MAPPING_CLASSES][0])


def __set_version(param):
    global version
    version = param


def get_asn1_mapping():
    return asn1_mapping


def get_asn1_mapping_keys():
    return list(asn1_mapping.keys())
