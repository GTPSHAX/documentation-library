---
title: std::basic_string::basic_string
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/basic_string
---


```cpp
dcl rev multi|num=1|since1=c++11|until1=c++17|dcl1=
basic_string() : basic_string(Allocator()) {}
|notes2=<sup>(constexpr C++20)</sup>|dcl2=
basic_string() noexcept(noexcept(Allocator()))
: basic_string(Allocator()) {}
dcl rev multi|num=2|until1=c++11|dcl1=
explicit basic_string( const Allocator& alloc = Allocator() );
|notes2=<br /><sup>(constexpr C++20)</sup>|dcl2=
explicit basic_string( const Allocator& alloc );
dcla|num=3|constexpr=c++20|1=
basic_string( size_type count, CharT ch,
const Allocator& alloc = Allocator() );
dcla|num=4|constexpr=c++20|1=
template< class InputIt >
basic_string( InputIt first, InputIt last,
const Allocator& alloc = Allocator() );
dcl|num=5|since=c++23|1=
template< container-compatible-range<CharT> R >
constexpr basic_string( std::from_range_t, R&& rg,
const Allocator& = Allocator());
dcla|num=6|constexpr=c++20|1=
basic_string( const CharT* s, size_type count,
const Allocator& alloc = Allocator() );
dcla|num=7|constexpr=c++20|1=
basic_string( const CharT* s, const Allocator& alloc = Allocator() );
dcl|num=8|since=c++23|1=
basic_string( std::nullptr_t ) = delete;
dcla|num=9|since=c++17|constexpr=c++20|1=
template< class StringViewLike >
explicit basic_string( const StringViewLike& t,
const Allocator& alloc = Allocator() );
dcl|num=10|since=c++17|constexpr=c++20|1=
template< class StringViewLike >
basic_string( const StringViewLike& t,
size_type pos, size_type count,
const Allocator& alloc = Allocator() );
dcla|num=11|constexpr=c++20|
basic_string( const basic_string& other );
dcla|num=12|since=c++11|constexpr=c++20|
basic_string( basic_string&& other ) noexcept;
dcla|num=13|since=c++11|constexpr=c++20|
basic_string( const basic_string& other, const Allocator& alloc );
dcla|num=14|since=c++11|constexpr=c++20|
basic_string( basic_string&& other, const Allocator& alloc );
dcla|num=15|constexpr=c++20|1=
basic_string( const basic_string& other, size_type pos,
const Allocator& alloc = Allocator() );
dcl|num=16|since=c++23|1=
constexpr basic_string( basic_string&& other, size_type pos,
const Allocator& alloc = Allocator() );
dcla|num=17|constexpr=c++20|1=
basic_string( const basic_string& other,
size_type pos, size_type count,
const Allocator& alloc = Allocator() );
dcl|num=18|since=c++23|1=
constexpr basic_string( basic_string&& other,
size_type pos, size_type count,
const Allocator& alloc = Allocator() );
dcla|num=19|since=c++11|constexpr=c++20|1=
basic_string( std::initializer_list<CharT> ilist,
const Allocator& alloc = Allocator() );
```

Constructs new string from a variety of data sources and optionally using user supplied allocator `alloc`.
1. The default constructor since C++11. Constructs an empty string with a default-constructed allocator.
@@ If Allocator is not *DefaultConstructible*, the behavior is undefined.
2. The default constructor until C++11. Constructs an empty string with the given allocator `alloc`.
3. Constructs a string with `count` copies of character `ch`.
rev|since=c++11|
If `CharT` is not *CopyInsertable* into `std::basic_string<CharT>`, the behavior is undefined.
rev|since=c++17|
.
4. Constructs a string with the contents of the range [first, last). Each iterator in [first, last) is dereferenced exactly once.
rev|until=c++11|
If `InputIt` does not satisfy the requirements of *InputIterator*, overload  is called instead with arguments `static_cast<size_type>(first)`, `last` and `alloc`.
rev|since=c++11|
.
If `CharT` is not *EmplaceConstructible* into `std::basic_string<CharT>` from `*first`, the behavior is undefined.
5. Constructs a string with the contents of the range `rg`. Each iterator in `rg` is dereferenced exactly once.
@@ If `CharT` is not *EmplaceConstructible* into `std::basic_string<CharT>` from `*ranges::begin(rg)`, the behavior is undefined.
6. Constructs a string with the contents of the range [s, s + count).
@@ If [s, s + count) is not a valid range, the behavior is undefined.
7. Equivalent to `basic_string(s, Traits::length(s), alloc)`.
rrev|since=c++17|
.
8. `std::basic_string` cannot be constructed from `nullptr`.
9.
10.
@11-18@ Constructs a string with (part of) the contents of `other`. If the type of `other` is `basic_string&&`, when the construction finishes, `other` is in a valid but unspecified state.
:@11@ The copy constructor.
rrev|since=c++11|
The allocator is obtained as if by calling .
:@12@ The move constructor. The allocator is obtained by move construction from `other.get_allocator()`.
:@13@ Same as the copy constructor, except that `alloc` is used as the allocator.
:@@ If `CharT` is not *CopyInsertable* into `std::basic_string<CharT>`, the behavior is undefined.
:@14@ Same as the move constructor, except that `alloc` is used as the allocator.
:@@ If `CharT` is not *MoveInsertable* into `std::basic_string<CharT>`, the behavior is undefined.
:@15,16@ Constructs a string with the contents of the range [other.data() + pos, other.data() + other.size()).
:@17,18@ Constructs a string with the contents of the range [other.data() + pos, other.data() + (pos + std::min(count, other.size() - pos))).
19. Equivalent to `basic_string(ilist.begin(), ilist.end())`.

