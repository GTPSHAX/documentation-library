---
title: std::ranges::view_interface::operator bool
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/view_interface/operator_bool
---


```cpp
dcl|num=1|since=c++20|
constexpr explicit operator bool() requires /* see below */;
dcl|num=2|since=c++20|
constexpr explicit operator bool() const requires /* see below */;
```

The default implementation of `operator bool` member function checks whether the view is non-empty. It makes the derived type contextually convertible to `bool`.
1. Let `derived` be `static_cast<D&>(*this)`. The expression in the requires-clause is equal to }, and the function body is equivalent to `return !ranges::empty(derived);`.
2. Same as , except that `derived` is `static_cast<const D&>(*this)`.

## Return value

`false` if the value of the derived type is empty (determined by `ranges::empty|std::ranges::empty`), `true` otherwise.

## Notes

In C++20, no type derived from `ranges::view_interface|std::ranges::view_interface` in the standard library provides their own `operator bool`. Almost all of these types use the default implementation.
A notable exception is `ranges::basic_istream_view|std::ranges::basic_istream_view`. For its iterator type never satisfies , the view cannot use the inherited `operator bool`.

## Example

auto negs = ints | std::views::filter([](int i) { return i < 0; });
std::cout << std::boolalpha
<< "Has odd numbers: " << (!!odds) << ' ' << '\n'
<< "Has negative numbers: " << (!!negs) << ' ' << '\n';
}
|output=
Has odd numbers: true
Has negative numbers: false

## See also


| cpp/ranges/dsc empty | (see dedicated page) |
| cpp/ranges/view_interface/dsc empty | (see dedicated page) |
| cpp/iterator/dsc empty | (see dedicated page) |

