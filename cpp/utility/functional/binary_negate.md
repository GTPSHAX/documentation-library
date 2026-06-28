---
title: std::binary_negate
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/binary_negate
---


```cpp
**Header:** `<`functional`>`
dcl rev multi|until1=c++11|dcl1=
template< class Predicate >
struct binary_negate
: public std::binary_function<
Predicate::first_argument_type,
Predicate::second_argument_type,
bool
>;
|notes2=|dcl2=
template< class Predicate >
struct binary_negate;
```

`std::binary_negate` is a wrapper function object returning the complement of the binary predicate it holds.
The binary predicate type must define two member types, `first_argument_type` and `second_argument_type`, that are convertible to the predicate's parameter types. The function objects obtained from `std::owner_less`, `std::ref`, `std::cref`, `std::plus`, `std::minus`, `std::multiplies`, `std::divides`, `std::modulus`, `std::equal_to`, `std::not_equal_to`, `std::greater`, `std::less`, `std::greater_equal`, `std::less_equal`, `std::logical_not`, `std::logical_or`, `std::bit_and`, `std::bit_or`, `std::bit_xor`, `std::mem_fn`, `std::map::value_comp`, `std::multimap::value_comp`, `std::function`, or from a call to `std::not2` have these types defined, as are function objects derived from the deprecated `std::binary_function`.
`std::binary_negate` objects are easily constructed with helper function `std::not2`.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions

member|binary_negate|2=

```cpp
dcla|constexpr=c++14|1=
explicit binary_negate( Predicate const& pred );
```

Constructs a `std::binary_negate` function object with the stored predicate `pred`.

## Parameters


### Parameters

- `pred` - predicate function object
member|operator()|2=

```cpp
dcla|constexpr=c++14|1=
bool operator()( first_argument_type const& x,
second_argument_type const& y ) const;
```

Returns the logical complement of the result of calling `pred(x, y)`.

## Parameters


### Parameters

- `x` - first argument to pass through to predicate
- `y` - second argument to pass through to predicate

## Return value

The logical complement of the result of calling `pred(x, y)`.

## Example


### Example

```cpp
#include <algorithm>
#include <cstddef>
#include <functional>
#include <iostream>
#include <vector>

struct same : std::binary_function<int, int, bool>
{
    bool operator()(int a, int b) const { return a == b; }
};

int main()
{
    std::vector<int> v1;
    for (int i = 0; i < 7; ++i)
        v1.push_back(i);

    std::vector<int> v2(v1.size());
    std::reverse_copy(v1.begin(), v1.end(), v2.begin());

    std::vector<bool> v3(v1.size());

    std::binary_negate<same> not_same((same()));

    // C++11 solution:
    // std::function<bool (int, int)> not_same =
    //     [](int x, int y) -> bool { return !same()(x, y); };

    std::transform(v1.begin(), v1.end(), v2.begin(), v3.begin(), not_same);

    std::cout.setf(std::ios_base::boolalpha);
    for (std::size_t i = 0; i != v1.size(); ++i)
        std::cout << v1[i] << " != " << v2[i] << " : " << v3[i] << '\n';
}
```


**Output:**
```
0 != 6 : true
1 != 5 : true
2 != 4 : true
3 != 3 : false
4 != 2 : true
5 != 1 : true
6 != 0 : true
```


## See also


| cpp/utility/functional/dsc binary_function | (see dedicated page) |
| cpp/utility/functional/dsc function | (see dedicated page) |
| cpp/utility/functional/dsc move_only_function | (see dedicated page) |
| cpp/utility/functional/dsc not2 | (see dedicated page) |
| cpp/utility/functional/dsc ptr_fun | (see dedicated page) |
| cpp/utility/functional/dsc unary_negate | (see dedicated page) |

