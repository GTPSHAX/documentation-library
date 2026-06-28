---
title: std::basic_format_arg
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/basic_format_arg
---

ddcl|header = format|since=c++20|1=
template< class Context >
class basic_format_arg;
Provides access to a formatting argument.
`basic_format_arg` objects are typically created by `std::make_format_args` and accessed through `std::visit_format_arg`<sup>(since C++26)</sup>  or the `visit` member functions.
A `basic_format_arg` object behaves as if it stores a `std::variant` of the following types:
* `std::monostate` (only if the object was default-constructed)
* `bool`
* `Context::char_type`
* `int`
* `unsigned int`
* `long long int`
* `unsigned long long int`
* `float`
* `double`
* `long double`
* `const Context::char_type*`
* `std::basic_string_view<Context::char_type>`
* `const void*`
* `basic_format_arg::handle`

## Member classes


## Member functions


## Non-member functions


| cpp/utility/format/dsc visit_format_arg | (see dedicated page) |

member|basic_format_arg|2=
ddcl|since=c++20|
basic_format_arg() noexcept;
Default constructor. Constructs a `basic_format_arg` that does not hold a formatting argument. The stored object has type `std::monostate`.
To create a `basic_format_arg` that holds a formatting argument, `std::make_format_args` has to be used.
member|operator bool|2=
ddcl|since=c++20|
explicit operator bool() const noexcept;
Checks whether `*this` holds a formatting argument.
Returns `true` if `*this` holds a formatting argument (i.e. the stored object does not have type `std::monostate`), `false` otherwise.
member|visit|2=

```cpp
dcl|num=1|since=c++26|
template< class Visitor >
decltype(auto) visit( this basic_format_arg arg, Visitor&& vis );
dcl|num=2|since=c++26|
template< class R, class Visitor >
R visit( this basic_format_arg arg, Visitor&& vis );
```

Applies the visitor `vis` to the object contained in `arg`.
The `visit` functions do not modify the `basic_format_arg` object on which it is called because a copy of the object is used when calling `vis`.
1. Equivalent to `return std::visit(std::forward<Visitor>(vis), v);`, where `v` is the `std::variant` stored in `arg`.
2. Equivalent to `return std::visit<R>(std::forward<Visitor>(vis), v);`, where `v` is the `std::variant` stored in `arg`.

## Notes


## Example


## See also


| cpp/utility/format/dsc basic_format_args | (see dedicated page) |

