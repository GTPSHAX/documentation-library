---
title: std::less
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/less
---


```cpp
**Header:** `<`functional`>`
dcl rev multi
|dcl1=
template< class T >
struct less;
|since2=c++14|dcl2=
template< class T = void >
struct less;
```

Function object for performing comparisons. The main template invokes `operator<` on type `T`.

## Specializations


| cpp/utility/functional/dsc less_void | (see dedicated page) |


## Member functions

member|operator()|2=

```cpp
dcla|constexpr=c++14|1=
bool operator()( const T& lhs, const T& rhs ) const;
```

Checks whether `lhs` is ''less'' than `rhs`.

## Parameters


### Parameters

- `lhs, rhs` - values to compare

## Return value

`lhs < rhs`.
If `T` is a pointer type, the result is consistent with the implementation-defined strict total order over pointers.

## Possible implementation

eq fun|1=
constexpr bool operator()(const T& lhs, const T& rhs) const
{
return lhs < rhs; // assumes that the implementation handles pointer total order
}

## Example


### Example

```cpp
#include <functional>

template<typename A, typename B, typename C = std::less<>>
constexpr bool fun(A a, B b, C cmp = C{})
{
    return cmp(a, b);
}

static_assert(fun(1, 2) == true);
static_assert(fun(1.0, 1) == false);
static_assert(fun(1, 2.0) == true);
static_assert(std::less<int>{}(5, 5.6) == false);   // 5 < 5 (warn: implicit conversion)
static_assert(std::less<double>{}(5, 5.6) == true); // 5.0 < 5.6
static_assert(std::less<int>{}(5.6, 5.7) == false); // 5 < 5 (warn: implicit conversion)
static_assert(std::less{}(5, 5.6) == true);         // less<void>: 5.0 < 5.6

int main() {}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2562 | C++98 | the pointer total order might be inconsistent | guaranteed to be consistent |


## See also


| cpp/utility/functional/dsc equal_to | (see dedicated page) |
| cpp/utility/functional/dsc greater | (see dedicated page) |
| cpp/utility/functional/ranges/dsc {{SUBPAGENAMEE | (see dedicated page) |

