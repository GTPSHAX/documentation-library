---
title: std::priority_queue::priority_queue
type: Containers
source: https://en.cppreference.com/w/cpp/container/priority_queue/priority_queue
---


```cpp
dcl|num=1|since=c++11|
priority_queue() : priority_queue(Compare(), Container()) {}
dcl|num=2|since=c++11|
explicit priority_queue( const Compare& compare )
: priority_queue(compare, Container()) {}
dcl rev multi|num=3
|dcl1=
explicit priority_queue( const Compare& compare = Compare(),
const Container& cont = Container() );
|since2=c++11|dcl2=
priority_queue( const Compare& compare, const Container& cont );
dcl|num=4|since=c++11|
priority_queue( const Compare& compare, Container&& cont );
dcl|num=5|
priority_queue( const priority_queue& other );
dcl|num=6|since=c++11|
priority_queue( priority_queue&& other );
dcl|num=7|since=c++11|1=
template< class InputIt >
priority_queue( InputIt first, InputIt last,
const Compare& compare = Compare() );
dcl rev multi|num=8
|dcl1=
template< class InputIt >
priority_queue( InputIt first, InputIt last,
const Compare& compare = Compare(),
const Container& cont = Container() );
|since2=c++11|dcl2=
template< class InputIt >
priority_queue( InputIt first, InputIt last,
const Compare& compare, const Container& cont );
dcl|num=9|since=c++11|
template< class InputIt >
priority_queue( InputIt first, InputIt last,
const Compare& compare, Container&& cont );
dcl|num=10|since=c++11|
template< class Alloc >
explicit priority_queue( const Alloc& alloc );
dcl|num=11|since=c++11|
template< class Alloc >
priority_queue( const Compare& compare, const Alloc& alloc );
dcl|num=12|since=c++11|
template< class Alloc >
priority_queue( const Compare& compare, const Container& cont,
const Alloc& alloc );
dcl|num=13|since=c++11|
template< class Alloc >
priority_queue( const Compare& compare, Container&& cont,
const Alloc& alloc );
dcl|num=14|since=c++11|
template< class Alloc >
priority_queue( const priority_queue& other, const Alloc& alloc );
dcl|num=15|since=c++11|
template< class Alloc >
priority_queue( priority_queue&& other, const Alloc& alloc );
dcl|num=16|since=c++11|
template< class InputIt, class Alloc >
priority_queue( InputIt first, InputIt last, const Alloc& alloc );
dcl|num=17|since=c++11|
template< class InputIt, class Alloc >
priority_queue( InputIt first, InputIt last, const Compare& compare,
const Alloc& alloc );
dcl|num=18|since=c++11|
template< class InputIt, class Alloc >
priority_queue( InputIt first, InputIt last, const Compare& compare,
const Container& cont, const Alloc& alloc );
dcl|num=19|since=c++11|
template< class InputIt, class Alloc >
priority_queue( InputIt first, InputIt last, const Compare& compare,
Container&& cont, const Alloc& alloc );
dcla|num=20|since=c++23|1=
template< container-compatible-range<T> R >
priority_queue( std::from_range_t, R&& rg,
const Compare& compare = Compare() );
dcl|num=21|since=c++23|
template< container-compatible-range<T> R, class Alloc >
priority_queue( std::from_range_t, R&& rg,
const Compare& compare, const Alloc& alloc );
dcl|num=22|since=c++23|
template< container-compatible-range<T> R, class Alloc >
priority_queue( std::from_range_t, R&& rg, const Alloc& alloc );
```

