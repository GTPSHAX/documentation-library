---
title: std::vector::vector
type: Containers
source: https://en.cppreference.com/w/cpp/container/vector/vector
---


```cpp
dcl rev multi|num=1|since1=c++11|until1=c++17|dcl1=
vector() : vector(Allocator()) {}
|constexpr2=c++20|dcl2=
vector() noexcept(noexcept(Allocator())) : vector(Allocator()) {}
dcl rev multi|num=2|until1=c++11|dcl1=
explicit vector( const Allocator& alloc = Allocator() );
|noexcept2=c++17|constexpr2=c++20|dcl2=
explicit vector( const Allocator& alloc );
dcl|num=3|since=c++11|1=
explicit vector( size_type count,
const Allocator& alloc = Allocator() );
dcl rev multi|num=4|until1=c++11|dcl1=
explicit vector( size_type count, const T& value = T(),
const Allocator& alloc = Allocator() );
|constexpr2=c++20|dcl2=
vector( size_type count, const T& value,
const Allocator& alloc = Allocator() );
dcla|num=5|constexpr=c++20|1=
template< class InputIt >
vector( InputIt first, InputIt last,
const Allocator& alloc = Allocator() );
dcla|num=6|since=c++23|1=
template< container-compatible-range<T> R >
constexpr vector( std::from_range_t, R&& rg,
const Allocator& alloc = Allocator() );
dcla|num=7|constexpr=c++20|
vector( const vector& other );
dcla|num=8|since=c++11|noexcept=c++17|constexpr=c++20|
vector( vector&& other );
dcl rev multi|num=9|since1=c++11|constexpr1=c++20|until1=c++23|dcl1=
vector( const vector& other, const Allocator& alloc );
|dcl2=
constexpr vector( const vector& other,
const std::type_identity_t<Allocator>& alloc );
dcl rev multi|num=10|since1=c++11|constexpr1=c++20|until1=c++23|dcl1=
vector( vector&& other, const Allocator& alloc );
|dcl2=
constexpr vector( vector&& other,
const std::type_identity_t<Allocator>& alloc );
dcl|num=11|since=c++11|1=
vector( std::initializer_list<T> init,
const Allocator& alloc = Allocator() );
```

Constructs a new `vector` from a variety of data sources, optionally using a user supplied allocator `alloc`.
1. The default constructor since C++11. Constructs an empty `vector` with a default-constructed allocator.
@@ If `Allocator` is not *DefaultConstructible*, the behavior is undefined.
2. The default constructor until C++11. Constructs an empty `vector` with the given allocator `alloc`.
3. Constructs a `vector` with `count` default-inserted objects of `T`. No copies are made.
@@ If `T` is not *DefaultInsertable* into `std::vector<T>`, the behavior is undefined.
4. Constructs a `vector` with `count` copies of elements with value `value`.
rrev|since=c++11|
If `T` is not *CopyInsertable* into `std::vector<T>`, the behavior is undefined.
5. Constructs a `vector` with the contents of the range [first, last). Each iterator in [first, last) is dereferenced exactly once.
rev|until=c++11|
If `InputIt` does not satisfy the requirements of *InputIterator*, overload  is called instead with arguments `static_cast<size_type>(first)`, `last` and `alloc`.
rev|since=c++11|
.
If any of the following conditions is satisfied, the behavior is undefined:
* `T` is not *EmplaceConstructible* into `std::vector<T>` from `*first`.
* `Iter` does not satisfy the requirements of *ForwardIterator*, and `T` is not *MoveInsertable* into `std::vector<T>`.
6. Constructs a `vector` with the contents of the range `rg`. Each iterator in `rg` is dereferenced exactly once.
@@ If any of the following conditions is satisfied, the behavior is undefined:
* `T` is not *EmplaceConstructible* into `std::vector<T>` from `*ranges::begin(rg)`.
* `R` models neither  nor , and `T` is not *MoveInsertable* into `std::vector<T>`.
@7-10@ Constructs a `vector` with the contents of `other`.
:@7@ The copy constructor.
rrev|since=c++11|
The allocator is obtained as if by calling `std::allocator_traits<Allocator>::select_on_container_copy_construction(alloc)` where `alloc` is the allocator of `other`.
:@8@ The move constructor. The allocator is obtained by move construction from `other.get_allocator()`.
:@9@ Same as the copy constructor, except that `alloc` is used as the allocator.
:@@ If `T` is not *CopyInsertable* into `std::vector<T>`, the behavior is undefined.
:@10@ Same as the move constructor, except that `alloc` is used as the allocator.
:@@ If `T` is not *MoveInsertable* into `std::vector<T>`, the behavior is undefined.
11. Equivalent to `vector(il.begin(), il.end(), alloc)`.

