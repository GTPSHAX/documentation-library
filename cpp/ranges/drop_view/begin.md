---
title: std::ranges::drop_view::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/drop_view/begin
---


```cpp
dcl|num=1|since=c++20|
constexpr auto begin()
requires (!(/*simple-view*/<V> &&
ranges::random_access_range<const V> &&
ranges::sized_range<const V>));
dcl|num=2|since=c++20|
constexpr auto begin() const
requires ranges::random_access_range<const V> &&
ranges::sized_range<const V>;
```

Returns an iterator to the first element of the `drop_view`, that is, an iterator to the ''N'' element of the underlying view, or to the end of the underlying view if it has less than ''N'' elements.
If `V` is not a  or a , in order to provide the amortized constant time complexity required by the  concept, the overload  caches the result within the underlying  object for use on subsequent calls.

## Return value

.

## Example


### Example

```cpp
#include <array>
#include <concepts>
#include <iostream>
#include <iterator>
#include <ranges>

void println(std::ranges::range auto const& range)
{
    for (auto const& elem : range)
        std::cout << elem;
    std::cout << '\n';
}

int main()
{
    std::array hi{'H', 'e', 'l', 'l', 'o', ',', ' ', 'C', '+', '+', '2', '0', '!'};
    println(hi);

    const auto pos = std::distance(hi.begin(), std::ranges::find(hi, 'C'));
    auto cxx = std::ranges::drop_view{hi, pos};
    std::cout << "*drop_view::begin() == '" << *cxx.begin() << "'\n";
//  *cxx.begin() = 'c'; // undefined: 'views' are to be used as observers
    println(cxx);
}
```


**Output:**
```
Hello, C++20!
*drop_view::begin() == 'C'
C++20!
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-3482 | C++20 | the const overload can be called with unsized ranges | the const overload requires tt |


## See also


| cpp/ranges/adaptor/dsc end|drop_view | (see dedicated page) |
| cpp/ranges/dsc begin | (see dedicated page) |
| cpp/ranges/dsc end | (see dedicated page) |

