from conan import ConanFile
from conan.errors import ConanException
from conan.tools.files import copy
#from conan.tools.scm import Git
import os
#import semantic_version


class  TestTools(ConanFile):
    name = 'testtools'
    exports_sources = "conf/cx.yaml", "src/*"
    description = "This is a toolspackage"
    version = "1.0.0"

    def package(self):
        copy(self, "*.py", self.source_folder, os.path.join(self.package_folder), keep_path=False)

    def package_info(self):
        self.buildenv_info.define_path("TESTTOOLS", os.path.join(self.package_folder))
