---
title: Standard Library
type: Standard
source: https://en.cppreference.com/w/cpp/standard_library
---


# C++ Standard Library

The C++ standard library provides a wide range of facilities that are usable in standard C++.

## Category

The language support library provides components that are required by certain parts of the C++ language, such as memory allocation (new/delete) and exception processing.
rrev|since=c++20|
The concepts library describes library components that C++ programs may use to perform compile-time validation of template arguments and perform function dispatch based on properties of types.
The diagnostics library provides a consistent framework for reporting errors in a C++ program, including predefined exception classes.
The memory management library provides components for memory management, including <sup>(since C++11)</sup>  and scoped allocator.
rrev|since=c++11|
The metaprogramming library describes facilities for use in templates and during constant evaluation, including type traits<sup>(since C++14)</sup> ,  and rational arithmetic.
The general utilities library includes components used by other library elements, such as a predefined storage allocator for dynamic storage management, and components used as infrastructure in C++ programs, such as<sup>(since C++11)</sup>   function wrappers.
The s, s<sup>(since C++20)</sup> , , and s libraries provide a C++ program with access to a subset of the most widely used algorithms and data structures.
The strings library provides support for manipulating text represented as homogeneous sequences of following types: `char`<sup>(since C++20)</sup> , `char8_t`<sup>(since C++11)</sup> , `char16_t`, `char32_t`, `wchar_t`, and any other character-like types.
The text processing library provides <sup>(since C++11)</sup> regular expression matching and searching<sup>(since C++20)</sup> , utilities for text formatting<sup>(since C++26)</sup>  and identifying text encodings, and localization facilities.
The numerics library provides  and complex number components that extend support for numeric processing. The  component provides support for n-at-a-time processing, potentially implemented as parallel operations on platforms that support such processing.<sup>(since C++11)</sup>  The random number component provides facilities for generating pseudo-random numbers.
The time library provides generally useful time utilities.
The input/output library provides the iostream components that are the primary mechanism for C++ program input and output. They can be used with other elements of the library, particularly strings, locales, and iterators.
rrev|since=c++11|
The thread support library provides components to create and manage threads, including atomic operations, mutual exclusion, and inter-thread communication.
<p>
rrev|since=c++26|
The execution support library provides a framework for managing asynchronous execution on generic execution resources.

## Library contents

The C++ standard library provides definitions for the entities and macros described in the synopses of the C++ standard library headers, unless otherwise specified.
All library entities except `operator new` and `operator delete` are defined within the namespace `std` or s nested within namespace `std` (except the entities for the C standard library facilities, see below).<sup>(since C++11)</sup>  It is unspecified whether names declared in a specific namespace are declared directly in that namespace or in an inline namespace inside that namespace.

### Headers

Each element of the C++ standard library is declared or defined (as appropriate) in a ''header''. A header is not necessarily a source file, nor are the sequences delimited by **`&lt;`** and **`&gt;`** in header names necessarily valid source file names.
The C++ standard library provides the ''C++ library headers'' and ''additional C++ headers for C library facilities'' (see “” page for descriptions):


