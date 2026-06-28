---
title: std::ranges::equal_range
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/equal_range
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|anchor=Version_1|since1=c++20|until1=c++26
|dcl1=
template< std::forward_iterator I, std::sentinel_for<I> S,
class T, class Proj = std::identity,
std::indirect_strict_weak_order
<const T*, std::projected<I, Proj>> Comp = ranges::less >
constexpr ranges::subrange<I> equal_range( I first, S last, const T& value,
Comp comp = {}, Proj proj = {} );
|dcl2=
template< std::forward_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
class T = std::projected_value_t<I, Proj>,
std::indirect_strict_weak_order
<const T*, std::projected<I, Proj>> Comp = ranges::less >
constexpr ranges::subrange<I> equal_range( I first, S last, const T& value,
Comp comp = {}, Proj proj = {} );
dcl rev multi|num=2|since1=c++20|until1=c++26
|dcl1=
template< ranges::forward_range R,
class T, class Proj = std::identity,
std::indirect_strict_weak_order
<const T*, std::projected<ranges::iterator_t<R>,
Proj>> Comp = ranges::less >
constexpr ranges::borrowed_subrange_t<R>
equal_range( R&& r, const T& value, Comp comp = {}, Proj proj = {} );
|dcl2=
template< ranges::forward_range R,
class Proj = std::identity,
class T = std::projected_value_t<ranges::iterator_t<R>, Proj>,
std::indirect_strict_weak_order
<const T*, std::projected<ranges::iterator_t<R>,
Proj>> Comp = ranges::less >
constexpr ranges::borrowed_subrange_t<R>
equal_range( R&& r, const T& value, Comp comp = {}, Proj proj = {} );
```

1. Returns a view containing all elements equivalent to `value` in the range [first, last).
The range [first, last) must be at least partially ordered with respect to `value`, i.e. it must satisfy all of the following requirements:
* partitioned with respect to `element < value` or `comp(element, value)` (that is, all elements for which the expression is `true` precedes all elements for which the expression is `false`).
* partitioned with respect to `!(value < element)` or `!comp(value, element)`.
* for all elements, if `element < value` or `comp(element, value)` is `true` then `!(value < element)` or `!comp(value, element)` is also `true`.
A fully-sorted range meets these criteria.
The returned view is constructed from two iterators, one pointing to the first element that is ''not less'' than `value` and another pointing to the first element ''greater'' than `value`. The first iterator may be alternatively obtained with `std::ranges::lower_bound()`, the second - with `std::ranges::upper_bound()`.
2. Same as , but uses `r` as the source range, as if using the range `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to examine, sentinel=yes}})` - 
- `r` - the range of the elements to examine
- `value` - value to compare the elements to
- `comp` - if the first argument is ''less'' than (i.e. is ordered before) the second
- `proj` - projection to apply to the elements

## Return value

`std::ranges::subrange` containing a pair of iterators defining the wanted range, the first pointing to the first element that is ''not less'' than `value` and the second pointing to the first element ''greater'' than `value`.
If there are no elements ''not less'' than `value`, the last iterator (iterator that is equal to `last` or `ranges::end(r)`) is returned as the first element. Similarly if there are no elements ''greater'' than `value`, the last iterator is returned as the second element.

## Complexity

The number of comparisons performed is logarithmic in the distance between `first` and `last` (at most $2 * log comparisons). However, for an iterator that does not model , the number of iterator increments is linear.

## Possible implementation

eq fun|1=
struct equal_range_fn
{
template<std::forward_iterator I, std::sentinel_for<I> S,
class Proj = std::identity, class T = std::projected_value_t<I, Proj>,
std::indirect_strict_weak_order
<const T*, std::projected<I, Proj>> Comp = ranges::less>
constexpr ranges::subrange<I>
operator()(I first, S last, const T& value, Comp comp = {}, Proj proj = {}) const
{
return ranges::subrange
(
ranges::lower_bound(first, last, value, std::ref(comp), std::ref(proj)),
ranges::upper_bound(first, last, value, std::ref(comp), std::ref(proj))
);
}
template<ranges::forward_range R, class Proj = std::identity,
class T = std::projected_value_t<ranges::iterator_t<R>, Proj>,
std::indirect_strict_weak_order
<const T*, std::projected<ranges::iterator_t<R>,
Proj>> Comp = ranges::less>
constexpr ranges::borrowed_subrange_t<R>
operator()(R&& r, const T& value, Comp comp = {}, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), value,
std::ref(comp), std::ref(proj));
}
};
inline constexpr equal_range_fn equal_range;

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <compare>
#include <complex>
#include <iostream>
#include <vector>

struct S
{
    int number {};
    char name {};
    // note: name is ignored by these comparison operators
    friend bool operator== (const S s1, const S s2) { return s1.number == s2.number; }
    friend auto operator<=>(const S s1, const S s2) { return s1.number <=> s2.number; }
    friend std::ostream& operator<<(std::ostream& os, S o)
    {
        return os << '{' << o.number << ", '" << o.name << "'}";
    }
};

void println(auto rem, const auto& v)
{
    for (std::cout << rem; const auto& e : v)
        std::cout << e << ' ';
    std::cout << '\n';
}

int main()
{
    // note: not ordered, only partitioned w.r.t. S defined below
    std::vector<S> vec
    {
        {1,'A'}, {2,'B'}, {2,'C'}, {2,'D'}, {4, 'D'}, {4,'G'}, {3,'F'}
    };

    const S value{2, '?'};

    namespace ranges = std::ranges;

    auto a = ranges::equal_range(vec, value);
    println("1. ", a);

    auto b = ranges::equal_range(vec.begin(), vec.end(), value);
    println("2. ", b);

    auto c = ranges::equal_range(vec, 'D', ranges::less {}, &S::name);
    println("3. ", c);

    auto d = ranges::equal_range(vec.begin(), vec.end(), 'D', ranges::less {}, &S::name);
    println("4. ", d);

    using CD = std::complex<double>;
    std::vector<CD> nums{<!---->{1, 0}, {2, 2}, {2, 1}, {3, 0}, {3, 1}<!---->};
    auto cmpz = [](CD x, CD y) { return x.real() < y.real(); };
    #ifdef __cpp_lib_algorithm_default_value_type
        auto p3 = ranges::equal_range(nums, {2, 0}, cmpz);
    #else
        auto p3 = ranges::equal_range(nums, CD{2, 0}, cmpz);
    #endif
    println("5. ", p3);
}
```


**Output:**
```
1. {2, 'B'} {2, 'C'} {2, 'D'}
2. {2, 'B'} {2, 'C'} {2, 'D'}
3. {2, 'D'} {4, 'D'}
4. {2, 'D'} {4, 'D'}
5. (2,2) (2,1)
```


## See also


| cpp/algorithm/ranges/dsc lower_bound | (see dedicated page) |
| cpp/algorithm/ranges/dsc upper_bound | (see dedicated page) |
| cpp/algorithm/ranges/dsc binary_search | (see dedicated page) |
| cpp/algorithm/ranges/dsc partition | (see dedicated page) |
| cpp/algorithm/ranges/dsc equal | (see dedicated page) |
| cpp/algorithm/dsc equal_range | (see dedicated page) |

