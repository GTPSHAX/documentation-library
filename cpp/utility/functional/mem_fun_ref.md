---
title: std::mem_fun_ref
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/mem_fun_ref
---


```cpp
**Header:** `<`functional`>`
dcl|deprecated=c++11|until=c++17|num=1|
template< class Res, class T >
std::mem_fun_ref_t<Res,T> mem_fun_ref( Res (T::*f)() );
dcl|deprecated=c++11|until=c++17|num=1|
template< class Res, class T >
std::const_mem_fun_ref_t<Res,T> mem_fun_ref( Res (T::*f)() const );
dcl|deprecated=c++11|until=c++17|num=2|
template< class Res, class T, class Arg >
std::mem_fun1_ref_t<Res,T,Arg> mem_fun_ref( Res (T::*f)(Arg) );
dcl|deprecated=c++11|until=c++17|num=2|
template< class Res, class T, class Arg >
std::const_mem_fun1_ref_t<Res,T,Arg> mem_fun_ref( Res (T::*f)(Arg) const );
```

Creates a member function wrapper object, deducing the target type from the template arguments. The wrapper object expects a reference to an object of type `T` as the first parameter to its `operator()`.
1. Effectively calls `std::mem_fun_ref_t<S,T>(f)` or `std::const_mem_fun_ref_t<S,T>(f)`.
2. Effectively calls `std::mem_fun1_ref_t<S,T>(f)` or `std::const_mem_fun1_ref_t<S,T>(f)`.
This function and the related types were deprecated in C++11 and removed in C++17 in favor of the more general `std::mem_fn` and `std::bind`, both of which create callable adaptor-compatible function objects from member functions.

## Parameters


### Parameters

- `f` - pointer to a member function to create a wrapper for

## Return value

A function object wrapping `f`.

## Notes

The difference between `std::mem_fun` and `std::mem_fun_ref` is that the former produces a function wrapper that expects a pointer to an object, whereas the latter &mdash; a reference.

## Example


### Example

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>

int main()
{
    std::vector<std::string> v = {"once", "upon", "a", "time"};
    std::transform(v.cbegin(), v.cend(),
                   std::ostream_iterator<std::size_t>(std::cout, " "),
                   std::mem_fun_ref(&std::string::size));
}
```


**Output:**
```
4 4 1 4
```


## See also


| cpp/utility/functional/dsc mem_fun | (see dedicated page) |

