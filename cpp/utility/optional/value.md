---
title: std::optional::value
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/optional/value
---


```cpp
dcl|num=1|since=c++17|1=
constexpr T& value() &;
constexpr const T& value() const &;
dcl|num = 2|since=c++17|1=
constexpr T&& value() &&;
constexpr const T&& value() const &&;
```

If `*this` contains a value, returns a reference to the contained value.
Otherwise, throws a `std::bad_optional_access` exception.

## Parameters

(none)

## Return value

A reference to the contained value.

## Exceptions

`std::bad_optional_access` if `*this` does not contain a value.

## Notes

The dereference operator `operator*()` does not check if this optional contains a value, which may be more efficient than `value()`.

## Example


### Example

```cpp
#include <iostream>
#include <optional>

int main()
{
    std::optional<int> opt = {};

    try
    {
        [[maybe_unused]] int n = opt.value();
    }
    catch(const std::bad_optional_access& e)
    {
        std::cout << e.what() << '\n';
    }

    try
    {
        opt.value() = 42;
    }
    catch(const std::bad_optional_access& e)
    {
        std::cout << e.what() << '\n';
    }

    opt = 43;
    std::cout << *opt << '\n';

    opt.value() = 44;
    std::cout << opt.value() << '\n';
}
<!--|p=true -->
```


**Output:**
```
bad optional access
bad optional access
43
44
```


## See also


| cpp/utility/optional/dsc value_or | (see dedicated page) |
| cpp/utility/optional/dsc operator* | (see dedicated page) |
| cpp/utility/optional/dsc bad_optional_access | (see dedicated page) |

