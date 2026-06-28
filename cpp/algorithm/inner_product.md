---
title: std::inner_product
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/inner_product
---


```cpp
**Header:** `<`numeric`>`
dcla|num=1|constexpr=c++20|
template< class InputIt1, class InputIt2, class T >
T inner_product( InputIt1 first1, InputIt1 last1,
InputIt2 first2, T init );
dcla|num=2|constexpr=c++20|
template< class InputIt1, class InputIt2, class T,
class BinaryOp1, class BinaryOp2 >
T inner_product( InputIt1 first1, InputIt1 last1,
InputIt2 first2, T init,
BinaryOp1 op1, BinaryOp2 op2 );
```

Computes inner product (i.e. sum of products) or performs ordered map/reduce operation on the range [first1, last1) and the range of `std::distance(first1, last1)` elements beginning at `first2`.
1. Initializes the accumulator `acc` (of type `T`) with the initial value `init` and then  modifies it with the expression <sup>(until C++20)</sup> `1=acc = acc + (*i1) * (*i2)`<sup>(since C++20)</sup> `1=acc = std::move(acc) + (*i1) * (*i2)` for every iterator `i1` in the range [first1, last1) in order and its corresponding iterator `i2` in the range beginning at `first2`. For built-in meaning of + and *, this computes inner product of the two ranges.
2. Initializes the accumulator `acc` (of type `T`) with the initial value `init` and then  modifies it with the expression <sup>(until C++20)</sup> `1=acc = op1(acc, op2(*i1, *i2))`<sup>(since C++20)</sup> `1=acc = op1(std::move(acc), op2(*i1, *i2))` for every iterator `i1` in the range [first1, last1) in order and its corresponding iterator `i2` in the range beginning at `first2`.
Given `last2` as the `std::distance(first1, last1)` next iterator of `first2`, if any of the following conditions is satisfied, the behavior is undefined:
* `T` is not *CopyConstructible*.
* `T` is not *CopyAssignable*.
* `op1` or `op2` modifies any element of [first1, last1) or [first2, last2).
* `op1` or `op2` invalidates any iterator or subrange in  or .

## Parameters


### Parameters

- `[first1, last1}})` - 
- `first2` - the beginning of the second range of elements
- `init` - initial value of the sum of the products

**Type requirements:**

- `InputIt1, InputIt2`

## Return value

`acc` after all modifications.

## Possible implementation

eq impl
|title1=inner_product (1)|ver1=1|1=
template<class InputIt1, class InputIt2, class T>
constexpr // since C++20
T inner_product(InputIt1 first1, InputIt1 last1, InputIt2 first2, T init)
{
while (first1 != last1)
{
init = std::move(init) + (*first1) * (*first2); // std::move since C++20
++first1;
++first2;
}
return init;
}
|title2=inner_product (2)|ver2=2|2=
template<class InputIt1, class InputIt2, class T,
class BinaryOp1, class BinaryOp2>
constexpr // since C++20
T inner_product(InputIt1 first1, InputIt1 last1, InputIt2 first2, T init,
BinaryOp1 op1, BinaryOp2 op2)
{
while (first1 != last1)
{
init = op1(std::move(init), op2(*first1, *first2)); // std::move since C++20
++first1;
++first2;
}
return init;
}

## Notes

The parallelizable version of this algorithm, `std::transform_reduce`, requires `op1` and `op2` to be commutative and associative, but `std::inner_product` makes no such requirement, and always performs the operations in the order given.

## Example


### Example

```cpp
#include <functional>
#include <iostream>
#include <numeric>
#include <vector>

int main()
{
    std::vector<int> a{0, 1, 2, 3, 4};
    std::vector<int> b{5, 4, 2, 3, 1};

    int r1 = std::inner_product(a.begin(), a.end(), b.begin(), 0);
    std::cout << "Inner product of a and b: " << r1 << '\n';

    int r2 = std::inner_product(a.begin(), a.end(), b.begin(), 0,
                                std::plus<>(), std::equal_to<>());
    std::cout << "Number of pairwise matches between a and b: " <<  r2 << '\n';
}
```


**Output:**
```
Inner product of a and b: 21
Number of pairwise matches between a and b: 2
```


## Defect reports


## See also


| cpp/algorithm/dsc transform_reduce | (see dedicated page) |
| cpp/algorithm/dsc accumulate | (see dedicated page) |
| cpp/algorithm/dsc partial_sum | (see dedicated page) |

