---
title: std::basic_istream::operator>>
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_istream/operator_gtgt
---


```cpp
dcl|num=1|
basic_istream& operator>>( unsigned short& value );
dcl|num=2|
basic_istream& operator>>( unsigned int& value );
dcl|num=3|
basic_istream& operator>>( long& value );
dcl|num=4|
basic_istream& operator>>( unsigned long& value );
dcl|num=5|since=c++11|
basic_istream& operator>>( long long& value );
dcl|num=6|since=c++11|
basic_istream& operator>>( unsigned long long& value );
dcl|num=7|
basic_istream& operator>>( float& value );
dcl|num=8|
basic_istream& operator>>( double& value );
dcl|num=9|
basic_istream& operator>>( long double& value );
dcl|num=10|
basic_istream& operator>>( bool& value );
dcl|num=11|
basic_istream& operator>>( void*& value );
dcl|num=12|
basic_istream& operator>>( short& value );
dcl|num=13|
basic_istream& operator>>( int& value );
dcla|num=14|since=c++23|
basic_istream& operator>>( /* extended-floating-point-type */& value );
dcl|num=15|
basic_istream& operator>>( std::ios_base& (*func)(std::ios_base&) );
dcl|num=16|
basic_istream& operator>>( std::basic_ios<CharT, Traits>&
(*func)(std::basic_ios<CharT, Traits>&) );
dcl|num=17|
basic_istream& operator>>( basic_istream& (*func)(basic_istream&) );
dcl|num=18|
basic_istream& operator>>( std::basic_streambuf<CharT, Traits>* sb );
```

Extracts values from an input stream.
@1-11@ Extracts a value potentially skipping preceding whitespace. The value is stored to a given reference `value`.
@@ This function behaves as a *FormattedInputFunction*. After constructing and checking the sentry object, which may skip leading whitespace, extracts a value by calling .
12. Extracts a `short` value potentially skipping preceding whitespace. The value is stored to a given reference `value`.
@@ This function behaves as a *FormattedInputFunction*. After constructing and checking the sentry object, which may skip leading whitespace, extracts a `long` value `lval` by calling . After that:
* If `lval < std::numeric_limits<short>::min()`, sets `failbit` and stores `std::numeric_limits<short>::min()` to `val`.
* Otherwise, if `std::numeric_limits<short>::max() < lval`, sets `failbit` and stores `std::numeric_limits<short>::max()` to `val`.
* Otherwise, stores `static_cast<short>(lval)` to `val`.
13. Extracts an `int` value potentially skipping preceding whitespace. The value is stored to a given reference `value`.
@@ This function behaves as a *FormattedInputFunction*. After constructing and checking the sentry object, which may skip leading whitespace, extracts a `long` value `lval` by calling . After that:
* If `lval < std::numeric_limits<int>::min()`, sets `failbit` and stores `std::numeric_limits<int>::min()` to `val`.
* Otherwise, if `std::numeric_limits<int>::max() < lval`, sets `failbit` and stores `std::numeric_limits<int>::max()` to `val`.
* Otherwise, stores `static_cast<int>(lval)` to `val`.
14. Extracts an extended floating-point value potentially skipping preceding whitespace. The value is stored to a given reference `value`. The library provides overloads for all cv-unqualified extended floating-point types as the referenced type of the parameter `value`.
@@ Determines the standard floating-point type `FP` as follows:
* If the floating-point conversion rank of `/* extended-floating-point-type */` is less than or equal to that of `float`, then `FP` is `float`.
* Otherwise, if the floating-point conversion rank of `/* extended-floating-point-type */` is less than or equal to that of `double`, then `FP` is `double`.
* Otherwise, `FP` is `long double`.
@@ This function behaves as a *FormattedInputFunction*. After constructing and checking the sentry object, which may skip leading whitespace, extracts an `FP` value `fval` by calling . After that:
* If `fval < -std::numeric_limits</* extended-floating-point-type */>::max()`, sets `failbit` and stores `-std::numeric_limits</* extended-floating-point-type */>::max()` to `val`.
* Otherwise, if `std::numeric_limits</* extended-floating-point-type */>::max() < fval`, sets `failbit` and stores `std::numeric_limits</* extended-floating-point-type */>::max()` to `val`.
* Otherwise, stores `static_cast</* extended-floating-point-type */>(fval)` to `val`.
@15-17@ Calls `func(*this)`, where `func` is an I/O manipulator.
18. Behaves as an *UnformattedInputFunction*. After constructing and checking the sentry object, extracts all data from `*this` and stores it to `sb`. The extraction stops if one of the following conditions are met:
:* end-of-file occurs on the input sequence;
:* inserting in the output sequence fails (in which case the character to be inserted is not extracted);
:* an exception occurs (in which case the exception is caught, and only rethrown if it inserted no characters and `failbit` is enabled in `exceptions()`).
In either case, stores the number of characters extracted in the member variable accessed by subsequent calls to `gcount()`. If `sb` is a null pointer or if no characters were inserted into `sb`, calls `setstate(failbit)` (which may throw `std::ios_base::failure` if enabled).
If extraction fails (e.g. if a letter was entered where a digit is expected), zero is written to `value` and `failbit` is set. For signed integers, if extraction results in the value too large or too small to fit in `value`, `std::numeric_limits<T>::max()` or `std::numeric_limits<T>::min()` (respectively) is written and `failbit` flag is set. For unsigned integers, if extraction results in the value too large or too small to fit in `value`, `std::numeric_limits<T>::max()` is written and `failbit` flag is set.

## Parameters


### Parameters

- `value` - reference to an integer or floating-point value to store the extracted value to
- `func` - pointer to I/O manipulator function
- `sb` - pointer to the stream buffer to write all the data to

## Return value

@1-16,18@ `*this`
17. `func(*this)`

## Notes

For overload , when the extended floating-point type has a floating-point conversion rank that is not equal to the rank of any standard floating-point type, then double rounding during the conversion can result in inaccurate results.  can be used in situations where maximum accuracy is important.

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <sstream>

int main()
{
    std::string input = "41 3.14 false hello world";
    std::istringstream stream(input);

    int n;
    double f;
    bool b;

    stream >> n >> f >> std::boolalpha >> b;
    std::cout << "n = " << n << '\n'
              << "f = " << f << '\n'
              << "b = " << std::boolalpha << b << '\n';

    // extract the rest using the streambuf overload
    stream >> std::cout.rdbuf();
    std::cout << '\n';
}
```


**Output:**
```
n = 41
f = 3.14
b = false
hello world
```


## Defect reports


## See also


| cpp/io/basic_istream/dsc operator gtgt2 | (see dedicated page) |
| cpp/string/basic_string/dsc operator ltltgtgt | (see dedicated page) |
| cpp/utility/bitset/dsc operator ltltgtgt2 | (see dedicated page) |
| cpp/numeric/complex/dsc operator ltltgtgt | (see dedicated page) |
| cpp/numeric/random/engine/dsc operator ltltgtgt|linear_congruential_engine | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator ltltgtgt|uniform_int_distribution | (see dedicated page) |
| cpp/io/basic_istream/dsc read | (see dedicated page) |
| cpp/io/basic_istream/dsc readsome | (see dedicated page) |
| cpp/io/basic_istream/dsc get | (see dedicated page) |
| cpp/io/basic_istream/dsc getline | (see dedicated page) |
| cpp/utility/dsc from_chars | (see dedicated page) |