Constructs new underlying container of the container adaptor from a variety of data sources.
1. Default constructor. Value-initializes the comparator and the underlying container.
2. Copy-constructs the comparison functor `comp` with the contents of `compare`. Value-initializes the underlying container `c`.
3. Copy-constructs the underlying container `c` with the contents of `cont`. Copy-constructs the comparison functor `comp` with the contents of `compare`. Calls `std::make_heap(c.begin(), c.end(), comp)`. <sup>(until C++11)</sup> This is also the default constructor.
4. Move-constructs the underlying container `c` with `std::move(cont)`. Copy-constructs the comparison functor `comp` with `compare`. Calls `std::make_heap(c.begin(), c.end(), comp)`.
5. Copy constructor. The underlying container is copy-constructed with `other.c`. The comparison functor is copy-constructed with `other.comp`.
6. Move constructor. The underlying container is constructed with `std::move(other.c)`. The comparison functor is constructed with `std::move(other.comp)`.
@7-9@ Iterator-pair constructors. .
7. Constructs `c` as if by `c(first, last)` and `comp` from `compare`. Then calls `std::make_heap(c.begin(), c.end(), comp);`.
8. Copy-constructs `c` from `cont` and `comp` from `compare`. Then calls `c.insert(c.end(), first, last);`, and then calls `std::make_heap(c.begin(), c.end(), comp);`.
9. Move-constructs `c` from `std::move(cont)` and copy-constructs `comp` from `compare`. Then calls `c.insert(c.end(), first, last);`, and then calls `std::make_heap(c.begin(), c.end(), comp);`.
@10-15@ Allocator-extended constructors. .
10. Constructs the underlying container using `alloc` as allocator. Effectively calls `c(alloc)`. `comp` is value-initialized.
11. Constructs the underlying container using `alloc` as allocator. Effectively calls `c(alloc)`. Copy-constructs `comp` from `compare`.
12. Constructs the underlying container with the contents of `cont` and using `alloc` as allocator, as if by `c(cont, alloc)`. Copy-constructs `comp` from `compare`. Then calls `std::make_heap(c.begin(), c.end(), comp)`.
13. Constructs the underlying container with the contents of `cont` using move semantics while using `alloc` as allocator, as if by `c(std::move(cont), alloc)`. Copy-constructs `comp` from `compare`. Then calls `std::make_heap(c.begin(), c.end(), comp)`.
14. Constructs the underlying container with the contents of `other.c` and using `alloc` as allocator. Effectively calls `c(other.c, alloc)`. Copy-constructs `comp` from `other.comp`.
15. Constructs the underlying container with the contents of `other` using move semantics while utilizing `alloc` as allocator. Effectively calls `c(std::move(other.c), alloc)`. Move-constructs `comp` from `other.comp`.
@16-19@ Allocator-extended iterator-pair constructors. Same as , except that `alloc` is used for constructing the underlying container. .
20. Initializes `comp` with `compare` and `c` with `ranges::to<Container>(std::forward<R>(rg))`. Then calls `std::make_heap(c.begin(), c.end(), comp)`.
21. Initializes `comp` with `compare` and `c` with `ranges::to<Container>(std::forward<R>(rg), alloc)`. Then calls `std::make_heap(c.begin(), c.end(), comp)`.
22. Initializes `c` with `ranges::to<Container>(std::forward<R>(rg), alloc)`. Then calls `std::make_heap(c.begin(), c.end(), comp)`.
Note that how an implementation checks whether a type satisfies *InputIterator* is unspecified, except that integral types are required to be rejected.

## Parameters


### Parameters

- `alloc` - allocator to use for all memory allocations of the underlying container
- `other` - another container adaptor to be used as source to initialize the underlying container
- `cont` - container to be used as source to initialize the underlying container
- `compare` - the comparison function object to initialize the underlying comparison functor
- `rg` - a , that is, an  whose elements are convertible to `T`

**Type requirements:**

- `Alloc`
- `Compare`
- `Container`
- `InputIt`

## Complexity

