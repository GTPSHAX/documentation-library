---
title: std::shared_ptr::unique
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/shared_ptr/unique
---

ddcl|deprecated=c++17|removed=c++20|
bool unique() const noexcept;
Checks if `*this` is the only `shared_ptr` instance managing the current object, i.e. whether `1=use_count() == 1`.

## Parameters

(none)

## Return value

`true` if `*this` is the only `shared_ptr` instance managing the current object, `false` otherwise.

## Notes

This function was deprecated in C++17 and removed in C++20 because `1=use_count() == 1` is meaningless in multithreaded environment (see `Notes` in `use_count`).

## Example


### Example

```cpp
#include <iostream> 
#include <memory> 

int main() 
{ 
    auto sp1 = std::make_shared<int>(5);
    std::cout << std::boolalpha;
    std::cout << "sp1.unique() == " << sp1.unique() << '\n'; 

    std::shared_ptr<int> sp2 = sp1; 
    std::cout << "sp1.unique() == " << sp1.unique() << '\n'; 
}
```


**Output:**
```
sp1.unique() == true
sp1.unique() == false
```


## See also


| cpp/memory/shared_ptr/dsc use_count | (see dedicated page) |

