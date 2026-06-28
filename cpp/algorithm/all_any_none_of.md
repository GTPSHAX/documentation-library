---
title: std::all_of
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/all_any_none_of
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|since=c++11|constexpr=c++20|
template< class InputIt, class UnaryPred >
bool all_of( InputIt first, InputIt last, UnaryPred p );
dcla|num=2|since=c++11|constexpr=c++20|
template< class InputIt, class UnaryPred >
bool any_of( InputIt first, InputIt last, UnaryPred p );
dcla|num=3|since=c++11|constexpr=c++20|
template< class InputIt, class UnaryPred >
bool none_of( InputIt first, InputIt last, UnaryPred p );
dcla|num=4|since=c++17|
template< class ExecutionPolicy, class ForwardIt, class UnaryPred >
bool all_of( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last, UnaryPred p );
dcl|num=5|since=c++17|
template< class ExecutionPolicy, class ForwardIt, class UnaryPred >
bool any_of( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last, UnaryPred p );
dcl|num=6|since=c++17|
template< class ExecutionPolicy, class ForwardIt, class UnaryPred >
bool none_of( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last, UnaryPred p );
```

1. Checks if unary predicate `p` returns `true` for all elements in the range [first, last).
2. Checks if unary predicate `p` returns `true` for at least one element in the range [first, last).
3. Checks if unary predicate `p` returns `true` for none of the elements in the range [first, last).
@4-6@ Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `policy` - execution policy

**Type requirements:**

- `InputIt`
- `ForwardIt`
- `UnaryPred`

## Return value


## Complexity

@1-6@ At most `std::distance(first, last)` applications of `p`.

## Exceptions

@4-6@

## Notes


## Possible implementation

See also the implementations of
* `all_of` in [https://github.com/gcc-mirror/gcc/blob/d9375e490072d1aae73a93949aa158fcd2a27018/libstdc%2B%2B-v3/include/bits/stl_algo.h#L508 libstdc++] and [https://github.com/llvm-mirror/libcxx/blob/a12cb9d211019d99b5875b6d8034617cbc24c2cc/include/algorithm#L838 libc++].
* `any_of` in [https://github.com/gcc-mirror/gcc/blob/d9375e490072d1aae73a93949aa158fcd2a27018/libstdc%2B%2B-v3/include/bits/stl_algo.h#L541 libstdc++] and [https://github.com/llvm-mirror/libcxx/blob/a12cb9d211019d99b5875b6d8034617cbc24c2cc/include/algorithm#L852 libc++].
* `none_of` in [https://github.com/gcc-mirror/gcc/blob/d9375e490072d1aae73a93949aa158fcd2a27018/libstdc%2B%2B-v3/include/bits/stl_algo.h#L523 libstdc++] and [https://github.com/llvm-mirror/libcxx/blob/a12cb9d211019d99b5875b6d8034617cbc24c2cc/include/algorithm#L866 libc++].
eq impl
|title1=all_of|ver1=1|1=
template<class InputIt, class UnaryPred>
constexpr bool all_of(InputIt first, InputIt last, UnaryPred p)
{
return std::find_if_not(first, last, p) == last;
}
|title2=any_of|ver2=2|2=
template<class InputIt, class UnaryPred>
constexpr bool any_of(InputIt first, InputIt last, UnaryPred p)
{
return std::find_if(first, last, p) != last;
}
|title3=none_of|ver3=3|3=
template<class InputIt, class UnaryPred>
constexpr bool none_of(InputIt first, InputIt last, UnaryPred p)
{
return std::find_if(first, last, p) == last;
}

## Example


### Example

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <iterator>
#include <numeric>
#include <vector>

int main()
{
    std::vector<int> v(10, 2);
    std::partial_sum(v.cbegin(), v.cend(), v.begin());
    std::cout << "Among the numbers: ";
    std::copy(v.cbegin(), v.cend(), std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';

    if (std::all_of(v.cbegin(), v.cend(), [](int i) { return i % 2 == 0; }))
        std::cout << "All numbers are even\n";

    using namespace std::placeholders;
    if (std::none_of(v.cbegin(), v.cend(), std::bind(std::modulus<>(), _1, 2)))
        std::cout << "None of them are odd\n";

    struct DivisibleBy
    {
        const int d;
        DivisibleBy(int n) : d(n) {}
        bool operator()(int n) const { return n % d == 0; }
    };

    if (std::any_of(v.cbegin(), v.cend(), DivisibleBy(7)))
        std::cout << "At least one number is divisible by 7\n";
}
```


**Output:**
```
Among the numbers: 2 4 6 8 10 12 14 16 18 20
All numbers are even
None of them are odd
At least one number is divisible by 7
```


## See also


| cpp/algorithm/ranges/dsc all_any_none_of | (see dedicated page) |

