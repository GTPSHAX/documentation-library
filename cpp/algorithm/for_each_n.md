---
title: std::for_each_n
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/for_each_n
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|constexpr=c++20|
template< class InputIt, class Size, class UnaryFunc >
InputIt for_each_n( InputIt first, Size count, UnaryFunc f );
dcl|num=2|since=c++17|
template< class ExecutionPolicy,
class ForwardIt, class Size, class UnaryFunc >
ForwardIt for_each_n( ExecutionPolicy&& policy,
ForwardIt first, Size count, UnaryFunc f );
```

Applies the given invocable object `f` to each element in the target range [first, std::next(first, count)). If `f` returns a result, the result is ignored.
1. `f` is applied in order starting from `first`.
@@ .
2. `f` might not be applied in order. The algorithm is executed according to `policy`.
@@ Unlike other , `for_each_n` is not allowed to make arbitrary copies of elements from the target range.
@@
@@ .
.

## Parameters


### Parameters

- `first` - the beginning of the target range
- `count` - the number of elements in the target range
- `policy` - execution policy

**Type requirements:**

- `InputIt`
- `ForwardIt`

## Return value

`std::next(first, count)`

## Complexity

Exactly `count` applications of `f`.

## Exceptions

2.

## Notes

If the iterator type (`InputIt`/`ForwardIt`) is mutable, `f` may modify the elements in the target range.

## Possible implementation

See also the implementation in [https://github.com/gcc-mirror/gcc/blob/d9375e490072d1aae73a93949aa158fcd2a27018/libstdc%2B%2B-v3/include/pstl/algorithm_impl.h#L82 libstdc++], [https://github.com/llvm-mirror/libcxx/blob/a12cb9d211019d99b5875b6d8034617cbc24c2cc/include/algorithm#L896 libc++] and [https://github.com/microsoft/STL/blob/ff83542af4b683fb2f2dea1423fd6c50fe3e13b0/stl/inc/algorithm#L246 MSVC stdlib].
eq fun|1=
template<class InputIt, class Size, class UnaryFunc>
InputIt for_each_n(InputIt first, Size count, UnaryFunc f)
{
for (Size i = 0; i < count; ++first, (void) ++i)
f(*first);
return first;
}

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

void println(const auto& v)
{
    for (auto count{v.size()}; const auto& e : v)
        std::cout << e << (--count ? ", " : "\n");
}

int main()
{
    std::vector<int> vi{1, 2, 3, 4, 5};
    println(vi);

    std::for_each_n(vi.begin(), 3, [](auto& n) { n *= 2; });
    println(vi);
}
```


**Output:**
```
1, 2, 3, 4, 5
2, 4, 6, 4, 5
```


## Defect reports


## See also


| cpp/algorithm/ranges/dsc for_each_n | (see dedicated page) |
| cpp/algorithm/dsc for_each | (see dedicated page) |
| cpp/algorithm/dsc transform | (see dedicated page) |
| cpp/language/dsc range-for | (see dedicated page) |