| -style="text-align: center; font-size: 16px; line-height: 16px;" |
| colspan="5" | C++ library headers |
| - |
| header | algorithm |
| header | iomanip |
| header | list |
| header | ostream |
| header | streambuf |
| - |
| header | bitset |
| header | ios |
| header | locale |
| header | queue |
| header | string |
| - |
| header | complex |
| header | iosfwd |
| header | map |
| header | set |
| header | typeinfo |
| - |
| header | deque |
| header | iostream |
| header | memory |
| header | sstream |
| header | utility |
| - |
| header | exception |
| header | istream |
| header | new |
| header | stack |
| header | valarray |
| - |
| header | fstream |
| header | iterator |
| header | numeric |
| header | stdexcept |
| header | vector |
| - |
| header | functional |
| header | limits |
|  |
|  |
|  |
| -style="text-align:center" |
| colspan="5" | Headers added in C++11 |
| - |
| header | array |
| header | condition_variable |
| header | mutex |
| header | scoped_allocator |
| header | type_traits |
| - |
| header | atomic |
| header | forward_list |
| header | random |
| header | system_error |
| header | typeindex |
| - |
| header | chrono |
| header | future |
| header | ratio |
| header | thread |
| header | unordered_map |
| - |
| header | codecvt |
| header | initializer_list |
| header | regex |
| header | tuple |
| header | unordered_set |
| -style="text-align:center" |
| colspan="5" | Headers added in C++14 |
| - |
| header | shared_mutex |
|  |
|  |
|  |
|  |
| -style="text-align:center" |
| colspan="5" | Headers added in C++17 |
| - |
| header | any |
| header | execution |
| header | memory_resource |
| header | string_view |
| header | variant |
| - |
| header | charconv |
| header | filesystem |
| header | optional |
|  |
|  |
| -style="text-align:center" |
| colspan="5" | Headers added in C++20 |
| - |
| header | barrier |
| header | concepts |
| header | latch |
| header | semaphore |
| header | stop_token |
| - |
| header | bit |
| header | coroutine |
| header | numbers |
| header | source_location |
| header | syncstream |
| - |
| header | compare |
| header | format |
| header | ranges |
| header | span |
| header | version |
| -style="text-align:center" |
| colspan="5" | Headers added in C++23 |
| - |
| header | expected |
| header | flat_set |
| header | mdspan |
| header | spanstream |
| header | stdfloat |
| - |
| header | flat_map |
| header | generator |
| header | print |
| header | stacktrace |
|  |
| -style="text-align:center" |
| colspan="5" | Headers added in C++26 |
| - |
| header | contracts |
| header | hazard_pointer |
| header | inplace_vector |
| header | rcu |
| header | text_encoding |
| - |
| header | debugging |
| header | hive |
| header | linalg |
| header | simd |
|  |
| -style="text-align:center; font-size:16px; line-height:16px;" |
| colspan="5" | Removed headers |
| - |
| header | codecvt |
| colspan="4" | mark life | since=c++11 | deprecated=c++17 | removed=c++26 |
| - |
| header | strstream |
| colspan="4" | mark life | deprecated=c++98 | removed=c++26 |


| -style="text-align:center; font-size:16px; line-height:16px;" |
| colspan="4" | C++ headers for C library facilities |
| - |
| header | cassert |
| header | clocale |
| header | cstdarg |
| header | cstring |
| - |
| header | cctype |
| header | cmath |
| header | cstddef |
| header | ctime |
| - |
| header | cerrno |
| header | csetjmp |
| header | cstdio |
| header | cwchar |
| - |
| header | cfloat |
| header | csignal |
| header | cstdlib |
| header | cwctype |
| - |
| header | climits |
|  |
|  |
|  |
| -style="text-align:center" |
| colspan="4" | Headers added in C++11 |
| - |
| header | cfenv |
| header | cinttypes |
| header | cstdint |
| header | cuchar |
| -style="text-align:center; font-size:16px; line-height:16px;" |
| colspan="5" | Removed headers |
| - |
| header | ccomplex |
| colspan="4" | mark life | since=c++11 | deprecated=c++17 | removed=c++20 |
| - |
| header | ciso646 |
| colspan="4" | mark until c++20 | removed=yes |
| - |
| header | cstdalign |
| colspan="4" | mark life | since=c++11 | deprecated=c++17 | removed=c++20 |
| - |
| header | cstdbool |
| colspan="4" | mark life | since=c++11 | deprecated=c++17 | removed=c++20 |
| - |
| header | ctgmath |
| colspan="4" | mark life | since=c++11 | deprecated=c++17 | removed=c++20 |

A freestanding implementation has an implementation-defined set of headers, see here for the minimal requirement on the set of headers.

## C standard library

