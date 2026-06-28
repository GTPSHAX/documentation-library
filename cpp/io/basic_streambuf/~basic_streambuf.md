---
title: std::basic_streambuf::~basic_streambuf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/~basic_streambuf
---


```cpp
dcl|1=
virtual ~basic_streambuf();
```

This destructor has no effect: the members of this `basic_streambuf` (the pointers and the locale) are destructed in accordance with the usual object destruction sequence after this destructor returns. However, since it is declared public virtual, it allows the objects that are derived from `std::basic_streambuf` to be deleted through a pointer to base class.

## Parameters

(none)

## Example


### Example

```cpp
#include <fstream>
#include <iostream>

int main()
{
    std::filebuf* fbp = new std::filebuf;
    fbp->open("test.txt", std::ios_base::out);
    fbp->sputn("Hello\n", 6);

    std::streambuf* sbp = fbp;
    delete sbp; // the file is closed, output flushed and written

    std::ifstream f("test.txt");
    std::cout << f.rdbuf(); // proof
}
```


**Output:**
```
Hello
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-54 | C++98 | the effect of the destructor was not specified | specified as no effect |


## See also


| cpp/io/basic_streambuf/dsc basic_streambuf | (see dedicated page) |

