---
title: Extending the namespace std
type: Language
source: https://en.cppreference.com/w/cpp/language/extending_std
---


# Extending the namespace tt|std


## Adding declarations to `std`

It is undefined behavior to add declarations or definitions to namespace `std` or to any namespace nested within `std`, with a few exceptions noted below.

```cpp
#include <utility>

namespace std
{
    // a function definition added to namespace std: undefined behavior
    pair<int, int> operator+(pair<int, int> a, pair<int, int> b)
    {
        return {a.first + b.first, a.second + b.second};
    }
}
```


## Adding template specializations


### Class templates

It is allowed to add template specializations for any standard library class template to the namespace `std` only if the declaration depends on at least one  and the specialization satisfies all requirements for the original template, except where such specializations are prohibited.

```cpp
// Get the declaration of the primary std::hash template.
// We are not permitted to declare it ourselves.
// <typeindex> is guaranteed to provide such a declaration, 
// and is much cheaper to include than <functional>.

#include <typeindex> 

// Specialize std::hash so that MyType can be used as a key in 
// std::unordered_set and std::unordered_map.  Opening namespace
// std can accidentally introduce undefined behavior, and is not
// necessary for specializing class templates.
template<>
struct std::hash<MyType>
{
    std::size_t operator()(const MyType& t) const { return t.hash(); }
};
```

* Specializing the template `std::complex` for any type other than `float`, `double`, and `long double` is unspecified.
* Specializations of `std::numeric_limits` must define all members declared <sup>(until C++11)</sup> `static const`<sup>(since C++11)</sup> `static constexpr` in the primary template, in such a way that they are usable as `integral constant expressions`.
rrev|since=c++11|
* None of the templates defined in  may be specialized for a , except for `std::common_type`<sup>(since C++20)</sup>  and `cpp/types/common_reference#Helper types|std::basic_common_reference`. This includes the type traits and the class template `std::integral_constant`.
* Specializations of `std::hash` for program-defined types must satisfy *Hash* requirements.
* Specializations of `std::atomic` must have a deleted copy constructor, a deleted copy assignment operator, and a constexpr value constructor.
* Specializations of `std::shared_ptr` and `std::weak_ptr` must be *CopyConstructible* and *CopyAssignable*. In addition, specializations of `std::shared_ptr` must be *LessThanComparable*, and convertible to `bool`.
* Specializations of `std::istreambuf_iterator` must have a trivial copy constructor, a constexpr default constructor, and a trivial destructor.
rrev|until=c++17|
* `std::unary_function` and `std::binary_function` may not be specialized.
It is undefined behavior to declare a full or partial specialization of any member class template of a standard library class or class template.

### Function templates and member functions of templates

rrev multi|until1=c++20
|rev1=
It is allowed to add template specializations for any standard library function template to the namespace `std` only if the declaration depends on at least one  and the specialization satisfies all requirements for the original template, except where such specializations are prohibited.
|rev2=
It is undefined behavior to declare a full specialization of any standard library function template.
It is undefined behavior to declare a full specialization of any member function of a standard library class template:
It is undefined behavior to declare a full specialization of any member function template of a standard library class or class template:

### Variable templates

rrev|since=c++14|
It is undefined behavior to declare a full or partial specialization of any standard library variable template, except where explicitly allowed.
rrev|since=c++20|
* Specializations of `std::sized_sentinel_for|std::disable_sized_sentinel_for`, `std::ranges::sized_range|std::ranges::disable_sized_range`, `std::ranges::view|std::ranges::enable_view` and `std::ranges::borrowed_range|std::ranges::enable_borrowed_range` shall be usable in constant expressions and have type `const bool`. And
** `std::disable_sized_sentinel_for` may be specialized for cv-unqualified non-array object types `S` and `I` at least one of which is a .
** `std::ranges::disable_sized_range`, `std::ranges::enable_view` and `std::ranges::enable_borrowed_range` may be specialized for cv-unqualified program-defined types.
* Every mathematical constant variable template may be partially or explicitly specialized, provided that the specialization depends on a program-defined type.

## Explicit instantiation of templates

It is allowed to explicitly instantiate a <sup>(since C++20)</sup> class template defined in the standard library only if the declaration depends on the name of at least one  and the instantiation meets the standard library requirements for the original template.

## Other restrictions

The namespace `std` may not be declared as an `inline namespace`.
rrev|since=c++20|

### Addressing restriction

The behavior of a C++ program is unspecified (possibly ill-formed) if it explicitly or implicitly attempts to form a pointer, reference (for free functions and static member functions) or pointer-to-member (for non-static member functions) to a standard library function or an instantiation of a standard library function template, unless it is designated an ''addressable function'' (see below).
Following code was well-defined in C++17, but leads to unspecified behaviors and possibly fails to compile since C++20:

```cpp
#include <cmath>
#include <memory>

int main()
{
    // by unary operator&
    auto fptr0 = &static_cast<float(&)(float, float)>(std::betaf);

    // by std::addressof
    auto fptr1 = std::addressof(static_cast<float(&)(float, float)>(std::betaf));

    // by function-to-pointer implicit conversion
    auto fptr2 = static_cast<float(&)(float)>(std::riemann_zetaf);

    // forming a reference
    auto& fref = static_cast<float(&)(float)>(std::riemann_zetaf);
}
```


### Designated addressable functions

* I/O manipulators:
** `fmtflags` manipulators:
*** `std::boolalpha`
*** `std::boolalpha|std::noboolalpha`
*** `std::showbase`
*** `std::showbase|std::noshowbase`
*** `std::showpoint`
*** `std::showpoint|std::noshowpoint`
*** `std::showpos`
*** `std::showpos|std::noshowpos`
*** `std::skipws`
*** `std::skipws|std::noskipws`
*** `std::uppercase`
*** `std::uppercase|std::nouppercase`
*** `std::unitbuf`
*** `std::unitbuf|std::nounitbuf`
** `adjustfield` manipulators:
*** `std::left|std::internal`
*** `std::left`
*** `std::left|std::right`
** `basefield` manipulators:
*** `std::hex|std::dec`
*** `std::hex`
*** `std::hex|std::oct`
** `floatfield` manipulators:
*** `std::fixed`
*** `std::fixed|std::scientific`
*** `std::fixed|std::hexfloat`
*** `std::fixed|std::defaultfloat`
** `basic_istream` manipulators:
*** `std::ws`
** `basic_ostream` manipulators:
*** `std::endl`
*** `std::ends`
*** `std::flush`
<!-- Mapping not established yet
*** `std::emit_on_flush`
*** `std::emit_on_flush|std::noemit_on_flush`
*** `std::flush_emit`
-->
*** `cpp/io/manip/emit_on_flush|std::emit_on_flush`
*** `cpp/io/manip/emit_on_flush|std::noemit_on_flush`
*** `cpp/io/manip/flush_emit|std::flush_emit`

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-120 | C++98 | users could explicitly instantiate standard<br>library templates for non-user defined types | prohibited |
| lwg-232 | C++98 | users could explicitly specialize standard library templates<br>if the declaration depends on a user-defined name of<br>external linkage (which can refer to a non-user-defined type) | only allowed for<br>user-defined types |
| lwg-422 | C++98 | users could specialize individual members or member templates<br>without specializing the whole standard library class or class template | the behavior is<br>undefined in this case |

