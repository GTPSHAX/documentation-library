---
title: std::variant::~variant
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/variant/~variant
---


```cpp
dcla|anchor=no|since=c++17|constexpr=c++20|
~variant();
```

If  is `true`, does nothing. Otherwise, destroys the currently contained object.
This destructor is trivial if `std::is_trivially_destructible_v<T_i>` is `true` for all `T_i` in `Types...`.

## Notes


## Example


### Example

```cpp
#include <cstdio>
#include <variant>

int main()
{
    struct X { ~X() { puts("X::~X();"); } };
    struct Y { ~Y() { puts("Y::~Y();"); } };

    {
        puts("entering block #1");
        std::variant<X,Y> var;
        puts("leaving block #1");
    }

    {
        puts("entering block #2");
        std::variant<X,Y> var{ std::in_place_index_t<1>{} }; // constructs var(Y)
        puts("leaving block #2");
    }
}
```


**Output:**
```
entering block #1
leaving block #1
X::~X();
entering block #2
leaving block #2
Y::~Y();
```


## Defect reports

