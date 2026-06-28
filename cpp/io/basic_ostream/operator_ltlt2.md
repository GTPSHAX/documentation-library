---
title: operator<<(std::basic_ostream)
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ostream/operator_ltlt2
---


# operator<<small|(std::basic_ostream)


```cpp
**Header:** `<`ostream`>`
dcl|num=1|1=
template< class CharT, class Traits >
basic_ostream<CharT, Traits>&
operator<<( basic_ostream<CharT, Traits>& os, CharT ch );
template< class CharT, class Traits >
basic_ostream<CharT, Traits>&
operator<<( basic_ostream<CharT, Traits>& os, char ch );
template< class Traits >
basic_ostream<char, Traits>&
operator<<( basic_ostream<char, Traits>& os, char ch );
template< class Traits >
basic_ostream<char, Traits>&
operator<<( basic_ostream<char, Traits>& os, signed char ch );
template< class Traits >
basic_ostream<char, Traits>&
operator<<( basic_ostream<char, Traits>& os, unsigned char ch );
dcl|num=2|1=
template< class CharT, class Traits >
basic_ostream<CharT, Traits>&
operator<<( basic_ostream<CharT, Traits>& os, const CharT* s );
template< class CharT, class Traits >
basic_ostream<CharT, Traits>&
operator<<( basic_ostream<CharT, Traits>& os, const char* s );
template< class Traits >
basic_ostream<char, Traits>&
operator<<( basic_ostream<char, Traits>& os, const char* s );
template< class Traits >
basic_ostream<char, Traits>&
operator<<( basic_ostream<char, Traits>& os, const signed char* s );
template< class Traits >
basic_ostream<char, Traits>&
operator<<( basic_ostream<char, Traits>& os, const unsigned char* s );
dcl|num=3|since=c++11|
template< class Ostream, class T >
Ostream&& operator<<( Ostream&& os, const T& value );
dcl|num=4|since=c++20|1=
template< class Traits >
basic_ostream<char, Traits>&
operator<<( basic_ostream<char, Traits>& os, wchar_t ch ) = delete;
template< class Traits >
basic_ostream<char, Traits>&
operator<<( basic_ostream<char, Traits>& os, char8_t ch ) = delete;
template< class Traits >
basic_ostream<char, Traits>&
operator<<( basic_ostream<char, Traits>& os, char16_t ch ) = delete;
template< class Traits >
basic_ostream<char, Traits>&
operator<<( basic_ostream<char, Traits>& os, char32_t ch ) = delete;
template< class Traits >
basic_ostream<wchar_t, Traits>&
operator<<( basic_ostream<wchar_t, Traits>& os, char8_t ch ) = delete;
template< class Traits >
basic_ostream<wchar_t, Traits>&
operator<<( basic_ostream<wchar_t, Traits>& os, char16_t ch ) = delete;
template< class Traits >
basic_ostream<wchar_t, Traits>&
operator<<( basic_ostream<wchar_t, Traits>& os, char32_t ch ) = delete;
template< class Traits >
basic_ostream<char, Traits>&
operator<<( basic_ostream<char, Traits>& os, const wchar_t* s ) = delete;
template< class Traits >
basic_ostream<char, Traits>&
operator<<( basic_ostream<char, Traits>& os, const char8_t* s ) = delete;
template< class Traits >
basic_ostream<char, Traits>&
operator<<( basic_ostream<char, Traits>& os, const char16_t* s ) = delete;
template< class Traits >
basic_ostream<char, Traits>&
operator<<( basic_ostream<char, Traits>& os, const char32_t* s ) = delete;
template< class Traits >
basic_ostream<wchar_t, Traits>&
operator<<( basic_ostream<wchar_t, Traits>& os, const char8_t* s ) = delete;
template< class Traits >
basic_ostream<wchar_t, Traits>&
operator<<( basic_ostream<wchar_t, Traits>& os, const char16_t* s ) = delete;
template< class Traits >
basic_ostream<wchar_t, Traits>&
operator<<( basic_ostream<wchar_t, Traits>& os, const char32_t* s ) = delete;
```

Inserts a character or a character string.
1. Behaves as a *FormattedOutputFunction*. After constructing and checking the `sentry` object, inserts the character `ch`. If `ch` has type `char` and the character container type of `os` is not `char`, `os.widen(ch)` will be inserted instead.
@@ Padding is determined as follows:
* If `os.width() > 1`, then `os.width() - 1` copies of `os.fill()` are added to the output character to form the output character sequence.
* If `1=(out.flags() & std::ios_base::adjustfield) == std::ios_base::left`, the fill characters are placed after the output character, otherwise before.
@@ After insertion, `os.width(0)` is called to cancel the effects of `std::setw`, if any.
2. Behaves as a *FormattedOutputFunction*. After constructing and checking the sentry object, inserts successive characters from the character array whose first element is pointed to by `s`.
* For the first and third overloads (where `CharT` matches the type of `ch`), exactly `traits::length(s)` characters are inserted.
* For the second overload, exactly `std::char_traits<char>::length(s)` characters are inserted.
* For the last two overloads, exactly `traits::length(reinterpret_cast<const char*>(s))` are inserted.
@@ Before insertion, first, all characters are widened using `os.widen()`, then padding is determined as follows:
* If the number of characters to insert is less than `os.width()`, then enough copies of `os.fill()` are added to the character sequence to make its length equal `os.width()`.
* If `1=(out.flags() & std::ios_base::adjustfield) == std::ios_base::left`, the fill characters are added at the end of the output sequence, otherwise they are added before the output sequence.
@@ After insertion, `os.width(0)` is called to cancel the effects of `std::setw`, if any.
@@ If `s` is a null pointer, the behavior is undefined.
3. Calls the appropriate insertion operator, given an rvalue reference to an output stream object (equivalent to `os << value`). .
4. Overloads that accept `char16_t`, `char32_t` etc (or null terminated sequence thereof) are deleted: `std::cout << u'X'` is not allowed. Previously, these would print an integer or pointer value.

## Parameters


### Parameters

- `os` - output stream to insert data to
- `ch` - reference to a character to insert
- `s` - pointer to a character string to insert

## Return value

@1,2@ `os`
3. `std::move(os)`

## Notes

Before , code such as `(std::ostringstream() << 1.2).str()` does not compile.

## Example


### Example

```cpp
#include <fstream>
#include <iostream>

void foo()
{
    // error: operator<< (basic_ostream<char, _Traits>&, char8_t) is deleted
//  std::cout << u8'z' << '\n';
}

std::ostream& operator<<(std::ostream& os, char8_t const& ch)
{
    return os << static_cast<char>(ch);
}

int main()
{
    std::cout << "Hello, world" // uses `const char*` overload
              << '\n';          // uses `char` overload
    std::ofstream{"test.txt"} << 1.2; // uses rvalue overload

    std::cout << u8'!' << '\n'; // uses program-defined operator<<(os, char8_t const&)
}
```


**Output:**
```
Hello, world
!
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-1203 | C++11 | overload for rvalue stream returned<br>lvalue reference to the base class | returns rvalue reference<br>to the derived class |
| lwg-2534 | C++11 | overload for rvalue stream was not constrained | constrained |


## See also


| cpp/io/basic_ostream/dsc operator_ltlt | (see dedicated page) |
| cpp/io/basic_ostream/dsc print | (see dedicated page) |
| cpp/io/basic_ios/dsc widen | (see dedicated page) |

