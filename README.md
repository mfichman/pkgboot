pkgboot
=======

Sets up a full work environment for a C++ project that's built with SCons.  To use pkgboot:

* Run `pkgboot NAME` to create an SConstruct file for your project
* Edit SConstruct to add library dependencies, etc. to the generated file
* Create a precompiled header file named 'Common.hpp'

The generated project layout is:

    root/
        SConstruct
        src/
        include/
        bin/
        test/
        build/

The `include` directory is optional.  Place your source in `src`.
