---
title: std::any::swap
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/any/swap
---


```cpp
dcl|since=c++17|
void swap( any& other ) noexcept;
```

Swaps the content of two `any` objects.

## Parameters


### Parameters

- `other` - object to swap with

## Example


### Example

```cpp
#include <any>
#include <print>
#include <string>
#include <string_view>

int main()
{
    std::any a = std::string{"King"};
    std::any b = std::string_view{"Queen"};
    std::println("a = {}", std::any_cast<std::string&>(a));
    std::println("b = {}", std::any_cast<std::string_view&>(b));
    std::println("swap(a, b)");
    a.swap(b);
    std::println("a = {}", std::any_cast<std::string_view&>(a));
    std::println("b = {}", std::any_cast<std::string&>(b));
}
```


**Output:**
```
a = King
b = Queen
swap(a, b)
a = Queen
b = King
```

