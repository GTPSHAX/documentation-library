---
title: std::unary_negate
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/unary_negate
---


```cpp
**Header:** `<`functional`>`
dcl rev multi|until1=c++11|dcl1=
template< class Predicate >
struct unary_negate : public std::unary_function<Predicate::argument_type, bool>;
|notes2=|dcl2=
template< class Predicate >
struct unary_negate;
```

`std::unary_negate` is a wrapper function object returning the complement of the unary predicate it holds.
The unary predicate type must define a member type, `argument_type`, that is convertible to the predicate's parameter type. The unary function objects obtained from `std::ref`, `std::cref`, `std::negate`, `std::logical_not`, `std::mem_fn`, `std::function`, `std::hash`, or from another call to `std::not1` have this type defined, as are function objects derived from the deprecated `std::unary_function`.
`std::unary_negate` objects are easily constructed with helper function `std::not1`.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions

member|unary_negate|2=

```cpp
dcla|constexpr=c++14|1=
explicit unary_negate( Predicate const& pred );
```

Constructs a `std::unary_negate` function object with the stored predicate `pred`.

## Parameters


### Parameters

- `pred` - predicate function object
member|operator()|2=

```cpp
dcla|constexpr=c++14|1=
bool operator()( argument_type const& x ) const;
```

Returns the logical complement of the result of calling  `pred(x)`.

## Parameters


### Parameters

- `x` - argument to pass through to predicate

## Return value

The logical complement of the result of calling `pred(x)`.

## Example


### Example

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <vector>

struct less_than_7 : std::unary_function<int, bool>
{
    bool operator()(int i) const { return i < 7; }
};

int main()
{
    std::vector<int> v(7, 7);
    v[0] = v[1] = v[2] = 6;

    std::unary_negate<less_than_7> not_less_than_7((less_than_7()));
    // C++11 solution:
    // Use std::function<bool (int)>
    // std::function<bool (int)> not_less_than_7 =
    //     [](int x)->bool { return !less_than_7()(x); };

    std::cout << std::count_if(v.begin(), v.end(), not_less_than_7);
}
```


**Output:**
```
4
```


## See also


| cpp/utility/functional/dsc binary_negate | (see dedicated page) |
| cpp/utility/functional/dsc function | (see dedicated page) |
| cpp/utility/functional/dsc move_only_function | (see dedicated page) |
| cpp/utility/functional/dsc not1 | (see dedicated page) |
| cpp/utility/functional/dsc ptr_fun | (see dedicated page) |
| cpp/utility/functional/dsc unary_function | (see dedicated page) |

