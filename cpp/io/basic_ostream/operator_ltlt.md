---
title: std::basic_ostream::operator<<
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ostream/operator_ltlt
---


```cpp
dcl|num=1|
basic_ostream& operator<<( bool value );
dcla|num=2|
basic_ostream& operator<<( long value );
dcl|num=3|
basic_ostream& operator<<( unsigned long value );
dcl|num=4|since=c++11|
basic_ostream& operator<<( long long value );
dcl|num=5|since=c++11|
basic_ostream& operator<<( unsigned long long value );
dcl|num=6|
basic_ostream& operator<<( double value );
dcl|num=7|
basic_ostream& operator<<( long double value );
dcla|num=8|
basic_ostream& operator<<( const void* value );
dcl|num=9|since=c++23|
basic_ostream& operator<<( const volatile void* value );
dcl|num=10|since=c++17|
basic_ostream& operator<<( std::nullptr_t );
dcla|num=11|
basic_ostream& operator<<( short value );
dcl|num=12|
basic_ostream& operator<<( int value );
dcl|num=13|
basic_ostream& operator<<( unsigned short value );
dcl|num=14|
basic_ostream& operator<<( unsigned int value );
dcl|num=15|
basic_ostream& operator<<( float value );
dcl|num=16|since=c++23|
basic_ostream& operator<<( /* extended-floating-point-type */ value );
dcl|num=17|
basic_ostream& operator<<( std::basic_streambuf<CharT, Traits>* sb );
dcla|num=18|
basic_ostream& operator<<(
std::ios_base& (*func)(std::ios_base&) );
dcl|num=19|
basic_ostream& operator<<(
std::basic_ios<CharT, Traits>& (*func)(std::basic_ios<CharT, Traits>&) );
dcl|num=20|
basic_ostream& operator<<(
std::basic_ostream<CharT, Traits>& (*func)
(std::basic_ostream<CharT, Traits>&) );
```

Inserts data into the stream.
@1-8@ Inserts `value`.
@@ This function behaves as a *FormattedOutputFunction*. After constructing and checking the sentry object, inserts a value by calling . If the end of file condition was encountered during output (`1=put().failed() == true`), sets `badbit`.
9. Equivalent to `return operator<<(const_cast<const void*>(p));`.
10. Equivalent to `return *this << s;`, where `s` is an implementation-defined null-terminated character type string.
11. Inserts a value from `short` `value`.
@@ This function behaves as a *FormattedOutputFunction*. After constructing and checking the sentry object, inserts a `long` value `lval` as in , where `lval` is
* `static_cast<long>(static_cast<unsigned short>(value))`, if `flags() & std::ios_base::basefield` is `std::ios_base::oct` or `std::ios_base::hex`, or
* `static_cast<long>(value)` otherwise.
12. Inserts a value from `int` `value`.
@@ This function behaves as a *FormattedOutputFunction*. After constructing and checking the sentry object, inserts a `long` value `lval` as in , where `lval` is
* `static_cast<long>(static_cast<unsigned int>(value))`, if `flags() & std::ios_base::basefield` is `std::ios_base::oct` or `std::ios_base::hex`, or
* `static_cast<long>(value)` otherwise.
@13,14@ Inserts a value from `unsigned short` or `unsigned int` `value`.
@@ This function behaves as a *FormattedOutputFunction*. After constructing and checking the sentry object, inserts `static_cast<unsigned long>(value)` as in .
15. Inserts a value from `float` `value`.
@@ This function behaves as a *FormattedOutputFunction*. After constructing and checking the sentry object, inserts `static_cast<double>(value)` as in .
16. Inserts a value from `value`. The library provides overloads for all cv-unqualified extended floating-point types as the type of the parameter value.
@@ This function behaves as a *FormattedOutputFunction*. After constructing and checking the sentry object, checks the floating-point conversion rank of `/* extended-floating-point-type */`:
* If the rank is less than or equal to that of `double`, inserts `static_cast<double>(value)` as in .
* Otherwise, if the rank is less than or equal to that of `long double`, inserts `static_cast<long double>(value)` as in .
* Otherwise, an invocation of this overload is conditionally supported with implementation-defined semantics.
17. This function behaves as an *UnformattedOutputFunction*. After constructing and checking the sentry object, checks if `sb` is a null pointer. If it is, executes `setstate(badbit)` and exits. Otherwise, extracts characters from the input sequence controlled by `sb` and inserts them into `*this` until one of the following conditions are met:
:* end-of-file occurs on the input sequence;
:* inserting in the output sequence fails (in which case the character to be inserted is not extracted);
:* an exception occurs (in which case the exception is caught).
If no characters were inserted, executes `setstate(failbit)`. If an exception was thrown while extracting, sets `failbit` and, if `failbit` is set in `exceptions()`, rethrows the exception.
@18-20@ Calls `func(*this)`. These overloads are used to implement output I/O manipulators such as `std::endl`.

