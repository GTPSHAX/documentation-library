---
title: std::ranges::subrange
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/subrange
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++20|1=
template<
std::input_or_output_iterator I,
std::sentinel_for<I> S = I,
ranges::subrange_kind K = std::sized_sentinel_for<S, I> ?
ranges::subrange_kind::sized :
ranges::subrange_kind::unsized >
requires (K == ranges::subrange_kind::sized  !std::sized_sentinel_for<S, I>)
class subrange
: public ranges::view_interface<subrange<I, S, K>>
dcla|num=2|expos=yes|1=
template<class From, class To>
concept /*uses-nonqualification-pointer-conversion*/ =
/* see description */;
dcla|num=3|expos=yes|1=
template<class From, class To>
concept /*convertible-to-non-slicing*/ = /* see description */;
```

1. The `subrange` class template combines together an iterator and a sentinel into a single . It models  whenever the final template parameter is `subrange_kind​::​sized` (which happens when `std::sized_sentinel_for<S, I>` is satisfied or when size is passed explicitly as a constructor argument).
2. Determines whether `From` is convertible to `To` without . Equivalent to:

```cpp
template<class From, class To>
concept /*uses-nonqualification-pointer-conversion*/ =
    std::is_pointer_v<From> && std::is_pointer_v<To> &&
        !std::convertible_to<std::remove_pointer_t<From>(*)[],
                             std::remove_pointer_t<To>(*)[]>;
```

3. Determines whether `From` is convertible to `To` without derived-to-base conversion:

```cpp
template<class From, class To>
concept /*convertible-to-non-slicing*/ =
    std::convertible_to<From, To> &&
        !/*uses-nonqualification-pointer-conversion*/
            <std::decay_t<From>, std::decay_t<To>>;
```


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/subrange/dsc operator PairLike | (see dedicated page) |

#### Observers

| cpp/ranges/subrange/dsc begin | (see dedicated page) |
| cpp/ranges/subrange/dsc end | (see dedicated page) |
| cpp/ranges/subrange/dsc empty | (see dedicated page) |
| cpp/ranges/subrange/dsc size | (see dedicated page) |

#### Iterator operations

| cpp/ranges/subrange/dsc advance | (see dedicated page) |
| cpp/ranges/subrange/dsc prev | (see dedicated page) |
| cpp/ranges/subrange/dsc next | (see dedicated page) |


## 


## Non-member functions


| cpp/ranges/subrange/dsc get | (see dedicated page) |


## Helper types


| cpp/ranges/dsc subrange_kind | (see dedicated page) |
| cpp/ranges/subrange/dsc tuple_size | (see dedicated page) |
| cpp/ranges/subrange/dsc tuple_element | (see dedicated page) |


## Helper templates

ddcl|since=c++20|1=
template< class I, class S, ranges::subrange_kind K >
constexpr bool ranges::enable_borrowed_range<ranges::subrange<I, S, K>> = true;
This specialization of `ranges::enable_borrowed_range` makes `subrange` satisfy .

## Example


### Example

```cpp
#include <map>
#include <print>
#include <ranges>

void make_uppercase(char& v)
{
    v += 'A' - 'a';
}

void uppercase_transform(std::multimap<int, char>& m, int k)
{
    auto [first, last] = m.equal_range(k);
    for (auto& [_, v] : std::ranges::subrange(first, last))
        make_uppercase(v);
}

int main()
{
    std::multimap<int, char> mm{<!---->{4, 'a'}, {3, '-'}, {4, 'b'}, {5, '-'}, {4, 'c'}<!---->};
    std::println("Before: {}", mm);
    uppercase_transform(mm, 4);
    std::println("After:  {}", mm);
}
```


**Output:**
```
Before: {3: '-', 4: 'a', 4: 'b', 4: 'c', 5: '-'}
After:  {3: '-', 4: 'A', 4: 'B', 4: 'C', 5: '-'}
```


## Defect reports


## See also


| cpp/ranges/dsc view_interface | (see dedicated page) |


## External links

