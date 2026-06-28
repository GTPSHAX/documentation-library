---
title: std::for_each
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/for_each
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|constexpr=c++20|
template< class InputIt, class UnaryFunc >
UnaryFunc for_each( InputIt first, InputIt last, UnaryFunc f );
dcla|num=2|since=c++17|
template< class ExecutionPolicy, class ForwardIt, class UnaryFunc >
void for_each( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last, UnaryFunc f );
```

Applies the given invocable object `f` to each element in the target range [first, last). If `f` returns a result, the result is ignored.
1. `f` is applied in order starting from `first`.
rrev|since=c++11|
.
2. `f` might not be applied in order. The algorithm is executed according to `policy`.
@@ Unlike other , `for_each` is not allowed to make arbitrary copies of elements from the target range.
@@
@@ .

## Parameters


### Parameters

- `[range=target, simple=yes}})` - 
- `policy` - execution policy

**Type requirements:**

- `InputIt`
- `ForwardIt`

## Return value

1. `f`

## Complexity

Exactly `std::distance(first, last)` applications of `f`.

## Exceptions

2.

## Notes

If the iterator type (`InputIt`/`ForwardIt`) is mutable, `f` may modify the elements in the target range.
For overload , `f` can be a stateful invocable object. The return value can be considered as the final state of the batch operation.
For overload , multiple copies of `f` may be created to perform parallel invocation. No value is returned because parallelization often does not permit efficient state accumulation.

## Possible implementation

See also the implementations in [https://github.com/gcc-mirror/gcc/blob/d9375e490072d1aae73a93949aa158fcd2a27018/libstdc%2B%2B-v3/include/bits/stl_algo.h#L3858 libstdc++], [https://github.com/llvm-mirror/libcxx/blob/a12cb9d211019d99b5875b6d8034617cbc24c2cc/include/algorithm#L880 libc++] and [https://github.com/microsoft/STL/blob/ff83542af4b683fb2f2dea1423fd6c50fe3e13b0/stl/inc/algorithm#L229 MSVC stdlib].
eq fun|1=
template<class InputIt, class UnaryFunc>
constexpr UnaryFunc for_each(InputIt first, InputIt last, UnaryFunc f)
{
for (; first != last; ++first)
f(*first);
return f; // implicit move since C++11
}

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> v{3, -4, 2, -8, 15, 267};

    auto print = [](const int& n) { std::cout << n << ' '; };

    std::cout << "before:\t";
    std::for_each(v.cbegin(), v.cend(), print);
    std::cout << '\n';

    // increment elements in-place
    std::for_each(v.begin(), v.end(), [](int &n) { n++; });

    std::cout << "after:\t";
    std::for_each(v.cbegin(), v.cend(), print);
    std::cout << '\n';

    struct Sum
    {
        void operator()(int n) { sum += n; }
        int sum {0};
    };

    // invoke Sum::operator() for each element
    Sum s = std::for_each(v.cbegin(), v.cend(), Sum());    
    std::cout << "sum:\t" << s.sum << '\n';
}
```


**Output:**
```
before:	3 -4 2 -8 15 267 
after:	4 -3 3 -7 16 268 
sum:	281
```


## Defect reports


## See also


| cpp/algorithm/ranges/dsc for_each | (see dedicated page) |
| cpp/algorithm/dsc for_each_n | (see dedicated page) |
| cpp/algorithm/dsc transform | (see dedicated page) |
| cpp/language/dsc range-for | (see dedicated page) |

