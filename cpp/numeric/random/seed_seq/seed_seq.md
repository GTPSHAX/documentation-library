---
title: std::seed_seq::seed_seq
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/seed_seq/seed_seq
---


```cpp
dcla|num=1|since=c++11|
seed_seq() noexcept;
dcl|num=2|since=c++11|1=
seed_seq( const seed_seq& ) = delete;
dcl|num=3|since=c++11|
template< class InputIt >
seed_seq( InputIt begin, InputIt end );
dcla|num=4|since=c++11|
template< class T >
seed_seq( std::initializer_list<T> il );
```

1. The default constructor. After construction,  is empty.
2. The copy constructor is deleted: `std::seed_seq` is not copyable.
3. Constructs a `std::seed_seq` with the values in the range [begin, end). Equivalent to default-initializing  followed by , where mathjax-or|1=\(\scriptsize \mathrm{modseed}(x)=x \mod 2^{32} \)|2=mod_seed(x)=x mod 2.
@@ If `std::iterator_traits<InputIt>::value_type` is not an integer type, the program is ill-formed.
@@ If `InputIt` does not satisfy the requirements of *InputIterator*, the behavior is undefined.
4. Equivalent to `seed_seq(il.begin(), il.end())`. This constructor enables list-initialization from the list of seed values.
@@ .

## Parameters


### Parameters

- `begin, end` - the pair of iterators denoting the initial seed sequence
- `il` - the initial seed sequence

## Example


### Example

```cpp
#include <iterator>
#include <random>
#include <sstream>

int main()
{
    std::seed_seq s1; // default-constructible
    std::seed_seq s2{1, 2, 3}; // can use list-initialization
    std::seed_seq s3 = {-1, 0, 1}; // another form of list-initialization
    int a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    std::seed_seq s4(a, a + 10); // can use iterators
    std::istringstream buf("1 2 3 4 5"); 
    std::istream_iterator<int> beg(buf), end;
    std::seed_seq s5(beg, end); // even stream input iterators
}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2180 | C++11 | all constructors were non-throwing | only overload vl |

