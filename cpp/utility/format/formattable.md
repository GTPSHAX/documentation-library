---
title: std::formattable
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/formattable
---


```cpp
**Header:** `<`format`>`
dcl|num=1|since=c++23|1=
template< class T, class CharT >
concept formattable = /* formattable_with */<
std::remove_reference_t<T>,
std::basic_format_context</* fmt_iter_for */<CharT>, CharT>
>;
|1=
template< class CharT >
using /* fmt_iter_for */ = /* unspecified */;
|1=
template< class T, class Context,
class Formatter =
typename Context::template
formatter_type<std::remove_const_t<T>> >
concept /* formattable_with */ =
std::semiregular<Formatter> &&
requires (Formatter& f, const Formatter& cf, T&& t, Context fc,
std::basic_format_parse_context<
typename Context::char_type
> pc) {
{ f.parse(pc) } -> std::same_as<typename decltype(pc)::iterator>;
{ cf.format(t, fc) } -> std::same_as<typename Context::iterator>;
};
```

The concept `formattable` specifies that `std::formatter<std::remove_cvref_t<T>, CharT>` meets the requirements of *BasicFormatter* and *Formatter* (if `std::remove_reference_t<T>` is const-qualified).
The exposition-only alias template `/* fmt_iter_for */` yields an unspecified type that satisfies `std::output_iterator<const CharT&>`.

## Defect reports


## See also


| cpp/utility/format/dsc formatter | (see dedicated page) |

