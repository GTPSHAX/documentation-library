---
title: std::search
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/search
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|notes=<sup>(constexpr C++20)</sup>|
template< class ForwardIt1, class ForwardIt2 >
ForwardIt1 search( ForwardIt1 first, ForwardIt1 last,
ForwardIt2 s_first, ForwardIt2 s_last );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class ForwardIt1, class ForwardIt2 >
ForwardIt1 search( ExecutionPolicy&& policy,
ForwardIt1 first, ForwardIt1 last,
ForwardIt2 s_first, ForwardIt2 s_last );
dcla|num=3|notes=<sup>(constexpr C++20)</sup>|
template< class ForwardIt1, class ForwardIt2, class BinaryPred >
ForwardIt1 search( ForwardIt1 first, ForwardIt1 last,
ForwardIt2 s_first, ForwardIt2 s_last,
BinaryPred p );
dcl|num=4|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class BinaryPred >
ForwardIt1 search( ExecutionPolicy&& policy,
ForwardIt1 first, ForwardIt1 last,
ForwardIt2 s_first, ForwardIt2 s_last,
BinaryPred p );
|
template< class ForwardIt, class Searcher >
ForwardIt search( ForwardIt first, ForwardIt last,
const Searcher& searcher );
```

@1-4@ Searches for the first occurrence of the sequence of elements [s_first, s_last) in the range [first, last).
:@1@ Elements are compared using `1=operator==`.
:@3@ Elements are compared using the given binary predicate `p`.
:@2,4@ Same as , but executed according to `policy`.
:@@
5. Searches the range [first, last) for the pattern specified in the constructor of `searcher`.
rrev|since=c++17|
The standard library provides the following searchers:


| cpp/utility/functional/dsc default_searcher | (see dedicated page) |
| cpp/utility/functional/dsc boyer_moore_searcher | (see dedicated page) |
| cpp/utility/functional/dsc boyer_moore_horspool_searcher | (see dedicated page) |


## Parameters


### Parameters

- `[s_first, s_last)` - 
- `policy` - execution policy
- `searcher` - the searcher encapsulating the search algorithm and the pattern to look for

**Type requirements:**

- `ForwardIt1, ForwardIt2`
- `BinaryPred`

## Return value

@1-4@ Iterator to the beginning of first occurrence of the sequence [s_first, s_last) in the range [first, last). If no such occurrence is found, `last` is returned.
@@ If [s_first, s_last) is empty, `first` is returned.
5. `searcher(first, last).first`.

## Complexity

@1-4@ Given  as `std::distance(first, last)` and  as `std::distance(s_first, s_last)`:
:@1,2@ At most  comparisons using `1=operator==`.
:@3,4@ At most  applications of the predicate `p`.
5. Depends on `searcher`.

## Exceptions


## Possible implementation

eq impl
|title1=search (1)|ver1=1|1=
template<class ForwardIt1, class ForwardIt2>
constexpr //< since C++20
ForwardIt1 search(ForwardIt1 first, ForwardIt1 last,
ForwardIt2 s_first, ForwardIt2 s_last)
{
while (true)
{
ForwardIt1 it = first;
for (ForwardIt2 s_it = s_first; ; ++it, ++s_it)
{
if (s_it == s_last)
return first;
if (it == last)
return last;
if (!(*it == *s_it))
break;
}
++first;
}
}
|title2=search (3)|ver2=3|2=
template<class ForwardIt1, class ForwardIt2, class BinaryPred>
constexpr //< since C++20
ForwardIt1 search(ForwardIt1 first, ForwardIt1 last,
ForwardIt2 s_first, ForwardIt2 s_last, BinaryPred p)
{
while (true)
{
ForwardIt1 it = first;
for (ForwardIt2 s_it = s_first; ; ++it, ++s_it)
{
if (s_it == s_last)
return first;
if (it == last)
return last;
if (!p(*it, *s_it))
break;
}
++first;
}
}

## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <string_view>
#include <vector>

using namespace std::literals;

bool contains(const auto& cont, std::string_view s)
{
    // str.find() (or str.contains(), since C++23) can be used as well
    return std::search(cont.begin(), cont.end(), s.begin(), s.end()) != cont.end();
}

int main()
{
    const auto str{"why waste time learning, when ignorance is instantaneous?"sv};
    assert(contains(str, "learning"));
    assert(not contains(str, "lemming"));

    const std::vector vec(str.begin(), str.end());
    assert(contains(vec, "learning"));
    assert(not contains(vec, "leaning"));

    // The C++17 overload with searchers demo:
    constexpr auto quote
    {
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed "
        "do eiusmod tempor incididunt ut labore et dolore magna aliqua"sv
    };

    for (const auto word : {"pisci"sv, "Pisci"sv})
    {
        std::cout << "The string " << std::quoted(word) << ' ';
        const std::boyer_moore_searcher searcher(word.begin(), word.end());
        const auto it = std::search(quote.begin(), quote.end(), searcher);
        if (it == quote.end())
            std::cout << "not found\n";
        else
            std::cout << "found at offset " << std::distance(quote.begin(), it) << '\n';
    }
}
```


**Output:**
```
The string "pisci" found at offset 43
The string "Pisci" not found
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2150 | C++98 | the condition of “sequence occurence” was incorrect | corrected |


## See also


| cpp/algorithm/dsc find_end | (see dedicated page) |
| cpp/algorithm/dsc includes | (see dedicated page) |
| cpp/algorithm/dsc equal | (see dedicated page) |
| cpp/algorithm/dsc find | (see dedicated page) |
| cpp/algorithm/dsc lexicographical_compare | (see dedicated page) |
| cpp/algorithm/dsc mismatch | (see dedicated page) |
| cpp/algorithm/dsc search_n | (see dedicated page) |
| cpp/utility/functional/dsc default_searcher | (see dedicated page) |
| cpp/utility/functional/dsc boyer_moore_searcher | (see dedicated page) |
| cpp/utility/functional/dsc boyer_moore_horspool_searcher | (see dedicated page) |
| cpp/algorithm/ranges/dsc search | (see dedicated page) |

