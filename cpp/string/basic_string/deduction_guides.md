---
title: deduction guides for std::basic_string
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/deduction_guides
---


# deduction guides for tt|std::basic_string


```cpp
**Header:** `<`string`>`
dcl|since=c++17|num=1|1=
template< class InputIt, class Alloc = std::allocator<
typename std::iterator_traits<InputIt>::value_type> >
basic_string( InputIt, InputIt, Alloc = Alloc() )
-> basic_string<typename std::iterator_traits<InputIt>::value_type,
std::char_traits<
typename std::iterator_traits<InputIt>::value_type>, Alloc>;
dcla|since=c++17|num=2|1=
template< class CharT,
class Traits,
class Alloc = std::allocator<CharT> >
explicit basic_string( std::basic_string_view<CharT, Traits>, const Alloc& = Alloc() )
-> basic_string<CharT, Traits, Alloc>;
dcl|since=c++17|num=3|1=
template< class CharT,
class Traits,
class Alloc = std::allocator<CharT>> >
basic_string( std::basic_string_view<CharT, Traits>,
typename /* see below */::size_type,
typename /* see below */::size_type,
const Alloc& = Alloc() )
-> basic_string<CharT, Traits, Alloc>;
dcla|since=c++23|num=4|1=
template< ranges::input_range R,
class Alloc = std::allocator<ranges::range_value_t<R>> >
basic_string( std::from_range_t, R&&, Alloc = Alloc() )
-> basic_string<ranges::range_value_t<R>,
std::char_traits<ranges::range_value_t<R>>, Alloc>;
```

1. This deduction guide is provided for `std::basic_string` to allow deduction from an iterator range. .
@2,3@ These deduction guides are provided for `std::basic_string` to allow deduction from a `std::basic_string_view`. The `size_type` parameter type in  refers to the `size_type` member type of the type deduced by the deduction guide. .
4. This deduction guide is provided for `std::basic_string` to allow deduction from a `cpp/ranges/from_range|std::from_range_t` tag and an .

## Notes

Guides  are needed because the `std::basic_string` constructors for `std::basic_string_view`s are made templates to avoid causing ambiguities in existing code, and those templates do not support class template argument deduction.

## Notes


## Example


### Example

```cpp
#include <cassert>
#include <string>
#include <vector>

int main()
{
    std::vector<char> v = {'a', 'b', 'c'};
    std::basic_string s1(v.begin(), v.end()); // uses deduction guide (1)
    assert(s1 == "abc");

#if __cpp_lib_containers_ranges >= 202202L
    std::vector<wchar_t> v4{0x43, 43, 053, 0x32, 0x33};
    std::basic_string s4(std::from_range, v4); // uses deduction guide (4)
    assert(s4 == L"C++23");
#endif
}
```


## Defect reports

