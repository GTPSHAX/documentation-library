---
title: std::istrstream::~istrstream
type: Input/output
source: https://en.cppreference.com/w/cpp/io/istrstream/~istrstream
---

ddcl|deprecated=c++98|removed=c++26|1=
virtual ~istrstream();
Destroys a `std::istrstream` object, which also destroys the member `std::strstreambuf`.

## Parameters

(none)

## Notes

The constructors of `std::istrstream` do not create the underlying `std::strstreambuf` in dynamically allocated mode, so the memory leaks that are possible with `std::ostrstream::~ostrstream` or `std::strstream::~strstream` do not apply.

## Example


### Example

```cpp
#include <iostream>
#include <strstream>

int main()
{
    {
        std::istrstream s("1.234");
        double d;
        s >> d;
        std::cout << d << '\n';
    } // destructor called
}
```


**Output:**
```
1.234
```

