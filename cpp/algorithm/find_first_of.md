---
title: std::find_first_of
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/find_first_of
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|constexpr=c++20|
template< class InputIt, class ForwardIt >
InputIt find_first_of( InputIt first1, InputIt last1,
ForwardIt first2, ForwardIt last2 );
dcla|num=2|constexpr=c++20|
template< class InputIt, class ForwardIt, class BinaryPred >
InputIt find_first_of( InputIt first1, InputIt last1,
ForwardIt first2, ForwardIt last2,
BinaryPred p );
dcl|num=3|since=c++17|
template< class ExecutionPolicy, class ForwardIt1, class ForwardIt2 >
ForwardIt1 find_first_of( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2 );
dcl|num=4|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class BinaryPred >
ForwardIt1 find_first_of( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt last1,
ForwardIt2 first2, ForwardIt2 last2,
BinaryPred p );
```

Searches the source range [first1, last1) for any of the elements in the target range [first2, last2).
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

- `InputIt`
- `ForwardIt`
- `ForwardIt1`
- `ForwardIt2`
- `BinaryPred`

## Return value

Iterator to the first element in the source range that matches an element from the target range.
If the target range is empty or if no such element is found, `last1` is returned.

## Complexity

Given  as `std::distance(first1, last1)` and  as `std::distance(first2, last2)`:
1. At most ⋅N comparisons using `1=operator==`.
2. At most ⋅N applications of `p`.
3. } comparisons using `1=operator==`.
4. } applications of `p`.

## Exceptions

@3,4@

## Possible implementation

eq impl
|title1=find_first_of (1)|ver1=1|1=
template<class InputIt, class ForwardIt>
InputIt find_first_of(InputIt first1, InputIt last1,
ForwardIt first2, ForwardIt last2)
{
for (; first1 != last1; ++first1)
for (ForwardIt it = first2; it != last2; ++it)
if (*first1 == *it)
return first1;
return last1;
}
|title2=find_first_of (2)|ver2=2|2=
template<class InputIt, class ForwardIt, class BinaryPred>
InputIt find_first_of(InputIt first1, InputIt last1,
ForwardIt first2, ForwardIt last2,
BinaryPred p)
{
for (; first1 != last1; ++first1)
for (ForwardIt it = first2; it != last2; ++it)
if (p(*first1, *it))
return first1;
return last1;
}

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

auto print_sequence = [](const auto id, const auto& seq, int pos = -1)
{
    std::cout << id << "{ ";
    for (int i{}; const auto& e : seq)
    {
        const bool mark{i == pos};
        std::cout << (i++ ? ", " : "");
        std::cout << (mark ? "[ " : "") << e << (mark ? " ]" : "");
    }
    std::cout << " }\n";
};

int main()
{
    const std::vector<int> v{0, 2, 3, 25, 5};
    const auto t1 = {19, 10, 3, 4};
    const auto t2 = {1, 6, 7, 9};

    auto find_any_of = [](const auto& v, const auto& t)
    {
        const auto result = std::find_first_of(v.begin(), v.end(),
                                               t.begin(), t.end());
        if (result == v.end())
        {
            std::cout << "No elements of v are equal to any element of ";
            print_sequence("t = ", t);
            print_sequence("v = ", v);
        }
        else
        {
            const auto pos = std::distance(v.begin(), result);
            std::cout << "Found a match (" << *result << ") at position " << pos;
            print_sequence(", where t = ", t);
            print_sequence("v = ", v, pos);
        }
    };

    find_any_of(v, t1);
    find_any_of(v, t2);
}
```


**Output:**
```
Found a match (3) at position 2, where t = { 19, 10, 3, 4 }
v = { 0, 2, [ 3 ], 25, 5 }
No elements of v are equal to any element of t = { 1, 6, 7, 9 }
v = { 0, 2, 3, 25, 5 }
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-1205 | C++98 | the return value was unclear if the target range is empty | returns c |


## See also


| cpp/algorithm/ranges/dsc find_first_of | (see dedicated page) |
| cpp/algorithm/dsc find | (see dedicated page) |

