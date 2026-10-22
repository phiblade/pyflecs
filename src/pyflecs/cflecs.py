"""Generated from vendored Flecs 4.1.0 by tools/generate_bindings.py.
Do not edit by hand; configuration: FLECS_NDEBUG, 64-bit Unix.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types


class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):
    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value


# End preamble

_libs = {}
_libdirs = []

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(
                        os.path.join(os.path.dirname(__file__), fmt % libname)
                    )

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
from ._native import library_path as _library_path

_libs["flecs"] = load_library(_library_path())

# 1 libraries
# End libraries

# No modules

NULL = None  # <built-in>

__darwin_intptr_t = c_long  # /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/_types.h: 40

# /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_string.h: 75
for _lib in _libs.values():
    if not _lib.has("memcmp", "cdecl"):
        continue
    memcmp = _lib.get("memcmp", "cdecl")
    memcmp.argtypes = [POINTER(None), POINTER(None), c_size_t]
    memcmp.restype = c_int
    break

# /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_string.h: 77
for _lib in _libs.values():
    if not _lib.has("memcpy", "cdecl"):
        continue
    memcpy = _lib.get("memcpy", "cdecl")
    memcpy.argtypes = [POINTER(None), POINTER(None), c_size_t]
    memcpy.restype = POINTER(c_ubyte)
    memcpy.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_string.h: 80
for _lib in _libs.values():
    if not _lib.has("memmove", "cdecl"):
        continue
    memmove = _lib.get("memmove", "cdecl")
    memmove.argtypes = [POINTER(None), POINTER(None), c_size_t]
    memmove.restype = POINTER(c_ubyte)
    memmove.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_string.h: 83
for _lib in _libs.values():
    if not _lib.has("memset", "cdecl"):
        continue
    memset = _lib.get("memset", "cdecl")
    memset.argtypes = [POINTER(None), c_int, c_size_t]
    memset.restype = POINTER(c_ubyte)
    memset.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_string.h: 85
for _lib in _libs.values():
    if not _lib.has("strcat", "cdecl"):
        continue
    strcat = _lib.get("strcat", "cdecl")
    strcat.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        strcat.restype = ReturnString
    else:
        strcat.restype = String
        strcat.errcheck = ReturnString
    break

# /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_string.h: 89
for _lib in _libs.values():
    if not _lib.has("strcmp", "cdecl"):
        continue
    strcmp = _lib.get("strcmp", "cdecl")
    strcmp.argtypes = [String, String]
    strcmp.restype = c_int
    break

# /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_string.h: 91
for _lib in _libs.values():
    if not _lib.has("strcpy", "cdecl"):
        continue
    strcpy = _lib.get("strcpy", "cdecl")
    strcpy.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        strcpy.restype = ReturnString
    else:
        strcpy.restype = String
        strcpy.errcheck = ReturnString
    break

# /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_string.h: 96
for _lib in _libs.values():
    if not _lib.has("strlen", "cdecl"):
        continue
    strlen = _lib.get("strlen", "cdecl")
    strlen.argtypes = [String]
    strlen.restype = c_size_t
    break

# /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_string.h: 101
for _lib in _libs.values():
    if not _lib.has("strncmp", "cdecl"):
        continue
    strncmp = _lib.get("strncmp", "cdecl")
    strncmp.argtypes = [String, String, c_size_t]
    strncmp.restype = c_int
    break

# /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_string.h: 103
for _lib in _libs.values():
    if not _lib.has("strncpy", "cdecl"):
        continue
    strncpy = _lib.get("strncpy", "cdecl")
    strncpy.argtypes = [String, String, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        strncpy.restype = ReturnString
    else:
        strncpy.restype = String
        strncpy.errcheck = ReturnString
    break

intptr_t = __darwin_intptr_t  # /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_intptr_t.h: 32

uintptr_t = c_ulong  # /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_uintptr_t.h: 34

uint8_t = c_ubyte  # /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_types/_uint8_t.h: 31

uint16_t = c_ushort  # /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_types/_uint16_t.h: 31

uint32_t = c_uint  # /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_types/_uint32_t.h: 31

uint64_t = c_ulonglong  # /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_types/_uint64_t.h: 31

# /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/alloca.h: 35
for _lib in _libs.values():
    if not _lib.has("alloca", "cdecl"):
        continue
    alloca = _lib.get("alloca", "cdecl")
    alloca.argtypes = [c_size_t]
    alloca.restype = POINTER(c_ubyte)
    alloca.errcheck = lambda v, *a: cast(v, c_void_p)
    break

ecs_flags8_t = uint8_t  # vendor/flecs/flecs.h: 875

ecs_flags16_t = uint16_t  # vendor/flecs/flecs.h: 876

ecs_flags32_t = uint32_t  # vendor/flecs/flecs.h: 877

ecs_flags64_t = uint64_t  # vendor/flecs/flecs.h: 878

ecs_size_t = c_int32  # vendor/flecs/flecs.h: 895


# vendor/flecs/flecs.h: 2004
class struct_ecs_allocator_t(Structure):
    pass


ecs_allocator_t = struct_ecs_allocator_t  # vendor/flecs/flecs.h: 898


# vendor/flecs/flecs.h: 1162
class struct_ecs_vec_t(Structure):
    pass


struct_ecs_vec_t.__slots__ = [
    "array",
    "count",
    "size",
]
struct_ecs_vec_t._fields_ = [
    ("array", POINTER(None)),
    ("count", c_int32),
    ("size", c_int32),
]

ecs_vec_t = struct_ecs_vec_t  # vendor/flecs/flecs.h: 1162

# vendor/flecs/flecs.h: 1165
for _lib in _libs.values():
    if not _lib.has("ecs_vec_init", "cdecl"):
        continue
    ecs_vec_init = _lib.get("ecs_vec_init", "cdecl")
    ecs_vec_init.argtypes = [
        POINTER(struct_ecs_allocator_t),
        POINTER(ecs_vec_t),
        ecs_size_t,
        c_int32,
    ]
    ecs_vec_init.restype = None
    break

# vendor/flecs/flecs.h: 1172
for _lib in _libs.values():
    if not _lib.has("ecs_vec_init_w_dbg_info", "cdecl"):
        continue
    ecs_vec_init_w_dbg_info = _lib.get("ecs_vec_init_w_dbg_info", "cdecl")
    ecs_vec_init_w_dbg_info.argtypes = [
        POINTER(struct_ecs_allocator_t),
        POINTER(ecs_vec_t),
        ecs_size_t,
        c_int32,
        String,
    ]
    ecs_vec_init_w_dbg_info.restype = None
    break

# vendor/flecs/flecs.h: 1183
for _lib in _libs.values():
    if not _lib.has("ecs_vec_init_if", "cdecl"):
        continue
    ecs_vec_init_if = _lib.get("ecs_vec_init_if", "cdecl")
    ecs_vec_init_if.argtypes = [POINTER(ecs_vec_t), ecs_size_t]
    ecs_vec_init_if.restype = None
    break

# vendor/flecs/flecs.h: 1191
for _lib in _libs.values():
    if not _lib.has("ecs_vec_fini", "cdecl"):
        continue
    ecs_vec_fini = _lib.get("ecs_vec_fini", "cdecl")
    ecs_vec_fini.argtypes = [
        POINTER(struct_ecs_allocator_t),
        POINTER(ecs_vec_t),
        ecs_size_t,
    ]
    ecs_vec_fini.restype = None
    break

# vendor/flecs/flecs.h: 1200
for _lib in _libs.values():
    if not _lib.has("ecs_vec_reset", "cdecl"):
        continue
    ecs_vec_reset = _lib.get("ecs_vec_reset", "cdecl")
    ecs_vec_reset.argtypes = [
        POINTER(struct_ecs_allocator_t),
        POINTER(ecs_vec_t),
        ecs_size_t,
    ]
    ecs_vec_reset.restype = POINTER(ecs_vec_t)
    break

# vendor/flecs/flecs.h: 1209
for _lib in _libs.values():
    if not _lib.has("ecs_vec_clear", "cdecl"):
        continue
    ecs_vec_clear = _lib.get("ecs_vec_clear", "cdecl")
    ecs_vec_clear.argtypes = [POINTER(ecs_vec_t)]
    ecs_vec_clear.restype = None
    break

# vendor/flecs/flecs.h: 1213
for _lib in _libs.values():
    if not _lib.has("ecs_vec_append", "cdecl"):
        continue
    ecs_vec_append = _lib.get("ecs_vec_append", "cdecl")
    ecs_vec_append.argtypes = [
        POINTER(struct_ecs_allocator_t),
        POINTER(ecs_vec_t),
        ecs_size_t,
    ]
    ecs_vec_append.restype = POINTER(c_ubyte)
    ecs_vec_append.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1222
for _lib in _libs.values():
    if not _lib.has("ecs_vec_remove", "cdecl"):
        continue
    ecs_vec_remove = _lib.get("ecs_vec_remove", "cdecl")
    ecs_vec_remove.argtypes = [POINTER(ecs_vec_t), ecs_size_t, c_int32]
    ecs_vec_remove.restype = None
    break

# vendor/flecs/flecs.h: 1231
for _lib in _libs.values():
    if not _lib.has("ecs_vec_remove_ordered", "cdecl"):
        continue
    ecs_vec_remove_ordered = _lib.get("ecs_vec_remove_ordered", "cdecl")
    ecs_vec_remove_ordered.argtypes = [POINTER(ecs_vec_t), ecs_size_t, c_int32]
    ecs_vec_remove_ordered.restype = None
    break

# vendor/flecs/flecs.h: 1240
for _lib in _libs.values():
    if not _lib.has("ecs_vec_remove_last", "cdecl"):
        continue
    ecs_vec_remove_last = _lib.get("ecs_vec_remove_last", "cdecl")
    ecs_vec_remove_last.argtypes = [POINTER(ecs_vec_t)]
    ecs_vec_remove_last.restype = None
    break

# vendor/flecs/flecs.h: 1244
for _lib in _libs.values():
    if not _lib.has("ecs_vec_copy", "cdecl"):
        continue
    ecs_vec_copy = _lib.get("ecs_vec_copy", "cdecl")
    ecs_vec_copy.argtypes = [
        POINTER(struct_ecs_allocator_t),
        POINTER(ecs_vec_t),
        ecs_size_t,
    ]
    ecs_vec_copy.restype = ecs_vec_t
    break

# vendor/flecs/flecs.h: 1253
for _lib in _libs.values():
    if not _lib.has("ecs_vec_copy_shrink", "cdecl"):
        continue
    ecs_vec_copy_shrink = _lib.get("ecs_vec_copy_shrink", "cdecl")
    ecs_vec_copy_shrink.argtypes = [
        POINTER(struct_ecs_allocator_t),
        POINTER(ecs_vec_t),
        ecs_size_t,
    ]
    ecs_vec_copy_shrink.restype = ecs_vec_t
    break

# vendor/flecs/flecs.h: 1262
for _lib in _libs.values():
    if not _lib.has("ecs_vec_reclaim", "cdecl"):
        continue
    ecs_vec_reclaim = _lib.get("ecs_vec_reclaim", "cdecl")
    ecs_vec_reclaim.argtypes = [
        POINTER(struct_ecs_allocator_t),
        POINTER(ecs_vec_t),
        ecs_size_t,
    ]
    ecs_vec_reclaim.restype = None
    break

# vendor/flecs/flecs.h: 1271
for _lib in _libs.values():
    if not _lib.has("ecs_vec_set_size", "cdecl"):
        continue
    ecs_vec_set_size = _lib.get("ecs_vec_set_size", "cdecl")
    ecs_vec_set_size.argtypes = [
        POINTER(struct_ecs_allocator_t),
        POINTER(ecs_vec_t),
        ecs_size_t,
        c_int32,
    ]
    ecs_vec_set_size.restype = None
    break

# vendor/flecs/flecs.h: 1281
for _lib in _libs.values():
    if not _lib.has("ecs_vec_set_min_size", "cdecl"):
        continue
    ecs_vec_set_min_size = _lib.get("ecs_vec_set_min_size", "cdecl")
    ecs_vec_set_min_size.argtypes = [
        POINTER(struct_ecs_allocator_t),
        POINTER(ecs_vec_t),
        ecs_size_t,
        c_int32,
    ]
    ecs_vec_set_min_size.restype = None
    break

# vendor/flecs/flecs.h: 1291
for _lib in _libs.values():
    if not _lib.has("ecs_vec_set_min_count", "cdecl"):
        continue
    ecs_vec_set_min_count = _lib.get("ecs_vec_set_min_count", "cdecl")
    ecs_vec_set_min_count.argtypes = [
        POINTER(struct_ecs_allocator_t),
        POINTER(ecs_vec_t),
        ecs_size_t,
        c_int32,
    ]
    ecs_vec_set_min_count.restype = None
    break

# vendor/flecs/flecs.h: 1301
for _lib in _libs.values():
    if not _lib.has("ecs_vec_set_min_count_zeromem", "cdecl"):
        continue
    ecs_vec_set_min_count_zeromem = _lib.get("ecs_vec_set_min_count_zeromem", "cdecl")
    ecs_vec_set_min_count_zeromem.argtypes = [
        POINTER(struct_ecs_allocator_t),
        POINTER(ecs_vec_t),
        ecs_size_t,
        c_int32,
    ]
    ecs_vec_set_min_count_zeromem.restype = None
    break

# vendor/flecs/flecs.h: 1311
for _lib in _libs.values():
    if not _lib.has("ecs_vec_set_count", "cdecl"):
        continue
    ecs_vec_set_count = _lib.get("ecs_vec_set_count", "cdecl")
    ecs_vec_set_count.argtypes = [
        POINTER(struct_ecs_allocator_t),
        POINTER(ecs_vec_t),
        ecs_size_t,
        c_int32,
    ]
    ecs_vec_set_count.restype = None
    break

# vendor/flecs/flecs.h: 1321
for _lib in _libs.values():
    if not _lib.has("ecs_vec_grow", "cdecl"):
        continue
    ecs_vec_grow = _lib.get("ecs_vec_grow", "cdecl")
    ecs_vec_grow.argtypes = [
        POINTER(struct_ecs_allocator_t),
        POINTER(ecs_vec_t),
        ecs_size_t,
        c_int32,
    ]
    ecs_vec_grow.restype = POINTER(c_ubyte)
    ecs_vec_grow.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1331
for _lib in _libs.values():
    if not _lib.has("ecs_vec_count", "cdecl"):
        continue
    ecs_vec_count = _lib.get("ecs_vec_count", "cdecl")
    ecs_vec_count.argtypes = [POINTER(ecs_vec_t)]
    ecs_vec_count.restype = c_int32
    break

# vendor/flecs/flecs.h: 1335
for _lib in _libs.values():
    if not _lib.has("ecs_vec_size", "cdecl"):
        continue
    ecs_vec_size = _lib.get("ecs_vec_size", "cdecl")
    ecs_vec_size.argtypes = [POINTER(ecs_vec_t)]
    ecs_vec_size.restype = c_int32
    break

# vendor/flecs/flecs.h: 1339
for _lib in _libs.values():
    if not _lib.has("ecs_vec_get", "cdecl"):
        continue
    ecs_vec_get = _lib.get("ecs_vec_get", "cdecl")
    ecs_vec_get.argtypes = [POINTER(ecs_vec_t), ecs_size_t, c_int32]
    ecs_vec_get.restype = POINTER(c_ubyte)
    ecs_vec_get.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1348
for _lib in _libs.values():
    if not _lib.has("ecs_vec_first", "cdecl"):
        continue
    ecs_vec_first = _lib.get("ecs_vec_first", "cdecl")
    ecs_vec_first.argtypes = [POINTER(ecs_vec_t)]
    ecs_vec_first.restype = POINTER(c_ubyte)
    ecs_vec_first.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1355
for _lib in _libs.values():
    if not _lib.has("ecs_vec_last", "cdecl"):
        continue
    ecs_vec_last = _lib.get("ecs_vec_last", "cdecl")
    ecs_vec_last.argtypes = [POINTER(ecs_vec_t), ecs_size_t]
    ecs_vec_last.restype = POINTER(c_ubyte)
    ecs_vec_last.errcheck = lambda v, *a: cast(v, c_void_p)
    break


# vendor/flecs/flecs.h: 1611
class struct_ecs_block_allocator_t(Structure):
    pass


# vendor/flecs/flecs.h: 1402
class struct_ecs_sparse_t(Structure):
    pass


struct_ecs_sparse_t.__slots__ = [
    "dense",
    "pages",
    "size",
    "count",
    "max_id",
    "allocator",
    "page_allocator",
]
struct_ecs_sparse_t._fields_ = [
    ("dense", ecs_vec_t),
    ("pages", ecs_vec_t),
    ("size", ecs_size_t),
    ("count", c_int32),
    ("max_id", uint64_t),
    ("allocator", POINTER(struct_ecs_allocator_t)),
    ("page_allocator", POINTER(struct_ecs_block_allocator_t)),
]

ecs_sparse_t = struct_ecs_sparse_t  # vendor/flecs/flecs.h: 1402

# vendor/flecs/flecs.h: 1406
for _lib in _libs.values():
    if not _lib.has("flecs_sparse_init", "cdecl"):
        continue
    flecs_sparse_init = _lib.get("flecs_sparse_init", "cdecl")
    flecs_sparse_init.argtypes = [
        POINTER(ecs_sparse_t),
        POINTER(struct_ecs_allocator_t),
        POINTER(struct_ecs_block_allocator_t),
        ecs_size_t,
    ]
    flecs_sparse_init.restype = None
    break

# vendor/flecs/flecs.h: 1416
for _lib in _libs.values():
    if not _lib.has("flecs_sparse_fini", "cdecl"):
        continue
    flecs_sparse_fini = _lib.get("flecs_sparse_fini", "cdecl")
    flecs_sparse_fini.argtypes = [POINTER(ecs_sparse_t)]
    flecs_sparse_fini.restype = None
    break

# vendor/flecs/flecs.h: 1421
for _lib in _libs.values():
    if not _lib.has("flecs_sparse_clear", "cdecl"):
        continue
    flecs_sparse_clear = _lib.get("flecs_sparse_clear", "cdecl")
    flecs_sparse_clear.argtypes = [POINTER(ecs_sparse_t)]
    flecs_sparse_clear.restype = None
    break

# vendor/flecs/flecs.h: 1426
for _lib in _libs.values():
    if not _lib.has("flecs_sparse_add", "cdecl"):
        continue
    flecs_sparse_add = _lib.get("flecs_sparse_add", "cdecl")
    flecs_sparse_add.argtypes = [POINTER(ecs_sparse_t), ecs_size_t]
    flecs_sparse_add.restype = POINTER(c_ubyte)
    flecs_sparse_add.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1435
for _lib in _libs.values():
    if not _lib.has("flecs_sparse_last_id", "cdecl"):
        continue
    flecs_sparse_last_id = _lib.get("flecs_sparse_last_id", "cdecl")
    flecs_sparse_last_id.argtypes = [POINTER(ecs_sparse_t)]
    flecs_sparse_last_id.restype = uint64_t
    break

# vendor/flecs/flecs.h: 1440
for _lib in _libs.values():
    if not _lib.has("flecs_sparse_new_id", "cdecl"):
        continue
    flecs_sparse_new_id = _lib.get("flecs_sparse_new_id", "cdecl")
    flecs_sparse_new_id.argtypes = [POINTER(ecs_sparse_t)]
    flecs_sparse_new_id.restype = uint64_t
    break

# vendor/flecs/flecs.h: 1445
for _lib in _libs.values():
    if not _lib.has("flecs_sparse_remove", "cdecl"):
        continue
    flecs_sparse_remove = _lib.get("flecs_sparse_remove", "cdecl")
    flecs_sparse_remove.argtypes = [POINTER(ecs_sparse_t), ecs_size_t, uint64_t]
    flecs_sparse_remove.restype = c_bool
    break

# vendor/flecs/flecs.h: 1454
for _lib in _libs.values():
    if not _lib.has("flecs_sparse_remove_w_gen", "cdecl"):
        continue
    flecs_sparse_remove_w_gen = _lib.get("flecs_sparse_remove_w_gen", "cdecl")
    flecs_sparse_remove_w_gen.argtypes = [POINTER(ecs_sparse_t), ecs_size_t, uint64_t]
    flecs_sparse_remove_w_gen.restype = c_bool
    break

# vendor/flecs/flecs.h: 1464
for _lib in _libs.values():
    if not _lib.has("flecs_sparse_is_alive", "cdecl"):
        continue
    flecs_sparse_is_alive = _lib.get("flecs_sparse_is_alive", "cdecl")
    flecs_sparse_is_alive.argtypes = [POINTER(ecs_sparse_t), uint64_t]
    flecs_sparse_is_alive.restype = c_bool
    break

# vendor/flecs/flecs.h: 1471
for _lib in _libs.values():
    if not _lib.has("flecs_sparse_get_dense", "cdecl"):
        continue
    flecs_sparse_get_dense = _lib.get("flecs_sparse_get_dense", "cdecl")
    flecs_sparse_get_dense.argtypes = [POINTER(ecs_sparse_t), ecs_size_t, c_int32]
    flecs_sparse_get_dense.restype = POINTER(c_ubyte)
    flecs_sparse_get_dense.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1481
for _lib in _libs.values():
    if not _lib.has("flecs_sparse_count", "cdecl"):
        continue
    flecs_sparse_count = _lib.get("flecs_sparse_count", "cdecl")
    flecs_sparse_count.argtypes = [POINTER(ecs_sparse_t)]
    flecs_sparse_count.restype = c_int32
    break

# vendor/flecs/flecs.h: 1485
for _lib in _libs.values():
    if not _lib.has("flecs_sparse_has", "cdecl"):
        continue
    flecs_sparse_has = _lib.get("flecs_sparse_has", "cdecl")
    flecs_sparse_has.argtypes = [POINTER(ecs_sparse_t), uint64_t]
    flecs_sparse_has.restype = c_bool
    break

# vendor/flecs/flecs.h: 1491
for _lib in _libs.values():
    if not _lib.has("flecs_sparse_get", "cdecl"):
        continue
    flecs_sparse_get = _lib.get("flecs_sparse_get", "cdecl")
    flecs_sparse_get.argtypes = [POINTER(ecs_sparse_t), ecs_size_t, uint64_t]
    flecs_sparse_get.restype = POINTER(c_ubyte)
    flecs_sparse_get.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1501
for _lib in _libs.values():
    if not _lib.has("flecs_sparse_insert", "cdecl"):
        continue
    flecs_sparse_insert = _lib.get("flecs_sparse_insert", "cdecl")
    flecs_sparse_insert.argtypes = [POINTER(ecs_sparse_t), ecs_size_t, uint64_t]
    flecs_sparse_insert.restype = POINTER(c_ubyte)
    flecs_sparse_insert.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1511
for _lib in _libs.values():
    if not _lib.has("flecs_sparse_ensure", "cdecl"):
        continue
    flecs_sparse_ensure = _lib.get("flecs_sparse_ensure", "cdecl")
    flecs_sparse_ensure.argtypes = [
        POINTER(ecs_sparse_t),
        ecs_size_t,
        uint64_t,
        POINTER(c_bool),
    ]
    flecs_sparse_ensure.restype = POINTER(c_ubyte)
    flecs_sparse_ensure.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1522
for _lib in _libs.values():
    if not _lib.has("flecs_sparse_ensure_fast", "cdecl"):
        continue
    flecs_sparse_ensure_fast = _lib.get("flecs_sparse_ensure_fast", "cdecl")
    flecs_sparse_ensure_fast.argtypes = [POINTER(ecs_sparse_t), ecs_size_t, uint64_t]
    flecs_sparse_ensure_fast.restype = POINTER(c_ubyte)
    flecs_sparse_ensure_fast.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1532
for _lib in _libs.values():
    if not _lib.has("flecs_sparse_ids", "cdecl"):
        continue
    flecs_sparse_ids = _lib.get("flecs_sparse_ids", "cdecl")
    flecs_sparse_ids.argtypes = [POINTER(ecs_sparse_t)]
    flecs_sparse_ids.restype = POINTER(uint64_t)
    break

# vendor/flecs/flecs.h: 1536
for _lib in _libs.values():
    if not _lib.has("flecs_sparse_shrink", "cdecl"):
        continue
    flecs_sparse_shrink = _lib.get("flecs_sparse_shrink", "cdecl")
    flecs_sparse_shrink.argtypes = [POINTER(ecs_sparse_t)]
    flecs_sparse_shrink.restype = None
    break

# vendor/flecs/flecs.h: 1544
for _lib in _libs.values():
    if not _lib.has("ecs_sparse_init", "cdecl"):
        continue
    ecs_sparse_init = _lib.get("ecs_sparse_init", "cdecl")
    ecs_sparse_init.argtypes = [POINTER(ecs_sparse_t), ecs_size_t]
    ecs_sparse_init.restype = None
    break

# vendor/flecs/flecs.h: 1552
for _lib in _libs.values():
    if not _lib.has("ecs_sparse_add", "cdecl"):
        continue
    ecs_sparse_add = _lib.get("ecs_sparse_add", "cdecl")
    ecs_sparse_add.argtypes = [POINTER(ecs_sparse_t), ecs_size_t]
    ecs_sparse_add.restype = POINTER(c_ubyte)
    ecs_sparse_add.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1560
for _lib in _libs.values():
    if not _lib.has("ecs_sparse_last_id", "cdecl"):
        continue
    ecs_sparse_last_id = _lib.get("ecs_sparse_last_id", "cdecl")
    ecs_sparse_last_id.argtypes = [POINTER(ecs_sparse_t)]
    ecs_sparse_last_id.restype = uint64_t
    break

# vendor/flecs/flecs.h: 1564
for _lib in _libs.values():
    if not _lib.has("ecs_sparse_count", "cdecl"):
        continue
    ecs_sparse_count = _lib.get("ecs_sparse_count", "cdecl")
    ecs_sparse_count.argtypes = [POINTER(ecs_sparse_t)]
    ecs_sparse_count.restype = c_int32
    break

# vendor/flecs/flecs.h: 1568
for _lib in _libs.values():
    if not _lib.has("ecs_sparse_get_dense", "cdecl"):
        continue
    ecs_sparse_get_dense = _lib.get("ecs_sparse_get_dense", "cdecl")
    ecs_sparse_get_dense.argtypes = [POINTER(ecs_sparse_t), ecs_size_t, c_int32]
    ecs_sparse_get_dense.restype = POINTER(c_ubyte)
    ecs_sparse_get_dense.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1577
for _lib in _libs.values():
    if not _lib.has("ecs_sparse_get", "cdecl"):
        continue
    ecs_sparse_get = _lib.get("ecs_sparse_get", "cdecl")
    ecs_sparse_get.argtypes = [POINTER(ecs_sparse_t), ecs_size_t, uint64_t]
    ecs_sparse_get.restype = POINTER(c_ubyte)
    ecs_sparse_get.errcheck = lambda v, *a: cast(v, c_void_p)
    break


# vendor/flecs/flecs.h: 1826
class struct_ecs_map_t(Structure):
    pass


ecs_map_t = struct_ecs_map_t  # vendor/flecs/flecs.h: 1600


# vendor/flecs/flecs.h: 1602
class struct_ecs_block_allocator_block_t(Structure):
    pass


struct_ecs_block_allocator_block_t.__slots__ = [
    "memory",
    "next",
]
struct_ecs_block_allocator_block_t._fields_ = [
    ("memory", POINTER(None)),
    ("next", POINTER(struct_ecs_block_allocator_block_t)),
]

ecs_block_allocator_block_t = (
    struct_ecs_block_allocator_block_t  # vendor/flecs/flecs.h: 1605
)


# vendor/flecs/flecs.h: 1607
class struct_ecs_block_allocator_chunk_header_t(Structure):
    pass


struct_ecs_block_allocator_chunk_header_t.__slots__ = [
    "next",
]
struct_ecs_block_allocator_chunk_header_t._fields_ = [
    ("next", POINTER(struct_ecs_block_allocator_chunk_header_t)),
]

ecs_block_allocator_chunk_header_t = (
    struct_ecs_block_allocator_chunk_header_t  # vendor/flecs/flecs.h: 1609
)

struct_ecs_block_allocator_t.__slots__ = [
    "data_size",
    "chunk_size",
    "chunks_per_block",
    "block_size",
    "head",
    "block_head",
]
struct_ecs_block_allocator_t._fields_ = [
    ("data_size", c_int32),
    ("chunk_size", c_int32),
    ("chunks_per_block", c_int32),
    ("block_size", c_int32),
    ("head", POINTER(ecs_block_allocator_chunk_header_t)),
    ("block_head", POINTER(ecs_block_allocator_block_t)),
]

ecs_block_allocator_t = struct_ecs_block_allocator_t  # vendor/flecs/flecs.h: 1624

# vendor/flecs/flecs.h: 1627
for _lib in _libs.values():
    if not _lib.has("flecs_ballocator_init", "cdecl"):
        continue
    flecs_ballocator_init = _lib.get("flecs_ballocator_init", "cdecl")
    flecs_ballocator_init.argtypes = [POINTER(ecs_block_allocator_t), ecs_size_t]
    flecs_ballocator_init.restype = None
    break

# vendor/flecs/flecs.h: 1637
for _lib in _libs.values():
    if not _lib.has("flecs_ballocator_new", "cdecl"):
        continue
    flecs_ballocator_new = _lib.get("flecs_ballocator_new", "cdecl")
    flecs_ballocator_new.argtypes = [ecs_size_t]
    flecs_ballocator_new.restype = POINTER(ecs_block_allocator_t)
    break

# vendor/flecs/flecs.h: 1646
for _lib in _libs.values():
    if not _lib.has("flecs_ballocator_fini", "cdecl"):
        continue
    flecs_ballocator_fini = _lib.get("flecs_ballocator_fini", "cdecl")
    flecs_ballocator_fini.argtypes = [POINTER(ecs_block_allocator_t)]
    flecs_ballocator_fini.restype = None
    break

# vendor/flecs/flecs.h: 1650
for _lib in _libs.values():
    if not _lib.has("flecs_ballocator_free", "cdecl"):
        continue
    flecs_ballocator_free = _lib.get("flecs_ballocator_free", "cdecl")
    flecs_ballocator_free.argtypes = [POINTER(ecs_block_allocator_t)]
    flecs_ballocator_free.restype = None
    break

# vendor/flecs/flecs.h: 1654
for _lib in _libs.values():
    if not _lib.has("flecs_balloc", "cdecl"):
        continue
    flecs_balloc = _lib.get("flecs_balloc", "cdecl")
    flecs_balloc.argtypes = [POINTER(ecs_block_allocator_t)]
    flecs_balloc.restype = POINTER(c_ubyte)
    flecs_balloc.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1658
for _lib in _libs.values():
    if not _lib.has("flecs_balloc_w_dbg_info", "cdecl"):
        continue
    flecs_balloc_w_dbg_info = _lib.get("flecs_balloc_w_dbg_info", "cdecl")
    flecs_balloc_w_dbg_info.argtypes = [POINTER(ecs_block_allocator_t), String]
    flecs_balloc_w_dbg_info.restype = POINTER(c_ubyte)
    flecs_balloc_w_dbg_info.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1663
for _lib in _libs.values():
    if not _lib.has("flecs_bcalloc", "cdecl"):
        continue
    flecs_bcalloc = _lib.get("flecs_bcalloc", "cdecl")
    flecs_bcalloc.argtypes = [POINTER(ecs_block_allocator_t)]
    flecs_bcalloc.restype = POINTER(c_ubyte)
    flecs_bcalloc.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1667
for _lib in _libs.values():
    if not _lib.has("flecs_bcalloc_w_dbg_info", "cdecl"):
        continue
    flecs_bcalloc_w_dbg_info = _lib.get("flecs_bcalloc_w_dbg_info", "cdecl")
    flecs_bcalloc_w_dbg_info.argtypes = [POINTER(ecs_block_allocator_t), String]
    flecs_bcalloc_w_dbg_info.restype = POINTER(c_ubyte)
    flecs_bcalloc_w_dbg_info.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1672
for _lib in _libs.values():
    if not _lib.has("flecs_bfree", "cdecl"):
        continue
    flecs_bfree = _lib.get("flecs_bfree", "cdecl")
    flecs_bfree.argtypes = [POINTER(ecs_block_allocator_t), POINTER(None)]
    flecs_bfree.restype = None
    break

# vendor/flecs/flecs.h: 1677
for _lib in _libs.values():
    if not _lib.has("flecs_bfree_w_dbg_info", "cdecl"):
        continue
    flecs_bfree_w_dbg_info = _lib.get("flecs_bfree_w_dbg_info", "cdecl")
    flecs_bfree_w_dbg_info.argtypes = [
        POINTER(ecs_block_allocator_t),
        POINTER(None),
        String,
    ]
    flecs_bfree_w_dbg_info.restype = None
    break

# vendor/flecs/flecs.h: 1683
for _lib in _libs.values():
    if not _lib.has("flecs_brealloc", "cdecl"):
        continue
    flecs_brealloc = _lib.get("flecs_brealloc", "cdecl")
    flecs_brealloc.argtypes = [
        POINTER(ecs_block_allocator_t),
        POINTER(ecs_block_allocator_t),
        POINTER(None),
    ]
    flecs_brealloc.restype = POINTER(c_ubyte)
    flecs_brealloc.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1689
for _lib in _libs.values():
    if not _lib.has("flecs_brealloc_w_dbg_info", "cdecl"):
        continue
    flecs_brealloc_w_dbg_info = _lib.get("flecs_brealloc_w_dbg_info", "cdecl")
    flecs_brealloc_w_dbg_info.argtypes = [
        POINTER(ecs_block_allocator_t),
        POINTER(ecs_block_allocator_t),
        POINTER(None),
        String,
    ]
    flecs_brealloc_w_dbg_info.restype = POINTER(c_ubyte)
    flecs_brealloc_w_dbg_info.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1696
for _lib in _libs.values():
    if not _lib.has("flecs_bdup", "cdecl"):
        continue
    flecs_bdup = _lib.get("flecs_bdup", "cdecl")
    flecs_bdup.argtypes = [POINTER(ecs_block_allocator_t), POINTER(None)]
    flecs_bdup.restype = POINTER(c_ubyte)
    flecs_bdup.errcheck = lambda v, *a: cast(v, c_void_p)
    break


# vendor/flecs/flecs.h: 1712
class struct_ecs_stack_page_t(Structure):
    pass


struct_ecs_stack_page_t.__slots__ = [
    "data",
    "next",
    "sp",
    "id",
]
struct_ecs_stack_page_t._fields_ = [
    ("data", POINTER(None)),
    ("next", POINTER(struct_ecs_stack_page_t)),
    ("sp", c_int16),
    ("id", uint32_t),
]

ecs_stack_page_t = struct_ecs_stack_page_t  # vendor/flecs/flecs.h: 1717


# vendor/flecs/flecs.h: 1719
class struct_ecs_stack_cursor_t(Structure):
    pass


struct_ecs_stack_cursor_t.__slots__ = [
    "prev",
    "page",
    "sp",
    "is_free",
]
struct_ecs_stack_cursor_t._fields_ = [
    ("prev", POINTER(struct_ecs_stack_cursor_t)),
    ("page", POINTER(struct_ecs_stack_page_t)),
    ("sp", c_int16),
    ("is_free", c_bool),
]

ecs_stack_cursor_t = struct_ecs_stack_cursor_t  # vendor/flecs/flecs.h: 1727


# vendor/flecs/flecs.h: 1736
class struct_ecs_stack_t(Structure):
    pass


struct_ecs_stack_t.__slots__ = [
    "first",
    "tail_page",
    "tail_cursor",
]
struct_ecs_stack_t._fields_ = [
    ("first", POINTER(ecs_stack_page_t)),
    ("tail_page", POINTER(ecs_stack_page_t)),
    ("tail_cursor", POINTER(ecs_stack_cursor_t)),
]

ecs_stack_t = struct_ecs_stack_t  # vendor/flecs/flecs.h: 1736

# vendor/flecs/flecs.h: 1742
for _lib in _libs.values():
    if not _lib.has("flecs_stack_init", "cdecl"):
        continue
    flecs_stack_init = _lib.get("flecs_stack_init", "cdecl")
    flecs_stack_init.argtypes = [POINTER(ecs_stack_t)]
    flecs_stack_init.restype = None
    break

# vendor/flecs/flecs.h: 1746
for _lib in _libs.values():
    if not _lib.has("flecs_stack_fini", "cdecl"):
        continue
    flecs_stack_fini = _lib.get("flecs_stack_fini", "cdecl")
    flecs_stack_fini.argtypes = [POINTER(ecs_stack_t)]
    flecs_stack_fini.restype = None
    break

# vendor/flecs/flecs.h: 1750
for _lib in _libs.values():
    if not _lib.has("flecs_stack_alloc", "cdecl"):
        continue
    flecs_stack_alloc = _lib.get("flecs_stack_alloc", "cdecl")
    flecs_stack_alloc.argtypes = [POINTER(ecs_stack_t), ecs_size_t, ecs_size_t]
    flecs_stack_alloc.restype = POINTER(c_ubyte)
    flecs_stack_alloc.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1762
for _lib in _libs.values():
    if not _lib.has("flecs_stack_calloc", "cdecl"):
        continue
    flecs_stack_calloc = _lib.get("flecs_stack_calloc", "cdecl")
    flecs_stack_calloc.argtypes = [POINTER(ecs_stack_t), ecs_size_t, ecs_size_t]
    flecs_stack_calloc.restype = POINTER(c_ubyte)
    flecs_stack_calloc.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1774
for _lib in _libs.values():
    if not _lib.has("flecs_stack_free", "cdecl"):
        continue
    flecs_stack_free = _lib.get("flecs_stack_free", "cdecl")
    flecs_stack_free.argtypes = [POINTER(None), ecs_size_t]
    flecs_stack_free.restype = None
    break

# vendor/flecs/flecs.h: 1784
for _lib in _libs.values():
    if not _lib.has("flecs_stack_reset", "cdecl"):
        continue
    flecs_stack_reset = _lib.get("flecs_stack_reset", "cdecl")
    flecs_stack_reset.argtypes = [POINTER(ecs_stack_t)]
    flecs_stack_reset.restype = None
    break

# vendor/flecs/flecs.h: 1788
for _lib in _libs.values():
    if not _lib.has("flecs_stack_get_cursor", "cdecl"):
        continue
    flecs_stack_get_cursor = _lib.get("flecs_stack_get_cursor", "cdecl")
    flecs_stack_get_cursor.argtypes = [POINTER(ecs_stack_t)]
    flecs_stack_get_cursor.restype = POINTER(ecs_stack_cursor_t)
    break

# vendor/flecs/flecs.h: 1792
for _lib in _libs.values():
    if not _lib.has("flecs_stack_restore_cursor", "cdecl"):
        continue
    flecs_stack_restore_cursor = _lib.get("flecs_stack_restore_cursor", "cdecl")
    flecs_stack_restore_cursor.argtypes = [
        POINTER(ecs_stack_t),
        POINTER(ecs_stack_cursor_t),
    ]
    flecs_stack_restore_cursor.restype = None
    break

ecs_map_data_t = uint64_t  # vendor/flecs/flecs.h: 1811

ecs_map_key_t = ecs_map_data_t  # vendor/flecs/flecs.h: 1812

ecs_map_val_t = ecs_map_data_t  # vendor/flecs/flecs.h: 1813


# vendor/flecs/flecs.h: 1816
class struct_ecs_bucket_entry_t(Structure):
    pass


struct_ecs_bucket_entry_t.__slots__ = [
    "key",
    "value",
    "next",
]
struct_ecs_bucket_entry_t._fields_ = [
    ("key", ecs_map_key_t),
    ("value", ecs_map_val_t),
    ("next", POINTER(struct_ecs_bucket_entry_t)),
]

ecs_bucket_entry_t = struct_ecs_bucket_entry_t  # vendor/flecs/flecs.h: 1820


# vendor/flecs/flecs.h: 1824
class struct_ecs_bucket_t(Structure):
    pass


struct_ecs_bucket_t.__slots__ = [
    "first",
]
struct_ecs_bucket_t._fields_ = [
    ("first", POINTER(ecs_bucket_entry_t)),
]

ecs_bucket_t = struct_ecs_bucket_t  # vendor/flecs/flecs.h: 1824

struct_ecs_map_t.__slots__ = [
    "buckets",
    "bucket_count",
    "count",
    "bucket_shift",
    "allocator",
]
struct_ecs_map_t._fields_ = [
    ("buckets", POINTER(ecs_bucket_t)),
    ("bucket_count", c_int32),
    ("count", c_uint, 26),
    ("bucket_shift", c_uint, 6),
    ("allocator", POINTER(struct_ecs_allocator_t)),
]


# vendor/flecs/flecs.h: 1839
class struct_ecs_map_iter_t(Structure):
    pass


struct_ecs_map_iter_t.__slots__ = [
    "map",
    "bucket",
    "entry",
    "res",
]
struct_ecs_map_iter_t._fields_ = [
    ("map", POINTER(ecs_map_t)),
    ("bucket", POINTER(ecs_bucket_t)),
    ("entry", POINTER(ecs_bucket_entry_t)),
    ("res", POINTER(ecs_map_data_t)),
]

ecs_map_iter_t = struct_ecs_map_iter_t  # vendor/flecs/flecs.h: 1839


# vendor/flecs/flecs.h: 1844
class struct_ecs_map_params_t(Structure):
    pass


struct_ecs_map_params_t.__slots__ = [
    "allocator",
    "entry_allocator",
]
struct_ecs_map_params_t._fields_ = [
    ("allocator", POINTER(struct_ecs_allocator_t)),
    ("entry_allocator", struct_ecs_block_allocator_t),
]

ecs_map_params_t = struct_ecs_map_params_t  # vendor/flecs/flecs.h: 1844

# vendor/flecs/flecs.h: 1855
for _lib in _libs.values():
    if not _lib.has("ecs_map_params_init", "cdecl"):
        continue
    ecs_map_params_init = _lib.get("ecs_map_params_init", "cdecl")
    ecs_map_params_init.argtypes = [
        POINTER(ecs_map_params_t),
        POINTER(struct_ecs_allocator_t),
    ]
    ecs_map_params_init.restype = None
    break

# vendor/flecs/flecs.h: 1860
for _lib in _libs.values():
    if not _lib.has("ecs_map_params_fini", "cdecl"):
        continue
    ecs_map_params_fini = _lib.get("ecs_map_params_fini", "cdecl")
    ecs_map_params_fini.argtypes = [POINTER(ecs_map_params_t)]
    ecs_map_params_fini.restype = None
    break

# vendor/flecs/flecs.h: 1865
for _lib in _libs.values():
    if not _lib.has("ecs_map_init", "cdecl"):
        continue
    ecs_map_init = _lib.get("ecs_map_init", "cdecl")
    ecs_map_init.argtypes = [POINTER(ecs_map_t), POINTER(struct_ecs_allocator_t)]
    ecs_map_init.restype = None
    break

# vendor/flecs/flecs.h: 1871
for _lib in _libs.values():
    if not _lib.has("ecs_map_init_w_params", "cdecl"):
        continue
    ecs_map_init_w_params = _lib.get("ecs_map_init_w_params", "cdecl")
    ecs_map_init_w_params.argtypes = [POINTER(ecs_map_t), POINTER(ecs_map_params_t)]
    ecs_map_init_w_params.restype = None
    break

# vendor/flecs/flecs.h: 1877
for _lib in _libs.values():
    if not _lib.has("ecs_map_init_if", "cdecl"):
        continue
    ecs_map_init_if = _lib.get("ecs_map_init_if", "cdecl")
    ecs_map_init_if.argtypes = [POINTER(ecs_map_t), POINTER(struct_ecs_allocator_t)]
    ecs_map_init_if.restype = None
    break

# vendor/flecs/flecs.h: 1882
for _lib in _libs.values():
    if not _lib.has("ecs_map_init_w_params_if", "cdecl"):
        continue
    ecs_map_init_w_params_if = _lib.get("ecs_map_init_w_params_if", "cdecl")
    ecs_map_init_w_params_if.argtypes = [POINTER(ecs_map_t), POINTER(ecs_map_params_t)]
    ecs_map_init_w_params_if.restype = None
    break

# vendor/flecs/flecs.h: 1888
for _lib in _libs.values():
    if not _lib.has("ecs_map_fini", "cdecl"):
        continue
    ecs_map_fini = _lib.get("ecs_map_fini", "cdecl")
    ecs_map_fini.argtypes = [POINTER(ecs_map_t)]
    ecs_map_fini.restype = None
    break

# vendor/flecs/flecs.h: 1893
for _lib in _libs.values():
    if not _lib.has("ecs_map_get", "cdecl"):
        continue
    ecs_map_get = _lib.get("ecs_map_get", "cdecl")
    ecs_map_get.argtypes = [POINTER(ecs_map_t), ecs_map_key_t]
    ecs_map_get.restype = POINTER(ecs_map_val_t)
    break

# vendor/flecs/flecs.h: 1899
for _lib in _libs.values():
    if not _lib.has("ecs_map_get_deref_", "cdecl"):
        continue
    ecs_map_get_deref_ = _lib.get("ecs_map_get_deref_", "cdecl")
    ecs_map_get_deref_.argtypes = [POINTER(ecs_map_t), ecs_map_key_t]
    ecs_map_get_deref_.restype = POINTER(c_ubyte)
    ecs_map_get_deref_.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1905
for _lib in _libs.values():
    if not _lib.has("ecs_map_ensure", "cdecl"):
        continue
    ecs_map_ensure = _lib.get("ecs_map_ensure", "cdecl")
    ecs_map_ensure.argtypes = [POINTER(ecs_map_t), ecs_map_key_t]
    ecs_map_ensure.restype = POINTER(ecs_map_val_t)
    break

# vendor/flecs/flecs.h: 1911
for _lib in _libs.values():
    if not _lib.has("ecs_map_ensure_alloc", "cdecl"):
        continue
    ecs_map_ensure_alloc = _lib.get("ecs_map_ensure_alloc", "cdecl")
    ecs_map_ensure_alloc.argtypes = [POINTER(ecs_map_t), ecs_size_t, ecs_map_key_t]
    ecs_map_ensure_alloc.restype = POINTER(c_ubyte)
    ecs_map_ensure_alloc.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1918
for _lib in _libs.values():
    if not _lib.has("ecs_map_insert", "cdecl"):
        continue
    ecs_map_insert = _lib.get("ecs_map_insert", "cdecl")
    ecs_map_insert.argtypes = [POINTER(ecs_map_t), ecs_map_key_t, ecs_map_val_t]
    ecs_map_insert.restype = None
    break

# vendor/flecs/flecs.h: 1925
for _lib in _libs.values():
    if not _lib.has("ecs_map_insert_alloc", "cdecl"):
        continue
    ecs_map_insert_alloc = _lib.get("ecs_map_insert_alloc", "cdecl")
    ecs_map_insert_alloc.argtypes = [POINTER(ecs_map_t), ecs_size_t, ecs_map_key_t]
    ecs_map_insert_alloc.restype = POINTER(c_ubyte)
    ecs_map_insert_alloc.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 1932
for _lib in _libs.values():
    if not _lib.has("ecs_map_remove", "cdecl"):
        continue
    ecs_map_remove = _lib.get("ecs_map_remove", "cdecl")
    ecs_map_remove.argtypes = [POINTER(ecs_map_t), ecs_map_key_t]
    ecs_map_remove.restype = ecs_map_val_t
    break

# vendor/flecs/flecs.h: 1938
for _lib in _libs.values():
    if not _lib.has("ecs_map_remove_free", "cdecl"):
        continue
    ecs_map_remove_free = _lib.get("ecs_map_remove_free", "cdecl")
    ecs_map_remove_free.argtypes = [POINTER(ecs_map_t), ecs_map_key_t]
    ecs_map_remove_free.restype = None
    break

# vendor/flecs/flecs.h: 1944
for _lib in _libs.values():
    if not _lib.has("ecs_map_clear", "cdecl"):
        continue
    ecs_map_clear = _lib.get("ecs_map_clear", "cdecl")
    ecs_map_clear.argtypes = [POINTER(ecs_map_t)]
    ecs_map_clear.restype = None
    break

# vendor/flecs/flecs.h: 1955
for _lib in _libs.values():
    if not _lib.has("ecs_map_iter", "cdecl"):
        continue
    ecs_map_iter = _lib.get("ecs_map_iter", "cdecl")
    ecs_map_iter.argtypes = [POINTER(ecs_map_t)]
    ecs_map_iter.restype = ecs_map_iter_t
    break

# vendor/flecs/flecs.h: 1960
for _lib in _libs.values():
    if not _lib.has("ecs_map_next", "cdecl"):
        continue
    ecs_map_next = _lib.get("ecs_map_next", "cdecl")
    ecs_map_next.argtypes = [POINTER(ecs_map_iter_t)]
    ecs_map_next.restype = c_bool
    break

# vendor/flecs/flecs.h: 1965
for _lib in _libs.values():
    if not _lib.has("ecs_map_copy", "cdecl"):
        continue
    ecs_map_copy = _lib.get("ecs_map_copy", "cdecl")
    ecs_map_copy.argtypes = [POINTER(ecs_map_t), POINTER(ecs_map_t)]
    ecs_map_copy.restype = None
    break

# vendor/flecs/flecs.h: 1999
for _lib in _libs.values():
    try:
        ecs_block_allocator_alloc_count = (c_int64).in_dll(
            _lib, "ecs_block_allocator_alloc_count"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 2000
for _lib in _libs.values():
    try:
        ecs_block_allocator_free_count = (c_int64).in_dll(
            _lib, "ecs_block_allocator_free_count"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 2001
for _lib in _libs.values():
    try:
        ecs_stack_allocator_alloc_count = (c_int64).in_dll(
            _lib, "ecs_stack_allocator_alloc_count"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 2002
for _lib in _libs.values():
    try:
        ecs_stack_allocator_free_count = (c_int64).in_dll(
            _lib, "ecs_stack_allocator_free_count"
        )
        break
    except:
        pass

struct_ecs_allocator_t.__slots__ = [
    "chunks",
    "sizes",
]
struct_ecs_allocator_t._fields_ = [
    ("chunks", ecs_block_allocator_t),
    ("sizes", struct_ecs_sparse_t),
]

# vendor/flecs/flecs.h: 2014
for _lib in _libs.values():
    if not _lib.has("flecs_allocator_init", "cdecl"):
        continue
    flecs_allocator_init = _lib.get("flecs_allocator_init", "cdecl")
    flecs_allocator_init.argtypes = [POINTER(ecs_allocator_t)]
    flecs_allocator_init.restype = None
    break

# vendor/flecs/flecs.h: 2018
for _lib in _libs.values():
    if not _lib.has("flecs_allocator_fini", "cdecl"):
        continue
    flecs_allocator_fini = _lib.get("flecs_allocator_fini", "cdecl")
    flecs_allocator_fini.argtypes = [POINTER(ecs_allocator_t)]
    flecs_allocator_fini.restype = None
    break

# vendor/flecs/flecs.h: 2022
for _lib in _libs.values():
    if not _lib.has("flecs_allocator_get", "cdecl"):
        continue
    flecs_allocator_get = _lib.get("flecs_allocator_get", "cdecl")
    flecs_allocator_get.argtypes = [POINTER(ecs_allocator_t), ecs_size_t]
    flecs_allocator_get.restype = POINTER(ecs_block_allocator_t)
    break

# vendor/flecs/flecs.h: 2027
for _lib in _libs.values():
    if not _lib.has("flecs_strdup", "cdecl"):
        continue
    flecs_strdup = _lib.get("flecs_strdup", "cdecl")
    flecs_strdup.argtypes = [POINTER(ecs_allocator_t), String]
    if sizeof(c_int) == sizeof(c_void_p):
        flecs_strdup.restype = ReturnString
    else:
        flecs_strdup.restype = String
        flecs_strdup.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 2032
for _lib in _libs.values():
    if not _lib.has("flecs_strfree", "cdecl"):
        continue
    flecs_strfree = _lib.get("flecs_strfree", "cdecl")
    flecs_strfree.argtypes = [POINTER(ecs_allocator_t), String]
    flecs_strfree.restype = None
    break

# vendor/flecs/flecs.h: 2037
for _lib in _libs.values():
    if not _lib.has("flecs_dup", "cdecl"):
        continue
    flecs_dup = _lib.get("flecs_dup", "cdecl")
    flecs_dup.argtypes = [POINTER(ecs_allocator_t), ecs_size_t, POINTER(None)]
    flecs_dup.restype = POINTER(c_ubyte)
    flecs_dup.errcheck = lambda v, *a: cast(v, c_void_p)
    break


# vendor/flecs/flecs.h: 2147
class struct_ecs_strbuf_list_elem(Structure):
    pass


struct_ecs_strbuf_list_elem.__slots__ = [
    "count",
    "separator",
]
struct_ecs_strbuf_list_elem._fields_ = [
    ("count", c_int32),
    ("separator", String),
]

ecs_strbuf_list_elem = struct_ecs_strbuf_list_elem  # vendor/flecs/flecs.h: 2147


# vendor/flecs/flecs.h: 2158
class struct_ecs_strbuf_t(Structure):
    pass


struct_ecs_strbuf_t.__slots__ = [
    "content",
    "length",
    "size",
    "list_stack",
    "list_sp",
    "small_string",
]
struct_ecs_strbuf_t._fields_ = [
    ("content", String),
    ("length", ecs_size_t),
    ("size", ecs_size_t),
    ("list_stack", ecs_strbuf_list_elem * int(32)),
    ("list_sp", c_int32),
    ("small_string", c_char * int(512)),
]

ecs_strbuf_t = struct_ecs_strbuf_t  # vendor/flecs/flecs.h: 2158

# vendor/flecs/flecs.h: 2163
for _lib in _libs.values():
    if _lib.has("ecs_strbuf_append", "cdecl"):
        _func = _lib.get("ecs_strbuf_append", "cdecl")
        _restype = None
        _errcheck = None
        _argtypes = [POINTER(ecs_strbuf_t), String]
        ecs_strbuf_append = _variadic_function(_func, _restype, _argtypes, _errcheck)

# vendor/flecs/flecs.h: 2171
for _lib in _libs.values():
    if not _lib.has("ecs_strbuf_vappend", "cdecl"):
        continue
    ecs_strbuf_vappend = _lib.get("ecs_strbuf_vappend", "cdecl")
    ecs_strbuf_vappend.argtypes = [POINTER(ecs_strbuf_t), String, c_void_p]
    ecs_strbuf_vappend.restype = None
    break

# vendor/flecs/flecs.h: 2179
for _lib in _libs.values():
    if not _lib.has("ecs_strbuf_appendstr", "cdecl"):
        continue
    ecs_strbuf_appendstr = _lib.get("ecs_strbuf_appendstr", "cdecl")
    ecs_strbuf_appendstr.argtypes = [POINTER(ecs_strbuf_t), String]
    ecs_strbuf_appendstr.restype = None
    break

# vendor/flecs/flecs.h: 2186
for _lib in _libs.values():
    if not _lib.has("ecs_strbuf_appendch", "cdecl"):
        continue
    ecs_strbuf_appendch = _lib.get("ecs_strbuf_appendch", "cdecl")
    ecs_strbuf_appendch.argtypes = [POINTER(ecs_strbuf_t), c_char]
    ecs_strbuf_appendch.restype = None
    break

# vendor/flecs/flecs.h: 2193
for _lib in _libs.values():
    if not _lib.has("ecs_strbuf_appendint", "cdecl"):
        continue
    ecs_strbuf_appendint = _lib.get("ecs_strbuf_appendint", "cdecl")
    ecs_strbuf_appendint.argtypes = [POINTER(ecs_strbuf_t), c_int64]
    ecs_strbuf_appendint.restype = None
    break

# vendor/flecs/flecs.h: 2200
for _lib in _libs.values():
    if not _lib.has("ecs_strbuf_appendflt", "cdecl"):
        continue
    ecs_strbuf_appendflt = _lib.get("ecs_strbuf_appendflt", "cdecl")
    ecs_strbuf_appendflt.argtypes = [POINTER(ecs_strbuf_t), c_double, c_char]
    ecs_strbuf_appendflt.restype = None
    break

# vendor/flecs/flecs.h: 2208
for _lib in _libs.values():
    if not _lib.has("ecs_strbuf_appendbool", "cdecl"):
        continue
    ecs_strbuf_appendbool = _lib.get("ecs_strbuf_appendbool", "cdecl")
    ecs_strbuf_appendbool.argtypes = [POINTER(ecs_strbuf_t), c_bool]
    ecs_strbuf_appendbool.restype = None
    break

# vendor/flecs/flecs.h: 2215
for _lib in _libs.values():
    if not _lib.has("ecs_strbuf_mergebuff", "cdecl"):
        continue
    ecs_strbuf_mergebuff = _lib.get("ecs_strbuf_mergebuff", "cdecl")
    ecs_strbuf_mergebuff.argtypes = [POINTER(ecs_strbuf_t), POINTER(ecs_strbuf_t)]
    ecs_strbuf_mergebuff.restype = None
    break

# vendor/flecs/flecs.h: 2222
for _lib in _libs.values():
    if not _lib.has("ecs_strbuf_appendstrn", "cdecl"):
        continue
    ecs_strbuf_appendstrn = _lib.get("ecs_strbuf_appendstrn", "cdecl")
    ecs_strbuf_appendstrn.argtypes = [POINTER(ecs_strbuf_t), String, c_int32]
    ecs_strbuf_appendstrn.restype = None
    break

# vendor/flecs/flecs.h: 2229
for _lib in _libs.values():
    if not _lib.has("ecs_strbuf_get", "cdecl"):
        continue
    ecs_strbuf_get = _lib.get("ecs_strbuf_get", "cdecl")
    ecs_strbuf_get.argtypes = [POINTER(ecs_strbuf_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_strbuf_get.restype = ReturnString
    else:
        ecs_strbuf_get.restype = String
        ecs_strbuf_get.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 2234
for _lib in _libs.values():
    if not _lib.has("ecs_strbuf_get_small", "cdecl"):
        continue
    ecs_strbuf_get_small = _lib.get("ecs_strbuf_get_small", "cdecl")
    ecs_strbuf_get_small.argtypes = [POINTER(ecs_strbuf_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_strbuf_get_small.restype = ReturnString
    else:
        ecs_strbuf_get_small.restype = String
        ecs_strbuf_get_small.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 2239
for _lib in _libs.values():
    if not _lib.has("ecs_strbuf_reset", "cdecl"):
        continue
    ecs_strbuf_reset = _lib.get("ecs_strbuf_reset", "cdecl")
    ecs_strbuf_reset.argtypes = [POINTER(ecs_strbuf_t)]
    ecs_strbuf_reset.restype = None
    break

# vendor/flecs/flecs.h: 2244
for _lib in _libs.values():
    if not _lib.has("ecs_strbuf_list_push", "cdecl"):
        continue
    ecs_strbuf_list_push = _lib.get("ecs_strbuf_list_push", "cdecl")
    ecs_strbuf_list_push.argtypes = [POINTER(ecs_strbuf_t), String, String]
    ecs_strbuf_list_push.restype = None
    break

# vendor/flecs/flecs.h: 2251
for _lib in _libs.values():
    if not _lib.has("ecs_strbuf_list_pop", "cdecl"):
        continue
    ecs_strbuf_list_pop = _lib.get("ecs_strbuf_list_pop", "cdecl")
    ecs_strbuf_list_pop.argtypes = [POINTER(ecs_strbuf_t), String]
    ecs_strbuf_list_pop.restype = None
    break

# vendor/flecs/flecs.h: 2257
for _lib in _libs.values():
    if not _lib.has("ecs_strbuf_list_next", "cdecl"):
        continue
    ecs_strbuf_list_next = _lib.get("ecs_strbuf_list_next", "cdecl")
    ecs_strbuf_list_next.argtypes = [POINTER(ecs_strbuf_t)]
    ecs_strbuf_list_next.restype = None
    break

# vendor/flecs/flecs.h: 2262
for _lib in _libs.values():
    if not _lib.has("ecs_strbuf_list_appendch", "cdecl"):
        continue
    ecs_strbuf_list_appendch = _lib.get("ecs_strbuf_list_appendch", "cdecl")
    ecs_strbuf_list_appendch.argtypes = [POINTER(ecs_strbuf_t), c_char]
    ecs_strbuf_list_appendch.restype = None
    break

# vendor/flecs/flecs.h: 2268
for _lib in _libs.values():
    if _lib.has("ecs_strbuf_list_append", "cdecl"):
        _func = _lib.get("ecs_strbuf_list_append", "cdecl")
        _restype = None
        _errcheck = None
        _argtypes = [POINTER(ecs_strbuf_t), String]
        ecs_strbuf_list_append = _variadic_function(
            _func, _restype, _argtypes, _errcheck
        )

# vendor/flecs/flecs.h: 2275
for _lib in _libs.values():
    if not _lib.has("ecs_strbuf_list_appendstr", "cdecl"):
        continue
    ecs_strbuf_list_appendstr = _lib.get("ecs_strbuf_list_appendstr", "cdecl")
    ecs_strbuf_list_appendstr.argtypes = [POINTER(ecs_strbuf_t), String]
    ecs_strbuf_list_appendstr.restype = None
    break

# vendor/flecs/flecs.h: 2281
for _lib in _libs.values():
    if not _lib.has("ecs_strbuf_list_appendstrn", "cdecl"):
        continue
    ecs_strbuf_list_appendstrn = _lib.get("ecs_strbuf_list_appendstrn", "cdecl")
    ecs_strbuf_list_appendstrn.argtypes = [POINTER(ecs_strbuf_t), String, c_int32]
    ecs_strbuf_list_appendstrn.restype = None
    break

# vendor/flecs/flecs.h: 2287
for _lib in _libs.values():
    if not _lib.has("ecs_strbuf_written", "cdecl"):
        continue
    ecs_strbuf_written = _lib.get("ecs_strbuf_written", "cdecl")
    ecs_strbuf_written.argtypes = [POINTER(ecs_strbuf_t)]
    ecs_strbuf_written.restype = c_int32
    break


# vendor/flecs/flecs.h: 2341
class struct_ecs_time_t(Structure):
    pass


struct_ecs_time_t.__slots__ = [
    "sec",
    "nanosec",
]
struct_ecs_time_t._fields_ = [
    ("sec", uint32_t),
    ("nanosec", uint32_t),
]

ecs_time_t = struct_ecs_time_t  # vendor/flecs/flecs.h: 2341

# vendor/flecs/flecs.h: 2344
for _lib in _libs.values():
    try:
        ecs_os_api_malloc_count = (c_int64).in_dll(_lib, "ecs_os_api_malloc_count")
        break
    except:
        pass

# vendor/flecs/flecs.h: 2345
for _lib in _libs.values():
    try:
        ecs_os_api_realloc_count = (c_int64).in_dll(_lib, "ecs_os_api_realloc_count")
        break
    except:
        pass

# vendor/flecs/flecs.h: 2346
for _lib in _libs.values():
    try:
        ecs_os_api_calloc_count = (c_int64).in_dll(_lib, "ecs_os_api_calloc_count")
        break
    except:
        pass

# vendor/flecs/flecs.h: 2347
for _lib in _libs.values():
    try:
        ecs_os_api_free_count = (c_int64).in_dll(_lib, "ecs_os_api_free_count")
        break
    except:
        pass

ecs_os_thread_t = uintptr_t  # vendor/flecs/flecs.h: 2350

ecs_os_cond_t = uintptr_t  # vendor/flecs/flecs.h: 2351

ecs_os_mutex_t = uintptr_t  # vendor/flecs/flecs.h: 2352

ecs_os_dl_t = uintptr_t  # vendor/flecs/flecs.h: 2353

ecs_os_sock_t = uintptr_t  # vendor/flecs/flecs.h: 2354

ecs_os_thread_id_t = uint64_t  # vendor/flecs/flecs.h: 2357

ecs_os_proc_t = CFUNCTYPE(
    UNCHECKED(None),
)  # vendor/flecs/flecs.h: 2360

ecs_os_api_init_t = CFUNCTYPE(
    UNCHECKED(None),
)  # vendor/flecs/flecs.h: 2364

ecs_os_api_fini_t = CFUNCTYPE(
    UNCHECKED(None),
)  # vendor/flecs/flecs.h: 2368

ecs_os_api_malloc_t = CFUNCTYPE(
    UNCHECKED(POINTER(c_ubyte)), ecs_size_t
)  # vendor/flecs/flecs.h: 2372

ecs_os_api_free_t = CFUNCTYPE(
    UNCHECKED(None), POINTER(None)
)  # vendor/flecs/flecs.h: 2377

ecs_os_api_realloc_t = CFUNCTYPE(
    UNCHECKED(POINTER(c_ubyte)), POINTER(None), ecs_size_t
)  # vendor/flecs/flecs.h: 2382

ecs_os_api_calloc_t = CFUNCTYPE(
    UNCHECKED(POINTER(c_ubyte)), ecs_size_t
)  # vendor/flecs/flecs.h: 2388

ecs_os_api_strdup_t = CFUNCTYPE(UNCHECKED(String), String)  # vendor/flecs/flecs.h: 2393

ecs_os_thread_callback_t = CFUNCTYPE(
    UNCHECKED(POINTER(c_ubyte)), POINTER(None)
)  # vendor/flecs/flecs.h: 2398

ecs_os_api_thread_new_t = CFUNCTYPE(
    UNCHECKED(ecs_os_thread_t), ecs_os_thread_callback_t, POINTER(None)
)  # vendor/flecs/flecs.h: 2403

ecs_os_api_thread_join_t = CFUNCTYPE(
    UNCHECKED(POINTER(c_ubyte)), ecs_os_thread_t
)  # vendor/flecs/flecs.h: 2409

ecs_os_api_thread_self_t = CFUNCTYPE(
    UNCHECKED(ecs_os_thread_id_t),
)  # vendor/flecs/flecs.h: 2414

ecs_os_api_task_new_t = CFUNCTYPE(
    UNCHECKED(ecs_os_thread_t), ecs_os_thread_callback_t, POINTER(None)
)  # vendor/flecs/flecs.h: 2418

ecs_os_api_task_join_t = CFUNCTYPE(
    UNCHECKED(POINTER(c_ubyte)), ecs_os_thread_t
)  # vendor/flecs/flecs.h: 2424

ecs_os_api_ainc_t = CFUNCTYPE(
    UNCHECKED(c_int32), POINTER(c_int32)
)  # vendor/flecs/flecs.h: 2430

ecs_os_api_lainc_t = CFUNCTYPE(
    UNCHECKED(c_int64), POINTER(c_int64)
)  # vendor/flecs/flecs.h: 2435

ecs_os_api_mutex_new_t = CFUNCTYPE(
    UNCHECKED(ecs_os_mutex_t),
)  # vendor/flecs/flecs.h: 2441

ecs_os_api_mutex_lock_t = CFUNCTYPE(
    UNCHECKED(None), ecs_os_mutex_t
)  # vendor/flecs/flecs.h: 2446

ecs_os_api_mutex_unlock_t = CFUNCTYPE(
    UNCHECKED(None), ecs_os_mutex_t
)  # vendor/flecs/flecs.h: 2451

ecs_os_api_mutex_free_t = CFUNCTYPE(
    UNCHECKED(None), ecs_os_mutex_t
)  # vendor/flecs/flecs.h: 2456

ecs_os_api_cond_new_t = CFUNCTYPE(
    UNCHECKED(ecs_os_cond_t),
)  # vendor/flecs/flecs.h: 2462

ecs_os_api_cond_free_t = CFUNCTYPE(
    UNCHECKED(None), ecs_os_cond_t
)  # vendor/flecs/flecs.h: 2467

ecs_os_api_cond_signal_t = CFUNCTYPE(
    UNCHECKED(None), ecs_os_cond_t
)  # vendor/flecs/flecs.h: 2472

ecs_os_api_cond_broadcast_t = CFUNCTYPE(
    UNCHECKED(None), ecs_os_cond_t
)  # vendor/flecs/flecs.h: 2477

ecs_os_api_cond_wait_t = CFUNCTYPE(
    UNCHECKED(None), ecs_os_cond_t, ecs_os_mutex_t
)  # vendor/flecs/flecs.h: 2482

ecs_os_api_sleep_t = CFUNCTYPE(
    UNCHECKED(None), c_int32, c_int32
)  # vendor/flecs/flecs.h: 2488

ecs_os_api_enable_high_timer_resolution_t = CFUNCTYPE(
    UNCHECKED(None), c_bool
)  # vendor/flecs/flecs.h: 2494

ecs_os_api_get_time_t = CFUNCTYPE(
    UNCHECKED(None), POINTER(ecs_time_t)
)  # vendor/flecs/flecs.h: 2499

ecs_os_api_now_t = CFUNCTYPE(
    UNCHECKED(uint64_t),
)  # vendor/flecs/flecs.h: 2504

ecs_os_api_log_t = CFUNCTYPE(
    UNCHECKED(None), c_int32, String, c_int32, String
)  # vendor/flecs/flecs.h: 2508

ecs_os_api_abort_t = CFUNCTYPE(
    UNCHECKED(None),
)  # vendor/flecs/flecs.h: 2516

ecs_os_api_dlopen_t = CFUNCTYPE(
    UNCHECKED(ecs_os_dl_t), String
)  # vendor/flecs/flecs.h: 2521

ecs_os_api_dlproc_t = CFUNCTYPE(
    UNCHECKED(ecs_os_proc_t), ecs_os_dl_t, String
)  # vendor/flecs/flecs.h: 2526

ecs_os_api_dlclose_t = CFUNCTYPE(
    UNCHECKED(None), ecs_os_dl_t
)  # vendor/flecs/flecs.h: 2532

ecs_os_api_module_to_path_t = CFUNCTYPE(
    UNCHECKED(String), String
)  # vendor/flecs/flecs.h: 2537

ecs_os_api_perf_trace_t = CFUNCTYPE(
    UNCHECKED(None), String, c_size_t, String
)  # vendor/flecs/flecs.h: 2541


# vendor/flecs/flecs.h: 2637
class struct_ecs_os_api_t(Structure):
    pass


struct_ecs_os_api_t.__slots__ = [
    "init_",
    "fini_",
    "malloc_",
    "realloc_",
    "calloc_",
    "free_",
    "strdup_",
    "thread_new_",
    "thread_join_",
    "thread_self_",
    "task_new_",
    "task_join_",
    "ainc_",
    "adec_",
    "lainc_",
    "ladec_",
    "mutex_new_",
    "mutex_free_",
    "mutex_lock_",
    "mutex_unlock_",
    "cond_new_",
    "cond_free_",
    "cond_signal_",
    "cond_broadcast_",
    "cond_wait_",
    "sleep_",
    "now_",
    "get_time_",
    "log_",
    "abort_",
    "dlopen_",
    "dlproc_",
    "dlclose_",
    "module_to_dl_",
    "module_to_etc_",
    "perf_trace_push_",
    "perf_trace_pop_",
    "log_level_",
    "log_indent_",
    "log_last_error_",
    "log_last_timestamp_",
    "flags_",
    "log_out_",
]
struct_ecs_os_api_t._fields_ = [
    ("init_", ecs_os_api_init_t),
    ("fini_", ecs_os_api_fini_t),
    ("malloc_", ecs_os_api_malloc_t),
    ("realloc_", ecs_os_api_realloc_t),
    ("calloc_", ecs_os_api_calloc_t),
    ("free_", ecs_os_api_free_t),
    ("strdup_", ecs_os_api_strdup_t),
    ("thread_new_", ecs_os_api_thread_new_t),
    ("thread_join_", ecs_os_api_thread_join_t),
    ("thread_self_", ecs_os_api_thread_self_t),
    ("task_new_", ecs_os_api_thread_new_t),
    ("task_join_", ecs_os_api_thread_join_t),
    ("ainc_", ecs_os_api_ainc_t),
    ("adec_", ecs_os_api_ainc_t),
    ("lainc_", ecs_os_api_lainc_t),
    ("ladec_", ecs_os_api_lainc_t),
    ("mutex_new_", ecs_os_api_mutex_new_t),
    ("mutex_free_", ecs_os_api_mutex_free_t),
    ("mutex_lock_", ecs_os_api_mutex_lock_t),
    ("mutex_unlock_", ecs_os_api_mutex_lock_t),
    ("cond_new_", ecs_os_api_cond_new_t),
    ("cond_free_", ecs_os_api_cond_free_t),
    ("cond_signal_", ecs_os_api_cond_signal_t),
    ("cond_broadcast_", ecs_os_api_cond_broadcast_t),
    ("cond_wait_", ecs_os_api_cond_wait_t),
    ("sleep_", ecs_os_api_sleep_t),
    ("now_", ecs_os_api_now_t),
    ("get_time_", ecs_os_api_get_time_t),
    ("log_", ecs_os_api_log_t),
    ("abort_", ecs_os_api_abort_t),
    ("dlopen_", ecs_os_api_dlopen_t),
    ("dlproc_", ecs_os_api_dlproc_t),
    ("dlclose_", ecs_os_api_dlclose_t),
    ("module_to_dl_", ecs_os_api_module_to_path_t),
    ("module_to_etc_", ecs_os_api_module_to_path_t),
    ("perf_trace_push_", ecs_os_api_perf_trace_t),
    ("perf_trace_pop_", ecs_os_api_perf_trace_t),
    ("log_level_", c_int32),
    ("log_indent_", c_int32),
    ("log_last_error_", c_int32),
    ("log_last_timestamp_", c_int64),
    ("flags_", ecs_flags32_t),
    ("log_out_", POINTER(None)),
]

ecs_os_api_t = struct_ecs_os_api_t  # vendor/flecs/flecs.h: 2637

# vendor/flecs/flecs.h: 2641
for _lib in _libs.values():
    try:
        ecs_os_api = (ecs_os_api_t).in_dll(_lib, "ecs_os_api")
        break
    except:
        pass

# vendor/flecs/flecs.h: 2655
for _lib in _libs.values():
    if not _lib.has("ecs_os_init", "cdecl"):
        continue
    ecs_os_init = _lib.get("ecs_os_init", "cdecl")
    ecs_os_init.argtypes = []
    ecs_os_init.restype = None
    break

# vendor/flecs/flecs.h: 2661
for _lib in _libs.values():
    if not _lib.has("ecs_os_fini", "cdecl"):
        continue
    ecs_os_fini = _lib.get("ecs_os_fini", "cdecl")
    ecs_os_fini.argtypes = []
    ecs_os_fini.restype = None
    break

# vendor/flecs/flecs.h: 2670
for _lib in _libs.values():
    if not _lib.has("ecs_os_set_api", "cdecl"):
        continue
    ecs_os_set_api = _lib.get("ecs_os_set_api", "cdecl")
    ecs_os_set_api.argtypes = [POINTER(ecs_os_api_t)]
    ecs_os_set_api.restype = None
    break

# vendor/flecs/flecs.h: 2679
for _lib in _libs.values():
    if not _lib.has("ecs_os_get_api", "cdecl"):
        continue
    ecs_os_get_api = _lib.get("ecs_os_get_api", "cdecl")
    ecs_os_get_api.argtypes = []
    ecs_os_get_api.restype = ecs_os_api_t
    break

# vendor/flecs/flecs.h: 2688
for _lib in _libs.values():
    if not _lib.has("ecs_os_set_api_defaults", "cdecl"):
        continue
    ecs_os_set_api_defaults = _lib.get("ecs_os_set_api_defaults", "cdecl")
    ecs_os_set_api_defaults.argtypes = []
    ecs_os_set_api_defaults.restype = None
    break

# vendor/flecs/flecs.h: 2873
for _lib in _libs.values():
    if not _lib.has("ecs_os_dbg", "cdecl"):
        continue
    ecs_os_dbg = _lib.get("ecs_os_dbg", "cdecl")
    ecs_os_dbg.argtypes = [String, c_int32, String]
    ecs_os_dbg.restype = None
    break

# vendor/flecs/flecs.h: 2885
for _lib in _libs.values():
    if not _lib.has("ecs_os_trace", "cdecl"):
        continue
    ecs_os_trace = _lib.get("ecs_os_trace", "cdecl")
    ecs_os_trace.argtypes = [String, c_int32, String]
    ecs_os_trace.restype = None
    break

# vendor/flecs/flecs.h: 2897
for _lib in _libs.values():
    if not _lib.has("ecs_os_warn", "cdecl"):
        continue
    ecs_os_warn = _lib.get("ecs_os_warn", "cdecl")
    ecs_os_warn.argtypes = [String, c_int32, String]
    ecs_os_warn.restype = None
    break

# vendor/flecs/flecs.h: 2909
for _lib in _libs.values():
    if not _lib.has("ecs_os_err", "cdecl"):
        continue
    ecs_os_err = _lib.get("ecs_os_err", "cdecl")
    ecs_os_err.argtypes = [String, c_int32, String]
    ecs_os_err.restype = None
    break

# vendor/flecs/flecs.h: 2921
for _lib in _libs.values():
    if not _lib.has("ecs_os_fatal", "cdecl"):
        continue
    ecs_os_fatal = _lib.get("ecs_os_fatal", "cdecl")
    ecs_os_fatal.argtypes = [String, c_int32, String]
    ecs_os_fatal.restype = None
    break

# vendor/flecs/flecs.h: 2932
for _lib in _libs.values():
    if not _lib.has("ecs_os_strerror", "cdecl"):
        continue
    ecs_os_strerror = _lib.get("ecs_os_strerror", "cdecl")
    ecs_os_strerror.argtypes = [c_int]
    ecs_os_strerror.restype = c_char_p
    break

# vendor/flecs/flecs.h: 2942
for _lib in _libs.values():
    if not _lib.has("ecs_os_strset", "cdecl"):
        continue
    ecs_os_strset = _lib.get("ecs_os_strset", "cdecl")
    ecs_os_strset.argtypes = [POINTER(POINTER(c_char)), String]
    ecs_os_strset.restype = None
    break

# vendor/flecs/flecs.h: 2955
for _lib in _libs.values():
    if not _lib.has("ecs_os_perf_trace_push_", "cdecl"):
        continue
    ecs_os_perf_trace_push_ = _lib.get("ecs_os_perf_trace_push_", "cdecl")
    ecs_os_perf_trace_push_.argtypes = [String, c_size_t, String]
    ecs_os_perf_trace_push_.restype = None
    break

# vendor/flecs/flecs.h: 2960
for _lib in _libs.values():
    if not _lib.has("ecs_os_perf_trace_pop_", "cdecl"):
        continue
    ecs_os_perf_trace_pop_ = _lib.get("ecs_os_perf_trace_pop_", "cdecl")
    ecs_os_perf_trace_pop_.argtypes = [String, c_size_t, String]
    ecs_os_perf_trace_pop_.restype = None
    break

# vendor/flecs/flecs.h: 2970
for _lib in _libs.values():
    if not _lib.has("ecs_sleepf", "cdecl"):
        continue
    ecs_sleepf = _lib.get("ecs_sleepf", "cdecl")
    ecs_sleepf.argtypes = [c_double]
    ecs_sleepf.restype = None
    break

# vendor/flecs/flecs.h: 2989
for _lib in _libs.values():
    if not _lib.has("ecs_time_measure", "cdecl"):
        continue
    ecs_time_measure = _lib.get("ecs_time_measure", "cdecl")
    ecs_time_measure.argtypes = [POINTER(ecs_time_t)]
    ecs_time_measure.restype = c_double
    break

# vendor/flecs/flecs.h: 2999
for _lib in _libs.values():
    if not _lib.has("ecs_time_sub", "cdecl"):
        continue
    ecs_time_sub = _lib.get("ecs_time_sub", "cdecl")
    ecs_time_sub.argtypes = [ecs_time_t, ecs_time_t]
    ecs_time_sub.restype = ecs_time_t
    break

# vendor/flecs/flecs.h: 3009
for _lib in _libs.values():
    if not _lib.has("ecs_time_to_double", "cdecl"):
        continue
    ecs_time_to_double = _lib.get("ecs_time_to_double", "cdecl")
    ecs_time_to_double.argtypes = [ecs_time_t]
    ecs_time_to_double.restype = c_double
    break

# vendor/flecs/flecs.h: 3019
for _lib in _libs.values():
    if not _lib.has("ecs_os_memdup", "cdecl"):
        continue
    ecs_os_memdup = _lib.get("ecs_os_memdup", "cdecl")
    ecs_os_memdup.argtypes = [POINTER(None), ecs_size_t]
    ecs_os_memdup.restype = POINTER(c_ubyte)
    ecs_os_memdup.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 3025
for _lib in _libs.values():
    if not _lib.has("ecs_os_has_heap", "cdecl"):
        continue
    ecs_os_has_heap = _lib.get("ecs_os_has_heap", "cdecl")
    ecs_os_has_heap.argtypes = []
    ecs_os_has_heap.restype = c_bool
    break

# vendor/flecs/flecs.h: 3029
for _lib in _libs.values():
    if not _lib.has("ecs_os_has_threading", "cdecl"):
        continue
    ecs_os_has_threading = _lib.get("ecs_os_has_threading", "cdecl")
    ecs_os_has_threading.argtypes = []
    ecs_os_has_threading.restype = c_bool
    break

# vendor/flecs/flecs.h: 3033
for _lib in _libs.values():
    if not _lib.has("ecs_os_has_task_support", "cdecl"):
        continue
    ecs_os_has_task_support = _lib.get("ecs_os_has_task_support", "cdecl")
    ecs_os_has_task_support.argtypes = []
    ecs_os_has_task_support.restype = c_bool
    break

# vendor/flecs/flecs.h: 3037
for _lib in _libs.values():
    if not _lib.has("ecs_os_has_time", "cdecl"):
        continue
    ecs_os_has_time = _lib.get("ecs_os_has_time", "cdecl")
    ecs_os_has_time.argtypes = []
    ecs_os_has_time.restype = c_bool
    break

# vendor/flecs/flecs.h: 3041
for _lib in _libs.values():
    if not _lib.has("ecs_os_has_logging", "cdecl"):
        continue
    ecs_os_has_logging = _lib.get("ecs_os_has_logging", "cdecl")
    ecs_os_has_logging.argtypes = []
    ecs_os_has_logging.restype = c_bool
    break

# vendor/flecs/flecs.h: 3045
for _lib in _libs.values():
    if not _lib.has("ecs_os_has_dl", "cdecl"):
        continue
    ecs_os_has_dl = _lib.get("ecs_os_has_dl", "cdecl")
    ecs_os_has_dl.argtypes = []
    ecs_os_has_dl.restype = c_bool
    break

# vendor/flecs/flecs.h: 3049
for _lib in _libs.values():
    if not _lib.has("ecs_os_has_modules", "cdecl"):
        continue
    ecs_os_has_modules = _lib.get("ecs_os_has_modules", "cdecl")
    ecs_os_has_modules.argtypes = []
    ecs_os_has_modules.restype = c_bool
    break

ecs_id_t = uint64_t  # vendor/flecs/flecs.h: 3080

ecs_entity_t = ecs_id_t  # vendor/flecs/flecs.h: 3087


# vendor/flecs/flecs.h: 3107
class struct_anon_8(Structure):
    pass


struct_anon_8.__slots__ = [
    "array",
    "count",
]
struct_anon_8._fields_ = [
    ("array", POINTER(ecs_id_t)),
    ("count", c_int32),
]

ecs_type_t = struct_anon_8  # vendor/flecs/flecs.h: 3107


# vendor/flecs/flecs.h: 3131
class struct_ecs_world_t(Structure):
    pass


ecs_world_t = struct_ecs_world_t  # vendor/flecs/flecs.h: 3131


# vendor/flecs/flecs.h: 3134
class struct_ecs_stage_t(Structure):
    pass


ecs_stage_t = struct_ecs_stage_t  # vendor/flecs/flecs.h: 3134


# vendor/flecs/flecs.h: 3137
class struct_ecs_table_t(Structure):
    pass


ecs_table_t = struct_ecs_table_t  # vendor/flecs/flecs.h: 3137


# vendor/flecs/flecs.h: 3494
class struct_ecs_term_t(Structure):
    pass


ecs_term_t = struct_ecs_term_t  # vendor/flecs/flecs.h: 3140


# vendor/flecs/flecs.h: 3518
class struct_ecs_query_t(Structure):
    pass


ecs_query_t = struct_ecs_query_t  # vendor/flecs/flecs.h: 3143


# vendor/flecs/flecs.h: 3559
class struct_ecs_observer_t(Structure):
    pass


ecs_observer_t = struct_ecs_observer_t  # vendor/flecs/flecs.h: 3162


# vendor/flecs/flecs.h: 3746
class struct_ecs_observable_t(Structure):
    pass


ecs_observable_t = struct_ecs_observable_t  # vendor/flecs/flecs.h: 3167


# vendor/flecs/flecs.h: 4860
class struct_ecs_iter_t(Structure):
    pass


ecs_iter_t = struct_ecs_iter_t  # vendor/flecs/flecs.h: 3173


# vendor/flecs/flecs.h: 3774
class struct_ecs_ref_t(Structure):
    pass


ecs_ref_t = struct_ecs_ref_t  # vendor/flecs/flecs.h: 3183


# vendor/flecs/flecs.h: 3631
class struct_ecs_type_hooks_t(Structure):
    pass


ecs_type_hooks_t = struct_ecs_type_hooks_t  # vendor/flecs/flecs.h: 3188


# vendor/flecs/flecs.h: 3695
class struct_ecs_type_info_t(Structure):
    pass


ecs_type_info_t = struct_ecs_type_info_t  # vendor/flecs/flecs.h: 3193


# vendor/flecs/flecs.h: 4401
class struct_ecs_record_t(Structure):
    pass


ecs_record_t = struct_ecs_record_t  # vendor/flecs/flecs.h: 3196


# vendor/flecs/flecs.h: 3199
class struct_ecs_component_record_t(Structure):
    pass


ecs_component_record_t = struct_ecs_component_record_t  # vendor/flecs/flecs.h: 3199

ecs_poly_t = None  # vendor/flecs/flecs.h: 3220


# vendor/flecs/flecs.h: 3223
class struct_ecs_mixins_t(Structure):
    pass


ecs_mixins_t = struct_ecs_mixins_t  # vendor/flecs/flecs.h: 3223


# vendor/flecs/flecs.h: 3230
class struct_ecs_header_t(Structure):
    pass


struct_ecs_header_t.__slots__ = [
    "type",
    "refcount",
    "mixins",
]
struct_ecs_header_t._fields_ = [
    ("type", c_int32),
    ("refcount", c_int32),
    ("mixins", POINTER(ecs_mixins_t)),
]

ecs_header_t = struct_ecs_header_t  # vendor/flecs/flecs.h: 3230


# vendor/flecs/flecs.h: 4418
class struct_ecs_table_record_t(Structure):
    pass


ecs_table_record_t = struct_ecs_table_record_t  # vendor/flecs/flecs.h: 3232

ecs_run_action_t = CFUNCTYPE(
    UNCHECKED(None), POINTER(ecs_iter_t)
)  # vendor/flecs/flecs.h: 3252

ecs_iter_action_t = CFUNCTYPE(
    UNCHECKED(None), POINTER(ecs_iter_t)
)  # vendor/flecs/flecs.h: 3261

ecs_iter_next_action_t = CFUNCTYPE(
    UNCHECKED(c_bool), POINTER(ecs_iter_t)
)  # vendor/flecs/flecs.h: 3271

ecs_iter_fini_action_t = CFUNCTYPE(
    UNCHECKED(None), POINTER(ecs_iter_t)
)  # vendor/flecs/flecs.h: 3279

ecs_order_by_action_t = CFUNCTYPE(
    UNCHECKED(c_int), ecs_entity_t, POINTER(None), ecs_entity_t, POINTER(None)
)  # vendor/flecs/flecs.h: 3283

ecs_sort_table_action_t = CFUNCTYPE(
    UNCHECKED(None),
    POINTER(ecs_world_t),
    POINTER(ecs_table_t),
    POINTER(ecs_entity_t),
    POINTER(None),
    c_int32,
    c_int32,
    c_int32,
    ecs_order_by_action_t,
)  # vendor/flecs/flecs.h: 3290

ecs_group_by_action_t = CFUNCTYPE(
    UNCHECKED(uint64_t),
    POINTER(ecs_world_t),
    POINTER(ecs_table_t),
    ecs_id_t,
    POINTER(None),
)  # vendor/flecs/flecs.h: 3301

ecs_group_create_action_t = CFUNCTYPE(
    UNCHECKED(POINTER(c_ubyte)), POINTER(ecs_world_t), uint64_t, POINTER(None)
)  # vendor/flecs/flecs.h: 3308

ecs_group_delete_action_t = CFUNCTYPE(
    UNCHECKED(None), POINTER(ecs_world_t), uint64_t, POINTER(None), POINTER(None)
)  # vendor/flecs/flecs.h: 3314

ecs_module_action_t = CFUNCTYPE(
    UNCHECKED(None), POINTER(ecs_world_t)
)  # vendor/flecs/flecs.h: 3321

ecs_fini_action_t = CFUNCTYPE(
    UNCHECKED(None), POINTER(ecs_world_t), POINTER(None)
)  # vendor/flecs/flecs.h: 3325

ecs_ctx_free_t = CFUNCTYPE(UNCHECKED(None), POINTER(None))  # vendor/flecs/flecs.h: 3330

ecs_compare_action_t = CFUNCTYPE(
    UNCHECKED(c_int), POINTER(None), POINTER(None)
)  # vendor/flecs/flecs.h: 3334

ecs_hash_value_action_t = CFUNCTYPE(
    UNCHECKED(uint64_t), POINTER(None)
)  # vendor/flecs/flecs.h: 3339

ecs_xtor_t = CFUNCTYPE(
    UNCHECKED(None), POINTER(None), c_int32, POINTER(ecs_type_info_t)
)  # vendor/flecs/flecs.h: 3343

ecs_copy_t = CFUNCTYPE(
    UNCHECKED(None), POINTER(None), POINTER(None), c_int32, POINTER(ecs_type_info_t)
)  # vendor/flecs/flecs.h: 3349

ecs_move_t = CFUNCTYPE(
    UNCHECKED(None), POINTER(None), POINTER(None), c_int32, POINTER(ecs_type_info_t)
)  # vendor/flecs/flecs.h: 3356

ecs_cmp_t = CFUNCTYPE(
    UNCHECKED(c_int), POINTER(None), POINTER(None), POINTER(ecs_type_info_t)
)  # vendor/flecs/flecs.h: 3363

ecs_equals_t = CFUNCTYPE(
    UNCHECKED(c_bool), POINTER(None), POINTER(None), POINTER(ecs_type_info_t)
)  # vendor/flecs/flecs.h: 3369

flecs_poly_dtor_t = CFUNCTYPE(
    UNCHECKED(None), POINTER(ecs_poly_t)
)  # vendor/flecs/flecs.h: 3375

enum_ecs_inout_kind_t = c_int  # vendor/flecs/flecs.h: 3395

EcsInOutDefault = 0  # vendor/flecs/flecs.h: 3395

EcsInOutNone = EcsInOutDefault + 1  # vendor/flecs/flecs.h: 3395

EcsInOutFilter = EcsInOutNone + 1  # vendor/flecs/flecs.h: 3395

EcsInOut = EcsInOutFilter + 1  # vendor/flecs/flecs.h: 3395

EcsIn = EcsInOut + 1  # vendor/flecs/flecs.h: 3395

EcsOut = EcsIn + 1  # vendor/flecs/flecs.h: 3395

ecs_inout_kind_t = enum_ecs_inout_kind_t  # vendor/flecs/flecs.h: 3395

enum_ecs_oper_kind_t = c_int  # vendor/flecs/flecs.h: 3406

EcsAnd = 0  # vendor/flecs/flecs.h: 3406

EcsOr = EcsAnd + 1  # vendor/flecs/flecs.h: 3406

EcsNot = EcsOr + 1  # vendor/flecs/flecs.h: 3406

EcsOptional = EcsNot + 1  # vendor/flecs/flecs.h: 3406

EcsAndFrom = EcsOptional + 1  # vendor/flecs/flecs.h: 3406

EcsOrFrom = EcsAndFrom + 1  # vendor/flecs/flecs.h: 3406

EcsNotFrom = EcsOrFrom + 1  # vendor/flecs/flecs.h: 3406

ecs_oper_kind_t = enum_ecs_oper_kind_t  # vendor/flecs/flecs.h: 3406

enum_ecs_query_cache_kind_t = c_int  # vendor/flecs/flecs.h: 3414

EcsQueryCacheDefault = 0  # vendor/flecs/flecs.h: 3414

EcsQueryCacheAuto = EcsQueryCacheDefault + 1  # vendor/flecs/flecs.h: 3414

EcsQueryCacheAll = EcsQueryCacheAuto + 1  # vendor/flecs/flecs.h: 3414

EcsQueryCacheNone = EcsQueryCacheAll + 1  # vendor/flecs/flecs.h: 3414

ecs_query_cache_kind_t = enum_ecs_query_cache_kind_t  # vendor/flecs/flecs.h: 3414


# vendor/flecs/flecs.h: 3491
class struct_ecs_term_ref_t(Structure):
    pass


struct_ecs_term_ref_t.__slots__ = [
    "id",
    "name",
]
struct_ecs_term_ref_t._fields_ = [
    ("id", ecs_entity_t),
    ("name", String),
]

ecs_term_ref_t = struct_ecs_term_ref_t  # vendor/flecs/flecs.h: 3491

struct_ecs_term_t.__slots__ = [
    "id",
    "src",
    "first",
    "second",
    "trav",
    "inout",
    "oper",
    "field_index",
    "flags_",
]
struct_ecs_term_t._fields_ = [
    ("id", ecs_id_t),
    ("src", ecs_term_ref_t),
    ("first", ecs_term_ref_t),
    ("second", ecs_term_ref_t),
    ("trav", ecs_entity_t),
    ("inout", c_int16),
    ("oper", c_int16),
    ("field_index", c_int8),
    ("flags_", ecs_flags16_t),
]

struct_ecs_query_t.__slots__ = [
    "hdr",
    "terms",
    "sizes",
    "ids",
    "bloom_filter",
    "flags",
    "var_count",
    "term_count",
    "field_count",
    "fixed_fields",
    "var_fields",
    "static_id_fields",
    "data_fields",
    "write_fields",
    "read_fields",
    "row_fields",
    "shared_readonly_fields",
    "set_fields",
    "cache_kind",
    "vars",
    "ctx",
    "binding_ctx",
    "entity",
    "real_world",
    "world",
    "eval_count",
]
struct_ecs_query_t._fields_ = [
    ("hdr", ecs_header_t),
    ("terms", POINTER(ecs_term_t)),
    ("sizes", POINTER(c_int32)),
    ("ids", POINTER(ecs_id_t)),
    ("bloom_filter", uint64_t),
    ("flags", ecs_flags32_t),
    ("var_count", c_int8),
    ("term_count", c_int8),
    ("field_count", c_int8),
    ("fixed_fields", ecs_flags32_t),
    ("var_fields", ecs_flags32_t),
    ("static_id_fields", ecs_flags32_t),
    ("data_fields", ecs_flags32_t),
    ("write_fields", ecs_flags32_t),
    ("read_fields", ecs_flags32_t),
    ("row_fields", ecs_flags32_t),
    ("shared_readonly_fields", ecs_flags32_t),
    ("set_fields", ecs_flags32_t),
    ("cache_kind", ecs_query_cache_kind_t),
    ("vars", POINTER(POINTER(c_char))),
    ("ctx", POINTER(None)),
    ("binding_ctx", POINTER(None)),
    ("entity", ecs_entity_t),
    ("real_world", POINTER(ecs_world_t)),
    ("world", POINTER(ecs_world_t)),
    ("eval_count", c_int32),
]

struct_ecs_observer_t.__slots__ = [
    "hdr",
    "query",
    "events",
    "event_count",
    "callback",
    "run",
    "ctx",
    "callback_ctx",
    "run_ctx",
    "ctx_free",
    "callback_ctx_free",
    "run_ctx_free",
    "observable",
    "world",
    "entity",
]
struct_ecs_observer_t._fields_ = [
    ("hdr", ecs_header_t),
    ("query", POINTER(ecs_query_t)),
    ("events", ecs_entity_t * int(8)),
    ("event_count", c_int32),
    ("callback", ecs_iter_action_t),
    ("run", ecs_run_action_t),
    ("ctx", POINTER(None)),
    ("callback_ctx", POINTER(None)),
    ("run_ctx", POINTER(None)),
    ("ctx_free", ecs_ctx_free_t),
    ("callback_ctx_free", ecs_ctx_free_t),
    ("run_ctx_free", ecs_ctx_free_t),
    ("observable", POINTER(ecs_observable_t)),
    ("world", POINTER(ecs_world_t)),
    ("entity", ecs_entity_t),
]

struct_ecs_type_hooks_t.__slots__ = [
    "ctor",
    "dtor",
    "copy",
    "move",
    "copy_ctor",
    "move_ctor",
    "ctor_move_dtor",
    "move_dtor",
    "cmp",
    "equals",
    "flags",
    "on_add",
    "on_set",
    "on_remove",
    "ctx",
    "binding_ctx",
    "lifecycle_ctx",
    "ctx_free",
    "binding_ctx_free",
    "lifecycle_ctx_free",
]
struct_ecs_type_hooks_t._fields_ = [
    ("ctor", ecs_xtor_t),
    ("dtor", ecs_xtor_t),
    ("copy", ecs_copy_t),
    ("move", ecs_move_t),
    ("copy_ctor", ecs_copy_t),
    ("move_ctor", ecs_move_t),
    ("ctor_move_dtor", ecs_move_t),
    ("move_dtor", ecs_move_t),
    ("cmp", ecs_cmp_t),
    ("equals", ecs_equals_t),
    ("flags", ecs_flags32_t),
    ("on_add", ecs_iter_action_t),
    ("on_set", ecs_iter_action_t),
    ("on_remove", ecs_iter_action_t),
    ("ctx", POINTER(None)),
    ("binding_ctx", POINTER(None)),
    ("lifecycle_ctx", POINTER(None)),
    ("ctx_free", ecs_ctx_free_t),
    ("binding_ctx_free", ecs_ctx_free_t),
    ("lifecycle_ctx_free", ecs_ctx_free_t),
]

struct_ecs_type_info_t.__slots__ = [
    "size",
    "alignment",
    "hooks",
    "component",
    "name",
]
struct_ecs_type_info_t._fields_ = [
    ("size", ecs_size_t),
    ("alignment", ecs_size_t),
    ("hooks", ecs_type_hooks_t),
    ("component", ecs_entity_t),
    ("name", String),
]


# vendor/flecs/flecs.h: 3725
class struct_ecs_data_t(Structure):
    pass


ecs_data_t = struct_ecs_data_t  # vendor/flecs/flecs.h: 3725


# vendor/flecs/flecs.h: 3728
class struct_ecs_query_cache_match_t(Structure):
    pass


ecs_query_cache_match_t = struct_ecs_query_cache_match_t  # vendor/flecs/flecs.h: 3728


# vendor/flecs/flecs.h: 3731
class struct_ecs_query_cache_group_t(Structure):
    pass


ecs_query_cache_group_t = struct_ecs_query_cache_group_t  # vendor/flecs/flecs.h: 3731


# vendor/flecs/flecs.h: 3739
class struct_ecs_event_id_record_t(Structure):
    pass


# vendor/flecs/flecs.h: 3744
class struct_ecs_event_record_t(Structure):
    pass


struct_ecs_event_record_t.__slots__ = [
    "any",
    "wildcard",
    "wildcard_pair",
    "event_ids",
    "event",
]
struct_ecs_event_record_t._fields_ = [
    ("any", POINTER(struct_ecs_event_id_record_t)),
    ("wildcard", POINTER(struct_ecs_event_id_record_t)),
    ("wildcard_pair", POINTER(struct_ecs_event_id_record_t)),
    ("event_ids", ecs_map_t),
    ("event", ecs_entity_t),
]

ecs_event_record_t = struct_ecs_event_record_t  # vendor/flecs/flecs.h: 3744

struct_ecs_observable_t.__slots__ = [
    "on_add",
    "on_remove",
    "on_set",
    "on_wildcard",
    "events",
    "last_observer_id",
]
struct_ecs_observable_t._fields_ = [
    ("on_add", ecs_event_record_t),
    ("on_remove", ecs_event_record_t),
    ("on_set", ecs_event_record_t),
    ("on_wildcard", ecs_event_record_t),
    ("events", ecs_sparse_t),
    ("last_observer_id", uint64_t),
]


# vendor/flecs/flecs.h: 3760
class struct_ecs_table_range_t(Structure):
    pass


struct_ecs_table_range_t.__slots__ = [
    "table",
    "offset",
    "count",
]
struct_ecs_table_range_t._fields_ = [
    ("table", POINTER(ecs_table_t)),
    ("offset", c_int32),
    ("count", c_int32),
]

ecs_table_range_t = struct_ecs_table_range_t  # vendor/flecs/flecs.h: 3760


# vendor/flecs/flecs.h: 3771
class struct_ecs_var_t(Structure):
    pass


struct_ecs_var_t.__slots__ = [
    "range",
    "entity",
]
struct_ecs_var_t._fields_ = [
    ("range", ecs_table_range_t),
    ("entity", ecs_entity_t),
]

ecs_var_t = struct_ecs_var_t  # vendor/flecs/flecs.h: 3771

struct_ecs_ref_t.__slots__ = [
    "entity",
    "id",
    "table_id",
    "table_version_fast",
    "table_version",
    "record",
    "ptr",
]
struct_ecs_ref_t._fields_ = [
    ("entity", ecs_entity_t),
    ("id", ecs_entity_t),
    ("table_id", uint64_t),
    ("table_version_fast", uint32_t),
    ("table_version", uint16_t),
    ("record", POINTER(ecs_record_t)),
    ("ptr", POINTER(None)),
]


# vendor/flecs/flecs.h: 3789
class struct_ecs_page_iter_t(Structure):
    pass


struct_ecs_page_iter_t.__slots__ = [
    "offset",
    "limit",
    "remaining",
]
struct_ecs_page_iter_t._fields_ = [
    ("offset", c_int32),
    ("limit", c_int32),
    ("remaining", c_int32),
]

ecs_page_iter_t = struct_ecs_page_iter_t  # vendor/flecs/flecs.h: 3789


# vendor/flecs/flecs.h: 3795
class struct_ecs_worker_iter_t(Structure):
    pass


struct_ecs_worker_iter_t.__slots__ = [
    "index",
    "count",
]
struct_ecs_worker_iter_t._fields_ = [
    ("index", c_int32),
    ("count", c_int32),
]

ecs_worker_iter_t = struct_ecs_worker_iter_t  # vendor/flecs/flecs.h: 3795


# vendor/flecs/flecs.h: 4409
class struct_ecs_table_cache_hdr_t(Structure):
    pass


# vendor/flecs/flecs.h: 3802
class struct_ecs_table_cache_iter_t(Structure):
    pass


struct_ecs_table_cache_iter_t.__slots__ = [
    "cur",
    "next",
    "iter_fill",
    "iter_empty",
]
struct_ecs_table_cache_iter_t._fields_ = [
    ("cur", POINTER(struct_ecs_table_cache_hdr_t)),
    ("next", POINTER(struct_ecs_table_cache_hdr_t)),
    ("iter_fill", c_bool),
    ("iter_empty", c_bool),
]

ecs_table_cache_iter_t = struct_ecs_table_cache_iter_t  # vendor/flecs/flecs.h: 3802


# vendor/flecs/flecs.h: 3814
class struct_ecs_each_iter_t(Structure):
    pass


struct_ecs_each_iter_t.__slots__ = [
    "it",
    "ids",
    "sources",
    "sizes",
    "columns",
    "trs",
]
struct_ecs_each_iter_t._fields_ = [
    ("it", ecs_table_cache_iter_t),
    ("ids", ecs_id_t),
    ("sources", ecs_entity_t),
    ("sizes", ecs_size_t),
    ("columns", c_int32),
    ("trs", POINTER(ecs_table_record_t)),
]

ecs_each_iter_t = struct_ecs_each_iter_t  # vendor/flecs/flecs.h: 3814


# vendor/flecs/flecs.h: 3818
class struct_ecs_query_op_profile_t(Structure):
    pass


struct_ecs_query_op_profile_t.__slots__ = [
    "count",
]
struct_ecs_query_op_profile_t._fields_ = [
    ("count", c_int32 * int(2)),
]

ecs_query_op_profile_t = struct_ecs_query_op_profile_t  # vendor/flecs/flecs.h: 3818


# vendor/flecs/flecs.h: 3823
class struct_ecs_query_var_t(Structure):
    pass


# vendor/flecs/flecs.h: 3824
class struct_ecs_query_op_t(Structure):
    pass


# vendor/flecs/flecs.h: 3825
class struct_ecs_query_op_ctx_t(Structure):
    pass


# vendor/flecs/flecs.h: 3839
class struct_ecs_query_iter_t(Structure):
    pass


struct_ecs_query_iter_t.__slots__ = [
    "vars",
    "query_vars",
    "ops",
    "op_ctx",
    "written",
    "group",
    "tables",
    "all_tables",
    "elem",
    "cur",
    "all_cur",
    "profile",
    "op",
    "iter_single_group",
]
struct_ecs_query_iter_t._fields_ = [
    ("vars", POINTER(struct_ecs_var_t)),
    ("query_vars", POINTER(struct_ecs_query_var_t)),
    ("ops", POINTER(struct_ecs_query_op_t)),
    ("op_ctx", POINTER(struct_ecs_query_op_ctx_t)),
    ("written", POINTER(uint64_t)),
    ("group", POINTER(ecs_query_cache_group_t)),
    ("tables", POINTER(ecs_vec_t)),
    ("all_tables", POINTER(ecs_vec_t)),
    ("elem", POINTER(ecs_query_cache_match_t)),
    ("cur", c_int32),
    ("all_cur", c_int32),
    ("profile", POINTER(ecs_query_op_profile_t)),
    ("op", c_int16),
    ("iter_single_group", c_bool),
]

ecs_query_iter_t = struct_ecs_query_iter_t  # vendor/flecs/flecs.h: 3839


# vendor/flecs/flecs.h: 3844
class union_anon_9(Union):
    pass


union_anon_9.__slots__ = [
    "query",
    "page",
    "worker",
    "each",
]
union_anon_9._fields_ = [
    ("query", ecs_query_iter_t),
    ("page", ecs_page_iter_t),
    ("worker", ecs_worker_iter_t),
    ("each", ecs_each_iter_t),
]


# vendor/flecs/flecs.h: 3853
class struct_ecs_iter_private_t(Structure):
    pass


struct_ecs_iter_private_t.__slots__ = [
    "iter",
    "entity_iter",
    "stack_cursor",
]
struct_ecs_iter_private_t._fields_ = [
    ("iter", union_anon_9),
    ("entity_iter", POINTER(None)),
    ("stack_cursor", POINTER(ecs_stack_cursor_t)),
]

ecs_iter_private_t = struct_ecs_iter_private_t  # vendor/flecs/flecs.h: 3853


# vendor/flecs/flecs.h: 3860
class struct_ecs_commands_t(Structure):
    pass


struct_ecs_commands_t.__slots__ = [
    "queue",
    "stack",
    "entries",
]
struct_ecs_commands_t._fields_ = [
    ("queue", ecs_vec_t),
    ("stack", ecs_stack_t),
    ("entries", ecs_sparse_t),
]

ecs_commands_t = struct_ecs_commands_t  # vendor/flecs/flecs.h: 3860

# vendor/flecs/flecs.h: 3906
for _lib in _libs.values():
    if not _lib.has("flecs_module_path_from_c", "cdecl"):
        continue
    flecs_module_path_from_c = _lib.get("flecs_module_path_from_c", "cdecl")
    flecs_module_path_from_c.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        flecs_module_path_from_c.restype = ReturnString
    else:
        flecs_module_path_from_c.restype = String
        flecs_module_path_from_c.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 3916
for _lib in _libs.values():
    if not _lib.has("flecs_default_ctor", "cdecl"):
        continue
    flecs_default_ctor = _lib.get("flecs_default_ctor", "cdecl")
    flecs_default_ctor.argtypes = [POINTER(None), c_int32, POINTER(ecs_type_info_t)]
    flecs_default_ctor.restype = None
    break

# vendor/flecs/flecs.h: 3928
for _lib in _libs.values():
    if not _lib.has("flecs_vasprintf", "cdecl"):
        continue
    flecs_vasprintf = _lib.get("flecs_vasprintf", "cdecl")
    flecs_vasprintf.argtypes = [String, c_void_p]
    if sizeof(c_int) == sizeof(c_void_p):
        flecs_vasprintf.restype = ReturnString
    else:
        flecs_vasprintf.restype = String
        flecs_vasprintf.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 3938
for _lib in _libs.values():
    if _lib.has("flecs_asprintf", "cdecl"):
        _func = _lib.get("flecs_asprintf", "cdecl")
        _restype = String
        _errcheck = None
        _argtypes = [String]
        flecs_asprintf = _variadic_function(_func, _restype, _argtypes, _errcheck)

# vendor/flecs/flecs.h: 3951
for _lib in _libs.values():
    if not _lib.has("flecs_chresc", "cdecl"):
        continue
    flecs_chresc = _lib.get("flecs_chresc", "cdecl")
    flecs_chresc.argtypes = [String, c_char, c_char]
    if sizeof(c_int) == sizeof(c_void_p):
        flecs_chresc.restype = ReturnString
    else:
        flecs_chresc.restype = String
        flecs_chresc.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 3963
for _lib in _libs.values():
    if not _lib.has("flecs_chrparse", "cdecl"):
        continue
    flecs_chrparse = _lib.get("flecs_chrparse", "cdecl")
    flecs_chrparse.argtypes = [String, String]
    flecs_chrparse.restype = c_char_p
    break

# vendor/flecs/flecs.h: 3980
for _lib in _libs.values():
    if not _lib.has("flecs_stresc", "cdecl"):
        continue
    flecs_stresc = _lib.get("flecs_stresc", "cdecl")
    flecs_stresc.argtypes = [String, ecs_size_t, c_char, String]
    flecs_stresc.restype = ecs_size_t
    break

# vendor/flecs/flecs.h: 3995
for _lib in _libs.values():
    if not _lib.has("flecs_astresc", "cdecl"):
        continue
    flecs_astresc = _lib.get("flecs_astresc", "cdecl")
    flecs_astresc.argtypes = [c_char, String]
    if sizeof(c_int) == sizeof(c_void_p):
        flecs_astresc.restype = ReturnString
    else:
        flecs_astresc.restype = String
        flecs_astresc.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 4006
for _lib in _libs.values():
    if not _lib.has("flecs_parse_ws_eol", "cdecl"):
        continue
    flecs_parse_ws_eol = _lib.get("flecs_parse_ws_eol", "cdecl")
    flecs_parse_ws_eol.argtypes = [String]
    flecs_parse_ws_eol.restype = c_char_p
    break

# vendor/flecs/flecs.h: 4018
for _lib in _libs.values():
    if not _lib.has("flecs_parse_digit", "cdecl"):
        continue
    flecs_parse_digit = _lib.get("flecs_parse_digit", "cdecl")
    flecs_parse_digit.argtypes = [String, String]
    flecs_parse_digit.restype = c_char_p
    break

# vendor/flecs/flecs.h: 4024
for _lib in _libs.values():
    if not _lib.has("flecs_to_snake_case", "cdecl"):
        continue
    flecs_to_snake_case = _lib.get("flecs_to_snake_case", "cdecl")
    flecs_to_snake_case.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        flecs_to_snake_case.restype = ReturnString
    else:
        flecs_to_snake_case.restype = String
        flecs_to_snake_case.errcheck = ReturnString
    break


# vendor/flecs/flecs.h: 4051
class struct_ecs_suspend_readonly_state_t(Structure):
    pass


struct_ecs_suspend_readonly_state_t.__slots__ = [
    "is_readonly",
    "is_deferred",
    "cmd_flushing",
    "defer_count",
    "scope",
    "with",
    "cmd_stack",
    "cmd",
    "stage",
]
struct_ecs_suspend_readonly_state_t._fields_ = [
    ("is_readonly", c_bool),
    ("is_deferred", c_bool),
    ("cmd_flushing", c_bool),
    ("defer_count", c_int32),
    ("scope", ecs_entity_t),
    ("with", ecs_entity_t),
    ("cmd_stack", ecs_commands_t * int(2)),
    ("cmd", POINTER(ecs_commands_t)),
    ("stage", POINTER(ecs_stage_t)),
]

ecs_suspend_readonly_state_t = (
    struct_ecs_suspend_readonly_state_t  # vendor/flecs/flecs.h: 4051
)

# vendor/flecs/flecs.h: 4054
for _lib in _libs.values():
    if not _lib.has("flecs_suspend_readonly", "cdecl"):
        continue
    flecs_suspend_readonly = _lib.get("flecs_suspend_readonly", "cdecl")
    flecs_suspend_readonly.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_suspend_readonly_state_t),
    ]
    flecs_suspend_readonly.restype = POINTER(ecs_world_t)
    break

# vendor/flecs/flecs.h: 4059
for _lib in _libs.values():
    if not _lib.has("flecs_resume_readonly", "cdecl"):
        continue
    flecs_resume_readonly = _lib.get("flecs_resume_readonly", "cdecl")
    flecs_resume_readonly.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_suspend_readonly_state_t),
    ]
    flecs_resume_readonly.restype = None
    break

# vendor/flecs/flecs.h: 4069
for _lib in _libs.values():
    if not _lib.has("flecs_table_observed_count", "cdecl"):
        continue
    flecs_table_observed_count = _lib.get("flecs_table_observed_count", "cdecl")
    flecs_table_observed_count.argtypes = [POINTER(ecs_table_t)]
    flecs_table_observed_count.restype = c_int32
    break

# vendor/flecs/flecs.h: 4077
for _lib in _libs.values():
    if not _lib.has("flecs_dump_backtrace", "cdecl"):
        continue
    flecs_dump_backtrace = _lib.get("flecs_dump_backtrace", "cdecl")
    flecs_dump_backtrace.argtypes = [POINTER(None)]
    flecs_dump_backtrace.restype = None
    break

# vendor/flecs/flecs.h: 4086
for _lib in _libs.values():
    if not _lib.has("flecs_poly_claim_", "cdecl"):
        continue
    flecs_poly_claim_ = _lib.get("flecs_poly_claim_", "cdecl")
    flecs_poly_claim_.argtypes = [POINTER(ecs_poly_t)]
    flecs_poly_claim_.restype = c_int32
    break

# vendor/flecs/flecs.h: 4095
for _lib in _libs.values():
    if not _lib.has("flecs_poly_release_", "cdecl"):
        continue
    flecs_poly_release_ = _lib.get("flecs_poly_release_", "cdecl")
    flecs_poly_release_.argtypes = [POINTER(ecs_poly_t)]
    flecs_poly_release_.restype = c_int32
    break

# vendor/flecs/flecs.h: 4110
for _lib in _libs.values():
    if not _lib.has("flecs_poly_refcount", "cdecl"):
        continue
    flecs_poly_refcount = _lib.get("flecs_poly_refcount", "cdecl")
    flecs_poly_refcount.argtypes = [POINTER(ecs_poly_t)]
    flecs_poly_refcount.restype = c_int32
    break

# vendor/flecs/flecs.h: 4120
for _lib in _libs.values():
    if not _lib.has("flecs_component_ids_index_get", "cdecl"):
        continue
    flecs_component_ids_index_get = _lib.get("flecs_component_ids_index_get", "cdecl")
    flecs_component_ids_index_get.argtypes = []
    flecs_component_ids_index_get.restype = c_int32
    break

# vendor/flecs/flecs.h: 4129
for _lib in _libs.values():
    if not _lib.has("flecs_component_ids_get", "cdecl"):
        continue
    flecs_component_ids_get = _lib.get("flecs_component_ids_get", "cdecl")
    flecs_component_ids_get.argtypes = [POINTER(ecs_world_t), c_int32]
    flecs_component_ids_get.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 4142
for _lib in _libs.values():
    if not _lib.has("flecs_component_ids_get_alive", "cdecl"):
        continue
    flecs_component_ids_get_alive = _lib.get("flecs_component_ids_get_alive", "cdecl")
    flecs_component_ids_get_alive.argtypes = [POINTER(ecs_world_t), c_int32]
    flecs_component_ids_get_alive.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 4153
for _lib in _libs.values():
    if not _lib.has("flecs_component_ids_set", "cdecl"):
        continue
    flecs_component_ids_set = _lib.get("flecs_component_ids_set", "cdecl")
    flecs_component_ids_set.argtypes = [POINTER(ecs_world_t), c_int32, ecs_entity_t]
    flecs_component_ids_set.restype = None
    break

# vendor/flecs/flecs.h: 4166
for _lib in _libs.values():
    if not _lib.has("flecs_query_trivial_cached_next", "cdecl"):
        continue
    flecs_query_trivial_cached_next = _lib.get(
        "flecs_query_trivial_cached_next", "cdecl"
    )
    flecs_query_trivial_cached_next.argtypes = [POINTER(ecs_iter_t)]
    flecs_query_trivial_cached_next.restype = c_bool
    break


# vendor/flecs/flecs.h: 4253
class struct_anon_10(Structure):
    pass


struct_anon_10.__slots__ = [
    "keys",
    "values",
]
struct_anon_10._fields_ = [
    ("keys", ecs_vec_t),
    ("values", ecs_vec_t),
]

ecs_hm_bucket_t = struct_anon_10  # vendor/flecs/flecs.h: 4253


# vendor/flecs/flecs.h: 4263
class struct_anon_11(Structure):
    pass


struct_anon_11.__slots__ = [
    "hash",
    "compare",
    "key_size",
    "value_size",
    "hashmap_allocator",
    "bucket_allocator",
    "impl",
]
struct_anon_11._fields_ = [
    ("hash", ecs_hash_value_action_t),
    ("compare", ecs_compare_action_t),
    ("key_size", ecs_size_t),
    ("value_size", ecs_size_t),
    ("hashmap_allocator", POINTER(ecs_block_allocator_t)),
    ("bucket_allocator", ecs_block_allocator_t),
    ("impl", ecs_map_t),
]

ecs_hashmap_t = struct_anon_11  # vendor/flecs/flecs.h: 4263


# vendor/flecs/flecs.h: 4269
class struct_anon_12(Structure):
    pass


struct_anon_12.__slots__ = [
    "it",
    "bucket",
    "index",
]
struct_anon_12._fields_ = [
    ("it", ecs_map_iter_t),
    ("bucket", POINTER(ecs_hm_bucket_t)),
    ("index", c_int32),
]

flecs_hashmap_iter_t = struct_anon_12  # vendor/flecs/flecs.h: 4269


# vendor/flecs/flecs.h: 4275
class struct_anon_13(Structure):
    pass


struct_anon_13.__slots__ = [
    "key",
    "value",
    "hash",
]
struct_anon_13._fields_ = [
    ("key", POINTER(None)),
    ("value", POINTER(None)),
    ("hash", uint64_t),
]

flecs_hashmap_result_t = struct_anon_13  # vendor/flecs/flecs.h: 4275

# vendor/flecs/flecs.h: 4278
for _lib in _libs.values():
    if not _lib.has("flecs_hashmap_init_", "cdecl"):
        continue
    flecs_hashmap_init_ = _lib.get("flecs_hashmap_init_", "cdecl")
    flecs_hashmap_init_.argtypes = [
        POINTER(ecs_hashmap_t),
        ecs_size_t,
        ecs_size_t,
        ecs_hash_value_action_t,
        ecs_compare_action_t,
        POINTER(ecs_allocator_t),
    ]
    flecs_hashmap_init_.restype = None
    break

# vendor/flecs/flecs.h: 4290
for _lib in _libs.values():
    if not _lib.has("flecs_hashmap_fini", "cdecl"):
        continue
    flecs_hashmap_fini = _lib.get("flecs_hashmap_fini", "cdecl")
    flecs_hashmap_fini.argtypes = [POINTER(ecs_hashmap_t)]
    flecs_hashmap_fini.restype = None
    break

# vendor/flecs/flecs.h: 4294
for _lib in _libs.values():
    if not _lib.has("flecs_hashmap_get_", "cdecl"):
        continue
    flecs_hashmap_get_ = _lib.get("flecs_hashmap_get_", "cdecl")
    flecs_hashmap_get_.argtypes = [
        POINTER(ecs_hashmap_t),
        ecs_size_t,
        POINTER(None),
        ecs_size_t,
    ]
    flecs_hashmap_get_.restype = POINTER(c_ubyte)
    flecs_hashmap_get_.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 4304
for _lib in _libs.values():
    if not _lib.has("flecs_hashmap_ensure_", "cdecl"):
        continue
    flecs_hashmap_ensure_ = _lib.get("flecs_hashmap_ensure_", "cdecl")
    flecs_hashmap_ensure_.argtypes = [
        POINTER(ecs_hashmap_t),
        ecs_size_t,
        POINTER(None),
        ecs_size_t,
    ]
    flecs_hashmap_ensure_.restype = flecs_hashmap_result_t
    break

# vendor/flecs/flecs.h: 4314
for _lib in _libs.values():
    if not _lib.has("flecs_hashmap_set_", "cdecl"):
        continue
    flecs_hashmap_set_ = _lib.get("flecs_hashmap_set_", "cdecl")
    flecs_hashmap_set_.argtypes = [
        POINTER(ecs_hashmap_t),
        ecs_size_t,
        POINTER(None),
        ecs_size_t,
        POINTER(None),
    ]
    flecs_hashmap_set_.restype = None
    break

# vendor/flecs/flecs.h: 4325
for _lib in _libs.values():
    if not _lib.has("flecs_hashmap_remove_", "cdecl"):
        continue
    flecs_hashmap_remove_ = _lib.get("flecs_hashmap_remove_", "cdecl")
    flecs_hashmap_remove_.argtypes = [
        POINTER(ecs_hashmap_t),
        ecs_size_t,
        POINTER(None),
        ecs_size_t,
    ]
    flecs_hashmap_remove_.restype = None
    break

# vendor/flecs/flecs.h: 4335
for _lib in _libs.values():
    if not _lib.has("flecs_hashmap_remove_w_hash_", "cdecl"):
        continue
    flecs_hashmap_remove_w_hash_ = _lib.get("flecs_hashmap_remove_w_hash_", "cdecl")
    flecs_hashmap_remove_w_hash_.argtypes = [
        POINTER(ecs_hashmap_t),
        ecs_size_t,
        POINTER(None),
        ecs_size_t,
        uint64_t,
    ]
    flecs_hashmap_remove_w_hash_.restype = None
    break

# vendor/flecs/flecs.h: 4346
for _lib in _libs.values():
    if not _lib.has("flecs_hashmap_get_bucket", "cdecl"):
        continue
    flecs_hashmap_get_bucket = _lib.get("flecs_hashmap_get_bucket", "cdecl")
    flecs_hashmap_get_bucket.argtypes = [POINTER(ecs_hashmap_t), uint64_t]
    flecs_hashmap_get_bucket.restype = POINTER(ecs_hm_bucket_t)
    break

# vendor/flecs/flecs.h: 4351
for _lib in _libs.values():
    if not _lib.has("flecs_hm_bucket_remove", "cdecl"):
        continue
    flecs_hm_bucket_remove = _lib.get("flecs_hm_bucket_remove", "cdecl")
    flecs_hm_bucket_remove.argtypes = [
        POINTER(ecs_hashmap_t),
        POINTER(ecs_hm_bucket_t),
        uint64_t,
        c_int32,
    ]
    flecs_hm_bucket_remove.restype = None
    break

# vendor/flecs/flecs.h: 4358
for _lib in _libs.values():
    if not _lib.has("flecs_hashmap_copy", "cdecl"):
        continue
    flecs_hashmap_copy = _lib.get("flecs_hashmap_copy", "cdecl")
    flecs_hashmap_copy.argtypes = [POINTER(ecs_hashmap_t), POINTER(ecs_hashmap_t)]
    flecs_hashmap_copy.restype = None
    break

# vendor/flecs/flecs.h: 4363
for _lib in _libs.values():
    if not _lib.has("flecs_hashmap_iter", "cdecl"):
        continue
    flecs_hashmap_iter = _lib.get("flecs_hashmap_iter", "cdecl")
    flecs_hashmap_iter.argtypes = [POINTER(ecs_hashmap_t)]
    flecs_hashmap_iter.restype = flecs_hashmap_iter_t
    break

# vendor/flecs/flecs.h: 4367
for _lib in _libs.values():
    if not _lib.has("flecs_hashmap_next_", "cdecl"):
        continue
    flecs_hashmap_next_ = _lib.get("flecs_hashmap_next_", "cdecl")
    flecs_hashmap_next_.argtypes = [
        POINTER(flecs_hashmap_iter_t),
        ecs_size_t,
        POINTER(None),
        ecs_size_t,
    ]
    flecs_hashmap_next_.restype = POINTER(c_ubyte)
    flecs_hashmap_next_.errcheck = lambda v, *a: cast(v, c_void_p)
    break

struct_ecs_record_t.__slots__ = [
    "cr",
    "table",
    "row",
    "dense",
]
struct_ecs_record_t._fields_ = [
    ("cr", POINTER(ecs_component_record_t)),
    ("table", POINTER(ecs_table_t)),
    ("row", uint32_t),
    ("dense", c_int32),
]


# vendor/flecs/flecs.h: 4410
class struct_ecs_table_cache_t(Structure):
    pass


struct_ecs_table_cache_hdr_t.__slots__ = [
    "cache",
    "table",
    "prev",
    "next",
]
struct_ecs_table_cache_hdr_t._fields_ = [
    ("cache", POINTER(struct_ecs_table_cache_t)),
    ("table", POINTER(ecs_table_t)),
    ("prev", POINTER(struct_ecs_table_cache_hdr_t)),
    ("next", POINTER(struct_ecs_table_cache_hdr_t)),
]

ecs_table_cache_hdr_t = struct_ecs_table_cache_hdr_t  # vendor/flecs/flecs.h: 4413

struct_ecs_table_record_t.__slots__ = [
    "hdr",
    "index",
    "count",
    "column",
]
struct_ecs_table_record_t._fields_ = [
    ("hdr", ecs_table_cache_hdr_t),
    ("index", c_int16),
    ("count", c_int16),
    ("column", c_int16),
]


# vendor/flecs/flecs.h: 4432
class struct_ecs_table_diff_t(Structure):
    pass


struct_ecs_table_diff_t.__slots__ = [
    "added",
    "removed",
    "added_flags",
    "removed_flags",
]
struct_ecs_table_diff_t._fields_ = [
    ("added", ecs_type_t),
    ("removed", ecs_type_t),
    ("added_flags", ecs_flags32_t),
    ("removed_flags", ecs_flags32_t),
]

ecs_table_diff_t = struct_ecs_table_diff_t  # vendor/flecs/flecs.h: 4432

# vendor/flecs/flecs.h: 4448
for _lib in _libs.values():
    if not _lib.has("ecs_record_find", "cdecl"):
        continue
    ecs_record_find = _lib.get("ecs_record_find", "cdecl")
    ecs_record_find.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_record_find.restype = POINTER(ecs_record_t)
    break

# vendor/flecs/flecs.h: 4459
for _lib in _libs.values():
    if not _lib.has("ecs_record_get_entity", "cdecl"):
        continue
    ecs_record_get_entity = _lib.get("ecs_record_get_entity", "cdecl")
    ecs_record_get_entity.argtypes = [POINTER(ecs_record_t)]
    ecs_record_get_entity.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 4481
for _lib in _libs.values():
    if not _lib.has("ecs_write_begin", "cdecl"):
        continue
    ecs_write_begin = _lib.get("ecs_write_begin", "cdecl")
    ecs_write_begin.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_write_begin.restype = POINTER(ecs_record_t)
    break

# vendor/flecs/flecs.h: 4492
for _lib in _libs.values():
    if not _lib.has("ecs_write_end", "cdecl"):
        continue
    ecs_write_end = _lib.get("ecs_write_end", "cdecl")
    ecs_write_end.argtypes = [POINTER(ecs_record_t)]
    ecs_write_end.restype = None
    break

# vendor/flecs/flecs.h: 4515
for _lib in _libs.values():
    if not _lib.has("ecs_read_begin", "cdecl"):
        continue
    ecs_read_begin = _lib.get("ecs_read_begin", "cdecl")
    ecs_read_begin.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_read_begin.restype = POINTER(ecs_record_t)
    break

# vendor/flecs/flecs.h: 4525
for _lib in _libs.values():
    if not _lib.has("ecs_read_end", "cdecl"):
        continue
    ecs_read_end = _lib.get("ecs_read_end", "cdecl")
    ecs_read_end.argtypes = [POINTER(ecs_record_t)]
    ecs_read_end.restype = None
    break

# vendor/flecs/flecs.h: 4544
for _lib in _libs.values():
    if not _lib.has("ecs_record_get_id", "cdecl"):
        continue
    ecs_record_get_id = _lib.get("ecs_record_get_id", "cdecl")
    ecs_record_get_id.argtypes = [POINTER(ecs_world_t), POINTER(ecs_record_t), ecs_id_t]
    ecs_record_get_id.restype = POINTER(c_ubyte)
    ecs_record_get_id.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 4558
for _lib in _libs.values():
    if not _lib.has("ecs_record_ensure_id", "cdecl"):
        continue
    ecs_record_ensure_id = _lib.get("ecs_record_ensure_id", "cdecl")
    ecs_record_ensure_id.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_record_t),
        ecs_id_t,
    ]
    ecs_record_ensure_id.restype = POINTER(c_ubyte)
    ecs_record_ensure_id.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 4571
for _lib in _libs.values():
    if not _lib.has("ecs_record_has_id", "cdecl"):
        continue
    ecs_record_has_id = _lib.get("ecs_record_has_id", "cdecl")
    ecs_record_has_id.argtypes = [POINTER(ecs_world_t), POINTER(ecs_record_t), ecs_id_t]
    ecs_record_has_id.restype = c_bool
    break

# vendor/flecs/flecs.h: 4593
for _lib in _libs.values():
    if not _lib.has("ecs_record_get_by_column", "cdecl"):
        continue
    ecs_record_get_by_column = _lib.get("ecs_record_get_by_column", "cdecl")
    ecs_record_get_by_column.argtypes = [POINTER(ecs_record_t), c_int32, c_size_t]
    ecs_record_get_by_column.restype = POINTER(c_ubyte)
    ecs_record_get_by_column.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 4605
for _lib in _libs.values():
    if not _lib.has("flecs_components_get", "cdecl"):
        continue
    flecs_components_get = _lib.get("flecs_components_get", "cdecl")
    flecs_components_get.argtypes = [POINTER(ecs_world_t), ecs_id_t]
    flecs_components_get.restype = POINTER(ecs_component_record_t)
    break

# vendor/flecs/flecs.h: 4615
for _lib in _libs.values():
    if not _lib.has("flecs_component_get_id", "cdecl"):
        continue
    flecs_component_get_id = _lib.get("flecs_component_get_id", "cdecl")
    flecs_component_get_id.argtypes = [POINTER(ecs_component_record_t)]
    flecs_component_get_id.restype = ecs_id_t
    break

# vendor/flecs/flecs.h: 4627
for _lib in _libs.values():
    if not _lib.has("flecs_component_get_table", "cdecl"):
        continue
    flecs_component_get_table = _lib.get("flecs_component_get_table", "cdecl")
    flecs_component_get_table.argtypes = [
        POINTER(ecs_component_record_t),
        POINTER(ecs_table_t),
    ]
    flecs_component_get_table.restype = POINTER(ecs_table_record_t)
    break

# vendor/flecs/flecs.h: 4653
for _lib in _libs.values():
    if not _lib.has("flecs_component_iter", "cdecl"):
        continue
    flecs_component_iter = _lib.get("flecs_component_iter", "cdecl")
    flecs_component_iter.argtypes = [
        POINTER(ecs_component_record_t),
        POINTER(ecs_table_cache_iter_t),
    ]
    flecs_component_iter.restype = c_bool
    break

# vendor/flecs/flecs.h: 4664
for _lib in _libs.values():
    if not _lib.has("flecs_component_next", "cdecl"):
        continue
    flecs_component_next = _lib.get("flecs_component_next", "cdecl")
    flecs_component_next.argtypes = [POINTER(ecs_table_cache_iter_t)]
    flecs_component_next.restype = POINTER(ecs_table_record_t)
    break


# vendor/flecs/flecs.h: 4671
class struct_ecs_table_records_t(Structure):
    pass


struct_ecs_table_records_t.__slots__ = [
    "array",
    "count",
]
struct_ecs_table_records_t._fields_ = [
    ("array", POINTER(ecs_table_record_t)),
    ("count", c_int32),
]

ecs_table_records_t = struct_ecs_table_records_t  # vendor/flecs/flecs.h: 4671

# vendor/flecs/flecs.h: 4680
for _lib in _libs.values():
    if not _lib.has("flecs_table_records", "cdecl"):
        continue
    flecs_table_records = _lib.get("flecs_table_records", "cdecl")
    flecs_table_records.argtypes = [POINTER(ecs_table_t)]
    flecs_table_records.restype = ecs_table_records_t
    break

# vendor/flecs/flecs.h: 4689
for _lib in _libs.values():
    if not _lib.has("flecs_table_record_get_component", "cdecl"):
        continue
    flecs_table_record_get_component = _lib.get(
        "flecs_table_record_get_component", "cdecl"
    )
    flecs_table_record_get_component.argtypes = [POINTER(ecs_table_record_t)]
    flecs_table_record_get_component.restype = POINTER(ecs_component_record_t)
    break

# vendor/flecs/flecs.h: 4699
for _lib in _libs.values():
    if not _lib.has("flecs_table_id", "cdecl"):
        continue
    flecs_table_id = _lib.get("flecs_table_id", "cdecl")
    flecs_table_id.argtypes = [POINTER(ecs_table_t)]
    flecs_table_id.restype = uint64_t
    break

# vendor/flecs/flecs.h: 4713
for _lib in _libs.values():
    if not _lib.has("flecs_table_traverse_add", "cdecl"):
        continue
    flecs_table_traverse_add = _lib.get("flecs_table_traverse_add", "cdecl")
    flecs_table_traverse_add.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_table_t),
        POINTER(ecs_id_t),
        POINTER(ecs_table_diff_t),
    ]
    flecs_table_traverse_add.restype = POINTER(ecs_table_t)
    break


# vendor/flecs/flecs.h: 4730
class struct_ecs_value_t(Structure):
    pass


struct_ecs_value_t.__slots__ = [
    "type",
    "ptr",
]
struct_ecs_value_t._fields_ = [
    ("type", ecs_entity_t),
    ("ptr", POINTER(None)),
]

ecs_value_t = struct_ecs_value_t  # vendor/flecs/flecs.h: 4730


# vendor/flecs/flecs.h: 4776
class struct_ecs_entity_desc_t(Structure):
    pass


struct_ecs_entity_desc_t.__slots__ = [
    "_canary",
    "id",
    "parent",
    "name",
    "sep",
    "root_sep",
    "symbol",
    "use_low_id",
    "add",
    "set",
    "add_expr",
]
struct_ecs_entity_desc_t._fields_ = [
    ("_canary", c_int32),
    ("id", ecs_entity_t),
    ("parent", ecs_entity_t),
    ("name", String),
    ("sep", String),
    ("root_sep", String),
    ("symbol", String),
    ("use_low_id", c_bool),
    ("add", POINTER(ecs_id_t)),
    ("set", POINTER(ecs_value_t)),
    ("add_expr", String),
]

ecs_entity_desc_t = struct_ecs_entity_desc_t  # vendor/flecs/flecs.h: 4776


# vendor/flecs/flecs.h: 4806
class struct_ecs_bulk_desc_t(Structure):
    pass


struct_ecs_bulk_desc_t.__slots__ = [
    "_canary",
    "entities",
    "count",
    "ids",
    "data",
    "table",
]
struct_ecs_bulk_desc_t._fields_ = [
    ("_canary", c_int32),
    ("entities", POINTER(ecs_entity_t)),
    ("count", c_int32),
    ("ids", ecs_id_t * int(32)),
    ("data", POINTER(POINTER(None))),
    ("table", POINTER(ecs_table_t)),
]

ecs_bulk_desc_t = struct_ecs_bulk_desc_t  # vendor/flecs/flecs.h: 4806


# vendor/flecs/flecs.h: 4820
class struct_ecs_component_desc_t(Structure):
    pass


struct_ecs_component_desc_t.__slots__ = [
    "_canary",
    "entity",
    "type",
]
struct_ecs_component_desc_t._fields_ = [
    ("_canary", c_int32),
    ("entity", ecs_entity_t),
    ("type", ecs_type_info_t),
]

ecs_component_desc_t = struct_ecs_component_desc_t  # vendor/flecs/flecs.h: 4820

struct_ecs_iter_t.__slots__ = [
    "world",
    "real_world",
    "offset",
    "count",
    "entities",
    "ptrs",
    "trs",
    "sizes",
    "table",
    "other_table",
    "ids",
    "sources",
    "constrained_vars",
    "set_fields",
    "ref_fields",
    "row_fields",
    "up_fields",
    "system",
    "event",
    "event_id",
    "event_cur",
    "field_count",
    "term_index",
    "query",
    "param",
    "ctx",
    "binding_ctx",
    "callback_ctx",
    "run_ctx",
    "delta_time",
    "delta_system_time",
    "frame_offset",
    "flags",
    "interrupted_by",
    "priv_",
    "next",
    "callback",
    "fini",
    "chain_it",
]
struct_ecs_iter_t._fields_ = [
    ("world", POINTER(ecs_world_t)),
    ("real_world", POINTER(ecs_world_t)),
    ("offset", c_int32),
    ("count", c_int32),
    ("entities", POINTER(ecs_entity_t)),
    ("ptrs", POINTER(POINTER(None))),
    ("trs", POINTER(POINTER(ecs_table_record_t))),
    ("sizes", POINTER(ecs_size_t)),
    ("table", POINTER(ecs_table_t)),
    ("other_table", POINTER(ecs_table_t)),
    ("ids", POINTER(ecs_id_t)),
    ("sources", POINTER(ecs_entity_t)),
    ("constrained_vars", ecs_flags64_t),
    ("set_fields", ecs_flags32_t),
    ("ref_fields", ecs_flags32_t),
    ("row_fields", ecs_flags32_t),
    ("up_fields", ecs_flags32_t),
    ("system", ecs_entity_t),
    ("event", ecs_entity_t),
    ("event_id", ecs_id_t),
    ("event_cur", c_int32),
    ("field_count", c_int8),
    ("term_index", c_int8),
    ("query", POINTER(ecs_query_t)),
    ("param", POINTER(None)),
    ("ctx", POINTER(None)),
    ("binding_ctx", POINTER(None)),
    ("callback_ctx", POINTER(None)),
    ("run_ctx", POINTER(None)),
    ("delta_time", c_float),
    ("delta_system_time", c_float),
    ("frame_offset", c_int32),
    ("flags", ecs_flags32_t),
    ("interrupted_by", ecs_entity_t),
    ("priv_", ecs_iter_private_t),
    ("next", ecs_iter_next_action_t),
    ("callback", ecs_iter_action_t),
    ("fini", ecs_iter_fini_action_t),
    ("chain_it", POINTER(ecs_iter_t)),
]


# vendor/flecs/flecs.h: 5037
class struct_ecs_query_desc_t(Structure):
    pass


struct_ecs_query_desc_t.__slots__ = [
    "_canary",
    "terms",
    "expr",
    "cache_kind",
    "flags",
    "order_by_callback",
    "order_by_table_callback",
    "order_by",
    "group_by",
    "group_by_callback",
    "on_group_create",
    "on_group_delete",
    "group_by_ctx",
    "group_by_ctx_free",
    "ctx",
    "binding_ctx",
    "ctx_free",
    "binding_ctx_free",
    "entity",
]
struct_ecs_query_desc_t._fields_ = [
    ("_canary", c_int32),
    ("terms", ecs_term_t * int(32)),
    ("expr", String),
    ("cache_kind", ecs_query_cache_kind_t),
    ("flags", ecs_flags32_t),
    ("order_by_callback", ecs_order_by_action_t),
    ("order_by_table_callback", ecs_sort_table_action_t),
    ("order_by", ecs_entity_t),
    ("group_by", ecs_id_t),
    ("group_by_callback", ecs_group_by_action_t),
    ("on_group_create", ecs_group_create_action_t),
    ("on_group_delete", ecs_group_delete_action_t),
    ("group_by_ctx", POINTER(None)),
    ("group_by_ctx_free", ecs_ctx_free_t),
    ("ctx", POINTER(None)),
    ("binding_ctx", POINTER(None)),
    ("ctx_free", ecs_ctx_free_t),
    ("binding_ctx_free", ecs_ctx_free_t),
    ("entity", ecs_entity_t),
]

ecs_query_desc_t = struct_ecs_query_desc_t  # vendor/flecs/flecs.h: 5037


# vendor/flecs/flecs.h: 5099
class struct_ecs_observer_desc_t(Structure):
    pass


struct_ecs_observer_desc_t.__slots__ = [
    "_canary",
    "entity",
    "query",
    "events",
    "yield_existing",
    "callback",
    "run",
    "ctx",
    "ctx_free",
    "callback_ctx",
    "callback_ctx_free",
    "run_ctx",
    "run_ctx_free",
    "observable",
    "last_event_id",
    "term_index_",
    "flags_",
]
struct_ecs_observer_desc_t._fields_ = [
    ("_canary", c_int32),
    ("entity", ecs_entity_t),
    ("query", ecs_query_desc_t),
    ("events", ecs_entity_t * int(8)),
    ("yield_existing", c_bool),
    ("callback", ecs_iter_action_t),
    ("run", ecs_run_action_t),
    ("ctx", POINTER(None)),
    ("ctx_free", ecs_ctx_free_t),
    ("callback_ctx", POINTER(None)),
    ("callback_ctx_free", ecs_ctx_free_t),
    ("run_ctx", POINTER(None)),
    ("run_ctx_free", ecs_ctx_free_t),
    ("observable", POINTER(ecs_poly_t)),
    ("last_event_id", POINTER(c_int32)),
    ("term_index_", c_int8),
    ("flags_", ecs_flags32_t),
]

ecs_observer_desc_t = struct_ecs_observer_desc_t  # vendor/flecs/flecs.h: 5099


# vendor/flecs/flecs.h: 5148
class struct_ecs_event_desc_t(Structure):
    pass


struct_ecs_event_desc_t.__slots__ = [
    "event",
    "ids",
    "table",
    "other_table",
    "offset",
    "count",
    "entity",
    "param",
    "const_param",
    "observable",
    "flags",
]
struct_ecs_event_desc_t._fields_ = [
    ("event", ecs_entity_t),
    ("ids", POINTER(ecs_type_t)),
    ("table", POINTER(ecs_table_t)),
    ("other_table", POINTER(ecs_table_t)),
    ("offset", c_int32),
    ("count", c_int32),
    ("entity", ecs_entity_t),
    ("param", POINTER(None)),
    ("const_param", POINTER(None)),
    ("observable", POINTER(ecs_poly_t)),
    ("flags", ecs_flags32_t),
]

ecs_event_desc_t = struct_ecs_event_desc_t  # vendor/flecs/flecs.h: 5148


# vendor/flecs/flecs.h: 5169
class struct_ecs_build_info_t(Structure):
    pass


struct_ecs_build_info_t.__slots__ = [
    "compiler",
    "addons",
    "version",
    "version_major",
    "version_minor",
    "version_patch",
    "debug",
    "sanitize",
    "perf_trace",
]
struct_ecs_build_info_t._fields_ = [
    ("compiler", String),
    ("addons", POINTER(POINTER(c_char))),
    ("version", String),
    ("version_major", c_int16),
    ("version_minor", c_int16),
    ("version_patch", c_int16),
    ("debug", c_bool),
    ("sanitize", c_bool),
    ("perf_trace", c_bool),
]

ecs_build_info_t = struct_ecs_build_info_t  # vendor/flecs/flecs.h: 5169


# vendor/flecs/flecs.h: 5209
class struct_anon_14(Structure):
    pass


struct_anon_14.__slots__ = [
    "add_count",
    "remove_count",
    "delete_count",
    "clear_count",
    "set_count",
    "ensure_count",
    "modified_count",
    "discard_count",
    "event_count",
    "other_count",
    "batched_entity_count",
    "batched_command_count",
]
struct_anon_14._fields_ = [
    ("add_count", c_int64),
    ("remove_count", c_int64),
    ("delete_count", c_int64),
    ("clear_count", c_int64),
    ("set_count", c_int64),
    ("ensure_count", c_int64),
    ("modified_count", c_int64),
    ("discard_count", c_int64),
    ("event_count", c_int64),
    ("other_count", c_int64),
    ("batched_entity_count", c_int64),
    ("batched_command_count", c_int64),
]


# vendor/flecs/flecs.h: 5228
class struct_ecs_world_info_t(Structure):
    pass


struct_ecs_world_info_t.__slots__ = [
    "last_component_id",
    "min_id",
    "max_id",
    "delta_time_raw",
    "delta_time",
    "time_scale",
    "target_fps",
    "frame_time_total",
    "system_time_total",
    "emit_time_total",
    "merge_time_total",
    "rematch_time_total",
    "world_time_total",
    "world_time_total_raw",
    "frame_count_total",
    "merge_count_total",
    "eval_comp_monitors_total",
    "rematch_count_total",
    "id_create_total",
    "id_delete_total",
    "table_create_total",
    "table_delete_total",
    "pipeline_build_count_total",
    "systems_ran_frame",
    "observers_ran_frame",
    "tag_id_count",
    "component_id_count",
    "pair_id_count",
    "table_count",
    "cmd",
    "name_prefix",
]
struct_ecs_world_info_t._fields_ = [
    ("last_component_id", ecs_entity_t),
    ("min_id", ecs_entity_t),
    ("max_id", ecs_entity_t),
    ("delta_time_raw", c_float),
    ("delta_time", c_float),
    ("time_scale", c_float),
    ("target_fps", c_float),
    ("frame_time_total", c_float),
    ("system_time_total", c_float),
    ("emit_time_total", c_float),
    ("merge_time_total", c_float),
    ("rematch_time_total", c_float),
    ("world_time_total", c_double),
    ("world_time_total_raw", c_double),
    ("frame_count_total", c_int64),
    ("merge_count_total", c_int64),
    ("eval_comp_monitors_total", c_int64),
    ("rematch_count_total", c_int64),
    ("id_create_total", c_int64),
    ("id_delete_total", c_int64),
    ("table_create_total", c_int64),
    ("table_delete_total", c_int64),
    ("pipeline_build_count_total", c_int64),
    ("systems_ran_frame", c_int64),
    ("observers_ran_frame", c_int64),
    ("tag_id_count", c_int32),
    ("component_id_count", c_int32),
    ("pair_id_count", c_int32),
    ("table_count", c_int32),
    ("cmd", struct_anon_14),
    ("name_prefix", String),
]

ecs_world_info_t = struct_ecs_world_info_t  # vendor/flecs/flecs.h: 5228


# vendor/flecs/flecs.h: 5236
class struct_ecs_query_group_info_t(Structure):
    pass


struct_ecs_query_group_info_t.__slots__ = [
    "id",
    "match_count",
    "table_count",
    "ctx",
]
struct_ecs_query_group_info_t._fields_ = [
    ("id", uint64_t),
    ("match_count", c_int32),
    ("table_count", c_int32),
    ("ctx", POINTER(None)),
]

ecs_query_group_info_t = struct_ecs_query_group_info_t  # vendor/flecs/flecs.h: 5236


# vendor/flecs/flecs.h: 5254
class struct_EcsIdentifier(Structure):
    pass


struct_EcsIdentifier.__slots__ = [
    "value",
    "length",
    "hash",
    "index_hash",
    "index",
]
struct_EcsIdentifier._fields_ = [
    ("value", String),
    ("length", ecs_size_t),
    ("hash", uint64_t),
    ("index_hash", uint64_t),
    ("index", POINTER(ecs_hashmap_t)),
]

EcsIdentifier = struct_EcsIdentifier  # vendor/flecs/flecs.h: 5254


# vendor/flecs/flecs.h: 5260
class struct_EcsComponent(Structure):
    pass


struct_EcsComponent.__slots__ = [
    "size",
    "alignment",
]
struct_EcsComponent._fields_ = [
    ("size", ecs_size_t),
    ("alignment", ecs_size_t),
]

EcsComponent = struct_EcsComponent  # vendor/flecs/flecs.h: 5260


# vendor/flecs/flecs.h: 5265
class struct_EcsPoly(Structure):
    pass


struct_EcsPoly.__slots__ = [
    "poly",
]
struct_EcsPoly._fields_ = [
    ("poly", POINTER(ecs_poly_t)),
]

EcsPoly = struct_EcsPoly  # vendor/flecs/flecs.h: 5265


# vendor/flecs/flecs.h: 5274
class struct_EcsDefaultChildComponent(Structure):
    pass


struct_EcsDefaultChildComponent.__slots__ = [
    "component",
]
struct_EcsDefaultChildComponent._fields_ = [
    ("component", ecs_id_t),
]

EcsDefaultChildComponent = struct_EcsDefaultChildComponent  # vendor/flecs/flecs.h: 5274

# vendor/flecs/flecs.h: 5320
for _lib in _libs.values():
    try:
        ECS_PAIR = (ecs_id_t).in_dll(_lib, "ECS_PAIR")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5323
for _lib in _libs.values():
    try:
        ECS_AUTO_OVERRIDE = (ecs_id_t).in_dll(_lib, "ECS_AUTO_OVERRIDE")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5326
for _lib in _libs.values():
    try:
        ECS_TOGGLE = (ecs_id_t).in_dll(_lib, "ECS_TOGGLE")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5338
for _lib in _libs.values():
    try:
        FLECS_IDEcsComponentID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsComponentID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5341
for _lib in _libs.values():
    try:
        FLECS_IDEcsIdentifierID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsIdentifierID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 5344
for _lib in _libs.values():
    try:
        FLECS_IDEcsPolyID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsPolyID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5347
for _lib in _libs.values():
    try:
        FLECS_IDEcsDefaultChildComponentID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsDefaultChildComponentID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 5350
for _lib in _libs.values():
    try:
        EcsQuery = (ecs_entity_t).in_dll(_lib, "EcsQuery")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5353
for _lib in _libs.values():
    try:
        EcsObserver = (ecs_entity_t).in_dll(_lib, "EcsObserver")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5356
for _lib in _libs.values():
    try:
        EcsSystem = (ecs_entity_t).in_dll(_lib, "EcsSystem")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5359
for _lib in _libs.values():
    try:
        FLECS_IDEcsTickSourceID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsTickSourceID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 5362
for _lib in _libs.values():
    try:
        FLECS_IDEcsPipelineQueryID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsPipelineQueryID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 5365
for _lib in _libs.values():
    try:
        FLECS_IDEcsTimerID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsTimerID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5368
for _lib in _libs.values():
    try:
        FLECS_IDEcsRateFilterID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsRateFilterID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 5371
for _lib in _libs.values():
    try:
        EcsFlecs = (ecs_entity_t).in_dll(_lib, "EcsFlecs")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5374
for _lib in _libs.values():
    try:
        EcsFlecsCore = (ecs_entity_t).in_dll(_lib, "EcsFlecsCore")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5377
for _lib in _libs.values():
    try:
        EcsWorld = (ecs_entity_t).in_dll(_lib, "EcsWorld")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5380
for _lib in _libs.values():
    try:
        EcsWildcard = (ecs_entity_t).in_dll(_lib, "EcsWildcard")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5383
for _lib in _libs.values():
    try:
        EcsAny = (ecs_entity_t).in_dll(_lib, "EcsAny")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5386
for _lib in _libs.values():
    try:
        EcsThis = (ecs_entity_t).in_dll(_lib, "EcsThis")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5389
for _lib in _libs.values():
    try:
        EcsVariable = (ecs_entity_t).in_dll(_lib, "EcsVariable")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5401
for _lib in _libs.values():
    try:
        EcsTransitive = (ecs_entity_t).in_dll(_lib, "EcsTransitive")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5410
for _lib in _libs.values():
    try:
        EcsReflexive = (ecs_entity_t).in_dll(_lib, "EcsReflexive")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5422
for _lib in _libs.values():
    try:
        EcsFinal = (ecs_entity_t).in_dll(_lib, "EcsFinal")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5429
for _lib in _libs.values():
    try:
        EcsInheritable = (ecs_entity_t).in_dll(_lib, "EcsInheritable")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5432
for _lib in _libs.values():
    try:
        EcsOnInstantiate = (ecs_entity_t).in_dll(_lib, "EcsOnInstantiate")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5437
for _lib in _libs.values():
    try:
        EcsOverride = (ecs_entity_t).in_dll(_lib, "EcsOverride")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5442
for _lib in _libs.values():
    try:
        EcsInherit = (ecs_entity_t).in_dll(_lib, "EcsInherit")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5448
for _lib in _libs.values():
    try:
        EcsDontInherit = (ecs_entity_t).in_dll(_lib, "EcsDontInherit")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5457
for _lib in _libs.values():
    try:
        EcsSymmetric = (ecs_entity_t).in_dll(_lib, "EcsSymmetric")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5468
for _lib in _libs.values():
    try:
        EcsExclusive = (ecs_entity_t).in_dll(_lib, "EcsExclusive")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5471
for _lib in _libs.values():
    try:
        EcsAcyclic = (ecs_entity_t).in_dll(_lib, "EcsAcyclic")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5475
for _lib in _libs.values():
    try:
        EcsTraversable = (ecs_entity_t).in_dll(_lib, "EcsTraversable")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5486
for _lib in _libs.values():
    try:
        EcsWith = (ecs_entity_t).in_dll(_lib, "EcsWith")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5497
for _lib in _libs.values():
    try:
        EcsOneOf = (ecs_entity_t).in_dll(_lib, "EcsOneOf")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5500
for _lib in _libs.values():
    try:
        EcsCanToggle = (ecs_entity_t).in_dll(_lib, "EcsCanToggle")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5505
for _lib in _libs.values():
    try:
        EcsTrait = (ecs_entity_t).in_dll(_lib, "EcsTrait")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5516
for _lib in _libs.values():
    try:
        EcsRelationship = (ecs_entity_t).in_dll(_lib, "EcsRelationship")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5527
for _lib in _libs.values():
    try:
        EcsTarget = (ecs_entity_t).in_dll(_lib, "EcsTarget")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5531
for _lib in _libs.values():
    try:
        EcsPairIsTag = (ecs_entity_t).in_dll(_lib, "EcsPairIsTag")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5534
for _lib in _libs.values():
    try:
        EcsName = (ecs_entity_t).in_dll(_lib, "EcsName")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5537
for _lib in _libs.values():
    try:
        EcsSymbol = (ecs_entity_t).in_dll(_lib, "EcsSymbol")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5540
for _lib in _libs.values():
    try:
        EcsAlias = (ecs_entity_t).in_dll(_lib, "EcsAlias")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5543
for _lib in _libs.values():
    try:
        EcsChildOf = (ecs_entity_t).in_dll(_lib, "EcsChildOf")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5546
for _lib in _libs.values():
    try:
        EcsIsA = (ecs_entity_t).in_dll(_lib, "EcsIsA")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5549
for _lib in _libs.values():
    try:
        EcsDependsOn = (ecs_entity_t).in_dll(_lib, "EcsDependsOn")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5552
for _lib in _libs.values():
    try:
        EcsSlotOf = (ecs_entity_t).in_dll(_lib, "EcsSlotOf")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5555
for _lib in _libs.values():
    try:
        EcsOrderedChildren = (ecs_entity_t).in_dll(_lib, "EcsOrderedChildren")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5558
for _lib in _libs.values():
    try:
        EcsModule = (ecs_entity_t).in_dll(_lib, "EcsModule")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5561
for _lib in _libs.values():
    try:
        EcsPrivate = (ecs_entity_t).in_dll(_lib, "EcsPrivate")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5565
for _lib in _libs.values():
    try:
        EcsPrefab = (ecs_entity_t).in_dll(_lib, "EcsPrefab")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5569
for _lib in _libs.values():
    try:
        EcsDisabled = (ecs_entity_t).in_dll(_lib, "EcsDisabled")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5574
for _lib in _libs.values():
    try:
        EcsNotQueryable = (ecs_entity_t).in_dll(_lib, "EcsNotQueryable")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5577
for _lib in _libs.values():
    try:
        EcsOnAdd = (ecs_entity_t).in_dll(_lib, "EcsOnAdd")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5580
for _lib in _libs.values():
    try:
        EcsOnRemove = (ecs_entity_t).in_dll(_lib, "EcsOnRemove")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5583
for _lib in _libs.values():
    try:
        EcsOnSet = (ecs_entity_t).in_dll(_lib, "EcsOnSet")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5586
for _lib in _libs.values():
    try:
        EcsMonitor = (ecs_entity_t).in_dll(_lib, "EcsMonitor")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5589
for _lib in _libs.values():
    try:
        EcsOnTableCreate = (ecs_entity_t).in_dll(_lib, "EcsOnTableCreate")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5592
for _lib in _libs.values():
    try:
        EcsOnTableDelete = (ecs_entity_t).in_dll(_lib, "EcsOnTableDelete")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5595
for _lib in _libs.values():
    try:
        EcsOnDelete = (ecs_entity_t).in_dll(_lib, "EcsOnDelete")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5599
for _lib in _libs.values():
    try:
        EcsOnDeleteTarget = (ecs_entity_t).in_dll(_lib, "EcsOnDeleteTarget")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5603
for _lib in _libs.values():
    try:
        EcsRemove = (ecs_entity_t).in_dll(_lib, "EcsRemove")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5607
for _lib in _libs.values():
    try:
        EcsDelete = (ecs_entity_t).in_dll(_lib, "EcsDelete")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5611
for _lib in _libs.values():
    try:
        EcsPanic = (ecs_entity_t).in_dll(_lib, "EcsPanic")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5614
for _lib in _libs.values():
    try:
        EcsSparse = (ecs_entity_t).in_dll(_lib, "EcsSparse")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5617
for _lib in _libs.values():
    try:
        EcsDontFragment = (ecs_entity_t).in_dll(_lib, "EcsDontFragment")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5620
for _lib in _libs.values():
    try:
        EcsPredEq = (ecs_entity_t).in_dll(_lib, "EcsPredEq")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5623
for _lib in _libs.values():
    try:
        EcsPredMatch = (ecs_entity_t).in_dll(_lib, "EcsPredMatch")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5626
for _lib in _libs.values():
    try:
        EcsPredLookup = (ecs_entity_t).in_dll(_lib, "EcsPredLookup")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5629
for _lib in _libs.values():
    try:
        EcsScopeOpen = (ecs_entity_t).in_dll(_lib, "EcsScopeOpen")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5632
for _lib in _libs.values():
    try:
        EcsScopeClose = (ecs_entity_t).in_dll(_lib, "EcsScopeClose")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5638
for _lib in _libs.values():
    try:
        EcsEmpty = (ecs_entity_t).in_dll(_lib, "EcsEmpty")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5640
for _lib in _libs.values():
    try:
        FLECS_IDEcsPipelineID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsPipelineID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5641
for _lib in _libs.values():
    try:
        EcsOnStart = (ecs_entity_t).in_dll(_lib, "EcsOnStart")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5642
for _lib in _libs.values():
    try:
        EcsPreFrame = (ecs_entity_t).in_dll(_lib, "EcsPreFrame")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5643
for _lib in _libs.values():
    try:
        EcsOnLoad = (ecs_entity_t).in_dll(_lib, "EcsOnLoad")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5644
for _lib in _libs.values():
    try:
        EcsPostLoad = (ecs_entity_t).in_dll(_lib, "EcsPostLoad")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5645
for _lib in _libs.values():
    try:
        EcsPreUpdate = (ecs_entity_t).in_dll(_lib, "EcsPreUpdate")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5646
for _lib in _libs.values():
    try:
        EcsOnUpdate = (ecs_entity_t).in_dll(_lib, "EcsOnUpdate")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5647
for _lib in _libs.values():
    try:
        EcsOnValidate = (ecs_entity_t).in_dll(_lib, "EcsOnValidate")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5648
for _lib in _libs.values():
    try:
        EcsPostUpdate = (ecs_entity_t).in_dll(_lib, "EcsPostUpdate")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5649
for _lib in _libs.values():
    try:
        EcsPreStore = (ecs_entity_t).in_dll(_lib, "EcsPreStore")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5650
for _lib in _libs.values():
    try:
        EcsOnStore = (ecs_entity_t).in_dll(_lib, "EcsOnStore")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5651
for _lib in _libs.values():
    try:
        EcsPostFrame = (ecs_entity_t).in_dll(_lib, "EcsPostFrame")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5652
for _lib in _libs.values():
    try:
        EcsPhase = (ecs_entity_t).in_dll(_lib, "EcsPhase")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5654
for _lib in _libs.values():
    try:
        EcsConstant = (ecs_entity_t).in_dll(_lib, "EcsConstant")
        break
    except:
        pass

# vendor/flecs/flecs.h: 5696
for _lib in _libs.values():
    if not _lib.has("ecs_init", "cdecl"):
        continue
    ecs_init = _lib.get("ecs_init", "cdecl")
    ecs_init.argtypes = []
    ecs_init.restype = POINTER(ecs_world_t)
    break

# vendor/flecs/flecs.h: 5705
for _lib in _libs.values():
    if not _lib.has("ecs_mini", "cdecl"):
        continue
    ecs_mini = _lib.get("ecs_mini", "cdecl")
    ecs_mini.argtypes = []
    ecs_mini.restype = POINTER(ecs_world_t)
    break

# vendor/flecs/flecs.h: 5715
for _lib in _libs.values():
    if not _lib.has("ecs_init_w_args", "cdecl"):
        continue
    ecs_init_w_args = _lib.get("ecs_init_w_args", "cdecl")
    ecs_init_w_args.argtypes = [c_int, POINTER(POINTER(c_char))]
    ecs_init_w_args.restype = POINTER(ecs_world_t)
    break

# vendor/flecs/flecs.h: 5726
for _lib in _libs.values():
    if not _lib.has("ecs_fini", "cdecl"):
        continue
    ecs_fini = _lib.get("ecs_fini", "cdecl")
    ecs_fini.argtypes = [POINTER(ecs_world_t)]
    ecs_fini.restype = c_int
    break

# vendor/flecs/flecs.h: 5737
for _lib in _libs.values():
    if not _lib.has("ecs_is_fini", "cdecl"):
        continue
    ecs_is_fini = _lib.get("ecs_is_fini", "cdecl")
    ecs_is_fini.argtypes = [POINTER(ecs_world_t)]
    ecs_is_fini.restype = c_bool
    break

# vendor/flecs/flecs.h: 5748
for _lib in _libs.values():
    if not _lib.has("ecs_atfini", "cdecl"):
        continue
    ecs_atfini = _lib.get("ecs_atfini", "cdecl")
    ecs_atfini.argtypes = [POINTER(ecs_world_t), ecs_fini_action_t, POINTER(None)]
    ecs_atfini.restype = None
    break


# vendor/flecs/flecs.h: 5758
class struct_ecs_entities_t(Structure):
    pass


struct_ecs_entities_t.__slots__ = [
    "ids",
    "count",
    "alive_count",
]
struct_ecs_entities_t._fields_ = [
    ("ids", POINTER(ecs_entity_t)),
    ("count", c_int32),
    ("alive_count", c_int32),
]

ecs_entities_t = struct_ecs_entities_t  # vendor/flecs/flecs.h: 5758

# vendor/flecs/flecs.h: 5787
for _lib in _libs.values():
    if not _lib.has("ecs_get_entities", "cdecl"):
        continue
    ecs_get_entities = _lib.get("ecs_get_entities", "cdecl")
    ecs_get_entities.argtypes = [POINTER(ecs_world_t)]
    ecs_get_entities.restype = ecs_entities_t
    break

# vendor/flecs/flecs.h: 5798
for _lib in _libs.values():
    if not _lib.has("ecs_world_get_flags", "cdecl"):
        continue
    ecs_world_get_flags = _lib.get("ecs_world_get_flags", "cdecl")
    ecs_world_get_flags.argtypes = [POINTER(ecs_world_t)]
    ecs_world_get_flags.restype = ecs_flags32_t
    break

# vendor/flecs/flecs.h: 5827
for _lib in _libs.values():
    if not _lib.has("ecs_frame_begin", "cdecl"):
        continue
    ecs_frame_begin = _lib.get("ecs_frame_begin", "cdecl")
    ecs_frame_begin.argtypes = [POINTER(ecs_world_t), c_float]
    ecs_frame_begin.restype = c_float
    break

# vendor/flecs/flecs.h: 5838
for _lib in _libs.values():
    if not _lib.has("ecs_frame_end", "cdecl"):
        continue
    ecs_frame_end = _lib.get("ecs_frame_end", "cdecl")
    ecs_frame_end.argtypes = [POINTER(ecs_world_t)]
    ecs_frame_end.restype = None
    break

# vendor/flecs/flecs.h: 5849
for _lib in _libs.values():
    if not _lib.has("ecs_run_post_frame", "cdecl"):
        continue
    ecs_run_post_frame = _lib.get("ecs_run_post_frame", "cdecl")
    ecs_run_post_frame.argtypes = [
        POINTER(ecs_world_t),
        ecs_fini_action_t,
        POINTER(None),
    ]
    ecs_run_post_frame.restype = None
    break

# vendor/flecs/flecs.h: 5861
for _lib in _libs.values():
    if not _lib.has("ecs_quit", "cdecl"):
        continue
    ecs_quit = _lib.get("ecs_quit", "cdecl")
    ecs_quit.argtypes = [POINTER(ecs_world_t)]
    ecs_quit.restype = None
    break

# vendor/flecs/flecs.h: 5871
for _lib in _libs.values():
    if not _lib.has("ecs_should_quit", "cdecl"):
        continue
    ecs_should_quit = _lib.get("ecs_should_quit", "cdecl")
    ecs_should_quit.argtypes = [POINTER(ecs_world_t)]
    ecs_should_quit.restype = c_bool
    break

# vendor/flecs/flecs.h: 5885
for _lib in _libs.values():
    if not _lib.has("ecs_measure_frame_time", "cdecl"):
        continue
    ecs_measure_frame_time = _lib.get("ecs_measure_frame_time", "cdecl")
    ecs_measure_frame_time.argtypes = [POINTER(ecs_world_t), c_bool]
    ecs_measure_frame_time.restype = None
    break

# vendor/flecs/flecs.h: 5899
for _lib in _libs.values():
    if not _lib.has("ecs_measure_system_time", "cdecl"):
        continue
    ecs_measure_system_time = _lib.get("ecs_measure_system_time", "cdecl")
    ecs_measure_system_time.argtypes = [POINTER(ecs_world_t), c_bool]
    ecs_measure_system_time.restype = None
    break

# vendor/flecs/flecs.h: 5919
for _lib in _libs.values():
    if not _lib.has("ecs_set_target_fps", "cdecl"):
        continue
    ecs_set_target_fps = _lib.get("ecs_set_target_fps", "cdecl")
    ecs_set_target_fps.argtypes = [POINTER(ecs_world_t), c_float]
    ecs_set_target_fps.restype = None
    break

# vendor/flecs/flecs.h: 5937
for _lib in _libs.values():
    if not _lib.has("ecs_set_default_query_flags", "cdecl"):
        continue
    ecs_set_default_query_flags = _lib.get("ecs_set_default_query_flags", "cdecl")
    ecs_set_default_query_flags.argtypes = [POINTER(ecs_world_t), ecs_flags32_t]
    ecs_set_default_query_flags.restype = None
    break

# vendor/flecs/flecs.h: 6018
for _lib in _libs.values():
    if not _lib.has("ecs_readonly_begin", "cdecl"):
        continue
    ecs_readonly_begin = _lib.get("ecs_readonly_begin", "cdecl")
    ecs_readonly_begin.argtypes = [POINTER(ecs_world_t), c_bool]
    ecs_readonly_begin.restype = c_bool
    break

# vendor/flecs/flecs.h: 6030
for _lib in _libs.values():
    if not _lib.has("ecs_readonly_end", "cdecl"):
        continue
    ecs_readonly_end = _lib.get("ecs_readonly_end", "cdecl")
    ecs_readonly_end.argtypes = [POINTER(ecs_world_t)]
    ecs_readonly_end.restype = None
    break

# vendor/flecs/flecs.h: 6044
for _lib in _libs.values():
    if not _lib.has("ecs_merge", "cdecl"):
        continue
    ecs_merge = _lib.get("ecs_merge", "cdecl")
    ecs_merge.argtypes = [POINTER(ecs_world_t)]
    ecs_merge.restype = None
    break

# vendor/flecs/flecs.h: 6063
for _lib in _libs.values():
    if not _lib.has("ecs_defer_begin", "cdecl"):
        continue
    ecs_defer_begin = _lib.get("ecs_defer_begin", "cdecl")
    ecs_defer_begin.argtypes = [POINTER(ecs_world_t)]
    ecs_defer_begin.restype = c_bool
    break

# vendor/flecs/flecs.h: 6077
for _lib in _libs.values():
    if not _lib.has("ecs_is_deferred", "cdecl"):
        continue
    ecs_is_deferred = _lib.get("ecs_is_deferred", "cdecl")
    ecs_is_deferred.argtypes = [POINTER(ecs_world_t)]
    ecs_is_deferred.restype = c_bool
    break

# vendor/flecs/flecs.h: 6094
for _lib in _libs.values():
    if not _lib.has("ecs_defer_end", "cdecl"):
        continue
    ecs_defer_end = _lib.get("ecs_defer_end", "cdecl")
    ecs_defer_end.argtypes = [POINTER(ecs_world_t)]
    ecs_defer_end.restype = c_bool
    break

# vendor/flecs/flecs.h: 6112
for _lib in _libs.values():
    if not _lib.has("ecs_defer_suspend", "cdecl"):
        continue
    ecs_defer_suspend = _lib.get("ecs_defer_suspend", "cdecl")
    ecs_defer_suspend.argtypes = [POINTER(ecs_world_t)]
    ecs_defer_suspend.restype = None
    break

# vendor/flecs/flecs.h: 6126
for _lib in _libs.values():
    if not _lib.has("ecs_defer_resume", "cdecl"):
        continue
    ecs_defer_resume = _lib.get("ecs_defer_resume", "cdecl")
    ecs_defer_resume.argtypes = [POINTER(ecs_world_t)]
    ecs_defer_resume.restype = None
    break

# vendor/flecs/flecs.h: 6143
for _lib in _libs.values():
    if not _lib.has("ecs_set_stage_count", "cdecl"):
        continue
    ecs_set_stage_count = _lib.get("ecs_set_stage_count", "cdecl")
    ecs_set_stage_count.argtypes = [POINTER(ecs_world_t), c_int32]
    ecs_set_stage_count.restype = None
    break

# vendor/flecs/flecs.h: 6154
for _lib in _libs.values():
    if not _lib.has("ecs_get_stage_count", "cdecl"):
        continue
    ecs_get_stage_count = _lib.get("ecs_get_stage_count", "cdecl")
    ecs_get_stage_count.argtypes = [POINTER(ecs_world_t)]
    ecs_get_stage_count.restype = c_int32
    break

# vendor/flecs/flecs.h: 6173
for _lib in _libs.values():
    if not _lib.has("ecs_get_stage", "cdecl"):
        continue
    ecs_get_stage = _lib.get("ecs_get_stage", "cdecl")
    ecs_get_stage.argtypes = [POINTER(ecs_world_t), c_int32]
    ecs_get_stage.restype = POINTER(ecs_world_t)
    break

# vendor/flecs/flecs.h: 6185
for _lib in _libs.values():
    if not _lib.has("ecs_stage_is_readonly", "cdecl"):
        continue
    ecs_stage_is_readonly = _lib.get("ecs_stage_is_readonly", "cdecl")
    ecs_stage_is_readonly.argtypes = [POINTER(ecs_world_t)]
    ecs_stage_is_readonly.restype = c_bool
    break

# vendor/flecs/flecs.h: 6196
for _lib in _libs.values():
    if not _lib.has("ecs_stage_new", "cdecl"):
        continue
    ecs_stage_new = _lib.get("ecs_stage_new", "cdecl")
    ecs_stage_new.argtypes = [POINTER(ecs_world_t)]
    ecs_stage_new.restype = POINTER(ecs_world_t)
    break

# vendor/flecs/flecs.h: 6204
for _lib in _libs.values():
    if not _lib.has("ecs_stage_free", "cdecl"):
        continue
    ecs_stage_free = _lib.get("ecs_stage_free", "cdecl")
    ecs_stage_free.argtypes = [POINTER(ecs_world_t)]
    ecs_stage_free.restype = None
    break

# vendor/flecs/flecs.h: 6215
for _lib in _libs.values():
    if not _lib.has("ecs_stage_get_id", "cdecl"):
        continue
    ecs_stage_get_id = _lib.get("ecs_stage_get_id", "cdecl")
    ecs_stage_get_id.argtypes = [POINTER(ecs_world_t)]
    ecs_stage_get_id.restype = c_int32
    break

# vendor/flecs/flecs.h: 6234
for _lib in _libs.values():
    if not _lib.has("ecs_set_ctx", "cdecl"):
        continue
    ecs_set_ctx = _lib.get("ecs_set_ctx", "cdecl")
    ecs_set_ctx.argtypes = [POINTER(ecs_world_t), POINTER(None), ecs_ctx_free_t]
    ecs_set_ctx.restype = None
    break

# vendor/flecs/flecs.h: 6248
for _lib in _libs.values():
    if not _lib.has("ecs_set_binding_ctx", "cdecl"):
        continue
    ecs_set_binding_ctx = _lib.get("ecs_set_binding_ctx", "cdecl")
    ecs_set_binding_ctx.argtypes = [POINTER(ecs_world_t), POINTER(None), ecs_ctx_free_t]
    ecs_set_binding_ctx.restype = None
    break

# vendor/flecs/flecs.h: 6261
for _lib in _libs.values():
    if not _lib.has("ecs_get_ctx", "cdecl"):
        continue
    ecs_get_ctx = _lib.get("ecs_get_ctx", "cdecl")
    ecs_get_ctx.argtypes = [POINTER(ecs_world_t)]
    ecs_get_ctx.restype = POINTER(c_ubyte)
    ecs_get_ctx.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 6272
for _lib in _libs.values():
    if not _lib.has("ecs_get_binding_ctx", "cdecl"):
        continue
    ecs_get_binding_ctx = _lib.get("ecs_get_binding_ctx", "cdecl")
    ecs_get_binding_ctx.argtypes = [POINTER(ecs_world_t)]
    ecs_get_binding_ctx.restype = POINTER(c_ubyte)
    ecs_get_binding_ctx.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 6281
for _lib in _libs.values():
    if not _lib.has("ecs_get_build_info", "cdecl"):
        continue
    ecs_get_build_info = _lib.get("ecs_get_build_info", "cdecl")
    ecs_get_build_info.argtypes = []
    ecs_get_build_info.restype = POINTER(ecs_build_info_t)
    break

# vendor/flecs/flecs.h: 6289
for _lib in _libs.values():
    if not _lib.has("ecs_get_world_info", "cdecl"):
        continue
    ecs_get_world_info = _lib.get("ecs_get_world_info", "cdecl")
    ecs_get_world_info.argtypes = [POINTER(ecs_world_t)]
    ecs_get_world_info.restype = POINTER(ecs_world_info_t)
    break

# vendor/flecs/flecs.h: 6301
for _lib in _libs.values():
    if not _lib.has("ecs_dim", "cdecl"):
        continue
    ecs_dim = _lib.get("ecs_dim", "cdecl")
    ecs_dim.argtypes = [POINTER(ecs_world_t), c_int32]
    ecs_dim.restype = None
    break

# vendor/flecs/flecs.h: 6320
for _lib in _libs.values():
    if not _lib.has("ecs_shrink", "cdecl"):
        continue
    ecs_shrink = _lib.get("ecs_shrink", "cdecl")
    ecs_shrink.argtypes = [POINTER(ecs_world_t)]
    ecs_shrink.restype = None
    break

# vendor/flecs/flecs.h: 6339
for _lib in _libs.values():
    if not _lib.has("ecs_set_entity_range", "cdecl"):
        continue
    ecs_set_entity_range = _lib.get("ecs_set_entity_range", "cdecl")
    ecs_set_entity_range.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_entity_t]
    ecs_set_entity_range.restype = None
    break

# vendor/flecs/flecs.h: 6355
for _lib in _libs.values():
    if not _lib.has("ecs_enable_range_check", "cdecl"):
        continue
    ecs_enable_range_check = _lib.get("ecs_enable_range_check", "cdecl")
    ecs_enable_range_check.argtypes = [POINTER(ecs_world_t), c_bool]
    ecs_enable_range_check.restype = c_bool
    break

# vendor/flecs/flecs.h: 6365
for _lib in _libs.values():
    if not _lib.has("ecs_get_max_id", "cdecl"):
        continue
    ecs_get_max_id = _lib.get("ecs_get_max_id", "cdecl")
    ecs_get_max_id.argtypes = [POINTER(ecs_world_t)]
    ecs_get_max_id.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 6382
for _lib in _libs.values():
    if not _lib.has("ecs_run_aperiodic", "cdecl"):
        continue
    ecs_run_aperiodic = _lib.get("ecs_run_aperiodic", "cdecl")
    ecs_run_aperiodic.argtypes = [POINTER(ecs_world_t), ecs_flags32_t]
    ecs_run_aperiodic.restype = None
    break


# vendor/flecs/flecs.h: 6396
class struct_ecs_delete_empty_tables_desc_t(Structure):
    pass


struct_ecs_delete_empty_tables_desc_t.__slots__ = [
    "clear_generation",
    "delete_generation",
    "time_budget_seconds",
]
struct_ecs_delete_empty_tables_desc_t._fields_ = [
    ("clear_generation", uint16_t),
    ("delete_generation", uint16_t),
    ("time_budget_seconds", c_double),
]

ecs_delete_empty_tables_desc_t = (
    struct_ecs_delete_empty_tables_desc_t  # vendor/flecs/flecs.h: 6396
)

# vendor/flecs/flecs.h: 6428
for _lib in _libs.values():
    if not _lib.has("ecs_delete_empty_tables", "cdecl"):
        continue
    ecs_delete_empty_tables = _lib.get("ecs_delete_empty_tables", "cdecl")
    ecs_delete_empty_tables.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_delete_empty_tables_desc_t),
    ]
    ecs_delete_empty_tables.restype = c_int32
    break

# vendor/flecs/flecs.h: 6438
for _lib in _libs.values():
    if not _lib.has("ecs_get_world", "cdecl"):
        continue
    ecs_get_world = _lib.get("ecs_get_world", "cdecl")
    ecs_get_world.argtypes = [POINTER(ecs_poly_t)]
    ecs_get_world.restype = POINTER(ecs_world_t)
    break

# vendor/flecs/flecs.h: 6447
for _lib in _libs.values():
    if not _lib.has("ecs_get_entity", "cdecl"):
        continue
    ecs_get_entity = _lib.get("ecs_get_entity", "cdecl")
    ecs_get_entity.argtypes = [POINTER(ecs_poly_t)]
    ecs_get_entity.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 6464
for _lib in _libs.values():
    if not _lib.has("flecs_poly_is_", "cdecl"):
        continue
    flecs_poly_is_ = _lib.get("flecs_poly_is_", "cdecl")
    flecs_poly_is_.argtypes = [POINTER(ecs_poly_t), c_int32]
    flecs_poly_is_.restype = c_bool
    break

# vendor/flecs/flecs.h: 6483
for _lib in _libs.values():
    if not _lib.has("ecs_make_pair", "cdecl"):
        continue
    ecs_make_pair = _lib.get("ecs_make_pair", "cdecl")
    ecs_make_pair.argtypes = [ecs_entity_t, ecs_entity_t]
    ecs_make_pair.restype = ecs_id_t
    break

# vendor/flecs/flecs.h: 6510
for _lib in _libs.values():
    if not _lib.has("ecs_exclusive_access_begin", "cdecl"):
        continue
    ecs_exclusive_access_begin = _lib.get("ecs_exclusive_access_begin", "cdecl")
    ecs_exclusive_access_begin.argtypes = [POINTER(ecs_world_t), String]
    ecs_exclusive_access_begin.restype = None
    break

# vendor/flecs/flecs.h: 6537
for _lib in _libs.values():
    if not _lib.has("ecs_exclusive_access_end", "cdecl"):
        continue
    ecs_exclusive_access_end = _lib.get("ecs_exclusive_access_end", "cdecl")
    ecs_exclusive_access_end.argtypes = [POINTER(ecs_world_t), c_bool]
    ecs_exclusive_access_end.restype = None
    break

# vendor/flecs/flecs.h: 6568
for _lib in _libs.values():
    if not _lib.has("ecs_new", "cdecl"):
        continue
    ecs_new = _lib.get("ecs_new", "cdecl")
    ecs_new.argtypes = [POINTER(ecs_world_t)]
    ecs_new.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 6589
for _lib in _libs.values():
    if not _lib.has("ecs_new_low_id", "cdecl"):
        continue
    ecs_new_low_id = _lib.get("ecs_new_low_id", "cdecl")
    ecs_new_low_id.argtypes = [POINTER(ecs_world_t)]
    ecs_new_low_id.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 6601
for _lib in _libs.values():
    if not _lib.has("ecs_new_w_id", "cdecl"):
        continue
    ecs_new_w_id = _lib.get("ecs_new_w_id", "cdecl")
    ecs_new_w_id.argtypes = [POINTER(ecs_world_t), ecs_id_t]
    ecs_new_w_id.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 6613
for _lib in _libs.values():
    if not _lib.has("ecs_new_w_table", "cdecl"):
        continue
    ecs_new_w_table = _lib.get("ecs_new_w_table", "cdecl")
    ecs_new_w_table.argtypes = [POINTER(ecs_world_t), POINTER(ecs_table_t)]
    ecs_new_w_table.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 6636
for _lib in _libs.values():
    if not _lib.has("ecs_entity_init", "cdecl"):
        continue
    ecs_entity_init = _lib.get("ecs_entity_init", "cdecl")
    ecs_entity_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_entity_desc_t)]
    ecs_entity_init.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 6667
for _lib in _libs.values():
    if not _lib.has("ecs_bulk_init", "cdecl"):
        continue
    ecs_bulk_init = _lib.get("ecs_bulk_init", "cdecl")
    ecs_bulk_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_bulk_desc_t)]
    ecs_bulk_init.restype = POINTER(ecs_entity_t)
    break

# vendor/flecs/flecs.h: 6681
for _lib in _libs.values():
    if not _lib.has("ecs_bulk_new_w_id", "cdecl"):
        continue
    ecs_bulk_new_w_id = _lib.get("ecs_bulk_new_w_id", "cdecl")
    ecs_bulk_new_w_id.argtypes = [POINTER(ecs_world_t), ecs_id_t, c_int32]
    ecs_bulk_new_w_id.restype = POINTER(ecs_entity_t)
    break

# vendor/flecs/flecs.h: 6702
for _lib in _libs.values():
    if not _lib.has("ecs_clone", "cdecl"):
        continue
    ecs_clone = _lib.get("ecs_clone", "cdecl")
    ecs_clone.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_entity_t, c_bool]
    ecs_clone.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 6717
for _lib in _libs.values():
    if not _lib.has("ecs_delete", "cdecl"):
        continue
    ecs_delete = _lib.get("ecs_delete", "cdecl")
    ecs_delete.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_delete.restype = None
    break

# vendor/flecs/flecs.h: 6729
for _lib in _libs.values():
    if not _lib.has("ecs_delete_with", "cdecl"):
        continue
    ecs_delete_with = _lib.get("ecs_delete_with", "cdecl")
    ecs_delete_with.argtypes = [POINTER(ecs_world_t), ecs_id_t]
    ecs_delete_with.restype = None
    break

# vendor/flecs/flecs.h: 6751
for _lib in _libs.values():
    if not _lib.has("ecs_set_child_order", "cdecl"):
        continue
    ecs_set_child_order = _lib.get("ecs_set_child_order", "cdecl")
    ecs_set_child_order.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        POINTER(ecs_entity_t),
        c_int32,
    ]
    ecs_set_child_order.restype = None
    break

# vendor/flecs/flecs.h: 6767
for _lib in _libs.values():
    if not _lib.has("ecs_get_ordered_children", "cdecl"):
        continue
    ecs_get_ordered_children = _lib.get("ecs_get_ordered_children", "cdecl")
    ecs_get_ordered_children.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_get_ordered_children.restype = ecs_entities_t
    break

# vendor/flecs/flecs.h: 6789
for _lib in _libs.values():
    if not _lib.has("ecs_add_id", "cdecl"):
        continue
    ecs_add_id = _lib.get("ecs_add_id", "cdecl")
    ecs_add_id.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_id_t]
    ecs_add_id.restype = None
    break

# vendor/flecs/flecs.h: 6803
for _lib in _libs.values():
    if not _lib.has("ecs_remove_id", "cdecl"):
        continue
    ecs_remove_id = _lib.get("ecs_remove_id", "cdecl")
    ecs_remove_id.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_id_t]
    ecs_remove_id.restype = None
    break

# vendor/flecs/flecs.h: 6860
for _lib in _libs.values():
    if not _lib.has("ecs_auto_override_id", "cdecl"):
        continue
    ecs_auto_override_id = _lib.get("ecs_auto_override_id", "cdecl")
    ecs_auto_override_id.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_id_t]
    ecs_auto_override_id.restype = None
    break

# vendor/flecs/flecs.h: 6872
for _lib in _libs.values():
    if not _lib.has("ecs_clear", "cdecl"):
        continue
    ecs_clear = _lib.get("ecs_clear", "cdecl")
    ecs_clear.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_clear.restype = None
    break

# vendor/flecs/flecs.h: 6884
for _lib in _libs.values():
    if not _lib.has("ecs_remove_all", "cdecl"):
        continue
    ecs_remove_all = _lib.get("ecs_remove_all", "cdecl")
    ecs_remove_all.argtypes = [POINTER(ecs_world_t), ecs_id_t]
    ecs_remove_all.restype = None
    break

# vendor/flecs/flecs.h: 6896
for _lib in _libs.values():
    if not _lib.has("ecs_set_with", "cdecl"):
        continue
    ecs_set_with = _lib.get("ecs_set_with", "cdecl")
    ecs_set_with.argtypes = [POINTER(ecs_world_t), ecs_id_t]
    ecs_set_with.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 6907
for _lib in _libs.values():
    if not _lib.has("ecs_get_with", "cdecl"):
        continue
    ecs_get_with = _lib.get("ecs_get_with", "cdecl")
    ecs_get_with.argtypes = [POINTER(ecs_world_t)]
    ecs_get_with.restype = ecs_id_t
    break

# vendor/flecs/flecs.h: 6929
for _lib in _libs.values():
    if not _lib.has("ecs_enable", "cdecl"):
        continue
    ecs_enable = _lib.get("ecs_enable", "cdecl")
    ecs_enable.argtypes = [POINTER(ecs_world_t), ecs_entity_t, c_bool]
    ecs_enable.restype = None
    break

# vendor/flecs/flecs.h: 6948
for _lib in _libs.values():
    if not _lib.has("ecs_enable_id", "cdecl"):
        continue
    ecs_enable_id = _lib.get("ecs_enable_id", "cdecl")
    ecs_enable_id.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_id_t, c_bool]
    ecs_enable_id.restype = None
    break

# vendor/flecs/flecs.h: 6965
for _lib in _libs.values():
    if not _lib.has("ecs_is_enabled_id", "cdecl"):
        continue
    ecs_is_enabled_id = _lib.get("ecs_is_enabled_id", "cdecl")
    ecs_is_enabled_id.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_id_t]
    ecs_is_enabled_id.restype = c_bool
    break

# vendor/flecs/flecs.h: 6994
for _lib in _libs.values():
    if not _lib.has("ecs_get_id", "cdecl"):
        continue
    ecs_get_id = _lib.get("ecs_get_id", "cdecl")
    ecs_get_id.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_id_t]
    ecs_get_id.restype = POINTER(c_ubyte)
    ecs_get_id.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 7011
for _lib in _libs.values():
    if not _lib.has("ecs_get_mut_id", "cdecl"):
        continue
    ecs_get_mut_id = _lib.get("ecs_get_mut_id", "cdecl")
    ecs_get_mut_id.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_id_t]
    ecs_get_mut_id.restype = POINTER(c_ubyte)
    ecs_get_mut_id.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 7034
for _lib in _libs.values():
    if not _lib.has("ecs_ensure_id", "cdecl"):
        continue
    ecs_ensure_id = _lib.get("ecs_ensure_id", "cdecl")
    ecs_ensure_id.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_id_t]
    ecs_ensure_id.restype = POINTER(c_ubyte)
    ecs_ensure_id.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 7051
for _lib in _libs.values():
    if not _lib.has("ecs_ensure_modified_id", "cdecl"):
        continue
    ecs_ensure_modified_id = _lib.get("ecs_ensure_modified_id", "cdecl")
    ecs_ensure_modified_id.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_id_t]
    ecs_ensure_modified_id.restype = POINTER(c_ubyte)
    ecs_ensure_modified_id.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 7068
for _lib in _libs.values():
    if not _lib.has("ecs_get_mut_modified_id", "cdecl"):
        continue
    ecs_get_mut_modified_id = _lib.get("ecs_get_mut_modified_id", "cdecl")
    ecs_get_mut_modified_id.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_id_t]
    ecs_get_mut_modified_id.restype = POINTER(c_ubyte)
    ecs_get_mut_modified_id.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 7084
for _lib in _libs.values():
    if not _lib.has("ecs_ref_init_id", "cdecl"):
        continue
    ecs_ref_init_id = _lib.get("ecs_ref_init_id", "cdecl")
    ecs_ref_init_id.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_id_t]
    ecs_ref_init_id.restype = ecs_ref_t
    break

# vendor/flecs/flecs.h: 7098
for _lib in _libs.values():
    if not _lib.has("ecs_ref_get_id", "cdecl"):
        continue
    ecs_ref_get_id = _lib.get("ecs_ref_get_id", "cdecl")
    ecs_ref_get_id.argtypes = [POINTER(ecs_world_t), POINTER(ecs_ref_t), ecs_id_t]
    ecs_ref_get_id.restype = POINTER(c_ubyte)
    ecs_ref_get_id.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 7111
for _lib in _libs.values():
    if not _lib.has("ecs_ref_update", "cdecl"):
        continue
    ecs_ref_update = _lib.get("ecs_ref_update", "cdecl")
    ecs_ref_update.argtypes = [POINTER(ecs_world_t), POINTER(ecs_ref_t)]
    ecs_ref_update.restype = None
    break

# vendor/flecs/flecs.h: 7135
for _lib in _libs.values():
    if not _lib.has("ecs_emplace_id", "cdecl"):
        continue
    ecs_emplace_id = _lib.get("ecs_emplace_id", "cdecl")
    ecs_emplace_id.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        ecs_id_t,
        POINTER(c_bool),
    ]
    ecs_emplace_id.restype = POINTER(c_ubyte)
    ecs_emplace_id.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 7151
for _lib in _libs.values():
    if not _lib.has("ecs_modified_id", "cdecl"):
        continue
    ecs_modified_id = _lib.get("ecs_modified_id", "cdecl")
    ecs_modified_id.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_id_t]
    ecs_modified_id.restype = None
    break

# vendor/flecs/flecs.h: 7172
for _lib in _libs.values():
    if not _lib.has("ecs_set_id", "cdecl"):
        continue
    ecs_set_id = _lib.get("ecs_set_id", "cdecl")
    ecs_set_id.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        ecs_id_t,
        c_size_t,
        POINTER(None),
    ]
    ecs_set_id.restype = None
    break

# vendor/flecs/flecs.h: 7207
for _lib in _libs.values():
    if not _lib.has("ecs_is_valid", "cdecl"):
        continue
    ecs_is_valid = _lib.get("ecs_is_valid", "cdecl")
    ecs_is_valid.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_is_valid.restype = c_bool
    break

# vendor/flecs/flecs.h: 7237
for _lib in _libs.values():
    if not _lib.has("ecs_is_alive", "cdecl"):
        continue
    ecs_is_alive = _lib.get("ecs_is_alive", "cdecl")
    ecs_is_alive.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_is_alive.restype = c_bool
    break

# vendor/flecs/flecs.h: 7247
for _lib in _libs.values():
    if not _lib.has("ecs_strip_generation", "cdecl"):
        continue
    ecs_strip_generation = _lib.get("ecs_strip_generation", "cdecl")
    ecs_strip_generation.argtypes = [ecs_entity_t]
    ecs_strip_generation.restype = ecs_id_t
    break

# vendor/flecs/flecs.h: 7267
for _lib in _libs.values():
    if not _lib.has("ecs_get_alive", "cdecl"):
        continue
    ecs_get_alive = _lib.get("ecs_get_alive", "cdecl")
    ecs_get_alive.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_get_alive.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 7294
for _lib in _libs.values():
    if not _lib.has("ecs_make_alive", "cdecl"):
        continue
    ecs_make_alive = _lib.get("ecs_make_alive", "cdecl")
    ecs_make_alive.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_make_alive.restype = None
    break

# vendor/flecs/flecs.h: 7317
for _lib in _libs.values():
    if not _lib.has("ecs_make_alive_id", "cdecl"):
        continue
    ecs_make_alive_id = _lib.get("ecs_make_alive_id", "cdecl")
    ecs_make_alive_id.argtypes = [POINTER(ecs_world_t), ecs_id_t]
    ecs_make_alive_id.restype = None
    break

# vendor/flecs/flecs.h: 7329
for _lib in _libs.values():
    if not _lib.has("ecs_exists", "cdecl"):
        continue
    ecs_exists = _lib.get("ecs_exists", "cdecl")
    ecs_exists.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_exists.restype = c_bool
    break

# vendor/flecs/flecs.h: 7348
for _lib in _libs.values():
    if not _lib.has("ecs_set_version", "cdecl"):
        continue
    ecs_set_version = _lib.get("ecs_set_version", "cdecl")
    ecs_set_version.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_set_version.restype = None
    break

# vendor/flecs/flecs.h: 7368
for _lib in _libs.values():
    if not _lib.has("ecs_get_type", "cdecl"):
        continue
    ecs_get_type = _lib.get("ecs_get_type", "cdecl")
    ecs_get_type.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_get_type.restype = POINTER(ecs_type_t)
    break

# vendor/flecs/flecs.h: 7379
for _lib in _libs.values():
    if not _lib.has("ecs_get_table", "cdecl"):
        continue
    ecs_get_table = _lib.get("ecs_get_table", "cdecl")
    ecs_get_table.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_get_table.restype = POINTER(ecs_table_t)
    break

# vendor/flecs/flecs.h: 7391
for _lib in _libs.values():
    if not _lib.has("ecs_type_str", "cdecl"):
        continue
    ecs_type_str = _lib.get("ecs_type_str", "cdecl")
    ecs_type_str.argtypes = [POINTER(ecs_world_t), POINTER(ecs_type_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_type_str.restype = ReturnString
    else:
        ecs_type_str.restype = String
        ecs_type_str.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 7407
for _lib in _libs.values():
    if not _lib.has("ecs_table_str", "cdecl"):
        continue
    ecs_table_str = _lib.get("ecs_table_str", "cdecl")
    ecs_table_str.argtypes = [POINTER(ecs_world_t), POINTER(ecs_table_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_table_str.restype = ReturnString
    else:
        ecs_table_str.restype = String
        ecs_table_str.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 7426
for _lib in _libs.values():
    if not _lib.has("ecs_entity_str", "cdecl"):
        continue
    ecs_entity_str = _lib.get("ecs_entity_str", "cdecl")
    ecs_entity_str.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_entity_str.restype = ReturnString
    else:
        ecs_entity_str.restype = String
        ecs_entity_str.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 7441
for _lib in _libs.values():
    if not _lib.has("ecs_has_id", "cdecl"):
        continue
    ecs_has_id = _lib.get("ecs_has_id", "cdecl")
    ecs_has_id.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_id_t]
    ecs_has_id.restype = c_bool
    break

# vendor/flecs/flecs.h: 7457
for _lib in _libs.values():
    if not _lib.has("ecs_owns_id", "cdecl"):
        continue
    ecs_owns_id = _lib.get("ecs_owns_id", "cdecl")
    ecs_owns_id.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_id_t]
    ecs_owns_id.restype = c_bool
    break

# vendor/flecs/flecs.h: 7477
for _lib in _libs.values():
    if not _lib.has("ecs_get_target", "cdecl"):
        continue
    ecs_get_target = _lib.get("ecs_get_target", "cdecl")
    ecs_get_target.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        ecs_entity_t,
        c_int32,
    ]
    ecs_get_target.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 7497
for _lib in _libs.values():
    if not _lib.has("ecs_get_parent", "cdecl"):
        continue
    ecs_get_parent = _lib.get("ecs_get_parent", "cdecl")
    ecs_get_parent.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_get_parent.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 7522
for _lib in _libs.values():
    if not _lib.has("ecs_get_target_for_id", "cdecl"):
        continue
    ecs_get_target_for_id = _lib.get("ecs_get_target_for_id", "cdecl")
    ecs_get_target_for_id.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        ecs_entity_t,
        ecs_id_t,
    ]
    ecs_get_target_for_id.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 7539
for _lib in _libs.values():
    if not _lib.has("ecs_get_depth", "cdecl"):
        continue
    ecs_get_depth = _lib.get("ecs_get_depth", "cdecl")
    ecs_get_depth.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_entity_t]
    ecs_get_depth.restype = c_int32
    break

# vendor/flecs/flecs.h: 7552
for _lib in _libs.values():
    if not _lib.has("ecs_count_id", "cdecl"):
        continue
    ecs_count_id = _lib.get("ecs_count_id", "cdecl")
    ecs_count_id.argtypes = [POINTER(ecs_world_t), ecs_id_t]
    ecs_count_id.restype = c_int32
    break

# vendor/flecs/flecs.h: 7576
for _lib in _libs.values():
    if not _lib.has("ecs_get_name", "cdecl"):
        continue
    ecs_get_name = _lib.get("ecs_get_name", "cdecl")
    ecs_get_name.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_get_name.restype = c_char_p
    break

# vendor/flecs/flecs.h: 7590
for _lib in _libs.values():
    if not _lib.has("ecs_get_symbol", "cdecl"):
        continue
    ecs_get_symbol = _lib.get("ecs_get_symbol", "cdecl")
    ecs_get_symbol.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_get_symbol.restype = c_char_p
    break

# vendor/flecs/flecs.h: 7608
for _lib in _libs.values():
    if not _lib.has("ecs_set_name", "cdecl"):
        continue
    ecs_set_name = _lib.get("ecs_set_name", "cdecl")
    ecs_set_name.argtypes = [POINTER(ecs_world_t), ecs_entity_t, String]
    ecs_set_name.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 7627
for _lib in _libs.values():
    if not _lib.has("ecs_set_symbol", "cdecl"):
        continue
    ecs_set_symbol = _lib.get("ecs_set_symbol", "cdecl")
    ecs_set_symbol.argtypes = [POINTER(ecs_world_t), ecs_entity_t, String]
    ecs_set_symbol.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 7644
for _lib in _libs.values():
    if not _lib.has("ecs_set_alias", "cdecl"):
        continue
    ecs_set_alias = _lib.get("ecs_set_alias", "cdecl")
    ecs_set_alias.argtypes = [POINTER(ecs_world_t), ecs_entity_t, String]
    ecs_set_alias.restype = None
    break

# vendor/flecs/flecs.h: 7665
for _lib in _libs.values():
    if not _lib.has("ecs_lookup", "cdecl"):
        continue
    ecs_lookup = _lib.get("ecs_lookup", "cdecl")
    ecs_lookup.argtypes = [POINTER(ecs_world_t), String]
    ecs_lookup.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 7684
for _lib in _libs.values():
    if not _lib.has("ecs_lookup_child", "cdecl"):
        continue
    ecs_lookup_child = _lib.get("ecs_lookup_child", "cdecl")
    ecs_lookup_child.argtypes = [POINTER(ecs_world_t), ecs_entity_t, String]
    ecs_lookup_child.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 7712
for _lib in _libs.values():
    if not _lib.has("ecs_lookup_path_w_sep", "cdecl"):
        continue
    ecs_lookup_path_w_sep = _lib.get("ecs_lookup_path_w_sep", "cdecl")
    ecs_lookup_path_w_sep.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        String,
        String,
        String,
        c_bool,
    ]
    ecs_lookup_path_w_sep.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 7738
for _lib in _libs.values():
    if not _lib.has("ecs_lookup_symbol", "cdecl"):
        continue
    ecs_lookup_symbol = _lib.get("ecs_lookup_symbol", "cdecl")
    ecs_lookup_symbol.argtypes = [POINTER(ecs_world_t), String, c_bool, c_bool]
    ecs_lookup_symbol.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 7766
for _lib in _libs.values():
    if not _lib.has("ecs_get_path_w_sep", "cdecl"):
        continue
    ecs_get_path_w_sep = _lib.get("ecs_get_path_w_sep", "cdecl")
    ecs_get_path_w_sep.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        ecs_entity_t,
        String,
        String,
    ]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_get_path_w_sep.restype = ReturnString
    else:
        ecs_get_path_w_sep.restype = String
        ecs_get_path_w_sep.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 7786
for _lib in _libs.values():
    if not _lib.has("ecs_get_path_w_sep_buf", "cdecl"):
        continue
    ecs_get_path_w_sep_buf = _lib.get("ecs_get_path_w_sep_buf", "cdecl")
    ecs_get_path_w_sep_buf.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        ecs_entity_t,
        String,
        String,
        POINTER(ecs_strbuf_t),
        c_bool,
    ]
    ecs_get_path_w_sep_buf.restype = None
    break

# vendor/flecs/flecs.h: 7811
for _lib in _libs.values():
    if not _lib.has("ecs_new_from_path_w_sep", "cdecl"):
        continue
    ecs_new_from_path_w_sep = _lib.get("ecs_new_from_path_w_sep", "cdecl")
    ecs_new_from_path_w_sep.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        String,
        String,
        String,
    ]
    ecs_new_from_path_w_sep.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 7833
for _lib in _libs.values():
    if not _lib.has("ecs_add_path_w_sep", "cdecl"):
        continue
    ecs_add_path_w_sep = _lib.get("ecs_add_path_w_sep", "cdecl")
    ecs_add_path_w_sep.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        ecs_entity_t,
        String,
        String,
        String,
    ]
    ecs_add_path_w_sep.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 7855
for _lib in _libs.values():
    if not _lib.has("ecs_set_scope", "cdecl"):
        continue
    ecs_set_scope = _lib.get("ecs_set_scope", "cdecl")
    ecs_set_scope.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_set_scope.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 7867
for _lib in _libs.values():
    if not _lib.has("ecs_get_scope", "cdecl"):
        continue
    ecs_get_scope = _lib.get("ecs_get_scope", "cdecl")
    ecs_get_scope.argtypes = [POINTER(ecs_world_t)]
    ecs_get_scope.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 7880
for _lib in _libs.values():
    if not _lib.has("ecs_set_name_prefix", "cdecl"):
        continue
    ecs_set_name_prefix = _lib.get("ecs_set_name_prefix", "cdecl")
    ecs_set_name_prefix.argtypes = [POINTER(ecs_world_t), String]
    ecs_set_name_prefix.restype = c_char_p
    break

# vendor/flecs/flecs.h: 7911
for _lib in _libs.values():
    if not _lib.has("ecs_set_lookup_path", "cdecl"):
        continue
    ecs_set_lookup_path = _lib.get("ecs_set_lookup_path", "cdecl")
    ecs_set_lookup_path.argtypes = [POINTER(ecs_world_t), POINTER(ecs_entity_t)]
    ecs_set_lookup_path.restype = POINTER(ecs_entity_t)
    break

# vendor/flecs/flecs.h: 7922
for _lib in _libs.values():
    if not _lib.has("ecs_get_lookup_path", "cdecl"):
        continue
    ecs_get_lookup_path = _lib.get("ecs_get_lookup_path", "cdecl")
    ecs_get_lookup_path.argtypes = [POINTER(ecs_world_t)]
    ecs_get_lookup_path.restype = POINTER(ecs_entity_t)
    break

# vendor/flecs/flecs.h: 7950
for _lib in _libs.values():
    if not _lib.has("ecs_component_init", "cdecl"):
        continue
    ecs_component_init = _lib.get("ecs_component_init", "cdecl")
    ecs_component_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_component_desc_t)]
    ecs_component_init.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 7964
for _lib in _libs.values():
    if not _lib.has("ecs_get_type_info", "cdecl"):
        continue
    ecs_get_type_info = _lib.get("ecs_get_type_info", "cdecl")
    ecs_get_type_info.argtypes = [POINTER(ecs_world_t), ecs_id_t]
    ecs_get_type_info.restype = POINTER(ecs_type_info_t)
    break

# vendor/flecs/flecs.h: 7980
for _lib in _libs.values():
    if not _lib.has("ecs_set_hooks_id", "cdecl"):
        continue
    ecs_set_hooks_id = _lib.get("ecs_set_hooks_id", "cdecl")
    ecs_set_hooks_id.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        POINTER(ecs_type_hooks_t),
    ]
    ecs_set_hooks_id.restype = None
    break

# vendor/flecs/flecs.h: 7992
for _lib in _libs.values():
    if not _lib.has("ecs_get_hooks_id", "cdecl"):
        continue
    ecs_get_hooks_id = _lib.get("ecs_get_hooks_id", "cdecl")
    ecs_get_hooks_id.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_get_hooks_id.restype = POINTER(ecs_type_hooks_t)
    break

# vendor/flecs/flecs.h: 8020
for _lib in _libs.values():
    if not _lib.has("ecs_id_is_tag", "cdecl"):
        continue
    ecs_id_is_tag = _lib.get("ecs_id_is_tag", "cdecl")
    ecs_id_is_tag.argtypes = [POINTER(ecs_world_t), ecs_id_t]
    ecs_id_is_tag.restype = c_bool
    break

# vendor/flecs/flecs.h: 8033
for _lib in _libs.values():
    if not _lib.has("ecs_id_in_use", "cdecl"):
        continue
    ecs_id_in_use = _lib.get("ecs_id_in_use", "cdecl")
    ecs_id_in_use.argtypes = [POINTER(ecs_world_t), ecs_id_t]
    ecs_id_in_use.restype = c_bool
    break

# vendor/flecs/flecs.h: 8057
for _lib in _libs.values():
    if not _lib.has("ecs_get_typeid", "cdecl"):
        continue
    ecs_get_typeid = _lib.get("ecs_get_typeid", "cdecl")
    ecs_get_typeid.argtypes = [POINTER(ecs_world_t), ecs_id_t]
    ecs_get_typeid.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 8070
for _lib in _libs.values():
    if not _lib.has("ecs_id_match", "cdecl"):
        continue
    ecs_id_match = _lib.get("ecs_id_match", "cdecl")
    ecs_id_match.argtypes = [ecs_id_t, ecs_id_t]
    ecs_id_match.restype = c_bool
    break

# vendor/flecs/flecs.h: 8080
for _lib in _libs.values():
    if not _lib.has("ecs_id_is_pair", "cdecl"):
        continue
    ecs_id_is_pair = _lib.get("ecs_id_is_pair", "cdecl")
    ecs_id_is_pair.argtypes = [ecs_id_t]
    ecs_id_is_pair.restype = c_bool
    break

# vendor/flecs/flecs.h: 8089
for _lib in _libs.values():
    if not _lib.has("ecs_id_is_wildcard", "cdecl"):
        continue
    ecs_id_is_wildcard = _lib.get("ecs_id_is_wildcard", "cdecl")
    ecs_id_is_wildcard.argtypes = [ecs_id_t]
    ecs_id_is_wildcard.restype = c_bool
    break

# vendor/flecs/flecs.h: 8097
for _lib in _libs.values():
    if not _lib.has("ecs_id_is_any", "cdecl"):
        continue
    ecs_id_is_any = _lib.get("ecs_id_is_any", "cdecl")
    ecs_id_is_any.argtypes = [ecs_id_t]
    ecs_id_is_any.restype = c_bool
    break

# vendor/flecs/flecs.h: 8114
for _lib in _libs.values():
    if not _lib.has("ecs_id_is_valid", "cdecl"):
        continue
    ecs_id_is_valid = _lib.get("ecs_id_is_valid", "cdecl")
    ecs_id_is_valid.argtypes = [POINTER(ecs_world_t), ecs_id_t]
    ecs_id_is_valid.restype = c_bool
    break

# vendor/flecs/flecs.h: 8127
for _lib in _libs.values():
    if not _lib.has("ecs_id_get_flags", "cdecl"):
        continue
    ecs_id_get_flags = _lib.get("ecs_id_get_flags", "cdecl")
    ecs_id_get_flags.argtypes = [POINTER(ecs_world_t), ecs_id_t]
    ecs_id_get_flags.restype = ecs_flags32_t
    break

# vendor/flecs/flecs.h: 8138
for _lib in _libs.values():
    if not _lib.has("ecs_id_flag_str", "cdecl"):
        continue
    ecs_id_flag_str = _lib.get("ecs_id_flag_str", "cdecl")
    ecs_id_flag_str.argtypes = [ecs_id_t]
    ecs_id_flag_str.restype = c_char_p
    break

# vendor/flecs/flecs.h: 8149
for _lib in _libs.values():
    if not _lib.has("ecs_id_str", "cdecl"):
        continue
    ecs_id_str = _lib.get("ecs_id_str", "cdecl")
    ecs_id_str.argtypes = [POINTER(ecs_world_t), ecs_id_t]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_id_str.restype = ReturnString
    else:
        ecs_id_str.restype = String
        ecs_id_str.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 8161
for _lib in _libs.values():
    if not _lib.has("ecs_id_str_buf", "cdecl"):
        continue
    ecs_id_str_buf = _lib.get("ecs_id_str_buf", "cdecl")
    ecs_id_str_buf.argtypes = [POINTER(ecs_world_t), ecs_id_t, POINTER(ecs_strbuf_t)]
    ecs_id_str_buf.restype = None
    break

# vendor/flecs/flecs.h: 8174
for _lib in _libs.values():
    if not _lib.has("ecs_id_from_str", "cdecl"):
        continue
    ecs_id_from_str = _lib.get("ecs_id_from_str", "cdecl")
    ecs_id_from_str.argtypes = [POINTER(ecs_world_t), String]
    ecs_id_from_str.restype = ecs_id_t
    break

# vendor/flecs/flecs.h: 8192
for _lib in _libs.values():
    if not _lib.has("ecs_term_ref_is_set", "cdecl"):
        continue
    ecs_term_ref_is_set = _lib.get("ecs_term_ref_is_set", "cdecl")
    ecs_term_ref_is_set.argtypes = [POINTER(ecs_term_ref_t)]
    ecs_term_ref_is_set.restype = c_bool
    break

# vendor/flecs/flecs.h: 8207
for _lib in _libs.values():
    if not _lib.has("ecs_term_is_initialized", "cdecl"):
        continue
    ecs_term_is_initialized = _lib.get("ecs_term_is_initialized", "cdecl")
    ecs_term_is_initialized.argtypes = [POINTER(ecs_term_t)]
    ecs_term_is_initialized.restype = c_bool
    break

# vendor/flecs/flecs.h: 8225
for _lib in _libs.values():
    if not _lib.has("ecs_term_match_this", "cdecl"):
        continue
    ecs_term_match_this = _lib.get("ecs_term_match_this", "cdecl")
    ecs_term_match_this.argtypes = [POINTER(ecs_term_t)]
    ecs_term_match_this.restype = c_bool
    break

# vendor/flecs/flecs.h: 8241
for _lib in _libs.values():
    if not _lib.has("ecs_term_match_0", "cdecl"):
        continue
    ecs_term_match_0 = _lib.get("ecs_term_match_0", "cdecl")
    ecs_term_match_0.argtypes = [POINTER(ecs_term_t)]
    ecs_term_match_0.restype = c_bool
    break

# vendor/flecs/flecs.h: 8253
for _lib in _libs.values():
    if not _lib.has("ecs_term_str", "cdecl"):
        continue
    ecs_term_str = _lib.get("ecs_term_str", "cdecl")
    ecs_term_str.argtypes = [POINTER(ecs_world_t), POINTER(ecs_term_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_term_str.restype = ReturnString
    else:
        ecs_term_str.restype = String
        ecs_term_str.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 8265
for _lib in _libs.values():
    if not _lib.has("ecs_query_str", "cdecl"):
        continue
    ecs_query_str = _lib.get("ecs_query_str", "cdecl")
    ecs_query_str.argtypes = [POINTER(ecs_query_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_query_str.restype = ReturnString
    else:
        ecs_query_str.restype = String
        ecs_query_str.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 8309
for _lib in _libs.values():
    if not _lib.has("ecs_each_id", "cdecl"):
        continue
    ecs_each_id = _lib.get("ecs_each_id", "cdecl")
    ecs_each_id.argtypes = [POINTER(ecs_world_t), ecs_id_t]
    ecs_each_id.restype = ecs_iter_t
    break

# vendor/flecs/flecs.h: 8319
for _lib in _libs.values():
    if not _lib.has("ecs_each_next", "cdecl"):
        continue
    ecs_each_next = _lib.get("ecs_each_next", "cdecl")
    ecs_each_next.argtypes = [POINTER(ecs_iter_t)]
    ecs_each_next.restype = c_bool
    break

# vendor/flecs/flecs.h: 8339
for _lib in _libs.values():
    if not _lib.has("ecs_children", "cdecl"):
        continue
    ecs_children = _lib.get("ecs_children", "cdecl")
    ecs_children.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_children.restype = ecs_iter_t
    break

# vendor/flecs/flecs.h: 8349
for _lib in _libs.values():
    if not _lib.has("ecs_children_next", "cdecl"):
        continue
    ecs_children_next = _lib.get("ecs_children_next", "cdecl")
    ecs_children_next.argtypes = [POINTER(ecs_iter_t)]
    ecs_children_next.restype = c_bool
    break

# vendor/flecs/flecs.h: 8368
for _lib in _libs.values():
    if not _lib.has("ecs_query_init", "cdecl"):
        continue
    ecs_query_init = _lib.get("ecs_query_init", "cdecl")
    ecs_query_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_query_desc_t)]
    ecs_query_init.restype = POINTER(ecs_query_t)
    break

# vendor/flecs/flecs.h: 8377
for _lib in _libs.values():
    if not _lib.has("ecs_query_fini", "cdecl"):
        continue
    ecs_query_fini = _lib.get("ecs_query_fini", "cdecl")
    ecs_query_fini.argtypes = [POINTER(ecs_query_t)]
    ecs_query_fini.restype = None
    break

# vendor/flecs/flecs.h: 8389
for _lib in _libs.values():
    if not _lib.has("ecs_query_find_var", "cdecl"):
        continue
    ecs_query_find_var = _lib.get("ecs_query_find_var", "cdecl")
    ecs_query_find_var.argtypes = [POINTER(ecs_query_t), String]
    ecs_query_find_var.restype = c_int32
    break

# vendor/flecs/flecs.h: 8401
for _lib in _libs.values():
    if not _lib.has("ecs_query_var_name", "cdecl"):
        continue
    ecs_query_var_name = _lib.get("ecs_query_var_name", "cdecl")
    ecs_query_var_name.argtypes = [POINTER(ecs_query_t), c_int32]
    ecs_query_var_name.restype = c_char_p
    break

# vendor/flecs/flecs.h: 8416
for _lib in _libs.values():
    if not _lib.has("ecs_query_var_is_entity", "cdecl"):
        continue
    ecs_query_var_is_entity = _lib.get("ecs_query_var_is_entity", "cdecl")
    ecs_query_var_is_entity.argtypes = [POINTER(ecs_query_t), c_int32]
    ecs_query_var_is_entity.restype = c_bool
    break

# vendor/flecs/flecs.h: 8489
for _lib in _libs.values():
    if not _lib.has("ecs_query_iter", "cdecl"):
        continue
    ecs_query_iter = _lib.get("ecs_query_iter", "cdecl")
    ecs_query_iter.argtypes = [POINTER(ecs_world_t), POINTER(ecs_query_t)]
    ecs_query_iter.restype = ecs_iter_t
    break

# vendor/flecs/flecs.h: 8501
for _lib in _libs.values():
    if not _lib.has("ecs_query_next", "cdecl"):
        continue
    ecs_query_next = _lib.get("ecs_query_next", "cdecl")
    ecs_query_next.argtypes = [POINTER(ecs_iter_t)]
    ecs_query_next.restype = c_bool
    break

# vendor/flecs/flecs.h: 8523
for _lib in _libs.values():
    if not _lib.has("ecs_query_has", "cdecl"):
        continue
    ecs_query_has = _lib.get("ecs_query_has", "cdecl")
    ecs_query_has.argtypes = [POINTER(ecs_query_t), ecs_entity_t, POINTER(ecs_iter_t)]
    ecs_query_has.restype = c_bool
    break

# vendor/flecs/flecs.h: 8547
for _lib in _libs.values():
    if not _lib.has("ecs_query_has_table", "cdecl"):
        continue
    ecs_query_has_table = _lib.get("ecs_query_has_table", "cdecl")
    ecs_query_has_table.argtypes = [
        POINTER(ecs_query_t),
        POINTER(ecs_table_t),
        POINTER(ecs_iter_t),
    ]
    ecs_query_has_table.restype = c_bool
    break

# vendor/flecs/flecs.h: 8579
for _lib in _libs.values():
    if not _lib.has("ecs_query_has_range", "cdecl"):
        continue
    ecs_query_has_range = _lib.get("ecs_query_has_range", "cdecl")
    ecs_query_has_range.argtypes = [
        POINTER(ecs_query_t),
        POINTER(ecs_table_range_t),
        POINTER(ecs_iter_t),
    ]
    ecs_query_has_range.restype = c_bool
    break

# vendor/flecs/flecs.h: 8592
for _lib in _libs.values():
    if not _lib.has("ecs_query_match_count", "cdecl"):
        continue
    ecs_query_match_count = _lib.get("ecs_query_match_count", "cdecl")
    ecs_query_match_count.argtypes = [POINTER(ecs_query_t)]
    ecs_query_match_count.restype = c_int32
    break

# vendor/flecs/flecs.h: 8605
for _lib in _libs.values():
    if not _lib.has("ecs_query_plan", "cdecl"):
        continue
    ecs_query_plan = _lib.get("ecs_query_plan", "cdecl")
    ecs_query_plan.argtypes = [POINTER(ecs_query_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_query_plan.restype = ReturnString
    else:
        ecs_query_plan.restype = String
        ecs_query_plan.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 8623
for _lib in _libs.values():
    if not _lib.has("ecs_query_plan_w_profile", "cdecl"):
        continue
    ecs_query_plan_w_profile = _lib.get("ecs_query_plan_w_profile", "cdecl")
    ecs_query_plan_w_profile.argtypes = [POINTER(ecs_query_t), POINTER(ecs_iter_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_query_plan_w_profile.restype = ReturnString
    else:
        ecs_query_plan_w_profile.restype = String
        ecs_query_plan_w_profile.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 8645
for _lib in _libs.values():
    if not _lib.has("ecs_query_args_parse", "cdecl"):
        continue
    ecs_query_args_parse = _lib.get("ecs_query_args_parse", "cdecl")
    ecs_query_args_parse.argtypes = [POINTER(ecs_query_t), POINTER(ecs_iter_t), String]
    ecs_query_args_parse.restype = c_char_p
    break

# vendor/flecs/flecs.h: 8678
for _lib in _libs.values():
    if not _lib.has("ecs_query_changed", "cdecl"):
        continue
    ecs_query_changed = _lib.get("ecs_query_changed", "cdecl")
    ecs_query_changed.argtypes = [POINTER(ecs_query_t)]
    ecs_query_changed.restype = c_bool
    break

# vendor/flecs/flecs.h: 8690
for _lib in _libs.values():
    if not _lib.has("ecs_query_get", "cdecl"):
        continue
    ecs_query_get = _lib.get("ecs_query_get", "cdecl")
    ecs_query_get.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_query_get.restype = POINTER(ecs_query_t)
    break

# vendor/flecs/flecs.h: 8705
for _lib in _libs.values():
    if not _lib.has("ecs_iter_skip", "cdecl"):
        continue
    ecs_iter_skip = _lib.get("ecs_iter_skip", "cdecl")
    ecs_iter_skip.argtypes = [POINTER(ecs_iter_t)]
    ecs_iter_skip.restype = None
    break

# vendor/flecs/flecs.h: 8731
for _lib in _libs.values():
    if not _lib.has("ecs_iter_set_group", "cdecl"):
        continue
    ecs_iter_set_group = _lib.get("ecs_iter_set_group", "cdecl")
    ecs_iter_set_group.argtypes = [POINTER(ecs_iter_t), uint64_t]
    ecs_iter_set_group.restype = None
    break

# vendor/flecs/flecs.h: 8744
for _lib in _libs.values():
    if not _lib.has("ecs_query_get_group_ctx", "cdecl"):
        continue
    ecs_query_get_group_ctx = _lib.get("ecs_query_get_group_ctx", "cdecl")
    ecs_query_get_group_ctx.argtypes = [POINTER(ecs_query_t), uint64_t]
    ecs_query_get_group_ctx.restype = POINTER(c_ubyte)
    ecs_query_get_group_ctx.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 8757
for _lib in _libs.values():
    if not _lib.has("ecs_query_get_group_info", "cdecl"):
        continue
    ecs_query_get_group_info = _lib.get("ecs_query_get_group_info", "cdecl")
    ecs_query_get_group_info.argtypes = [POINTER(ecs_query_t), uint64_t]
    ecs_query_get_group_info.restype = POINTER(ecs_query_group_info_t)
    break


# vendor/flecs/flecs.h: 8768
class struct_ecs_query_count_t(Structure):
    pass


struct_ecs_query_count_t.__slots__ = [
    "results",
    "entities",
    "tables",
]
struct_ecs_query_count_t._fields_ = [
    ("results", c_int32),
    ("entities", c_int32),
    ("tables", c_int32),
]

ecs_query_count_t = struct_ecs_query_count_t  # vendor/flecs/flecs.h: 8768

# vendor/flecs/flecs.h: 8777
for _lib in _libs.values():
    if not _lib.has("ecs_query_count", "cdecl"):
        continue
    ecs_query_count = _lib.get("ecs_query_count", "cdecl")
    ecs_query_count.argtypes = [POINTER(ecs_query_t)]
    ecs_query_count.restype = ecs_query_count_t
    break

# vendor/flecs/flecs.h: 8786
for _lib in _libs.values():
    if not _lib.has("ecs_query_is_true", "cdecl"):
        continue
    ecs_query_is_true = _lib.get("ecs_query_is_true", "cdecl")
    ecs_query_is_true.argtypes = [POINTER(ecs_query_t)]
    ecs_query_is_true.restype = c_bool
    break

# vendor/flecs/flecs.h: 8798
for _lib in _libs.values():
    if not _lib.has("ecs_query_get_cache_query", "cdecl"):
        continue
    ecs_query_get_cache_query = _lib.get("ecs_query_get_cache_query", "cdecl")
    ecs_query_get_cache_query.argtypes = [POINTER(ecs_query_t)]
    ecs_query_get_cache_query.restype = POINTER(ecs_query_t)
    break

# vendor/flecs/flecs.h: 8830
for _lib in _libs.values():
    if not _lib.has("ecs_emit", "cdecl"):
        continue
    ecs_emit = _lib.get("ecs_emit", "cdecl")
    ecs_emit.argtypes = [POINTER(ecs_world_t), POINTER(ecs_event_desc_t)]
    ecs_emit.restype = None
    break

# vendor/flecs/flecs.h: 8845
for _lib in _libs.values():
    if not _lib.has("ecs_enqueue", "cdecl"):
        continue
    ecs_enqueue = _lib.get("ecs_enqueue", "cdecl")
    ecs_enqueue.argtypes = [POINTER(ecs_world_t), POINTER(ecs_event_desc_t)]
    ecs_enqueue.restype = None
    break

# vendor/flecs/flecs.h: 8860
for _lib in _libs.values():
    if not _lib.has("ecs_observer_init", "cdecl"):
        continue
    ecs_observer_init = _lib.get("ecs_observer_init", "cdecl")
    ecs_observer_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_observer_desc_t)]
    ecs_observer_init.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 8873
for _lib in _libs.values():
    if not _lib.has("ecs_observer_get", "cdecl"):
        continue
    ecs_observer_get = _lib.get("ecs_observer_get", "cdecl")
    ecs_observer_get.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_observer_get.restype = POINTER(ecs_observer_t)
    break

# vendor/flecs/flecs.h: 8900
for _lib in _libs.values():
    if not _lib.has("ecs_iter_next", "cdecl"):
        continue
    ecs_iter_next = _lib.get("ecs_iter_next", "cdecl")
    ecs_iter_next.argtypes = [POINTER(ecs_iter_t)]
    ecs_iter_next.restype = c_bool
    break

# vendor/flecs/flecs.h: 8913
for _lib in _libs.values():
    if not _lib.has("ecs_iter_fini", "cdecl"):
        continue
    ecs_iter_fini = _lib.get("ecs_iter_fini", "cdecl")
    ecs_iter_fini.argtypes = [POINTER(ecs_iter_t)]
    ecs_iter_fini.restype = None
    break

# vendor/flecs/flecs.h: 8928
for _lib in _libs.values():
    if not _lib.has("ecs_iter_count", "cdecl"):
        continue
    ecs_iter_count = _lib.get("ecs_iter_count", "cdecl")
    ecs_iter_count.argtypes = [POINTER(ecs_iter_t)]
    ecs_iter_count.restype = c_int32
    break

# vendor/flecs/flecs.h: 8944
for _lib in _libs.values():
    if not _lib.has("ecs_iter_is_true", "cdecl"):
        continue
    ecs_iter_is_true = _lib.get("ecs_iter_is_true", "cdecl")
    ecs_iter_is_true.argtypes = [POINTER(ecs_iter_t)]
    ecs_iter_is_true.restype = c_bool
    break

# vendor/flecs/flecs.h: 8955
for _lib in _libs.values():
    if not _lib.has("ecs_iter_first", "cdecl"):
        continue
    ecs_iter_first = _lib.get("ecs_iter_first", "cdecl")
    ecs_iter_first.argtypes = [POINTER(ecs_iter_t)]
    ecs_iter_first.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 8997
for _lib in _libs.values():
    if not _lib.has("ecs_iter_set_var", "cdecl"):
        continue
    ecs_iter_set_var = _lib.get("ecs_iter_set_var", "cdecl")
    ecs_iter_set_var.argtypes = [POINTER(ecs_iter_t), c_int32, ecs_entity_t]
    ecs_iter_set_var.restype = None
    break

# vendor/flecs/flecs.h: 9013
for _lib in _libs.values():
    if not _lib.has("ecs_iter_set_var_as_table", "cdecl"):
        continue
    ecs_iter_set_var_as_table = _lib.get("ecs_iter_set_var_as_table", "cdecl")
    ecs_iter_set_var_as_table.argtypes = [
        POINTER(ecs_iter_t),
        c_int32,
        POINTER(ecs_table_t),
    ]
    ecs_iter_set_var_as_table.restype = None
    break

# vendor/flecs/flecs.h: 9029
for _lib in _libs.values():
    if not _lib.has("ecs_iter_set_var_as_range", "cdecl"):
        continue
    ecs_iter_set_var_as_range = _lib.get("ecs_iter_set_var_as_range", "cdecl")
    ecs_iter_set_var_as_range.argtypes = [
        POINTER(ecs_iter_t),
        c_int32,
        POINTER(ecs_table_range_t),
    ]
    ecs_iter_set_var_as_range.restype = None
    break

# vendor/flecs/flecs.h: 9047
for _lib in _libs.values():
    if not _lib.has("ecs_iter_get_var", "cdecl"):
        continue
    ecs_iter_get_var = _lib.get("ecs_iter_get_var", "cdecl")
    ecs_iter_get_var.argtypes = [POINTER(ecs_iter_t), c_int32]
    ecs_iter_get_var.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 9058
for _lib in _libs.values():
    if not _lib.has("ecs_iter_get_var_name", "cdecl"):
        continue
    ecs_iter_get_var_name = _lib.get("ecs_iter_get_var_name", "cdecl")
    ecs_iter_get_var_name.argtypes = [POINTER(ecs_iter_t), c_int32]
    ecs_iter_get_var_name.restype = c_char_p
    break

# vendor/flecs/flecs.h: 9068
for _lib in _libs.values():
    if not _lib.has("ecs_iter_get_var_count", "cdecl"):
        continue
    ecs_iter_get_var_count = _lib.get("ecs_iter_get_var_count", "cdecl")
    ecs_iter_get_var_count.argtypes = [POINTER(ecs_iter_t)]
    ecs_iter_get_var_count.restype = c_int32
    break

# vendor/flecs/flecs.h: 9077
for _lib in _libs.values():
    if not _lib.has("ecs_iter_get_vars", "cdecl"):
        continue
    ecs_iter_get_vars = _lib.get("ecs_iter_get_vars", "cdecl")
    ecs_iter_get_vars.argtypes = [POINTER(ecs_iter_t)]
    ecs_iter_get_vars.restype = POINTER(ecs_var_t)
    break

# vendor/flecs/flecs.h: 9094
for _lib in _libs.values():
    if not _lib.has("ecs_iter_get_var_as_table", "cdecl"):
        continue
    ecs_iter_get_var_as_table = _lib.get("ecs_iter_get_var_as_table", "cdecl")
    ecs_iter_get_var_as_table.argtypes = [POINTER(ecs_iter_t), c_int32]
    ecs_iter_get_var_as_table.restype = POINTER(ecs_table_t)
    break

# vendor/flecs/flecs.h: 9112
for _lib in _libs.values():
    if not _lib.has("ecs_iter_get_var_as_range", "cdecl"):
        continue
    ecs_iter_get_var_as_range = _lib.get("ecs_iter_get_var_as_range", "cdecl")
    ecs_iter_get_var_as_range.argtypes = [POINTER(ecs_iter_t), c_int32]
    ecs_iter_get_var_as_range.restype = ecs_table_range_t
    break

# vendor/flecs/flecs.h: 9128
for _lib in _libs.values():
    if not _lib.has("ecs_iter_var_is_constrained", "cdecl"):
        continue
    ecs_iter_var_is_constrained = _lib.get("ecs_iter_var_is_constrained", "cdecl")
    ecs_iter_var_is_constrained.argtypes = [POINTER(ecs_iter_t), c_int32]
    ecs_iter_var_is_constrained.restype = c_bool
    break

# vendor/flecs/flecs.h: 9144
for _lib in _libs.values():
    if not _lib.has("ecs_iter_get_group", "cdecl"):
        continue
    ecs_iter_get_group = _lib.get("ecs_iter_get_group", "cdecl")
    ecs_iter_get_group.argtypes = [POINTER(ecs_iter_t)]
    ecs_iter_get_group.restype = uint64_t
    break

# vendor/flecs/flecs.h: 9159
for _lib in _libs.values():
    if not _lib.has("ecs_iter_changed", "cdecl"):
        continue
    ecs_iter_changed = _lib.get("ecs_iter_changed", "cdecl")
    ecs_iter_changed.argtypes = [POINTER(ecs_iter_t)]
    ecs_iter_changed.restype = c_bool
    break

# vendor/flecs/flecs.h: 9174
for _lib in _libs.values():
    if not _lib.has("ecs_iter_str", "cdecl"):
        continue
    ecs_iter_str = _lib.get("ecs_iter_str", "cdecl")
    ecs_iter_str.argtypes = [POINTER(ecs_iter_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_iter_str.restype = ReturnString
    else:
        ecs_iter_str.restype = String
        ecs_iter_str.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 9193
for _lib in _libs.values():
    if not _lib.has("ecs_page_iter", "cdecl"):
        continue
    ecs_page_iter = _lib.get("ecs_page_iter", "cdecl")
    ecs_page_iter.argtypes = [POINTER(ecs_iter_t), c_int32, c_int32]
    ecs_page_iter.restype = ecs_iter_t
    break

# vendor/flecs/flecs.h: 9205
for _lib in _libs.values():
    if not _lib.has("ecs_page_next", "cdecl"):
        continue
    ecs_page_next = _lib.get("ecs_page_next", "cdecl")
    ecs_page_next.argtypes = [POINTER(ecs_iter_t)]
    ecs_page_next.restype = c_bool
    break

# vendor/flecs/flecs.h: 9229
for _lib in _libs.values():
    if not _lib.has("ecs_worker_iter", "cdecl"):
        continue
    ecs_worker_iter = _lib.get("ecs_worker_iter", "cdecl")
    ecs_worker_iter.argtypes = [POINTER(ecs_iter_t), c_int32, c_int32]
    ecs_worker_iter.restype = ecs_iter_t
    break

# vendor/flecs/flecs.h: 9241
for _lib in _libs.values():
    if not _lib.has("ecs_worker_next", "cdecl"):
        continue
    ecs_worker_next = _lib.get("ecs_worker_next", "cdecl")
    ecs_worker_next.argtypes = [POINTER(ecs_iter_t)]
    ecs_worker_next.restype = c_bool
    break

# vendor/flecs/flecs.h: 9286
for _lib in _libs.values():
    if not _lib.has("ecs_field_w_size", "cdecl"):
        continue
    ecs_field_w_size = _lib.get("ecs_field_w_size", "cdecl")
    ecs_field_w_size.argtypes = [POINTER(ecs_iter_t), c_size_t, c_int8]
    ecs_field_w_size.restype = POINTER(c_ubyte)
    ecs_field_w_size.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 9313
for _lib in _libs.values():
    if not _lib.has("ecs_field_at_w_size", "cdecl"):
        continue
    ecs_field_at_w_size = _lib.get("ecs_field_at_w_size", "cdecl")
    ecs_field_at_w_size.argtypes = [POINTER(ecs_iter_t), c_size_t, c_int8, c_int32]
    ecs_field_at_w_size.restype = POINTER(c_ubyte)
    ecs_field_at_w_size.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 9328
for _lib in _libs.values():
    if not _lib.has("ecs_field_is_readonly", "cdecl"):
        continue
    ecs_field_is_readonly = _lib.get("ecs_field_is_readonly", "cdecl")
    ecs_field_is_readonly.argtypes = [POINTER(ecs_iter_t), c_int8]
    ecs_field_is_readonly.restype = c_bool
    break

# vendor/flecs/flecs.h: 9343
for _lib in _libs.values():
    if not _lib.has("ecs_field_is_writeonly", "cdecl"):
        continue
    ecs_field_is_writeonly = _lib.get("ecs_field_is_writeonly", "cdecl")
    ecs_field_is_writeonly.argtypes = [POINTER(ecs_iter_t), c_int8]
    ecs_field_is_writeonly.restype = c_bool
    break

# vendor/flecs/flecs.h: 9354
for _lib in _libs.values():
    if not _lib.has("ecs_field_is_set", "cdecl"):
        continue
    ecs_field_is_set = _lib.get("ecs_field_is_set", "cdecl")
    ecs_field_is_set.argtypes = [POINTER(ecs_iter_t), c_int8]
    ecs_field_is_set.restype = c_bool
    break

# vendor/flecs/flecs.h: 9365
for _lib in _libs.values():
    if not _lib.has("ecs_field_id", "cdecl"):
        continue
    ecs_field_id = _lib.get("ecs_field_id", "cdecl")
    ecs_field_id.argtypes = [POINTER(ecs_iter_t), c_int8]
    ecs_field_id.restype = ecs_id_t
    break

# vendor/flecs/flecs.h: 9378
for _lib in _libs.values():
    if not _lib.has("ecs_field_column", "cdecl"):
        continue
    ecs_field_column = _lib.get("ecs_field_column", "cdecl")
    ecs_field_column.argtypes = [POINTER(ecs_iter_t), c_int8]
    ecs_field_column.restype = c_int32
    break

# vendor/flecs/flecs.h: 9390
for _lib in _libs.values():
    if not _lib.has("ecs_field_src", "cdecl"):
        continue
    ecs_field_src = _lib.get("ecs_field_src", "cdecl")
    ecs_field_src.argtypes = [POINTER(ecs_iter_t), c_int8]
    ecs_field_src.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 9402
for _lib in _libs.values():
    if not _lib.has("ecs_field_size", "cdecl"):
        continue
    ecs_field_size = _lib.get("ecs_field_size", "cdecl")
    ecs_field_size.argtypes = [POINTER(ecs_iter_t), c_int8]
    ecs_field_size.restype = c_size_t
    break

# vendor/flecs/flecs.h: 9420
for _lib in _libs.values():
    if not _lib.has("ecs_field_is_self", "cdecl"):
        continue
    ecs_field_is_self = _lib.get("ecs_field_is_self", "cdecl")
    ecs_field_is_self.argtypes = [POINTER(ecs_iter_t), c_int8]
    ecs_field_is_self.restype = c_bool
    break

# vendor/flecs/flecs.h: 9440
for _lib in _libs.values():
    if not _lib.has("ecs_table_get_type", "cdecl"):
        continue
    ecs_table_get_type = _lib.get("ecs_table_get_type", "cdecl")
    ecs_table_get_type.argtypes = [POINTER(ecs_table_t)]
    ecs_table_get_type.restype = POINTER(ecs_type_t)
    break

# vendor/flecs/flecs.h: 9454
for _lib in _libs.values():
    if not _lib.has("ecs_table_get_type_index", "cdecl"):
        continue
    ecs_table_get_type_index = _lib.get("ecs_table_get_type_index", "cdecl")
    ecs_table_get_type_index.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_table_t),
        ecs_id_t,
    ]
    ecs_table_get_type_index.restype = c_int32
    break

# vendor/flecs/flecs.h: 9469
for _lib in _libs.values():
    if not _lib.has("ecs_table_get_column_index", "cdecl"):
        continue
    ecs_table_get_column_index = _lib.get("ecs_table_get_column_index", "cdecl")
    ecs_table_get_column_index.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_table_t),
        ecs_id_t,
    ]
    ecs_table_get_column_index.restype = c_int32
    break

# vendor/flecs/flecs.h: 9482
for _lib in _libs.values():
    if not _lib.has("ecs_table_column_count", "cdecl"):
        continue
    ecs_table_column_count = _lib.get("ecs_table_column_count", "cdecl")
    ecs_table_column_count.argtypes = [POINTER(ecs_table_t)]
    ecs_table_column_count.restype = c_int32
    break

# vendor/flecs/flecs.h: 9499
for _lib in _libs.values():
    if not _lib.has("ecs_table_type_to_column_index", "cdecl"):
        continue
    ecs_table_type_to_column_index = _lib.get("ecs_table_type_to_column_index", "cdecl")
    ecs_table_type_to_column_index.argtypes = [POINTER(ecs_table_t), c_int32]
    ecs_table_type_to_column_index.restype = c_int32
    break

# vendor/flecs/flecs.h: 9512
for _lib in _libs.values():
    if not _lib.has("ecs_table_column_to_type_index", "cdecl"):
        continue
    ecs_table_column_to_type_index = _lib.get("ecs_table_column_to_type_index", "cdecl")
    ecs_table_column_to_type_index.argtypes = [POINTER(ecs_table_t), c_int32]
    ecs_table_column_to_type_index.restype = c_int32
    break

# vendor/flecs/flecs.h: 9525
for _lib in _libs.values():
    if not _lib.has("ecs_table_get_column", "cdecl"):
        continue
    ecs_table_get_column = _lib.get("ecs_table_get_column", "cdecl")
    ecs_table_get_column.argtypes = [POINTER(ecs_table_t), c_int32, c_int32]
    ecs_table_get_column.restype = POINTER(c_ubyte)
    ecs_table_get_column.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 9540
for _lib in _libs.values():
    if not _lib.has("ecs_table_get_id", "cdecl"):
        continue
    ecs_table_get_id = _lib.get("ecs_table_get_id", "cdecl")
    ecs_table_get_id.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_table_t),
        ecs_id_t,
        c_int32,
    ]
    ecs_table_get_id.restype = POINTER(c_ubyte)
    ecs_table_get_id.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 9554
for _lib in _libs.values():
    if not _lib.has("ecs_table_get_column_size", "cdecl"):
        continue
    ecs_table_get_column_size = _lib.get("ecs_table_get_column_size", "cdecl")
    ecs_table_get_column_size.argtypes = [POINTER(ecs_table_t), c_int32]
    ecs_table_get_column_size.restype = c_size_t
    break

# vendor/flecs/flecs.h: 9565
for _lib in _libs.values():
    if not _lib.has("ecs_table_count", "cdecl"):
        continue
    ecs_table_count = _lib.get("ecs_table_count", "cdecl")
    ecs_table_count.argtypes = [POINTER(ecs_table_t)]
    ecs_table_count.restype = c_int32
    break

# vendor/flecs/flecs.h: 9576
for _lib in _libs.values():
    if not _lib.has("ecs_table_size", "cdecl"):
        continue
    ecs_table_size = _lib.get("ecs_table_size", "cdecl")
    ecs_table_size.argtypes = [POINTER(ecs_table_t)]
    ecs_table_size.restype = c_int32
    break

# vendor/flecs/flecs.h: 9586
for _lib in _libs.values():
    if not _lib.has("ecs_table_entities", "cdecl"):
        continue
    ecs_table_entities = _lib.get("ecs_table_entities", "cdecl")
    ecs_table_entities.argtypes = [POINTER(ecs_table_t)]
    ecs_table_entities.restype = POINTER(ecs_entity_t)
    break

# vendor/flecs/flecs.h: 9600
for _lib in _libs.values():
    if not _lib.has("ecs_table_has_id", "cdecl"):
        continue
    ecs_table_has_id = _lib.get("ecs_table_has_id", "cdecl")
    ecs_table_has_id.argtypes = [POINTER(ecs_world_t), POINTER(ecs_table_t), ecs_id_t]
    ecs_table_has_id.restype = c_bool
    break

# vendor/flecs/flecs.h: 9616
for _lib in _libs.values():
    if not _lib.has("ecs_table_get_depth", "cdecl"):
        continue
    ecs_table_get_depth = _lib.get("ecs_table_get_depth", "cdecl")
    ecs_table_get_depth.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_table_t),
        ecs_entity_t,
    ]
    ecs_table_get_depth.restype = c_int32
    break

# vendor/flecs/flecs.h: 9631
for _lib in _libs.values():
    if not _lib.has("ecs_table_add_id", "cdecl"):
        continue
    ecs_table_add_id = _lib.get("ecs_table_add_id", "cdecl")
    ecs_table_add_id.argtypes = [POINTER(ecs_world_t), POINTER(ecs_table_t), ecs_id_t]
    ecs_table_add_id.restype = POINTER(ecs_table_t)
    break

# vendor/flecs/flecs.h: 9647
for _lib in _libs.values():
    if not _lib.has("ecs_table_find", "cdecl"):
        continue
    ecs_table_find = _lib.get("ecs_table_find", "cdecl")
    ecs_table_find.argtypes = [POINTER(ecs_world_t), POINTER(ecs_id_t), c_int32]
    ecs_table_find.restype = POINTER(ecs_table_t)
    break

# vendor/flecs/flecs.h: 9662
for _lib in _libs.values():
    if not _lib.has("ecs_table_remove_id", "cdecl"):
        continue
    ecs_table_remove_id = _lib.get("ecs_table_remove_id", "cdecl")
    ecs_table_remove_id.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_table_t),
        ecs_id_t,
    ]
    ecs_table_remove_id.restype = POINTER(ecs_table_t)
    break

# vendor/flecs/flecs.h: 9683
for _lib in _libs.values():
    if not _lib.has("ecs_table_lock", "cdecl"):
        continue
    ecs_table_lock = _lib.get("ecs_table_lock", "cdecl")
    ecs_table_lock.argtypes = [POINTER(ecs_world_t), POINTER(ecs_table_t)]
    ecs_table_lock.restype = None
    break

# vendor/flecs/flecs.h: 9694
for _lib in _libs.values():
    if not _lib.has("ecs_table_unlock", "cdecl"):
        continue
    ecs_table_unlock = _lib.get("ecs_table_unlock", "cdecl")
    ecs_table_unlock.argtypes = [POINTER(ecs_world_t), POINTER(ecs_table_t)]
    ecs_table_unlock.restype = None
    break

# vendor/flecs/flecs.h: 9708
for _lib in _libs.values():
    if not _lib.has("ecs_table_has_flags", "cdecl"):
        continue
    ecs_table_has_flags = _lib.get("ecs_table_has_flags", "cdecl")
    ecs_table_has_flags.argtypes = [POINTER(ecs_table_t), ecs_flags32_t]
    ecs_table_has_flags.restype = c_bool
    break

# vendor/flecs/flecs.h: 9720
for _lib in _libs.values():
    if not _lib.has("ecs_table_swap_rows", "cdecl"):
        continue
    ecs_table_swap_rows = _lib.get("ecs_table_swap_rows", "cdecl")
    ecs_table_swap_rows.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_table_t),
        c_int32,
        c_int32,
    ]
    ecs_table_swap_rows.restype = None
    break

# vendor/flecs/flecs.h: 9749
for _lib in _libs.values():
    if not _lib.has("ecs_commit", "cdecl"):
        continue
    ecs_commit = _lib.get("ecs_commit", "cdecl")
    ecs_commit.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        POINTER(ecs_record_t),
        POINTER(ecs_table_t),
        POINTER(ecs_type_t),
        POINTER(ecs_type_t),
    ]
    ecs_commit.restype = c_bool
    break

# vendor/flecs/flecs.h: 9777
for _lib in _libs.values():
    if not _lib.has("ecs_search", "cdecl"):
        continue
    ecs_search = _lib.get("ecs_search", "cdecl")
    ecs_search.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_table_t),
        ecs_id_t,
        POINTER(ecs_id_t),
    ]
    ecs_search.restype = c_int32
    break

# vendor/flecs/flecs.h: 9819
for _lib in _libs.values():
    if not _lib.has("ecs_search_offset", "cdecl"):
        continue
    ecs_search_offset = _lib.get("ecs_search_offset", "cdecl")
    ecs_search_offset.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_table_t),
        c_int32,
        ecs_id_t,
        POINTER(ecs_id_t),
    ]
    ecs_search_offset.restype = c_int32
    break

# vendor/flecs/flecs.h: 9868
for _lib in _libs.values():
    if not _lib.has("ecs_search_relation", "cdecl"):
        continue
    ecs_search_relation = _lib.get("ecs_search_relation", "cdecl")
    ecs_search_relation.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_table_t),
        c_int32,
        ecs_id_t,
        ecs_entity_t,
        ecs_flags64_t,
        POINTER(ecs_entity_t),
        POINTER(ecs_id_t),
        POINTER(POINTER(struct_ecs_table_record_t)),
    ]
    ecs_search_relation.restype = c_int32
    break

# vendor/flecs/flecs.h: 9887
for _lib in _libs.values():
    if not _lib.has("ecs_table_clear_entities", "cdecl"):
        continue
    ecs_table_clear_entities = _lib.get("ecs_table_clear_entities", "cdecl")
    ecs_table_clear_entities.argtypes = [POINTER(ecs_world_t), POINTER(ecs_table_t)]
    ecs_table_clear_entities.restype = None
    break

# vendor/flecs/flecs.h: 9908
for _lib in _libs.values():
    if not _lib.has("ecs_value_init", "cdecl"):
        continue
    ecs_value_init = _lib.get("ecs_value_init", "cdecl")
    ecs_value_init.argtypes = [POINTER(ecs_world_t), ecs_entity_t, POINTER(None)]
    ecs_value_init.restype = c_int
    break

# vendor/flecs/flecs.h: 9921
for _lib in _libs.values():
    if not _lib.has("ecs_value_init_w_type_info", "cdecl"):
        continue
    ecs_value_init_w_type_info = _lib.get("ecs_value_init_w_type_info", "cdecl")
    ecs_value_init_w_type_info.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_type_info_t),
        POINTER(None),
    ]
    ecs_value_init_w_type_info.restype = c_int
    break

# vendor/flecs/flecs.h: 9933
for _lib in _libs.values():
    if not _lib.has("ecs_value_new", "cdecl"):
        continue
    ecs_value_new = _lib.get("ecs_value_new", "cdecl")
    ecs_value_new.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_value_new.restype = POINTER(c_ubyte)
    ecs_value_new.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 9943
for _lib in _libs.values():
    if not _lib.has("ecs_value_new_w_type_info", "cdecl"):
        continue
    ecs_value_new_w_type_info = _lib.get("ecs_value_new_w_type_info", "cdecl")
    ecs_value_new_w_type_info.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_type_info_t),
    ]
    ecs_value_new_w_type_info.restype = POINTER(c_ubyte)
    ecs_value_new_w_type_info.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 9954
for _lib in _libs.values():
    if not _lib.has("ecs_value_fini_w_type_info", "cdecl"):
        continue
    ecs_value_fini_w_type_info = _lib.get("ecs_value_fini_w_type_info", "cdecl")
    ecs_value_fini_w_type_info.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_type_info_t),
        POINTER(None),
    ]
    ecs_value_fini_w_type_info.restype = c_int
    break

# vendor/flecs/flecs.h: 9967
for _lib in _libs.values():
    if not _lib.has("ecs_value_fini", "cdecl"):
        continue
    ecs_value_fini = _lib.get("ecs_value_fini", "cdecl")
    ecs_value_fini.argtypes = [POINTER(ecs_world_t), ecs_entity_t, POINTER(None)]
    ecs_value_fini.restype = c_int
    break

# vendor/flecs/flecs.h: 9980
for _lib in _libs.values():
    if not _lib.has("ecs_value_free", "cdecl"):
        continue
    ecs_value_free = _lib.get("ecs_value_free", "cdecl")
    ecs_value_free.argtypes = [POINTER(ecs_world_t), ecs_entity_t, POINTER(None)]
    ecs_value_free.restype = c_int
    break

# vendor/flecs/flecs.h: 9994
for _lib in _libs.values():
    if not _lib.has("ecs_value_copy_w_type_info", "cdecl"):
        continue
    ecs_value_copy_w_type_info = _lib.get("ecs_value_copy_w_type_info", "cdecl")
    ecs_value_copy_w_type_info.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_type_info_t),
        POINTER(None),
        POINTER(None),
    ]
    ecs_value_copy_w_type_info.restype = c_int
    break

# vendor/flecs/flecs.h: 10009
for _lib in _libs.values():
    if not _lib.has("ecs_value_copy", "cdecl"):
        continue
    ecs_value_copy = _lib.get("ecs_value_copy", "cdecl")
    ecs_value_copy.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        POINTER(None),
        POINTER(None),
    ]
    ecs_value_copy.restype = c_int
    break

# vendor/flecs/flecs.h: 10023
for _lib in _libs.values():
    if not _lib.has("ecs_value_move_w_type_info", "cdecl"):
        continue
    ecs_value_move_w_type_info = _lib.get("ecs_value_move_w_type_info", "cdecl")
    ecs_value_move_w_type_info.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_type_info_t),
        POINTER(None),
        POINTER(None),
    ]
    ecs_value_move_w_type_info.restype = c_int
    break

# vendor/flecs/flecs.h: 10037
for _lib in _libs.values():
    if not _lib.has("ecs_value_move", "cdecl"):
        continue
    ecs_value_move = _lib.get("ecs_value_move", "cdecl")
    ecs_value_move.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        POINTER(None),
        POINTER(None),
    ]
    ecs_value_move.restype = c_int
    break

# vendor/flecs/flecs.h: 10051
for _lib in _libs.values():
    if not _lib.has("ecs_value_move_ctor_w_type_info", "cdecl"):
        continue
    ecs_value_move_ctor_w_type_info = _lib.get(
        "ecs_value_move_ctor_w_type_info", "cdecl"
    )
    ecs_value_move_ctor_w_type_info.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_type_info_t),
        POINTER(None),
        POINTER(None),
    ]
    ecs_value_move_ctor_w_type_info.restype = c_int
    break

# vendor/flecs/flecs.h: 10065
for _lib in _libs.values():
    if not _lib.has("ecs_value_move_ctor", "cdecl"):
        continue
    ecs_value_move_ctor = _lib.get("ecs_value_move_ctor", "cdecl")
    ecs_value_move_ctor.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        POINTER(None),
        POINTER(None),
    ]
    ecs_value_move_ctor.restype = c_int
    break

# vendor/flecs/flecs.h: 11109
for _lib in _libs.values():
    if not _lib.has("ecs_deprecated_", "cdecl"):
        continue
    ecs_deprecated_ = _lib.get("ecs_deprecated_", "cdecl")
    ecs_deprecated_.argtypes = [String, c_int32, String]
    ecs_deprecated_.restype = None
    break

# vendor/flecs/flecs.h: 11121
for _lib in _libs.values():
    if not _lib.has("ecs_log_push_", "cdecl"):
        continue
    ecs_log_push_ = _lib.get("ecs_log_push_", "cdecl")
    ecs_log_push_.argtypes = [c_int32]
    ecs_log_push_.restype = None
    break

# vendor/flecs/flecs.h: 11130
for _lib in _libs.values():
    if not _lib.has("ecs_log_pop_", "cdecl"):
        continue
    ecs_log_pop_ = _lib.get("ecs_log_pop_", "cdecl")
    ecs_log_pop_.argtypes = [c_int32]
    ecs_log_pop_.restype = None
    break

# vendor/flecs/flecs.h: 11140
for _lib in _libs.values():
    if not _lib.has("ecs_should_log", "cdecl"):
        continue
    ecs_should_log = _lib.get("ecs_should_log", "cdecl")
    ecs_should_log.argtypes = [c_int32]
    ecs_should_log.restype = c_bool
    break

# vendor/flecs/flecs.h: 11148
for _lib in _libs.values():
    if not _lib.has("ecs_strerror", "cdecl"):
        continue
    ecs_strerror = _lib.get("ecs_strerror", "cdecl")
    ecs_strerror.argtypes = [c_int32]
    ecs_strerror.restype = c_char_p
    break

# vendor/flecs/flecs.h: 11177
for _lib in _libs.values():
    if _lib.has("ecs_print_", "cdecl"):
        _func = _lib.get("ecs_print_", "cdecl")
        _restype = None
        _errcheck = None
        _argtypes = [c_int32, String, c_int32, String]
        ecs_print_ = _variadic_function(_func, _restype, _argtypes, _errcheck)

# vendor/flecs/flecs.h: 11185
for _lib in _libs.values():
    if not _lib.has("ecs_printv_", "cdecl"):
        continue
    ecs_printv_ = _lib.get("ecs_printv_", "cdecl")
    ecs_printv_.argtypes = [c_int, String, c_int32, String, c_void_p]
    ecs_printv_.restype = None
    break

# vendor/flecs/flecs.h: 11193
for _lib in _libs.values():
    if _lib.has("ecs_log_", "cdecl"):
        _func = _lib.get("ecs_log_", "cdecl")
        _restype = None
        _errcheck = None
        _argtypes = [c_int32, String, c_int32, String]
        ecs_log_ = _variadic_function(_func, _restype, _argtypes, _errcheck)

# vendor/flecs/flecs.h: 11201
for _lib in _libs.values():
    if not _lib.has("ecs_logv_", "cdecl"):
        continue
    ecs_logv_ = _lib.get("ecs_logv_", "cdecl")
    ecs_logv_.argtypes = [c_int, String, c_int32, String, c_void_p]
    ecs_logv_.restype = None
    break

# vendor/flecs/flecs.h: 11209
for _lib in _libs.values():
    if _lib.has("ecs_abort_", "cdecl"):
        _func = _lib.get("ecs_abort_", "cdecl")
        _restype = None
        _errcheck = None
        _argtypes = [c_int32, String, c_int32, String]
        ecs_abort_ = _variadic_function(_func, _restype, _argtypes, _errcheck)

# vendor/flecs/flecs.h: 11217
for _lib in _libs.values():
    if _lib.has("ecs_assert_log_", "cdecl"):
        _func = _lib.get("ecs_assert_log_", "cdecl")
        _restype = None
        _errcheck = None
        _argtypes = [c_int32, String, String, c_int32, String]
        ecs_assert_log_ = _variadic_function(_func, _restype, _argtypes, _errcheck)

# vendor/flecs/flecs.h: 11226
for _lib in _libs.values():
    if _lib.has("ecs_parser_error_", "cdecl"):
        _func = _lib.get("ecs_parser_error_", "cdecl")
        _restype = None
        _errcheck = None
        _argtypes = [String, String, c_int64, String]
        ecs_parser_error_ = _variadic_function(_func, _restype, _argtypes, _errcheck)

# vendor/flecs/flecs.h: 11234
for _lib in _libs.values():
    if not _lib.has("ecs_parser_errorv_", "cdecl"):
        continue
    ecs_parser_errorv_ = _lib.get("ecs_parser_errorv_", "cdecl")
    ecs_parser_errorv_.argtypes = [String, String, c_int64, String, c_void_p]
    ecs_parser_errorv_.restype = None
    break

# vendor/flecs/flecs.h: 11242
for _lib in _libs.values():
    if _lib.has("ecs_parser_warning_", "cdecl"):
        _func = _lib.get("ecs_parser_warning_", "cdecl")
        _restype = None
        _errcheck = None
        _argtypes = [String, String, c_int64, String]
        ecs_parser_warning_ = _variadic_function(_func, _restype, _argtypes, _errcheck)

# vendor/flecs/flecs.h: 11250
for _lib in _libs.values():
    if not _lib.has("ecs_parser_warningv_", "cdecl"):
        continue
    ecs_parser_warningv_ = _lib.get("ecs_parser_warningv_", "cdecl")
    ecs_parser_warningv_.argtypes = [String, String, c_int64, String, c_void_p]
    ecs_parser_warningv_.restype = None
    break

# vendor/flecs/flecs.h: 11534
for _lib in _libs.values():
    if not _lib.has("ecs_log_set_level", "cdecl"):
        continue
    ecs_log_set_level = _lib.get("ecs_log_set_level", "cdecl")
    ecs_log_set_level.argtypes = [c_int]
    ecs_log_set_level.restype = c_int
    break

# vendor/flecs/flecs.h: 11542
for _lib in _libs.values():
    if not _lib.has("ecs_log_get_level", "cdecl"):
        continue
    ecs_log_get_level = _lib.get("ecs_log_get_level", "cdecl")
    ecs_log_get_level.argtypes = []
    ecs_log_get_level.restype = c_int
    break

# vendor/flecs/flecs.h: 11551
for _lib in _libs.values():
    if not _lib.has("ecs_log_enable_colors", "cdecl"):
        continue
    ecs_log_enable_colors = _lib.get("ecs_log_enable_colors", "cdecl")
    ecs_log_enable_colors.argtypes = [c_bool]
    ecs_log_enable_colors.restype = c_bool
    break

# vendor/flecs/flecs.h: 11562
for _lib in _libs.values():
    if not _lib.has("ecs_log_enable_timestamp", "cdecl"):
        continue
    ecs_log_enable_timestamp = _lib.get("ecs_log_enable_timestamp", "cdecl")
    ecs_log_enable_timestamp.argtypes = [c_bool]
    ecs_log_enable_timestamp.restype = c_bool
    break

# vendor/flecs/flecs.h: 11579
for _lib in _libs.values():
    if not _lib.has("ecs_log_enable_timedelta", "cdecl"):
        continue
    ecs_log_enable_timedelta = _lib.get("ecs_log_enable_timedelta", "cdecl")
    ecs_log_enable_timedelta.argtypes = [c_bool]
    ecs_log_enable_timedelta.restype = c_bool
    break

# vendor/flecs/flecs.h: 11588
for _lib in _libs.values():
    if not _lib.has("ecs_log_last_error", "cdecl"):
        continue
    ecs_log_last_error = _lib.get("ecs_log_last_error", "cdecl")
    ecs_log_last_error.argtypes = []
    ecs_log_last_error.restype = c_int
    break

ecs_app_init_action_t = CFUNCTYPE(
    UNCHECKED(c_int), POINTER(ecs_world_t)
)  # vendor/flecs/flecs.h: 11711


# vendor/flecs/flecs.h: 11728
class struct_ecs_app_desc_t(Structure):
    pass


struct_ecs_app_desc_t.__slots__ = [
    "target_fps",
    "delta_time",
    "threads",
    "frames",
    "enable_rest",
    "enable_stats",
    "port",
    "init",
    "ctx",
]
struct_ecs_app_desc_t._fields_ = [
    ("target_fps", c_float),
    ("delta_time", c_float),
    ("threads", c_int32),
    ("frames", c_int32),
    ("enable_rest", c_bool),
    ("enable_stats", c_bool),
    ("port", uint16_t),
    ("init", ecs_app_init_action_t),
    ("ctx", POINTER(None)),
]

ecs_app_desc_t = struct_ecs_app_desc_t  # vendor/flecs/flecs.h: 11728

ecs_app_run_action_t = CFUNCTYPE(
    UNCHECKED(c_int), POINTER(ecs_world_t), POINTER(ecs_app_desc_t)
)  # vendor/flecs/flecs.h: 11731

ecs_app_frame_action_t = CFUNCTYPE(
    UNCHECKED(c_int), POINTER(ecs_world_t), POINTER(ecs_app_desc_t)
)  # vendor/flecs/flecs.h: 11736

# vendor/flecs/flecs.h: 11752
for _lib in _libs.values():
    if not _lib.has("ecs_app_run", "cdecl"):
        continue
    ecs_app_run = _lib.get("ecs_app_run", "cdecl")
    ecs_app_run.argtypes = [POINTER(ecs_world_t), POINTER(ecs_app_desc_t)]
    ecs_app_run.restype = c_int
    break

# vendor/flecs/flecs.h: 11765
for _lib in _libs.values():
    if not _lib.has("ecs_app_run_frame", "cdecl"):
        continue
    ecs_app_run_frame = _lib.get("ecs_app_run_frame", "cdecl")
    ecs_app_run_frame.argtypes = [POINTER(ecs_world_t), POINTER(ecs_app_desc_t)]
    ecs_app_run_frame.restype = c_int
    break

# vendor/flecs/flecs.h: 11775
for _lib in _libs.values():
    if not _lib.has("ecs_app_set_run_action", "cdecl"):
        continue
    ecs_app_set_run_action = _lib.get("ecs_app_set_run_action", "cdecl")
    ecs_app_set_run_action.argtypes = [ecs_app_run_action_t]
    ecs_app_set_run_action.restype = c_int
    break

# vendor/flecs/flecs.h: 11784
for _lib in _libs.values():
    if not _lib.has("ecs_app_set_frame_action", "cdecl"):
        continue
    ecs_app_set_frame_action = _lib.get("ecs_app_set_frame_action", "cdecl")
    ecs_app_set_frame_action.argtypes = [ecs_app_frame_action_t]
    ecs_app_set_frame_action.restype = c_int
    break


# vendor/flecs/flecs.h: 11850
class struct_ecs_http_server_t(Structure):
    pass


ecs_http_server_t = struct_ecs_http_server_t  # vendor/flecs/flecs.h: 11850


# vendor/flecs/flecs.h: 11859
class struct_anon_15(Structure):
    pass


struct_anon_15.__slots__ = [
    "id",
    "server",
    "host",
    "port",
]
struct_anon_15._fields_ = [
    ("id", uint64_t),
    ("server", POINTER(ecs_http_server_t)),
    ("host", c_char * int(128)),
    ("port", c_char * int(16)),
]

ecs_http_connection_t = struct_anon_15  # vendor/flecs/flecs.h: 11859


# vendor/flecs/flecs.h: 11865
class struct_anon_16(Structure):
    pass


struct_anon_16.__slots__ = [
    "key",
    "value",
]
struct_anon_16._fields_ = [
    ("key", String),
    ("value", String),
]

ecs_http_key_value_t = struct_anon_16  # vendor/flecs/flecs.h: 11865

enum_anon_17 = c_int  # vendor/flecs/flecs.h: 11875

EcsHttpGet = 0  # vendor/flecs/flecs.h: 11875

EcsHttpPost = EcsHttpGet + 1  # vendor/flecs/flecs.h: 11875

EcsHttpPut = EcsHttpPost + 1  # vendor/flecs/flecs.h: 11875

EcsHttpDelete = EcsHttpPut + 1  # vendor/flecs/flecs.h: 11875

EcsHttpOptions = EcsHttpDelete + 1  # vendor/flecs/flecs.h: 11875

EcsHttpMethodUnsupported = EcsHttpOptions + 1  # vendor/flecs/flecs.h: 11875

ecs_http_method_t = enum_anon_17  # vendor/flecs/flecs.h: 11875


# vendor/flecs/flecs.h: 11890
class struct_anon_18(Structure):
    pass


struct_anon_18.__slots__ = [
    "id",
    "method",
    "path",
    "body",
    "headers",
    "params",
    "header_count",
    "param_count",
    "conn",
]
struct_anon_18._fields_ = [
    ("id", uint64_t),
    ("method", ecs_http_method_t),
    ("path", String),
    ("body", String),
    ("headers", ecs_http_key_value_t * int(32)),
    ("params", ecs_http_key_value_t * int(32)),
    ("header_count", c_int32),
    ("param_count", c_int32),
    ("conn", POINTER(ecs_http_connection_t)),
]

ecs_http_request_t = struct_anon_18  # vendor/flecs/flecs.h: 11890


# vendor/flecs/flecs.h: 11899
class struct_anon_19(Structure):
    pass


struct_anon_19.__slots__ = [
    "code",
    "body",
    "status",
    "content_type",
    "headers",
]
struct_anon_19._fields_ = [
    ("code", c_int),
    ("body", ecs_strbuf_t),
    ("status", String),
    ("content_type", String),
    ("headers", ecs_strbuf_t),
]

ecs_http_reply_t = struct_anon_19  # vendor/flecs/flecs.h: 11899

# vendor/flecs/flecs.h: 11905
for _lib in _libs.values():
    try:
        ecs_http_request_received_count = (c_int64).in_dll(
            _lib, "ecs_http_request_received_count"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 11906
for _lib in _libs.values():
    try:
        ecs_http_request_invalid_count = (c_int64).in_dll(
            _lib, "ecs_http_request_invalid_count"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 11907
for _lib in _libs.values():
    try:
        ecs_http_request_handled_ok_count = (c_int64).in_dll(
            _lib, "ecs_http_request_handled_ok_count"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 11908
for _lib in _libs.values():
    try:
        ecs_http_request_handled_error_count = (c_int64).in_dll(
            _lib, "ecs_http_request_handled_error_count"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 11909
for _lib in _libs.values():
    try:
        ecs_http_request_not_handled_count = (c_int64).in_dll(
            _lib, "ecs_http_request_not_handled_count"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 11910
for _lib in _libs.values():
    try:
        ecs_http_request_preflight_count = (c_int64).in_dll(
            _lib, "ecs_http_request_preflight_count"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 11911
for _lib in _libs.values():
    try:
        ecs_http_send_ok_count = (c_int64).in_dll(_lib, "ecs_http_send_ok_count")
        break
    except:
        pass

# vendor/flecs/flecs.h: 11912
for _lib in _libs.values():
    try:
        ecs_http_send_error_count = (c_int64).in_dll(_lib, "ecs_http_send_error_count")
        break
    except:
        pass

# vendor/flecs/flecs.h: 11913
for _lib in _libs.values():
    try:
        ecs_http_busy_count = (c_int64).in_dll(_lib, "ecs_http_busy_count")
        break
    except:
        pass

ecs_http_reply_action_t = CFUNCTYPE(
    UNCHECKED(c_bool),
    POINTER(ecs_http_request_t),
    POINTER(ecs_http_reply_t),
    POINTER(None),
)  # vendor/flecs/flecs.h: 11919


# vendor/flecs/flecs.h: 11933
class struct_anon_20(Structure):
    pass


struct_anon_20.__slots__ = [
    "callback",
    "ctx",
    "port",
    "ipaddr",
    "send_queue_wait_ms",
    "cache_timeout",
    "cache_purge_timeout",
]
struct_anon_20._fields_ = [
    ("callback", ecs_http_reply_action_t),
    ("ctx", POINTER(None)),
    ("port", uint16_t),
    ("ipaddr", String),
    ("send_queue_wait_ms", c_int32),
    ("cache_timeout", c_double),
    ("cache_purge_timeout", c_double),
]

ecs_http_server_desc_t = struct_anon_20  # vendor/flecs/flecs.h: 11933

# vendor/flecs/flecs.h: 11942
for _lib in _libs.values():
    if not _lib.has("ecs_http_server_init", "cdecl"):
        continue
    ecs_http_server_init = _lib.get("ecs_http_server_init", "cdecl")
    ecs_http_server_init.argtypes = [POINTER(ecs_http_server_desc_t)]
    ecs_http_server_init.restype = POINTER(ecs_http_server_t)
    break

# vendor/flecs/flecs.h: 11951
for _lib in _libs.values():
    if not _lib.has("ecs_http_server_fini", "cdecl"):
        continue
    ecs_http_server_fini = _lib.get("ecs_http_server_fini", "cdecl")
    ecs_http_server_fini.argtypes = [POINTER(ecs_http_server_t)]
    ecs_http_server_fini.restype = None
    break

# vendor/flecs/flecs.h: 11961
for _lib in _libs.values():
    if not _lib.has("ecs_http_server_start", "cdecl"):
        continue
    ecs_http_server_start = _lib.get("ecs_http_server_start", "cdecl")
    ecs_http_server_start.argtypes = [POINTER(ecs_http_server_t)]
    ecs_http_server_start.restype = c_int
    break

# vendor/flecs/flecs.h: 11971
for _lib in _libs.values():
    if not _lib.has("ecs_http_server_dequeue", "cdecl"):
        continue
    ecs_http_server_dequeue = _lib.get("ecs_http_server_dequeue", "cdecl")
    ecs_http_server_dequeue.argtypes = [POINTER(ecs_http_server_t), c_float]
    ecs_http_server_dequeue.restype = None
    break

# vendor/flecs/flecs.h: 11981
for _lib in _libs.values():
    if not _lib.has("ecs_http_server_stop", "cdecl"):
        continue
    ecs_http_server_stop = _lib.get("ecs_http_server_stop", "cdecl")
    ecs_http_server_stop.argtypes = [POINTER(ecs_http_server_t)]
    ecs_http_server_stop.restype = None
    break

# vendor/flecs/flecs.h: 11995
for _lib in _libs.values():
    if not _lib.has("ecs_http_server_http_request", "cdecl"):
        continue
    ecs_http_server_http_request = _lib.get("ecs_http_server_http_request", "cdecl")
    ecs_http_server_http_request.argtypes = [
        POINTER(ecs_http_server_t),
        String,
        ecs_size_t,
        POINTER(ecs_http_reply_t),
    ]
    ecs_http_server_http_request.restype = c_int
    break

# vendor/flecs/flecs.h: 12003
for _lib in _libs.values():
    if not _lib.has("ecs_http_server_request", "cdecl"):
        continue
    ecs_http_server_request = _lib.get("ecs_http_server_request", "cdecl")
    ecs_http_server_request.argtypes = [
        POINTER(ecs_http_server_t),
        String,
        String,
        String,
        POINTER(ecs_http_reply_t),
    ]
    ecs_http_server_request.restype = c_int
    break

# vendor/flecs/flecs.h: 12012
for _lib in _libs.values():
    if not _lib.has("ecs_http_server_ctx", "cdecl"):
        continue
    ecs_http_server_ctx = _lib.get("ecs_http_server_ctx", "cdecl")
    ecs_http_server_ctx.argtypes = [POINTER(ecs_http_server_t)]
    ecs_http_server_ctx.restype = POINTER(c_ubyte)
    ecs_http_server_ctx.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 12022
for _lib in _libs.values():
    if not _lib.has("ecs_http_get_header", "cdecl"):
        continue
    ecs_http_get_header = _lib.get("ecs_http_get_header", "cdecl")
    ecs_http_get_header.argtypes = [POINTER(ecs_http_request_t), String]
    ecs_http_get_header.restype = c_char_p
    break

# vendor/flecs/flecs.h: 12033
for _lib in _libs.values():
    if not _lib.has("ecs_http_get_param", "cdecl"):
        continue
    ecs_http_get_param = _lib.get("ecs_http_get_param", "cdecl")
    ecs_http_get_param.argtypes = [POINTER(ecs_http_request_t), String]
    ecs_http_get_param.restype = c_char_p
    break

# vendor/flecs/flecs.h: 12098
for _lib in _libs.values():
    try:
        FLECS_IDEcsRestID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsRestID_")
        break
    except:
        pass


# vendor/flecs/flecs.h: 12105
class struct_anon_21(Structure):
    pass


struct_anon_21.__slots__ = [
    "port",
    "ipaddr",
    "impl",
]
struct_anon_21._fields_ = [
    ("port", uint16_t),
    ("ipaddr", String),
    ("impl", POINTER(None)),
]

EcsRest = struct_anon_21  # vendor/flecs/flecs.h: 12105

# vendor/flecs/flecs.h: 12116
for _lib in _libs.values():
    if not _lib.has("ecs_rest_server_init", "cdecl"):
        continue
    ecs_rest_server_init = _lib.get("ecs_rest_server_init", "cdecl")
    ecs_rest_server_init.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_http_server_desc_t),
    ]
    ecs_rest_server_init.restype = POINTER(ecs_http_server_t)
    break

# vendor/flecs/flecs.h: 12124
for _lib in _libs.values():
    if not _lib.has("ecs_rest_server_fini", "cdecl"):
        continue
    ecs_rest_server_fini = _lib.get("ecs_rest_server_fini", "cdecl")
    ecs_rest_server_fini.argtypes = [POINTER(ecs_http_server_t)]
    ecs_rest_server_fini.restype = None
    break

# vendor/flecs/flecs.h: 12136
for _lib in _libs.values():
    if not _lib.has("FlecsRestImport", "cdecl"):
        continue
    FlecsRestImport = _lib.get("FlecsRestImport", "cdecl")
    FlecsRestImport.argtypes = [POINTER(ecs_world_t)]
    FlecsRestImport.restype = None
    break


# vendor/flecs/flecs.h: 12196
class struct_EcsTimer(Structure):
    pass


struct_EcsTimer.__slots__ = [
    "timeout",
    "time",
    "overshoot",
    "fired_count",
    "active",
    "single_shot",
]
struct_EcsTimer._fields_ = [
    ("timeout", c_float),
    ("time", c_float),
    ("overshoot", c_float),
    ("fired_count", c_int32),
    ("active", c_bool),
    ("single_shot", c_bool),
]

EcsTimer = struct_EcsTimer  # vendor/flecs/flecs.h: 12196


# vendor/flecs/flecs.h: 12204
class struct_EcsRateFilter(Structure):
    pass


struct_EcsRateFilter.__slots__ = [
    "src",
    "rate",
    "tick_count",
    "time_elapsed",
]
struct_EcsRateFilter._fields_ = [
    ("src", ecs_entity_t),
    ("rate", c_int32),
    ("tick_count", c_int32),
    ("time_elapsed", c_float),
]

EcsRateFilter = struct_EcsRateFilter  # vendor/flecs/flecs.h: 12204

# vendor/flecs/flecs.h: 12226
for _lib in _libs.values():
    if not _lib.has("ecs_set_timeout", "cdecl"):
        continue
    ecs_set_timeout = _lib.get("ecs_set_timeout", "cdecl")
    ecs_set_timeout.argtypes = [POINTER(ecs_world_t), ecs_entity_t, c_float]
    ecs_set_timeout.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 12251
for _lib in _libs.values():
    if not _lib.has("ecs_get_timeout", "cdecl"):
        continue
    ecs_get_timeout = _lib.get("ecs_get_timeout", "cdecl")
    ecs_get_timeout.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_get_timeout.restype = c_float
    break

# vendor/flecs/flecs.h: 12273
for _lib in _libs.values():
    if not _lib.has("ecs_set_interval", "cdecl"):
        continue
    ecs_set_interval = _lib.get("ecs_set_interval", "cdecl")
    ecs_set_interval.argtypes = [POINTER(ecs_world_t), ecs_entity_t, c_float]
    ecs_set_interval.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 12287
for _lib in _libs.values():
    if not _lib.has("ecs_get_interval", "cdecl"):
        continue
    ecs_get_interval = _lib.get("ecs_get_interval", "cdecl")
    ecs_get_interval.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_get_interval.restype = c_float
    break

# vendor/flecs/flecs.h: 12298
for _lib in _libs.values():
    if not _lib.has("ecs_start_timer", "cdecl"):
        continue
    ecs_start_timer = _lib.get("ecs_start_timer", "cdecl")
    ecs_start_timer.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_start_timer.restype = None
    break

# vendor/flecs/flecs.h: 12309
for _lib in _libs.values():
    if not _lib.has("ecs_stop_timer", "cdecl"):
        continue
    ecs_stop_timer = _lib.get("ecs_stop_timer", "cdecl")
    ecs_stop_timer.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_stop_timer.restype = None
    break

# vendor/flecs/flecs.h: 12320
for _lib in _libs.values():
    if not _lib.has("ecs_reset_timer", "cdecl"):
        continue
    ecs_reset_timer = _lib.get("ecs_reset_timer", "cdecl")
    ecs_reset_timer.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_reset_timer.restype = None
    break

# vendor/flecs/flecs.h: 12331
for _lib in _libs.values():
    if not _lib.has("ecs_randomize_timers", "cdecl"):
        continue
    ecs_randomize_timers = _lib.get("ecs_randomize_timers", "cdecl")
    ecs_randomize_timers.argtypes = [POINTER(ecs_world_t)]
    ecs_randomize_timers.restype = None
    break

# vendor/flecs/flecs.h: 12365
for _lib in _libs.values():
    if not _lib.has("ecs_set_rate", "cdecl"):
        continue
    ecs_set_rate = _lib.get("ecs_set_rate", "cdecl")
    ecs_set_rate.argtypes = [POINTER(ecs_world_t), ecs_entity_t, c_int32, ecs_entity_t]
    ecs_set_rate.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 12394
for _lib in _libs.values():
    if not _lib.has("ecs_set_tick_source", "cdecl"):
        continue
    ecs_set_tick_source = _lib.get("ecs_set_tick_source", "cdecl")
    ecs_set_tick_source.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_entity_t]
    ecs_set_tick_source.restype = None
    break

# vendor/flecs/flecs.h: 12413
for _lib in _libs.values():
    if not _lib.has("FlecsTimerImport", "cdecl"):
        continue
    FlecsTimerImport = _lib.get("FlecsTimerImport", "cdecl")
    FlecsTimerImport.argtypes = [POINTER(ecs_world_t)]
    FlecsTimerImport.restype = None
    break


# vendor/flecs/flecs.h: 12547
class struct_ecs_pipeline_desc_t(Structure):
    pass


struct_ecs_pipeline_desc_t.__slots__ = [
    "entity",
    "query",
]
struct_ecs_pipeline_desc_t._fields_ = [
    ("entity", ecs_entity_t),
    ("query", ecs_query_desc_t),
]

ecs_pipeline_desc_t = struct_ecs_pipeline_desc_t  # vendor/flecs/flecs.h: 12547

# vendor/flecs/flecs.h: 12556
for _lib in _libs.values():
    if not _lib.has("ecs_pipeline_init", "cdecl"):
        continue
    ecs_pipeline_init = _lib.get("ecs_pipeline_init", "cdecl")
    ecs_pipeline_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_pipeline_desc_t)]
    ecs_pipeline_init.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 12567
for _lib in _libs.values():
    if not _lib.has("ecs_set_pipeline", "cdecl"):
        continue
    ecs_set_pipeline = _lib.get("ecs_set_pipeline", "cdecl")
    ecs_set_pipeline.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_set_pipeline.restype = None
    break

# vendor/flecs/flecs.h: 12578
for _lib in _libs.values():
    if not _lib.has("ecs_get_pipeline", "cdecl"):
        continue
    ecs_get_pipeline = _lib.get("ecs_get_pipeline", "cdecl")
    ecs_get_pipeline.argtypes = [POINTER(ecs_world_t)]
    ecs_get_pipeline.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 12600
for _lib in _libs.values():
    if not _lib.has("ecs_progress", "cdecl"):
        continue
    ecs_progress = _lib.get("ecs_progress", "cdecl")
    ecs_progress.argtypes = [POINTER(ecs_world_t), c_float]
    ecs_progress.restype = c_bool
    break

# vendor/flecs/flecs.h: 12611
for _lib in _libs.values():
    if not _lib.has("ecs_set_time_scale", "cdecl"):
        continue
    ecs_set_time_scale = _lib.get("ecs_set_time_scale", "cdecl")
    ecs_set_time_scale.argtypes = [POINTER(ecs_world_t), c_float]
    ecs_set_time_scale.restype = None
    break

# vendor/flecs/flecs.h: 12621
for _lib in _libs.values():
    if not _lib.has("ecs_reset_clock", "cdecl"):
        continue
    ecs_reset_clock = _lib.get("ecs_reset_clock", "cdecl")
    ecs_reset_clock.argtypes = [POINTER(ecs_world_t)]
    ecs_reset_clock.restype = None
    break

# vendor/flecs/flecs.h: 12641
for _lib in _libs.values():
    if not _lib.has("ecs_run_pipeline", "cdecl"):
        continue
    ecs_run_pipeline = _lib.get("ecs_run_pipeline", "cdecl")
    ecs_run_pipeline.argtypes = [POINTER(ecs_world_t), ecs_entity_t, c_float]
    ecs_run_pipeline.restype = None
    break

# vendor/flecs/flecs.h: 12663
for _lib in _libs.values():
    if not _lib.has("ecs_set_threads", "cdecl"):
        continue
    ecs_set_threads = _lib.get("ecs_set_threads", "cdecl")
    ecs_set_threads.argtypes = [POINTER(ecs_world_t), c_int32]
    ecs_set_threads.restype = None
    break

# vendor/flecs/flecs.h: 12684
for _lib in _libs.values():
    if not _lib.has("ecs_set_task_threads", "cdecl"):
        continue
    ecs_set_task_threads = _lib.get("ecs_set_task_threads", "cdecl")
    ecs_set_task_threads.argtypes = [POINTER(ecs_world_t), c_int32]
    ecs_set_task_threads.restype = None
    break

# vendor/flecs/flecs.h: 12694
for _lib in _libs.values():
    if not _lib.has("ecs_using_task_threads", "cdecl"):
        continue
    ecs_using_task_threads = _lib.get("ecs_using_task_threads", "cdecl")
    ecs_using_task_threads.argtypes = [POINTER(ecs_world_t)]
    ecs_using_task_threads.restype = c_bool
    break

# vendor/flecs/flecs.h: 12710
for _lib in _libs.values():
    if not _lib.has("FlecsPipelineImport", "cdecl"):
        continue
    FlecsPipelineImport = _lib.get("FlecsPipelineImport", "cdecl")
    FlecsPipelineImport.argtypes = [POINTER(ecs_world_t)]
    FlecsPipelineImport.restype = None
    break


# vendor/flecs/flecs.h: 12763
class struct_EcsTickSource(Structure):
    pass


struct_EcsTickSource.__slots__ = [
    "tick",
    "time_elapsed",
]
struct_EcsTickSource._fields_ = [
    ("tick", c_bool),
    ("time_elapsed", c_float),
]

EcsTickSource = struct_EcsTickSource  # vendor/flecs/flecs.h: 12763


# vendor/flecs/flecs.h: 12826
class struct_ecs_system_desc_t(Structure):
    pass


struct_ecs_system_desc_t.__slots__ = [
    "_canary",
    "entity",
    "query",
    "callback",
    "run",
    "ctx",
    "ctx_free",
    "callback_ctx",
    "callback_ctx_free",
    "run_ctx",
    "run_ctx_free",
    "interval",
    "rate",
    "tick_source",
    "multi_threaded",
    "immediate",
]
struct_ecs_system_desc_t._fields_ = [
    ("_canary", c_int32),
    ("entity", ecs_entity_t),
    ("query", ecs_query_desc_t),
    ("callback", ecs_iter_action_t),
    ("run", ecs_run_action_t),
    ("ctx", POINTER(None)),
    ("ctx_free", ecs_ctx_free_t),
    ("callback_ctx", POINTER(None)),
    ("callback_ctx_free", ecs_ctx_free_t),
    ("run_ctx", POINTER(None)),
    ("run_ctx_free", ecs_ctx_free_t),
    ("interval", c_float),
    ("rate", c_int32),
    ("tick_source", ecs_entity_t),
    ("multi_threaded", c_bool),
    ("immediate", c_bool),
]

ecs_system_desc_t = struct_ecs_system_desc_t  # vendor/flecs/flecs.h: 12826

# vendor/flecs/flecs.h: 12830
for _lib in _libs.values():
    if not _lib.has("ecs_system_init", "cdecl"):
        continue
    ecs_system_init = _lib.get("ecs_system_init", "cdecl")
    ecs_system_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_system_desc_t)]
    ecs_system_init.restype = ecs_entity_t
    break


# vendor/flecs/flecs.h: 12888
class struct_ecs_system_t(Structure):
    pass


struct_ecs_system_t.__slots__ = [
    "hdr",
    "run",
    "action",
    "query",
    "tick_source",
    "multi_threaded",
    "immediate",
    "name",
    "ctx",
    "callback_ctx",
    "run_ctx",
    "ctx_free",
    "callback_ctx_free",
    "run_ctx_free",
    "time_spent",
    "time_passed",
    "last_frame",
    "dtor",
]
struct_ecs_system_t._fields_ = [
    ("hdr", ecs_header_t),
    ("run", ecs_run_action_t),
    ("action", ecs_iter_action_t),
    ("query", POINTER(ecs_query_t)),
    ("tick_source", ecs_entity_t),
    ("multi_threaded", c_bool),
    ("immediate", c_bool),
    ("name", String),
    ("ctx", POINTER(None)),
    ("callback_ctx", POINTER(None)),
    ("run_ctx", POINTER(None)),
    ("ctx_free", ecs_ctx_free_t),
    ("callback_ctx_free", ecs_ctx_free_t),
    ("run_ctx_free", ecs_ctx_free_t),
    ("time_spent", c_float),
    ("time_passed", c_float),
    ("last_frame", c_int64),
    ("dtor", flecs_poly_dtor_t),
]

ecs_system_t = struct_ecs_system_t  # vendor/flecs/flecs.h: 12888

# vendor/flecs/flecs.h: 12899
for _lib in _libs.values():
    if not _lib.has("ecs_system_get", "cdecl"):
        continue
    ecs_system_get = _lib.get("ecs_system_get", "cdecl")
    ecs_system_get.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_system_get.restype = POINTER(ecs_system_t)
    break

# vendor/flecs/flecs.h: 13000
for _lib in _libs.values():
    if not _lib.has("ecs_run", "cdecl"):
        continue
    ecs_run = _lib.get("ecs_run", "cdecl")
    ecs_run.argtypes = [POINTER(ecs_world_t), ecs_entity_t, c_float, POINTER(None)]
    ecs_run.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 13017
for _lib in _libs.values():
    if not _lib.has("ecs_run_worker", "cdecl"):
        continue
    ecs_run_worker = _lib.get("ecs_run_worker", "cdecl")
    ecs_run_worker.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        c_int32,
        c_int32,
        c_float,
        POINTER(None),
    ]
    ecs_run_worker.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 13034
for _lib in _libs.values():
    if not _lib.has("FlecsSystemImport", "cdecl"):
        continue
    FlecsSystemImport = _lib.get("FlecsSystemImport", "cdecl")
    FlecsSystemImport.argtypes = [POINTER(ecs_world_t)]
    FlecsSystemImport.restype = None
    break


# vendor/flecs/flecs.h: 13099
class struct_ecs_gauge_t(Structure):
    pass


struct_ecs_gauge_t.__slots__ = [
    "avg",
    "min",
    "max",
]
struct_ecs_gauge_t._fields_ = [
    ("avg", c_float * int(60)),
    ("min", c_float * int(60)),
    ("max", c_float * int(60)),
]

ecs_gauge_t = struct_ecs_gauge_t  # vendor/flecs/flecs.h: 13099


# vendor/flecs/flecs.h: 13105
class struct_ecs_counter_t(Structure):
    pass


struct_ecs_counter_t.__slots__ = [
    "rate",
    "value",
]
struct_ecs_counter_t._fields_ = [
    ("rate", ecs_gauge_t),
    ("value", c_double * int(60)),
]

ecs_counter_t = struct_ecs_counter_t  # vendor/flecs/flecs.h: 13105


# vendor/flecs/flecs.h: 13111
class union_ecs_metric_t(Union):
    pass


union_ecs_metric_t.__slots__ = [
    "gauge",
    "counter",
]
union_ecs_metric_t._fields_ = [
    ("gauge", ecs_gauge_t),
    ("counter", ecs_counter_t),
]

ecs_metric_t = union_ecs_metric_t  # vendor/flecs/flecs.h: 13111


# vendor/flecs/flecs.h: 13117
class struct_anon_22(Structure):
    pass


struct_anon_22.__slots__ = [
    "count",
    "not_alive_count",
]
struct_anon_22._fields_ = [
    ("count", ecs_metric_t),
    ("not_alive_count", ecs_metric_t),
]


# vendor/flecs/flecs.h: 13123
class struct_anon_23(Structure):
    pass


struct_anon_23.__slots__ = [
    "tag_count",
    "component_count",
    "pair_count",
    "type_count",
    "create_count",
    "delete_count",
]
struct_anon_23._fields_ = [
    ("tag_count", ecs_metric_t),
    ("component_count", ecs_metric_t),
    ("pair_count", ecs_metric_t),
    ("type_count", ecs_metric_t),
    ("create_count", ecs_metric_t),
    ("delete_count", ecs_metric_t),
]


# vendor/flecs/flecs.h: 13133
class struct_anon_24(Structure):
    pass


struct_anon_24.__slots__ = [
    "count",
    "empty_count",
    "create_count",
    "delete_count",
]
struct_anon_24._fields_ = [
    ("count", ecs_metric_t),
    ("empty_count", ecs_metric_t),
    ("create_count", ecs_metric_t),
    ("delete_count", ecs_metric_t),
]


# vendor/flecs/flecs.h: 13141
class struct_anon_25(Structure):
    pass


struct_anon_25.__slots__ = [
    "query_count",
    "observer_count",
    "system_count",
]
struct_anon_25._fields_ = [
    ("query_count", ecs_metric_t),
    ("observer_count", ecs_metric_t),
    ("system_count", ecs_metric_t),
]


# vendor/flecs/flecs.h: 13148
class struct_anon_26(Structure):
    pass


struct_anon_26.__slots__ = [
    "add_count",
    "remove_count",
    "delete_count",
    "clear_count",
    "set_count",
    "ensure_count",
    "modified_count",
    "other_count",
    "discard_count",
    "batched_entity_count",
    "batched_count",
]
struct_anon_26._fields_ = [
    ("add_count", ecs_metric_t),
    ("remove_count", ecs_metric_t),
    ("delete_count", ecs_metric_t),
    ("clear_count", ecs_metric_t),
    ("set_count", ecs_metric_t),
    ("ensure_count", ecs_metric_t),
    ("modified_count", ecs_metric_t),
    ("other_count", ecs_metric_t),
    ("discard_count", ecs_metric_t),
    ("batched_entity_count", ecs_metric_t),
    ("batched_count", ecs_metric_t),
]


# vendor/flecs/flecs.h: 13163
class struct_anon_27(Structure):
    pass


struct_anon_27.__slots__ = [
    "frame_count",
    "merge_count",
    "rematch_count",
    "pipeline_build_count",
    "systems_ran",
    "observers_ran",
    "event_emit_count",
]
struct_anon_27._fields_ = [
    ("frame_count", ecs_metric_t),
    ("merge_count", ecs_metric_t),
    ("rematch_count", ecs_metric_t),
    ("pipeline_build_count", ecs_metric_t),
    ("systems_ran", ecs_metric_t),
    ("observers_ran", ecs_metric_t),
    ("event_emit_count", ecs_metric_t),
]


# vendor/flecs/flecs.h: 13174
class struct_anon_28(Structure):
    pass


struct_anon_28.__slots__ = [
    "world_time_raw",
    "world_time",
    "frame_time",
    "system_time",
    "emit_time",
    "merge_time",
    "rematch_time",
    "fps",
    "delta_time",
]
struct_anon_28._fields_ = [
    ("world_time_raw", ecs_metric_t),
    ("world_time", ecs_metric_t),
    ("frame_time", ecs_metric_t),
    ("system_time", ecs_metric_t),
    ("emit_time", ecs_metric_t),
    ("merge_time", ecs_metric_t),
    ("rematch_time", ecs_metric_t),
    ("fps", ecs_metric_t),
    ("delta_time", ecs_metric_t),
]


# vendor/flecs/flecs.h: 13186
class struct_anon_29(Structure):
    pass


struct_anon_29.__slots__ = [
    "alloc_count",
    "realloc_count",
    "free_count",
    "outstanding_alloc_count",
    "block_alloc_count",
    "block_free_count",
    "block_outstanding_alloc_count",
    "stack_alloc_count",
    "stack_free_count",
    "stack_outstanding_alloc_count",
]
struct_anon_29._fields_ = [
    ("alloc_count", ecs_metric_t),
    ("realloc_count", ecs_metric_t),
    ("free_count", ecs_metric_t),
    ("outstanding_alloc_count", ecs_metric_t),
    ("block_alloc_count", ecs_metric_t),
    ("block_free_count", ecs_metric_t),
    ("block_outstanding_alloc_count", ecs_metric_t),
    ("stack_alloc_count", ecs_metric_t),
    ("stack_free_count", ecs_metric_t),
    ("stack_outstanding_alloc_count", ecs_metric_t),
]


# vendor/flecs/flecs.h: 13203
class struct_anon_30(Structure):
    pass


struct_anon_30.__slots__ = [
    "request_received_count",
    "request_invalid_count",
    "request_handled_ok_count",
    "request_handled_error_count",
    "request_not_handled_count",
    "request_preflight_count",
    "send_ok_count",
    "send_error_count",
    "busy_count",
]
struct_anon_30._fields_ = [
    ("request_received_count", ecs_metric_t),
    ("request_invalid_count", ecs_metric_t),
    ("request_handled_ok_count", ecs_metric_t),
    ("request_handled_error_count", ecs_metric_t),
    ("request_not_handled_count", ecs_metric_t),
    ("request_preflight_count", ecs_metric_t),
    ("send_ok_count", ecs_metric_t),
    ("send_error_count", ecs_metric_t),
    ("busy_count", ecs_metric_t),
]


# vendor/flecs/flecs.h: 13219
class struct_ecs_world_stats_t(Structure):
    pass


struct_ecs_world_stats_t.__slots__ = [
    "first_",
    "entities",
    "components",
    "tables",
    "queries",
    "commands",
    "frame",
    "performance",
    "memory",
    "http",
    "last_",
    "t",
]
struct_ecs_world_stats_t._fields_ = [
    ("first_", c_int64),
    ("entities", struct_anon_22),
    ("components", struct_anon_23),
    ("tables", struct_anon_24),
    ("queries", struct_anon_25),
    ("commands", struct_anon_26),
    ("frame", struct_anon_27),
    ("performance", struct_anon_28),
    ("memory", struct_anon_29),
    ("http", struct_anon_30),
    ("last_", c_int64),
    ("t", c_int32),
]

ecs_world_stats_t = struct_ecs_world_stats_t  # vendor/flecs/flecs.h: 13219


# vendor/flecs/flecs.h: 13231
class struct_ecs_query_stats_t(Structure):
    pass


struct_ecs_query_stats_t.__slots__ = [
    "first_",
    "result_count",
    "matched_table_count",
    "matched_entity_count",
    "last_",
    "t",
]
struct_ecs_query_stats_t._fields_ = [
    ("first_", c_int64),
    ("result_count", ecs_metric_t),
    ("matched_table_count", ecs_metric_t),
    ("matched_entity_count", ecs_metric_t),
    ("last_", c_int64),
    ("t", c_int32),
]

ecs_query_stats_t = struct_ecs_query_stats_t  # vendor/flecs/flecs.h: 13231


# vendor/flecs/flecs.h: 13242
class struct_ecs_system_stats_t(Structure):
    pass


struct_ecs_system_stats_t.__slots__ = [
    "first_",
    "time_spent",
    "last_",
    "task",
    "query",
]
struct_ecs_system_stats_t._fields_ = [
    ("first_", c_int64),
    ("time_spent", ecs_metric_t),
    ("last_", c_int64),
    ("task", c_bool),
    ("query", ecs_query_stats_t),
]

ecs_system_stats_t = struct_ecs_system_stats_t  # vendor/flecs/flecs.h: 13242


# vendor/flecs/flecs.h: 13254
class struct_ecs_sync_stats_t(Structure):
    pass


struct_ecs_sync_stats_t.__slots__ = [
    "first_",
    "time_spent",
    "commands_enqueued",
    "last_",
    "system_count",
    "multi_threaded",
    "immediate",
]
struct_ecs_sync_stats_t._fields_ = [
    ("first_", c_int64),
    ("time_spent", ecs_metric_t),
    ("commands_enqueued", ecs_metric_t),
    ("last_", c_int64),
    ("system_count", c_int32),
    ("multi_threaded", c_bool),
    ("immediate", c_bool),
]

ecs_sync_stats_t = struct_ecs_sync_stats_t  # vendor/flecs/flecs.h: 13254


# vendor/flecs/flecs.h: 13274
class struct_ecs_pipeline_stats_t(Structure):
    pass


struct_ecs_pipeline_stats_t.__slots__ = [
    "canary_",
    "systems",
    "sync_points",
    "t",
    "system_count",
    "active_system_count",
    "rebuild_count",
]
struct_ecs_pipeline_stats_t._fields_ = [
    ("canary_", c_int8),
    ("systems", ecs_vec_t),
    ("sync_points", ecs_vec_t),
    ("t", c_int32),
    ("system_count", c_int32),
    ("active_system_count", c_int32),
    ("rebuild_count", c_int32),
]

ecs_pipeline_stats_t = struct_ecs_pipeline_stats_t  # vendor/flecs/flecs.h: 13274

# vendor/flecs/flecs.h: 13282
for _lib in _libs.values():
    if not _lib.has("ecs_world_stats_get", "cdecl"):
        continue
    ecs_world_stats_get = _lib.get("ecs_world_stats_get", "cdecl")
    ecs_world_stats_get.argtypes = [POINTER(ecs_world_t), POINTER(ecs_world_stats_t)]
    ecs_world_stats_get.restype = None
    break

# vendor/flecs/flecs.h: 13288
for _lib in _libs.values():
    if not _lib.has("ecs_world_stats_reduce", "cdecl"):
        continue
    ecs_world_stats_reduce = _lib.get("ecs_world_stats_reduce", "cdecl")
    ecs_world_stats_reduce.argtypes = [
        POINTER(ecs_world_stats_t),
        POINTER(ecs_world_stats_t),
    ]
    ecs_world_stats_reduce.restype = None
    break

# vendor/flecs/flecs.h: 13294
for _lib in _libs.values():
    if not _lib.has("ecs_world_stats_reduce_last", "cdecl"):
        continue
    ecs_world_stats_reduce_last = _lib.get("ecs_world_stats_reduce_last", "cdecl")
    ecs_world_stats_reduce_last.argtypes = [
        POINTER(ecs_world_stats_t),
        POINTER(ecs_world_stats_t),
        c_int32,
    ]
    ecs_world_stats_reduce_last.restype = None
    break

# vendor/flecs/flecs.h: 13301
for _lib in _libs.values():
    if not _lib.has("ecs_world_stats_repeat_last", "cdecl"):
        continue
    ecs_world_stats_repeat_last = _lib.get("ecs_world_stats_repeat_last", "cdecl")
    ecs_world_stats_repeat_last.argtypes = [POINTER(ecs_world_stats_t)]
    ecs_world_stats_repeat_last.restype = None
    break

# vendor/flecs/flecs.h: 13306
for _lib in _libs.values():
    if not _lib.has("ecs_world_stats_copy_last", "cdecl"):
        continue
    ecs_world_stats_copy_last = _lib.get("ecs_world_stats_copy_last", "cdecl")
    ecs_world_stats_copy_last.argtypes = [
        POINTER(ecs_world_stats_t),
        POINTER(ecs_world_stats_t),
    ]
    ecs_world_stats_copy_last.restype = None
    break

# vendor/flecs/flecs.h: 13311
for _lib in _libs.values():
    if not _lib.has("ecs_world_stats_log", "cdecl"):
        continue
    ecs_world_stats_log = _lib.get("ecs_world_stats_log", "cdecl")
    ecs_world_stats_log.argtypes = [POINTER(ecs_world_t), POINTER(ecs_world_stats_t)]
    ecs_world_stats_log.restype = None
    break

# vendor/flecs/flecs.h: 13323
for _lib in _libs.values():
    if not _lib.has("ecs_query_stats_get", "cdecl"):
        continue
    ecs_query_stats_get = _lib.get("ecs_query_stats_get", "cdecl")
    ecs_query_stats_get.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_query_t),
        POINTER(ecs_query_stats_t),
    ]
    ecs_query_stats_get.restype = None
    break

# vendor/flecs/flecs.h: 13330
for _lib in _libs.values():
    if not _lib.has("ecs_query_cache_stats_reduce", "cdecl"):
        continue
    ecs_query_cache_stats_reduce = _lib.get("ecs_query_cache_stats_reduce", "cdecl")
    ecs_query_cache_stats_reduce.argtypes = [
        POINTER(ecs_query_stats_t),
        POINTER(ecs_query_stats_t),
    ]
    ecs_query_cache_stats_reduce.restype = None
    break

# vendor/flecs/flecs.h: 13336
for _lib in _libs.values():
    if not _lib.has("ecs_query_cache_stats_reduce_last", "cdecl"):
        continue
    ecs_query_cache_stats_reduce_last = _lib.get(
        "ecs_query_cache_stats_reduce_last", "cdecl"
    )
    ecs_query_cache_stats_reduce_last.argtypes = [
        POINTER(ecs_query_stats_t),
        POINTER(ecs_query_stats_t),
        c_int32,
    ]
    ecs_query_cache_stats_reduce_last.restype = None
    break

# vendor/flecs/flecs.h: 13343
for _lib in _libs.values():
    if not _lib.has("ecs_query_cache_stats_repeat_last", "cdecl"):
        continue
    ecs_query_cache_stats_repeat_last = _lib.get(
        "ecs_query_cache_stats_repeat_last", "cdecl"
    )
    ecs_query_cache_stats_repeat_last.argtypes = [POINTER(ecs_query_stats_t)]
    ecs_query_cache_stats_repeat_last.restype = None
    break

# vendor/flecs/flecs.h: 13348
for _lib in _libs.values():
    if not _lib.has("ecs_query_cache_stats_copy_last", "cdecl"):
        continue
    ecs_query_cache_stats_copy_last = _lib.get(
        "ecs_query_cache_stats_copy_last", "cdecl"
    )
    ecs_query_cache_stats_copy_last.argtypes = [
        POINTER(ecs_query_stats_t),
        POINTER(ecs_query_stats_t),
    ]
    ecs_query_cache_stats_copy_last.restype = None
    break

# vendor/flecs/flecs.h: 13361
for _lib in _libs.values():
    if not _lib.has("ecs_system_stats_get", "cdecl"):
        continue
    ecs_system_stats_get = _lib.get("ecs_system_stats_get", "cdecl")
    ecs_system_stats_get.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        POINTER(ecs_system_stats_t),
    ]
    ecs_system_stats_get.restype = c_bool
    break

# vendor/flecs/flecs.h: 13368
for _lib in _libs.values():
    if not _lib.has("ecs_system_stats_reduce", "cdecl"):
        continue
    ecs_system_stats_reduce = _lib.get("ecs_system_stats_reduce", "cdecl")
    ecs_system_stats_reduce.argtypes = [
        POINTER(ecs_system_stats_t),
        POINTER(ecs_system_stats_t),
    ]
    ecs_system_stats_reduce.restype = None
    break

# vendor/flecs/flecs.h: 13374
for _lib in _libs.values():
    if not _lib.has("ecs_system_stats_reduce_last", "cdecl"):
        continue
    ecs_system_stats_reduce_last = _lib.get("ecs_system_stats_reduce_last", "cdecl")
    ecs_system_stats_reduce_last.argtypes = [
        POINTER(ecs_system_stats_t),
        POINTER(ecs_system_stats_t),
        c_int32,
    ]
    ecs_system_stats_reduce_last.restype = None
    break

# vendor/flecs/flecs.h: 13381
for _lib in _libs.values():
    if not _lib.has("ecs_system_stats_repeat_last", "cdecl"):
        continue
    ecs_system_stats_repeat_last = _lib.get("ecs_system_stats_repeat_last", "cdecl")
    ecs_system_stats_repeat_last.argtypes = [POINTER(ecs_system_stats_t)]
    ecs_system_stats_repeat_last.restype = None
    break

# vendor/flecs/flecs.h: 13386
for _lib in _libs.values():
    if not _lib.has("ecs_system_stats_copy_last", "cdecl"):
        continue
    ecs_system_stats_copy_last = _lib.get("ecs_system_stats_copy_last", "cdecl")
    ecs_system_stats_copy_last.argtypes = [
        POINTER(ecs_system_stats_t),
        POINTER(ecs_system_stats_t),
    ]
    ecs_system_stats_copy_last.restype = None
    break

# vendor/flecs/flecs.h: 13399
for _lib in _libs.values():
    if not _lib.has("ecs_pipeline_stats_get", "cdecl"):
        continue
    ecs_pipeline_stats_get = _lib.get("ecs_pipeline_stats_get", "cdecl")
    ecs_pipeline_stats_get.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        POINTER(ecs_pipeline_stats_t),
    ]
    ecs_pipeline_stats_get.restype = c_bool
    break

# vendor/flecs/flecs.h: 13409
for _lib in _libs.values():
    if not _lib.has("ecs_pipeline_stats_fini", "cdecl"):
        continue
    ecs_pipeline_stats_fini = _lib.get("ecs_pipeline_stats_fini", "cdecl")
    ecs_pipeline_stats_fini.argtypes = [POINTER(ecs_pipeline_stats_t)]
    ecs_pipeline_stats_fini.restype = None
    break

# vendor/flecs/flecs.h: 13414
for _lib in _libs.values():
    if not _lib.has("ecs_pipeline_stats_reduce", "cdecl"):
        continue
    ecs_pipeline_stats_reduce = _lib.get("ecs_pipeline_stats_reduce", "cdecl")
    ecs_pipeline_stats_reduce.argtypes = [
        POINTER(ecs_pipeline_stats_t),
        POINTER(ecs_pipeline_stats_t),
    ]
    ecs_pipeline_stats_reduce.restype = None
    break

# vendor/flecs/flecs.h: 13420
for _lib in _libs.values():
    if not _lib.has("ecs_pipeline_stats_reduce_last", "cdecl"):
        continue
    ecs_pipeline_stats_reduce_last = _lib.get("ecs_pipeline_stats_reduce_last", "cdecl")
    ecs_pipeline_stats_reduce_last.argtypes = [
        POINTER(ecs_pipeline_stats_t),
        POINTER(ecs_pipeline_stats_t),
        c_int32,
    ]
    ecs_pipeline_stats_reduce_last.restype = None
    break

# vendor/flecs/flecs.h: 13427
for _lib in _libs.values():
    if not _lib.has("ecs_pipeline_stats_repeat_last", "cdecl"):
        continue
    ecs_pipeline_stats_repeat_last = _lib.get("ecs_pipeline_stats_repeat_last", "cdecl")
    ecs_pipeline_stats_repeat_last.argtypes = [POINTER(ecs_pipeline_stats_t)]
    ecs_pipeline_stats_repeat_last.restype = None
    break

# vendor/flecs/flecs.h: 13438
for _lib in _libs.values():
    if not _lib.has("ecs_pipeline_stats_copy_last", "cdecl"):
        continue
    ecs_pipeline_stats_copy_last = _lib.get("ecs_pipeline_stats_copy_last", "cdecl")
    ecs_pipeline_stats_copy_last.argtypes = [
        POINTER(ecs_pipeline_stats_t),
        POINTER(ecs_pipeline_stats_t),
    ]
    ecs_pipeline_stats_copy_last.restype = None
    break

# vendor/flecs/flecs.h: 13444
for _lib in _libs.values():
    if not _lib.has("ecs_metric_reduce", "cdecl"):
        continue
    ecs_metric_reduce = _lib.get("ecs_metric_reduce", "cdecl")
    ecs_metric_reduce.argtypes = [
        POINTER(ecs_metric_t),
        POINTER(ecs_metric_t),
        c_int32,
        c_int32,
    ]
    ecs_metric_reduce.restype = None
    break

# vendor/flecs/flecs.h: 13452
for _lib in _libs.values():
    if not _lib.has("ecs_metric_reduce_last", "cdecl"):
        continue
    ecs_metric_reduce_last = _lib.get("ecs_metric_reduce_last", "cdecl")
    ecs_metric_reduce_last.argtypes = [POINTER(ecs_metric_t), c_int32, c_int32]
    ecs_metric_reduce_last.restype = None
    break

# vendor/flecs/flecs.h: 13459
for _lib in _libs.values():
    if not _lib.has("ecs_metric_copy", "cdecl"):
        continue
    ecs_metric_copy = _lib.get("ecs_metric_copy", "cdecl")
    ecs_metric_copy.argtypes = [POINTER(ecs_metric_t), c_int32, c_int32]
    ecs_metric_copy.restype = None
    break

# vendor/flecs/flecs.h: 13464
for _lib in _libs.values():
    try:
        FLECS_IDFlecsStatsID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDFlecsStatsID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13465
for _lib in _libs.values():
    try:
        FLECS_IDEcsWorldStatsID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsWorldStatsID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 13466
for _lib in _libs.values():
    try:
        FLECS_IDEcsWorldSummaryID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsWorldSummaryID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 13467
for _lib in _libs.values():
    try:
        FLECS_IDEcsSystemStatsID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsSystemStatsID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 13468
for _lib in _libs.values():
    try:
        FLECS_IDEcsPipelineStatsID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsPipelineStatsID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 13470
for _lib in _libs.values():
    try:
        EcsPeriod1s = (ecs_entity_t).in_dll(_lib, "EcsPeriod1s")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13471
for _lib in _libs.values():
    try:
        EcsPeriod1m = (ecs_entity_t).in_dll(_lib, "EcsPeriod1m")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13472
for _lib in _libs.values():
    try:
        EcsPeriod1h = (ecs_entity_t).in_dll(_lib, "EcsPeriod1h")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13473
for _lib in _libs.values():
    try:
        EcsPeriod1d = (ecs_entity_t).in_dll(_lib, "EcsPeriod1d")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13474
for _lib in _libs.values():
    try:
        EcsPeriod1w = (ecs_entity_t).in_dll(_lib, "EcsPeriod1w")
        break
    except:
        pass


# vendor/flecs/flecs.h: 13480
class struct_anon_31(Structure):
    pass


struct_anon_31.__slots__ = [
    "elapsed",
    "reduce_count",
]
struct_anon_31._fields_ = [
    ("elapsed", c_float),
    ("reduce_count", c_int32),
]

EcsStatsHeader = struct_anon_31  # vendor/flecs/flecs.h: 13480


# vendor/flecs/flecs.h: 13486
class struct_anon_32(Structure):
    pass


struct_anon_32.__slots__ = [
    "hdr",
    "stats",
]
struct_anon_32._fields_ = [
    ("hdr", EcsStatsHeader),
    ("stats", ecs_world_stats_t),
]

EcsWorldStats = struct_anon_32  # vendor/flecs/flecs.h: 13486


# vendor/flecs/flecs.h: 13492
class struct_anon_33(Structure):
    pass


struct_anon_33.__slots__ = [
    "hdr",
    "stats",
]
struct_anon_33._fields_ = [
    ("hdr", EcsStatsHeader),
    ("stats", ecs_map_t),
]

EcsSystemStats = struct_anon_33  # vendor/flecs/flecs.h: 13492


# vendor/flecs/flecs.h: 13498
class struct_anon_34(Structure):
    pass


struct_anon_34.__slots__ = [
    "hdr",
    "stats",
]
struct_anon_34._fields_ = [
    ("hdr", EcsStatsHeader),
    ("stats", ecs_map_t),
]

EcsPipelineStats = struct_anon_34  # vendor/flecs/flecs.h: 13498


# vendor/flecs/flecs.h: 13521
class struct_anon_35(Structure):
    pass


struct_anon_35.__slots__ = [
    "target_fps",
    "time_scale",
    "frame_time_total",
    "system_time_total",
    "merge_time_total",
    "frame_time_last",
    "system_time_last",
    "merge_time_last",
    "frame_count",
    "command_count",
    "build_info",
]
struct_anon_35._fields_ = [
    ("target_fps", c_double),
    ("time_scale", c_double),
    ("frame_time_total", c_double),
    ("system_time_total", c_double),
    ("merge_time_total", c_double),
    ("frame_time_last", c_double),
    ("system_time_last", c_double),
    ("merge_time_last", c_double),
    ("frame_count", c_int64),
    ("command_count", c_int64),
    ("build_info", ecs_build_info_t),
]

EcsWorldSummary = struct_anon_35  # vendor/flecs/flecs.h: 13521

# vendor/flecs/flecs.h: 13532
for _lib in _libs.values():
    if not _lib.has("FlecsStatsImport", "cdecl"):
        continue
    FlecsStatsImport = _lib.get("FlecsStatsImport", "cdecl")
    FlecsStatsImport.argtypes = [POINTER(ecs_world_t)]
    FlecsStatsImport.restype = None
    break

# vendor/flecs/flecs.h: 13589
for _lib in _libs.values():
    try:
        FLECS_IDFlecsMetricsID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDFlecsMetricsID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13592
for _lib in _libs.values():
    try:
        EcsMetric = (ecs_entity_t).in_dll(_lib, "EcsMetric")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13592
for _lib in _libs.values():
    try:
        FLECS_IDEcsMetricID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsMetricID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13595
for _lib in _libs.values():
    try:
        EcsCounter = (ecs_entity_t).in_dll(_lib, "EcsCounter")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13595
for _lib in _libs.values():
    try:
        FLECS_IDEcsCounterID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsCounterID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13598
for _lib in _libs.values():
    try:
        EcsCounterIncrement = (ecs_entity_t).in_dll(_lib, "EcsCounterIncrement")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13598
for _lib in _libs.values():
    try:
        FLECS_IDEcsCounterIncrementID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsCounterIncrementID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 13601
for _lib in _libs.values():
    try:
        EcsCounterId = (ecs_entity_t).in_dll(_lib, "EcsCounterId")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13601
for _lib in _libs.values():
    try:
        FLECS_IDEcsCounterIdID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsCounterIdID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13604
for _lib in _libs.values():
    try:
        EcsGauge = (ecs_entity_t).in_dll(_lib, "EcsGauge")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13604
for _lib in _libs.values():
    try:
        FLECS_IDEcsGaugeID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsGaugeID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13607
for _lib in _libs.values():
    try:
        EcsMetricInstance = (ecs_entity_t).in_dll(_lib, "EcsMetricInstance")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13607
for _lib in _libs.values():
    try:
        FLECS_IDEcsMetricInstanceID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsMetricInstanceID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 13610
for _lib in _libs.values():
    try:
        FLECS_IDEcsMetricValueID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsMetricValueID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 13613
for _lib in _libs.values():
    try:
        FLECS_IDEcsMetricSourceID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsMetricSourceID_"
        )
        break
    except:
        pass


# vendor/flecs/flecs.h: 13618
class struct_EcsMetricValue(Structure):
    pass


struct_EcsMetricValue.__slots__ = [
    "value",
]
struct_EcsMetricValue._fields_ = [
    ("value", c_double),
]

EcsMetricValue = struct_EcsMetricValue  # vendor/flecs/flecs.h: 13618


# vendor/flecs/flecs.h: 13623
class struct_EcsMetricSource(Structure):
    pass


struct_EcsMetricSource.__slots__ = [
    "entity",
]
struct_EcsMetricSource._fields_ = [
    ("entity", ecs_entity_t),
]

EcsMetricSource = struct_EcsMetricSource  # vendor/flecs/flecs.h: 13623


# vendor/flecs/flecs.h: 13656
class struct_ecs_metric_desc_t(Structure):
    pass


struct_ecs_metric_desc_t.__slots__ = [
    "_canary",
    "entity",
    "member",
    "dotmember",
    "id",
    "targets",
    "kind",
    "brief",
]
struct_ecs_metric_desc_t._fields_ = [
    ("_canary", c_int32),
    ("entity", ecs_entity_t),
    ("member", ecs_entity_t),
    ("dotmember", String),
    ("id", ecs_id_t),
    ("targets", c_bool),
    ("kind", ecs_entity_t),
    ("brief", String),
]

ecs_metric_desc_t = struct_ecs_metric_desc_t  # vendor/flecs/flecs.h: 13656

# vendor/flecs/flecs.h: 13698
for _lib in _libs.values():
    if not _lib.has("ecs_metric_init", "cdecl"):
        continue
    ecs_metric_init = _lib.get("ecs_metric_init", "cdecl")
    ecs_metric_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_metric_desc_t)]
    ecs_metric_init.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 13725
for _lib in _libs.values():
    if not _lib.has("FlecsMetricsImport", "cdecl"):
        continue
    FlecsMetricsImport = _lib.get("FlecsMetricsImport", "cdecl")
    FlecsMetricsImport.argtypes = [POINTER(ecs_world_t)]
    FlecsMetricsImport.restype = None
    break

# vendor/flecs/flecs.h: 13777
for _lib in _libs.values():
    try:
        FLECS_IDFlecsAlertsID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDFlecsAlertsID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13781
for _lib in _libs.values():
    try:
        FLECS_IDEcsAlertID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsAlertID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13782
for _lib in _libs.values():
    try:
        FLECS_IDEcsAlertInstanceID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsAlertInstanceID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 13783
for _lib in _libs.values():
    try:
        FLECS_IDEcsAlertsActiveID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsAlertsActiveID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 13784
for _lib in _libs.values():
    try:
        FLECS_IDEcsAlertTimeoutID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsAlertTimeoutID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 13787
for _lib in _libs.values():
    try:
        EcsAlertInfo = (ecs_entity_t).in_dll(_lib, "EcsAlertInfo")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13787
for _lib in _libs.values():
    try:
        FLECS_IDEcsAlertInfoID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsAlertInfoID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13788
for _lib in _libs.values():
    try:
        EcsAlertWarning = (ecs_entity_t).in_dll(_lib, "EcsAlertWarning")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13788
for _lib in _libs.values():
    try:
        FLECS_IDEcsAlertWarningID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsAlertWarningID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 13789
for _lib in _libs.values():
    try:
        EcsAlertError = (ecs_entity_t).in_dll(_lib, "EcsAlertError")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13789
for _lib in _libs.values():
    try:
        FLECS_IDEcsAlertErrorID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsAlertErrorID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 13790
for _lib in _libs.values():
    try:
        EcsAlertCritical = (ecs_entity_t).in_dll(_lib, "EcsAlertCritical")
        break
    except:
        pass

# vendor/flecs/flecs.h: 13790
for _lib in _libs.values():
    try:
        FLECS_IDEcsAlertCriticalID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsAlertCriticalID_"
        )
        break
    except:
        pass


# vendor/flecs/flecs.h: 13795
class struct_EcsAlertInstance(Structure):
    pass


struct_EcsAlertInstance.__slots__ = [
    "message",
]
struct_EcsAlertInstance._fields_ = [
    ("message", String),
]

EcsAlertInstance = struct_EcsAlertInstance  # vendor/flecs/flecs.h: 13795


# vendor/flecs/flecs.h: 13803
class struct_EcsAlertsActive(Structure):
    pass


struct_EcsAlertsActive.__slots__ = [
    "info_count",
    "warning_count",
    "error_count",
    "alerts",
]
struct_EcsAlertsActive._fields_ = [
    ("info_count", c_int32),
    ("warning_count", c_int32),
    ("error_count", c_int32),
    ("alerts", ecs_map_t),
]

EcsAlertsActive = struct_EcsAlertsActive  # vendor/flecs/flecs.h: 13803


# vendor/flecs/flecs.h: 13817
class struct_ecs_alert_severity_filter_t(Structure):
    pass


struct_ecs_alert_severity_filter_t.__slots__ = [
    "severity",
    "with",
    "var",
    "_var_index",
]
struct_ecs_alert_severity_filter_t._fields_ = [
    ("severity", ecs_entity_t),
    ("with", ecs_id_t),
    ("var", String),
    ("_var_index", c_int32),
]

ecs_alert_severity_filter_t = (
    struct_ecs_alert_severity_filter_t  # vendor/flecs/flecs.h: 13817
)


# vendor/flecs/flecs.h: 13876
class struct_ecs_alert_desc_t(Structure):
    pass


struct_ecs_alert_desc_t.__slots__ = [
    "_canary",
    "entity",
    "query",
    "message",
    "doc_name",
    "brief",
    "severity",
    "severity_filters",
    "retain_period",
    "member",
    "id",
    "var",
]
struct_ecs_alert_desc_t._fields_ = [
    ("_canary", c_int32),
    ("entity", ecs_entity_t),
    ("query", ecs_query_desc_t),
    ("message", String),
    ("doc_name", String),
    ("brief", String),
    ("severity", ecs_entity_t),
    ("severity_filters", ecs_alert_severity_filter_t * int(4)),
    ("retain_period", c_float),
    ("member", ecs_entity_t),
    ("id", ecs_id_t),
    ("var", String),
]

ecs_alert_desc_t = struct_ecs_alert_desc_t  # vendor/flecs/flecs.h: 13876

# vendor/flecs/flecs.h: 13904
for _lib in _libs.values():
    if not _lib.has("ecs_alert_init", "cdecl"):
        continue
    ecs_alert_init = _lib.get("ecs_alert_init", "cdecl")
    ecs_alert_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_alert_desc_t)]
    ecs_alert_init.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 13926
for _lib in _libs.values():
    if not _lib.has("ecs_get_alert_count", "cdecl"):
        continue
    ecs_get_alert_count = _lib.get("ecs_get_alert_count", "cdecl")
    ecs_get_alert_count.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_entity_t]
    ecs_get_alert_count.restype = c_int32
    break

# vendor/flecs/flecs.h: 13941
for _lib in _libs.values():
    if not _lib.has("ecs_get_alert", "cdecl"):
        continue
    ecs_get_alert = _lib.get("ecs_get_alert", "cdecl")
    ecs_get_alert.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_entity_t]
    ecs_get_alert.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 13955
for _lib in _libs.values():
    if not _lib.has("FlecsAlertsImport", "cdecl"):
        continue
    FlecsAlertsImport = _lib.get("FlecsAlertsImport", "cdecl")
    FlecsAlertsImport.argtypes = [POINTER(ecs_world_t)]
    FlecsAlertsImport.restype = None
    break


# vendor/flecs/flecs.h: 14029
class struct_ecs_from_json_desc_t(Structure):
    pass


struct_ecs_from_json_desc_t.__slots__ = [
    "name",
    "expr",
    "lookup_action",
    "lookup_ctx",
    "strict",
]
struct_ecs_from_json_desc_t._fields_ = [
    ("name", String),
    ("expr", String),
    (
        "lookup_action",
        CFUNCTYPE(UNCHECKED(ecs_entity_t), POINTER(ecs_world_t), String, POINTER(None)),
    ),
    ("lookup_ctx", POINTER(None)),
    ("strict", c_bool),
]

ecs_from_json_desc_t = struct_ecs_from_json_desc_t  # vendor/flecs/flecs.h: 14029

# vendor/flecs/flecs.h: 14043
for _lib in _libs.values():
    if not _lib.has("ecs_ptr_from_json", "cdecl"):
        continue
    ecs_ptr_from_json = _lib.get("ecs_ptr_from_json", "cdecl")
    ecs_ptr_from_json.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        POINTER(None),
        String,
        POINTER(ecs_from_json_desc_t),
    ]
    ecs_ptr_from_json.restype = c_char_p
    break

# vendor/flecs/flecs.h: 14061
for _lib in _libs.values():
    if not _lib.has("ecs_entity_from_json", "cdecl"):
        continue
    ecs_entity_from_json = _lib.get("ecs_entity_from_json", "cdecl")
    ecs_entity_from_json.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        String,
        POINTER(ecs_from_json_desc_t),
    ]
    ecs_entity_from_json.restype = c_char_p
    break

# vendor/flecs/flecs.h: 14076
for _lib in _libs.values():
    if not _lib.has("ecs_world_from_json", "cdecl"):
        continue
    ecs_world_from_json = _lib.get("ecs_world_from_json", "cdecl")
    ecs_world_from_json.argtypes = [
        POINTER(ecs_world_t),
        String,
        POINTER(ecs_from_json_desc_t),
    ]
    ecs_world_from_json.restype = c_char_p
    break

# vendor/flecs/flecs.h: 14089
for _lib in _libs.values():
    if not _lib.has("ecs_world_from_json_file", "cdecl"):
        continue
    ecs_world_from_json_file = _lib.get("ecs_world_from_json_file", "cdecl")
    ecs_world_from_json_file.argtypes = [
        POINTER(ecs_world_t),
        String,
        POINTER(ecs_from_json_desc_t),
    ]
    ecs_world_from_json_file.restype = c_char_p
    break

# vendor/flecs/flecs.h: 14109
for _lib in _libs.values():
    if not _lib.has("ecs_array_to_json", "cdecl"):
        continue
    ecs_array_to_json = _lib.get("ecs_array_to_json", "cdecl")
    ecs_array_to_json.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        POINTER(None),
        c_int32,
    ]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_array_to_json.restype = ReturnString
    else:
        ecs_array_to_json.restype = String
        ecs_array_to_json.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 14126
for _lib in _libs.values():
    if not _lib.has("ecs_array_to_json_buf", "cdecl"):
        continue
    ecs_array_to_json_buf = _lib.get("ecs_array_to_json_buf", "cdecl")
    ecs_array_to_json_buf.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        POINTER(None),
        c_int32,
        POINTER(ecs_strbuf_t),
    ]
    ecs_array_to_json_buf.restype = c_int
    break

# vendor/flecs/flecs.h: 14142
for _lib in _libs.values():
    if not _lib.has("ecs_ptr_to_json", "cdecl"):
        continue
    ecs_ptr_to_json = _lib.get("ecs_ptr_to_json", "cdecl")
    ecs_ptr_to_json.argtypes = [POINTER(ecs_world_t), ecs_entity_t, POINTER(None)]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_ptr_to_json.restype = ReturnString
    else:
        ecs_ptr_to_json.restype = String
        ecs_ptr_to_json.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 14157
for _lib in _libs.values():
    if not _lib.has("ecs_ptr_to_json_buf", "cdecl"):
        continue
    ecs_ptr_to_json_buf = _lib.get("ecs_ptr_to_json_buf", "cdecl")
    ecs_ptr_to_json_buf.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        POINTER(None),
        POINTER(ecs_strbuf_t),
    ]
    ecs_ptr_to_json_buf.restype = c_int
    break

# vendor/flecs/flecs.h: 14174
for _lib in _libs.values():
    if not _lib.has("ecs_type_info_to_json", "cdecl"):
        continue
    ecs_type_info_to_json = _lib.get("ecs_type_info_to_json", "cdecl")
    ecs_type_info_to_json.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_type_info_to_json.restype = ReturnString
    else:
        ecs_type_info_to_json.restype = String
        ecs_type_info_to_json.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 14187
for _lib in _libs.values():
    if not _lib.has("ecs_type_info_to_json_buf", "cdecl"):
        continue
    ecs_type_info_to_json_buf = _lib.get("ecs_type_info_to_json_buf", "cdecl")
    ecs_type_info_to_json_buf.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        POINTER(ecs_strbuf_t),
    ]
    ecs_type_info_to_json_buf.restype = c_int
    break


# vendor/flecs/flecs.h: 14204
class struct_ecs_entity_to_json_desc_t(Structure):
    pass


struct_ecs_entity_to_json_desc_t.__slots__ = [
    "serialize_entity_id",
    "serialize_doc",
    "serialize_full_paths",
    "serialize_inherited",
    "serialize_values",
    "serialize_builtin",
    "serialize_type_info",
    "serialize_alerts",
    "serialize_refs",
    "serialize_matches",
]
struct_ecs_entity_to_json_desc_t._fields_ = [
    ("serialize_entity_id", c_bool),
    ("serialize_doc", c_bool),
    ("serialize_full_paths", c_bool),
    ("serialize_inherited", c_bool),
    ("serialize_values", c_bool),
    ("serialize_builtin", c_bool),
    ("serialize_type_info", c_bool),
    ("serialize_alerts", c_bool),
    ("serialize_refs", ecs_entity_t),
    ("serialize_matches", c_bool),
]

ecs_entity_to_json_desc_t = (
    struct_ecs_entity_to_json_desc_t  # vendor/flecs/flecs.h: 14204
)

# vendor/flecs/flecs.h: 14246
for _lib in _libs.values():
    if not _lib.has("ecs_entity_to_json", "cdecl"):
        continue
    ecs_entity_to_json = _lib.get("ecs_entity_to_json", "cdecl")
    ecs_entity_to_json.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        POINTER(ecs_entity_to_json_desc_t),
    ]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_entity_to_json.restype = ReturnString
    else:
        ecs_entity_to_json.restype = String
        ecs_entity_to_json.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 14260
for _lib in _libs.values():
    if not _lib.has("ecs_entity_to_json_buf", "cdecl"):
        continue
    ecs_entity_to_json_buf = _lib.get("ecs_entity_to_json_buf", "cdecl")
    ecs_entity_to_json_buf.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        POINTER(ecs_strbuf_t),
        POINTER(ecs_entity_to_json_desc_t),
    ]
    ecs_entity_to_json_buf.restype = c_int
    break


# vendor/flecs/flecs.h: 14286
class struct_ecs_iter_to_json_desc_t(Structure):
    pass


struct_ecs_iter_to_json_desc_t.__slots__ = [
    "serialize_entity_ids",
    "serialize_values",
    "serialize_builtin",
    "serialize_doc",
    "serialize_full_paths",
    "serialize_fields",
    "serialize_inherited",
    "serialize_table",
    "serialize_type_info",
    "serialize_field_info",
    "serialize_query_info",
    "serialize_query_plan",
    "serialize_query_profile",
    "dont_serialize_results",
    "serialize_alerts",
    "serialize_refs",
    "serialize_matches",
    "query",
]
struct_ecs_iter_to_json_desc_t._fields_ = [
    ("serialize_entity_ids", c_bool),
    ("serialize_values", c_bool),
    ("serialize_builtin", c_bool),
    ("serialize_doc", c_bool),
    ("serialize_full_paths", c_bool),
    ("serialize_fields", c_bool),
    ("serialize_inherited", c_bool),
    ("serialize_table", c_bool),
    ("serialize_type_info", c_bool),
    ("serialize_field_info", c_bool),
    ("serialize_query_info", c_bool),
    ("serialize_query_plan", c_bool),
    ("serialize_query_profile", c_bool),
    ("dont_serialize_results", c_bool),
    ("serialize_alerts", c_bool),
    ("serialize_refs", ecs_entity_t),
    ("serialize_matches", c_bool),
    ("query", POINTER(ecs_poly_t)),
]

ecs_iter_to_json_desc_t = struct_ecs_iter_to_json_desc_t  # vendor/flecs/flecs.h: 14286

# vendor/flecs/flecs.h: 14341
for _lib in _libs.values():
    if not _lib.has("ecs_iter_to_json", "cdecl"):
        continue
    ecs_iter_to_json = _lib.get("ecs_iter_to_json", "cdecl")
    ecs_iter_to_json.argtypes = [POINTER(ecs_iter_t), POINTER(ecs_iter_to_json_desc_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_iter_to_json.restype = ReturnString
    else:
        ecs_iter_to_json.restype = String
        ecs_iter_to_json.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 14353
for _lib in _libs.values():
    if not _lib.has("ecs_iter_to_json_buf", "cdecl"):
        continue
    ecs_iter_to_json_buf = _lib.get("ecs_iter_to_json_buf", "cdecl")
    ecs_iter_to_json_buf.argtypes = [
        POINTER(ecs_iter_t),
        POINTER(ecs_strbuf_t),
        POINTER(ecs_iter_to_json_desc_t),
    ]
    ecs_iter_to_json_buf.restype = c_int
    break


# vendor/flecs/flecs.h: 14362
class struct_ecs_world_to_json_desc_t(Structure):
    pass


struct_ecs_world_to_json_desc_t.__slots__ = [
    "serialize_builtin",
    "serialize_modules",
]
struct_ecs_world_to_json_desc_t._fields_ = [
    ("serialize_builtin", c_bool),
    ("serialize_modules", c_bool),
]

ecs_world_to_json_desc_t = (
    struct_ecs_world_to_json_desc_t  # vendor/flecs/flecs.h: 14362
)

# vendor/flecs/flecs.h: 14382
for _lib in _libs.values():
    if not _lib.has("ecs_world_to_json", "cdecl"):
        continue
    ecs_world_to_json = _lib.get("ecs_world_to_json", "cdecl")
    ecs_world_to_json.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_world_to_json_desc_t),
    ]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_world_to_json.restype = ReturnString
    else:
        ecs_world_to_json.restype = String
        ecs_world_to_json.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 14394
for _lib in _libs.values():
    if not _lib.has("ecs_world_to_json_buf", "cdecl"):
        continue
    ecs_world_to_json_buf = _lib.get("ecs_world_to_json_buf", "cdecl")
    ecs_world_to_json_buf.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_strbuf_t),
        POINTER(ecs_world_to_json_desc_t),
    ]
    ecs_world_to_json_buf.restype = c_int
    break

# vendor/flecs/flecs.h: 14472
for _lib in _libs.values():
    try:
        EcsUnitPrefixes = (ecs_entity_t).in_dll(_lib, "EcsUnitPrefixes")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14474
for _lib in _libs.values():
    try:
        EcsYocto = (ecs_entity_t).in_dll(_lib, "EcsYocto")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14475
for _lib in _libs.values():
    try:
        EcsZepto = (ecs_entity_t).in_dll(_lib, "EcsZepto")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14476
for _lib in _libs.values():
    try:
        EcsAtto = (ecs_entity_t).in_dll(_lib, "EcsAtto")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14477
for _lib in _libs.values():
    try:
        EcsFemto = (ecs_entity_t).in_dll(_lib, "EcsFemto")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14478
for _lib in _libs.values():
    try:
        EcsPico = (ecs_entity_t).in_dll(_lib, "EcsPico")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14479
for _lib in _libs.values():
    try:
        EcsNano = (ecs_entity_t).in_dll(_lib, "EcsNano")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14480
for _lib in _libs.values():
    try:
        EcsMicro = (ecs_entity_t).in_dll(_lib, "EcsMicro")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14481
for _lib in _libs.values():
    try:
        EcsMilli = (ecs_entity_t).in_dll(_lib, "EcsMilli")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14482
for _lib in _libs.values():
    try:
        EcsCenti = (ecs_entity_t).in_dll(_lib, "EcsCenti")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14483
for _lib in _libs.values():
    try:
        EcsDeci = (ecs_entity_t).in_dll(_lib, "EcsDeci")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14484
for _lib in _libs.values():
    try:
        EcsDeca = (ecs_entity_t).in_dll(_lib, "EcsDeca")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14485
for _lib in _libs.values():
    try:
        EcsHecto = (ecs_entity_t).in_dll(_lib, "EcsHecto")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14486
for _lib in _libs.values():
    try:
        EcsKilo = (ecs_entity_t).in_dll(_lib, "EcsKilo")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14487
for _lib in _libs.values():
    try:
        EcsMega = (ecs_entity_t).in_dll(_lib, "EcsMega")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14488
for _lib in _libs.values():
    try:
        EcsGiga = (ecs_entity_t).in_dll(_lib, "EcsGiga")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14489
for _lib in _libs.values():
    try:
        EcsTera = (ecs_entity_t).in_dll(_lib, "EcsTera")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14490
for _lib in _libs.values():
    try:
        EcsPeta = (ecs_entity_t).in_dll(_lib, "EcsPeta")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14491
for _lib in _libs.values():
    try:
        EcsExa = (ecs_entity_t).in_dll(_lib, "EcsExa")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14492
for _lib in _libs.values():
    try:
        EcsZetta = (ecs_entity_t).in_dll(_lib, "EcsZetta")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14493
for _lib in _libs.values():
    try:
        EcsYotta = (ecs_entity_t).in_dll(_lib, "EcsYotta")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14495
for _lib in _libs.values():
    try:
        EcsKibi = (ecs_entity_t).in_dll(_lib, "EcsKibi")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14496
for _lib in _libs.values():
    try:
        EcsMebi = (ecs_entity_t).in_dll(_lib, "EcsMebi")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14497
for _lib in _libs.values():
    try:
        EcsGibi = (ecs_entity_t).in_dll(_lib, "EcsGibi")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14498
for _lib in _libs.values():
    try:
        EcsTebi = (ecs_entity_t).in_dll(_lib, "EcsTebi")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14499
for _lib in _libs.values():
    try:
        EcsPebi = (ecs_entity_t).in_dll(_lib, "EcsPebi")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14500
for _lib in _libs.values():
    try:
        EcsExbi = (ecs_entity_t).in_dll(_lib, "EcsExbi")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14501
for _lib in _libs.values():
    try:
        EcsZebi = (ecs_entity_t).in_dll(_lib, "EcsZebi")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14502
for _lib in _libs.values():
    try:
        EcsYobi = (ecs_entity_t).in_dll(_lib, "EcsYobi")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14512
for _lib in _libs.values():
    try:
        EcsDuration = (ecs_entity_t).in_dll(_lib, "EcsDuration")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14513
for _lib in _libs.values():
    try:
        EcsPicoSeconds = (ecs_entity_t).in_dll(_lib, "EcsPicoSeconds")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14514
for _lib in _libs.values():
    try:
        EcsNanoSeconds = (ecs_entity_t).in_dll(_lib, "EcsNanoSeconds")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14515
for _lib in _libs.values():
    try:
        EcsMicroSeconds = (ecs_entity_t).in_dll(_lib, "EcsMicroSeconds")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14516
for _lib in _libs.values():
    try:
        EcsMilliSeconds = (ecs_entity_t).in_dll(_lib, "EcsMilliSeconds")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14517
for _lib in _libs.values():
    try:
        EcsSeconds = (ecs_entity_t).in_dll(_lib, "EcsSeconds")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14518
for _lib in _libs.values():
    try:
        EcsMinutes = (ecs_entity_t).in_dll(_lib, "EcsMinutes")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14519
for _lib in _libs.values():
    try:
        EcsHours = (ecs_entity_t).in_dll(_lib, "EcsHours")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14520
for _lib in _libs.values():
    try:
        EcsDays = (ecs_entity_t).in_dll(_lib, "EcsDays")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14530
for _lib in _libs.values():
    try:
        EcsTime = (ecs_entity_t).in_dll(_lib, "EcsTime")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14531
for _lib in _libs.values():
    try:
        EcsDate = (ecs_entity_t).in_dll(_lib, "EcsDate")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14541
for _lib in _libs.values():
    try:
        EcsMass = (ecs_entity_t).in_dll(_lib, "EcsMass")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14542
for _lib in _libs.values():
    try:
        EcsGrams = (ecs_entity_t).in_dll(_lib, "EcsGrams")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14543
for _lib in _libs.values():
    try:
        EcsKiloGrams = (ecs_entity_t).in_dll(_lib, "EcsKiloGrams")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14553
for _lib in _libs.values():
    try:
        EcsElectricCurrent = (ecs_entity_t).in_dll(_lib, "EcsElectricCurrent")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14554
for _lib in _libs.values():
    try:
        EcsAmpere = (ecs_entity_t).in_dll(_lib, "EcsAmpere")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14564
for _lib in _libs.values():
    try:
        EcsAmount = (ecs_entity_t).in_dll(_lib, "EcsAmount")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14565
for _lib in _libs.values():
    try:
        EcsMole = (ecs_entity_t).in_dll(_lib, "EcsMole")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14575
for _lib in _libs.values():
    try:
        EcsLuminousIntensity = (ecs_entity_t).in_dll(_lib, "EcsLuminousIntensity")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14576
for _lib in _libs.values():
    try:
        EcsCandela = (ecs_entity_t).in_dll(_lib, "EcsCandela")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14586
for _lib in _libs.values():
    try:
        EcsForce = (ecs_entity_t).in_dll(_lib, "EcsForce")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14587
for _lib in _libs.values():
    try:
        EcsNewton = (ecs_entity_t).in_dll(_lib, "EcsNewton")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14597
for _lib in _libs.values():
    try:
        EcsLength = (ecs_entity_t).in_dll(_lib, "EcsLength")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14598
for _lib in _libs.values():
    try:
        EcsMeters = (ecs_entity_t).in_dll(_lib, "EcsMeters")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14599
for _lib in _libs.values():
    try:
        EcsPicoMeters = (ecs_entity_t).in_dll(_lib, "EcsPicoMeters")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14600
for _lib in _libs.values():
    try:
        EcsNanoMeters = (ecs_entity_t).in_dll(_lib, "EcsNanoMeters")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14601
for _lib in _libs.values():
    try:
        EcsMicroMeters = (ecs_entity_t).in_dll(_lib, "EcsMicroMeters")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14602
for _lib in _libs.values():
    try:
        EcsMilliMeters = (ecs_entity_t).in_dll(_lib, "EcsMilliMeters")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14603
for _lib in _libs.values():
    try:
        EcsCentiMeters = (ecs_entity_t).in_dll(_lib, "EcsCentiMeters")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14604
for _lib in _libs.values():
    try:
        EcsKiloMeters = (ecs_entity_t).in_dll(_lib, "EcsKiloMeters")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14605
for _lib in _libs.values():
    try:
        EcsMiles = (ecs_entity_t).in_dll(_lib, "EcsMiles")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14606
for _lib in _libs.values():
    try:
        EcsPixels = (ecs_entity_t).in_dll(_lib, "EcsPixels")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14616
for _lib in _libs.values():
    try:
        EcsPressure = (ecs_entity_t).in_dll(_lib, "EcsPressure")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14617
for _lib in _libs.values():
    try:
        EcsPascal = (ecs_entity_t).in_dll(_lib, "EcsPascal")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14618
for _lib in _libs.values():
    try:
        EcsBar = (ecs_entity_t).in_dll(_lib, "EcsBar")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14628
for _lib in _libs.values():
    try:
        EcsSpeed = (ecs_entity_t).in_dll(_lib, "EcsSpeed")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14629
for _lib in _libs.values():
    try:
        EcsMetersPerSecond = (ecs_entity_t).in_dll(_lib, "EcsMetersPerSecond")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14630
for _lib in _libs.values():
    try:
        EcsKiloMetersPerSecond = (ecs_entity_t).in_dll(_lib, "EcsKiloMetersPerSecond")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14631
for _lib in _libs.values():
    try:
        EcsKiloMetersPerHour = (ecs_entity_t).in_dll(_lib, "EcsKiloMetersPerHour")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14632
for _lib in _libs.values():
    try:
        EcsMilesPerHour = (ecs_entity_t).in_dll(_lib, "EcsMilesPerHour")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14642
for _lib in _libs.values():
    try:
        EcsTemperature = (ecs_entity_t).in_dll(_lib, "EcsTemperature")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14643
for _lib in _libs.values():
    try:
        EcsKelvin = (ecs_entity_t).in_dll(_lib, "EcsKelvin")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14644
for _lib in _libs.values():
    try:
        EcsCelsius = (ecs_entity_t).in_dll(_lib, "EcsCelsius")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14645
for _lib in _libs.values():
    try:
        EcsFahrenheit = (ecs_entity_t).in_dll(_lib, "EcsFahrenheit")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14655
for _lib in _libs.values():
    try:
        EcsData = (ecs_entity_t).in_dll(_lib, "EcsData")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14656
for _lib in _libs.values():
    try:
        EcsBits = (ecs_entity_t).in_dll(_lib, "EcsBits")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14657
for _lib in _libs.values():
    try:
        EcsKiloBits = (ecs_entity_t).in_dll(_lib, "EcsKiloBits")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14658
for _lib in _libs.values():
    try:
        EcsMegaBits = (ecs_entity_t).in_dll(_lib, "EcsMegaBits")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14659
for _lib in _libs.values():
    try:
        EcsGigaBits = (ecs_entity_t).in_dll(_lib, "EcsGigaBits")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14660
for _lib in _libs.values():
    try:
        EcsBytes = (ecs_entity_t).in_dll(_lib, "EcsBytes")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14661
for _lib in _libs.values():
    try:
        EcsKiloBytes = (ecs_entity_t).in_dll(_lib, "EcsKiloBytes")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14662
for _lib in _libs.values():
    try:
        EcsMegaBytes = (ecs_entity_t).in_dll(_lib, "EcsMegaBytes")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14663
for _lib in _libs.values():
    try:
        EcsGigaBytes = (ecs_entity_t).in_dll(_lib, "EcsGigaBytes")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14664
for _lib in _libs.values():
    try:
        EcsKibiBytes = (ecs_entity_t).in_dll(_lib, "EcsKibiBytes")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14665
for _lib in _libs.values():
    try:
        EcsMebiBytes = (ecs_entity_t).in_dll(_lib, "EcsMebiBytes")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14666
for _lib in _libs.values():
    try:
        EcsGibiBytes = (ecs_entity_t).in_dll(_lib, "EcsGibiBytes")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14676
for _lib in _libs.values():
    try:
        EcsDataRate = (ecs_entity_t).in_dll(_lib, "EcsDataRate")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14677
for _lib in _libs.values():
    try:
        EcsBitsPerSecond = (ecs_entity_t).in_dll(_lib, "EcsBitsPerSecond")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14678
for _lib in _libs.values():
    try:
        EcsKiloBitsPerSecond = (ecs_entity_t).in_dll(_lib, "EcsKiloBitsPerSecond")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14679
for _lib in _libs.values():
    try:
        EcsMegaBitsPerSecond = (ecs_entity_t).in_dll(_lib, "EcsMegaBitsPerSecond")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14680
for _lib in _libs.values():
    try:
        EcsGigaBitsPerSecond = (ecs_entity_t).in_dll(_lib, "EcsGigaBitsPerSecond")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14681
for _lib in _libs.values():
    try:
        EcsBytesPerSecond = (ecs_entity_t).in_dll(_lib, "EcsBytesPerSecond")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14682
for _lib in _libs.values():
    try:
        EcsKiloBytesPerSecond = (ecs_entity_t).in_dll(_lib, "EcsKiloBytesPerSecond")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14683
for _lib in _libs.values():
    try:
        EcsMegaBytesPerSecond = (ecs_entity_t).in_dll(_lib, "EcsMegaBytesPerSecond")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14684
for _lib in _libs.values():
    try:
        EcsGigaBytesPerSecond = (ecs_entity_t).in_dll(_lib, "EcsGigaBytesPerSecond")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14694
for _lib in _libs.values():
    try:
        EcsAngle = (ecs_entity_t).in_dll(_lib, "EcsAngle")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14695
for _lib in _libs.values():
    try:
        EcsRadians = (ecs_entity_t).in_dll(_lib, "EcsRadians")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14696
for _lib in _libs.values():
    try:
        EcsDegrees = (ecs_entity_t).in_dll(_lib, "EcsDegrees")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14706
for _lib in _libs.values():
    try:
        EcsFrequency = (ecs_entity_t).in_dll(_lib, "EcsFrequency")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14707
for _lib in _libs.values():
    try:
        EcsHertz = (ecs_entity_t).in_dll(_lib, "EcsHertz")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14708
for _lib in _libs.values():
    try:
        EcsKiloHertz = (ecs_entity_t).in_dll(_lib, "EcsKiloHertz")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14709
for _lib in _libs.values():
    try:
        EcsMegaHertz = (ecs_entity_t).in_dll(_lib, "EcsMegaHertz")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14710
for _lib in _libs.values():
    try:
        EcsGigaHertz = (ecs_entity_t).in_dll(_lib, "EcsGigaHertz")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14720
for _lib in _libs.values():
    try:
        EcsUri = (ecs_entity_t).in_dll(_lib, "EcsUri")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14721
for _lib in _libs.values():
    try:
        EcsUriHyperlink = (ecs_entity_t).in_dll(_lib, "EcsUriHyperlink")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14722
for _lib in _libs.values():
    try:
        EcsUriImage = (ecs_entity_t).in_dll(_lib, "EcsUriImage")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14723
for _lib in _libs.values():
    try:
        EcsUriFile = (ecs_entity_t).in_dll(_lib, "EcsUriFile")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14733
for _lib in _libs.values():
    try:
        EcsColor = (ecs_entity_t).in_dll(_lib, "EcsColor")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14734
for _lib in _libs.values():
    try:
        EcsColorRgb = (ecs_entity_t).in_dll(_lib, "EcsColorRgb")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14735
for _lib in _libs.values():
    try:
        EcsColorHsl = (ecs_entity_t).in_dll(_lib, "EcsColorHsl")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14736
for _lib in _libs.values():
    try:
        EcsColorCss = (ecs_entity_t).in_dll(_lib, "EcsColorCss")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14741
for _lib in _libs.values():
    try:
        EcsAcceleration = (ecs_entity_t).in_dll(_lib, "EcsAcceleration")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14742
for _lib in _libs.values():
    try:
        EcsPercentage = (ecs_entity_t).in_dll(_lib, "EcsPercentage")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14743
for _lib in _libs.values():
    try:
        EcsBel = (ecs_entity_t).in_dll(_lib, "EcsBel")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14744
for _lib in _libs.values():
    try:
        EcsDeciBel = (ecs_entity_t).in_dll(_lib, "EcsDeciBel")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14759
for _lib in _libs.values():
    if not _lib.has("FlecsUnitsImport", "cdecl"):
        continue
    FlecsUnitsImport = _lib.get("FlecsUnitsImport", "cdecl")
    FlecsUnitsImport.argtypes = [POINTER(ecs_world_t)]
    FlecsUnitsImport.restype = None
    break

# vendor/flecs/flecs.h: 14894
for _lib in _libs.values():
    try:
        FLECS_IDEcsScriptID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsScriptID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14897
for _lib in _libs.values():
    try:
        EcsScriptTemplate = (ecs_entity_t).in_dll(_lib, "EcsScriptTemplate")
        break
    except:
        pass

# vendor/flecs/flecs.h: 14897
for _lib in _libs.values():
    try:
        FLECS_IDEcsScriptTemplateID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsScriptTemplateID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 14900
for _lib in _libs.values():
    try:
        FLECS_IDEcsScriptConstVarID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsScriptConstVarID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 14903
for _lib in _libs.values():
    try:
        FLECS_IDEcsScriptFunctionID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsScriptFunctionID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 14906
for _lib in _libs.values():
    try:
        FLECS_IDEcsScriptMethodID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsScriptMethodID_"
        )
        break
    except:
        pass


# vendor/flecs/flecs.h: 14909
class struct_ecs_script_template_t(Structure):
    pass


ecs_script_template_t = struct_ecs_script_template_t  # vendor/flecs/flecs.h: 14909


# vendor/flecs/flecs.h: 14918
class struct_ecs_script_var_t(Structure):
    pass


struct_ecs_script_var_t.__slots__ = [
    "name",
    "value",
    "type_info",
    "sp",
    "is_const",
]
struct_ecs_script_var_t._fields_ = [
    ("name", String),
    ("value", ecs_value_t),
    ("type_info", POINTER(ecs_type_info_t)),
    ("sp", c_int32),
    ("is_const", c_bool),
]

ecs_script_var_t = struct_ecs_script_var_t  # vendor/flecs/flecs.h: 14918


# vendor/flecs/flecs.h: 14921
class struct_ecs_script_vars_t(Structure):
    pass


struct_ecs_script_vars_t.__slots__ = [
    "parent",
    "sp",
    "var_index",
    "vars",
    "world",
    "stack",
    "cursor",
    "allocator",
]
struct_ecs_script_vars_t._fields_ = [
    ("parent", POINTER(struct_ecs_script_vars_t)),
    ("sp", c_int32),
    ("var_index", ecs_hashmap_t),
    ("vars", ecs_vec_t),
    ("world", POINTER(ecs_world_t)),
    ("stack", POINTER(struct_ecs_stack_t)),
    ("cursor", POINTER(ecs_stack_cursor_t)),
    ("allocator", POINTER(ecs_allocator_t)),
]

ecs_script_vars_t = struct_ecs_script_vars_t  # vendor/flecs/flecs.h: 14932


# vendor/flecs/flecs.h: 14939
class struct_ecs_script_t(Structure):
    pass


struct_ecs_script_t.__slots__ = [
    "world",
    "name",
    "code",
]
struct_ecs_script_t._fields_ = [
    ("world", POINTER(ecs_world_t)),
    ("name", String),
    ("code", String),
]

ecs_script_t = struct_ecs_script_t  # vendor/flecs/flecs.h: 14939


# vendor/flecs/flecs.h: 14942
class struct_ecs_script_runtime_t(Structure):
    pass


ecs_script_runtime_t = struct_ecs_script_runtime_t  # vendor/flecs/flecs.h: 14942


# vendor/flecs/flecs.h: 14950
class struct_EcsScript(Structure):
    pass


struct_EcsScript.__slots__ = [
    "script",
    "template_",
]
struct_EcsScript._fields_ = [
    ("script", POINTER(ecs_script_t)),
    ("template_", POINTER(ecs_script_template_t)),
]

EcsScript = struct_EcsScript  # vendor/flecs/flecs.h: 14950


# vendor/flecs/flecs.h: 14957
class struct_ecs_function_ctx_t(Structure):
    pass


struct_ecs_function_ctx_t.__slots__ = [
    "world",
    "function",
    "ctx",
]
struct_ecs_function_ctx_t._fields_ = [
    ("world", POINTER(ecs_world_t)),
    ("function", ecs_entity_t),
    ("ctx", POINTER(None)),
]

ecs_function_ctx_t = struct_ecs_function_ctx_t  # vendor/flecs/flecs.h: 14957

ecs_function_callback_t = CFUNCTYPE(
    UNCHECKED(None),
    POINTER(ecs_function_ctx_t),
    c_int32,
    POINTER(ecs_value_t),
    POINTER(ecs_value_t),
)  # vendor/flecs/flecs.h: 14960


# vendor/flecs/flecs.h: 14970
class struct_ecs_script_parameter_t(Structure):
    pass


struct_ecs_script_parameter_t.__slots__ = [
    "name",
    "type",
]
struct_ecs_script_parameter_t._fields_ = [
    ("name", String),
    ("type", ecs_entity_t),
]

ecs_script_parameter_t = struct_ecs_script_parameter_t  # vendor/flecs/flecs.h: 14970


# vendor/flecs/flecs.h: 14978
class struct_EcsScriptConstVar(Structure):
    pass


struct_EcsScriptConstVar.__slots__ = [
    "value",
    "type_info",
]
struct_EcsScriptConstVar._fields_ = [
    ("value", ecs_value_t),
    ("type_info", POINTER(ecs_type_info_t)),
]

EcsScriptConstVar = struct_EcsScriptConstVar  # vendor/flecs/flecs.h: 14978


# vendor/flecs/flecs.h: 14988
class struct_EcsScriptFunction(Structure):
    pass


struct_EcsScriptFunction.__slots__ = [
    "return_type",
    "params",
    "callback",
    "ctx",
]
struct_EcsScriptFunction._fields_ = [
    ("return_type", ecs_entity_t),
    ("params", ecs_vec_t),
    ("callback", ecs_function_callback_t),
    ("ctx", POINTER(None)),
]

EcsScriptFunction = struct_EcsScriptFunction  # vendor/flecs/flecs.h: 14988


# vendor/flecs/flecs.h: 15000
class struct_EcsScriptMethod(Structure):
    pass


struct_EcsScriptMethod.__slots__ = [
    "return_type",
    "params",
    "callback",
    "ctx",
]
struct_EcsScriptMethod._fields_ = [
    ("return_type", ecs_entity_t),
    ("params", ecs_vec_t),
    ("callback", ecs_function_callback_t),
    ("ctx", POINTER(None)),
]

EcsScriptMethod = struct_EcsScriptMethod  # vendor/flecs/flecs.h: 15000


# vendor/flecs/flecs.h: 15008
class struct_ecs_script_eval_desc_t(Structure):
    pass


struct_ecs_script_eval_desc_t.__slots__ = [
    "vars",
    "runtime",
]
struct_ecs_script_eval_desc_t._fields_ = [
    ("vars", POINTER(ecs_script_vars_t)),
    ("runtime", POINTER(ecs_script_runtime_t)),
]

ecs_script_eval_desc_t = struct_ecs_script_eval_desc_t  # vendor/flecs/flecs.h: 15008

# vendor/flecs/flecs.h: 15025
for _lib in _libs.values():
    if not _lib.has("ecs_script_parse", "cdecl"):
        continue
    ecs_script_parse = _lib.get("ecs_script_parse", "cdecl")
    ecs_script_parse.argtypes = [
        POINTER(ecs_world_t),
        String,
        String,
        POINTER(ecs_script_eval_desc_t),
    ]
    ecs_script_parse.restype = POINTER(ecs_script_t)
    break

# vendor/flecs/flecs.h: 15043
for _lib in _libs.values():
    if not _lib.has("ecs_script_eval", "cdecl"):
        continue
    ecs_script_eval = _lib.get("ecs_script_eval", "cdecl")
    ecs_script_eval.argtypes = [POINTER(ecs_script_t), POINTER(ecs_script_eval_desc_t)]
    ecs_script_eval.restype = c_int
    break

# vendor/flecs/flecs.h: 15057
for _lib in _libs.values():
    if not _lib.has("ecs_script_free", "cdecl"):
        continue
    ecs_script_free = _lib.get("ecs_script_free", "cdecl")
    ecs_script_free.argtypes = [POINTER(ecs_script_t)]
    ecs_script_free.restype = None
    break

# vendor/flecs/flecs.h: 15076
for _lib in _libs.values():
    if not _lib.has("ecs_script_run", "cdecl"):
        continue
    ecs_script_run = _lib.get("ecs_script_run", "cdecl")
    ecs_script_run.argtypes = [POINTER(ecs_world_t), String, String]
    ecs_script_run.restype = c_int
    break

# vendor/flecs/flecs.h: 15091
for _lib in _libs.values():
    if not _lib.has("ecs_script_run_file", "cdecl"):
        continue
    ecs_script_run_file = _lib.get("ecs_script_run_file", "cdecl")
    ecs_script_run_file.argtypes = [POINTER(ecs_world_t), String]
    ecs_script_run_file.restype = c_int
    break

# vendor/flecs/flecs.h: 15109
for _lib in _libs.values():
    if not _lib.has("ecs_script_runtime_new", "cdecl"):
        continue
    ecs_script_runtime_new = _lib.get("ecs_script_runtime_new", "cdecl")
    ecs_script_runtime_new.argtypes = []
    ecs_script_runtime_new.restype = POINTER(ecs_script_runtime_t)
    break

# vendor/flecs/flecs.h: 15117
for _lib in _libs.values():
    if not _lib.has("ecs_script_runtime_free", "cdecl"):
        continue
    ecs_script_runtime_free = _lib.get("ecs_script_runtime_free", "cdecl")
    ecs_script_runtime_free.argtypes = [POINTER(ecs_script_runtime_t)]
    ecs_script_runtime_free.restype = None
    break

# vendor/flecs/flecs.h: 15129
for _lib in _libs.values():
    if not _lib.has("ecs_script_ast_to_buf", "cdecl"):
        continue
    ecs_script_ast_to_buf = _lib.get("ecs_script_ast_to_buf", "cdecl")
    ecs_script_ast_to_buf.argtypes = [
        POINTER(ecs_script_t),
        POINTER(ecs_strbuf_t),
        c_bool,
    ]
    ecs_script_ast_to_buf.restype = c_int
    break

# vendor/flecs/flecs.h: 15142
for _lib in _libs.values():
    if not _lib.has("ecs_script_ast_to_str", "cdecl"):
        continue
    ecs_script_ast_to_str = _lib.get("ecs_script_ast_to_str", "cdecl")
    ecs_script_ast_to_str.argtypes = [POINTER(ecs_script_t), c_bool]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_script_ast_to_str.restype = ReturnString
    else:
        ecs_script_ast_to_str.restype = String
        ecs_script_ast_to_str.errcheck = ReturnString
    break


# vendor/flecs/flecs.h: 15154
class struct_ecs_script_desc_t(Structure):
    pass


struct_ecs_script_desc_t.__slots__ = [
    "entity",
    "filename",
    "code",
]
struct_ecs_script_desc_t._fields_ = [
    ("entity", ecs_entity_t),
    ("filename", String),
    ("code", String),
]

ecs_script_desc_t = struct_ecs_script_desc_t  # vendor/flecs/flecs.h: 15154

# vendor/flecs/flecs.h: 15167
for _lib in _libs.values():
    if not _lib.has("ecs_script_init", "cdecl"):
        continue
    ecs_script_init = _lib.get("ecs_script_init", "cdecl")
    ecs_script_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_script_desc_t)]
    ecs_script_init.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 15182
for _lib in _libs.values():
    if not _lib.has("ecs_script_update", "cdecl"):
        continue
    ecs_script_update = _lib.get("ecs_script_update", "cdecl")
    ecs_script_update.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        ecs_entity_t,
        String,
    ]
    ecs_script_update.restype = c_int
    break

# vendor/flecs/flecs.h: 15195
for _lib in _libs.values():
    if not _lib.has("ecs_script_clear", "cdecl"):
        continue
    ecs_script_clear = _lib.get("ecs_script_clear", "cdecl")
    ecs_script_clear.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_entity_t]
    ecs_script_clear.restype = None
    break

# vendor/flecs/flecs.h: 15220
for _lib in _libs.values():
    if not _lib.has("ecs_script_vars_init", "cdecl"):
        continue
    ecs_script_vars_init = _lib.get("ecs_script_vars_init", "cdecl")
    ecs_script_vars_init.argtypes = [POINTER(ecs_world_t)]
    ecs_script_vars_init.restype = POINTER(ecs_script_vars_t)
    break

# vendor/flecs/flecs.h: 15230
for _lib in _libs.values():
    if not _lib.has("ecs_script_vars_fini", "cdecl"):
        continue
    ecs_script_vars_fini = _lib.get("ecs_script_vars_fini", "cdecl")
    ecs_script_vars_fini.argtypes = [POINTER(ecs_script_vars_t)]
    ecs_script_vars_fini.restype = None
    break

# vendor/flecs/flecs.h: 15245
for _lib in _libs.values():
    if not _lib.has("ecs_script_vars_push", "cdecl"):
        continue
    ecs_script_vars_push = _lib.get("ecs_script_vars_push", "cdecl")
    ecs_script_vars_push.argtypes = [POINTER(ecs_script_vars_t)]
    ecs_script_vars_push.restype = POINTER(ecs_script_vars_t)
    break

# vendor/flecs/flecs.h: 15257
for _lib in _libs.values():
    if not _lib.has("ecs_script_vars_pop", "cdecl"):
        continue
    ecs_script_vars_pop = _lib.get("ecs_script_vars_pop", "cdecl")
    ecs_script_vars_pop.argtypes = [POINTER(ecs_script_vars_t)]
    ecs_script_vars_pop.restype = POINTER(ecs_script_vars_t)
    break

# vendor/flecs/flecs.h: 15273
for _lib in _libs.values():
    if not _lib.has("ecs_script_vars_declare", "cdecl"):
        continue
    ecs_script_vars_declare = _lib.get("ecs_script_vars_declare", "cdecl")
    ecs_script_vars_declare.argtypes = [POINTER(ecs_script_vars_t), String]
    ecs_script_vars_declare.restype = POINTER(ecs_script_var_t)
    break

# vendor/flecs/flecs.h: 15293
for _lib in _libs.values():
    if not _lib.has("ecs_script_vars_define_id", "cdecl"):
        continue
    ecs_script_vars_define_id = _lib.get("ecs_script_vars_define_id", "cdecl")
    ecs_script_vars_define_id.argtypes = [
        POINTER(ecs_script_vars_t),
        String,
        ecs_entity_t,
    ]
    ecs_script_vars_define_id.restype = POINTER(ecs_script_var_t)
    break

# vendor/flecs/flecs.h: 15311
for _lib in _libs.values():
    if not _lib.has("ecs_script_vars_lookup", "cdecl"):
        continue
    ecs_script_vars_lookup = _lib.get("ecs_script_vars_lookup", "cdecl")
    ecs_script_vars_lookup.argtypes = [POINTER(ecs_script_vars_t), String]
    ecs_script_vars_lookup.restype = POINTER(ecs_script_var_t)
    break

# vendor/flecs/flecs.h: 15328
for _lib in _libs.values():
    if not _lib.has("ecs_script_vars_from_sp", "cdecl"):
        continue
    ecs_script_vars_from_sp = _lib.get("ecs_script_vars_from_sp", "cdecl")
    ecs_script_vars_from_sp.argtypes = [POINTER(ecs_script_vars_t), c_int32]
    ecs_script_vars_from_sp.restype = POINTER(ecs_script_var_t)
    break

# vendor/flecs/flecs.h: 15338
for _lib in _libs.values():
    if not _lib.has("ecs_script_vars_print", "cdecl"):
        continue
    ecs_script_vars_print = _lib.get("ecs_script_vars_print", "cdecl")
    ecs_script_vars_print.argtypes = [POINTER(ecs_script_vars_t)]
    ecs_script_vars_print.restype = None
    break

# vendor/flecs/flecs.h: 15350
for _lib in _libs.values():
    if not _lib.has("ecs_script_vars_set_size", "cdecl"):
        continue
    ecs_script_vars_set_size = _lib.get("ecs_script_vars_set_size", "cdecl")
    ecs_script_vars_set_size.argtypes = [POINTER(ecs_script_vars_t), c_int32]
    ecs_script_vars_set_size.restype = None
    break

# vendor/flecs/flecs.h: 15387
for _lib in _libs.values():
    if not _lib.has("ecs_script_vars_from_iter", "cdecl"):
        continue
    ecs_script_vars_from_iter = _lib.get("ecs_script_vars_from_iter", "cdecl")
    ecs_script_vars_from_iter.argtypes = [
        POINTER(ecs_iter_t),
        POINTER(ecs_script_vars_t),
        c_int,
    ]
    ecs_script_vars_from_iter.restype = None
    break


# vendor/flecs/flecs.h: 15420
class struct_ecs_expr_eval_desc_t(Structure):
    pass


struct_ecs_expr_eval_desc_t.__slots__ = [
    "name",
    "expr",
    "vars",
    "type",
    "lookup_action",
    "lookup_ctx",
    "disable_folding",
    "disable_dynamic_variable_binding",
    "allow_unresolved_identifiers",
    "runtime",
]
struct_ecs_expr_eval_desc_t._fields_ = [
    ("name", String),
    ("expr", String),
    ("vars", POINTER(ecs_script_vars_t)),
    ("type", ecs_entity_t),
    (
        "lookup_action",
        CFUNCTYPE(UNCHECKED(ecs_entity_t), POINTER(ecs_world_t), String, POINTER(None)),
    ),
    ("lookup_ctx", POINTER(None)),
    ("disable_folding", c_bool),
    ("disable_dynamic_variable_binding", c_bool),
    ("allow_unresolved_identifiers", c_bool),
    ("runtime", POINTER(ecs_script_runtime_t)),
]

ecs_expr_eval_desc_t = struct_ecs_expr_eval_desc_t  # vendor/flecs/flecs.h: 15420

# vendor/flecs/flecs.h: 15437
for _lib in _libs.values():
    if not _lib.has("ecs_expr_run", "cdecl"):
        continue
    ecs_expr_run = _lib.get("ecs_expr_run", "cdecl")
    ecs_expr_run.argtypes = [
        POINTER(ecs_world_t),
        String,
        POINTER(ecs_value_t),
        POINTER(ecs_expr_eval_desc_t),
    ]
    ecs_expr_run.restype = c_char_p
    break

# vendor/flecs/flecs.h: 15453
for _lib in _libs.values():
    if not _lib.has("ecs_expr_parse", "cdecl"):
        continue
    ecs_expr_parse = _lib.get("ecs_expr_parse", "cdecl")
    ecs_expr_parse.argtypes = [
        POINTER(ecs_world_t),
        String,
        POINTER(ecs_expr_eval_desc_t),
    ]
    ecs_expr_parse.restype = POINTER(ecs_script_t)
    break

# vendor/flecs/flecs.h: 15473
for _lib in _libs.values():
    if not _lib.has("ecs_expr_eval", "cdecl"):
        continue
    ecs_expr_eval = _lib.get("ecs_expr_eval", "cdecl")
    ecs_expr_eval.argtypes = [
        POINTER(ecs_script_t),
        POINTER(ecs_value_t),
        POINTER(ecs_expr_eval_desc_t),
    ]
    ecs_expr_eval.restype = c_int
    break

# vendor/flecs/flecs.h: 15491
for _lib in _libs.values():
    if not _lib.has("ecs_script_string_interpolate", "cdecl"):
        continue
    ecs_script_string_interpolate = _lib.get("ecs_script_string_interpolate", "cdecl")
    ecs_script_string_interpolate.argtypes = [
        POINTER(ecs_world_t),
        String,
        POINTER(ecs_script_vars_t),
    ]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_script_string_interpolate.restype = ReturnString
    else:
        ecs_script_string_interpolate.restype = String
        ecs_script_string_interpolate.errcheck = ReturnString
    break


# vendor/flecs/flecs.h: 15513
class struct_ecs_const_var_desc_t(Structure):
    pass


struct_ecs_const_var_desc_t.__slots__ = [
    "name",
    "parent",
    "type",
    "value",
]
struct_ecs_const_var_desc_t._fields_ = [
    ("name", String),
    ("parent", ecs_entity_t),
    ("type", ecs_entity_t),
    ("value", POINTER(None)),
]

ecs_const_var_desc_t = struct_ecs_const_var_desc_t  # vendor/flecs/flecs.h: 15513

# vendor/flecs/flecs.h: 15522
for _lib in _libs.values():
    if not _lib.has("ecs_const_var_init", "cdecl"):
        continue
    ecs_const_var_init = _lib.get("ecs_const_var_init", "cdecl")
    ecs_const_var_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_const_var_desc_t)]
    ecs_const_var_init.restype = ecs_entity_t
    break


# vendor/flecs/flecs.h: 15551
class struct_ecs_function_desc_t(Structure):
    pass


struct_ecs_function_desc_t.__slots__ = [
    "name",
    "parent",
    "params",
    "return_type",
    "callback",
    "ctx",
]
struct_ecs_function_desc_t._fields_ = [
    ("name", String),
    ("parent", ecs_entity_t),
    ("params", ecs_script_parameter_t * int(16)),
    ("return_type", ecs_entity_t),
    ("callback", ecs_function_callback_t),
    ("ctx", POINTER(None)),
]

ecs_function_desc_t = struct_ecs_function_desc_t  # vendor/flecs/flecs.h: 15551

# vendor/flecs/flecs.h: 15561
for _lib in _libs.values():
    if not _lib.has("ecs_function_init", "cdecl"):
        continue
    ecs_function_init = _lib.get("ecs_function_init", "cdecl")
    ecs_function_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_function_desc_t)]
    ecs_function_init.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 15581
for _lib in _libs.values():
    if not _lib.has("ecs_method_init", "cdecl"):
        continue
    ecs_method_init = _lib.get("ecs_method_init", "cdecl")
    ecs_method_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_function_desc_t)]
    ecs_method_init.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 15601
for _lib in _libs.values():
    if not _lib.has("ecs_ptr_to_expr", "cdecl"):
        continue
    ecs_ptr_to_expr = _lib.get("ecs_ptr_to_expr", "cdecl")
    ecs_ptr_to_expr.argtypes = [POINTER(ecs_world_t), ecs_entity_t, POINTER(None)]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_ptr_to_expr.restype = ReturnString
    else:
        ecs_ptr_to_expr.restype = String
        ecs_ptr_to_expr.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 15616
for _lib in _libs.values():
    if not _lib.has("ecs_ptr_to_expr_buf", "cdecl"):
        continue
    ecs_ptr_to_expr_buf = _lib.get("ecs_ptr_to_expr_buf", "cdecl")
    ecs_ptr_to_expr_buf.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        POINTER(None),
        POINTER(ecs_strbuf_t),
    ]
    ecs_ptr_to_expr_buf.restype = c_int
    break

# vendor/flecs/flecs.h: 15634
for _lib in _libs.values():
    if not _lib.has("ecs_ptr_to_str", "cdecl"):
        continue
    ecs_ptr_to_str = _lib.get("ecs_ptr_to_str", "cdecl")
    ecs_ptr_to_str.argtypes = [POINTER(ecs_world_t), ecs_entity_t, POINTER(None)]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_ptr_to_str.restype = ReturnString
    else:
        ecs_ptr_to_str.restype = String
        ecs_ptr_to_str.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 15649
for _lib in _libs.values():
    if not _lib.has("ecs_ptr_to_str_buf", "cdecl"):
        continue
    ecs_ptr_to_str_buf = _lib.get("ecs_ptr_to_str_buf", "cdecl")
    ecs_ptr_to_str_buf.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        POINTER(None),
        POINTER(ecs_strbuf_t),
    ]
    ecs_ptr_to_str_buf.restype = c_int
    break


# vendor/flecs/flecs.h: 15655
class struct_ecs_expr_node_t(Structure):
    pass


ecs_expr_node_t = struct_ecs_expr_node_t  # vendor/flecs/flecs.h: 15655

# vendor/flecs/flecs.h: 15666
for _lib in _libs.values():
    if not _lib.has("FlecsScriptImport", "cdecl"):
        continue
    FlecsScriptImport = _lib.get("FlecsScriptImport", "cdecl")
    FlecsScriptImport.argtypes = [POINTER(ecs_world_t)]
    FlecsScriptImport.restype = None
    break

# vendor/flecs/flecs.h: 15716
for _lib in _libs.values():
    try:
        FLECS_IDEcsDocDescriptionID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsDocDescriptionID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 15721
for _lib in _libs.values():
    try:
        EcsDocUuid = (ecs_entity_t).in_dll(_lib, "EcsDocUuid")
        break
    except:
        pass

# vendor/flecs/flecs.h: 15726
for _lib in _libs.values():
    try:
        EcsDocBrief = (ecs_entity_t).in_dll(_lib, "EcsDocBrief")
        break
    except:
        pass

# vendor/flecs/flecs.h: 15731
for _lib in _libs.values():
    try:
        EcsDocDetail = (ecs_entity_t).in_dll(_lib, "EcsDocDetail")
        break
    except:
        pass

# vendor/flecs/flecs.h: 15736
for _lib in _libs.values():
    try:
        EcsDocLink = (ecs_entity_t).in_dll(_lib, "EcsDocLink")
        break
    except:
        pass

# vendor/flecs/flecs.h: 15741
for _lib in _libs.values():
    try:
        EcsDocColor = (ecs_entity_t).in_dll(_lib, "EcsDocColor")
        break
    except:
        pass


# vendor/flecs/flecs.h: 15753
class struct_EcsDocDescription(Structure):
    pass


struct_EcsDocDescription.__slots__ = [
    "value",
]
struct_EcsDocDescription._fields_ = [
    ("value", String),
]

EcsDocDescription = struct_EcsDocDescription  # vendor/flecs/flecs.h: 15753

# vendor/flecs/flecs.h: 15767
for _lib in _libs.values():
    if not _lib.has("ecs_doc_set_uuid", "cdecl"):
        continue
    ecs_doc_set_uuid = _lib.get("ecs_doc_set_uuid", "cdecl")
    ecs_doc_set_uuid.argtypes = [POINTER(ecs_world_t), ecs_entity_t, String]
    ecs_doc_set_uuid.restype = None
    break

# vendor/flecs/flecs.h: 15785
for _lib in _libs.values():
    if not _lib.has("ecs_doc_set_name", "cdecl"):
        continue
    ecs_doc_set_name = _lib.get("ecs_doc_set_name", "cdecl")
    ecs_doc_set_name.argtypes = [POINTER(ecs_world_t), ecs_entity_t, String]
    ecs_doc_set_name.restype = None
    break

# vendor/flecs/flecs.h: 15801
for _lib in _libs.values():
    if not _lib.has("ecs_doc_set_brief", "cdecl"):
        continue
    ecs_doc_set_brief = _lib.get("ecs_doc_set_brief", "cdecl")
    ecs_doc_set_brief.argtypes = [POINTER(ecs_world_t), ecs_entity_t, String]
    ecs_doc_set_brief.restype = None
    break

# vendor/flecs/flecs.h: 15817
for _lib in _libs.values():
    if not _lib.has("ecs_doc_set_detail", "cdecl"):
        continue
    ecs_doc_set_detail = _lib.get("ecs_doc_set_detail", "cdecl")
    ecs_doc_set_detail.argtypes = [POINTER(ecs_world_t), ecs_entity_t, String]
    ecs_doc_set_detail.restype = None
    break

# vendor/flecs/flecs.h: 15833
for _lib in _libs.values():
    if not _lib.has("ecs_doc_set_link", "cdecl"):
        continue
    ecs_doc_set_link = _lib.get("ecs_doc_set_link", "cdecl")
    ecs_doc_set_link.argtypes = [POINTER(ecs_world_t), ecs_entity_t, String]
    ecs_doc_set_link.restype = None
    break

# vendor/flecs/flecs.h: 15850
for _lib in _libs.values():
    if not _lib.has("ecs_doc_set_color", "cdecl"):
        continue
    ecs_doc_set_color = _lib.get("ecs_doc_set_color", "cdecl")
    ecs_doc_set_color.argtypes = [POINTER(ecs_world_t), ecs_entity_t, String]
    ecs_doc_set_color.restype = None
    break

# vendor/flecs/flecs.h: 15865
for _lib in _libs.values():
    if not _lib.has("ecs_doc_get_uuid", "cdecl"):
        continue
    ecs_doc_get_uuid = _lib.get("ecs_doc_get_uuid", "cdecl")
    ecs_doc_get_uuid.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_doc_get_uuid.restype = c_char_p
    break

# vendor/flecs/flecs.h: 15894
for _lib in _libs.values():
    if not _lib.has("ecs_doc_get_name", "cdecl"):
        continue
    ecs_doc_get_name = _lib.get("ecs_doc_get_name", "cdecl")
    ecs_doc_get_name.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_doc_get_name.restype = c_char_p
    break

# vendor/flecs/flecs.h: 15909
for _lib in _libs.values():
    if not _lib.has("ecs_doc_get_brief", "cdecl"):
        continue
    ecs_doc_get_brief = _lib.get("ecs_doc_get_brief", "cdecl")
    ecs_doc_get_brief.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_doc_get_brief.restype = c_char_p
    break

# vendor/flecs/flecs.h: 15924
for _lib in _libs.values():
    if not _lib.has("ecs_doc_get_detail", "cdecl"):
        continue
    ecs_doc_get_detail = _lib.get("ecs_doc_get_detail", "cdecl")
    ecs_doc_get_detail.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_doc_get_detail.restype = c_char_p
    break

# vendor/flecs/flecs.h: 15939
for _lib in _libs.values():
    if not _lib.has("ecs_doc_get_link", "cdecl"):
        continue
    ecs_doc_get_link = _lib.get("ecs_doc_get_link", "cdecl")
    ecs_doc_get_link.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_doc_get_link.restype = c_char_p
    break

# vendor/flecs/flecs.h: 15954
for _lib in _libs.values():
    if not _lib.has("ecs_doc_get_color", "cdecl"):
        continue
    ecs_doc_get_color = _lib.get("ecs_doc_get_color", "cdecl")
    ecs_doc_get_color.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_doc_get_color.restype = c_char_p
    break

# vendor/flecs/flecs.h: 15967
for _lib in _libs.values():
    if not _lib.has("FlecsDocImport", "cdecl"):
        continue
    FlecsDocImport = _lib.get("FlecsDocImport", "cdecl")
    FlecsDocImport.argtypes = [POINTER(ecs_world_t)]
    FlecsDocImport.restype = None
    break

ecs_bool_t = c_bool  # vendor/flecs/flecs.h: 16080

ecs_char_t = c_char  # vendor/flecs/flecs.h: 16081

ecs_byte_t = c_ubyte  # vendor/flecs/flecs.h: 16082

ecs_u8_t = uint8_t  # vendor/flecs/flecs.h: 16083

ecs_u16_t = uint16_t  # vendor/flecs/flecs.h: 16084

ecs_u32_t = uint32_t  # vendor/flecs/flecs.h: 16085

ecs_u64_t = uint64_t  # vendor/flecs/flecs.h: 16086

ecs_uptr_t = uintptr_t  # vendor/flecs/flecs.h: 16087

ecs_i8_t = c_int8  # vendor/flecs/flecs.h: 16088

ecs_i16_t = c_int16  # vendor/flecs/flecs.h: 16089

ecs_i32_t = c_int32  # vendor/flecs/flecs.h: 16090

ecs_i64_t = c_int64  # vendor/flecs/flecs.h: 16091

ecs_iptr_t = intptr_t  # vendor/flecs/flecs.h: 16092

ecs_f32_t = c_float  # vendor/flecs/flecs.h: 16093

ecs_f64_t = c_double  # vendor/flecs/flecs.h: 16094

ecs_string_t = String  # vendor/flecs/flecs.h: 16095

# vendor/flecs/flecs.h: 16098
for _lib in _libs.values():
    try:
        FLECS_IDEcsTypeID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsTypeID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16099
for _lib in _libs.values():
    try:
        FLECS_IDEcsTypeSerializerID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsTypeSerializerID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 16100
for _lib in _libs.values():
    try:
        FLECS_IDEcsPrimitiveID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsPrimitiveID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16101
for _lib in _libs.values():
    try:
        FLECS_IDEcsEnumID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsEnumID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16102
for _lib in _libs.values():
    try:
        FLECS_IDEcsBitmaskID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsBitmaskID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16103
for _lib in _libs.values():
    try:
        FLECS_IDEcsMemberID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsMemberID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16104
for _lib in _libs.values():
    try:
        FLECS_IDEcsMemberRangesID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsMemberRangesID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 16105
for _lib in _libs.values():
    try:
        FLECS_IDEcsStructID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsStructID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16106
for _lib in _libs.values():
    try:
        FLECS_IDEcsArrayID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsArrayID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16107
for _lib in _libs.values():
    try:
        FLECS_IDEcsVectorID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsVectorID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16108
for _lib in _libs.values():
    try:
        FLECS_IDEcsOpaqueID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsOpaqueID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16109
for _lib in _libs.values():
    try:
        FLECS_IDEcsUnitID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDEcsUnitID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16110
for _lib in _libs.values():
    try:
        FLECS_IDEcsUnitPrefixID_ = (ecs_entity_t).in_dll(
            _lib, "FLECS_IDEcsUnitPrefixID_"
        )
        break
    except:
        pass

# vendor/flecs/flecs.h: 16111
for _lib in _libs.values():
    try:
        EcsQuantity = (ecs_entity_t).in_dll(_lib, "EcsQuantity")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16115
for _lib in _libs.values():
    try:
        FLECS_IDecs_bool_tID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDecs_bool_tID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16116
for _lib in _libs.values():
    try:
        FLECS_IDecs_char_tID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDecs_char_tID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16117
for _lib in _libs.values():
    try:
        FLECS_IDecs_byte_tID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDecs_byte_tID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16118
for _lib in _libs.values():
    try:
        FLECS_IDecs_u8_tID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDecs_u8_tID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16119
for _lib in _libs.values():
    try:
        FLECS_IDecs_u16_tID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDecs_u16_tID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16120
for _lib in _libs.values():
    try:
        FLECS_IDecs_u32_tID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDecs_u32_tID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16121
for _lib in _libs.values():
    try:
        FLECS_IDecs_u64_tID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDecs_u64_tID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16122
for _lib in _libs.values():
    try:
        FLECS_IDecs_uptr_tID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDecs_uptr_tID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16123
for _lib in _libs.values():
    try:
        FLECS_IDecs_i8_tID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDecs_i8_tID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16124
for _lib in _libs.values():
    try:
        FLECS_IDecs_i16_tID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDecs_i16_tID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16125
for _lib in _libs.values():
    try:
        FLECS_IDecs_i32_tID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDecs_i32_tID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16126
for _lib in _libs.values():
    try:
        FLECS_IDecs_i64_tID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDecs_i64_tID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16127
for _lib in _libs.values():
    try:
        FLECS_IDecs_iptr_tID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDecs_iptr_tID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16128
for _lib in _libs.values():
    try:
        FLECS_IDecs_f32_tID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDecs_f32_tID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16129
for _lib in _libs.values():
    try:
        FLECS_IDecs_f64_tID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDecs_f64_tID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16130
for _lib in _libs.values():
    try:
        FLECS_IDecs_string_tID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDecs_string_tID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16131
for _lib in _libs.values():
    try:
        FLECS_IDecs_entity_tID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDecs_entity_tID_")
        break
    except:
        pass

# vendor/flecs/flecs.h: 16132
for _lib in _libs.values():
    try:
        FLECS_IDecs_id_tID_ = (ecs_entity_t).in_dll(_lib, "FLECS_IDecs_id_tID_")
        break
    except:
        pass

enum_ecs_type_kind_t = c_int  # vendor/flecs/flecs.h: 16144

EcsPrimitiveType = 0  # vendor/flecs/flecs.h: 16144

EcsBitmaskType = EcsPrimitiveType + 1  # vendor/flecs/flecs.h: 16144

EcsEnumType = EcsBitmaskType + 1  # vendor/flecs/flecs.h: 16144

EcsStructType = EcsEnumType + 1  # vendor/flecs/flecs.h: 16144

EcsArrayType = EcsStructType + 1  # vendor/flecs/flecs.h: 16144

EcsVectorType = EcsArrayType + 1  # vendor/flecs/flecs.h: 16144

EcsOpaqueType = EcsVectorType + 1  # vendor/flecs/flecs.h: 16144

EcsTypeKindLast = EcsOpaqueType  # vendor/flecs/flecs.h: 16144

ecs_type_kind_t = enum_ecs_type_kind_t  # vendor/flecs/flecs.h: 16144


# vendor/flecs/flecs.h: 16151
class struct_EcsType(Structure):
    pass


struct_EcsType.__slots__ = [
    "kind",
    "existing",
    "partial",
]
struct_EcsType._fields_ = [
    ("kind", ecs_type_kind_t),
    ("existing", c_bool),
    ("partial", c_bool),
]

EcsType = struct_EcsType  # vendor/flecs/flecs.h: 16151

enum_ecs_primitive_kind_t = c_int  # vendor/flecs/flecs.h: 16174

EcsBool = 1  # vendor/flecs/flecs.h: 16174

EcsChar = EcsBool + 1  # vendor/flecs/flecs.h: 16174

EcsByte = EcsChar + 1  # vendor/flecs/flecs.h: 16174

EcsU8 = EcsByte + 1  # vendor/flecs/flecs.h: 16174

EcsU16 = EcsU8 + 1  # vendor/flecs/flecs.h: 16174

EcsU32 = EcsU16 + 1  # vendor/flecs/flecs.h: 16174

EcsU64 = EcsU32 + 1  # vendor/flecs/flecs.h: 16174

EcsI8 = EcsU64 + 1  # vendor/flecs/flecs.h: 16174

EcsI16 = EcsI8 + 1  # vendor/flecs/flecs.h: 16174

EcsI32 = EcsI16 + 1  # vendor/flecs/flecs.h: 16174

EcsI64 = EcsI32 + 1  # vendor/flecs/flecs.h: 16174

EcsF32 = EcsI64 + 1  # vendor/flecs/flecs.h: 16174

EcsF64 = EcsF32 + 1  # vendor/flecs/flecs.h: 16174

EcsUPtr = EcsF64 + 1  # vendor/flecs/flecs.h: 16174

EcsIPtr = EcsUPtr + 1  # vendor/flecs/flecs.h: 16174

EcsString = EcsIPtr + 1  # vendor/flecs/flecs.h: 16174

EcsEntity = EcsString + 1  # vendor/flecs/flecs.h: 16174

EcsId = EcsEntity + 1  # vendor/flecs/flecs.h: 16174

EcsPrimitiveKindLast = EcsId  # vendor/flecs/flecs.h: 16174

ecs_primitive_kind_t = enum_ecs_primitive_kind_t  # vendor/flecs/flecs.h: 16174


# vendor/flecs/flecs.h: 16179
class struct_EcsPrimitive(Structure):
    pass


struct_EcsPrimitive.__slots__ = [
    "kind",
]
struct_EcsPrimitive._fields_ = [
    ("kind", ecs_primitive_kind_t),
]

EcsPrimitive = struct_EcsPrimitive  # vendor/flecs/flecs.h: 16179


# vendor/flecs/flecs.h: 16188
class struct_EcsMember(Structure):
    pass


struct_EcsMember.__slots__ = [
    "type",
    "count",
    "unit",
    "offset",
    "use_offset",
]
struct_EcsMember._fields_ = [
    ("type", ecs_entity_t),
    ("count", c_int32),
    ("unit", ecs_entity_t),
    ("offset", c_int32),
    ("use_offset", c_bool),
]

EcsMember = struct_EcsMember  # vendor/flecs/flecs.h: 16188


# vendor/flecs/flecs.h: 16194
class struct_ecs_member_value_range_t(Structure):
    pass


struct_ecs_member_value_range_t.__slots__ = [
    "min",
    "max",
]
struct_ecs_member_value_range_t._fields_ = [
    ("min", c_double),
    ("max", c_double),
]

ecs_member_value_range_t = (
    struct_ecs_member_value_range_t  # vendor/flecs/flecs.h: 16194
)


# vendor/flecs/flecs.h: 16201
class struct_EcsMemberRanges(Structure):
    pass


struct_EcsMemberRanges.__slots__ = [
    "value",
    "warning",
    "error",
]
struct_EcsMemberRanges._fields_ = [
    ("value", ecs_member_value_range_t),
    ("warning", ecs_member_value_range_t),
    ("error", ecs_member_value_range_t),
]

EcsMemberRanges = struct_EcsMemberRanges  # vendor/flecs/flecs.h: 16201


# vendor/flecs/flecs.h: 16244
class struct_ecs_member_t(Structure):
    pass


struct_ecs_member_t.__slots__ = [
    "name",
    "type",
    "count",
    "offset",
    "unit",
    "use_offset",
    "range",
    "error_range",
    "warning_range",
    "size",
    "member",
]
struct_ecs_member_t._fields_ = [
    ("name", String),
    ("type", ecs_entity_t),
    ("count", c_int32),
    ("offset", c_int32),
    ("unit", ecs_entity_t),
    ("use_offset", c_bool),
    ("range", ecs_member_value_range_t),
    ("error_range", ecs_member_value_range_t),
    ("warning_range", ecs_member_value_range_t),
    ("size", ecs_size_t),
    ("member", ecs_entity_t),
]

ecs_member_t = struct_ecs_member_t  # vendor/flecs/flecs.h: 16244


# vendor/flecs/flecs.h: 16250
class struct_EcsStruct(Structure):
    pass


struct_EcsStruct.__slots__ = [
    "members",
]
struct_EcsStruct._fields_ = [
    ("members", ecs_vec_t),
]

EcsStruct = struct_EcsStruct  # vendor/flecs/flecs.h: 16250


# vendor/flecs/flecs.h: 16265
class struct_ecs_enum_constant_t(Structure):
    pass


struct_ecs_enum_constant_t.__slots__ = [
    "name",
    "value",
    "value_unsigned",
    "constant",
]
struct_ecs_enum_constant_t._fields_ = [
    ("name", String),
    ("value", c_int64),
    ("value_unsigned", uint64_t),
    ("constant", ecs_entity_t),
]

ecs_enum_constant_t = struct_ecs_enum_constant_t  # vendor/flecs/flecs.h: 16265


# vendor/flecs/flecs.h: 16276
class struct_EcsEnum(Structure):
    pass


struct_EcsEnum.__slots__ = [
    "underlying_type",
    "constants",
    "ordered_constants",
]
struct_EcsEnum._fields_ = [
    ("underlying_type", ecs_entity_t),
    ("constants", ecs_map_t),
    ("ordered_constants", ecs_vec_t),
]

EcsEnum = struct_EcsEnum  # vendor/flecs/flecs.h: 16276


# vendor/flecs/flecs.h: 16291
class struct_ecs_bitmask_constant_t(Structure):
    pass


struct_ecs_bitmask_constant_t.__slots__ = [
    "name",
    "value",
    "_unused",
    "constant",
]
struct_ecs_bitmask_constant_t._fields_ = [
    ("name", String),
    ("value", ecs_flags64_t),
    ("_unused", c_int64),
    ("constant", ecs_entity_t),
]

ecs_bitmask_constant_t = struct_ecs_bitmask_constant_t  # vendor/flecs/flecs.h: 16291


# vendor/flecs/flecs.h: 16299
class struct_EcsBitmask(Structure):
    pass


struct_EcsBitmask.__slots__ = [
    "constants",
    "ordered_constants",
]
struct_EcsBitmask._fields_ = [
    ("constants", ecs_map_t),
    ("ordered_constants", ecs_vec_t),
]

EcsBitmask = struct_EcsBitmask  # vendor/flecs/flecs.h: 16299


# vendor/flecs/flecs.h: 16305
class struct_EcsArray(Structure):
    pass


struct_EcsArray.__slots__ = [
    "type",
    "count",
]
struct_EcsArray._fields_ = [
    ("type", ecs_entity_t),
    ("count", c_int32),
]

EcsArray = struct_EcsArray  # vendor/flecs/flecs.h: 16305


# vendor/flecs/flecs.h: 16310
class struct_EcsVector(Structure):
    pass


struct_EcsVector.__slots__ = [
    "type",
]
struct_EcsVector._fields_ = [
    ("type", ecs_entity_t),
]

EcsVector = struct_EcsVector  # vendor/flecs/flecs.h: 16310


# vendor/flecs/flecs.h: 16318
class struct_ecs_serializer_t(Structure):
    pass


struct_ecs_serializer_t.__slots__ = [
    "value",
    "member",
    "world",
    "ctx",
]
struct_ecs_serializer_t._fields_ = [
    (
        "value",
        CFUNCTYPE(
            UNCHECKED(c_int),
            POINTER(struct_ecs_serializer_t),
            ecs_entity_t,
            POINTER(None),
        ),
    ),
    ("member", CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_ecs_serializer_t), String)),
    ("world", POINTER(ecs_world_t)),
    ("ctx", POINTER(None)),
]

ecs_serializer_t = struct_ecs_serializer_t  # vendor/flecs/flecs.h: 16332

ecs_meta_serialize_t = CFUNCTYPE(
    UNCHECKED(c_int), POINTER(ecs_serializer_t), POINTER(None)
)  # vendor/flecs/flecs.h: 16369

ecs_meta_serialize_member_t = CFUNCTYPE(
    UNCHECKED(c_int), POINTER(ecs_serializer_t), POINTER(None), String
)  # vendor/flecs/flecs.h: 16375

ecs_meta_serialize_element_t = CFUNCTYPE(
    UNCHECKED(c_int), POINTER(ecs_serializer_t), POINTER(None), c_size_t
)  # vendor/flecs/flecs.h: 16381


# vendor/flecs/flecs.h: 16470
class struct_EcsOpaque(Structure):
    pass


struct_EcsOpaque.__slots__ = [
    "as_type",
    "serialize",
    "serialize_member",
    "serialize_element",
    "assign_bool",
    "assign_char",
    "assign_int",
    "assign_uint",
    "assign_float",
    "assign_string",
    "assign_entity",
    "assign_id",
    "assign_null",
    "clear",
    "ensure_element",
    "ensure_member",
    "count",
    "resize",
]
struct_EcsOpaque._fields_ = [
    ("as_type", ecs_entity_t),
    ("serialize", ecs_meta_serialize_t),
    ("serialize_member", ecs_meta_serialize_member_t),
    ("serialize_element", ecs_meta_serialize_element_t),
    ("assign_bool", CFUNCTYPE(UNCHECKED(None), POINTER(None), c_bool)),
    ("assign_char", CFUNCTYPE(UNCHECKED(None), POINTER(None), c_char)),
    ("assign_int", CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int64)),
    ("assign_uint", CFUNCTYPE(UNCHECKED(None), POINTER(None), uint64_t)),
    ("assign_float", CFUNCTYPE(UNCHECKED(None), POINTER(None), c_double)),
    ("assign_string", CFUNCTYPE(UNCHECKED(None), POINTER(None), String)),
    (
        "assign_entity",
        CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(ecs_world_t), ecs_entity_t),
    ),
    (
        "assign_id",
        CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(ecs_world_t), ecs_id_t),
    ),
    ("assign_null", CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ("clear", CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ("ensure_element", CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(None), c_size_t)),
    ("ensure_member", CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(None), String)),
    ("count", CFUNCTYPE(UNCHECKED(c_size_t), POINTER(None))),
    ("resize", CFUNCTYPE(UNCHECKED(None), POINTER(None), c_size_t)),
]

EcsOpaque = struct_EcsOpaque  # vendor/flecs/flecs.h: 16470


# vendor/flecs/flecs.h: 16485
class struct_ecs_unit_translation_t(Structure):
    pass


struct_ecs_unit_translation_t.__slots__ = [
    "factor",
    "power",
]
struct_ecs_unit_translation_t._fields_ = [
    ("factor", c_int32),
    ("power", c_int32),
]

ecs_unit_translation_t = struct_ecs_unit_translation_t  # vendor/flecs/flecs.h: 16485


# vendor/flecs/flecs.h: 16494
class struct_EcsUnit(Structure):
    pass


struct_EcsUnit.__slots__ = [
    "symbol",
    "prefix",
    "base",
    "over",
    "translation",
]
struct_EcsUnit._fields_ = [
    ("symbol", String),
    ("prefix", ecs_entity_t),
    ("base", ecs_entity_t),
    ("over", ecs_entity_t),
    ("translation", ecs_unit_translation_t),
]

EcsUnit = struct_EcsUnit  # vendor/flecs/flecs.h: 16494


# vendor/flecs/flecs.h: 16500
class struct_EcsUnitPrefix(Structure):
    pass


struct_EcsUnitPrefix.__slots__ = [
    "symbol",
    "translation",
]
struct_EcsUnitPrefix._fields_ = [
    ("symbol", String),
    ("translation", ecs_unit_translation_t),
]

EcsUnitPrefix = struct_EcsUnitPrefix  # vendor/flecs/flecs.h: 16500

enum_ecs_meta_type_op_kind_t = c_int  # vendor/flecs/flecs.h: 16543

EcsOpArray = 0  # vendor/flecs/flecs.h: 16543

EcsOpVector = EcsOpArray + 1  # vendor/flecs/flecs.h: 16543

EcsOpOpaque = EcsOpVector + 1  # vendor/flecs/flecs.h: 16543

EcsOpPush = EcsOpOpaque + 1  # vendor/flecs/flecs.h: 16543

EcsOpPop = EcsOpPush + 1  # vendor/flecs/flecs.h: 16543

EcsOpScope = EcsOpPop + 1  # vendor/flecs/flecs.h: 16543

EcsOpEnum = EcsOpScope + 1  # vendor/flecs/flecs.h: 16543

EcsOpBitmask = EcsOpEnum + 1  # vendor/flecs/flecs.h: 16543

EcsOpPrimitive = EcsOpBitmask + 1  # vendor/flecs/flecs.h: 16543

EcsOpBool = EcsOpPrimitive + 1  # vendor/flecs/flecs.h: 16543

EcsOpChar = EcsOpBool + 1  # vendor/flecs/flecs.h: 16543

EcsOpByte = EcsOpChar + 1  # vendor/flecs/flecs.h: 16543

EcsOpU8 = EcsOpByte + 1  # vendor/flecs/flecs.h: 16543

EcsOpU16 = EcsOpU8 + 1  # vendor/flecs/flecs.h: 16543

EcsOpU32 = EcsOpU16 + 1  # vendor/flecs/flecs.h: 16543

EcsOpU64 = EcsOpU32 + 1  # vendor/flecs/flecs.h: 16543

EcsOpI8 = EcsOpU64 + 1  # vendor/flecs/flecs.h: 16543

EcsOpI16 = EcsOpI8 + 1  # vendor/flecs/flecs.h: 16543

EcsOpI32 = EcsOpI16 + 1  # vendor/flecs/flecs.h: 16543

EcsOpI64 = EcsOpI32 + 1  # vendor/flecs/flecs.h: 16543

EcsOpF32 = EcsOpI64 + 1  # vendor/flecs/flecs.h: 16543

EcsOpF64 = EcsOpF32 + 1  # vendor/flecs/flecs.h: 16543

EcsOpUPtr = EcsOpF64 + 1  # vendor/flecs/flecs.h: 16543

EcsOpIPtr = EcsOpUPtr + 1  # vendor/flecs/flecs.h: 16543

EcsOpString = EcsOpIPtr + 1  # vendor/flecs/flecs.h: 16543

EcsOpEntity = EcsOpString + 1  # vendor/flecs/flecs.h: 16543

EcsOpId = EcsOpEntity + 1  # vendor/flecs/flecs.h: 16543

EcsMetaTypeOpKindLast = EcsOpId  # vendor/flecs/flecs.h: 16543

ecs_meta_type_op_kind_t = enum_ecs_meta_type_op_kind_t  # vendor/flecs/flecs.h: 16543


# vendor/flecs/flecs.h: 16556
class struct_ecs_meta_type_op_t(Structure):
    pass


struct_ecs_meta_type_op_t.__slots__ = [
    "kind",
    "offset",
    "count",
    "name",
    "op_count",
    "size",
    "type",
    "member_index",
    "members",
]
struct_ecs_meta_type_op_t._fields_ = [
    ("kind", ecs_meta_type_op_kind_t),
    ("offset", ecs_size_t),
    ("count", c_int32),
    ("name", String),
    ("op_count", c_int32),
    ("size", ecs_size_t),
    ("type", ecs_entity_t),
    ("member_index", c_int32),
    ("members", POINTER(ecs_hashmap_t)),
]

ecs_meta_type_op_t = struct_ecs_meta_type_op_t  # vendor/flecs/flecs.h: 16556


# vendor/flecs/flecs.h: 16563
class struct_EcsTypeSerializer(Structure):
    pass


struct_EcsTypeSerializer.__slots__ = [
    "ops",
]
struct_EcsTypeSerializer._fields_ = [
    ("ops", ecs_vec_t),
]

EcsTypeSerializer = struct_EcsTypeSerializer  # vendor/flecs/flecs.h: 16563


# vendor/flecs/flecs.h: 16589
class struct_ecs_meta_scope_t(Structure):
    pass


struct_ecs_meta_scope_t.__slots__ = [
    "type",
    "ops",
    "op_count",
    "op_cur",
    "elem_cur",
    "prev_depth",
    "ptr",
    "comp",
    "opaque",
    "vector",
    "members",
    "is_collection",
    "is_inline_array",
    "is_empty_scope",
]
struct_ecs_meta_scope_t._fields_ = [
    ("type", ecs_entity_t),
    ("ops", POINTER(ecs_meta_type_op_t)),
    ("op_count", c_int32),
    ("op_cur", c_int32),
    ("elem_cur", c_int32),
    ("prev_depth", c_int32),
    ("ptr", POINTER(None)),
    ("comp", POINTER(EcsComponent)),
    ("opaque", POINTER(EcsOpaque)),
    ("vector", POINTER(ecs_vec_t)),
    ("members", POINTER(ecs_hashmap_t)),
    ("is_collection", c_bool),
    ("is_inline_array", c_bool),
    ("is_empty_scope", c_bool),
]

ecs_meta_scope_t = struct_ecs_meta_scope_t  # vendor/flecs/flecs.h: 16589


# vendor/flecs/flecs.h: 16602
class struct_ecs_meta_cursor_t(Structure):
    pass


struct_ecs_meta_cursor_t.__slots__ = [
    "world",
    "scope",
    "depth",
    "valid",
    "is_primitive_scope",
    "lookup_action",
    "lookup_ctx",
]
struct_ecs_meta_cursor_t._fields_ = [
    ("world", POINTER(ecs_world_t)),
    ("scope", ecs_meta_scope_t * int(32)),
    ("depth", c_int32),
    ("valid", c_bool),
    ("is_primitive_scope", c_bool),
    (
        "lookup_action",
        CFUNCTYPE(UNCHECKED(ecs_entity_t), POINTER(ecs_world_t), String, POINTER(None)),
    ),
    ("lookup_ctx", POINTER(None)),
]

ecs_meta_cursor_t = struct_ecs_meta_cursor_t  # vendor/flecs/flecs.h: 16602

# vendor/flecs/flecs.h: 16619
for _lib in _libs.values():
    if not _lib.has("ecs_meta_cursor", "cdecl"):
        continue
    ecs_meta_cursor = _lib.get("ecs_meta_cursor", "cdecl")
    ecs_meta_cursor.argtypes = [POINTER(ecs_world_t), ecs_entity_t, POINTER(None)]
    ecs_meta_cursor.restype = ecs_meta_cursor_t
    break

# vendor/flecs/flecs.h: 16630
for _lib in _libs.values():
    if not _lib.has("ecs_meta_get_ptr", "cdecl"):
        continue
    ecs_meta_get_ptr = _lib.get("ecs_meta_get_ptr", "cdecl")
    ecs_meta_get_ptr.argtypes = [POINTER(ecs_meta_cursor_t)]
    ecs_meta_get_ptr.restype = POINTER(c_ubyte)
    ecs_meta_get_ptr.errcheck = lambda v, *a: cast(v, c_void_p)
    break

# vendor/flecs/flecs.h: 16639
for _lib in _libs.values():
    if not _lib.has("ecs_meta_next", "cdecl"):
        continue
    ecs_meta_next = _lib.get("ecs_meta_next", "cdecl")
    ecs_meta_next.argtypes = [POINTER(ecs_meta_cursor_t)]
    ecs_meta_next.restype = c_int
    break

# vendor/flecs/flecs.h: 16648
for _lib in _libs.values():
    if not _lib.has("ecs_meta_elem", "cdecl"):
        continue
    ecs_meta_elem = _lib.get("ecs_meta_elem", "cdecl")
    ecs_meta_elem.argtypes = [POINTER(ecs_meta_cursor_t), c_int32]
    ecs_meta_elem.restype = c_int
    break

# vendor/flecs/flecs.h: 16659
for _lib in _libs.values():
    if not _lib.has("ecs_meta_member", "cdecl"):
        continue
    ecs_meta_member = _lib.get("ecs_meta_member", "cdecl")
    ecs_meta_member.argtypes = [POINTER(ecs_meta_cursor_t), String]
    ecs_meta_member.restype = c_int
    break

# vendor/flecs/flecs.h: 16671
for _lib in _libs.values():
    if not _lib.has("ecs_meta_dotmember", "cdecl"):
        continue
    ecs_meta_dotmember = _lib.get("ecs_meta_dotmember", "cdecl")
    ecs_meta_dotmember.argtypes = [POINTER(ecs_meta_cursor_t), String]
    ecs_meta_dotmember.restype = c_int
    break

# vendor/flecs/flecs.h: 16681
for _lib in _libs.values():
    if not _lib.has("ecs_meta_push", "cdecl"):
        continue
    ecs_meta_push = _lib.get("ecs_meta_push", "cdecl")
    ecs_meta_push.argtypes = [POINTER(ecs_meta_cursor_t)]
    ecs_meta_push.restype = c_int
    break

# vendor/flecs/flecs.h: 16690
for _lib in _libs.values():
    if not _lib.has("ecs_meta_pop", "cdecl"):
        continue
    ecs_meta_pop = _lib.get("ecs_meta_pop", "cdecl")
    ecs_meta_pop.argtypes = [POINTER(ecs_meta_cursor_t)]
    ecs_meta_pop.restype = c_int
    break

# vendor/flecs/flecs.h: 16699
for _lib in _libs.values():
    if not _lib.has("ecs_meta_is_collection", "cdecl"):
        continue
    ecs_meta_is_collection = _lib.get("ecs_meta_is_collection", "cdecl")
    ecs_meta_is_collection.argtypes = [POINTER(ecs_meta_cursor_t)]
    ecs_meta_is_collection.restype = c_bool
    break

# vendor/flecs/flecs.h: 16708
for _lib in _libs.values():
    if not _lib.has("ecs_meta_get_type", "cdecl"):
        continue
    ecs_meta_get_type = _lib.get("ecs_meta_get_type", "cdecl")
    ecs_meta_get_type.argtypes = [POINTER(ecs_meta_cursor_t)]
    ecs_meta_get_type.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 16717
for _lib in _libs.values():
    if not _lib.has("ecs_meta_get_unit", "cdecl"):
        continue
    ecs_meta_get_unit = _lib.get("ecs_meta_get_unit", "cdecl")
    ecs_meta_get_unit.argtypes = [POINTER(ecs_meta_cursor_t)]
    ecs_meta_get_unit.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 16726
for _lib in _libs.values():
    if not _lib.has("ecs_meta_get_member", "cdecl"):
        continue
    ecs_meta_get_member = _lib.get("ecs_meta_get_member", "cdecl")
    ecs_meta_get_member.argtypes = [POINTER(ecs_meta_cursor_t)]
    ecs_meta_get_member.restype = c_char_p
    break

# vendor/flecs/flecs.h: 16735
for _lib in _libs.values():
    if not _lib.has("ecs_meta_get_member_id", "cdecl"):
        continue
    ecs_meta_get_member_id = _lib.get("ecs_meta_get_member_id", "cdecl")
    ecs_meta_get_member_id.argtypes = [POINTER(ecs_meta_cursor_t)]
    ecs_meta_get_member_id.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 16749
for _lib in _libs.values():
    if not _lib.has("ecs_meta_set_bool", "cdecl"):
        continue
    ecs_meta_set_bool = _lib.get("ecs_meta_set_bool", "cdecl")
    ecs_meta_set_bool.argtypes = [POINTER(ecs_meta_cursor_t), c_bool]
    ecs_meta_set_bool.restype = c_int
    break

# vendor/flecs/flecs.h: 16760
for _lib in _libs.values():
    if not _lib.has("ecs_meta_set_char", "cdecl"):
        continue
    ecs_meta_set_char = _lib.get("ecs_meta_set_char", "cdecl")
    ecs_meta_set_char.argtypes = [POINTER(ecs_meta_cursor_t), c_char]
    ecs_meta_set_char.restype = c_int
    break

# vendor/flecs/flecs.h: 16771
for _lib in _libs.values():
    if not _lib.has("ecs_meta_set_int", "cdecl"):
        continue
    ecs_meta_set_int = _lib.get("ecs_meta_set_int", "cdecl")
    ecs_meta_set_int.argtypes = [POINTER(ecs_meta_cursor_t), c_int64]
    ecs_meta_set_int.restype = c_int
    break

# vendor/flecs/flecs.h: 16782
for _lib in _libs.values():
    if not _lib.has("ecs_meta_set_uint", "cdecl"):
        continue
    ecs_meta_set_uint = _lib.get("ecs_meta_set_uint", "cdecl")
    ecs_meta_set_uint.argtypes = [POINTER(ecs_meta_cursor_t), uint64_t]
    ecs_meta_set_uint.restype = c_int
    break

# vendor/flecs/flecs.h: 16793
for _lib in _libs.values():
    if not _lib.has("ecs_meta_set_float", "cdecl"):
        continue
    ecs_meta_set_float = _lib.get("ecs_meta_set_float", "cdecl")
    ecs_meta_set_float.argtypes = [POINTER(ecs_meta_cursor_t), c_double]
    ecs_meta_set_float.restype = c_int
    break

# vendor/flecs/flecs.h: 16804
for _lib in _libs.values():
    if not _lib.has("ecs_meta_set_string", "cdecl"):
        continue
    ecs_meta_set_string = _lib.get("ecs_meta_set_string", "cdecl")
    ecs_meta_set_string.argtypes = [POINTER(ecs_meta_cursor_t), String]
    ecs_meta_set_string.restype = c_int
    break

# vendor/flecs/flecs.h: 16815
for _lib in _libs.values():
    if not _lib.has("ecs_meta_set_string_literal", "cdecl"):
        continue
    ecs_meta_set_string_literal = _lib.get("ecs_meta_set_string_literal", "cdecl")
    ecs_meta_set_string_literal.argtypes = [POINTER(ecs_meta_cursor_t), String]
    ecs_meta_set_string_literal.restype = c_int
    break

# vendor/flecs/flecs.h: 16826
for _lib in _libs.values():
    if not _lib.has("ecs_meta_set_entity", "cdecl"):
        continue
    ecs_meta_set_entity = _lib.get("ecs_meta_set_entity", "cdecl")
    ecs_meta_set_entity.argtypes = [POINTER(ecs_meta_cursor_t), ecs_entity_t]
    ecs_meta_set_entity.restype = c_int
    break

# vendor/flecs/flecs.h: 16837
for _lib in _libs.values():
    if not _lib.has("ecs_meta_set_id", "cdecl"):
        continue
    ecs_meta_set_id = _lib.get("ecs_meta_set_id", "cdecl")
    ecs_meta_set_id.argtypes = [POINTER(ecs_meta_cursor_t), ecs_id_t]
    ecs_meta_set_id.restype = c_int
    break

# vendor/flecs/flecs.h: 16847
for _lib in _libs.values():
    if not _lib.has("ecs_meta_set_null", "cdecl"):
        continue
    ecs_meta_set_null = _lib.get("ecs_meta_set_null", "cdecl")
    ecs_meta_set_null.argtypes = [POINTER(ecs_meta_cursor_t)]
    ecs_meta_set_null.restype = c_int
    break

# vendor/flecs/flecs.h: 16857
for _lib in _libs.values():
    if not _lib.has("ecs_meta_set_value", "cdecl"):
        continue
    ecs_meta_set_value = _lib.get("ecs_meta_set_value", "cdecl")
    ecs_meta_set_value.argtypes = [POINTER(ecs_meta_cursor_t), POINTER(ecs_value_t)]
    ecs_meta_set_value.restype = c_int
    break

# vendor/flecs/flecs.h: 16869
for _lib in _libs.values():
    if not _lib.has("ecs_meta_get_bool", "cdecl"):
        continue
    ecs_meta_get_bool = _lib.get("ecs_meta_get_bool", "cdecl")
    ecs_meta_get_bool.argtypes = [POINTER(ecs_meta_cursor_t)]
    ecs_meta_get_bool.restype = c_bool
    break

# vendor/flecs/flecs.h: 16878
for _lib in _libs.values():
    if not _lib.has("ecs_meta_get_char", "cdecl"):
        continue
    ecs_meta_get_char = _lib.get("ecs_meta_get_char", "cdecl")
    ecs_meta_get_char.argtypes = [POINTER(ecs_meta_cursor_t)]
    ecs_meta_get_char.restype = c_char
    break

# vendor/flecs/flecs.h: 16887
for _lib in _libs.values():
    if not _lib.has("ecs_meta_get_int", "cdecl"):
        continue
    ecs_meta_get_int = _lib.get("ecs_meta_get_int", "cdecl")
    ecs_meta_get_int.argtypes = [POINTER(ecs_meta_cursor_t)]
    ecs_meta_get_int.restype = c_int64
    break

# vendor/flecs/flecs.h: 16896
for _lib in _libs.values():
    if not _lib.has("ecs_meta_get_uint", "cdecl"):
        continue
    ecs_meta_get_uint = _lib.get("ecs_meta_get_uint", "cdecl")
    ecs_meta_get_uint.argtypes = [POINTER(ecs_meta_cursor_t)]
    ecs_meta_get_uint.restype = uint64_t
    break

# vendor/flecs/flecs.h: 16905
for _lib in _libs.values():
    if not _lib.has("ecs_meta_get_float", "cdecl"):
        continue
    ecs_meta_get_float = _lib.get("ecs_meta_get_float", "cdecl")
    ecs_meta_get_float.argtypes = [POINTER(ecs_meta_cursor_t)]
    ecs_meta_get_float.restype = c_double
    break

# vendor/flecs/flecs.h: 16916
for _lib in _libs.values():
    if not _lib.has("ecs_meta_get_string", "cdecl"):
        continue
    ecs_meta_get_string = _lib.get("ecs_meta_get_string", "cdecl")
    ecs_meta_get_string.argtypes = [POINTER(ecs_meta_cursor_t)]
    ecs_meta_get_string.restype = c_char_p
    break

# vendor/flecs/flecs.h: 16926
for _lib in _libs.values():
    if not _lib.has("ecs_meta_get_entity", "cdecl"):
        continue
    ecs_meta_get_entity = _lib.get("ecs_meta_get_entity", "cdecl")
    ecs_meta_get_entity.argtypes = [POINTER(ecs_meta_cursor_t)]
    ecs_meta_get_entity.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 16935
for _lib in _libs.values():
    if not _lib.has("ecs_meta_get_id", "cdecl"):
        continue
    ecs_meta_get_id = _lib.get("ecs_meta_get_id", "cdecl")
    ecs_meta_get_id.argtypes = [POINTER(ecs_meta_cursor_t)]
    ecs_meta_get_id.restype = ecs_id_t
    break

# vendor/flecs/flecs.h: 16945
for _lib in _libs.values():
    if not _lib.has("ecs_meta_ptr_to_float", "cdecl"):
        continue
    ecs_meta_ptr_to_float = _lib.get("ecs_meta_ptr_to_float", "cdecl")
    ecs_meta_ptr_to_float.argtypes = [ecs_primitive_kind_t, POINTER(None)]
    ecs_meta_ptr_to_float.restype = c_double
    break


# vendor/flecs/flecs.h: 16955
class struct_ecs_primitive_desc_t(Structure):
    pass


struct_ecs_primitive_desc_t.__slots__ = [
    "entity",
    "kind",
]
struct_ecs_primitive_desc_t._fields_ = [
    ("entity", ecs_entity_t),
    ("kind", ecs_primitive_kind_t),
]

ecs_primitive_desc_t = struct_ecs_primitive_desc_t  # vendor/flecs/flecs.h: 16955

# vendor/flecs/flecs.h: 16964
for _lib in _libs.values():
    if not _lib.has("ecs_primitive_init", "cdecl"):
        continue
    ecs_primitive_init = _lib.get("ecs_primitive_init", "cdecl")
    ecs_primitive_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_primitive_desc_t)]
    ecs_primitive_init.restype = ecs_entity_t
    break


# vendor/flecs/flecs.h: 16974
class struct_ecs_enum_desc_t(Structure):
    pass


struct_ecs_enum_desc_t.__slots__ = [
    "entity",
    "constants",
    "underlying_type",
]
struct_ecs_enum_desc_t._fields_ = [
    ("entity", ecs_entity_t),
    ("constants", ecs_enum_constant_t * int(32)),
    ("underlying_type", ecs_entity_t),
]

ecs_enum_desc_t = struct_ecs_enum_desc_t  # vendor/flecs/flecs.h: 16974

# vendor/flecs/flecs.h: 16983
for _lib in _libs.values():
    if not _lib.has("ecs_enum_init", "cdecl"):
        continue
    ecs_enum_init = _lib.get("ecs_enum_init", "cdecl")
    ecs_enum_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_enum_desc_t)]
    ecs_enum_init.restype = ecs_entity_t
    break


# vendor/flecs/flecs.h: 16992
class struct_ecs_bitmask_desc_t(Structure):
    pass


struct_ecs_bitmask_desc_t.__slots__ = [
    "entity",
    "constants",
]
struct_ecs_bitmask_desc_t._fields_ = [
    ("entity", ecs_entity_t),
    ("constants", ecs_bitmask_constant_t * int(32)),
]

ecs_bitmask_desc_t = struct_ecs_bitmask_desc_t  # vendor/flecs/flecs.h: 16992

# vendor/flecs/flecs.h: 17001
for _lib in _libs.values():
    if not _lib.has("ecs_bitmask_init", "cdecl"):
        continue
    ecs_bitmask_init = _lib.get("ecs_bitmask_init", "cdecl")
    ecs_bitmask_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_bitmask_desc_t)]
    ecs_bitmask_init.restype = ecs_entity_t
    break


# vendor/flecs/flecs.h: 17011
class struct_ecs_array_desc_t(Structure):
    pass


struct_ecs_array_desc_t.__slots__ = [
    "entity",
    "type",
    "count",
]
struct_ecs_array_desc_t._fields_ = [
    ("entity", ecs_entity_t),
    ("type", ecs_entity_t),
    ("count", c_int32),
]

ecs_array_desc_t = struct_ecs_array_desc_t  # vendor/flecs/flecs.h: 17011

# vendor/flecs/flecs.h: 17020
for _lib in _libs.values():
    if not _lib.has("ecs_array_init", "cdecl"):
        continue
    ecs_array_init = _lib.get("ecs_array_init", "cdecl")
    ecs_array_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_array_desc_t)]
    ecs_array_init.restype = ecs_entity_t
    break


# vendor/flecs/flecs.h: 17029
class struct_ecs_vector_desc_t(Structure):
    pass


struct_ecs_vector_desc_t.__slots__ = [
    "entity",
    "type",
]
struct_ecs_vector_desc_t._fields_ = [
    ("entity", ecs_entity_t),
    ("type", ecs_entity_t),
]

ecs_vector_desc_t = struct_ecs_vector_desc_t  # vendor/flecs/flecs.h: 17029

# vendor/flecs/flecs.h: 17038
for _lib in _libs.values():
    if not _lib.has("ecs_vector_init", "cdecl"):
        continue
    ecs_vector_init = _lib.get("ecs_vector_init", "cdecl")
    ecs_vector_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_vector_desc_t)]
    ecs_vector_init.restype = ecs_entity_t
    break


# vendor/flecs/flecs.h: 17047
class struct_ecs_struct_desc_t(Structure):
    pass


struct_ecs_struct_desc_t.__slots__ = [
    "entity",
    "members",
]
struct_ecs_struct_desc_t._fields_ = [
    ("entity", ecs_entity_t),
    ("members", ecs_member_t * int(32)),
]

ecs_struct_desc_t = struct_ecs_struct_desc_t  # vendor/flecs/flecs.h: 17047

# vendor/flecs/flecs.h: 17056
for _lib in _libs.values():
    if not _lib.has("ecs_struct_init", "cdecl"):
        continue
    ecs_struct_init = _lib.get("ecs_struct_init", "cdecl")
    ecs_struct_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_struct_desc_t)]
    ecs_struct_init.restype = ecs_entity_t
    break


# vendor/flecs/flecs.h: 17065
class struct_ecs_opaque_desc_t(Structure):
    pass


struct_ecs_opaque_desc_t.__slots__ = [
    "entity",
    "type",
]
struct_ecs_opaque_desc_t._fields_ = [
    ("entity", ecs_entity_t),
    ("type", EcsOpaque),
]

ecs_opaque_desc_t = struct_ecs_opaque_desc_t  # vendor/flecs/flecs.h: 17065

# vendor/flecs/flecs.h: 17090
for _lib in _libs.values():
    if not _lib.has("ecs_opaque_init", "cdecl"):
        continue
    ecs_opaque_init = _lib.get("ecs_opaque_init", "cdecl")
    ecs_opaque_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_opaque_desc_t)]
    ecs_opaque_init.restype = ecs_entity_t
    break


# vendor/flecs/flecs.h: 17122
class struct_ecs_unit_desc_t(Structure):
    pass


struct_ecs_unit_desc_t.__slots__ = [
    "entity",
    "symbol",
    "quantity",
    "base",
    "over",
    "translation",
    "prefix",
]
struct_ecs_unit_desc_t._fields_ = [
    ("entity", ecs_entity_t),
    ("symbol", String),
    ("quantity", ecs_entity_t),
    ("base", ecs_entity_t),
    ("over", ecs_entity_t),
    ("translation", ecs_unit_translation_t),
    ("prefix", ecs_entity_t),
]

ecs_unit_desc_t = struct_ecs_unit_desc_t  # vendor/flecs/flecs.h: 17122

# vendor/flecs/flecs.h: 17131
for _lib in _libs.values():
    if not _lib.has("ecs_unit_init", "cdecl"):
        continue
    ecs_unit_init = _lib.get("ecs_unit_init", "cdecl")
    ecs_unit_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_unit_desc_t)]
    ecs_unit_init.restype = ecs_entity_t
    break


# vendor/flecs/flecs.h: 17146
class struct_ecs_unit_prefix_desc_t(Structure):
    pass


struct_ecs_unit_prefix_desc_t.__slots__ = [
    "entity",
    "symbol",
    "translation",
]
struct_ecs_unit_prefix_desc_t._fields_ = [
    ("entity", ecs_entity_t),
    ("symbol", String),
    ("translation", ecs_unit_translation_t),
]

ecs_unit_prefix_desc_t = struct_ecs_unit_prefix_desc_t  # vendor/flecs/flecs.h: 17146

# vendor/flecs/flecs.h: 17155
for _lib in _libs.values():
    if not _lib.has("ecs_unit_prefix_init", "cdecl"):
        continue
    ecs_unit_prefix_init = _lib.get("ecs_unit_prefix_init", "cdecl")
    ecs_unit_prefix_init.argtypes = [
        POINTER(ecs_world_t),
        POINTER(ecs_unit_prefix_desc_t),
    ]
    ecs_unit_prefix_init.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 17167
for _lib in _libs.values():
    if not _lib.has("ecs_quantity_init", "cdecl"):
        continue
    ecs_quantity_init = _lib.get("ecs_quantity_init", "cdecl")
    ecs_quantity_init.argtypes = [POINTER(ecs_world_t), POINTER(ecs_entity_desc_t)]
    ecs_quantity_init.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 17223
for _lib in _libs.values():
    if not _lib.has("FlecsMetaImport", "cdecl"):
        continue
    FlecsMetaImport = _lib.get("FlecsMetaImport", "cdecl")
    FlecsMetaImport.argtypes = [POINTER(ecs_world_t)]
    FlecsMetaImport.restype = None
    break

# vendor/flecs/flecs.h: 17294
for _lib in _libs.values():
    if not _lib.has("ecs_meta_from_desc", "cdecl"):
        continue
    ecs_meta_from_desc = _lib.get("ecs_meta_from_desc", "cdecl")
    ecs_meta_from_desc.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        ecs_type_kind_t,
        String,
    ]
    ecs_meta_from_desc.restype = c_int
    break

# vendor/flecs/flecs.h: 17418
for _lib in _libs.values():
    if not _lib.has("ecs_set_os_api_impl", "cdecl"):
        continue
    ecs_set_os_api_impl = _lib.get("ecs_set_os_api_impl", "cdecl")
    ecs_set_os_api_impl.argtypes = []
    ecs_set_os_api_impl.restype = None
    break

# vendor/flecs/flecs.h: 17482
for _lib in _libs.values():
    if not _lib.has("ecs_import", "cdecl"):
        continue
    ecs_import = _lib.get("ecs_import", "cdecl")
    ecs_import.argtypes = [POINTER(ecs_world_t), ecs_module_action_t, String]
    ecs_import.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 17496
for _lib in _libs.values():
    if not _lib.has("ecs_import_c", "cdecl"):
        continue
    ecs_import_c = _lib.get("ecs_import_c", "cdecl")
    ecs_import_c.argtypes = [POINTER(ecs_world_t), ecs_module_action_t, String]
    ecs_import_c.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 17520
for _lib in _libs.values():
    if not _lib.has("ecs_import_from_library", "cdecl"):
        continue
    ecs_import_from_library = _lib.get("ecs_import_from_library", "cdecl")
    ecs_import_from_library.argtypes = [POINTER(ecs_world_t), String, String]
    ecs_import_from_library.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 17527
for _lib in _libs.values():
    if not _lib.has("ecs_module_init", "cdecl"):
        continue
    ecs_module_init = _lib.get("ecs_module_init", "cdecl")
    ecs_module_init.argtypes = [
        POINTER(ecs_world_t),
        String,
        POINTER(ecs_component_desc_t),
    ]
    ecs_module_init.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 17615
for _lib in _libs.values():
    if not _lib.has("ecs_cpp_get_type_name", "cdecl"):
        continue
    ecs_cpp_get_type_name = _lib.get("ecs_cpp_get_type_name", "cdecl")
    ecs_cpp_get_type_name.argtypes = [String, String, c_size_t, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_cpp_get_type_name.restype = ReturnString
    else:
        ecs_cpp_get_type_name.restype = String
        ecs_cpp_get_type_name.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 17622
for _lib in _libs.values():
    if not _lib.has("ecs_cpp_get_symbol_name", "cdecl"):
        continue
    ecs_cpp_get_symbol_name = _lib.get("ecs_cpp_get_symbol_name", "cdecl")
    ecs_cpp_get_symbol_name.argtypes = [String, String, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_cpp_get_symbol_name.restype = ReturnString
    else:
        ecs_cpp_get_symbol_name.restype = String
        ecs_cpp_get_symbol_name.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 17628
for _lib in _libs.values():
    if not _lib.has("ecs_cpp_get_constant_name", "cdecl"):
        continue
    ecs_cpp_get_constant_name = _lib.get("ecs_cpp_get_constant_name", "cdecl")
    ecs_cpp_get_constant_name.argtypes = [String, String, c_size_t, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        ecs_cpp_get_constant_name.restype = ReturnString
    else:
        ecs_cpp_get_constant_name.restype = String
        ecs_cpp_get_constant_name.errcheck = ReturnString
    break

# vendor/flecs/flecs.h: 17635
for _lib in _libs.values():
    if not _lib.has("ecs_cpp_trim_module", "cdecl"):
        continue
    ecs_cpp_trim_module = _lib.get("ecs_cpp_trim_module", "cdecl")
    ecs_cpp_trim_module.argtypes = [POINTER(ecs_world_t), String]
    ecs_cpp_trim_module.restype = c_char_p
    break

# vendor/flecs/flecs.h: 17640
for _lib in _libs.values():
    if not _lib.has("ecs_cpp_component_register", "cdecl"):
        continue
    ecs_cpp_component_register = _lib.get("ecs_cpp_component_register", "cdecl")
    ecs_cpp_component_register.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        c_int32,
        String,
        String,
        String,
        c_size_t,
        c_size_t,
        c_bool,
        c_bool,
        POINTER(c_bool),
        POINTER(c_bool),
    ]
    ecs_cpp_component_register.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 17655
for _lib in _libs.values():
    if not _lib.has("ecs_cpp_enum_init", "cdecl"):
        continue
    ecs_cpp_enum_init = _lib.get("ecs_cpp_enum_init", "cdecl")
    ecs_cpp_enum_init.argtypes = [POINTER(ecs_world_t), ecs_entity_t, ecs_entity_t]
    ecs_cpp_enum_init.restype = None
    break

# vendor/flecs/flecs.h: 17661
for _lib in _libs.values():
    if not _lib.has("ecs_cpp_enum_constant_register", "cdecl"):
        continue
    ecs_cpp_enum_constant_register = _lib.get("ecs_cpp_enum_constant_register", "cdecl")
    ecs_cpp_enum_constant_register.argtypes = [
        POINTER(ecs_world_t),
        ecs_entity_t,
        ecs_entity_t,
        String,
        POINTER(None),
        ecs_entity_t,
        c_size_t,
    ]
    ecs_cpp_enum_constant_register.restype = ecs_entity_t
    break

# vendor/flecs/flecs.h: 17672
for _lib in _libs.values():
    if not _lib.has("ecs_cpp_last_member", "cdecl"):
        continue
    ecs_cpp_last_member = _lib.get("ecs_cpp_last_member", "cdecl")
    ecs_cpp_last_member.argtypes = [POINTER(ecs_world_t), ecs_entity_t]
    ecs_cpp_last_member.restype = POINTER(ecs_member_t)
    break

# <built-in>
try:
    __clang_major__ = 21
except:
    pass

# vendor/flecs/flecs.h: 36
try:
    FLECS_VERSION_MAJOR = 4
except:
    pass

# vendor/flecs/flecs.h: 37
try:
    FLECS_VERSION_MINOR = 1
except:
    pass

# vendor/flecs/flecs.h: 38
try:
    FLECS_VERSION_PATCH = 0
except:
    pass

# vendor/flecs/flecs.h: 41
try:
    FLECS_VERSION = FLECS_VERSION_IMPL(
        FLECS_VERSION_MAJOR, FLECS_VERSION_MINOR, FLECS_VERSION_PATCH
    )
except:
    pass

ecs_float_t = c_float  # vendor/flecs/flecs.h: 54

# vendor/flecs/flecs.h: 261
try:
    FLECS_HI_COMPONENT_ID = 256
except:
    pass

# vendor/flecs/flecs.h: 271
try:
    FLECS_HI_ID_RECORD_ID = 1024
except:
    pass

# vendor/flecs/flecs.h: 280
try:
    FLECS_SPARSE_PAGE_BITS = 6
except:
    pass

# vendor/flecs/flecs.h: 286
try:
    FLECS_ENTITY_PAGE_BITS = 10
except:
    pass

# vendor/flecs/flecs.h: 298
try:
    FLECS_ID_DESC_MAX = 32
except:
    pass

# vendor/flecs/flecs.h: 304
try:
    FLECS_EVENT_DESC_MAX = 8
except:
    pass

# vendor/flecs/flecs.h: 309
try:
    FLECS_VARIABLE_COUNT_MAX = 64
except:
    pass

# vendor/flecs/flecs.h: 314
try:
    FLECS_TERM_COUNT_MAX = 32
except:
    pass

# vendor/flecs/flecs.h: 320
try:
    FLECS_TERM_ARG_COUNT_MAX = 16
except:
    pass

# vendor/flecs/flecs.h: 326
try:
    FLECS_QUERY_VARIABLE_COUNT_MAX = 64
except:
    pass

# vendor/flecs/flecs.h: 332
try:
    FLECS_QUERY_SCOPE_NESTING_MAX = 8
except:
    pass

# vendor/flecs/flecs.h: 340
try:
    FLECS_DAG_DEPTH_MAX = 128
except:
    pass

# vendor/flecs/flecs.h: 374
try:
    EcsWorldQuitWorkers = 1 << 0
except:
    pass

# vendor/flecs/flecs.h: 375
try:
    EcsWorldReadonly = 1 << 1
except:
    pass

# vendor/flecs/flecs.h: 376
try:
    EcsWorldInit = 1 << 2
except:
    pass

# vendor/flecs/flecs.h: 377
try:
    EcsWorldQuit = 1 << 3
except:
    pass

# vendor/flecs/flecs.h: 378
try:
    EcsWorldFini = 1 << 4
except:
    pass

# vendor/flecs/flecs.h: 379
try:
    EcsWorldMeasureFrameTime = 1 << 5
except:
    pass

# vendor/flecs/flecs.h: 380
try:
    EcsWorldMeasureSystemTime = 1 << 6
except:
    pass

# vendor/flecs/flecs.h: 381
try:
    EcsWorldMultiThreaded = 1 << 7
except:
    pass

# vendor/flecs/flecs.h: 382
try:
    EcsWorldFrameInProgress = 1 << 8
except:
    pass

# vendor/flecs/flecs.h: 388
try:
    EcsOsApiHighResolutionTimer = 1 << 0
except:
    pass

# vendor/flecs/flecs.h: 389
try:
    EcsOsApiLogWithColors = 1 << 1
except:
    pass

# vendor/flecs/flecs.h: 390
try:
    EcsOsApiLogWithTimeStamp = 1 << 2
except:
    pass

# vendor/flecs/flecs.h: 391
try:
    EcsOsApiLogWithTimeDelta = 1 << 3
except:
    pass

# vendor/flecs/flecs.h: 398
try:
    EcsEntityIsId = 1 << 31
except:
    pass

# vendor/flecs/flecs.h: 399
try:
    EcsEntityIsTarget = 1 << 30
except:
    pass

# vendor/flecs/flecs.h: 400
try:
    EcsEntityIsTraversable = 1 << 29
except:
    pass

# vendor/flecs/flecs.h: 401
try:
    EcsEntityHasDontFragment = 1 << 28
except:
    pass

# vendor/flecs/flecs.h: 408
try:
    EcsIdOnDeleteRemove = 1 << 0
except:
    pass

# vendor/flecs/flecs.h: 409
try:
    EcsIdOnDeleteDelete = 1 << 1
except:
    pass

# vendor/flecs/flecs.h: 410
try:
    EcsIdOnDeletePanic = 1 << 2
except:
    pass

# vendor/flecs/flecs.h: 411
try:
    EcsIdOnDeleteMask = (EcsIdOnDeletePanic | EcsIdOnDeleteRemove) | EcsIdOnDeleteDelete
except:
    pass

# vendor/flecs/flecs.h: 414
try:
    EcsIdOnDeleteTargetRemove = 1 << 3
except:
    pass

# vendor/flecs/flecs.h: 415
try:
    EcsIdOnDeleteTargetDelete = 1 << 4
except:
    pass

# vendor/flecs/flecs.h: 416
try:
    EcsIdOnDeleteTargetPanic = 1 << 5
except:
    pass

# vendor/flecs/flecs.h: 417
try:
    EcsIdOnDeleteTargetMask = (
        EcsIdOnDeleteTargetPanic | EcsIdOnDeleteTargetRemove
    ) | EcsIdOnDeleteTargetDelete
except:
    pass

# vendor/flecs/flecs.h: 421
try:
    EcsIdOnInstantiateOverride = 1 << 6
except:
    pass

# vendor/flecs/flecs.h: 422
try:
    EcsIdOnInstantiateInherit = 1 << 7
except:
    pass

# vendor/flecs/flecs.h: 423
try:
    EcsIdOnInstantiateDontInherit = 1 << 8
except:
    pass

# vendor/flecs/flecs.h: 424
try:
    EcsIdOnInstantiateMask = (
        EcsIdOnInstantiateOverride | EcsIdOnInstantiateInherit
    ) | EcsIdOnInstantiateDontInherit
except:
    pass

# vendor/flecs/flecs.h: 428
try:
    EcsIdExclusive = 1 << 9
except:
    pass

# vendor/flecs/flecs.h: 429
try:
    EcsIdTraversable = 1 << 10
except:
    pass

# vendor/flecs/flecs.h: 430
try:
    EcsIdTag = 1 << 11
except:
    pass

# vendor/flecs/flecs.h: 431
try:
    EcsIdWith = 1 << 12
except:
    pass

# vendor/flecs/flecs.h: 432
try:
    EcsIdCanToggle = 1 << 13
except:
    pass

# vendor/flecs/flecs.h: 433
try:
    EcsIdIsTransitive = 1 << 14
except:
    pass

# vendor/flecs/flecs.h: 434
try:
    EcsIdIsInheritable = 1 << 15
except:
    pass

# vendor/flecs/flecs.h: 436
try:
    EcsIdHasOnAdd = 1 << 16
except:
    pass

# vendor/flecs/flecs.h: 437
try:
    EcsIdHasOnRemove = 1 << 17
except:
    pass

# vendor/flecs/flecs.h: 438
try:
    EcsIdHasOnSet = 1 << 18
except:
    pass

# vendor/flecs/flecs.h: 439
try:
    EcsIdHasOnTableCreate = 1 << 21
except:
    pass

# vendor/flecs/flecs.h: 440
try:
    EcsIdHasOnTableDelete = 1 << 22
except:
    pass

# vendor/flecs/flecs.h: 441
try:
    EcsIdIsSparse = 1 << 23
except:
    pass

# vendor/flecs/flecs.h: 442
try:
    EcsIdDontFragment = 1 << 24
except:
    pass

# vendor/flecs/flecs.h: 443
try:
    EcsIdMatchDontFragment = 1 << 25
except:
    pass

# vendor/flecs/flecs.h: 444
try:
    EcsIdOrderedChildren = 1 << 28
except:
    pass

# vendor/flecs/flecs.h: 445
try:
    EcsIdEventMask = (
        (
            (
                ((EcsIdHasOnAdd | EcsIdHasOnRemove) | EcsIdHasOnSet)
                | EcsIdHasOnTableCreate
            )
            | EcsIdHasOnTableDelete
        )
        | EcsIdIsSparse
    ) | EcsIdOrderedChildren
except:
    pass

# vendor/flecs/flecs.h: 450
try:
    EcsIdMarkedForDelete = 1 << 30
except:
    pass


# vendor/flecs/flecs.h: 457
def ECS_ID_ON_DELETE_FLAG(id):
    return 1 << (id - EcsRemove)


# vendor/flecs/flecs.h: 458
def ECS_ID_ON_DELETE_TARGET_FLAG(id):
    return 1 << (3 + (id - EcsRemove))


# vendor/flecs/flecs.h: 464
def ECS_ID_ON_INSTANTIATE_FLAG(id):
    return 1 << (6 + (id - EcsOverride))


# vendor/flecs/flecs.h: 471
try:
    EcsNonTrivialIdSparse = 1 << 0
except:
    pass

# vendor/flecs/flecs.h: 472
try:
    EcsNonTrivialIdNonFragmenting = 1 << 1
except:
    pass

# vendor/flecs/flecs.h: 473
try:
    EcsNonTrivialIdInherit = 1 << 2
except:
    pass

# vendor/flecs/flecs.h: 480
try:
    EcsIterIsValid = 1 << 0
except:
    pass

# vendor/flecs/flecs.h: 481
try:
    EcsIterNoData = 1 << 1
except:
    pass

# vendor/flecs/flecs.h: 482
try:
    EcsIterNoResults = 1 << 2
except:
    pass

# vendor/flecs/flecs.h: 483
try:
    EcsIterMatchEmptyTables = 1 << 3
except:
    pass

# vendor/flecs/flecs.h: 484
try:
    EcsIterIgnoreThis = 1 << 4
except:
    pass

# vendor/flecs/flecs.h: 485
try:
    EcsIterTrivialChangeDetection = 1 << 5
except:
    pass

# vendor/flecs/flecs.h: 486
try:
    EcsIterHasCondSet = 1 << 6
except:
    pass

# vendor/flecs/flecs.h: 487
try:
    EcsIterProfile = 1 << 7
except:
    pass

# vendor/flecs/flecs.h: 488
try:
    EcsIterTrivialSearch = 1 << 8
except:
    pass

# vendor/flecs/flecs.h: 489
try:
    EcsIterTrivialTest = 1 << 11
except:
    pass

# vendor/flecs/flecs.h: 490
try:
    EcsIterTrivialCached = 1 << 14
except:
    pass

# vendor/flecs/flecs.h: 491
try:
    EcsIterCached = 1 << 15
except:
    pass

# vendor/flecs/flecs.h: 492
try:
    EcsIterFixedInChangeComputed = 1 << 16
except:
    pass

# vendor/flecs/flecs.h: 493
try:
    EcsIterFixedInChanged = 1 << 17
except:
    pass

# vendor/flecs/flecs.h: 494
try:
    EcsIterSkip = 1 << 18
except:
    pass

# vendor/flecs/flecs.h: 495
try:
    EcsIterCppEach = 1 << 19
except:
    pass

# vendor/flecs/flecs.h: 499
try:
    EcsIterTableOnly = 1 << 20
except:
    pass

# vendor/flecs/flecs.h: 506
try:
    EcsEventTableOnly = 1 << 20
except:
    pass

# vendor/flecs/flecs.h: 507
try:
    EcsEventNoOnSet = 1 << 16
except:
    pass

# vendor/flecs/flecs.h: 515
try:
    EcsQueryMatchThis = 1 << 11
except:
    pass

# vendor/flecs/flecs.h: 516
try:
    EcsQueryMatchOnlyThis = 1 << 12
except:
    pass

# vendor/flecs/flecs.h: 517
try:
    EcsQueryMatchOnlySelf = 1 << 13
except:
    pass

# vendor/flecs/flecs.h: 518
try:
    EcsQueryMatchWildcards = 1 << 14
except:
    pass

# vendor/flecs/flecs.h: 519
try:
    EcsQueryMatchNothing = 1 << 15
except:
    pass

# vendor/flecs/flecs.h: 520
try:
    EcsQueryHasCondSet = 1 << 16
except:
    pass

# vendor/flecs/flecs.h: 521
try:
    EcsQueryHasPred = 1 << 17
except:
    pass

# vendor/flecs/flecs.h: 522
try:
    EcsQueryHasScopes = 1 << 18
except:
    pass

# vendor/flecs/flecs.h: 523
try:
    EcsQueryHasRefs = 1 << 19
except:
    pass

# vendor/flecs/flecs.h: 524
try:
    EcsQueryHasOutTerms = 1 << 20
except:
    pass

# vendor/flecs/flecs.h: 525
try:
    EcsQueryHasNonThisOutTerms = 1 << 21
except:
    pass

# vendor/flecs/flecs.h: 526
try:
    EcsQueryHasChangeDetection = 1 << 22
except:
    pass

# vendor/flecs/flecs.h: 527
try:
    EcsQueryIsTrivial = 1 << 23
except:
    pass

# vendor/flecs/flecs.h: 528
try:
    EcsQueryHasCacheable = 1 << 24
except:
    pass

# vendor/flecs/flecs.h: 529
try:
    EcsQueryIsCacheable = 1 << 25
except:
    pass

# vendor/flecs/flecs.h: 530
try:
    EcsQueryHasTableThisVar = 1 << 26
except:
    pass

# vendor/flecs/flecs.h: 531
try:
    EcsQueryCacheYieldEmptyTables = 1 << 27
except:
    pass

# vendor/flecs/flecs.h: 532
try:
    EcsQueryTrivialCache = 1 << 28
except:
    pass

# vendor/flecs/flecs.h: 533
try:
    EcsQueryNested = 1 << 29
except:
    pass

# vendor/flecs/flecs.h: 539
try:
    EcsTermMatchAny = 1 << 0
except:
    pass

# vendor/flecs/flecs.h: 540
try:
    EcsTermMatchAnySrc = 1 << 1
except:
    pass

# vendor/flecs/flecs.h: 541
try:
    EcsTermTransitive = 1 << 2
except:
    pass

# vendor/flecs/flecs.h: 542
try:
    EcsTermReflexive = 1 << 3
except:
    pass

# vendor/flecs/flecs.h: 543
try:
    EcsTermIdInherited = 1 << 4
except:
    pass

# vendor/flecs/flecs.h: 544
try:
    EcsTermIsTrivial = 1 << 5
except:
    pass

# vendor/flecs/flecs.h: 545
try:
    EcsTermIsCacheable = 1 << 7
except:
    pass

# vendor/flecs/flecs.h: 546
try:
    EcsTermIsScope = 1 << 8
except:
    pass

# vendor/flecs/flecs.h: 547
try:
    EcsTermIsMember = 1 << 9
except:
    pass

# vendor/flecs/flecs.h: 548
try:
    EcsTermIsToggle = 1 << 10
except:
    pass

# vendor/flecs/flecs.h: 549
try:
    EcsTermKeepAlive = 1 << 11
except:
    pass

# vendor/flecs/flecs.h: 550
try:
    EcsTermIsSparse = 1 << 12
except:
    pass

# vendor/flecs/flecs.h: 551
try:
    EcsTermIsOr = 1 << 13
except:
    pass

# vendor/flecs/flecs.h: 552
try:
    EcsTermDontFragment = 1 << 14
except:
    pass

# vendor/flecs/flecs.h: 559
try:
    EcsObserverMatchPrefab = 1 << 1
except:
    pass

# vendor/flecs/flecs.h: 560
try:
    EcsObserverMatchDisabled = 1 << 2
except:
    pass

# vendor/flecs/flecs.h: 561
try:
    EcsObserverIsMulti = 1 << 3
except:
    pass

# vendor/flecs/flecs.h: 562
try:
    EcsObserverIsMonitor = 1 << 4
except:
    pass

# vendor/flecs/flecs.h: 563
try:
    EcsObserverIsDisabled = 1 << 5
except:
    pass

# vendor/flecs/flecs.h: 564
try:
    EcsObserverIsParentDisabled = 1 << 6
except:
    pass

# vendor/flecs/flecs.h: 565
try:
    EcsObserverBypassQuery = 1 << 7
except:
    pass

# vendor/flecs/flecs.h: 566
try:
    EcsObserverYieldOnCreate = 1 << 8
except:
    pass

# vendor/flecs/flecs.h: 567
try:
    EcsObserverYieldOnDelete = 1 << 9
except:
    pass

# vendor/flecs/flecs.h: 568
try:
    EcsObserverKeepAlive = 1 << 11
except:
    pass

# vendor/flecs/flecs.h: 574
try:
    EcsTableHasBuiltins = 1 << 1
except:
    pass

# vendor/flecs/flecs.h: 575
try:
    EcsTableIsPrefab = 1 << 2
except:
    pass

# vendor/flecs/flecs.h: 576
try:
    EcsTableHasIsA = 1 << 3
except:
    pass

# vendor/flecs/flecs.h: 577
try:
    EcsTableHasChildOf = 1 << 4
except:
    pass

# vendor/flecs/flecs.h: 578
try:
    EcsTableHasName = 1 << 5
except:
    pass

# vendor/flecs/flecs.h: 579
try:
    EcsTableHasPairs = 1 << 6
except:
    pass

# vendor/flecs/flecs.h: 580
try:
    EcsTableHasModule = 1 << 7
except:
    pass

# vendor/flecs/flecs.h: 581
try:
    EcsTableIsDisabled = 1 << 8
except:
    pass

# vendor/flecs/flecs.h: 582
try:
    EcsTableNotQueryable = 1 << 9
except:
    pass

# vendor/flecs/flecs.h: 583
try:
    EcsTableHasCtors = 1 << 10
except:
    pass

# vendor/flecs/flecs.h: 584
try:
    EcsTableHasDtors = 1 << 11
except:
    pass

# vendor/flecs/flecs.h: 585
try:
    EcsTableHasCopy = 1 << 12
except:
    pass

# vendor/flecs/flecs.h: 586
try:
    EcsTableHasMove = 1 << 13
except:
    pass

# vendor/flecs/flecs.h: 587
try:
    EcsTableHasToggle = 1 << 14
except:
    pass

# vendor/flecs/flecs.h: 588
try:
    EcsTableHasOverrides = 1 << 15
except:
    pass

# vendor/flecs/flecs.h: 590
try:
    EcsTableHasOnAdd = 1 << 16
except:
    pass

# vendor/flecs/flecs.h: 591
try:
    EcsTableHasOnRemove = 1 << 17
except:
    pass

# vendor/flecs/flecs.h: 592
try:
    EcsTableHasOnSet = 1 << 18
except:
    pass

# vendor/flecs/flecs.h: 593
try:
    EcsTableHasOnTableFill = 1 << 19
except:
    pass

# vendor/flecs/flecs.h: 594
try:
    EcsTableHasOnTableEmpty = 1 << 20
except:
    pass

# vendor/flecs/flecs.h: 595
try:
    EcsTableHasOnTableCreate = 1 << 21
except:
    pass

# vendor/flecs/flecs.h: 596
try:
    EcsTableHasOnTableDelete = 1 << 22
except:
    pass

# vendor/flecs/flecs.h: 597
try:
    EcsTableHasSparse = 1 << 23
except:
    pass

# vendor/flecs/flecs.h: 598
try:
    EcsTableHasDontFragment = 1 << 24
except:
    pass

# vendor/flecs/flecs.h: 599
try:
    EcsTableOverrideDontFragment = 1 << 25
except:
    pass

# vendor/flecs/flecs.h: 601
try:
    EcsTableHasTraversable = 1 << 27
except:
    pass

# vendor/flecs/flecs.h: 602
try:
    EcsTableHasOrderedChildren = 1 << 28
except:
    pass

# vendor/flecs/flecs.h: 603
try:
    EcsTableEdgeReparent = 1 << 29
except:
    pass

# vendor/flecs/flecs.h: 604
try:
    EcsTableMarkedForDelete = 1 << 30
except:
    pass

# vendor/flecs/flecs.h: 607
try:
    EcsTableHasLifecycle = EcsTableHasCtors | EcsTableHasDtors
except:
    pass

# vendor/flecs/flecs.h: 608
try:
    EcsTableIsComplex = (EcsTableHasLifecycle | EcsTableHasToggle) | EcsTableHasSparse
except:
    pass

# vendor/flecs/flecs.h: 609
try:
    EcsTableHasAddActions = (
        (EcsTableHasIsA | EcsTableHasCtors) | EcsTableHasOnAdd
    ) | EcsTableHasOnSet
except:
    pass

# vendor/flecs/flecs.h: 610
try:
    EcsTableHasRemoveActions = (EcsTableHasIsA | EcsTableHasDtors) | EcsTableHasOnRemove
except:
    pass

# vendor/flecs/flecs.h: 611
try:
    EcsTableEdgeFlags = (EcsTableHasOnAdd | EcsTableHasOnRemove) | EcsTableHasSparse
except:
    pass

# vendor/flecs/flecs.h: 612
try:
    EcsTableAddEdgeFlags = EcsTableHasOnAdd | EcsTableHasSparse
except:
    pass

# vendor/flecs/flecs.h: 613
try:
    EcsTableRemoveEdgeFlags = (
        EcsTableHasOnRemove | EcsTableHasSparse
    ) | EcsTableHasOrderedChildren
except:
    pass

# vendor/flecs/flecs.h: 619
try:
    EcsAperiodicComponentMonitors = 1 << 2
except:
    pass

# vendor/flecs/flecs.h: 620
try:
    EcsAperiodicEmptyQueries = 1 << 4
except:
    pass

# vendor/flecs/flecs.h: 679
try:
    ECS_CLANG_VERSION = __clang_major__
except:
    pass

# /Library/Developer/CommandLineTools/usr/lib/clang/21/include/stdbool.h: 25
try:
    true = 1
except:
    pass

# /Library/Developer/CommandLineTools/usr/lib/clang/21/include/stdbool.h: 26
try:
    false = 0
except:
    pass


# vendor/flecs/flecs.h: 900
def ECS_SIZEOF(T):
    return ECS_CAST(ecs_size_t, sizeof(T))


# vendor/flecs/flecs.h: 939
def ECS_ALIGN(size, alignment):
    return (
        ecs_size_t(
            ord_if_char(
                (
                    (
                        (
                            ((c_size_t(ord_if_char(size))).value - 1)
                            / (c_size_t(ord_if_char(alignment))).value
                        )
                        + 1
                    )
                    * (c_size_t(ord_if_char(alignment))).value
                )
            )
        )
    ).value


# vendor/flecs/flecs.h: 942
def ECS_MAX(a, b):
    return (a > b) and a or b


# vendor/flecs/flecs.h: 943
def ECS_MIN(a, b):
    return (a < b) and a or b


# vendor/flecs/flecs.h: 948
def ECS_CAST(T, V):
    return T(V)


# vendor/flecs/flecs.h: 955
def ECS_CONST_CAST(type, value):
    return (type(uintptr_t))(value)


# vendor/flecs/flecs.h: 962
def ECS_PTR_CAST(type, value):
    return (type(uintptr_t))(value)


# vendor/flecs/flecs.h: 968
def ECS_EQ(a, b):
    return (ecs_os_memcmp(pointer(a), pointer(b), sizeof(a))) == 0


# vendor/flecs/flecs.h: 969
def ECS_NEQ(a, b):
    return not (ECS_EQ(a, b))


# vendor/flecs/flecs.h: 974
def FLECS_VERSION_IMPLSTR(major, minor, patch):
    return (((major + ".") + minor) + ".") + patch


# vendor/flecs/flecs.h: 975
def FLECS_VERSION_IMPL(major, minor, patch):
    return FLECS_VERSION_IMPLSTR(major, minor, patch)


# vendor/flecs/flecs.h: 985
try:
    ecs_world_t_magic = 0x65637377
except:
    pass

# vendor/flecs/flecs.h: 986
try:
    ecs_stage_t_magic = 0x65637373
except:
    pass

# vendor/flecs/flecs.h: 987
try:
    ecs_query_t_magic = 0x65637375
except:
    pass

# vendor/flecs/flecs.h: 988
try:
    ecs_observer_t_magic = 0x65637362
except:
    pass

# vendor/flecs/flecs.h: 995
try:
    ECS_ROW_MASK = 0x0FFFFFFF
except:
    pass

# vendor/flecs/flecs.h: 996
try:
    ECS_ROW_FLAGS_MASK = ~ECS_ROW_MASK
except:
    pass


# vendor/flecs/flecs.h: 997
def ECS_RECORD_TO_ROW(v):
    return ECS_CAST(c_int32, ((ECS_CAST(uint32_t, v)) & ECS_ROW_MASK))


# vendor/flecs/flecs.h: 998
def ECS_RECORD_TO_ROW_FLAGS(v):
    return (ECS_CAST(uint32_t, v)) & ECS_ROW_FLAGS_MASK


# vendor/flecs/flecs.h: 999
def ECS_ROW_TO_RECORD(row, flags):
    return ECS_CAST(uint32_t, ((ECS_CAST(uint32_t, row)) | flags))


# vendor/flecs/flecs.h: 1001
try:
    ECS_ID_FLAGS_MASK = 0xFF << 60
except:
    pass

# vendor/flecs/flecs.h: 1002
try:
    ECS_ENTITY_MASK = 0xFFFFFFFF
except:
    pass

# vendor/flecs/flecs.h: 1003
try:
    ECS_GENERATION_MASK = 0xFFFF << 32
except:
    pass


# vendor/flecs/flecs.h: 1004
def ECS_GENERATION(e):
    return (e & ECS_GENERATION_MASK) >> 32


# vendor/flecs/flecs.h: 1005
def ECS_GENERATION_INC(e):
    return (e & (~ECS_GENERATION_MASK)) | ((0xFFFF & ((ECS_GENERATION(e)) + 1)) << 32)


# vendor/flecs/flecs.h: 1006
try:
    ECS_COMPONENT_MASK = ~ECS_ID_FLAGS_MASK
except:
    pass


# vendor/flecs/flecs.h: 1008
def ECS_IS_PAIR(id):
    return (id & ECS_ID_FLAGS_MASK) == ECS_PAIR


# vendor/flecs/flecs.h: 1009
def ECS_PAIR_FIRST(e):
    return ecs_entity_t_hi((e & ECS_COMPONENT_MASK))


# vendor/flecs/flecs.h: 1010
def ECS_PAIR_SECOND(e):
    return ecs_entity_t_lo(e)


# vendor/flecs/flecs.h: 1013
def ECS_TERM_REF_FLAGS(ref):
    return ((ref.contents.id).value) & EcsTermRefFlags


# vendor/flecs/flecs.h: 1014
def ECS_TERM_REF_ID(ref):
    return ((ref.contents.id).value) & (~EcsTermRefFlags)


# vendor/flecs/flecs.h: 1028
def ecs_entity_t_lo(value):
    return ECS_CAST(uint32_t, value)


# vendor/flecs/flecs.h: 1029
def ecs_entity_t_hi(value):
    return ECS_CAST(uint32_t, (value >> 32))


# vendor/flecs/flecs.h: 1030
def ecs_entity_t_comb(lo, hi):
    return ((ECS_CAST(uint64_t, hi)) << 32) + (ECS_CAST(uint32_t, lo))


# vendor/flecs/flecs.h: 1032
def ecs_pair(pred, obj):
    return ECS_PAIR | (ecs_entity_t_comb(obj, pred))


# vendor/flecs/flecs.h: 1034
def ecs_pair_first(world, pair):
    return ecs_get_alive(world, (ECS_PAIR_FIRST(pair)))


# vendor/flecs/flecs.h: 1035
def ecs_pair_second(world, pair):
    return ecs_get_alive(world, (ECS_PAIR_SECOND(pair)))


# vendor/flecs/flecs.h: 1036
try:
    ecs_pair_relation = ecs_pair_first
except:
    pass

# vendor/flecs/flecs.h: 1037
try:
    ecs_pair_target = ecs_pair_second
except:
    pass


# vendor/flecs/flecs.h: 1179
def ecs_vec_init_t(allocator, vec, T, elem_count):
    return ecs_vec_init_w_dbg_info(
        allocator, vec, (ECS_SIZEOF(T)), elem_count, (("vec<" + T) + ">")
    )


# vendor/flecs/flecs.h: 1187
def ecs_vec_init_if_t(vec, T):
    return ecs_vec_init_if(vec, (ECS_SIZEOF(T)))


# vendor/flecs/flecs.h: 1196
def ecs_vec_fini_t(allocator, vec, T):
    return ecs_vec_fini(allocator, vec, (ECS_SIZEOF(T)))


# vendor/flecs/flecs.h: 1205
def ecs_vec_reset_t(allocator, vec, T):
    return ecs_vec_reset(allocator, vec, (ECS_SIZEOF(T)))


# vendor/flecs/flecs.h: 1227
def ecs_vec_remove_t(vec, T, elem):
    return ecs_vec_remove(vec, (ECS_SIZEOF(T)), elem)


# vendor/flecs/flecs.h: 1236
def ecs_vec_remove_ordered_t(vec, T, elem):
    return ecs_vec_remove_ordered(vec, (ECS_SIZEOF(T)), elem)


# vendor/flecs/flecs.h: 1249
def ecs_vec_copy_t(allocator, vec, T):
    return ecs_vec_copy(allocator, vec, (ECS_SIZEOF(T)))


# vendor/flecs/flecs.h: 1258
def ecs_vec_copy_shrink_t(allocator, vec, T):
    return ecs_vec_copy_shrink(allocator, vec, (ECS_SIZEOF(T)))


# vendor/flecs/flecs.h: 1267
def ecs_vec_reclaim_t(allocator, vec, T):
    return ecs_vec_reclaim(allocator, vec, (ECS_SIZEOF(T)))


# vendor/flecs/flecs.h: 1277
def ecs_vec_set_size_t(allocator, vec, T, elem_count):
    return ecs_vec_set_size(allocator, vec, (ECS_SIZEOF(T)), elem_count)


# vendor/flecs/flecs.h: 1287
def ecs_vec_set_min_size_t(allocator, vec, T, elem_count):
    return ecs_vec_set_min_size(allocator, vec, (ECS_SIZEOF(T)), elem_count)


# vendor/flecs/flecs.h: 1297
def ecs_vec_set_min_count_t(allocator, vec, T, elem_count):
    return ecs_vec_set_min_count(allocator, vec, (ECS_SIZEOF(T)), elem_count)


# vendor/flecs/flecs.h: 1307
def ecs_vec_set_min_count_zeromem_t(allocator, vec, T, elem_count):
    return ecs_vec_set_min_count_zeromem(allocator, vec, (ECS_SIZEOF(T)), elem_count)


# vendor/flecs/flecs.h: 1317
def ecs_vec_set_count_t(allocator, vec, T, elem_count):
    return ecs_vec_set_count(allocator, vec, (ECS_SIZEOF(T)), elem_count)


# vendor/flecs/flecs.h: 1327
def ecs_vec_grow_t(allocator, vec, T, elem_count):
    return ecs_vec_grow(allocator, vec, (ECS_SIZEOF(T)), elem_count)


# vendor/flecs/flecs.h: 1382
try:
    FLECS_SPARSE_PAGE_SIZE = 1 << FLECS_SPARSE_PAGE_BITS
except:
    pass


# vendor/flecs/flecs.h: 1385
def FLECS_SPARSE_PAGE(index):
    return (
        c_int32(
            ord_if_char(
                ((uint32_t(ord_if_char(index))).value >> FLECS_SPARSE_PAGE_BITS)
            )
        )
    ).value


# vendor/flecs/flecs.h: 1388
def FLECS_SPARSE_OFFSET(index):
    return (c_int32(ord_if_char(index))).value & (FLECS_SPARSE_PAGE_SIZE - 1)


# vendor/flecs/flecs.h: 1412
def flecs_sparse_init_t(result, allocator, page_allocator, T):
    return flecs_sparse_init(result, allocator, page_allocator, (ECS_SIZEOF(T)))


# vendor/flecs/flecs.h: 1450
def flecs_sparse_remove_t(sparse, T, id):
    return flecs_sparse_remove(sparse, (ECS_SIZEOF(T)), id)


# vendor/flecs/flecs.h: 1459
def flecs_sparse_remove_w_gen_t(sparse, T, id):
    return flecs_sparse_remove_w_gen(sparse, (ECS_SIZEOF(T)), id)


# vendor/flecs/flecs.h: 1548
def ecs_sparse_init_t(sparse, T):
    return ecs_sparse_init(sparse, (ECS_SIZEOF(T)))


# vendor/flecs/flecs.h: 1631
def flecs_ballocator_init_t(ba, T):
    return flecs_ballocator_init(ba, (ECS_SIZEOF(T)))


# vendor/flecs/flecs.h: 1633
def flecs_ballocator_init_n(ba, T, count):
    return flecs_ballocator_init(ba, ((ECS_SIZEOF(T)) * count))


# vendor/flecs/flecs.h: 1640
def flecs_ballocator_new_t(T):
    return flecs_ballocator_new((ECS_SIZEOF(T)))


# vendor/flecs/flecs.h: 1642
def flecs_ballocator_new_n(T, count):
    return flecs_ballocator_new(((ECS_SIZEOF(T)) * count))


# vendor/flecs/flecs.h: 1738
try:
    FLECS_STACK_PAGE_OFFSET = ECS_ALIGN((ECS_SIZEOF(ecs_stack_page_t)), 16)
except:
    pass

# vendor/flecs/flecs.h: 1739
try:
    FLECS_STACK_PAGE_SIZE = 1024 - FLECS_STACK_PAGE_OFFSET
except:
    pass


# vendor/flecs/flecs.h: 1778
def flecs_stack_free_t(ptr, T):
    return flecs_stack_free(ptr, (ECS_SIZEOF(T)))


# vendor/flecs/flecs.h: 1781
def flecs_stack_free_n(ptr, T, count):
    return flecs_stack_free(ptr, ((ECS_SIZEOF(T)) * count))


# vendor/flecs/flecs.h: 1948
def ecs_map_count(map):
    return map and (map.contents.count) or 0


# vendor/flecs/flecs.h: 1951
def ecs_map_is_init(map):
    return map and (((map.contents.bucket_shift).value) != 0) or false


# vendor/flecs/flecs.h: 1971
def ecs_map_get_ptr(m, k):
    return ECS_CAST(POINTER(None), (ecs_map_get_deref_(m, k)))


# vendor/flecs/flecs.h: 1974
def ecs_map_insert_ptr(m, k, v):
    return ecs_map_insert(m, k, (ECS_CAST(ecs_map_val_t, (ECS_PTR_CAST(uintptr_t, v)))))


# vendor/flecs/flecs.h: 1977
def ecs_map_remove_ptr(m, k):
    return ECS_PTR_CAST(POINTER(None), (ECS_CAST(uintptr_t, (ecs_map_remove(m, k)))))


# vendor/flecs/flecs.h: 1979
def ecs_map_key(it):
    return (it.contents.res)[0]


# vendor/flecs/flecs.h: 1980
def ecs_map_value(it):
    return (it.contents.res)[1]


# vendor/flecs/flecs.h: 1981
def ecs_map_ptr(it):
    return ECS_PTR_CAST(POINTER(None), (ECS_CAST(uintptr_t, (ecs_map_value(it)))))


# vendor/flecs/flecs.h: 2043
def flecs_allocator(obj):
    return pointer(((obj.contents.allocators).dyn))


# vendor/flecs/flecs.h: 2045
def flecs_alloc(a, size):
    return flecs_balloc((flecs_allocator_get(a, size)))


# vendor/flecs/flecs.h: 2046
def flecs_alloc_w_dbg_info(a, size, type_name):
    return flecs_balloc_w_dbg_info((flecs_allocator_get(a, size)), type_name)


# vendor/flecs/flecs.h: 2047
def flecs_alloc_t(a, T):
    return flecs_alloc_w_dbg_info(a, (ECS_SIZEOF(T)), T)


# vendor/flecs/flecs.h: 2048
def flecs_alloc_n(a, T, count):
    return flecs_alloc_w_dbg_info(a, ((ECS_SIZEOF(T)) * count), T)


# vendor/flecs/flecs.h: 2050
def flecs_calloc(a, size):
    return flecs_bcalloc((flecs_allocator_get(a, size)))


# vendor/flecs/flecs.h: 2051
def flecs_calloc_w_dbg_info(a, size, type_name):
    return flecs_bcalloc_w_dbg_info((flecs_allocator_get(a, size)), type_name)


# vendor/flecs/flecs.h: 2052
def flecs_calloc_t(a, T):
    return flecs_calloc_w_dbg_info(a, (ECS_SIZEOF(T)), T)


# vendor/flecs/flecs.h: 2053
def flecs_calloc_n(a, T, count):
    return flecs_calloc_w_dbg_info(a, ((ECS_SIZEOF(T)) * count), T)


# vendor/flecs/flecs.h: 2055
def flecs_free(a, size, ptr):
    return flecs_bfree(ptr and (flecs_allocator_get(a, size)) or NULL, ptr)


# vendor/flecs/flecs.h: 2057
def flecs_free_t(a, T, ptr):
    return flecs_bfree_w_dbg_info(
        ptr and (flecs_allocator_get(a, (ECS_SIZEOF(T)))) or NULL, ptr, T
    )


# vendor/flecs/flecs.h: 2059
def flecs_free_n(a, T, count, ptr):
    return flecs_bfree_w_dbg_info(
        ptr and (flecs_allocator_get(a, ((ECS_SIZEOF(T)) * count))) or NULL, ptr, T
    )


# vendor/flecs/flecs.h: 2063
def flecs_realloc(a, size_dst, size_src, ptr):
    return flecs_brealloc(
        (flecs_allocator_get(a, size_dst)), (flecs_allocator_get(a, size_src)), ptr
    )


# vendor/flecs/flecs.h: 2067
def flecs_realloc_w_dbg_info(a, size_dst, size_src, ptr, type_name):
    return flecs_brealloc_w_dbg_info(
        (flecs_allocator_get(a, size_dst)),
        (flecs_allocator_get(a, size_src)),
        ptr,
        type_name,
    )


# vendor/flecs/flecs.h: 2072
def flecs_realloc_n(a, T, count_dst, count_src, ptr):
    return flecs_realloc(
        a, ((ECS_SIZEOF(T)) * count_dst), ((ECS_SIZEOF(T)) * count_src), ptr
    )


# vendor/flecs/flecs.h: 2075
def flecs_dup_n(a, T, count, ptr):
    return flecs_dup(a, ((ECS_SIZEOF(T)) * count), ptr)


# vendor/flecs/flecs.h: 2141
try:
    ECS_STRBUF_SMALL_STRING_SIZE = 512
except:
    pass

# vendor/flecs/flecs.h: 2142
try:
    ECS_STRBUF_MAX_LIST_DEPTH = 32
except:
    pass


# vendor/flecs/flecs.h: 2290
def ecs_strbuf_appendlit(buf, str):
    return ecs_strbuf_appendstrn(
        buf, str, (c_int32(ord_if_char((sizeof(str) - 1)))).value
    )


# vendor/flecs/flecs.h: 2293
def ecs_strbuf_list_appendlit(buf, str):
    return ecs_strbuf_list_appendstrn(
        buf, str, (c_int32(ord_if_char((sizeof(str) - 1)))).value
    )


# vendor/flecs/flecs.h: 2696
def ecs_os_malloc(size):
    return (ecs_os_api.malloc_)(size)


# vendor/flecs/flecs.h: 2699
def ecs_os_free(ptr):
    return (ecs_os_api.free_)(ptr)


# vendor/flecs/flecs.h: 2702
def ecs_os_realloc(ptr, size):
    return (ecs_os_api.realloc_)(ptr, size)


# vendor/flecs/flecs.h: 2705
def ecs_os_calloc(size):
    return (ecs_os_api.calloc_)(size)


# vendor/flecs/flecs.h: 2710
def ecs_os_alloca(size):
    return alloca((c_size_t(ord_if_char(size))).value)


# vendor/flecs/flecs.h: 2725
def ecs_os_strdup(str):
    return (ecs_os_api.strdup_)(str)


# vendor/flecs/flecs.h: 2736
def ecs_os_strlen(str):
    return (ecs_size_t(ord_if_char((strlen(str))))).value


# vendor/flecs/flecs.h: 2737
def ecs_os_strncmp(str1, str2, num):
    return strncmp(str1, str2, (c_size_t(ord_if_char(num))).value)


# vendor/flecs/flecs.h: 2738
def ecs_os_memcmp(ptr1, ptr2, num):
    return memcmp(ptr1, ptr2, (c_size_t(ord_if_char(num))).value)


# vendor/flecs/flecs.h: 2739
def ecs_os_memcpy(ptr1, ptr2, num):
    return memcpy(ptr1, ptr2, (c_size_t(ord_if_char(num))).value)


# vendor/flecs/flecs.h: 2740
def ecs_os_memset(ptr, value, num):
    return memset(ptr, value, (c_size_t(ord_if_char(num))).value)


# vendor/flecs/flecs.h: 2741
def ecs_os_memmove(dst, src, size):
    return memmove(dst, src, (c_size_t(ord_if_char(size))).value)


# vendor/flecs/flecs.h: 2744
def ecs_os_memcpy_t(ptr1, ptr2, T):
    return ecs_os_memcpy(ptr1, ptr2, (ECS_SIZEOF(T)))


# vendor/flecs/flecs.h: 2745
def ecs_os_memcpy_n(ptr1, ptr2, T, count):
    return ecs_os_memcpy(
        ptr1, ptr2, ((ECS_SIZEOF(T)) * (c_size_t(ord_if_char(count))).value)
    )


# vendor/flecs/flecs.h: 2746
def ecs_os_memcmp_t(ptr1, ptr2, T):
    return ecs_os_memcmp(ptr1, ptr2, (ECS_SIZEOF(T)))


# vendor/flecs/flecs.h: 2748
def ecs_os_memmove_t(ptr1, ptr2, T):
    return ecs_os_memmove(ptr1, ptr2, (ECS_SIZEOF(T)))


# vendor/flecs/flecs.h: 2749
def ecs_os_memmove_n(ptr1, ptr2, T, count):
    return ecs_os_memmove(
        ptr1, ptr2, ((ECS_SIZEOF(T)) * (c_size_t(ord_if_char(count))).value)
    )


# vendor/flecs/flecs.h: 2750
def ecs_os_memmove_t(ptr1, ptr2, T):
    return ecs_os_memmove(ptr1, ptr2, (ECS_SIZEOF(T)))


# vendor/flecs/flecs.h: 2752
def ecs_os_strcmp(str1, str2):
    return strcmp(str1, str2)


# vendor/flecs/flecs.h: 2753
def ecs_os_memset_t(ptr, value, T):
    return ecs_os_memset(ptr, value, (ECS_SIZEOF(T)))


# vendor/flecs/flecs.h: 2754
def ecs_os_memset_n(ptr, value, T, count):
    return ecs_os_memset(
        ptr, value, ((ECS_SIZEOF(T)) * (c_size_t(ord_if_char(count))).value)
    )


# vendor/flecs/flecs.h: 2755
def ecs_os_zeromem(ptr):
    return ecs_os_memset(ptr, 0, (ECS_SIZEOF((ptr[0]))))


# vendor/flecs/flecs.h: 2757
def ecs_os_memdup_t(ptr, T):
    return ecs_os_memdup(ptr, (ECS_SIZEOF(T)))


# vendor/flecs/flecs.h: 2758
def ecs_os_memdup_n(ptr, T, count):
    return ecs_os_memdup(ptr, ((ECS_SIZEOF(T)) * count))


# vendor/flecs/flecs.h: 2770
def ecs_os_strcat(str1, str2):
    return strcat(str1, str2)


# vendor/flecs/flecs.h: 2773
def ecs_os_strcpy(str1, str2):
    return strcpy(str1, str2)


# vendor/flecs/flecs.h: 2774
def ecs_os_strncpy(str1, str2, len):
    return strncpy(str1, str2, (ECS_CAST(c_size_t, len)))


# vendor/flecs/flecs.h: 2785
def ecs_os_thread_new(callback, param):
    return (ecs_os_api.thread_new_)(callback, param)


# vendor/flecs/flecs.h: 2786
def ecs_os_thread_join(thread):
    return (ecs_os_api.thread_join_)(thread)


# vendor/flecs/flecs.h: 2787
def ecs_os_thread_self():
    return ecs_os_api.thread_self_()


# vendor/flecs/flecs.h: 2790
def ecs_os_task_new(callback, param):
    return (ecs_os_api.task_new_)(callback, param)


# vendor/flecs/flecs.h: 2791
def ecs_os_task_join(thread):
    return (ecs_os_api.task_join_)(thread)


# vendor/flecs/flecs.h: 2794
def ecs_os_ainc(value):
    return (ecs_os_api.ainc_)(value)


# vendor/flecs/flecs.h: 2795
def ecs_os_adec(value):
    return (ecs_os_api.adec_)(value)


# vendor/flecs/flecs.h: 2796
def ecs_os_lainc(value):
    return (ecs_os_api.lainc_)(value)


# vendor/flecs/flecs.h: 2797
def ecs_os_ladec(value):
    return (ecs_os_api.ladec_)(value)


# vendor/flecs/flecs.h: 2800
def ecs_os_mutex_new():
    return ecs_os_api.mutex_new_()


# vendor/flecs/flecs.h: 2801
def ecs_os_mutex_free(mutex):
    return (ecs_os_api.mutex_free_)(mutex)


# vendor/flecs/flecs.h: 2802
def ecs_os_mutex_lock(mutex):
    return (ecs_os_api.mutex_lock_)(mutex)


# vendor/flecs/flecs.h: 2803
def ecs_os_mutex_unlock(mutex):
    return (ecs_os_api.mutex_unlock_)(mutex)


# vendor/flecs/flecs.h: 2806
def ecs_os_cond_new():
    return ecs_os_api.cond_new_()


# vendor/flecs/flecs.h: 2807
def ecs_os_cond_free(cond):
    return (ecs_os_api.cond_free_)(cond)


# vendor/flecs/flecs.h: 2808
def ecs_os_cond_signal(cond):
    return (ecs_os_api.cond_signal_)(cond)


# vendor/flecs/flecs.h: 2809
def ecs_os_cond_broadcast(cond):
    return (ecs_os_api.cond_broadcast_)(cond)


# vendor/flecs/flecs.h: 2810
def ecs_os_cond_wait(cond, mutex):
    return (ecs_os_api.cond_wait_)(cond, mutex)


# vendor/flecs/flecs.h: 2813
def ecs_os_sleep(sec, nanosec):
    return (ecs_os_api.sleep_)(sec, nanosec)


# vendor/flecs/flecs.h: 2814
def ecs_os_now():
    return ecs_os_api.now_()


# vendor/flecs/flecs.h: 2815
def ecs_os_get_time(time_out):
    return (ecs_os_api.get_time_)(time_out)


# vendor/flecs/flecs.h: 2824
def ecs_os_inc(v):
    return (v[0]) + 1


# vendor/flecs/flecs.h: 2825
def ecs_os_linc(v):
    return (v[0]) + 1


# vendor/flecs/flecs.h: 2826
def ecs_os_dec(v):
    return (v[0]) - 1


# vendor/flecs/flecs.h: 2827
def ecs_os_ldec(v):
    return (v[0]) - 1


# vendor/flecs/flecs.h: 2848
def ecs_os_abort():
    return ecs_os_api.abort_()


# vendor/flecs/flecs.h: 2851
def ecs_os_dlopen(libname):
    return (ecs_os_api.dlopen_)(libname)


# vendor/flecs/flecs.h: 2852
def ecs_os_dlproc(lib, procname):
    return (ecs_os_api.dlproc_)(lib, procname)


# vendor/flecs/flecs.h: 2853
def ecs_os_dlclose(lib):
    return (ecs_os_api.dlclose_)(lib)


# vendor/flecs/flecs.h: 2856
def ecs_os_module_to_dl(lib):
    return (ecs_os_api.module_to_dl_)(lib)


# vendor/flecs/flecs.h: 2857
def ecs_os_module_to_etc(lib):
    return (ecs_os_api.module_to_etc_)(lib)


# vendor/flecs/flecs.h: 3422
try:
    EcsSelf = 1 << 63
except:
    pass

# vendor/flecs/flecs.h: 3428
try:
    EcsUp = 1 << 62
except:
    pass

# vendor/flecs/flecs.h: 3434
try:
    EcsTrav = 1 << 61
except:
    pass

# vendor/flecs/flecs.h: 3440
try:
    EcsCascade = 1 << 60
except:
    pass

# vendor/flecs/flecs.h: 3446
try:
    EcsDesc = 1 << 59
except:
    pass

# vendor/flecs/flecs.h: 3452
try:
    EcsIsVariable = 1 << 58
except:
    pass

# vendor/flecs/flecs.h: 3458
try:
    EcsIsEntity = 1 << 57
except:
    pass

# vendor/flecs/flecs.h: 3464
try:
    EcsIsName = 1 << 56
except:
    pass

# vendor/flecs/flecs.h: 3470
try:
    EcsTraverseFlags = (((EcsSelf | EcsUp) | EcsTrav) | EcsCascade) | EcsDesc
except:
    pass

# vendor/flecs/flecs.h: 3476
try:
    EcsTermRefFlags = ((EcsTraverseFlags | EcsIsVariable) | EcsIsEntity) | EcsIsName
except:
    pass

# vendor/flecs/flecs.h: 3593
try:
    ECS_TYPE_HOOK_CTOR = ECS_CAST(ecs_flags32_t, (1 << 0))
except:
    pass

# vendor/flecs/flecs.h: 3594
try:
    ECS_TYPE_HOOK_DTOR = ECS_CAST(ecs_flags32_t, (1 << 1))
except:
    pass

# vendor/flecs/flecs.h: 3595
try:
    ECS_TYPE_HOOK_COPY = ECS_CAST(ecs_flags32_t, (1 << 2))
except:
    pass

# vendor/flecs/flecs.h: 3596
try:
    ECS_TYPE_HOOK_MOVE = ECS_CAST(ecs_flags32_t, (1 << 3))
except:
    pass

# vendor/flecs/flecs.h: 3597
try:
    ECS_TYPE_HOOK_COPY_CTOR = ECS_CAST(ecs_flags32_t, (1 << 4))
except:
    pass

# vendor/flecs/flecs.h: 3598
try:
    ECS_TYPE_HOOK_MOVE_CTOR = ECS_CAST(ecs_flags32_t, (1 << 5))
except:
    pass

# vendor/flecs/flecs.h: 3599
try:
    ECS_TYPE_HOOK_CTOR_MOVE_DTOR = ECS_CAST(ecs_flags32_t, (1 << 6))
except:
    pass

# vendor/flecs/flecs.h: 3600
try:
    ECS_TYPE_HOOK_MOVE_DTOR = ECS_CAST(ecs_flags32_t, (1 << 7))
except:
    pass

# vendor/flecs/flecs.h: 3601
try:
    ECS_TYPE_HOOK_CMP = ECS_CAST(ecs_flags32_t, (1 << 8))
except:
    pass

# vendor/flecs/flecs.h: 3602
try:
    ECS_TYPE_HOOK_EQUALS = ECS_CAST(ecs_flags32_t, (1 << 9))
except:
    pass

# vendor/flecs/flecs.h: 3606
try:
    ECS_TYPE_HOOK_CTOR_ILLEGAL = ECS_CAST(ecs_flags32_t, (1 << 10))
except:
    pass

# vendor/flecs/flecs.h: 3607
try:
    ECS_TYPE_HOOK_DTOR_ILLEGAL = ECS_CAST(ecs_flags32_t, (1 << 12))
except:
    pass

# vendor/flecs/flecs.h: 3608
try:
    ECS_TYPE_HOOK_COPY_ILLEGAL = ECS_CAST(ecs_flags32_t, (1 << 13))
except:
    pass

# vendor/flecs/flecs.h: 3609
try:
    ECS_TYPE_HOOK_MOVE_ILLEGAL = ECS_CAST(ecs_flags32_t, (1 << 14))
except:
    pass

# vendor/flecs/flecs.h: 3610
try:
    ECS_TYPE_HOOK_COPY_CTOR_ILLEGAL = ECS_CAST(ecs_flags32_t, (1 << 15))
except:
    pass

# vendor/flecs/flecs.h: 3611
try:
    ECS_TYPE_HOOK_MOVE_CTOR_ILLEGAL = ECS_CAST(ecs_flags32_t, (1 << 16))
except:
    pass

# vendor/flecs/flecs.h: 3612
try:
    ECS_TYPE_HOOK_CTOR_MOVE_DTOR_ILLEGAL = ECS_CAST(ecs_flags32_t, (1 << 17))
except:
    pass

# vendor/flecs/flecs.h: 3613
try:
    ECS_TYPE_HOOK_MOVE_DTOR_ILLEGAL = ECS_CAST(ecs_flags32_t, (1 << 18))
except:
    pass

# vendor/flecs/flecs.h: 3614
try:
    ECS_TYPE_HOOK_CMP_ILLEGAL = ECS_CAST(ecs_flags32_t, (1 << 19))
except:
    pass

# vendor/flecs/flecs.h: 3615
try:
    ECS_TYPE_HOOK_EQUALS_ILLEGAL = ECS_CAST(ecs_flags32_t, (1 << 20))
except:
    pass

# vendor/flecs/flecs.h: 3619
try:
    ECS_TYPE_HOOKS = (
        (
            (
                (
                    (
                        (
                            (
                                (ECS_TYPE_HOOK_CTOR | ECS_TYPE_HOOK_DTOR)
                                | ECS_TYPE_HOOK_COPY
                            )
                            | ECS_TYPE_HOOK_MOVE
                        )
                        | ECS_TYPE_HOOK_COPY_CTOR
                    )
                    | ECS_TYPE_HOOK_MOVE_CTOR
                )
                | ECS_TYPE_HOOK_CTOR_MOVE_DTOR
            )
            | ECS_TYPE_HOOK_MOVE_DTOR
        )
        | ECS_TYPE_HOOK_CMP
    ) | ECS_TYPE_HOOK_EQUALS
except:
    pass

# vendor/flecs/flecs.h: 3625
try:
    ECS_TYPE_HOOKS_ILLEGAL = (
        (
            (
                (
                    (
                        (
                            (
                                (
                                    ECS_TYPE_HOOK_CTOR_ILLEGAL
                                    | ECS_TYPE_HOOK_DTOR_ILLEGAL
                                )
                                | ECS_TYPE_HOOK_COPY_ILLEGAL
                            )
                            | ECS_TYPE_HOOK_MOVE_ILLEGAL
                        )
                        | ECS_TYPE_HOOK_COPY_CTOR_ILLEGAL
                    )
                    | ECS_TYPE_HOOK_MOVE_CTOR_ILLEGAL
                )
                | ECS_TYPE_HOOK_CTOR_MOVE_DTOR_ILLEGAL
            )
            | ECS_TYPE_HOOK_MOVE_DTOR_ILLEGAL
        )
        | ECS_TYPE_HOOK_CMP_ILLEGAL
    ) | ECS_TYPE_HOOK_EQUALS_ILLEGAL
except:
    pass

# vendor/flecs/flecs.h: 3889
try:
    ECS_MAX_COMPONENT_ID = ~(uint32_t(ord_if_char((ECS_ID_FLAGS_MASK >> 32)))).value
except:
    pass

# vendor/flecs/flecs.h: 3893
try:
    ECS_MAX_RECURSION = 512
except:
    pass

# vendor/flecs/flecs.h: 3896
try:
    ECS_MAX_TOKEN_SIZE = 256
except:
    pass


# vendor/flecs/flecs.h: 4206
def ECS_OFFSET(o, offset):
    return cast(
        ((uintptr_t(ord_if_char(o))).value + (uintptr_t(ord_if_char(offset))).value),
        POINTER(None),
    )


# vendor/flecs/flecs.h: 4208
def ECS_OFFSET_T(o, T):
    return ECS_OFFSET(o, (ECS_SIZEOF(T)))


# vendor/flecs/flecs.h: 4210
def ECS_ELEM(ptr, size, index):
    return ECS_OFFSET(ptr, (size * index))


# vendor/flecs/flecs.h: 4211
def ECS_ELEM_T(o, T, index):
    return ECS_ELEM(o, (ECS_SIZEOF(T)), index)


# vendor/flecs/flecs.h: 4225
def ECS_BIT_IS_SET(flags, bit):
    return flags & bit


# vendor/flecs/flecs.h: 4286
def flecs_hashmap_init(hm, K, V, hash, compare, allocator):
    return flecs_hashmap_init_(
        hm, (ECS_SIZEOF(K)), (ECS_SIZEOF(V)), hash, compare, allocator
    )


# vendor/flecs/flecs.h: 4310
def flecs_hashmap_ensure(map, key, V):
    return flecs_hashmap_ensure_(map, (ECS_SIZEOF((key[0]))), key, (ECS_SIZEOF(V)))


# vendor/flecs/flecs.h: 4321
def flecs_hashmap_set(map, key, value):
    return flecs_hashmap_set_(
        map, (ECS_SIZEOF((key[0]))), key, (ECS_SIZEOF((value[0]))), value
    )


# vendor/flecs/flecs.h: 4331
def flecs_hashmap_remove(map, key, V):
    return flecs_hashmap_remove_(map, (ECS_SIZEOF((key[0]))), key, (ECS_SIZEOF(V)))


# vendor/flecs/flecs.h: 4342
def flecs_hashmap_remove_w_hash(map, key, V, hash):
    return flecs_hashmap_remove_w_hash_(
        map, (ECS_SIZEOF((key[0]))), key, (ECS_SIZEOF(V)), hash
    )


# vendor/flecs/flecs.h: 4926
try:
    EcsQueryMatchPrefab = 1 << 1
except:
    pass

# vendor/flecs/flecs.h: 4932
try:
    EcsQueryMatchDisabled = 1 << 2
except:
    pass

# vendor/flecs/flecs.h: 4938
try:
    EcsQueryMatchEmptyTables = 1 << 3
except:
    pass

# vendor/flecs/flecs.h: 4944
try:
    EcsQueryAllowUnresolvedByName = 1 << 6
except:
    pass

# vendor/flecs/flecs.h: 4950
try:
    EcsQueryTableOnly = 1 << 7
except:
    pass

# vendor/flecs/flecs.h: 4962
try:
    EcsQueryDetectChanges = 1 << 8
except:
    pass

# vendor/flecs/flecs.h: 5392
try:
    EcsSingleton = EcsVariable
except:
    pass

# vendor/flecs/flecs.h: 5662
try:
    EcsFirstUserComponentId = 8
except:
    pass

# vendor/flecs/flecs.h: 5666
try:
    EcsFirstUserEntityId = FLECS_HI_COMPONENT_ID + 128
except:
    pass


# vendor/flecs/flecs.h: 10400
def ecs_new_w_pair(world, first, second):
    return ecs_new_w_id(world, (ecs_pair(first, second)))


# vendor/flecs/flecs.h: 10416
def ecs_add_pair(world, subject, first, second):
    return ecs_add_id(world, subject, (ecs_pair(first, second)))


# vendor/flecs/flecs.h: 10423
def ecs_remove_pair(world, subject, first, second):
    return ecs_remove_id(world, subject, (ecs_pair(first, second)))


# vendor/flecs/flecs.h: 10430
def ecs_auto_override_pair(world, subject, first, second):
    return ecs_auto_override_id(world, subject, (ecs_pair(first, second)))


# vendor/flecs/flecs.h: 10532
def ecs_modified_pair(world, subject, first, second):
    return ecs_modified_id(world, subject, (ecs_pair(first, second)))


# vendor/flecs/flecs.h: 10612
def ecs_has_pair(world, entity, first, second):
    return ecs_has_id(world, entity, (ecs_pair(first, second)))


# vendor/flecs/flecs.h: 10615
def ecs_owns_pair(world, entity, first, second):
    return ecs_owns_id(world, entity, (ecs_pair(first, second)))


# vendor/flecs/flecs.h: 10660
def ecs_lookup_from(world, parent, path):
    return ecs_lookup_path_w_sep(world, parent, path, ".", NULL, true)


# vendor/flecs/flecs.h: 10663
def ecs_get_path_from(world, parent, child):
    return ecs_get_path_w_sep(world, parent, child, ".", NULL)


# vendor/flecs/flecs.h: 10666
def ecs_get_path(world, child):
    return ecs_get_path_w_sep(world, 0, child, ".", NULL)


# vendor/flecs/flecs.h: 10669
def ecs_get_path_buf(world, child, buf):
    return ecs_get_path_w_sep_buf(world, 0, child, ".", NULL, buf, false)


# vendor/flecs/flecs.h: 10672
def ecs_new_from_path(world, parent, path):
    return ecs_new_from_path_w_sep(world, parent, path, ".", NULL)


# vendor/flecs/flecs.h: 10675
def ecs_add_path(world, entity, parent, path):
    return ecs_add_path_w_sep(world, entity, parent, path, ".", NULL)


# vendor/flecs/flecs.h: 10678
def ecs_add_fullpath(world, entity, path):
    return ecs_add_path_w_sep(world, entity, 0, path, ".", NULL)


# vendor/flecs/flecs.h: 10963
def ecs_isa(e):
    return ecs_pair(EcsIsA, e)


# vendor/flecs/flecs.h: 10964
def ecs_childof(e):
    return ecs_pair(EcsChildOf, e)


# vendor/flecs/flecs.h: 10965
def ecs_dependson(e):
    return ecs_pair(EcsDependsOn, e)


# vendor/flecs/flecs.h: 10966
def ecs_with(e):
    return ecs_pair(EcsWith, e)


# vendor/flecs/flecs.h: 10969
def ecs_each_pair(world, r, t):
    return ecs_each_id(world, (ecs_pair(r, t)))


# vendor/flecs/flecs.h: 11387
def ecs_should_log_1():
    return false


# vendor/flecs/flecs.h: 11388
def ecs_should_log_2():
    return false


# vendor/flecs/flecs.h: 11389
def ecs_should_log_3():
    return false


# vendor/flecs/flecs.h: 11412
def ecs_log_push():
    return ecs_log_push_(0)


# vendor/flecs/flecs.h: 11413
def ecs_log_pop():
    return ecs_log_pop_(0)


# vendor/flecs/flecs.h: 11499
def ecs_parser_errorv(name, expr, column, fmt, args):
    return ecs_parser_errorv_(name, expr, column, fmt, args)


# vendor/flecs/flecs.h: 11505
def ecs_parser_warningv(name, expr, column, fmt, args):
    return ecs_parser_warningv_(name, expr, column, fmt, args)


# vendor/flecs/flecs.h: 11595
try:
    ECS_INVALID_OPERATION = 1
except:
    pass

# vendor/flecs/flecs.h: 11596
try:
    ECS_INVALID_PARAMETER = 2
except:
    pass

# vendor/flecs/flecs.h: 11597
try:
    ECS_CONSTRAINT_VIOLATED = 3
except:
    pass

# vendor/flecs/flecs.h: 11598
try:
    ECS_OUT_OF_MEMORY = 4
except:
    pass

# vendor/flecs/flecs.h: 11599
try:
    ECS_OUT_OF_RANGE = 5
except:
    pass

# vendor/flecs/flecs.h: 11600
try:
    ECS_UNSUPPORTED = 6
except:
    pass

# vendor/flecs/flecs.h: 11601
try:
    ECS_INTERNAL_ERROR = 7
except:
    pass

# vendor/flecs/flecs.h: 11602
try:
    ECS_ALREADY_DEFINED = 8
except:
    pass

# vendor/flecs/flecs.h: 11603
try:
    ECS_MISSING_OS_API = 9
except:
    pass

# vendor/flecs/flecs.h: 11604
try:
    ECS_OPERATION_FAILED = 10
except:
    pass

# vendor/flecs/flecs.h: 11605
try:
    ECS_INVALID_CONVERSION = 11
except:
    pass

# vendor/flecs/flecs.h: 11606
try:
    ECS_ID_IN_USE = 12
except:
    pass

# vendor/flecs/flecs.h: 11607
try:
    ECS_CYCLE_DETECTED = 13
except:
    pass

# vendor/flecs/flecs.h: 11608
try:
    ECS_LEAK_DETECTED = 14
except:
    pass

# vendor/flecs/flecs.h: 11609
try:
    ECS_DOUBLE_FREE = 15
except:
    pass

# vendor/flecs/flecs.h: 11611
try:
    ECS_INCONSISTENT_NAME = 20
except:
    pass

# vendor/flecs/flecs.h: 11612
try:
    ECS_NAME_IN_USE = 21
except:
    pass

# vendor/flecs/flecs.h: 11613
try:
    ECS_NOT_A_COMPONENT = 22
except:
    pass

# vendor/flecs/flecs.h: 11614
try:
    ECS_INVALID_COMPONENT_SIZE = 23
except:
    pass

# vendor/flecs/flecs.h: 11615
try:
    ECS_INVALID_COMPONENT_ALIGNMENT = 24
except:
    pass

# vendor/flecs/flecs.h: 11616
try:
    ECS_COMPONENT_NOT_REGISTERED = 25
except:
    pass

# vendor/flecs/flecs.h: 11617
try:
    ECS_INCONSISTENT_COMPONENT_ID = 26
except:
    pass

# vendor/flecs/flecs.h: 11618
try:
    ECS_INCONSISTENT_COMPONENT_ACTION = 27
except:
    pass

# vendor/flecs/flecs.h: 11619
try:
    ECS_MODULE_UNDEFINED = 28
except:
    pass

# vendor/flecs/flecs.h: 11620
try:
    ECS_MISSING_SYMBOL = 29
except:
    pass

# vendor/flecs/flecs.h: 11621
try:
    ECS_ALREADY_IN_USE = 30
except:
    pass

# vendor/flecs/flecs.h: 11623
try:
    ECS_ACCESS_VIOLATION = 40
except:
    pass

# vendor/flecs/flecs.h: 11624
try:
    ECS_COLUMN_INDEX_OUT_OF_RANGE = 41
except:
    pass

# vendor/flecs/flecs.h: 11625
try:
    ECS_COLUMN_IS_NOT_SHARED = 42
except:
    pass

# vendor/flecs/flecs.h: 11626
try:
    ECS_COLUMN_IS_SHARED = 43
except:
    pass

# vendor/flecs/flecs.h: 11627
try:
    ECS_COLUMN_TYPE_MISMATCH = 45
except:
    pass

# vendor/flecs/flecs.h: 11629
try:
    ECS_INVALID_WHILE_READONLY = 70
except:
    pass

# vendor/flecs/flecs.h: 11630
try:
    ECS_LOCKED_STORAGE = 71
except:
    pass

# vendor/flecs/flecs.h: 11631
try:
    ECS_INVALID_FROM_WORKER = 72
except:
    pass

# vendor/flecs/flecs.h: 11638
try:
    ECS_BLACK = "\\033[1;30m"
except:
    pass

# vendor/flecs/flecs.h: 11639
try:
    ECS_RED = "\\033[0;31m"
except:
    pass

# vendor/flecs/flecs.h: 11640
try:
    ECS_GREEN = "\\033[0;32m"
except:
    pass

# vendor/flecs/flecs.h: 11641
try:
    ECS_YELLOW = "\\033[0;33m"
except:
    pass

# vendor/flecs/flecs.h: 11642
try:
    ECS_BLUE = "\\033[0;34m"
except:
    pass

# vendor/flecs/flecs.h: 11643
try:
    ECS_MAGENTA = "\\033[0;35m"
except:
    pass

# vendor/flecs/flecs.h: 11644
try:
    ECS_CYAN = "\\033[0;36m"
except:
    pass

# vendor/flecs/flecs.h: 11645
try:
    ECS_WHITE = "\\033[1;37m"
except:
    pass

# vendor/flecs/flecs.h: 11646
try:
    ECS_GREY = "\\033[0;37m"
except:
    pass

# vendor/flecs/flecs.h: 11647
try:
    ECS_NORMAL = "\\033[0;49m"
except:
    pass

# vendor/flecs/flecs.h: 11648
try:
    ECS_BOLD = "\\033[1;49m"
except:
    pass

# vendor/flecs/flecs.h: 11840
try:
    ECS_HTTP_HEADER_COUNT_MAX = 32
except:
    pass

# vendor/flecs/flecs.h: 11843
try:
    ECS_HTTP_QUERY_PARAM_COUNT_MAX = 32
except:
    pass

# vendor/flecs/flecs.h: 12095
try:
    ECS_REST_DEFAULT_PORT = 27750
except:
    pass

# vendor/flecs/flecs.h: 13092
try:
    ECS_STAT_WINDOW = 60
except:
    pass

# vendor/flecs/flecs.h: 13774
try:
    ECS_ALERT_MAX_SEVERITY_FILTERS = 4
except:
    pass

# vendor/flecs/flecs.h: 14891
try:
    FLECS_SCRIPT_FUNCTION_ARGS_MAX = 16
except:
    pass

# vendor/flecs/flecs.h: 16064
try:
    ECS_MEMBER_DESC_CACHE_SIZE = 32
except:
    pass

# vendor/flecs/flecs.h: 16571
try:
    ECS_META_MAX_SCOPE_DEPTH = 32
except:
    pass

ecs_allocator_t = struct_ecs_allocator_t  # vendor/flecs/flecs.h: 2004

ecs_vec_t = struct_ecs_vec_t  # vendor/flecs/flecs.h: 1162

ecs_block_allocator_t = struct_ecs_block_allocator_t  # vendor/flecs/flecs.h: 1611

ecs_sparse_t = struct_ecs_sparse_t  # vendor/flecs/flecs.h: 1402

ecs_map_t = struct_ecs_map_t  # vendor/flecs/flecs.h: 1826

ecs_block_allocator_block_t = (
    struct_ecs_block_allocator_block_t  # vendor/flecs/flecs.h: 1602
)

ecs_block_allocator_chunk_header_t = (
    struct_ecs_block_allocator_chunk_header_t  # vendor/flecs/flecs.h: 1607
)

ecs_stack_page_t = struct_ecs_stack_page_t  # vendor/flecs/flecs.h: 1712

ecs_stack_cursor_t = struct_ecs_stack_cursor_t  # vendor/flecs/flecs.h: 1719

ecs_stack_t = struct_ecs_stack_t  # vendor/flecs/flecs.h: 1736

ecs_bucket_entry_t = struct_ecs_bucket_entry_t  # vendor/flecs/flecs.h: 1816

ecs_bucket_t = struct_ecs_bucket_t  # vendor/flecs/flecs.h: 1824

ecs_map_iter_t = struct_ecs_map_iter_t  # vendor/flecs/flecs.h: 1839

ecs_map_params_t = struct_ecs_map_params_t  # vendor/flecs/flecs.h: 1844

ecs_strbuf_list_elem = struct_ecs_strbuf_list_elem  # vendor/flecs/flecs.h: 2147

ecs_strbuf_t = struct_ecs_strbuf_t  # vendor/flecs/flecs.h: 2158

ecs_time_t = struct_ecs_time_t  # vendor/flecs/flecs.h: 2341

ecs_os_api_t = struct_ecs_os_api_t  # vendor/flecs/flecs.h: 2637

ecs_world_t = struct_ecs_world_t  # vendor/flecs/flecs.h: 3131

ecs_stage_t = struct_ecs_stage_t  # vendor/flecs/flecs.h: 3134

ecs_table_t = struct_ecs_table_t  # vendor/flecs/flecs.h: 3137

ecs_term_t = struct_ecs_term_t  # vendor/flecs/flecs.h: 3494

ecs_query_t = struct_ecs_query_t  # vendor/flecs/flecs.h: 3518

ecs_observer_t = struct_ecs_observer_t  # vendor/flecs/flecs.h: 3559

ecs_observable_t = struct_ecs_observable_t  # vendor/flecs/flecs.h: 3746

ecs_iter_t = struct_ecs_iter_t  # vendor/flecs/flecs.h: 4860

ecs_ref_t = struct_ecs_ref_t  # vendor/flecs/flecs.h: 3774

ecs_type_hooks_t = struct_ecs_type_hooks_t  # vendor/flecs/flecs.h: 3631

ecs_type_info_t = struct_ecs_type_info_t  # vendor/flecs/flecs.h: 3695

ecs_record_t = struct_ecs_record_t  # vendor/flecs/flecs.h: 4401

ecs_component_record_t = struct_ecs_component_record_t  # vendor/flecs/flecs.h: 3199

ecs_mixins_t = struct_ecs_mixins_t  # vendor/flecs/flecs.h: 3223

ecs_header_t = struct_ecs_header_t  # vendor/flecs/flecs.h: 3230

ecs_table_record_t = struct_ecs_table_record_t  # vendor/flecs/flecs.h: 4418

ecs_term_ref_t = struct_ecs_term_ref_t  # vendor/flecs/flecs.h: 3491

ecs_data_t = struct_ecs_data_t  # vendor/flecs/flecs.h: 3725

ecs_query_cache_match_t = struct_ecs_query_cache_match_t  # vendor/flecs/flecs.h: 3728

ecs_query_cache_group_t = struct_ecs_query_cache_group_t  # vendor/flecs/flecs.h: 3731

ecs_event_id_record_t = struct_ecs_event_id_record_t  # vendor/flecs/flecs.h: 3739

ecs_event_record_t = struct_ecs_event_record_t  # vendor/flecs/flecs.h: 3744

ecs_table_range_t = struct_ecs_table_range_t  # vendor/flecs/flecs.h: 3760

ecs_var_t = struct_ecs_var_t  # vendor/flecs/flecs.h: 3771

ecs_page_iter_t = struct_ecs_page_iter_t  # vendor/flecs/flecs.h: 3789

ecs_worker_iter_t = struct_ecs_worker_iter_t  # vendor/flecs/flecs.h: 3795

ecs_table_cache_hdr_t = struct_ecs_table_cache_hdr_t  # vendor/flecs/flecs.h: 4409

ecs_table_cache_iter_t = struct_ecs_table_cache_iter_t  # vendor/flecs/flecs.h: 3802

ecs_each_iter_t = struct_ecs_each_iter_t  # vendor/flecs/flecs.h: 3814

ecs_query_op_profile_t = struct_ecs_query_op_profile_t  # vendor/flecs/flecs.h: 3818

ecs_query_var_t = struct_ecs_query_var_t  # vendor/flecs/flecs.h: 3823

ecs_query_op_t = struct_ecs_query_op_t  # vendor/flecs/flecs.h: 3824

ecs_query_op_ctx_t = struct_ecs_query_op_ctx_t  # vendor/flecs/flecs.h: 3825

ecs_query_iter_t = struct_ecs_query_iter_t  # vendor/flecs/flecs.h: 3839

ecs_iter_private_t = struct_ecs_iter_private_t  # vendor/flecs/flecs.h: 3853

ecs_commands_t = struct_ecs_commands_t  # vendor/flecs/flecs.h: 3860

ecs_suspend_readonly_state_t = (
    struct_ecs_suspend_readonly_state_t  # vendor/flecs/flecs.h: 4051
)

ecs_table_cache_t = struct_ecs_table_cache_t  # vendor/flecs/flecs.h: 4410

ecs_table_diff_t = struct_ecs_table_diff_t  # vendor/flecs/flecs.h: 4432

ecs_table_records_t = struct_ecs_table_records_t  # vendor/flecs/flecs.h: 4671

ecs_value_t = struct_ecs_value_t  # vendor/flecs/flecs.h: 4730

ecs_entity_desc_t = struct_ecs_entity_desc_t  # vendor/flecs/flecs.h: 4776

ecs_bulk_desc_t = struct_ecs_bulk_desc_t  # vendor/flecs/flecs.h: 4806

ecs_component_desc_t = struct_ecs_component_desc_t  # vendor/flecs/flecs.h: 4820

ecs_query_desc_t = struct_ecs_query_desc_t  # vendor/flecs/flecs.h: 5037

ecs_observer_desc_t = struct_ecs_observer_desc_t  # vendor/flecs/flecs.h: 5099

ecs_event_desc_t = struct_ecs_event_desc_t  # vendor/flecs/flecs.h: 5148

ecs_build_info_t = struct_ecs_build_info_t  # vendor/flecs/flecs.h: 5169

ecs_world_info_t = struct_ecs_world_info_t  # vendor/flecs/flecs.h: 5228

ecs_query_group_info_t = struct_ecs_query_group_info_t  # vendor/flecs/flecs.h: 5236

EcsIdentifier = struct_EcsIdentifier  # vendor/flecs/flecs.h: 5254

EcsComponent = struct_EcsComponent  # vendor/flecs/flecs.h: 5260

EcsPoly = struct_EcsPoly  # vendor/flecs/flecs.h: 5265

EcsDefaultChildComponent = struct_EcsDefaultChildComponent  # vendor/flecs/flecs.h: 5274

ecs_entities_t = struct_ecs_entities_t  # vendor/flecs/flecs.h: 5758

ecs_delete_empty_tables_desc_t = (
    struct_ecs_delete_empty_tables_desc_t  # vendor/flecs/flecs.h: 6396
)

ecs_query_count_t = struct_ecs_query_count_t  # vendor/flecs/flecs.h: 8768

ecs_app_desc_t = struct_ecs_app_desc_t  # vendor/flecs/flecs.h: 11728

ecs_http_server_t = struct_ecs_http_server_t  # vendor/flecs/flecs.h: 11850

EcsTimer = struct_EcsTimer  # vendor/flecs/flecs.h: 12196

EcsRateFilter = struct_EcsRateFilter  # vendor/flecs/flecs.h: 12204

ecs_pipeline_desc_t = struct_ecs_pipeline_desc_t  # vendor/flecs/flecs.h: 12547

EcsTickSource = struct_EcsTickSource  # vendor/flecs/flecs.h: 12763

ecs_system_desc_t = struct_ecs_system_desc_t  # vendor/flecs/flecs.h: 12826

ecs_system_t = struct_ecs_system_t  # vendor/flecs/flecs.h: 12888

ecs_gauge_t = struct_ecs_gauge_t  # vendor/flecs/flecs.h: 13099

ecs_counter_t = struct_ecs_counter_t  # vendor/flecs/flecs.h: 13105

ecs_metric_t = union_ecs_metric_t  # vendor/flecs/flecs.h: 13111

ecs_world_stats_t = struct_ecs_world_stats_t  # vendor/flecs/flecs.h: 13219

ecs_query_stats_t = struct_ecs_query_stats_t  # vendor/flecs/flecs.h: 13231

ecs_system_stats_t = struct_ecs_system_stats_t  # vendor/flecs/flecs.h: 13242

ecs_sync_stats_t = struct_ecs_sync_stats_t  # vendor/flecs/flecs.h: 13254

ecs_pipeline_stats_t = struct_ecs_pipeline_stats_t  # vendor/flecs/flecs.h: 13274

EcsMetricValue = struct_EcsMetricValue  # vendor/flecs/flecs.h: 13618

EcsMetricSource = struct_EcsMetricSource  # vendor/flecs/flecs.h: 13623

ecs_metric_desc_t = struct_ecs_metric_desc_t  # vendor/flecs/flecs.h: 13656

EcsAlertInstance = struct_EcsAlertInstance  # vendor/flecs/flecs.h: 13795

EcsAlertsActive = struct_EcsAlertsActive  # vendor/flecs/flecs.h: 13803

ecs_alert_severity_filter_t = (
    struct_ecs_alert_severity_filter_t  # vendor/flecs/flecs.h: 13817
)

ecs_alert_desc_t = struct_ecs_alert_desc_t  # vendor/flecs/flecs.h: 13876

ecs_from_json_desc_t = struct_ecs_from_json_desc_t  # vendor/flecs/flecs.h: 14029

ecs_entity_to_json_desc_t = (
    struct_ecs_entity_to_json_desc_t  # vendor/flecs/flecs.h: 14204
)

ecs_iter_to_json_desc_t = struct_ecs_iter_to_json_desc_t  # vendor/flecs/flecs.h: 14286

ecs_world_to_json_desc_t = (
    struct_ecs_world_to_json_desc_t  # vendor/flecs/flecs.h: 14362
)

ecs_script_template_t = struct_ecs_script_template_t  # vendor/flecs/flecs.h: 14909

ecs_script_var_t = struct_ecs_script_var_t  # vendor/flecs/flecs.h: 14918

ecs_script_vars_t = struct_ecs_script_vars_t  # vendor/flecs/flecs.h: 14921

ecs_script_t = struct_ecs_script_t  # vendor/flecs/flecs.h: 14939

ecs_script_runtime_t = struct_ecs_script_runtime_t  # vendor/flecs/flecs.h: 14942

EcsScript = struct_EcsScript  # vendor/flecs/flecs.h: 14950

ecs_function_ctx_t = struct_ecs_function_ctx_t  # vendor/flecs/flecs.h: 14957

ecs_script_parameter_t = struct_ecs_script_parameter_t  # vendor/flecs/flecs.h: 14970

EcsScriptConstVar = struct_EcsScriptConstVar  # vendor/flecs/flecs.h: 14978

EcsScriptFunction = struct_EcsScriptFunction  # vendor/flecs/flecs.h: 14988

EcsScriptMethod = struct_EcsScriptMethod  # vendor/flecs/flecs.h: 15000

ecs_script_eval_desc_t = struct_ecs_script_eval_desc_t  # vendor/flecs/flecs.h: 15008

ecs_script_desc_t = struct_ecs_script_desc_t  # vendor/flecs/flecs.h: 15154

ecs_expr_eval_desc_t = struct_ecs_expr_eval_desc_t  # vendor/flecs/flecs.h: 15420

ecs_const_var_desc_t = struct_ecs_const_var_desc_t  # vendor/flecs/flecs.h: 15513

ecs_function_desc_t = struct_ecs_function_desc_t  # vendor/flecs/flecs.h: 15551

ecs_expr_node_t = struct_ecs_expr_node_t  # vendor/flecs/flecs.h: 15655

EcsDocDescription = struct_EcsDocDescription  # vendor/flecs/flecs.h: 15753

EcsType = struct_EcsType  # vendor/flecs/flecs.h: 16151

EcsPrimitive = struct_EcsPrimitive  # vendor/flecs/flecs.h: 16179

EcsMember = struct_EcsMember  # vendor/flecs/flecs.h: 16188

ecs_member_value_range_t = (
    struct_ecs_member_value_range_t  # vendor/flecs/flecs.h: 16194
)

EcsMemberRanges = struct_EcsMemberRanges  # vendor/flecs/flecs.h: 16201

ecs_member_t = struct_ecs_member_t  # vendor/flecs/flecs.h: 16244

EcsStruct = struct_EcsStruct  # vendor/flecs/flecs.h: 16250

ecs_enum_constant_t = struct_ecs_enum_constant_t  # vendor/flecs/flecs.h: 16265

EcsEnum = struct_EcsEnum  # vendor/flecs/flecs.h: 16276

ecs_bitmask_constant_t = struct_ecs_bitmask_constant_t  # vendor/flecs/flecs.h: 16291

EcsBitmask = struct_EcsBitmask  # vendor/flecs/flecs.h: 16299

EcsArray = struct_EcsArray  # vendor/flecs/flecs.h: 16305

EcsVector = struct_EcsVector  # vendor/flecs/flecs.h: 16310

ecs_serializer_t = struct_ecs_serializer_t  # vendor/flecs/flecs.h: 16318

EcsOpaque = struct_EcsOpaque  # vendor/flecs/flecs.h: 16470

ecs_unit_translation_t = struct_ecs_unit_translation_t  # vendor/flecs/flecs.h: 16485

EcsUnit = struct_EcsUnit  # vendor/flecs/flecs.h: 16494

EcsUnitPrefix = struct_EcsUnitPrefix  # vendor/flecs/flecs.h: 16500

ecs_meta_type_op_t = struct_ecs_meta_type_op_t  # vendor/flecs/flecs.h: 16556

EcsTypeSerializer = struct_EcsTypeSerializer  # vendor/flecs/flecs.h: 16563

ecs_meta_scope_t = struct_ecs_meta_scope_t  # vendor/flecs/flecs.h: 16589

ecs_meta_cursor_t = struct_ecs_meta_cursor_t  # vendor/flecs/flecs.h: 16602

ecs_primitive_desc_t = struct_ecs_primitive_desc_t  # vendor/flecs/flecs.h: 16955

ecs_enum_desc_t = struct_ecs_enum_desc_t  # vendor/flecs/flecs.h: 16974

ecs_bitmask_desc_t = struct_ecs_bitmask_desc_t  # vendor/flecs/flecs.h: 16992

ecs_array_desc_t = struct_ecs_array_desc_t  # vendor/flecs/flecs.h: 17011

ecs_vector_desc_t = struct_ecs_vector_desc_t  # vendor/flecs/flecs.h: 17029

ecs_struct_desc_t = struct_ecs_struct_desc_t  # vendor/flecs/flecs.h: 17047

ecs_opaque_desc_t = struct_ecs_opaque_desc_t  # vendor/flecs/flecs.h: 17065

ecs_unit_desc_t = struct_ecs_unit_desc_t  # vendor/flecs/flecs.h: 17122

ecs_unit_prefix_desc_t = struct_ecs_unit_prefix_desc_t  # vendor/flecs/flecs.h: 17146

# No inserted files

# No prefix-stripping
