---
title: deduction guides for std::priority_queue
type: Containers
source: https://en.cppreference.com/w/cpp/container/priority_queue/deduction_guides
---


# deduction guides for tt|std::priority_queue


```cpp
**Header:** `<`queue`>`
dcl|num=1|since=c++17|1=
template< class Comp, class Container >
priority_queue( Comp, Container )
-> priority_queue<typename Container::value_type, Container, Comp>;
dcl|num=2|since=c++17|1=
template< class InputIt,
class Comp = std::less</*iter-val-t*/<InputIt>>,
class Container = std::vector</*iter-val-t*/<InputIt> >
priority_queue( InputIt, InputIt, Comp = Comp(), Container = Container() )
-> priority_queue</*iter-val-t*/<InputIt>, Container, Comp>;
dcla|num=3|since=c++17|1=
template< class Comp, class Container, class Alloc >
priority_queue( Comp, Container, Alloc )
-> priority_queue<typename Container::value_type, Container, Comp>;
dcla|num=4|since=c++17|
template< class InputIt, class Alloc >
priority_queue( InputIt, InputIt, Alloc )
-> priority_queue</*iter-val-t*/<InputIt>,
std::vector</*iter-val-t*/<InputIt>, Alloc>,
std::less</*iter-val-t*/<InputIt>>>;
dcl|num=5|since=c++17|
template< class InputIt, class Comp, class Alloc >
priority_queue( InputIt, InputIt, Comp, Alloc )
-> priority_queue</*iter-val-t*/<InputIt>,
std::vector</*iter-val-t*/<InputIt>, Alloc>, Comp>;
dcl|num=6|since=c++17|
template< class InputIt, class Comp, class Container, class Alloc >
priority_queue( InputIt, InputIt, Comp, Container, Alloc )
-> priority_queue<typename Container::value_type, Container, Comp>;
dcla|num=7|since=c++23|1=
template< ranges::input_range R,
class Comp = std::less<ranges::range_value_t<R>> >
priority_queue( std::from_range_t, R&&, Comp = Comp() )
-> priority_queue<ranges::range_value_t<R>,
std::vector<ranges::range_value_t<R>>, Comp>;
dcl|num=8|since=c++23|1=
template< ranges::input_range R, class Comp, class Alloc >
priority_queue( std::from_range_t, R&&, Comp, Alloc )
-> priority_queue<ranges::range_value_t<R>,
std::vector<ranges::range_value_t<R>, Alloc>, Comp>;
dcl|num=9|since=c++23|1=
template< ranges::input_range R, class Alloc >
priority_queue( std::from_range_t, R&&, Alloc )
-> priority_queue<ranges::range_value_t<R>,
std::vector<ranges::range_value_t<R>, Alloc>>;
```

The following deduction guides are provided for `std::priority_queue`:
@1-6@ Allow deduction from underlying container type and from an iterator range.
@7-9@ Allow deduction from a `cpp/ranges/from_range|std::from_range_t` tag and an `std::ranges::input_range|input_range`.
cpp/enable_if|plural=yes|
* `InputIt` satisfies *InputIterator*,
* `Comp` does not satisfy *Allocator*,
* `Container` does not satisfy *Allocator*,
* <sup>(since C++23)</sup> for overloads  `Alloc` satisfies *Allocator*, and
* for overloads , `std::uses_allocator_v<Container, Alloc>` is `true`.

## Notes


## Example


### Example

```cpp
#include <functional>
#include <iostream>
#include <queue>
#include <vector>

int main()
{
    const std::vector<int> v = {1, 2, 3, 4};
    std::priority_queue pq1{std::greater<int>{}, v}; // deduces std::priority_queue<
                                                     //     int, std::vector<int>,
                                                     //     std::greater<int>>
    for (; !pq1.empty(); pq1.pop())
        std::cout << pq1.top() << ' ';
    std::cout << '\n';

    std::priority_queue pq2{v.begin(), v.end()}; // deduces std::priority_queue<int>

    for (; !pq2.empty(); pq2.pop())
        std::cout << pq2.top() << ' ';
    std::cout << '\n';
}
```


**Output:**
```
1 2 3 4
4 3 2 1
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-3506 | C++17 | deduction guides from iterator and allocator were missing | added, vl |

