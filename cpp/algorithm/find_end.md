---
title: std::find_end
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/find_end
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|constexpr=c++20|
template< class ForwardIt1, class ForwardIt2 >
ForwardIt1 find_end( ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2 );
dcla|num=2|constexpr=c++20|
template< class ForwardIt1, class ForwardIt2, class BinaryPred >
ForwardIt1 find_end( ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2,
BinaryPred p );
dcl|num=3|since=c++17|
template< class ExecutionPolicy, class ForwardIt1, class ForwardIt2 >
ForwardIt1 find_end( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2 );
dcl|num=4|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class BinaryPred >
ForwardIt1 find_end( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2,
BinaryPred p );
```

Searches for the last occurrence of the target range [first2, last2) in the source range [first1, last1).
1. Elements are compared using `1=operator==`.
2. Elements are compared using the given binary predicate `p`.
@3,4@ Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `[first1, last1)` - 
- `[first2, last2)` - 
- `policy` - execution policy

**Type requirements:**

- `ForwardIt1`
- `ForwardIt2`

## Return value

Iterator to the beginning of the last occurrence of the target range in source range.
If the target range is empty or it does not appear in the source range, `last1` is returned.

## Complexity

Given  as `std::distance(first1, last1)` and  as `std::distance(first2, last2)`:
1. At most ⋅(N-N+1) comparisons using `1=operator==`.
2. At most ⋅(N-N+1) applications of `p`.
3. } comparisons using `1=operator==`.
4. } applications of `p`.

## Exceptions

@3,4@

## Possible implementation

eq impl
|title1=find_end (1)|ver1=1|1=
template<class ForwardIt1, class ForwardIt2>
constexpr //< since C++20
ForwardIt1 find_end(ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2)
{
if (first2 == last2)
return last1;
ForwardIt1 result = last1;
while (true)
{
ForwardIt1 new_result = std::search(first1, last1, first2, last2);
if (new_result == last1)
break;
else
{
result = new_result;
first1 = result;
++first1;
}
}
return result;
}
|title2=find_end (2)|ver2=2|2=
template<class ForwardIt1, class ForwardIt2, class BinaryPred>
constexpr //< since C++20
ForwardIt1 find_end(ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2, BinaryPred p)
{
if (first2== last2)
return last1;
ForwardIt1 result = last1;
while (true)
{
ForwardIt1 new_result = std::search(first1, last1, first2, first2, p);
if (new_result == last1)
break;
else
{
result = new_result;
first1 = result;
++first1;
}
}
return result;
}

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <cmath>
#include <iostream>

auto print_result = [](auto result, const auto& v)
{
    result == v.end()
        ? std::cout << "Sequence not found\n"
        : std::cout << "Last occurrence is at: " << std::distance(v.begin(), result)
                    << '\n';
};

int main()
{
    const auto v = {1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4};

    for (const auto& x : {std::array{1, 2, 3}, {4, 5, 6}<!---->})
    {
        auto iter = std::find_end(v.begin(), v.end(), x.begin(), x.end()); // overload (1)
        print_result(iter, v);
    }

    for (const auto& x : {std::array{-1, -2, -3}, {-4, -5, -6}<!---->})
    {
        auto iter = std::find_end(v.begin(), v.end(), x.begin(), x.end(), // overload (3)
                                  [](int x, int y)
                                  {
                                      return std::abs(x) == std::abs(y);
                                  });
        print_result(iter, v);
    }
}
```


**Output:**
```
Last occurrence is at: 8
Sequence not found
Last occurrence is at: 8
Sequence not found
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-1205 | C++98 | the return value was unclear if the target range is empty | returns c |
| lwg-2150 | C++98 | the condition of “occurence” was incorrect | corrected |


## See also


| cpp/algorithm/ranges/dsc find_end | (see dedicated page) |
| cpp/algorithm/dsc search | (see dedicated page) |
| cpp/algorithm/dsc includes | (see dedicated page) |
| cpp/algorithm/dsc adjacent_find | (see dedicated page) |
| cpp/algorithm/dsc find | (see dedicated page) |
| cpp/algorithm/dsc find_first_of | (see dedicated page) |
| cpp/algorithm/dsc search_n | (see dedicated page) |

