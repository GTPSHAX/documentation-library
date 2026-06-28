---
title: std::any::~any
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/any/~any
---

ddcl|since=c++17|
~any();
Destroys the contained object, if any, as if by a call to .

## Example


### Example

```cpp
#include <any>
#include <cstdio>

struct X
{
    X() { std::puts("X::X()"); }
    X(const X&) { std::puts("X::X(const X&)"); }
    ~X() { std::puts("X::~X()"); }
};

int main()
{
    std::any a{X{}<!---->};
    std::puts("Leaving main()...");
}
```


**Output:**
```
X::X()
X::X(const X&)
X::~X()
Leaving main()...
X::~X()
```


## See also


| cpp/utility/any/dsc clear | (see dedicated page) |

