---
title: std::basic_string::operator=
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/operator=
---


```cpp
dcla|anchor=no|num=1|constexpr=c++20|1=
basic_string& operator=( const basic_string& str );
dcla|anchor=no|num=2|since=c++11|constexpr=c++20|1=
basic_string& operator=( basic_string&& str )
noexcept(/* see below */);
dcla|anchor=no|num=3|constexpr=c++20|1=
basic_string& operator=( const CharT* s );
dcla|anchor=no|num=4|constexpr=c++20|1=
basic_string& operator=( CharT ch );
dcla|anchor=no|num=5|since=c++11|constexpr=c++20|1=
basic_string& operator=( std::initializer_list<CharT> ilist );
dcla|num=6|since=c++17|constexpr=c++20|1=
template<class StringViewLike>
basic_string& operator=( const StringViewLike& t );
dcl|num=7|since=c++23|1=
basic_string& operator=( std::nullptr_t ) = delete;
```

Replaces the contents of the string.
1. Replaces the contents with a copy of `str`. If `*this` and `str` are the same object, this function has no effect.
2. Replaces the contents with those of `str` using *SequenceContainer*'s move assignment semantics.
@@ Unlike other sequence container move assignments, references, pointers, and iterators to elements of `str` may be invalidated.
3. Replaces the contents with those of null-terminated character string pointed to by `s` as if by `assign(s, Traits::length(s))`.
4. Replaces the contents with character `ch` as if by `assign(std::addressof(ch), 1)`.
5. Replaces the contents with those of the initializer list `ilist` as if by `assign(ilist.begin(), ilist.size())`.
6.
7. `std::basic_string` cannot be assigned from `nullptr`.

## Parameters


### Parameters

- `ch` - value to initialize characters of the string with
- `str` - string to be used as source to initialize the string with
- `s` - pointer to a null-terminated character string to use as source to initialize the string with
- `ilist` - `std::initializer_list` to initialize the string with
- `t` - object convertible to `std::basic_string_view` to initialize the string with

## Return value

`*this`

## Complexity

1. Linear in size of `str`.
2. Linear in the size of `*this` (formally, each `CharT` has to be destroyed). If allocators do not compare equal and do not propagate, then also linear in the size of `str` (copy must be made).
3. Linear in size of `s`.
4. Constant.
5. Linear in size of `ilist`.
6. Linear in size of `t`.

## Exceptions

2. noexcept|std::allocator_traits<Allocator>::
propagate_on_container_move_assignment::value
std::allocator_traits<Allocator>::is_always_equal::value

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <string>

int main()
{
    std::string str1;
    std::string str2{"alpha"};

    // (1) operator=(const basic_string&);
    str1 = str2;
    std::cout << std::quoted(str1) << ' '   // "alpha"
              << std::quoted(str2) << '\n'; // "alpha"

    // (2) operator=(basic_string&&);
    str1 = std::move(str2);
    std::cout << std::quoted(str1) << ' '   // "alpha"
              << std::quoted(str2) << '\n'; // "" or "alpha" (unspecified)

    // (3) operator=(const CharT*);
    str1 = "beta";
    std::cout << std::quoted(str1) << '\n'; // "beta"

    // (4) operator=(CharT);
    str1 = '!'; 
    std::cout << std::quoted(str1) << '\n'; // "!"

    // (5) operator=(std::initializer_list<CharT>);
    str1 = {'g', 'a', 'm', 'm', 'a'};
    std::cout << std::quoted(str1) << '\n'; // "gamma"

    // (6) operator=(const T&);
    str1 = 35U; // equivalent to str1 = static_cast<char>(35U);
    std::cout << std::quoted(str1) << '\n'; // "#" (ASCII = 35)
}
```


**Output:**
```
"alpha" "alpha"
"alpha" ""
"beta"
"!"
"gamma"
"#"
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-847 | C++98 | there was no exception safety guarantee | added strong exception safety guarantee |


## See also


| cpp/string/basic_string/dsc constructor | (see dedicated page) |
| cpp/string/basic_string/dsc assign | (see dedicated page) |
| cpp/string/basic_string_view/dsc operator{{= | (see dedicated page) |

