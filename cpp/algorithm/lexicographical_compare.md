---
title: std::lexicographical_compare
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/lexicographical_compare
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2 >
bool lexicographical_compare( InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2 );
dcl|num=2|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2 >
bool lexicographical_compare( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2 );
dcla|num=3|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2, class Compare >
bool lexicographical_compare( InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2,
Compare comp );
dcl|num=4|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class Compare >
bool lexicographical_compare( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2,
Compare comp );
```

Checks if the first range [first1, last1) is lexicographically ''less'' than the second range [first2, last2).
1. Elements are compared using `operator<`.
3. Elements are compared using the given binary comparison function `comp`.
@2,4@ Same as , but executed according to `policy`.
Lexicographical comparison is an operation with the following properties:
* Two ranges are compared element by element.
* The first mismatching element defines which range is lexicographically ''less'' or ''greater'' than the other.
* If one range is a prefix of another, the shorter range is lexicographically ''less'' than the other.
* If two ranges have equivalent elements and are of the same length, then the ranges are lexicographically ''equal''.
* An empty range is lexicographically ''less'' than any non-empty range.
* Two empty ranges are lexicographically ''equal''.

## Parameters


### Parameters

- `[first1, last1)` - 
- `[first2, last2)` - 
- `policy` - execution policy

**Type requirements:**

- `InputIt1, InputIt2`
- `ForwardIt1, ForwardIt2`
- `Compare`

## Return value

`true` if the first range is lexicographically ''less'' than the second, otherwise `false`.

## Complexity

Given  as `std::distance(first1, last1)` and  as `std::distance(first2, last2)`:
@1,2@ At most ,N) comparisons using `operator<`.
@3,4@ At most ,N) applications of the comparison function `comp`.

## Exceptions


## Possible implementation

eq impl
|title1=lexicographical_compare (1)|ver1=1|1=
template<class InputIt1, class InputIt2>
bool lexicographical_compare(InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2)
{
for (; (first1 != last1) && (first2 != last2); ++first1, (void) ++first2)
{
if (*first1 < *first2)
return true;
if (*first2 < *first1)
return false;
}
return (first1 == last1) && (first2 != last2);
}
|title2=lexicographical_compare (3)|ver2=3|2=
template<class InputIt1, class InputIt2, class Compare>
bool lexicographical_compare(InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2, Compare comp)
{
for (; (first1 != last1) && (first2 != last2); ++first1, (void) ++first2)
{
if (comp(*first1, *first2))
return true;
if (comp(*first2, *first1))
return false;
}
return (first1 == last1) && (first2 != last2);
}

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <random>
#include <vector>

void print(const std::vector<char>& v, auto suffix)
{
    for (char c : v)
        std::cout << c << ' ';
    std::cout << suffix;
}

int main()
{
    std::vector<char> v1{'a', 'b', 'c', 'd'};
    std::vector<char> v2{'a', 'b', 'c', 'd'};

    for (std::mt19937 g{std::random_device{}()};
         !std::lexicographical_compare(v1.begin(), v1.end(),
                                       v2.begin(), v2.end());)
    {
        print(v1, ">= ");
        print(v2, '\n');

        std::shuffle(v1.begin(), v1.end(), g);
        std::shuffle(v2.begin(), v2.end(), g);
    }

    print(v1, "<  ");
    print(v2, '\n');
}
```


**Output:**
```
a b c d >= a b c d 
d a b c >= c b d a 
b d a c >= a d c b 
a c d b <  c d a b
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-1205 | C++98 | the results of lexicographical comparisons involving empty ranges were unclear | made clear |


## See also


| cpp/algorithm/dsc equal | (see dedicated page) |
| cpp/algorithm/dsc lexicographical_compare_three_way | (see dedicated page) |
| cpp/algorithm/ranges/dsc lexicographical_compare | (see dedicated page) |