## Parameters


### Parameters

- `alloc` - allocator to use for all memory allocations of this string
- `count` - size of the resulting string
- `ch` - value to initialize the string with
- `pos` - position of the first character to include
- `first, last` - range to copy the characters from
- `s` - pointer to an array of characters to use as source to initialize the string with
- `other` - another string to use as source to initialize the string with
- `ilist` - `std::initializer_list` to initialize the string with
- `t` - object (convertible to `std::basic_string_view`) to initialize the string with
- `rg` - a container compatible range

## Complexity

@1,2@ Constant.
@3-7@ Linear in the size of the string.
@9-11@ Linear in the size of the string.
12. Constant.
13. Linear in the size of the string.
14. Linear in the size of the string if `1=alloc != other.get_allocator()` is `true`, otherwise constant.
@15-19@ Linear in the size of the string.

## Exceptions

10. `std::out_of_range` if `pos` is out of range.
14. Throws nothing if `1=alloc == str.get_allocator()` is `true`.
@15-18@ `std::out_of_range` if `pos > other.size()` is `true`.
Throws `std::length_error` if the length of the constructed string would exceed `max_size()` (for example, if `count > max_size()` for ). Calls to `Allocator::allocate` may throw.

## Notes

Initialization with a  that contains embedded `'\0'` characters uses the overload , which stops at the first null character. This can be avoided by specifying a different constructor or by using `operator""s`:

```cpp
std::string s1 = "ab\0\0cd";   // s1 contains "ab"
std::string s2{"ab\0\0cd", 6}; // s2 contains "ab\0\0cd"
std::string s3 = "ab\0\0cd"s;  // s3 contains "ab\0\0cd"
```


## Example


### Example

```cpp
#include <cassert>
#include <cctype>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <string>

int main()
{
    std::cout << "1)  string(); ";
    std::string s1;
    assert(s1.empty() && (s1.length() == 0) && (s1.size() == 0));
    std::cout << "s1.capacity(): " << s1.capacity() << '\n'; // unspecified

    std::cout << "3)  string(size_type count, CharT ch): ";
    std::string s2(4, '=');
    std::cout << std::quoted(s2) << '\n'; // "===="

    std::cout << "4)  string(InputIt first, InputIt last): ";
    char mutable_c_str[] = "another C-style string";
    std::string s4(std::begin(mutable_c_str) + 8, std::end(mutable_c_str) - 1);
    std::cout << std::quoted(s4) << '\n'; // "C-style string"

    std::cout << "6)  string(CharT const* s, size_type count): ";
    std::string s6("C-style string", 7);
    std::cout << std::quoted(s6) << '\n'; // "C-style", i.e. [0, 7)

    std::cout << "7)  string(CharT const* s): ";
    std::string s7("C-style\0string");
    std::cout << std::quoted(s7) << '\n'; // "C-style"

    std::cout << "11) string(string&): ";
    std::string const other11("Exemplar");
    std::string s11(other11);
    std::cout << std::quoted(s11) << '\n'; // "Exemplar"

    std::cout << "12) string(string&&): ";
    std::string s12(std::string("C++ by ") + std::string("example"));
    std::cout << std::quoted(s12) << '\n'; // "C++ by example"

    std::cout << "15) string(const string& other, size_type pos): ";
    std::string const other15("Mutatis Mutandis");
    std::string s15(other15, 8);
    std::cout << std::quoted(s15) << '\n'; // "Mutandis", i.e. [8, 16)

    std::cout << "17) string(const string& other, size_type pos, size_type count): ";
    std::string const other17("Exemplary");
    std::string s17(other17, 0, other17.length() - 1);
    std::cout << std::quoted(s17) << '\n'; // "Exemplar"

    std::cout << "19) string(std::initializer_list<CharT>): ";
    std::string s19({'C', '-', 's', 't', 'y', 'l', 'e'});
    std::cout << std::quoted(s19) << '\n'; // "C-style"
}
```


**Output:**
```
1)  string(); s1.capacity(): 15
3)  string(size_type count, CharT ch): "===="
4)  string(InputIt first, InputIt last): "C-style string"
6)  string(CharT const* s, size_type count): "C-style"
7)  string(CharT const* s): "C-style"
11) string(string&): "Exemplar"
12) string(string&&): "C++ by example"
15) string(const string& other, size_type pos): "Mutandis"
17) string(const string& other, size_type pos, size_type count): "Exemplar"
19) string(std::initializer_list<CharT>): "C-style"
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-847 | C++98 | there was no exception safety guarantee | added strong exception safety guarantee |
| lwg-2193 | C++11 | the default constructor is explicit | made non-explicit |


## See also


| cpp/string/basic_string/dsc assign | (see dedicated page) |
| cpp/string/basic_string/dsc operator{{= | (see dedicated page) |
| cpp/string/basic_string/dsc to_string | (see dedicated page) |
| cpp/string/basic_string/dsc to_wstring | (see dedicated page) |
| cpp/string/basic_string_view/dsc constructor | (see dedicated page) |

