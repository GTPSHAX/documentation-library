---
title: std::basic_stringbuf::swap
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_stringbuf/swap
---


```cpp
dcl rev multi
|since1=c++11|dcl1=
void swap( basic_stringbuf& rhs );
|since2=c++20|dcl2=
void swap( basic_stringbuf& rhs ) noexcept(/* see below */);
```

Swaps the state and the contents of `*this` and `rhs`.
rrev|since=c++11|
The behavior is undefined if `Allocator` does not propagate on swap and the allocators of `*this` and `other` are unequal.

## Parameters


### Parameters

- `rhs` - another `basic_stringbuf`

## Return value

(none)

## Exceptions

rrev multi
|since1=c++11|rev1=
|since2=c++20|rev2=
noexcept|std::allocator_traits<Allocator>::propagate_on_container_swap::value
std::allocator_traits<Allocator>::is_always_equal::value

## Notes

This function is called automatically when swapping `std::stringstream` objects. It is rarely necessary to call it directly.

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>

int main()
{
    std::istringstream one("one");
    std::ostringstream two("two");

    std::cout << "Before swap: one = " << std::quoted(one.str())
              << ", two = " << std::quoted(two.str()) << ".\n";

    one.rdbuf()->swap(*two.rdbuf());

    std::cout << "After  swap: one = " << std::quoted(one.str())
              << ", two = " << std::quoted(two.str()) << ".\n";
}
```


**Output:**
```
Before swap: one = "one", two = "two".
After  swap: one = "two", two = "one".
```


## See also


| cpp/io/basic_stringbuf/dsc constructor | (see dedicated page) |
| cpp/io/basic_stringstream/dsc swap|basic_stringstream | (see dedicated page) |

