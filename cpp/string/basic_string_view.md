---
title: std::basic_string_view
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view
---

ddcl|header=string_view|since=c++17|1=
template<
class CharT,
class Traits = std::char_traits<CharT>
> class basic_string_view;
The class template `basic_string_view` describes an object that can refer to a constant contiguous sequence of `CharT` with the first element of the sequence at position zero.
For a `basic_string_view` `str`, pointers, iterators, and references to elements of `str` are invalidated when an operation invalidates a pointer in the range [str.data(), str.data() + str.size()).
rrev|since=c++23|
Every specialization of `std::basic_string_view` is a *TriviallyCopyable* type.
Several typedefs for common character types are provided:


| Item | Description |
|------|-------------|
| string_view | |
| **Type** | Definition |


## Template parameters


### Parameters

- `CharT` - character type
- `Traits` - *CharTraits* class specifying the operations on the character type. Like for `std::basic_string`, `Traits::char_type` must name the same type as `CharT` or the program is ill-formed.

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| dsc|`const_iterator`|implementation-defined constant *RandomAccessIterator*,<br> | |
| <sup>(until C++20)</sup> and *ContiguousIterator* | |
| <sup>(since C++20)</sup> *ConstexprIterator, and | |
| whose `value_type` is `CharT` | |

Note: `iterator` and `const_iterator` are the same type because string views are views into constant character sequences.
All requirements on the iterator types of a *Container* applies to the `iterator` and `const_iterator` types of `basic_string_view` as well.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


#### Constructors and assignment

| cpp/string/basic_string_view/dsc constructor | (see dedicated page) |
| cpp/string/basic_string_view/dsc operator{{= | (see dedicated page) |

#### Iterators

| cpp/string/basic_string_view/dsc begin | (see dedicated page) |
| cpp/string/basic_string_view/dsc end | (see dedicated page) |
| cpp/string/basic_string_view/dsc rbegin | (see dedicated page) |
| cpp/string/basic_string_view/dsc rend | (see dedicated page) |

#### Element access

| cpp/string/basic_string_view/dsc operator_at | (see dedicated page) |
| cpp/string/basic_string_view/dsc at | (see dedicated page) |
| cpp/string/basic_string_view/dsc front | (see dedicated page) |
| cpp/string/basic_string_view/dsc back | (see dedicated page) |
| cpp/string/basic_string_view/dsc data | (see dedicated page) |

#### Capacity

| cpp/string/basic_string_view/dsc size | (see dedicated page) |
| cpp/string/basic_string_view/dsc max_size | (see dedicated page) |
| cpp/string/basic_string_view/dsc empty | (see dedicated page) |

#### Modifiers

| cpp/string/basic_string_view/dsc remove_prefix | (see dedicated page) |
| cpp/string/basic_string_view/dsc remove_suffix | (see dedicated page) |
| cpp/string/basic_string_view/dsc swap | (see dedicated page) |

#### Operations

| cpp/string/basic_string_view/dsc copy | (see dedicated page) |
| cpp/string/basic_string_view/dsc substr | (see dedicated page) |
| cpp/string/basic_string_view/dsc subview | (see dedicated page) |
| cpp/string/basic_string_view/dsc compare | (see dedicated page) |
| cpp/string/basic_string_view/dsc starts_with | (see dedicated page) |
| cpp/string/basic_string_view/dsc ends_with | (see dedicated page) |
| cpp/string/basic_string_view/dsc contains | (see dedicated page) |
| cpp/string/basic_string_view/dsc find | (see dedicated page) |
| cpp/string/basic_string_view/dsc rfind | (see dedicated page) |
| cpp/string/basic_string_view/dsc find_first_of | (see dedicated page) |
| cpp/string/basic_string_view/dsc find_last_of | (see dedicated page) |
| cpp/string/basic_string_view/dsc find_first_not_of | (see dedicated page) |
| cpp/string/basic_string_view/dsc find_last_not_of | (see dedicated page) |
| cpp/string/basic_string_view/dsc npos | (see dedicated page) |


## Non-member functions


| cpp/string/basic_string_view/dsc operator cmp | (see dedicated page) |

#### Input/output

| cpp/string/basic_string_view/dsc operator ltlt | (see dedicated page) |


## Literals


| std::literals::string_view_literals|inline=true | |
| cpp/string/basic_string_view/dsc operator""sv | (see dedicated page) |


## Helper classes


| cpp/string/basic_string_view/dsc hash | (see dedicated page) |


## Helper templates

ddcl|since=c++20|1=
template< class CharT, class Traits >
inline constexpr bool
ranges::enable_borrowed_range<std::basic_string_view<CharT, Traits>> = true;
This specialization of `cpp/ranges/borrowed_range|ranges::enable_borrowed_range` makes `basic_string_view` satisfy .
ddcl|since=c++20|1=
template< class CharT, class Traits >
inline constexpr bool
ranges::enable_view<std::basic_string_view<CharT, Traits>> = true;
This specialization of `ranges::enable_view` makes `basic_string_view` satisfy .
rrev|since=c++20|

## 


## Notes

It is the programmer's responsibility to ensure that `std::string_view` does not outlive the  pointed-to character array:

```cpp
std::string_view good{"a string literal"};
    // "Good" case: `good` points to a static array.
    // String literals reside in persistent data storage.

std::string_view bad{"a temporary string"s};
    // "Bad" case: `bad` holds a dangling pointer since the std::string temporary,
    // created by std::operator""s, will be destroyed at the end of the statement.
```

Specializations of `std::basic_string_view` are already trivially copyable types in all existing implementations, even before the formal requirement introduced in C++23.

## Example


### Example

```cpp
#include <iostream>
#include <string_view>

int main()
{
    #define A "▀"
    #define B "▄"
    #define C "─"

    constexpr std::string_view blocks[]{A B C, B A C, A C B, B C A};

    for (int y{}, p{}; y != 8; ++y, p = ((p + 1) % 4))
    {
        for (char x{}; x != 29; ++x)
            std::cout << blocks[p];
        std::cout << '\n';
    }
}
```


**Output:**
```
▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─
▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─
▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄
▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀
▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─
▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─
▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄
▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀
```


## Defect reports


## See also


| cpp/string/dsc basic_string | (see dedicated page) |
| cpp/string/basic_string/dsc operator+ | (see dedicated page) |
| cpp/container/dsc span | (see dedicated page) |
| cpp/utility/dsc initializer_list | (see dedicated page) |

