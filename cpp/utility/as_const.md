---
title: std::as_const
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/as_const
---


```cpp
**Header:** `<`utility`>`
dcl|since=c++17|num=1|1=
template< class T >
constexpr std::add_const_t<T>& as_const( T& t ) noexcept;
dcl|since=c++17|num=2|1=
template< class T >
void as_const( const T&& ) = delete;
```

1. Forms lvalue reference to const type of `t`.
2. const rvalue reference overload is deleted to disallow rvalue arguments.

## Possible implementation

eq fun
|1=
template<class T>
constexpr std::add_const_t<T>& as_const(T& t) noexcept
{
return t;
}

## Notes


## Example


### Example

```cpp
#include <cassert>
#include <string>
#include <type_traits>
#include <utility>

int main()
{
    std::string mutableString = "Hello World!";
    auto&& constRef = std::as_const(mutableString);

    mutableString.clear(); // OK
//  constRef.clear(); // Error: 'constRef' is 'const' qualified,
                      //        but 'clear' is not marked const

    assert(&constRef == &mutableString);
    assert(&std::as_const(mutableString) == &mutableString);

    using ExprType = std::remove_reference_t<decltype(std::as_const(mutableString))>;

    static_assert(std::is_same_v<std::remove_const_t<ExprType>, std::string>,
                  "ExprType should be some kind of string.");
    static_assert(!std::is_same_v<ExprType, std::string>,
                  "ExprType shouldn't be a mutable string.");
}
```


## See also


| cpp/types/dsc is_const | (see dedicated page) |
| cpp/types/dsc add_cv | (see dedicated page) |
| cpp/types/dsc remove_cv | (see dedicated page) |
| cpp/ranges/dsc as_const_view | (see dedicated page) |

