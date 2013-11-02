
import pkgboot
import argparse
import os
import inspect

template = """
import pkgboot

class {name}(pkgboot.Package):
    defines = {{}}
    includes = []
    libs = []
    major_version = '0'
    minor_version = '0'
    patch = '0'

{name}()
"""


def main():
    parser = argparse.ArgumentParser(prog='winbrew', description='Package installer for Windows')
    parser.add_argument('name', type=str, help='name of the package to create')
    args = parser.parse_args()
    if not os.path.exists('SConstruct'):
        fd = open('SConstruct', 'w')
        fd.write(template.format(name=args.name))
        fd.close()

    fd = open('pkgboot.py', 'w')
    fd.write(inspect.getsource(pkgboot.package))
    fd.close()

if __name__ == '__main__':
    main()
