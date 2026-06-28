---
title: std::accumulate
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/accumulate
---


```cpp
**Header:** `<`numeric`>`
dcla|num=1|constexpr=c++20|
template< class InputIt, class T >
T accumulate( InputIt first, InputIt last, T init );
dcla|num=2|constexpr=c++20|
template< class InputIt, class T, class BinaryOp >
T accumulate( InputIt first, InputIt last, T init, BinaryOp op );
```

Computes the sum of the given value `init` and the elements in the range [first, last).
1. Initializes the accumulator `acc` (of type `T`) with the initial value `init` and then modifies it with <sup>(until C++20)</sup> `1=acc = acc + *i`<sup>(since C++20)</sup> `1=acc = std::move(acc) + *i` for every iterator `i` in the range [first, last) in order.
2. Initializes the accumulator `acc` (of type `T`) with the initial value `init` and then modifies it with <sup>(until C++20)</sup> `1=acc = op(acc, *i)`<sup>(since C++20)</sup> `1=acc = op(std::move(acc), *i)` for every iterator `i` in the range [first, last) in order.
If any of the following conditions is satisfied, the behavior is undefined:
* `T` is not *CopyConstructible*.
* `T` is not *CopyAssignable*.
* `op` modifies any element of [first, last).
* `op` invalidates any iterator or subrange in .

## Parameters


### Parameters

- `init` - initial value of the accumulate

**Type requirements:**

- `InputIt`

## Return value

`acc` after all modifications.

## Possible implementation

eq impl
|title1=accumulate (1)|ver1=1|1=
template<class InputIt, class T>
constexpr // since C++20
T accumulate(InputIt first, InputIt last, T init)
{
for (; first != last; ++first)
init = std::move(init) + *first; // std::move since C++20
return init;
}
|title2=accumulate (2)|ver2=2|2=
template<class InputIt, class T, class BinaryOperation>
constexpr // since C++20
T accumulate(InputIt first, InputIt last, T init, BinaryOperation op)
{
for (; first != last; ++first)
init = op(std::move(init), *first); // std::move since C++20
return init;
}

## Notes

`std::accumulate` performs a left fold. In order to perform a right fold, one must reverse the order of the arguments to the binary operator, and use reverse iterators.
If left to type inference, `op` operates on values of the same type as `init` which can result in unwanted casting of the iterator elements. For example, `std::accumulate(v.begin(), v.end(), 0)` likely does not give the result one wishes for when `v` is of type `std::vector<double>`.

## Example


### Example

```cpp
#include <functional>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

int main()
{
    std::vector<int> v{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    int sum = std::accumulate(v.begin(), v.end(), 0);
    int product = std::accumulate(v.begin(), v.end(), 1, std::multiplies<int>());

    auto dash_fold = [](std::string a, int b)
    {
        return std::move(a) + '-' + std::to_string(b);
    };

    std::string s = std::accumulate(std::next(v.begin()), v.end(),
                                    std::to_string(v[0]), // start with first element
                                    dash_fold);

    // Right fold using reverse iterators
    std::string rs = std::accumulate(std::next(v.rbegin()), v.rend(),
                                     std::to_string(v.back()), // start with last element
                                     dash_fold);

    std::cout << "sum: " << sum << '\n'
              << "product: " << product << '\n'
              << "dash-separated string: " << s << '\n'
              << "dash-separated string (right-folded): " << rs << '\n';
}
```


**Output:**
```
sum: 55
product: 3628800
dash-separated string: 1-2-3-4-5-6-7-8-9-10
dash-separated string (right-folded): 10-9-8-7-6-5-4-3-2-1
```


## Defect reports


## See also


| cpp/algorithm/dsc adjacent_difference | (see dedicated page) |
| cpp/algorithm/dsc inner_product | (see dedicated page) |
| cpp/algorithm/dsc partial_sum | (see dedicated page) |
| cpp/algorithm/dsc reduce | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left | (see dedicated page) |

