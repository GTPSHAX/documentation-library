---
title: std::declval
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/declval
---


```cpp
**Header:** `<`utility`>`
dcl rev multi
|since1=c++11|notes1=|dcl1=
template< class T >
typename std::add_rvalue_reference<T>::type declval() noexcept;
|since2=c++14|notes2=|dcl2=
template< class T >
std::add_rvalue_reference_t<T> declval() noexcept;
```

Helper template for writing expressions that appear in unevaluated contexts, typically the operand of `decltype`. In unevaluated context, this helper template converts any type `T` (which may be an incomplete type) to an expression of that type, making it possible to use member functions of T without the need to go through constructors.
`std::declval` can only be used in unevaluated contexts and is not required to be defined; it is an error to evaluate an expression that contains this function. Formally, the program is ill-formed if this function is odr-used.

## Parameters

(none)

## Return value

Cannot be evaluated and thus never returns a value. The return type is `T&&` (reference collapsing rules apply) unless `T` is (possibly cv-qualified) `void`, in which case the return type is `T`.

## Notes

`std::declval` is commonly used in templates where acceptable template parameters may have no constructor in common, but have the same member function whose return type is needed.

## Possible implementation

eq fun
|1=
template<typename T>
typename std::add_rvalue_reference<T>::type declval() noexcept
{
static_assert(false, "declval not allowed in an evaluated context");
}

## Example


### Example

```cpp
#include <iostream>
#include <utility>

struct Default
{
    int foo() const { return 1; }
};

struct NonDefault
{
    NonDefault() = delete;
    int foo() const { return 1; }
};

int main()
{
    decltype(Default().foo())               n1 = 1;     // type of n1 is int
    decltype(std::declval<Default>().foo()) n2 = 1;     // same

//  decltype(NonDefault().foo())               n3 = n1; // error: no default constructor
    decltype(std::declval<NonDefault>().foo()) n3 = n1; // type of n3 is int

    std::cout << "n1 = " << n1 << '\n'
              << "n2 = " << n2 << '\n'
              << "n3 = " << n3 << '\n';
}
```


**Output:**
```
n1 = 1
n2 = 1
n3 = 1
```


## See also


| cpp/language/dsc decltype | (see dedicated page) |
| cpp/types/dsc result_of | (see dedicated page) |

