---
title: std::ranges::iota
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/iota
---


```cpp
**Header:** `<`numeric`>`
dcl|num=1|since=c++23|1=
template< std::input_or_output_iterator O, std::sentinel_for<O> S,
std::weakly_incrementable T >
requires std::indirectly_writable<O, const T&>
constexpr iota_result<O, T>
iota( O first, S last, T value );
dcl|num=2|since=c++23|1=
template< std::weakly_incrementable T, ranges::output_range<const T&> R >
constexpr iota_result<ranges::borrowed_iterator_t<R>, T>
iota( R&& r, T value );
dcl|since=c++23|num=3|1=
template< class O, class T >
using iota_result = ranges::out_value_result<O, T>;
```

Fills the range [first, last) with sequentially increasing values, starting with `value` and repetitively evaluating `++value`.
Equivalent operation:

```cpp
*(first)     = value;
*(first + 1) = ++value;
*(first + 2) = ++value;
*(first + 3) = ++value;
...
```


## Parameters


### Parameters

- `[3=to fill with sequentially increasing values starting with {{c, value}})` - 
- `value` - initial value to store; the expression `++value` must be well-formed

## Return value

}

## Complexity

Exactly `last - first` increments and assignments.

## Possible implementation

eq fun|1=
struct iota_fn
{
template<std::input_or_output_iterator O, std::sentinel_for<O> S,
std::weakly_incrementable T>
requires std::indirectly_writable<O, const T&>
constexpr iota_result<O, T> operator()(O first, S last, T value) const
{
while (first != last)
{
*first = as_const(value);
++first;
++value;
}
return {std::move(first), std::move(value)};
}
template<std::weakly_incrementable T, std::ranges::output_range<const T&> R>
constexpr iota_result<std::ranges::borrowed_iterator_t<R>, T>
operator()(R&& r, T value) const
{
return (*this)(std::ranges::begin(r), std::ranges::end(r), std::move(value));
}
};
inline constexpr iota_fn iota;

## Notes

The function is named after the integer function <span style="font-size: 1.5em">⍳</span>  from the programming language [APL_(programming_language)|APL](https://en.wikipedia.org/wiki/APL_(programming_language)|APL).

## Example


### Example

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <list>
#include <numeric>
#include <random>
#include <vector>

template <typename Proj = std::identity>
void println(auto comment, std::ranges::input_range auto&& range, Proj proj = {})
{
    for (std::cout << comment; auto const &element : range)
        std::cout << proj(element) << ' ';
    std::cout << '\n';
}

int main()
{
    std::list<int> list(8);

    // Fill the list with ascending values: 0, 1, 2, ..., 7
    std::ranges::iota(list, 0);
    println("List: ", list);

    // A vector of iterators (see the comment to Example)
    std::vector<std::list<int>::iterator> vec(list.size());

    // Fill with iterators to consecutive list's elements
    std::ranges::iota(vec.begin(), vec.end(), list.begin());

    std::ranges::shuffle(vec, std::mt19937 {std::random_device {}()});
    println("List viewed via vector: ", vec, [](auto it) { return *it; });
}
```


**Output:**
```
List: 0 1 2 3 4 5 6 7
List viewed via vector: 5 7 6 0 1 3 4 2
```


## See also


| cpp/algorithm/dsc fill | (see dedicated page) |
| cpp/algorithm/ranges/dsc fill | (see dedicated page) |
| cpp/algorithm/dsc generate | (see dedicated page) |
| cpp/algorithm/ranges/dsc generate | (see dedicated page) |
| cpp/ranges/dsc iota_view | (see dedicated page) |
| cpp/ranges/dsc views indices | (see dedicated page) |
| cpp/algorithm/dsc iota | (see dedicated page) |

