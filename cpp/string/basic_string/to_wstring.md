---
title: std::to_wstring
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/to_wstring
---


```cpp
**Header:** `<`string`>`
dcl|num=1|since=c++11|
std::wstring to_wstring( int value );
dcl|num=2|since=c++11|
std::wstring to_wstring( long value );
dcl|num=3|since=c++11|
std::wstring to_wstring( long long value );
dcl|num=4|since=c++11|
std::wstring to_wstring( unsigned value );
dcl|num=5|since=c++11|
std::wstring to_wstring( unsigned long value );
dcl|num=6|since=c++11|
std::wstring to_wstring( unsigned long long value );
dcl|num=7|since=c++11|
std::wstring to_wstring( float value );
dcl|num=8|since=c++11|
std::wstring to_wstring( double value );
dcl|num=9|since=c++11|
std::wstring to_wstring( long double value );
```

Converts a numeric value to `std::wstring`.
rrev multi|until1=c++26
|rev1=
Let  be an internal to the conversion functions buffer, sufficiently large to contain the result of conversion.
1. Converts a signed decimal integer to a wide string as if by `std::swprintf(buf, sz, L"%d", value)`.
2. Converts a signed decimal integer to a wide string as if by `std::swprintf(buf, sz, L"%ld", value)`.
3. Converts a signed decimal integer to a wide string  as if by `std::swprintf(buf, sz, L"%lld", value)`.
4. Converts an unsigned decimal integer to a wide string as if by `std::swprintf(buf, sz, L"%u", value)`.
5. Converts an unsigned decimal integer to a wide string as if by `std::swprintf(buf, sz, L"%lu", value)`.
6. Converts an unsigned decimal integer to a wide string as if by `std::swprintf(buf, sz, L"%llu", value)`.
@7,8@ Converts a floating point value to a wide string as if by `std::swprintf(buf, sz, L"%f", value)`.
9. Converts a floating point value to a wide string as if by `std::swprintf(buf, sz, L"%Lf", value)`.
|rev2=
@1-9@ Converts a numeric value to a wide string as if by }.

## Parameters


### Parameters

- `value` - a numeric value to convert

## Return value

A wide string holding the converted value.

## Exceptions

May throw `std::bad_alloc` from the `std::wstring` constructor.

## Example


### Example

```cpp
#include <iostream>
#include <string>

int main()
{
    for (const double f : {23.43, 1e-9, 1e40, 1e-40, 123456789.0})
        std::wcout << "std::wcout: " << f << '\n'
                   << "to_wstring: " << std::to_wstring(f) << "\n\n";
}
```


**Output:**
```
std::wcout: 23.43
to_wstring: 23.430000

std::wcout: 1e-09
to_wstring: 0.000000

std::wcout: 1e+40
to_wstring: 10000000000000000303786028427003666890752.000000

std::wcout: 1e-40
to_wstring: 0.000000

std::wcout: 1.23457e+08
to_wstring: 123456789.000000
```


## See also


| cpp/string/basic_string/dsc to_string | (see dedicated page) |

