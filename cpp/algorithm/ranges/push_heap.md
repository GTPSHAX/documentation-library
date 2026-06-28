---
title: std::ranges::push_heap
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/push_heap
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::random_access_iterator I, std::sentinel_for<I> S,
class Comp = ranges::less, class Proj = std::identity >
requires std::sortable<I, Comp, Proj>
constexpr I push_heap( I first, S last, Comp comp = {}, Proj proj = {} );
dcl|num=2|since=c++20|1=
template< ranges::random_access_range R,
class Comp = ranges::less, class Proj = std::identity >
requires std::sortable<ranges::iterator_t<R>, Comp, Proj>
constexpr ranges::borrowed_iterator_t<R>
push_heap( R&& r, Comp comp = {}, Proj proj = {} );
```

Inserts the last element in the specified range into a heap with respect to `comp` and `proj`, where the heap consists of all elements in the range except the last. The heap after the insertion will be the entire range.
1. The specified range is [first, last).
2. The specified range is `r`.
If the specified range (excluding the last element) is not a heap with respect to `comp` and `proj`, the behavior is undefined.

## Parameters


### Parameters

- `[3=to modify, sentinel=yes}})` - 
- `r` - the  of elements to modify
- `comp` - comparator to apply to the projected elements
- `proj` - projection to apply to the elements

## Return value

1. `last`
2. `ranges::end(r)`

## Complexity

At most } applications of `comp` and } applications of `proj`, where  is:
1. `ranges::distance(first, last)`
2. `ranges::distance(r)`

## Possible implementation

eq fun|1=
struct push_heap_fn
{
template<std::random_access_iterator I, std::sentinel_for<I> S,
class Comp = ranges::less, class Proj = std::identity>
requires std::sortable<I, Comp, Proj>
constexpr I operator()(I first, S last, Comp comp = {}, Proj proj = {}) const
{
const auto n{ranges::distance(first, last)};
const auto length{n};
if (n > 1)
{
I last{first + n};
n = (n - 2) / 2;
I i{first + n};
if (std::invoke(comp, std::invoke(proj, *i), std::invoke(proj, *--last)))
{
std::iter_value_t<I> v {ranges::iter_move(last)};
do
{
*last = ranges::iter_move(i);
last = i;
if (n == 0)
break;
n = (n - 1) / 2;
i = first + n;
}
while (std::invoke(comp, std::invoke(proj, *i), std::invoke(proj, v)));
*last = std::move(v);
}
}
return first + length;
}
template<ranges::random_access_range R,
class Comp = ranges::less, class Proj = std::identity>
requires std::sortable<ranges::iterator_t<R>, Comp, Proj>
constexpr ranges::borrowed_iterator_t<R>
operator()(R&& r, Comp comp = {}, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::move(comp), std::move(proj));
}
};
inline constexpr push_heap_fn push_heap{};

## Example


### Example

```cpp
#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

void out(const auto& what, int n = 1)
{
    while (n-- > 0)
        std::cout << what;
}

void print(auto rem, auto const& v)
{
    out(rem);
    for (auto e : v)
        out(e), out(' ');
    out('\n');
}

void draw_heap(auto const& v)
{
    auto bails = [](int n, int w)
    {
        auto b = [](int w) { out("┌"), out("─", w), out("┴"), out("─", w), out("┐"); };
        if (!(n /= 2))
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

    const int m{static_cast<int>(std::ceil(std::log2(1 + v.size())))};
    auto first{v.cbegin()};
    for (int i{}; i != m; ++i)
        tier(i, m, first, v.cend());
}

int main()
{
    std::vector<int> v{1, 6, 1, 8, 0, 3,};
    print("source vector v: ", v);

    std::ranges::make_heap(v);
    print("after make_heap: ", v);
    draw_heap(v);

    v.push_back(9);

    print("before push_heap: ", v);
    draw_heap(v);

    std::ranges::push_heap(v);
    print("after push_heap: ", v);
    draw_heap(v);
}
```


**Output:**
```
<nowiki/>
source vector v: 1 6 1 8 0 3
after make_heap: 8 6 3 1 0 1
   8
 ┌─┴─┐
 6   3
┌┴┐ ┌┴┐
1 0 1
before push_heap: 8 6 3 1 0 1 9
   8
 ┌─┴─┐
 6   3
┌┴┐ ┌┴┐
1 0 1 9
after push_heap: 9 6 8 1 0 1 3
   9
 ┌─┴─┐
 6   8
┌┴┐ ┌┴┐
1 0 1 3
```


## See also


| cpp/algorithm/ranges/dsc is_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc is_heap_until | (see dedicated page) |
| cpp/algorithm/ranges/dsc make_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc pop_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc sort_heap | (see dedicated page) |
| cpp/algorithm/dsc push_heap | (see dedicated page) |

