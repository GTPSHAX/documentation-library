---
title: std::basic_regex::assign
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/basic_regex/assign
---


```cpp
dcl|num=1|since=c++11|
basic_regex& assign( const basic_regex& other );
dcl|num=2|since=c++11|
basic_regex& assign( basic_regex&& other ) noexcept;
dcl|num=3|since=c++11|1=
basic_regex& assign( const CharT* s,
flag_type f = std::regex_constants::ECMAScript );
dcl|num=4|since=c++11|1=
basic_regex& assign( const CharT* ptr, std::size_t count,
flag_type f = std::regex_constants::ECMAScript );
dcl|num=5|since=c++11|1=
template< class ST, class SA >
basic_regex& assign( const std::basic_string<CharT,ST,SA>& str,
flag_type f = std::regex_constants::ECMAScript );
dcl|num=6|since=c++11|1=
template< class InputIt >
basic_regex& assign( InputIt first, InputIt last,
flag_type f = std::regex_constants::ECMAScript );
dcl|num=7|since=c++11|1=
basic_regex& assign( std::initializer_list<CharT> ilist,
flag_type f = std::regex_constants::ECMAScript );
```

Assigns the contents to the regular expression.
1. Assigns the contents of `other`. `flags()` and `mark_count()` are equivalent to the values of `other.flags()` and `other.mark_count()` after the call.
2. Assigns the contents of `other` using move semantics. `flags()` and `mark_count()` are equivalent to the values of `other.flags()` and `other.mark_count()` before the assignment. After the call, `other` is in a valid, but unspecified state.
@3-7@ Assigns a sequence of characters to the regular expression. The syntax flags are set to `f`. `mark_count()` returns the number of marked subexpressions within the resulting subexpression after the call.
:@3@ Assigns a null-terminated string pointed to by `s`.
:@4@ Assigns a sequence of `count` characters, pointed to by `s`.
:@5@ Assigns the string `str`.
:@6@ Assigns the characters in the range [first, last).
:@7@ Assigns the characters in the initializer list `ilist`.

## Parameters


### Parameters

- `other` - another regular expression to assign
- `s` - pointer to a character sequence to assign
- `str` - string to assign
- `first, last` - the range of characters to assign
- `ilist` - initializer list containing characters to assign

**Type requirements:**

- `InputIt`

## Return value

`*this`

## Exceptions

1.
@3-7@ `std::regex_error` if the supplied regular expression is not valid. The object is not modified in that case.

## Example

