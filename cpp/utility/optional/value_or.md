---
title: std::optional::value_or
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/optional/value_or
---


```cpp
dcl|num=1|since=c++17|1=
template< class U = std::remove_cv_t<T> >
constexpr T value_or( U&& default_value ) const&;
dcl|num=2|since=c++17|1=
template< class U = std::remove_cv_t<T> >
constexpr T value_or( U&& default_value ) &&;
```

Returns the contained value if `*this` contains a value, otherwise returns `default_value`.
1. If `std::is_copy_constructible_v<T> && std::is_convertible_v<U&&, T>` is `false`, the program is ill-formed.
2. If `std::is_move_constructible_v<T> && std::is_convertible_v<U&&, T>` is `false`, the program is ill-formed.

## Parameters


### Parameters

- `default_value` - the value to be returned if `*this` does not contain a value

## Return value

1. `has_value() ? **this : static_cast<T>(std::forward<U>(default_value));`
2. `has_value() ? std::move(**this) : static_cast<T>(std::forward<U>(default_value))`

## Example


### Example

```cpp
#include <cstdlib>
#include <iostream>
#include <optional>

std::optional<const char*> maybe_getenv(const char* n)
{
    if (const char* x = std::getenv(n))
        return x;
    else
        return {};
}

int main()
{
    std::cout << maybe_getenv("SHELL").value_or("(none)") << '\n';
    std::cout << maybe_getenv("MYPWD").value_or("(none)") << '\n';
}
```


**Output:**
```
/usr/bin/zsh
(none)
```


## Defect reports


## See also


| cpp/utility/optional/dsc value | (see dedicated page) |