## Parameters


### Parameters

- `value` - integer, floating-point, boolean, or pointer value to insert
- `func` - function to call
- `sb` - pointer to the stream buffer to read the data from

## Return value

@1-19@ `*this`
20. `func(*this)`

## Notes

There are no overloads for pointers to non-static members<sup>(until C++23)</sup> , pointers to volatiles, or function pointers (other than the ones with signatures accepted by the  overloads).
* Attempting to output such objects invokes implicit conversion to `bool`, and, for any non-null pointer value, the value `1` is printed (unless `boolalpha` was set, in which case `true` is printed).
Character and character string arguments (e.g., of type `char` or `const char*`) are handled by the `non-member overloads` of `operator<<`.
* Attempting to output a character using the member function call syntax (e.g., `std::cout.operator<<('c');`) will call one of the overloads in  or  and output the numerical value.
* Attempting to output a character string using the member function call syntax will call overload  and print the pointer value instead.
Overload  was added by the resolution of , but it is never implemented in any standard library implementation under C++11/14 modes.

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <sstream>

int fun() { return 42; }

int main()
{
    std::istringstream input(" \"Some text.\" ");
    double f = 3.14;
    bool b = true;

    std::cout
        << fun()          // int overload (12)
        << ' '            // non-member overload
        << std::boolalpha // function overload (18)
        << b              // bool overload (1)
        << " "            // non-member overload
        << std::fixed     // function overload (18) again
        << f              // double overload (6)
        << input.rdbuf()  // streambuf overload
        << fun            // bool overload (1): there's no overload for int(*)()
        << std::endl;     // function overload (18) again

    int x = 0;
    int* p1 = &x;
    volatile int* p2 = &x;
    std::cout
        << "p1: " << p1 << '\n'  // `const void*` overload, prints address
        << "p2: " << p2 << '\n'; // before C++23 (P1147): bool overload :), because
            // operator<<(const void*) is not a match, as it discards the `volatile`
            // qualifier. To fix this, C++23 adds `const volatile void*` overload (9),
            // that prints the address as expected.
}
```


**Output:**
```
42 true 3.140000 "Some text." true
p1: 0x7ffcea766600
p2: 0x7ffcea766600
```


## Defect reports


## See also


| cpp/io/basic_ostream/dsc operator ltlt2 | (see dedicated page) |
| cpp/string/basic_string/dsc operator ltltgtgt | (see dedicated page) |
| cpp/string/basic_string_view/dsc operator ltlt | (see dedicated page) |
| cpp/utility/bitset/dsc operator ltltgtgt2 | (see dedicated page) |
| cpp/numeric/complex/dsc operator ltltgtgt | (see dedicated page) |
| cpp/numeric/random/engine/dsc operator ltltgtgt|linear_congruential_engine | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator ltltgtgt|uniform_int_distribution | (see dedicated page) |
| cpp/io/basic_ostream/dsc put | (see dedicated page) |
| cpp/io/basic_ostream/dsc write | (see dedicated page) |
| cpp/utility/dsc to_chars | (see dedicated page) |

