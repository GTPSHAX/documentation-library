---
title: std::lexicographical_compare_three_way
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/lexicographical_compare_three_way
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++20|num=1|
template< class InputIt1, class InputIt2, class Cmp >
constexpr auto lexicographical_compare_three_way
( InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2,
Cmp comp ) -> decltype(comp(*first1, *first2));
dcl|since=c++20|num=2|
template< class InputIt1, class InputIt2 >
constexpr auto lexicographical_compare_three_way
( InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2 );
```

Lexicographically compares two ranges [first1, last1) and [first2, last2) using three-way comparison and produces a result of the strongest applicable comparison category type.
1. Returns the order between the first non-equivalent pair of elements according to `comp` in both ranges if any, otherwise (if one ranges is equivalent to the prefix of another according to `comp`), returns the order between the length of both ranges.
2. Equivalent to
If the return type is not one of the three comparison category types, the program is ill-formed:
*
*
*

## Parameters


### Parameters

- `[first1, last1)` - 
- `[first2, last2)` - 
- `comp` - a function object

**Type requirements:**

- `InputIt1, InputIt2`

## Return value

The value of a comparison category type specified above.

## Complexity

Given  as `std::distance(first1, last1)` and  as `std::distance(first2, last2)`:
1. At most ,N) applications of `comp`.
2. At most ,N) applications of `std::compare_three_way()`.

## Possible implementation

eq fun|1=
template<class I1, class I2, class Cmp>
constexpr auto lexicographical_compare_three_way(I1 f1, I1 l1, I2 f2, I2 l2, Cmp comp)
-> decltype(comp(*f1, *f2))
{
using ret_t = decltype(comp(*f1, *f2));
static_assert(std::disjunction_v<
std::is_same<ret_t, std::strong_ordering>,
std::is_same<ret_t, std::weak_ordering>,
std::is_same<ret_t, std::partial_ordering>>,
"The return type must be a comparison category type.");
bool exhaust1 = (f1 == l1);
bool exhaust2 = (f2 == l2);
for (; !exhaust1 && !exhaust2; exhaust1 = (++f1 == l1), exhaust2 = (++f2 == l2))
if (auto c = comp(*f1, *f2); c != 0)
return c;
return !exhaust1 ? std::strong_ordering::greater:
!exhaust2 ? std::strong_ordering::less:
std::strong_ordering::equal;
}

## Example


### Example

```cpp
#include <algorithm>
#include <cctype>
#include <compare>
#include <iomanip>
#include <iostream>
#include <string_view>
#include <utility>

using namespace std::literals;

void show_result(std::string_view s1, std::string_view s2, std::strong_ordering o)
{
    std::cout << std::quoted(s1) << " is ";
    std::is_lt(o) ? std::cout << "less than ":
    std::is_gt(o) ? std::cout << "greater than ":
                    std::cout << "equal to ";
    std::cout << std::quoted(s2) << '\n';
}

std::strong_ordering cmp_icase(unsigned char x, unsigned char y)
{
    return std::toupper(x) <=> std::toupper(y);
};

int main()
{
    for (const auto& [s1, s2] :
    {
        std::pair{"one"sv, "ONE"sv}, {"two"sv, "four"sv}, {"three"sv, "two"sv}
    })
    {
        const auto res = std::lexicographical_compare_three_way(
            s1.cbegin(), s1.cend(), s2.cbegin(), s2.cend(), cmp_icase);
        show_result(s1, s2, res);
    }
}
```


**Output:**
```
"one" is equal to "ONE"
"two" is greater than "four"
"three" is less than "two"
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-3410 | C++20 | extraneous comparisons between iterators were required | such requirement removed |


## See also


| cpp/algorithm/dsc lexicographical_compare | (see dedicated page) |
| cpp/utility/compare/dsc compare_three_way | (see dedicated page) |
| cpp/algorithm/ranges/dsc lexicographical_compare | (see dedicated page) |