@1,2@ Constant.
@3,5,12@ mathjax-or|\(\scriptsize \mathcal{O}{(N)}\)|O(N) comparisons and mathjax-or|\(\scriptsize \mathcal{O}{(N)}\)|O(N) calls to the constructor of `value_type`, where  is `cont.size()`.
4. mathjax-or|\(\scriptsize \mathcal{O}{(N)}\)|O(N) comparisons, where  is `cont.size()`.
6. Constant.
@7,16,17@ mathjax-or|\(\scriptsize \mathcal{O}{(M)}\)|O(M) comparisons, where  is `std::distance(first, last)`.
@8,18@ mathjax-or|\(\scriptsize \mathcal{O}{(N + M)}\)|O(N + M) comparisons and mathjax-or|\(\scriptsize \mathcal{O}{(N)}\)|O(N) calls to the constructor of `value_type`, where  is `cont.size()` and  is `std::distance(first, last)`.
9. mathjax-or|\(\scriptsize \mathcal{O}{(N + M)}\)|O(N + M) comparisons, where  is `cont.size()` and  is `std::distance(first, last)`.
@10,11@ Constant.
13. mathjax-or|\(\scriptsize \mathcal{O}{(N)}\)|O(N) comparisons, where  is `cont.size()`.
14. Linear in size of `other`.
15. Constant if `Alloc` compares equal to the allocator of `other`. Linear in size of `other` otherwise.
19. mathjax-or|\(\scriptsize \mathcal{O}{(N + M)}\)|O(N + M) comparisons and possibly mathjax-or|\(\scriptsize \mathcal{O}{(N)}\)|O(N) calls to the constructor of `value_type` (present if `Alloc` does not compare equal to the allocator of `other`), where  is `cont.size()` and  is `std::distance(first, last)`.
20. mathjax-or|\(\scriptsize \mathcal{O}{(N)}\)|O(N) comparisons and mathjax-or|\(\scriptsize \mathcal{O}{(N)}\)|O(N) calls to the constructor of `value_type`, where  is `ranges::distance(rg)`.
@21,22@

## Notes


## Example


### Example

```cpp
#include <complex>
#include <functional>
#include <iostream>
#include <queue>
#include <vector>

int main()
{
    std::priority_queue<int> pq1;
    pq1.push(5);
    std::cout << "pq1.size() = " << pq1.size() << '\n';

    std::priority_queue<int> pq2 {pq1};
    std::cout << "pq2.size() = " << pq2.size() << '\n';

    std::vector<int> vec {3, 1, 4, 1, 5};
    std::priority_queue<int> pq3 {std::less<int>(), vec};
    std::cout << "pq3.size() = " << pq3.size() << '\n';

    for (std::cout << "pq3 : "; !pq3.empty(); pq3.pop())
        std::cout << pq3.top() << ' ';
    std::cout << '\n';

    // Demo With Custom Comparator:

    using my_value_t = std::complex<double>;
    using my_container_t = std::vector<my_value_t>;

    auto my_comp = [](const my_value_t& z1, const my_value_t& z2)
    {
        return z2.real() < z1.real();
    };

    std::priority_queue<my_value_t,
                        my_container_t,
                        decltype(my_comp)> pq4{my_comp};

    using namespace std::complex_literals;
    pq4.push(5.0 + 1i);
    pq4.push(3.0 + 2i);
    pq4.push(7.0 + 3i);

    for (; !pq4.empty(); pq4.pop())
    {
        const auto& z = pq4.top();
        std::cout << "pq4.top() = " << z << '\n';
    }

    // TODO: C++23 range-aware ctors
}
```


**Output:**
```
pq1.size() = 1
pq2.size() = 1
pq3.size() = 5
pq3 : 5 4 3 1 1
pq4.top() = (3,2)
pq4.top() = (5,1)
pq4.top() = (7,3)
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-3506 | C++11 | allocator-extended iterator-pair constructors were missing | added |
| lwg-3522 | C++11 | constraints on iterator-pair constructors were missing | added |


## See also


| cpp/container/dsc operator{{= | (see dedicated page) |

