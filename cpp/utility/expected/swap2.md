---
title: swap(std::expected)
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/expected/swap2
---


# swappetty|(std::expected)


```cpp
dcl|since=c++23|
friend constexpr void swap( expected& lhs, expected& rhs ) noexcept(/*see below*/);
```

Overloads the `std::swap` algorithm for `std::expected`. Exchanges the state of `lhs` with that of `rhs`. Effectively calls `lhs.swap(rhs)`.
.

## Parameters


### Parameters

- `lhs, rhs` - `expected` objects whose states to swap

## Return value

(none)

## Exceptions


## Example


### Example

```cpp
#include <expected>
#include <iostream>
#include <string>

using Ex = std::expected<std::string, int>;

void show(const Ex& ex1, const Ex& ex2)
{
    for (int i{}; i < 2; ++i)
    {
        std::cout << (i ? "ex2" : "ex1");
        if (const Ex& ex = (i ? ex2 : ex1); ex.has_value())
            std::cout << ".has_value() = " << *ex << '\n';
        else
            std::cout << ".error() = " << ex.error() << '\n';
    }
}

int main()
{
    Ex ex1("\N{DOG FACE}");
    Ex ex2{"\N{BONE}"};
    show(ex1, ex2);
    swap(ex1, ex2);
    std::cout << "swap(ex1, ex2);\n";
    show(ex1, ex2);
    std::cout << '\n';

    ex2 = std::unexpected(13);
    show(ex1, ex2);
    swap(ex1, ex2);
    std::cout << "swap(ex1, ex2);\n";
    show(ex1, ex2);
    std::cout << '\n';

    ex2 = std::unexpected(19937);
    show(ex1, ex2);
    swap(ex1, ex2);
    std::cout << "swap(ex1, ex2);\n";
    show(ex1, ex2);
    std::cout << '\n';
}
```


**Output:**
```
ex1.has_value() = 🐶
ex2.has_value() = 🦴
swap(ex1, ex2);
ex1.has_value() = 🦴
ex2.has_value() = 🐶

ex1.has_value() = 🦴
ex2.error() = 13
swap(ex1, ex2);
ex1.error() = 13
ex2.has_value() = 🦴

ex1.error() = 13
ex2.error() = 19937
swap(ex1, ex2);
ex1.error() = 19937
ex2.error() = 13
```


## See also


| cpp/utility/expected/dsc swap | (see dedicated page) |

