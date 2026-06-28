---
title: std::basic_string::assign
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/assign
---


```cpp
dcla|num=1|constexpr=c++20|
basic_string& assign( const basic_string& str );
dcla|num=2|since=c++11|constexpr=c++20|
basic_string& assign( basic_string&& str ) noexcept(/* see below */);
dcla|num=3|constexpr=c++20|
basic_string& assign( size_type count, CharT ch );
dcla|num=4|constexpr=c++20|
basic_string& assign( const CharT* s, size_type count );
dcla|num=5|constexpr=c++20|
basic_string& assign( const CharT* s );
dcla|num=6|since=c++17|constexpr=c++20|
template< class SV >
basic_string& assign( const SV& t );
dcla|num=7|since=c++17|constexpr=c++20|1=
template< class SV >
basic_string& assign( const SV& t,
size_type pos, size_type count = npos);
dcl rev multi|num=8|until1=c++14|dcl1=
basic_string& assign( const basic_string& str,
size_type pos, size_type count );
|notes2=<sup>(constexpr C++20)</sup>|dcl2=
basic_string& assign( const basic_string& str,
size_type pos, size_type count = npos);
dcla|num=9|constexpr=c++20|
template< class InputIt >
basic_string& assign( InputIt first, InputIt last );
dcla|num=10|since=c++11|constexpr=c++20|
basic_string& assign( std::initializer_list<CharT> ilist );
```

Replaces the contents of the string.
1. Equivalent to `1=return *this = str;`.
2. Equivalent to `1=return *this = std::move(str);`.
3. Replaces the contents with `count` copies of character `ch`.
@@ Equivalent to `clear(); resize(n, c); return *this;`.
4. Replaces the contents with copies of the characters in the range [s, s + count).
@@ If [s, s + count) is not a valid range, the behavior is undefined.
5. Equivalent to `return assign(s, Traits::length(s));`.
@6,7@ Replaces the contents with characters in a string view `sv` constructed from `t`.
* If only `t` is provided, replaces the contents with all characters in `sv`.
* If `pos` is also provided:
** If `count` is , replaces the contents with all characters in `sv` starting from `pos`.
** Otherwise, replaces the contents with the `std::min(count, sv.size() - pos)` characters in `sv` starting from `pos`.
@@ :
* `std::is_convertible_v<const SV&, std::basic_string_view<CharT, Traits>>` is `true`.
* `std::is_convertible_v<const SV&, const CharT*>` is `false`.
:@6@ Equivalent to .
:@7@ Equivalent to .
8. Replaces the contents with characters in `str`.
* If `count` is , replaces the contents with all characters in `str` starting from `pos`.
* Otherwise, replaces the contents with the `std::min(count, str.size() - pos)` characters in `str` starting from `pos`.
rrev|since=c++20|
@@ Equivalent to .
9. Equivalent to `return assign(basic_string(first, last, get_allocator()));`.
rrev|since=c++11|
.
10. Equivalent to `return assign(ilist.begin(), ilist.size());`.

## Parameters


### Parameters

- `str` - string to be used as source to initialize the characters with
- `count` - size of the resulting string
- `ch` - value to initialize characters of the string with
- `s` - pointer to a character string to use as source to initialize the string with
- `t` - object (convertible to `std::basic_string_view`) to initialize the characters of the string with
- `pos` - index of the first character to take
- `first, last` - range to copy the characters from
- `ilist` - `std::initializer_list` to initialize the characters of the string with

## Return value

`*this`

## Exceptions

2. noexcept|std::allocator_traits<Allocator>::
propagate_on_container_move_assignment::value
std::allocator_traits<Allocator>::is_always_equal::value
7. If `pos > sv.size()` is `true`, throws `std::out_of_range`.
8. If `pos > str.size()` is `true`, throws `std::out_of_range`.

## Example


### Example

```cpp
#include <iostream>
#include <iterator>
#include <string>

int main()
{
    std::string s;
    // assign(size_type count, CharT ch)
    s.assign(4, '=');
    std::cout << s << '\n'; // "===="

    std::string const c("Exemplary");
    // assign(const basic_string& str)
    s.assign(c);
    std::cout << c << " == " << s << '\n'; // "Exemplary == Exemplary"

    // assign(const basic_string& str, size_type pos, size_type count)
    s.assign(c, 0, c.length() - 1);
    std::cout << s << '\n'; // "Exemplar";

    // assign(basic_string&& str)
    s.assign(std::string("C++ by ") + "example");
    std::cout << s << '\n'; // "C++ by example"

    // assign(const CharT* s, size_type count)
    s.assign("C-style string", 7);
    std::cout << s << '\n'; // "C-style"

    // assign(const CharT* s)
    s.assign("C-style\0string");
    std::cout << s << '\n'; // "C-style"

    char mutable_c_str[] = "C-style string";
    // assign(InputIt first, InputIt last)
    s.assign(std::begin(mutable_c_str), std::end(mutable_c_str) - 1);
    std::cout << s << '\n'; // "C-style string"

    // assign(std::initializer_list<CharT> ilist)
    s.assign({'C', '-', 's', 't', 'y', 'l', 'e'});
    std::cout << s << '\n'; // "C-style"
}
```


**Output:**
```
====
Exemplary == Exemplary
Exemplar
C++ by example
C-style
C-style
C-style string
C-style
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-847 | C++98 | there was no exception safety guarantee | added strong exception safety guarantee |


## See also


| cpp/string/basic_string/dsc assign_range | (see dedicated page) |
| cpp/string/basic_string/dsc constructor | (see dedicated page) |
| cpp/string/basic_string/dsc operator{{= | (see dedicated page) |

