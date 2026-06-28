---
title: std::not1
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/not1
---


```cpp
**Header:** `<`functional`>`
dcl rev multi|until1=c++14|dcl1=
template< class Predicate >
std::unary_negate<Predicate> not1( const Predicate& pred );
|notes2=|dcl2=
template< class Predicate >
constexpr std::unary_negate<Predicate> not1( const Predicate& pred );
```

`std::not1` is a helper function to create a function object that returns the complement of the unary predicate function passed. The function object created is of type `std::unary_negate<Predicate>`.
The unary predicate type must define a member type, `argument_type`, that is convertible to the predicate's parameter type. The unary function objects obtained from `std::ref`, `std::cref`, `std::negate`, `std::logical_not`, `std::mem_fn`, `std::function`, `std::hash`, or from another call to `std::not1` have this type defined, as are function objects derived from the deprecated `std::unary_function`.

## Parameters


### Parameters

- `pred` - unary predicate

## Return value

`std::not1` returns an object of type `std::unary_negate<Predicate>`, constructed with `pred`.

## Example


### Example

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <iterator>
#include <numeric>
#include <vector>

struct LessThan7 : std::unary_function<int, bool>
{
    bool operator()(int i) const { return i < 7; }
};

int main()
{
    std::vector<int> v(10);
    std::iota(std::begin(v), std::end(v), 0);

    std::cout << std::count_if(begin(v), end(v), std::not1(LessThan7())) << '\n';

    // the same as above using std::function
    std::function<bool(int)> less_than_9 = [](int x) { return x < 9; };
    std::cout << std::count_if(begin(v), end(v), std::not1(less_than_9)) << '\n';
}
```


**Output:**
```
3
1
```


## See also


| cpp/utility/functional/dsc not_fn | (see dedicated page) |
| cpp/utility/functional/dsc unary_negate | (see dedicated page) |
| cpp/utility/functional/dsc function | (see dedicated page) |
| cpp/utility/functional/dsc move_only_function | (see dedicated page) |
| cpp/utility/functional/dsc not2 | (see dedicated page) |
| cpp/utility/functional/dsc ptr_fun | (see dedicated page) |
| cpp/utility/functional/dsc unary_function | (see dedicated page) |

