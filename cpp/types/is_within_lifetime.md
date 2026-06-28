---
title: std::is_within_lifetime
type: Utilities
source: https://en.cppreference.com/w/cpp/types/is_within_lifetime
---

ddcl|header=type_traits|since=c++26|
template< class T >
consteval bool is_within_lifetime( const T* ptr ) noexcept;
Determines whether the pointer `ptr` points to an object that is within its .
During the evaluation of an expression `E` as a core constant expression, a call to `std::is_within_lifetime` is ill-formed unless `ptr` points to an object
* that is , or
* whose complete object’s lifetime began within `E`.

## Parameters


### Parameters

- `ptr` - pointer to detect

## Return value

`true` if pointer `ptr` points to an object that is within its lifetime; otherwise `false`.

## Notes


## Example


### Example

```cpp
#include <type_traits>

// an optional boolean type occupying only one byte,
// assuming sizeof(bool) == sizeof(char)
struct optional_bool
{
    union { bool b; char c; };

    // assuming the value representations for true and false
    // are distinct from the value representation for 2
    constexpr optional_bool() : c(2) {}
    constexpr optional_bool(bool b) : b(b) {}

    constexpr auto has_value() const -> bool
    {
        if consteval
        {
            return std::is_within_lifetime(&b); // during constant evaluation,
                                                // cannot read from c
        }
        else
        {
            return c != 2; // during runtime, must read from c
        }
    }

    constexpr auto operator*() -> bool&
    {
        return b;
    }
};

int main()
{
    constexpr optional_bool disengaged;
    constexpr optional_bool engaged(true);

    static_assert(!disengaged.has_value());
    static_assert(engaged.has_value());
    static_assert(*engaged);
}
```


## See also


| cpp/types/dsc is_implicit_lifetime | (see dedicated page) |

