---
title: std::strstream::strstream
type: Input/output
source: https://en.cppreference.com/w/cpp/io/strstream/strstream
---


```cpp
dcl|num=1|deprecated=c++98|removed=c++26|1=
strstream();
dcl|num=2|deprecated=c++98|removed=c++26|1=
strstream( char* s, int n, std::ios_base::openmode mode =
std::ios_base::in | std::ios_base::out );
```

Constructs new input/output strstream and its underlying `std::strstreambuf`.
1. Default-constructs the underlying `std::strstreambuf`, which creates a dynamically growing buffer, and initializes the base class with the address of the strstreambuf member.
2. Initialized the base class with the address of the underlying `std::strstreambuf` member, which is initialized in one of the two possible ways, both of which use a user-provided fixed-size array:
:@a@ if `1=(mode & app) == 0` (the `app` bit is not set in `mode`), constructs the buffer by calling `strstreambuf(s, n, s)`. The behavior is undefined if there are less than `n` elements in the array whose first element is pointed to by `s`.
:@b@ if `1=(mode & app) != 0` (the `app` bit is set in `mode`), constructs the buffer by calling `strstreambuf(s, n, s + std::strlen(s))`. The behavior is undefined if there are less than `n` elements in the array whose first element is pointed to by `s` or if the array does not contain a valid null-terminated character sequence.

## Parameters


### Parameters

- `s` - `char` array to use as the output buffer
- `n` - size of the array to be used for output
- `mode` -  specifies stream open mode. It is a bitmask type, the following constants are defined (although only `app` is used): 

## Example


### Example

```cpp
#include <iostream>
#include <string>
#include <strstream>

int main()
{
    // dynamic buffer
    std::strstream s1;
    s1 << 1 << ' ' << 3.14 << " example" << std::ends;
    std::cout << "Buffer holds: '" << s1.str() << "'\n";
    s1.freeze(false);

    int n;
    double d;
    std::string w;
    s1 >> n >> d >> w;
    std::cout << "Read back: n = " << n
              << ", d = " << d
              << ", w = '" << w << "'\n";

    // static buffer
    char arr[20] = "-1 -3.14 ";
    std::strstream s2(arr, sizeof arr, std::ios_base::app);
    s2 << "another" << std::ends;
    std::cout << "Buffer holds: '" << s2.str() << "'\n";
    s2 >> n >> d >> w;
    std::cout << "Read back: n = " << n
              << ", d = " << d
              << ", w = '" << w << "'\n";
}
```


**Output:**
```
Buffer holds: '1 3.14 example'
Read back: n = 1, d = 3.14, w = 'example'
Buffer holds: '-1 -3.14 another'
Read back: n = -1, d = -3.14, w = 'another'
```


## Defect reports


## See also


| cpp/io/strstreambuf/dsc strstreambuf | (see dedicated page) |
| cpp/io/strstream/dsc constructor|istrstream | (see dedicated page) |
| cpp/io/strstream/dsc constructor|ostrstream | (see dedicated page) |

