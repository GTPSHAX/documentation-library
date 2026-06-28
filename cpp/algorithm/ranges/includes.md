---
title: std::ranges::includes
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/includes
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::input_iterator I1, std::sentinel_for<I1> S1,
std::input_iterator I2, std::sentinel_for<I2> S2,
class Proj1 = std::identity, class Proj2 = std::identity,
std::indirect_strict_weak_order<
std::projected<I1, Proj1>,
std::projected<I2, Proj2>> Comp = ranges::less >
constexpr bool
includes( I1 first1, S1 last1, I2 first2, S2 last2,
Comp comp = {}, Proj1 proj1 = {}, Proj2 proj2 = {} )
dcl|num=2|since=c++20|1=
template< ranges::input_range R1, ranges::input_range R2,
class Proj1 = std::identity, class Proj2 = std::identity,
std::indirect_strict_weak_order<
std::projected<ranges::iterator_t<R1>, Proj1>,
std::projected<ranges::iterator_t<R2>, Proj2>> Comp = ranges::less >
constexpr bool
includes( R1&& r1, R2&& r2, Comp comp = {}, Proj1 proj1 = {}, Proj2 proj2 = {} )
```

1. Returns `true` if the projections of the sorted range [first2, last2) is a [subsequence](https://en.wikipedia.org/wiki/subsequence) of the projections of the sorted range [first1, last1).
2. Same as , but uses `r1` and `r2` as the source ranges, as if by using `ranges::begin(r1)` and `ranges::begin(r2)` as `first1` and `first2` respectively, and `ranges::end(r1)` and `ranges::end(r2)` as `last1` and `last2` respectively.
Both ranges must be sorted with the given comparison function `comp`. A subsequence need not be contiguous.

## Parameters


### Parameters

- `[first1, last1)` - 
- `r1` - the sorted range of elements to examine
- `[first2, last2)` - 
- `r2` - the sorted range of elements to search for
- `comp` - comparison function to apply to the projected elements
- `proj1` - projection to apply to the elements in the first range
- `proj2` - projection to apply to the elements in the second range

## Return value

`true` if [first2, last2) is a subsequence of [first1, last1); otherwise `false`.

## Complexity

At most  comparisons, where  is `ranges::distance(r1)` and  is `ranges::distance(r2)`.

## Possible implementation

eq fun
|1=
struct includes_fn
{
template<std::input_iterator I1, std::sentinel_for<I1> S1,
std::input_iterator I2, std::sentinel_for<I2> S2,
class Proj1 = std::identity, class Proj2 = std::identity,
std::indirect_strict_weak_order<
std::projected<I1, Proj1>,
std::projected<I2, Proj2>> Comp = ranges::less>
constexpr bool operator()(I1 first1, S1 last1, I2 first2, S2 last2,
Comp comp = {}, Proj1 proj1 = {}, Proj2 proj2 = {}) const
{
for (; first2 != last2; ++first1)
{
if (first1 == last1  comp(*first2, *first1))
return false;
if (!comp(*first1, *first2))
++first2;
}
return true;
}
template<ranges::input_range R1, ranges::input_range R2,
class Proj1 = std::identity, class Proj2 = std::identity,
std::indirect_strict_weak_order<
std::projected<ranges::iterator_t<R1>, Proj1>,
std::projected<ranges::iterator_t<R2>, Proj2>> Comp = ranges::less>
constexpr bool operator()(R1&& r1, R2&& r2, Comp comp = {},
Proj1 proj1 = {}, Proj2 proj2 = {}) const
{
return (*this)(ranges::begin(r1), ranges::end(r1),
ranges::begin(r2), ranges::end(r2),
std::ref(comp), std::ref(proj1), std::ref(proj2));
}
};
inline constexpr auto includes = includes_fn {};

## Example


### Example

```cpp
#include <algorithm>
#include <cctype>
#include <initializer_list>
#include <iomanip>
#include <iostream>
#include <locale>
#include <string>

template<class T>
std::ostream& operator<<(std::ostream& os, std::initializer_list<T> const& list)
{
    for (os << "{ "; auto const& elem : list)
        os << elem << ' ';
    return os << "} ";
}

struct true_false : std::numpunct<char>
{
    std::string do_truename() const { return "? Yes\n"; }
    std::string do_falsename() const { return "? No\n"; }
};

int main()
{
    std::cout.imbue(std::locale(std::cout.getloc(), new true_false));

    auto ignore_case = [](char a, char b) { return std::tolower(a) < std::tolower(b); };

    const auto
        a = {'a', 'b', 'c'},
        b = {'a', 'c'},
        c = {'a', 'a', 'b'},
        d = {'g'},
        e = {'a', 'c', 'g'},
        f = {'A', 'B', 'C'},
        z = {'a', 'b', 'c', 'f', 'h', 'x'};

    std::cout
        << z << "includes\n" << std::boolalpha
        << a << std::ranges::includes(z.begin(), z.end(), a.begin(), a.end())
        << b << std::ranges::includes(z, b)
        << c << std::ranges::includes(z, c)
        << d << std::ranges::includes(z, d)
        << e << std::ranges::includes(z, e)
        << f << std::ranges::includes(z, f, ignore_case);
}
```


**Output:**
```
{ a b c f h x } includes
{ a b c } ? Yes
{ a c } ? Yes
{ a a b } ? No
{ g } ? No
{ a c g } ? No
{ A B C } ? Yes
```


## See also


| cpp/algorithm/ranges/dsc set_difference | (see dedicated page) |
| cpp/algorithm/ranges/dsc search | (see dedicated page) |
| cpp/algorithm/ranges/dsc contains | (see dedicated page) |
| cpp/algorithm/dsc includes | (see dedicated page) |

