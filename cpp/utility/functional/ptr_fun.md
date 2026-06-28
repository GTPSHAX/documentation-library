---
title: std::ptr_fun
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/ptr_fun
---


```cpp
**Header:** `<`functional`>`
dcl|deprecated=c++11|until=c++17|num=1|
template< class Arg, class Result >
std::pointer_to_unary_function<Arg,Result>
ptr_fun( Result (*f)(Arg) );
dcl|deprecated=c++11|until=c++17|num=2|
template< class Arg1, class Arg2, class Result >
std::pointer_to_binary_function<Arg1,Arg2,Result>
ptr_fun( Result (*f)(Arg1, Arg2) );
```

Creates a function wrapper object (either `std::pointer_to_unary_function` or `std::pointer_to_binary_function`), deducing the target type from the template arguments.
1. Effectively calls `std::pointer_to_unary_function<Arg,Result>(f)`.
2. Effectively calls `std::pointer_to_binary_function<Arg1,Arg2,Result>(f)`.
This function and the related types are deprecated as of C++11 in favor of the more general `std::function` and `std::ref`, both of which create callable adaptor-compatible function objects from plain functions.

## Parameters


### Parameters

- `f` - pointer to a function to create a wrapper for

## Return value

A function object wrapping `f`.

## Example


### Example

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <string_view>

constexpr bool is_vowel(char c)
{
    return std::string_view{"aeoiuAEIOU"}.find(c) != std::string_view::npos;
}

int main()
{
    std::string_view s = "Hello, world!";
    std::ranges::copy_if(s, std::ostreambuf_iterator<char>(std::cout),
        std::not1(std::ptr_fun(is_vowel)));
#if 0
// C++11 alternatives:
        std::not1(std::cref(is_vowel)));
        std::not1(std::function<bool(char)>(is_vowel)));
        [](char c) { return !is_vowel(c); });
// C++17 alternatives:
        std::not_fn(is_vowel));
#endif
}
```


**Output:**
```
Hll, wrld!
```


## See also


| cpp/utility/functional/dsc function | (see dedicated page) |
| cpp/utility/functional/dsc move_only_function | (see dedicated page) |
| cpp/utility/functional/dsc invoke | (see dedicated page) |
| cpp/utility/functional/dsc not_fn | (see dedicated page) |

