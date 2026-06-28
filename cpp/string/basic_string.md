---
title: std::basic_string
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string
---


```cpp
**Header:** `<`string`>`
dcl|num=1|1=
template<
class CharT,
class Traits = std::char_traits<CharT>,
class Allocator = std::allocator<CharT>
> class basic_string;
dcl|since=c++17|num=2|1=
namespace pmr {
template<
class CharT,
class Traits = std::char_traits<CharT>
> using basic_string =
std::basic_string<CharT, Traits, std::pmr::polymorphic_allocator<CharT>>;
}
```

The class template `basic_string` stores and manipulates sequences of character-like objects, which are non-array objects of *TrivialType* and *StandardLayoutType*. The class is dependent neither on the character type nor on the nature of operations on that type. The definitions of the operations are supplied via the `Traits` template parameter - a specialization of `std::char_traits` or a compatible traits class.
The elements of a `basic_string` are stored contiguously, that is, for a `basic_string` `s`, `1=&*(s.begin() + n) == &*s.begin() + n` for any `n` in [0, s.size())<sup>(since C++11)</sup> , and `1=*(s.begin() + s.size())` has value `1=CharT()` (a null terminator); or, equivalently, a pointer to `s[0]` can be passed to functions that expect a pointer to the first element of <sup>(until C++11)</sup> an array<sup>(since C++11)</sup> a null-terminated array of `CharT`.
`std::basic_string` satisfies the requirements of *AllocatorAwareContainer* (except that customized `construct`/`destroy` are not used for construction/destruction of elements), *SequenceContainer*<sup>(since C++17)</sup>  and *ContiguousContainer*.
If any of `Traits::char_type` and `Allocator::char_type` is different from `CharT`, the program is ill-formed.
Several typedefs for common character types are provided:


| Item | Description |
|------|-------------|
| string | |
| **Type** | Definition |


## Template parameters


### Parameters

- `CharT` - character type
- `Traits` - traits class specifying the operations on the character type
- `Allocator` - *Allocator* type used to allocate internal storage

## Iterator invalidation

References, pointers, and iterators referring to the elements of a `basic_string` may be invalidated by any standard library function taking a reference to non-const `basic_string` as an argument, such as `std::getline`, `std::swap`, or `cpp/string/basic_string/operator_ltltgtgt|operator>>`, and by calling non-const member functions, except `cpp/string/basic_string/operator_at|operator[]`, , , , , , , , and .

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| cpp/container/dsc allocator_type|basic_string | (see dedicated page) |
| cpp/container/dsc size_type|basic_string | (see dedicated page) |
| cpp/container/dsc difference_type|basic_string | (see dedicated page) |
| cpp/container/dsc reference|basic_string | (see dedicated page) |
| cpp/container/dsc const_reference|basic_string | (see dedicated page) |
| cpp/container/dsc pointer|basic_string | (see dedicated page) |
| cpp/container/dsc const_pointer|basic_string | (see dedicated page) |
| cpp/container/dsc iterator|basic_string | (see dedicated page) |
| cpp/container/dsc const_iterator|basic_string | (see dedicated page) |
| cpp/container/dsc reverse_iterator|basic_string | (see dedicated page) |
| cpp/container/dsc const_reverse_iterator|basic_string | (see dedicated page) |


## Data members


## Member functions


