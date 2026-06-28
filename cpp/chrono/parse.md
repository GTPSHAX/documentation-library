---
title: std::chrono::parse
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/parse
---


```cpp
dcl | since=c++20 | num=1 |
template< class CharT, class Parsable >
/* unspecified */ parse( const CharT* fmt, Parsable& tp );
dcl | since=c++20 | num=2 |
template< class CharT, class Traits, class Alloc, class Parsable >
/* unspecified */ parse( const std::basic_string<CharT, Traits, Alloc>& fmt,
Parsable& tp );
dcl | since=c++20 | num=3 | 1=
template< class CharT, class Traits, class Alloc, class Parsable >
/* unspecified */ parse( const CharT* fmt, Parsable& tp,
std::basic_string<CharT, Traits, Alloc>& abbrev );
dcl | since=c++20 | num=4 | 1=
template< class CharT, class Traits, class Alloc, class Parsable >
/* unspecified */ parse( const std::basic_string<CharT, Traits, Alloc>& fmt,
Parsable& tp,
std::basic_string<CharT, Traits, Alloc>& abbrev );
dcl | since=c++20 | num=5 | 1=
template< class CharT, class Parsable >
/* unspecified */ parse( const CharT* fmt, Parsable& tp,
std::chrono::minutes& offset );
dcl | since=c++20 | num=6 | 1=
template< class CharT, class Traits, class Alloc, class Parsable >
/* unspecified */ parse( const std::basic_string<CharT, Traits, Alloc>& fmt,
Parsable& tp, std::chrono::minutes& offset );
dcl | since=c++20 | num=7 | 1=
template< class CharT, class Traits, class Alloc, class Parsable >
/* unspecified */ parse( const CharT* fmt, Parsable& tp,
std::basic_string<CharT, Traits, Alloc>& abbrev,
std::chrono::minutes& offset );
dcl | since=c++20 | num=8 | 1=
template< class CharT, class Traits, class Alloc, class Parsable >
/* unspecified */ parse( const std::basic_string<CharT, Traits, Alloc>& fmt,
Parsable& tp,
std::basic_string<CharT, Traits, Alloc>& abbrev,
std::chrono::minutes& offset );
```

Returns an object `manip` of unspecified type such that, given a `std::basic_istream<CharT, Traits>` object `is`, the expression `is >> manip` calls `from_stream` (unqualified, to enable argument-dependent lookup) as follows:
1. `from_stream(is, fmt, tp)`
2. `from_stream(is, fmt.c_str(), tp)`
3. `from_stream(is, fmt, tp, std::addressof(abbrev))`
4. `from_stream(is, fmt.c_str(), tp, std::addressof(abbrev))`
5. c|from_stream(is, fmt, tp,
static_cast<std::basic_string<CharT, Traits, Alloc>*>(nullptr), &offset)
6. c|from_stream(is, fmt.c_str(), tp,
static_cast<std::basic_string<CharT, Traits, Alloc>*>(nullptr), &offset)
7. `from_stream(is, fmt, tp, std::addressof(abbrev), &offset)`
8. `from_stream(is, fmt.c_str(), tp, std::addressof(abbrev), &offset)`.
The expression `is >> manip` is an lvalue of type `std::basic_istream<CharT, Traits>` with the value `is`.
.
Implementations are recommended to make it difficult to use potentially dangling references to the format string, e.g., by making return types non-movable and preventing `operator>>` from accepting lvalues of return types.

## Parameters


### Parameters


## Format string


## Example


### Example

```cpp
#include <chrono>
#include <iostream>
#include <locale>
#include <sstream>

int main()
{
    auto parse = [&](auto str, auto fmt, auto o)
    {
        std::istringstream is{str};
        is.imbue(std::locale("en_US.utf-8"));
        is >> std::chrono::parse(fmt, o);
        is.fail() ? std::cout << "Parse failed!\n" : std::cout << o << '\n';
    };
    parse("01:02:03", "%H:%M:%S", std::chrono::hours{});
    parse("01:02:03", "%H:%M:%S", std::chrono::minutes{});
    parse("01:02:03", "%H:%M:%S", std::chrono::seconds{});
}
```


**Output:**
```
1h
62min
3723s
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-3554 | C++20 | overloads for plain null-terminated character type sequences were missing | added |


## See also

