---
title: std::expected::~expected
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/expected/~expected
---

ddcl|since=c++23|
constexpr ~expected();

## Main template destructor

Destroys the contained value:
* If `has_value()` is `true`, destroys the expected value.
* Otherwise, destroys the unexpected value.
This destructor is trivial if `std::is_trivially_destructible_v<T>` and `std::is_trivially_destructible_v<E>` are both `true`.

## `void` partial specialization destructor

If `has_value()` is `false`, destroys the unexpected value.
This destructor is trivial if `std::is_trivially_destructible_v<E>` is `true`.

## Example


### Example

```cpp
#include <expected>
#include <iostream>
#include <source_location>

inline
void name(int x, std::source_location sloc = std::source_location::current())
{
    std::cout << sloc.function_name() << " : " << x << '\n';
}

struct Value
{
    int m{};
    ~Value() { name(m); }
};

struct Error
{
    int e{};
    ~Error() { name(e); }
};

int main()
{
    std::expected<Value, Error> e1 {42};
    std::expected<Value, Error> e2 {std::unexpect, 13};
    std::expected<void, Error>  e3 {std::unexpect, 37};
}
```


**Output:**
```
Error::~Error : 37
Error::~Error : 13
Value::~Value : 42
```

