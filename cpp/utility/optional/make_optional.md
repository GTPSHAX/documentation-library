---
title: std::make_optional
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/optional/make_optional
---


```cpp
**Header:** `<`optional`>`
dcl|num=1|since=c++17|1=
template< class T >
constexpr std::optional<std::decay_t<T>> make_optional( T&& value );
dcla|num=2|since=c++17|1=
template< class T, class... Args >
constexpr std::optional<T> make_optional( Args&&... args );
dcl|num=3|since=c++17|1=
template< class T, class U, class... Args >
constexpr std::optional<T> make_optional( std::initializer_list<U> il,
Args&&... args );
```

1. Creates an optional object from `value`. Effectively calls `std::optional<std::decay_t<T>>(std::forward<T>(value))`.
2. Creates an optional object constructed in-place from `args...`. Equivalent to `return std::optional<T>(std::in_place, std::forward<Args>(args)...);`.<br>.
3. Creates an optional object constructed in-place from `il` and `args...`. Equivalent to `return std::optional<T>(std::in_place, il, std::forward<Args>(args)...);`.<br>.

## Parameters


### Parameters

- `value` - the value to construct optional object with
- `il, args` - arguments to be passed to the constructor of `T`

## Return value

The constructed optional object.

## Exceptions

Throws any exception thrown by the constructor of `T`.

## Notes

`T` need not be movable for overloads  due to guaranteed copy elision.

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <optional>
#include <string>
#include <vector>

int main()
{
    auto op1 = std::make_optional<std::vector<char>>({'a','b','c'});
    std::cout << "op1: ";
    for (char c : op1.value())
        std::cout << c << ',';
    auto op2 = std::make_optional<std::vector<int>>(5, 2);
    std::cout << "\nop2: ";
    for (int i : *op2)
        std::cout << i << ',';
    std::string str{"hello world"};
    auto op3 = std::make_optional<std::string>(std::move(str));
    std::cout << "\nop3: " << std::quoted(op3.value_or("empty value")) << '\n';
    std::cout << "str: " << std::quoted(str) << '\n';
}
```


**Output:**
```
op1: a,b,c,
op2: 2,2,2,2,2,
op3: "hello world"
str: ""
```


## See also


| cpp/utility/optional/dsc constructor | (see dedicated page) |

