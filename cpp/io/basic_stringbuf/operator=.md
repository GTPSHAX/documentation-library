---
title: std::basic_stringbuf::operator=
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_stringbuf/operator=
---


```cpp
dcl|since=c++11|num=1|1=
std::basic_stringbuf& operator=( std::basic_stringbuf&& rhs );
dcl|num=2|1=
std::basic_stringbuf& operator=( const std::basic_stringbuf& rhs ) = delete;
```

1. Move assignment operator: Moves the contents of `rhs` into `*this`. After the move, `*this` has the associated string, the open mode, the locale, and all other state formerly held by `rhs`. The six pointers of `std::basic_streambuf` in `*this` are guaranteed to be different from the corresponding pointers in the moved-from `rhs` unless null.
2. The copy assignment operator is deleted; `basic_stringbuf` is not *CopyAssignable*.

## Parameters


### Parameters

- `rhs` - another `basic_stringbuf` that will be moved from

## Return value

`*this`

## Example


### Example

```cpp
#include <iostream>
#include <sstream>
#include <string>

int main()
{
    std::istringstream one("one");
    std::ostringstream two("two");

    std::cout << "Before move, one = \"" << one.str() << '"'
              << " two = \"" << two.str() << "\"\n";

    *one.rdbuf() = std::move(*two.rdbuf());

    std::cout << "After move, one = \"" << one.str() << '"'
              << " two = \"" << two.str() << "\"\n";
}
```


**Output:**
```
Before move, one = "one" two = "two"
After move, one = "two" two = ""
```


## See also


| cpp/io/basic_stringbuf/dsc constructor | (see dedicated page) |

