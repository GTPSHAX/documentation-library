---
title: std::type_info::name
type: Utilities
source: https://en.cppreference.com/w/cpp/types/type_info/name
---


```cpp
dcla|anchor=no|noexcept=c++11|1=
const char* name() const;
```

Returns an implementation defined null-terminated character string containing the name of the type. No guarantees are given; in particular, the returned string can be identical for several types and change between invocations of the same program.

## Parameters

(none)

## Return value

containing the name of the type.

## Notes

The lifetime of the array pointed to by the returned pointer is not specified, but in practice it persists as long as the RTTI data structure for the given type exists, which has application lifetime unless loaded from a dynamic library (that can be unloaded).
Some implementations (such as MSVC, IBM, Oracle) produce a human-readable type name. Others, most notably gcc and clang, return the mangled name, which is specified by the [https://itanium-cxx-abi.github.io/cxx-abi/abi.html#typeid Itanium C++ ABI]. The mangled name can be converted to human-readable form using implementation-specific API such as [https://gcc.gnu.org/onlinedocs/libstdc++/manual/ext_demangling.html `abi::__cxa_demangle`] directly or through [https://www.boost.org/doc/libs/release/libs/core/doc/html/core/demangle.html `boost::core::demangle`]. It can also be piped through the command-line utility `c++filt -t`.

## Example


### Example

```cpp
#include <boost/core/demangle.hpp>
#include <cstdlib>
#include <iostream>
#include <string>
#include <typeinfo>

struct Base { virtual ~Base() = default; };
struct Derived : Base {};

int main()
{
    Base b1;
    Derived d1;

    const Base* pb = &b1;
    std::cout << typeid(*pb).name() << '\n';
    pb = &d1;
    std::cout << typeid(*pb).name() << '\n';

    std::string real_name = boost::core::demangle(typeid(pb).name());
    std::cout << typeid(pb).name() << " => " << real_name << '\n';

    std::cout << "c++filt => " << std::flush;
    std::string s = typeid(pb).name();
    std::system(("c++filt -t " + s).data());
}
```


**Output:**
```
// GCC/Clang:
4Base
7Derived
PK4Base => Base const*
c++filt => Base const*

// MSVC:
struct Base
struct Derived
struct Base const * __ptr64 => struct Base const * __ptr64
```


## See also


| cpp/types/type_info/dsc hash_code | (see dedicated page) |

