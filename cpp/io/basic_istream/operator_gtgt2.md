---
title: operator>>(std::basic_istream)
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_istream/operator_gtgt2
---


# operator>>small|(std::basic_istream)


```cpp
**Header:** `<`istream`>`
dcl|num=1|
template< class CharT, class Traits >
basic_istream<CharT, Traits>&
operator>>( basic_istream<CharT, Traits>& st, CharT& ch );
template< class Traits >
basic_istream<char, Traits>&
operator>>( basic_istream<char, Traits>& st, signed char& ch );
template< class Traits >
basic_istream<char, Traits>&
operator>>( basic_istream<char, Traits>& st, unsigned char& ch );
dcl rev multi|num=2|until1=c++20|dcl1=
template< class CharT, class Traits>
basic_istream<CharT, Traits>&
operator>>( basic_istream<CharT, Traits>& st, CharT* s );
template< class Traits >
basic_istream<char, Traits>&
operator>>( basic_istream<char, Traits>& st, signed char* s );
template< class Traits >
basic_istream<char, Traits>&
operator>>( basic_istream<char, Traits>& st, unsigned char* s );
|dcl2=
template< class CharT, class Traits, std::size_t N >
basic_istream<CharT, Traits>&
operator>>( basic_istream<CharT, Traits>& st, CharT (&s)[N] );
template< class Traits, std::size_t N >
basic_istream<char, Traits>&
operator>>( basic_istream<char, Traits>& st, signed char (&s)[N] );
template< class Traits, std::size_t N >
basic_istream<char, Traits>&
operator>>( basic_istream<char, Traits>& st, unsigned char (&s)[N] );
dcl|num=3|since=c++11|
template< class Istream, class T >
Istream&&
operator>>( Istream&& st, T&& value );
```

@1,2@ Performs character input operations.
1. Behaves as a *FormattedInputFunction*. After constructing and checking the sentry object, which may skip leading whitespace, extracts a character and stores it to `ch`. If no character is available, sets `cpp/io/ios_base/iostate|failbit` (in addition to `cpp/io/ios_base/iostate|eofbit` that is set as required of a *FormattedInputFunction*).
2. Behaves as a *FormattedInputFunction*. After constructing and checking the sentry object, which may skip leading whitespace, extracts successive characters and stores them at successive locations of <sup>(until C++20)</sup> a character array whose first element is pointed to by `s`. The extraction stops if any of the following conditions is met:
* A whitespace character (as determined by the `cpp/locale/ctype|ctype<CharT>` facet) is found. The whitespace character is not extracted.
rrev multi|until1=c++20|rev1=
* If `st.width()` is greater than zero, `st.width() - 1` characters are stored.
|rev2=
* `n - 1` characters are stored, where `n` is defined as follows:
:* If `st.width()` is greater than zero, `std::min(std::size_t(st.width()), N)`;
:* otherwise, `n` is `N`.
* End of file occurs in the input sequence (this also sets `cpp/io/ios_base/iostate|eofbit`).
In either case, an additional null character value `CharT()` is stored at the end of the output. If no characters were extracted, sets `cpp/io/ios_base/iostate|failbit` (the null character is still written, to the first position in the output). Finally, calls `st.width(0)` to cancel the effects of `std::setw`, if any.
3. Calls the appropriate extraction operator, given an rvalue reference to an input stream object (equivalent to `st >> std::forward<T>(value)`). .

## Notes

Extracting a single character that is the last character of the stream does not set `eofbit`: this is different from other formatted input functions, such as extracting the last integer with `operator>>`, but this behavior matches the behavior of `std::scanf` with `"%c"` format specifier.

## Parameters


### Parameters

- `st` - input stream to extract the data from
- `ch` - reference to a character to store the extracted character to
- `s` - <sup>(until C++20)</sup> pointer to a character array to store the extracted characters to

## Return value

@1,2@ `st`
3. `std::move(st)`

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <sstream>

int main()
{
    std::string input = "n greetings";
    std::istringstream stream(input);

    char c;
    const int MAX = 6;
    char cstr[MAX];

    stream >> c >> std::setw(MAX) >> cstr;
    std::cout << "c = " << c << '\n'
              << "cstr = " << cstr << '\n';

    double f;
    std::istringstream("1.23") >> f; // rvalue stream extraction
    std::cout << "f = " << f << '\n';
}
```


**Output:**
```
c = n
cstr = greet
f = 1.23
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-68 | C++98 | no null characters were stored at the end of the output for overload (2) | stores a null character |
| lwg-1203 | C++98 | overload for rvalue stream returned lvalue reference to the base class | returns rvalue reference<br>to the derived class |
| lwg-2328 | C++98 | overload for rvalue stream required another argument to be lvalue | made to accept rvalue |
| lwg-2534 | C++98 | overload for rvalue stream was not constrained | constrained |


## See also


| cpp/io/basic_istream/dsc operator_gtgt | (see dedicated page) |

