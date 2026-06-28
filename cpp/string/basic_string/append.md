---
title: std::basic_string::append
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/append
---


```cpp
dcla|num=1|constexpr=c++20|
basic_string& append( size_type count, CharT ch );
dcla|num=2|constexpr=c++20|
basic_string& append( const CharT* s, size_type count );
dcla|num=3|constexpr=c++20|
basic_string& append( const CharT* s );
dcla|num=4|since=c++17|constexpr=c++20|
template< class SV >
basic_string& append( const SV& t );
dcla|num=5|since=c++17|constexpr=c++20|1=
template< class SV >
basic_string& append( const SV& t, size_type pos,
size_type count = npos );
dcla|num=6|constexpr=c++20|
basic_string& append( const basic_string& str );
dcl rev multi|num=7|until1=c++14|dcl1=
basic_string& append( const basic_string& str,
size_type pos, size_type count );
|notes2=<sup>(constexpr C++20)</sup>|dcl2=
basic_string& append( const basic_string& str,
size_type pos, size_type count = npos );
dcla|num=8|constexpr=c++20|
template< class InputIt >
basic_string& append( InputIt first, InputIt last );
dcla|num=9|since=c++11|constexpr=c++20|
basic_string& append( std::initializer_list<CharT> ilist );
```

Appends additional characters to the string.
1. Appends `count` copies of character `ch`.
2. Appends characters in the range [s, s + count).
@@ If [s, s + count) is not a valid range, the behavior is undefined.
3. Equivalent to `return append(s, Traits::length(s));`.
@4,5@ Appends characters in a string view `sv` constructed from `t`.
* If only `t` is provided, all characters in `sv` are appended.
* If `pos` is also provided:
** If `count` is , all characters in `sv` starting from `pos` are appended.
** Otherwise, the `std::min(count, sv.size() - pos)` characters in `sv` starting from `pos` are appended.
@@ :
* `std::is_convertible_v<const SV&, std::basic_string_view<CharT, Traits>>` is `true`.
* `std::is_convertible_v<const SV&, const CharT*>` is `false`.
:@4@ Equivalent to .
:@5@ Equivalent to .
@6,7@ Appends characters in another string `str`.
* If only `str` is provided, all characters in it are appended.
* If `pos` is also provided:
** If `count` is , all characters in `str` starting from `pos` are appended.
** Otherwise, the `std::min(count, str.size() - pos)` characters in `str` starting from `pos` are appended.
:@6@ Equivalent to `return append(str.data(), str.size());`.
rrev|since=c++20|
:@7@ Equivalent to .
8. Equivalent to `return append(basic_string(first, last, get_allocator()));`.
rev|until=c++11|
This overload has the same effect as overload  if `InputIt` is an integral type.
rev|since=c++11|
.
9. Equivalent to `return append(ilist.begin(), ilist.size());`.

## Parameters


### Parameters

- `count` - number of characters to append
- `ch` - character value to append
- `s` - pointer to the character string to append
- `t` - object convertible to `std::basic_string_view` with the characters to append
- `pos` - the index of the first character to append
- `str` - string to append
- `first, last` - range of characters to append
- `ilist` - initializer list with the characters to append

## Return value

`*this`

## Complexity

There are no standard complexity guarantees, typical implementations behave similar to .

## Exceptions

5. If `pos > sv.size()` is `true`, throws `std::out_of_range`.
7. If `pos > str.size()` is `true`, throws `std::out_of_range`.

## Example


### Example

```cpp
#include <cassert>
#include <string>

int main()
{
    std::string str = "std::string";
    const char* cptr = "C-string";
    const char carr[] = "range";

    std::string result;

    // 1) Append a char 3 times.
    // Note: This is the only overload accepting “CharT”s.
    result.append(3, '*');
    assert(result == "***");

    // 2) Append a fixed-length C-string
    result.append(cptr, 5);
    assert(result == "***C-str");

    // 3) Append a null-terminated C-string
    // Note: Because “append” returns *this, we can chain calls together.
    result.append(1, ' ').append(cptr);
    assert(result == "***C-str C-string");

    // 6) Append a whole string
    result.append(1, ' ').append(str);
    assert(result == "***C-str C-string std::string");

    // 7) Append part of a string
    result.append(str, 3, 2);
    assert(result == "***C-str C-string std::string::");

    // 8) Append range
    result.append(&carr[2], &carr[3]);
    assert(result == "***C-str C-string std::string::n");

    // 9) Append initializer list
    result.append({'p', 'o', 's'});
    assert(result == "***C-str C-string std::string::npos");
}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-847 | C++98 | there was no exception safety guarantee | added strong exception safety guarantee |


## See also


| cpp/string/basic_string/dsc append_range | (see dedicated page) |
| cpp/string/basic_string/dsc operator+{{= | (see dedicated page) |
| cpp/string/byte/dsc strcat | (see dedicated page) |
| cpp/string/byte/dsc strncat | (see dedicated page) |
| cpp/string/wide/dsc wcscat | (see dedicated page) |
| cpp/string/wide/dsc wcsncat | (see dedicated page) |

