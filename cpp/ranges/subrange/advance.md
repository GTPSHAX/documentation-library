---
title: std::ranges::subrange::advance
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/subrange/advance
---

ddcl|since=c++20|
constexpr subrange& advance( std::iter_difference_t<I> n );
Increments or decrements :
* If `I` models  and `n < 0` is `true`, decrements  by `-n` elements.
: Equivalent to: .
* Otherwise, increments  by `n` elements, or until  is reached.
: Equivalent to: .
According to the preconditions of `ranges::advance`, if `n < 0` is `true` and  cannot be decremented by `-n` elements, the behavior is undefined.

## Parameters


### Parameters

- `n` - number of maximal increments of the iterator

## Return value

`*this`

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <iterator>
#include <ranges>

void print(auto name, auto const sub)
{
    std::cout << name << ".size() == " << sub.size() << "; { ";
    std::ranges::for_each(sub, [](int x) { std::cout << x << ' '; });
    std::cout << "}\n";
};

int main()
{
    std::array arr{1, 2, 3, 4, 5, 6, 7};
    std::ranges::subrange sub{std::next(arr.begin()), std::prev(arr.end())};
    print("1) sub", sub);
    print("2) sub", sub.advance(3));
    print("3) sub", sub.advance(-2));
}
```


**Output:**
```
1) sub.size() == 5; { 2 3 4 5 6 }
2) sub.size() == 2; { 5 6 }
3) sub.size() == 4; { 3 4 5 6 }
```


## Defect reports


## See also


| cpp/ranges/subrange/dsc next | (see dedicated page) |
| cpp/ranges/subrange/dsc prev | (see dedicated page) |
| cpp/iterator/dsc advance | (see dedicated page) |
| cpp/iterator/ranges/dsc advance | (see dedicated page) |

