---
title: std::ranges::split_view::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/split_view/begin
---


```cpp
dcl|since=c++20|1=
constexpr /*iterator*/ begin();
```

Returns an `iterator` to the first found subrange.
In order to provide the amortized constant time complexity required by the  concept, this function caches the result within the `split_view` (by means of  member) for use on subsequent calls.
Let  be the underlying data member. Equivalent to:

```cpp
constexpr /*iterator*/ begin()
{
    if (!cached_begin_.has_value())
        cached_begin_ = this->find_next(ranges::begin(base_));
    return {*this, ranges::begin(base_), cached_begin_.value()};
}
```


## Return value

An `iterator`.

## Complexity

Amortized }.

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <ranges>
#include <string_view>

int main()
{
    constexpr std::string_view sentence{"Keep..moving..forward.."};
    constexpr std::string_view delim{".."};
    std::ranges::split_view words{sentence, delim};

    std::cout << "begin(): " << std::quoted(std::string_view{*words.begin()})
              << "\nSubstrings: ";
    for (auto word : words)
        std::cout << std::quoted(std::string_view(word)) << ' ';

    std::ranges::split_view letters{sentence, std::string_view{""}<!---->};
    std::cout << "\nbegin(): " << std::quoted(std::string_view{*letters.begin()})
              << "\nLetters: ";
    for (auto letter : letters)
        std::cout << std::string_view(letter) << ' ';
    std::cout << '\n';
}
```


**Output:**
```
begin(): "Keep"
Substrings: "Keep" "moving" "forward" ""
begin(): "K"
Letters: K e e p . . m o v i n g . . f o r w a r d . .
```


## See also


| cpp/ranges/adaptor/dsc end|split_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|lazy_split_view | (see dedicated page) |
| cpp/ranges/dsc begin | (see dedicated page) |

