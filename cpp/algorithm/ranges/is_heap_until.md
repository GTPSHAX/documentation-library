---
title: std::ranges::is_heap_until
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/is_heap_until
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::random_access_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
std::indirect_strict_weak_order
< std::projected<I, Proj>> Comp = ranges::less >
constexpr I is_heap_until( I first, S last, Comp comp = {}, Proj proj = {} );
dcl|num=2|since=c++20|1=
template< ranges::random_access_range R, class Proj = std::identity,
std::indirect_strict_weak_order
<std::projected
<ranges::iterator_t<R>, Proj>> Comp = ranges::less >
constexpr ranges::borrowed_iterator_t<R>
is_heap_until( R&& r, Comp comp = {}, Proj proj = {} );
```

Within the specified range, finds the longest range which starting from the beginning of the specified range and represents a heap with respect to `comp` and `proj`.
1. The specified range is [first, last).
2. The specified range is `r`.

## Parameters


### Parameters

- `first, last` - the range of elements to examine
- `r` - the range of elements to examine
- `pred` - predicate to apply to the projected elements
- `proj` - projection to apply to the elements

## Return value

The last iterator `iter` in the specified range for which:
1. The range [first, iter) is a heap with respect to `comp` and `proj`.
2. The range [ranges::begin(r), iter) is a heap with respect to `comp` and `proj`.

## Complexity

applications of `comp` and `proj`, where  is:
1. `ranges::distance(first, last)`
2. `ranges::distance(r)`

## Possible implementation

eq fun|1=
struct is_heap_until_fn
{
template<std::random_access_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
std::indirect_strict_weak_order
<std::projected<I, Proj>> Comp = ranges::less>
constexpr I operator()(I first, S last, Comp comp = {}, Proj proj = {}) const
{
std::iter_difference_t<I> n{ranges::distance(first, last)}, dad{0}, son{1};
for (; son != n; ++son)
{
if (std::invoke(comp, std::invoke(proj, *(first + dad)),
std::invoke(proj, *(first + son))))
return first + son;
else if ((son % 2) == 0)
++dad;
}
return first + n;
}
template<ranges::random_access_range R, class Proj = std::identity,
std::indirect_strict_weak_order
<std::projected<ranges::iterator_t<R>, Proj>> Comp = ranges::less>
constexpr ranges::borrowed_iterator_t<R>
operator()(R&& r, Comp comp = {}, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::move(comp), std::move(proj));
}
};
inline constexpr is_heap_until_fn is_heap_until{};

## Example


### Example

```cpp
#include <algorithm>
#include <cmath>
#include <iostream>
#include <iterator>
#include <vector>

void out(const auto& what, int n = 1)
{
    while (n-- > 0)
        std::cout << what;
}

void draw_bin_tree(auto first, auto last)
{
    auto bails = [](int n, int w)
    {
        auto b = [](int w) { out("┌"), out("─", w), out("┴"), out("─", w), out("┐"); };
        n /= 2;
        if (!n)
            return;
        for (out(' ', w); n-- > 0;)
            b(w), out(' ', w + w + 1);
        out('\n');
    };

    auto data = [](int n, int w, auto& first, auto last)
    {
        for (out(' ', w); n-- > 0 && first != last; ++first)
            out(*first), out(' ', w + w + 1);
        out('\n');
    };

    auto tier = [&](int t, int m, auto& first, auto last)
    {
        const int n{1 << t};
        const int w{(1 << (m - t - 1)) - 1};
        bails(n, w), data(n, w, first, last);
    };

    const auto size{std::ranges::distance(first, last)};
    const int m{static_cast<int>(std::ceil(std::log2(1 + size)))};
    for (int i{}; i != m; ++i)
        tier(i, m, first, last);
}

int main()
{
    std::vector<int> v{3, 1, 4, 1, 5, 9};
    std::ranges::make_heap(v);

    // probably mess up the heap
    v.push_back(2);
    v.push_back(6);

    out("v after make_heap and push_back:\n");
    draw_bin_tree(v.begin(), v.end());

    out("the max-heap prefix of v:\n");
    const auto heap_end = std::ranges::is_heap_until(v);
    draw_bin_tree(v.begin(), heap_end);
}
```


**Output:**
```
<nowiki/>
v after make_heap and push_back: 
       9               
   ┌───┴───┐       
   5       4       
 ┌─┴─┐   ┌─┴─┐   
 1   1   3   2   
┌┴┐ ┌┴┐ ┌┴┐ ┌┴┐ 
6 
the max-heap prefix of v: 
   9       
 ┌─┴─┐   
 5   4   
┌┴┐ ┌┴┐ 
1 1 3 2
```


## See also


| cpp/algorithm/ranges/dsc is_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc make_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc push_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc pop_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc sort_heap | (see dedicated page) |
| cpp/algorithm/dsc is_heap_until | (see dedicated page) |

