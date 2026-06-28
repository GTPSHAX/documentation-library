---
title: std::basic_format_args
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/basic_format_args
---


```cpp
**Header:** `<`format`>`
dcl|num=1|since=c++20|1=
template< class Context >
class basic_format_args;
dcl|num=2|since=c++20|1=
using format_args = basic_format_args<std::format_context>;
dcl|num=3|since=c++20|1=
using wformat_args = basic_format_args<std::wformat_context>;
```

Provides access to formatting arguments.

## Member functions

member|basic_format_args|2=

```cpp
dcl|1=
template< class... Args >
basic_format_args( const /*format-arg-store*/<Context, Args...>& store ) noexcept;
```

Constructs a `basic_format_args` object from the result of a call to `std::make_format_args` or `std::make_wformat_args`.
member|get|2=
ddcl|1=
std::basic_format_arg<Context> get( std::size_t i ) const noexcept;
Returns a `std::basic_format_arg` holding the `i`-th argument in `args`, where `args` is the parameter pack passed to `std::make_format_args` or `std::make_wformat_args`.
If there's no such formatting argument (i.e. `*this` was default-constructed or `i` is not less than the number of formatting arguments), returns a default-constructed `std::basic_format_arg` (holding a `std::monostate` object).

## Deduction guides

ddcl|since=c++20|
template< class Context, class... Args >
basic_format_args( /*format-arg-store*/<Context, Args...> ) -> basic_format_args<Context>;

## Notes

`std::basic_format_args` has reference semantics. It is the programmer's responsibility to ensure that `*this` does not outlive `store` (which, in turn, should not outlive the arguments to `std::make_format_args` or `std::make_wformat_args`).

## Example


## See also


| cpp/utility/format/dsc basic_format_arg | (see dedicated page) |

