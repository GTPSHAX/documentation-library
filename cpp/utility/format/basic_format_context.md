---
title: std::basic_format_context
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/basic_format_context
---


```cpp
**Header:** `<`format`>`
dcl|num=1|since=c++20|1=
template< class OutputIt, class CharT >
class basic_format_context;
dcl|num=2|since=c++20|1=
using format_context = basic_format_context</* unspecified */, char>;
dcl|num=3|since=c++20|1=
using wformat_context = basic_format_context</* unspecified */, wchar_t>;
```

Provides access to formatting state consisting of the formatting arguments and the output iterator.
2. The unspecified template argument is an output iterator that appends to `std::string`, such as `std::back_insert_iterator<std::string>`. Implementations typically use an iterator to type-erased buffer type that supports appending to any contiguous and resizable container.
3. The unspecified template argument is an output iterator that appends to `std::wstring`.
The behavior is undefined if `OutputIt` does not model `std::output_iterator<const CharT&>`.
A program that declares an explicit or partial specialization of `std::basic_format_context` is ill-formed, no diagnostic required.
`std::basic_format_context` objects can only be created by the implementation. User codes are only allowed to modify the format context via the `format` function of `std::formatter` specializations.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member alias templates


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions

member|arg|2=
ddcl|1=
std::basic_format_arg<basic_format_context> arg( std::size_t id ) const;
Returns a `std::basic_format_arg` holding the `id`-th argument in `args`, where `args` is the parameter pack or `std::basic_format_args` object passed to the formatting function.
If `id` is not less than the number of formatting arguments, returns a default-constructed `std::basic_format_arg` (holding a `std::monostate` object).
member|locale|2=
ddcl|1=
std::locale locale();
Returns the locale passed to the formatting function, or a default-constructed `std::locale` if the formatting function does not take a locale.
member|out|2=
ddcl|1=
iterator out();
Returns the iterator to the output buffer. The result is move-constructed from the stored iterator.
member|advance_to|2=
ddcl|1=
void advance_to( iterator it );
Move assigns `it` to the stored output iterator. After a call to `advance_to`, the next call to `out()` will return an iterator with the value that `it` had before the assignment.

## Example


## Defect reports

