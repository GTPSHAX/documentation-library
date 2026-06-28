---
title: std::basic_regex::operator=
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/basic_regex/operator=
---


```cpp
**Header:** `<`regex`>`
dcl|num=1|since=c++11|1=
basic_regex& operator=( const basic_regex& other );
dcl|num=2|since=c++11|1=
basic_regex& operator=( basic_regex&& other ) noexcept;
dcl|num=3|since=c++11|1=
basic_regex& operator=( const CharT* ptr );
dcl|num=4|since=c++11|1=
basic_regex& operator=( std::initializer_list<CharT> il );
dcl|num=5|since=c++11|1=
template< class ST, class SA >
basic_regex& operator=( const std::basic_string<CharT,ST,SA>& p );
```

Assigns the contents.
1. Copy assignment operator. Assigns the contents of `other`. Equivalent to `assign(other);`.
2. Move assignment operator. Assigns the contents of `other` using move semantics. `other` is in valid, but unspecified state after the operation. Equivalent to `assign(other);`.
3. Assigns a null-terminated character string pointed to by `ptr`. Equivalent to `assign(ptr);`.
4. Assigns characters contained in initializer list `il`. Equivalent to `assign(il);`.
5. Assigns the contents of the string `p`. Equivalent to `assign(p);`.

## Parameters


### Parameters

- `other` - another regex object
- `ptr` - pointer to a null-terminated character string
- `il` - initializer list containing characters to assign
- `p` - string containing characters to assign

## Return value

`*this`

## Exceptions

1.
@3-5@ `std::regex_error` if the supplied regular expression is not valid. The object is not modified in that case.

## See also


| cpp/regex/basic_regex/dsc assign | (see dedicated page) |

