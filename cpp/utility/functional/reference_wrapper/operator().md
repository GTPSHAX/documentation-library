---
title: std::reference_wrapper::operator()
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/reference_wrapper/operator()
---


```cpp
dcl rev multi
|since1=c++11|dcl1=
template< class... ArgTypes >
typename std::result_of<T&(ArgTypes&&...)>::type
operator() ( ArgTypes&&... args ) const;
|since2=c++17|notes2=<sup>(constexpr C++20)</sup>|dcl2=
template< class... ArgTypes >
std::invoke_result_t<T&, ArgTypes...>
operator() ( ArgTypes&&... args ) const noexcept(/* see below */);
```

Calls the *Callable* object, reference to which is stored, as if by . This function is available only if the stored reference points to a *Callable* object.
`T` must be a complete type.

## Parameters


### Parameters

- `args` - arguments to pass to the called function

## Return value

The return value of the called function.

## Exceptions

rrev multi|since1=c++11|until1=c++17
|rev1=May throw implementation-defined exceptions.
|rev2=

## Example


### Example

```cpp
#include <functional>
#include <iostream>

void f1()
{
    std::cout << "reference to function called\n";
}

void f2(int n)
{
    std::cout << "bind expression called with " << n << " as the argument\n";
}

int main()
{
    std::reference_wrapper<void()> ref1 = std::ref(f1);
    ref1();

    auto b = std::bind(f2, std::placeholders::_1);
    auto ref2 = std::ref(b);
    ref2(7);

    auto c = []{ std::cout << "lambda function called\n"; };
    auto ref3 = std::ref(c);
    ref3();
}
```


**Output:**
```
reference to function called
bind expression called with 7 as the argument
lambda function called
```


## Defect reports


## See also


| cpp/utility/functional/reference_wrapper/dsc get | (see dedicated page) |

