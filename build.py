from git import Repo
import argparse
import os 
import subprocess
import sys

class PackageBuilder():
    def get_if_branch_build(self):
        l_repo = Repo(path=os.getcwd())
        l_branch = l_repo.active_branch.name
        sha = l_repo.head.object.hexsha
        tagmap = {}
        for t in l_repo.tags:
            tagmap.setdefault(l_repo.commit(t), []).append(t)

        try:
            print("sha id is =", sha)
            tags = tagmap[l_repo.commit(sha)]
        except KeyError:
            return 1

    def execute_cmnd(self, conan_cmd):
        try:
            self.conan_cmd = conan_cmd
            print("Conan cmd is:", self.conan_cmd)
            subprocess.run(self.conan_cmd, check = True)
        except subprocess.CalledProcessError as e:
            print ('Conan command failed', e.returncode)
            raise

    def main(self):
        if self.get_if_branch_build() == 1:
            print("Building from branch")
            l_repo = Repo(path=os.getcwd())
            l_branch = l_repo.active_branch.name
            print("Branch is : ", l_branch)
            l_branch = l_branch.replace("/","")
            channel = l_branch.lower()
        else:
            print("Building from tag")
            channel = "release"
        conan_cmd = "conan create . " + "--user autosar --channel " + channel
        self.execute_cmnd(conan_cmd)

if __name__ == '__main__':
    pkgBuild = PackageBuilder()
    pkgBuild.main()
