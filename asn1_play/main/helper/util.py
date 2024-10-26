from python_helpers.ph_util import PhUtil


class Util:
    @classmethod
    def make_dirs(cls, file_path):
        PhUtil.make_dirs(file_path=file_path, quite_mode=True)
