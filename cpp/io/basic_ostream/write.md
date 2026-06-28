---
title: std::basic_ostream::write
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ostream/write
---

ddcl|
basic_ostream& write( const char_type* s, std::streamsize count );
Behaves as an *UnformattedOutputFunction*. After constructing and checking the sentry object, outputs the characters from successive locations in the character array whose first element is pointed to by `s`. Characters are inserted into the output sequence until one of the following occurs:
* exactly `count` characters are inserted
* inserting into the output sequence fails (in which case `setstate(badbit)` is called).

## Parameters


### Parameters

- `s` - pointer to the character string to write
- `count` - number of characters to write

## Return value

`*this`

## Exceptions


## Notes

This function is not overloaded for the types `signed char` or `unsigned char`, unlike the formatted `operator<<`.
Also, unlike the formatted output functions, this function does not set the `failbit` on failure.
When using a non-converting locale (the default locale is non-converting), the overrider of this function in `std::basic_ofstream` may be optimized for zero-copy bulk I/O (by means of overriding `std::streambuf::xsputn`).

## Example


### Example

```cpp
#include <iostream>

int main()
{
    int n = 0x41424344;
    std::cout.write(reinterpret_cast<char*>(&n), sizeof n) << '\n';

    char c[] = "This is sample text.";
    std::cout.write(c, 4).write("!\n", 2);
}
```


**Output:**
```
DCBA
This!
```


## See also


| cpp/io/basic_ostream/dsc operator_ltlt2 | (see dedicated page) |
| cpp/io/basic_ostream/dsc put | (see dedicated page) |

