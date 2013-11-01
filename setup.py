from setuptools import setup

setup(
    name = 'pkgboot',
    version = '0.0.1',
    author = 'Matt Fichman',
    author_email = 'matt.fichman@gmail.com',
    description = ('C++ workspace setup with SCons'),
    license = 'MIT',
    keywords = ('installer', 'windows', 'workspace'),
    url = 'http://github.com/mfichman/pkgboot',
    packages = ['pkgboot'],
    install_requires = ['scons'],
    entry_points = {
        'console_scripts': (
            'pkgboot = pkgboot.main:main'
        )
    }
)
    
    
    
    