The C++ standard library also makes available the facilities of the C standard library, suitably adjusted to ensure static type safety. The descriptions of many library functions rely on the C standard library for the semantics of those functions.
In some cases, the signatures specified in standard C++ may be different from the signatures in the C standard library, and additional overloads may be declared, but the behavior and the preconditions <sup>(since C++17)</sup> (including those implied by C's `restrict`) are the same unless otherwise stated.
For compatibility with the C standard library, the C++ standard library provides the C headers listed below. The intended use of these headers is for interoperability only. It is possible that C++ source files need to include one of these headers in order to be valid ISO C. Source files that are not intended to also be valid ISO C should not use any of the C headers. See here for descriptions.


| -style="text-align:center; font-size:16px; line-height:16px;" |
| colspan="4" | C headers |
| - |
| ltt | cpp/header/cassert | <assert.h> |
| ltt | cpp/header/climits | <limits.h> |
| ltt | cpp/header/cstdarg | <stdarg.h> |
| ltt | cpp/header/cstring | <string.h> |
| - |
| ltt | cpp/header/cctype | <ctype.h> |
| ltt | cpp/header/clocale | <locale.h> |
| ltt | cpp/header/cstddef | <stddef.h> |
| ltt | cpp/header/ctime | &lt;time.h> |
| - |
| ltt | cpp/header/cerrno | <errno.h> |
| ltt | cpp/header/cmath | <math.h> |
| ltt | cpp/header/cstdio | <stdio.h> |
| ltt | cpp/header/cwchar | <wchar.h> |
| - |
| ltt | cpp/header/cfloat | <float.h> |
| ltt | cpp/header/csetjmp | <setjmp.h> |
| ltt | cpp/header/cstdlib | <stdlib.h> |
| ltt | cpp/header/cwctype | <wctype.h> |
| - |
| ltt | cpp/header/ciso646 | <iso646.h> |
| ltt | cpp/header/csignal | <signal.h> |
|  |
|  |
| -style="text-align:center" |
| colspan="4" | Headers added in C++11 |
| - |
| ltt | cpp/header/ccomplex | <complex.h> |
| ltt | cpp/header/cinttypes | <inttypes.h> |
| ltt | cpp/header/cstdbool | <stdbool.h> |
| ltt | cpp/header/ctgmath | <tgmath.h> |
| - |
| ltt | cpp/header/cfenv | <fenv.h> |
| ltt | cpp/header/cstdalign | <stdalign.h> |
| ltt | cpp/header/cstdint | <stdint.h> |
| ltt | cpp/header/cuchar | <uchar.h> |
| -style="text-align:center" |
| colspan="4" | Headers added in C++23 |
| - |
| ltt | cpp/header/stdatomic.h | <stdatomic.h> |
|  |
|  |
|  |
| -style="text-align:center" |
| colspan="4" | Headers added in C++26 |
| - |
| ltt | cpp/header/stdbit.h | <stdbit.h> |
| ltt | cpp/header/stdckdint.h | <stdckdint.h> |
|  |
|  |

Except otherwise noted, the contents of each header `c''xxx''` is the same as that of the corresponding header `''xxx''.h` as specified in the C standard library. In the C++ standard library, however, the declarations (except for names which are defined as macros in C) are within namespace scope of the namespace `std`. It is unspecified whether these names (including any overloads added) are first declared within the global namespace scope and are then injected into namespace `std` by explicit .
Names which are defined as macros in C (`cpp/error/assert`, `cpp/types/offsetof`, `cpp/utility/program/setjmp`, `cpp/utility/variadic/va_arg`, `cpp/utility/variadic/va_end` and `cpp/utility/variadic/va_start`) must be defined as macros in the C++ standard library, even if C grants license for implementation as functions.
Names that are defined as functions in C must be defined as functions in the C++ standard library. This disallows the practice, allowed in C, of providing a masking macro in addition to the function prototype. The only way to achieve equivalent inline behavior in C++ is to provide a definition as an extern inline function.
Identifiers that are keywords or operators in C++ cannot be defined as macros in C++ standard library headers. In particular, including the standard header `cpp/header/ciso646|<iso646.h>` has no effect.

### Names associated with safe functions in standard C <sup>(C++17)</sup>

If any C++ header is included, it is implementation-defined whether any of the following C standard Annex K names is declared in the global namespace (none of them is declared in namespace `std`):


| -style="text-align:center" |
| colspan="4" | C standard Annex K names |
| - |
| ltt | c/error/abort_handler_s |
| ltt | c/string/multibyte/mbstowcs | mbstowcs_s |
| ltt | c/string/byte/strncat | strncat_s |
| ltt | c/io/vfwscanf | vswscanf_s |
| - |
| ltt | c/chrono/asctime | asctime_s |
| ltt | c/string/byte/memcpy | memcpy_s |
| ltt | c/string/byte/strncpy | strncpy_s |
| ltt | c/io/vfwprintf | vwprintf_s |
| - |
| ltt | c/algorithm/bsearch | bsearch_s |
| ltt | c/string/byte/memmove | memmove_s |
| ltt | c/string/byte/strtok | strtok_s |
| ltt | c/io/vfwscanf | vwscanf_s |
| - |
| ltt | c/error/set_constraint_handler_s | constraint_handler_t |
| ltt | c/string/byte/memset | memset_s |
| ltt | c/io/fwprintf | swprintf_s |
| ltt | c/string/multibyte/wcrtomb | wcrtomb_s |
| - |
| ltt | c/chrono/ctime | ctime_s |
| ltt | c/io/fprintf | printf_s |
| ltt | c/io/fwscanf | swscanf_s |
| ltt | c/string/wide/wcscat | wcscat_s |
| - |
| ltt | c/error | errno_t |
| ltt | c/algorithm/qsort | qsort_s |
| ltt | c/io/tmpfile | tmpfile_s |
| ltt | c/string/wide/wcscpy | wcscpy_s |
| - |
| ltt | c/io/fopen | fopen_s |
| ltt | c/error | RSIZE_MAX |
| ltt | c/io/tmpnam | TMP_MAX_S |
| ltt | c/string/wide/wcsncat | wcsncat_s |
| - |
| ltt | c/io/fprintf | fprintf_s |
| ltt | c/error | rsize_t |
| ltt | c/io/tmpnam | tmpnam_s |
| ltt | c/string/wide/wcsncpy | wcsncpy_s |
| - |
| ltt | c/io/freopen | freopen_s |
| ltt | c/io/fscanf | scanf_s |
| ltt | c/io/vfprintf | vfprintf_s |
| ltt | c/string/wide/wcslen | wcsnlen_s |
| - |
| ltt | c/io/fscanf | fscanf_s |
| ltt | c/error/set_constraint_handler_s |
| ltt | c/io/vfscanf | vfscanf_s |
| ltt | c/string/multibyte/wcsrtombs | wcsrtombs_s |
| - |
| ltt | c/io/fwprintf | fwprintf_s |
| ltt | c/io/fprintf | snprintf_s |
| ltt | c/io/vfwprintf | vfwprintf_s |
| ltt | c/string/wide/wcstok | wcstok_s |
| - |
| ltt | c/io/fwscanf | fwscanf_s |
| ltt | c/io/fwprintf | snwprintf_s |
| ltt | c/io/vfwscanf | vfwscanf_s |
| ltt | c/string/multibyte/wcstombs | wcstombs_s |
| - |
| ltt | c/io/gets | gets_s |
| ltt | c/io/fscanf | sscanf_s |
| ltt | c/io/vfprintf | vprintf_s |
| ltt | c/string/wide/wmemcpy | wmemcpy_s |
| - |
| ltt | c/chrono/gmtime | gmtime_s |
| ltt | c/string/multibyte/mbstowcs | mbstowcs_s |
| ltt | c/io/vfscanf | vscanf_s |
| ltt | c/io/vfwscanf | vswscanf_s |
| - |
| ltt | c/error/abort_handler_s |
| ltt | c/string/byte/strcat | strcat_s |
| ltt | c/io/vfprintf | vsnprintf_s |
| ltt | c/string/wide | wmemmove | wmemmove_s |
| - |
| ltt | c/error/ignore_handler_s |
| ltt | c/string/byte/strcpy | strcpy_s |
| ltt | c/io/vfwprintf | vsnwprintf_s |
| ltt | c/io/fwprintf | wprintf_s |
| - |
| ltt | c/chrono/localtime | localtime_s |
| ltt | c/string/byte/strerror | strerrorlen_s |
| ltt | c/io/vfprintf | vsprintf_s |
| ltt | c/io/fwscanf | wscanf_s |
| - |
| ltt | c/io/tmpnam | L_tmpnam_s |
| ltt | c/string/byte/strerror | strerror_s |
| ltt | c/io/vfscanf | vsscanf_s |
|  |
| - |
| ltt | c/string/multibyte/mbsrtowcs | mbsrtowcs_s |
| ltt | c/string/byte/strlen | strlen_s |
| ltt | c/io/vfwprintf | vswprintf_s |
|  |


## Using the library


### Including headers

The entities in the C++ standard library are defined in headers, whose contents are made available to a translation unit when it contains the appropriate `cpp/preprocessor/include|#include` preprocessing directive.
A translation unit may include library headers in any order. Each may be included more than once, with no effect different from being included exactly once, except that the effect of including either  or `cpp/header/cassert|<assert.h>` depends each time on the lexically current definition of `NDEBUG`.
A translation unit can only include a header outside of any declaration or definition, and lexically before the first reference in that translation unit to any of the entities declared in that header. No diagnostic is required.
rrev|since=c++20|
In module units, headers can only be included in s.
rev|since=c++20|

### Importing headers

The C++ library headers, or, for a freestanding implementation, the subset of such headers that are provided by the implementation, are collectively known as the ''importable C++ library headers''.
The contents of importable C++ library headers are made available to a translation unit when it contains the appropriate import declaration.
rev|since=c++23|

### Importing modules

The C++ standard library provides the following ''C++ library modules'':
* The named module `std` exports declarations in namespace `std` that are provided by the importable C++ library headers (e.g. `std::rotr` from ) and the C++ headers for C library facilities (e.g. `std::puts` from ). It additionally exports declarations in the global namespace for the storage allocation and deallocation functions that are provided by  (e.g. `operator new|::operator new`).
* The named module `std.compat` exports the same declarations as the named module `std`, and additionally exports declarations in the global namespace corresponding to the declarations in namespace `std` that are provided by the C++ headers for C library facilities (e.g. `std::fclose|::fclose`).
For each declaration in the standard library,
* the module it attaches to is unspecified, and
* it denotes the same entity regardless of whether it was made reachable through including a header, importing a header unit, or importing a C++ library module.

### Linkage

Entities in the C++ standard library have . Unless otherwise specified, objects and functions have the default `extern "C++"` linkage.
Whether a name from the C standard library declared with external linkage has `extern "C"` or `extern "C++"` linkage is implementation-defined. The C++ standard recommends using `extern "C++"` in this case.
Objects and functions defined in the library and required by a C++ program are included in the program prior to program startup.

## Requirements on standard library implementations


### Guarantees

A C++ header must provide  and s that appear in
* the synopsis of that header, or
* the synopsis of another header which is appeared to be included in the synopsis of that header.
For types and macros defined in multiple headers (such as `cpp/types/NULL`), including any number of these headers in any order never violates the one definition rule.
Unless otherwise specified, all  defined by the C standard library that expand to integral s can be used in `#if` preprocessing directives.
Calling a standard library non-member function signature always results in actually calling that function. Therefore a conforming standard library implementation cannot define additional non-member functions that may be called by a valid C++ program.
Non-member function signatures are never declared with additional .
Unless otherwise specified, calls made by functions in the standard library to non-operator, non-member functions do not use functions from another  which are found through argument-dependent name lookup.
For each friend declaration of a function (template) within a class (template) definition, no other declaration is provided for that function (template).
rrev|since=c++11|1=
Standard library function signatures can only be declared as `constexpr` if they are required to be  (libstdc++ cmath [https://gcc.gnu.org/bugzilla/show_bug.cgi?id=102916 is notably non-conforming] here). If a header provides any non-defining declarations of constexpr functions or constructors, the corresponding definitions should also be provided within that header.
Unless otherwise specified, each standard library function should meet each of the following requirements to prevent data races:
* A C++ standard library function cannot (directly or indirectly) access objects accessible by threads other than the current thread unless the objects are accessed (directly or indirectly) via the function’s arguments, including `this`.
* A C++ standard library function cannot (directly or indirectly) modify objects accessible by threads other than the current thread unless the objects are accessed (directly or indirectly) via the function’s non-const arguments, including `this`.
** For example, an object with static storage duration cannot be used for internal purposes without synchronization because doing so can cause a data race even in programs that do not explicitly share objects between threads.
* A C++ standard library function cannot access objects indirectly accessible via its arguments or via elements of its  arguments except by invoking functions required by its specification on those container elements.
* An operation on s obtained by calling a standard library container or string member function can access, but not modify, the underlying container.
** In particular, container operations that invalidate iterators conflict with operations on iterators associated with that container.
* A C++ standard library function can only perform all operations solely within the current thread if those operations have effects that are visible to users.
** Operations without visible side effects can be parallelized.
For each class defined in the C++ standard library required to be derived from another class defined in the C++ standard library,
* the base class must be virtual if it is specified as `virtual`,
* the base class cannot be virtual if it is not specified as `virtual`, and
* unless otherwise specified, types with distinct names shall be distinct types.
rrev|since=c++11|
Unless otherwise specified, all types specified in the C++ standard library are non- types.
If a function defined in the C++ standard library is specified to throw an exception (in a particular situation) of a given type, the exception thrown can only have that type or a type derived from that type so that an exception handler for the base type can catch it.
Functions from the C standard library can only throw exceptions when such a function calls a program-supplied function that throws an exception ( and  meet this condition).
Destructor operations defined in the C++ standard library never throw exceptions. Every destructor in the C++ standard library behaves as if it had a non-throwing exception specification.
rrev|since=c++11|
If a function in the C++ standard library report errors via a `std::error_code` object, that object's  member must return `std::system_category()` for errors originating from the operating system, or a reference to an implementation-defined `std::error_category` object for errors originating elsewhere. The possible values of  for each of these error categories should be defined.
Objects of types defined in the C++ standard library may be moved from. Move operations can either be explicitly specified or implicitly generated. Unless otherwise specified, such moved-from objects will be placed in a valid but unspecified state.
An object of a type defined in the C++ standard library may be move-assigned to itself. Unless otherwise specified, such an assignment places the object in a valid but unspecified state.

### Implementation freedom

It is unspecified whether any member or non-member functions in the C++ standard library are defined as .
For a non- C++ standard library member function, a different set of member function signatures can be declared, provided that any call to that member function that would select an overload from the given set of declarations behaves as if that overload was selected. This allows, for instance:
* adding parameters with default arguments,
* replacing a member function with default arguments with two or more member functions with equivalent behavior, or
* adding additional signatures for a member function name.
Unless otherwise specified, it is implementation-defined which functions in the C++ standard library may be recursively reentered.
rrev|since=c++11|
C++ standard library implementations can share their own internal objects between threads if the objects are not visible to users and are protected against data races.
It is unspecified whether any function signature or class in the C++ standard library is a friend of another class in the C++ standard library.
The names and global function signatures described here are reserved to the implementation.
Any class in the C++ standard library can be derived from a class with a name reserved to the implementation. If a class defined in the C++ standard library is required to be derived from other classes in the C++ standard library, that class can be derived directly from the required base or indirectly through a hierarchy of base classes with names reserved to the implementation.
If a function defined in the C++ standard library is not specified to throw an exception but does not have a non-throwing exception specification, the exception thrown is implementation-defined, but its type should be `std::exception` or any type derived from `std::exception`.
The exception specification for a non-virtual function can be strengthened by adding a non-throwing exception specification.
rrev|since=c++26|1=

## Standard library hardening

An implementation can be a , whether the implementation is hardened is implementation-defined.
Some standard library functions (and function templates) have . When such a function is invoked:
* If the implementation is hardened, prior to any other observable side effects of the function, contract assertions whose predicates are as described in the hardened precondition are evaluated with a terminating semantic.
* If the implementation is not hardened, when a hardened precondition is violated, the behavior is undefined.

### Functions with hardened preconditions

<div style="max-width: 668px; max-height: 80vh; overflow: auto;">
</div>

## Notes


## Example


### Example

```cpp
import std;

struct Str : std::string // OK, std::string cannot be final
{
    ~Str(); // Guaranteed to be noexcept
};

int main()
{
    std::puts("Hello stdlib!");
    // ::puts("Hello stdlib!"); // Requires std.compat module or stdio.h header

    // constexpr auto& void_info = std::any().type(); // any::type cannot be constexpr

    std::string p, q;
    q = std::move(p); // OK, p is left in a valid (but unspecified) state
                      // This includes self move assignment q = std::move(q)

    // return EXIT_SUCCESS; // Macro EXIT_SUCCESS is not provided by either stdlib module
}
```


**Output:**
```
Hello stdlib!
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-1 | C++98 | the language linkages of the names from<br>the C standard library were unspecified | they are<br>implementation-defined |
| lwg-119 | C++98 | the exception specifications of virtual<br>functions could be strengthened | only allowed for<br>non-virtual functions |
| lwg-147 | C++98 | the specification on non-member<br>functions only considered global functions | also considers<br>non-global functions |
| lwg-225 | C++98 | standard library functions might call non-member functions<br>from other namespaces due to argument-dependent lookup | prohibited unless<br>otherwise specified |
| lwg-343 | C++98 | library header dependencies were not specified | specified (listed in synopses) |
| lwg-1178 | C++98 | C++ headers must include a C++ header<br>that contains any needed definition | C++ headers must provide declarations<br>and definitions that are directly or<br>indirectly included in its synopsis |
| lwg-2225 | C++98 | a diagnostic was required if a header<br>is included at an incorrect position | no diagnostic is<br>required in this case |