## Parameters


### Parameters

- `alloc` - allocator to use for all memory allocations of this container
- `count` - the size of the container
- `value` - the value to initialize elements of the container with
- `other` - another container to be used as source to initialize the elements of the container with
- `init` - initializer list to initialize the elements of the container with
- `rg` - a container compatible range

## Complexity

@1,2@ Constant.
@3,4@ Linear in `count`.
5. Given `std::distance(first, last)` as $N$:
* If `first` and `last` are both forward, bidirectional or random-access iterators,
:* The copy constructor of `T` is only called $N$ times, and
:* No reallocation occurs.
* Otherwise (`first` and `last` are just input iterators),
:* The copy constructor of `T` is called $O(N)$ times, and
:* Reallocation occurs $O(log N)$ times.
6. Given `ranges::distance(rg)` as $N$:
* If `R` models `ranges::forward_range` or `ranges::sized_range`,
:* Initializes exactly $N$ elements from the result of dereferencing successive iterators of `rg`, and
:* No reallocation occurs.
* Otherwise (`R` models input range),
:* The copy or move constructor of `T` is called $O(N)$ times, and
:* Reallocation occurs $O(log N)$ times.
7. Linear in `other.size()`.
8. Constant.
9. Linear in `other.size()`.
10. Linear in `other.size()` if `1=alloc != other.get_allocator()`, otherwise constant.
11. Linear in `init.size()`.

## Exceptions

Calls to `Allocator::allocate` may throw.

## Notes


## Example


### Example

```cpp
#include <iostream>
#include <string>
#include <vector>

template<typename T>
std::ostream& operator<<(std::ostream& s, const std::vector<T>& v)
{
    s.put('{');
    for (char comma[]{'\0', ' ', '\0'}; const auto& e : v)
        s << comma << e, comma[0] = ',';
    return s << "}\n";
}

int main()
{
    // C++11 initializer list syntax:
    std::vector<std::string> words1{"the", "frogurt", "is", "also", "cursed"};
    std::cout << "1: " << words1;

    // words2 == words1
    std::vector<std::string> words2(words1.begin(), words1.end());
    std::cout << "2: " << words2;

    // words3 == words1
    std::vector<std::string> words3(words1);
    std::cout << "3: " << words3;

    // words4 is {"Mo", "Mo", "Mo", "Mo", "Mo"}
    std::vector<std::string> words4(5, "Mo");
    std::cout << "4: " << words4;

    const auto rg = {"cat", "cow", "crow"};
#ifdef __cpp_lib_containers_ranges
    std::vector<std::string> words5(std::from_range, rg); // overload (6)
#else
    std::vector<std::string> words5(rg.begin(), rg.end()); // overload (5)
#endif
    std::cout << "5: " << words5;
}
```


**Output:**
```
1: {the, frogurt, is, also, cursed}
2: {the, frogurt, is, also, cursed}
3: {the, frogurt, is, also, cursed}
4: {Mo, Mo, Mo, Mo, Mo}
5: {cat, cow, crow}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2193 | C++11 | the default constructor was explicit | made non-explicit |


## See also


| cpp/container/dsc assign|vector | (see dedicated page) |
| cpp/container/dsc operator{{= | (see dedicated page) |

