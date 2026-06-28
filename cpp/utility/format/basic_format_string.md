---
title: std::wformat_string
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/basic_format_string
---


```cpp
**Header:** `<`format`>`
dcl|num=1|since=c++20|
template< class CharT, class... Args >
struct basic_format_string;
dcl|num=2|since=c++20|1=
template< class... Args >
using format_string =
basic_format_string<char, std::type_identity_t<Args>...>;
dcl|num=3|since=c++20|1=
template< class... Args >
using wformat_string =
basic_format_string<wchar_t, std::type_identity_t<Args>...>;
```

Class template `std::basic_format_string` wraps a `std::basic_string_view` that will be used by formatting functions.
The constructor of `std::basic_format_string` performs compile-time format string checks<sup>(since C++26)</sup>  unless the constructor argument is returned by `std::dynamic_format`.

## Member functions

member|1=basic_format_string|2=

```cpp
dcl|num=1|
template< class T >
consteval basic_format_string( const T& s );
dcl|num=2|since=c++26|
basic_format_string( /* dynamic-format-string */<CharT> s ) noexcept;
```

1. Constructs a `basic_format_string` object that stores a view of string `s`. If the argument is not a compile-time constant, or if it cannot be parsed as a format string for the formatting argument types `Args`, the construction is ill-formed.
@@ .
2. Constructs a `basic_format_string` object that stores a view of string `s` as returned by `std::dynamic_format`. It does not perform format string checks upon construction.

## Parameters


### Parameters

- `s` - 
member|1=get|2=

```cpp
dcl|1=
constexpr std::basic_string_view<CharT> get() const noexcept;
```

Returns the stored string view.

## Notes

The alias templates `format_string` and `wformat_string` use `std::type_identity_t` to inhibit template argument deduction. Typically, when they appear as a function parameter, their template arguments are deduced from other function arguments.

```cpp
template<class... Args>
std::string format(std::format_string<Args...> fmt, Args&&... args);

auto s = format("{} {}", 1.0, 2);
// Calls format<double, int>. Args are deduced from 1.0, 2
// Due to the use of type_identity_t in format_string, template argument deduction
// does not consider the type of the format string.
```


## Example

