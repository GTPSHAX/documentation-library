---
title: std::optional::or_else
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/optional/or_else
---


```cpp
dcl|num=1|since=c++23|
template< class F >
constexpr optional or_else( F&& f ) const&;
dcl|num=2|since=c++23|
template< class F >
constexpr optional or_else( F&& f ) &&;
```

Returns `*this` if it contains a value. Otherwise, returns the result of `f`.
The program is ill-formed if `std::remove_cvref_t<std::invoke_result_t<F>>` is not same as `std::optional<T>`.
1. Equivalent to `return *this ? *this : std::forward<F>(f)();`. .
2. Equivalent to `return *this ? std::move(*this) : std::forward<F>(f)();`. .

## Parameters


### Parameters

- `f` - a function or *Callable* object that returns an `std::optional<T>`

## Return value

`*this` or the result of `f`, as described above.

## Notes


## Example


### Example

```cpp
#include <iostream>
#include <optional>
#include <string>

int main()
{
    using maybe_int = std::optional<int>;

    auto valueless = []
    {
        std::cout << "Valueless: ";
        return maybe_int{0};
    };

    maybe_int x;
    std::cout << x.or_else(valueless).value() << '\n';

    x = 42;
    std::cout << "Has value: ";
    std::cout << x.or_else(valueless).value() << '\n';

    x.reset();
    std::cout << x.or_else(valueless).value() << '\n';
}
```


**Output:**
```
Valueless: 0
Has value: 42
Valueless: 0
```


## See also


| cpp/utility/optional/dsc value_or | (see dedicated page) |
| cpp/utility/optional/dsc and_then | (see dedicated page) |
| cpp/utility/optional/dsc transform | (see dedicated page) |

