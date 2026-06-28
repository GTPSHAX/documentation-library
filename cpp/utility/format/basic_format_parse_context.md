---
title: std::basic_format_parse_context
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/basic_format_parse_context
---


```cpp
**Header:** `<`format`>`
dcl|since=c++20|
template< class CharT >
class basic_format_parse_context;
```

Provides access to the format string parsing state consisting of the format string range being parsed and the argument counter for automatic indexing.
A `std::basic_format_parse_context` instance is passed to *Formatter* when parsing the format specification.
A program that declares an explicit or partial specialization of `std::basic_format_parse_context` is ill-formed, no diagnostic required.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions

member|basic_format_parse_context|2=

```cpp
dcl rev multi|num=1|until1=c++26|dcl1=
constexpr explicit
basic_format_parse_context( std::basic_string_view<CharT> fmt,
std::size_t num_args = 0 ) noexcept;
|since2=c++26|dcl2=
constexpr explicit
basic_format_parse_context( std::basic_string_view<CharT> fmt ) noexcept;
dcl|num=2|1=
basic_format_parse_context( const basic_format_parse_context& ) = delete;
```

1. Constructs a `std::basic_format_parse_context` instance. Initializes the format string range to [fmt.begin(), fmt.end()), and the argument count to <sup>(until C++26)</sup> `num_args`<sup>(since C++26)</sup> `0`.
<sup>(since C++26)</sup> Any call to `next_arg_id`, `check_arg_id`, or `check_dynamic_spec` on an instance of `std::basic_format_parse_context` initialized using this constructor is not a core constant expression.
2. The copy constructor is deleted. `std::basic_format_parse_context` is not copyable.
member|begin|2=
ddcl|
constexpr const_iterator begin() const noexcept;
Returns an iterator to the beginning of the format string range.
member|end|2=
ddcl|
constexpr const_iterator end() const noexcept;
Returns an iterator to the end of the format string range.
member|advance_to|2=
ddcl|
constexpr void advance_to( const_iterator it );
Sets the beginning of the format string range to `it`. After a call to `advance_to()`, subsequent calls to `begin()` will return a copy of `it`.
The behavior is undefined if `end()` is not reachable from `it`.
member|next_arg_id|2=
ddcl|
constexpr std::size_t next_arg_id();
Enters automatic argument indexing mode, and returns the next argument index, starting from 0.
If `*this` has already entered manual argument indexing mode, throws `std::format_error`.
If the next argument index is larger than or equal to the `num_args` provided in the constructor, the call is not a core constant expression.
member|check_arg_id|2=
ddcl|
constexpr void check_arg_id( std::size_t id );
Enters manual argument indexing mode.
If `*this` has already entered automatic argument indexing mode, throws `std::format_error`.
If `id` is larger than or equal to the `num_args` provided in the constructor, the call is not a core constant expression.
member|check_dynamic_spec|2=
ddcl|since=c++26|
template< class... Ts >
constexpr void check_dynamic_spec( std::size_t id ) noexcept;
If `id` is larger than or equal to the `num_args` provided in the constructor or the type of the corresponding format argument (after conversion to `std::basic_format_arg`) is not one of the types in `Ts...`, the call is not a core constant expression. A call to `check_dynamic_spec` has no effect at runtime.
The program is ill-formed unless `1=sizeof...(Ts) >= 1`, the types in `Ts...` are unique, and each type is one of `bool`, `char_type`, `int`, `unsigned int`, `long long int`, `unsigned long long int`, `float`, `double`, `long double`, `const char_type*`, `std::basic_string_view<char_type>`, or `const void*`.
member|check_dynamic_spec_integral|2=
ddcl|since=c++26|
constexpr void check_dynamic_spec_integral( std::size_t id ) noexcept;
Equivalent to call `check_dynamic_spec<int, unsigned int, long long int, unsigned long long int>(id)`. A call to `check_dynamic_spec_integral` has no effect at runtime.
member|check_dynamic_spec_string|2=
ddcl|since=c++26|
constexpr void check_dynamic_spec_string( std::size_t id ) noexcept;
Equivalent to call `check_dynamic_spec<const char_type*, std::basic_string_view<char_type>>(id)`. A call to `check_dynamic_spec_string` has no effect at runtime.

## Example


## Defect reports

