---
title: std::istrstream::istrstream
type: Input/output
source: https://en.cppreference.com/w/cpp/io/istrstream/istrstream
---


```cpp
dcl|num=1|deprecated=c++98|removed=c++26|1=
explicit istrstream( const char* s );
dcl|num=2|deprecated=c++98|removed=c++26|1=
explicit istrstream( char* s );
dcl|num=3|deprecated=c++98|removed=c++26|1=
istrstream( const char* s, std::streamsize n );
dcl|num=4|deprecated=c++98|removed=c++26|1=
istrstream( char* s, std::streamsize n );
```

Constructs new `std::istrstream` and its underlying `std::strstreambuf`.
@1,2@ Constructs the underlying `std::strstreambuf` by calling `strstreambuf(s, 0)` and initializes the base class with the address of the `strstreambuf`. The behavior is undefined if `s` is not pointing at an element of a null-terminated array.
@3,4@ Constructs the underlying `std::strstreambuf` by calling `strstreambuf(s, n)` and initializes the base class with the address of the `strstreambuf`. The behavior is undefined if `s` is not pointing at an element of an array whose length is at least `n` elements.

## Parameters


### Parameters

- `s` - C-string or char array to use as the contents of the stream
- `n` - size of the array

## Example


### Example

```cpp
#include <iostream>
#include <strstream>

int main()
{
    std::istrstream s1("1 2 3"); // string literal
    int n1, n2, n3;
    if (s1 >> n1 >> n2 >> n3)
        std::cout << n1 << ", " << n2 << ", " << n3 << '\n';

    char arr[] = {'4', ' ', '5', ' ', '6'};
    std::istrstream s2(arr, sizeof arr);
    if (s2 >> n1 >> n2 >> n3)
        std::cout << n1 << ", " << n2 << ", " << n3 << '\n';
}
```


**Output:**
```
1, 2, 3
4, 5, 6
```


## See also


| cpp/io/strstreambuf/dsc strstreambuf | (see dedicated page) |
| cpp/io/strstream/dsc constructor|ostrstream | (see dedicated page) |
| cpp/io/strstream/dsc constructor|strstream | (see dedicated page) |

