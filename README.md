pkgboot
=======

Sets up a full work environment for a C++ project that's built with SCons.  To use pkgboot:

1. Run `pkgboot NAME` to create an SConstruct file for your project
1. Edit SConstruct to add library dependencies, etc. to the generated file
1. Create a precompiled header file named 'Common.hpp'

The generated project layout is:

    root/
        SConstruct
        src/
        include/
        bin/
        test/
        build/

The `include` directory is optional.  Place your source in `src`.  Tests are
stand-alone programs (one per .cpp file) that are built into executables that
are installed under `bin/test/NAME`