| cpp/string/basic_string/dsc constructor | (see dedicated page) |
| cpp/string/basic_string/dsc destructor | (see dedicated page) |
| cpp/string/basic_string/dsc operator{{= | (see dedicated page) |
| cpp/string/basic_string/dsc assign | (see dedicated page) |
| cpp/string/basic_string/dsc assign_range | (see dedicated page) |
| cpp/string/basic_string/dsc get_allocator | (see dedicated page) |

#### Element access

| cpp/string/basic_string/dsc at | (see dedicated page) |
| cpp/string/basic_string/dsc operator_at | (see dedicated page) |
| cpp/string/basic_string/dsc front | (see dedicated page) |
| cpp/string/basic_string/dsc back | (see dedicated page) |
| cpp/string/basic_string/dsc data | (see dedicated page) |
| cpp/string/basic_string/dsc c_str | (see dedicated page) |
| cpp/string/basic_string/dsc operator_string_view | (see dedicated page) |

#### Iterators

| cpp/string/basic_string/dsc begin | (see dedicated page) |
| cpp/string/basic_string/dsc end | (see dedicated page) |
| cpp/string/basic_string/dsc rbegin | (see dedicated page) |
| cpp/string/basic_string/dsc rend | (see dedicated page) |

#### Capacity

| cpp/string/basic_string/dsc empty | (see dedicated page) |
| cpp/string/basic_string/dsc size | (see dedicated page) |
| cpp/string/basic_string/dsc max_size | (see dedicated page) |
| cpp/string/basic_string/dsc reserve | (see dedicated page) |
| cpp/string/basic_string/dsc capacity | (see dedicated page) |
| cpp/string/basic_string/dsc shrink_to_fit | (see dedicated page) |

#### Modifiers

| cpp/string/basic_string/dsc clear | (see dedicated page) |
| cpp/string/basic_string/dsc insert | (see dedicated page) |
| cpp/string/basic_string/dsc insert_range | (see dedicated page) |
| cpp/string/basic_string/dsc erase | (see dedicated page) |
| cpp/string/basic_string/dsc push_back | (see dedicated page) |
| cpp/string/basic_string/dsc pop_back | (see dedicated page) |
| cpp/string/basic_string/dsc append | (see dedicated page) |
| cpp/string/basic_string/dsc append_range | (see dedicated page) |
| cpp/string/basic_string/dsc operator+{{= | (see dedicated page) |
| cpp/string/basic_string/dsc replace | (see dedicated page) |
| cpp/string/basic_string/dsc replace_with_range | (see dedicated page) |
| cpp/string/basic_string/dsc copy | (see dedicated page) |
| cpp/string/basic_string/dsc resize | (see dedicated page) |
| cpp/string/basic_string/dsc resize_and_overwrite | (see dedicated page) |
| cpp/string/basic_string/dsc swap | (see dedicated page) |

#### Search

| cpp/string/basic_string/dsc find | (see dedicated page) |
| cpp/string/basic_string/dsc rfind | (see dedicated page) |
| cpp/string/basic_string/dsc find_first_of | (see dedicated page) |
| cpp/string/basic_string/dsc find_first_not_of | (see dedicated page) |
| cpp/string/basic_string/dsc find_last_of | (see dedicated page) |
| cpp/string/basic_string/dsc find_last_not_of | (see dedicated page) |

#### Operations

| cpp/string/basic_string/dsc compare | (see dedicated page) |
| cpp/string/basic_string/dsc starts_with | (see dedicated page) |
| cpp/string/basic_string/dsc ends_with | (see dedicated page) |
| cpp/string/basic_string/dsc contains | (see dedicated page) |
| cpp/string/basic_string/dsc substr | (see dedicated page) |
| cpp/string/basic_string/dsc subview | (see dedicated page) |


## Non-member functions


| cpp/string/basic_string/dsc operator+ | (see dedicated page) |
| cpp/string/basic_string/dsc operator_cmp | (see dedicated page) |
| cpp/string/basic_string/dsc swap2 | (see dedicated page) |
| cpp/container/dsc erase seq|basic_string | (see dedicated page) |

#### Input/output

| cpp/string/basic_string/dsc operator_ltltgtgt | (see dedicated page) |
| cpp/string/basic_string/dsc getline | (see dedicated page) |

#### Numeric conversions

| cpp/string/basic_string/dsc stol | (see dedicated page) |
| cpp/string/basic_string/dsc stoul | (see dedicated page) |
| cpp/string/basic_string/dsc stof | (see dedicated page) |
| cpp/string/basic_string/dsc to_string | (see dedicated page) |
| cpp/string/basic_string/dsc to_wstring | (see dedicated page) |


## Literals


| std::literals::string_literals|inline=true | |
| cpp/string/basic_string/dsc operator""s | (see dedicated page) |


## Helper classes


| cpp/string/basic_string/dsc hash | (see dedicated page) |


## Deduction guides <sup>(C++17)</sup>


## Notes

Although it is required that customized `construct` or `destroy` is used when constructing or destroying elements of `std::basic_string` until C++23, all implementations only used the default mechanism. The requirement is corrected by `P1072R10` to match existing practice.

## Example


### Example

```cpp
#include <iostream>
#include <string>

int main()
{
    using namespace std::literals;

    // Creating a string from const char*
    std::string str1 = "hello";

    // Creating a string using string literal
    auto str2 = "world"s;

    // Concatenating strings
    std::string str3 = str1 + " " + str2;

    // Print out the result
    std::cout << str3 << '\n';

    std::string::size_type pos = str3.find(" ");
    str1 = str3.substr(pos + 1); // the part after the space
    str2 = str3.substr(0, pos);  // the part till the space

    std::cout << str1 << ' ' << str2 << '\n';

    // Accessing an element using subscript operator[]
    std::cout << str1[0] << '\n';
    str1[0] = 'W';
    std::cout << str1 << '\n';
}
```


**Output:**
```
hello world
world hello
w
World
```


## Defect reports


## See also


| cpp/string/dsc basic_string_view | (see dedicated page) |


## External links

