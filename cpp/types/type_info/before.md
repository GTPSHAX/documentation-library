---
title: std::type_info::before
type: Utilities
source: https://en.cppreference.com/w/cpp/types/type_info/before
---


```cpp
dcla|anchor=no|noexcept=c++11|1=
bool before( const type_info& rhs ) const;
```

Returns `true` if the type of this `type_info` precedes the type of `rhs` in the implementation's collation order. No guarantees are given; in particular, the collation order can change between the invocations of the same program.

## Parameters


### Parameters

- `rhs` - another type information object to compare to

## Return value

`true` if the type of this `type_info` precedes the type of `rhs` in the implementation's collation order.

## Example


### Example

```cpp
#include <iostream>
#include <typeinfo>

int main()
{
    if (typeid(int).before(typeid(char)))
        std::cout << "int goes before char in this implementation.\n";
    else
        std::cout << "char goes before int in this implementation.\n";
}
```


**Output:**
```
char goes before int in this implementation.
```


## See also


| cpp/types/type_info/dsc operator_cmp | (see dedicated page) |

