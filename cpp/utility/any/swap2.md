---
title: std::swap(std::any)
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/any/swap2
---


# swapsmall|(std::any)

ddcl|header=any|since=c++17|
void swap( any& lhs, any& rhs ) noexcept;
Overloads the `std::swap` algorithm for `std::any`. Swaps the content of two `any` objects by calling `lhs.swap(rhs)`.

## Parameters


### Parameters

- `lhs, rhs` - objects to swap

## Example


### Example

```cpp
#include <any>
#include <print>
#include <string>

int main()
{
    std::any p = 42, q = std::string{"Bishop"};
    std::println("p: {}, q: {}", std::any_cast<int>(p), std::any_cast<std::string&>(q));
    std::println("swap(p, q)");
    std::swap(p, q);
    std::println("p: {}, q: {}", std::any_cast<std::string&>(p), std::any_cast<int>(q));
}
```


**Output:**
```
p: 42, q: Bishop
swap(p, q)
p: Bishop, q: 42
```


## See also


| cpp/utility/any/dsc swap | (see dedicated page) |

