---
title: std::random_shuffle
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/random_shuffle
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|until=c++17|deprecated=c++14|
template< class RandomIt >
void random_shuffle( RandomIt first, RandomIt last );
dcl rev multi|num=2|until1=c++11|dcl1=
template< class RandomIt, class RandomFunc >
void random_shuffle( RandomIt first, RandomIt last, RandomFunc& r );
|notes2=|dcl2=
template< class RandomIt, class RandomFunc >
void random_shuffle( RandomIt first, RandomIt last, RandomFunc&& r );
dcla|num=3|since=c++11|
template< class RandomIt, class URBG >
void shuffle( RandomIt first, RandomIt last, URBG&& g );
```

Reorders the elements in the given range [first, last) such that each possible permutation of those elements has equal probability of appearance.
1. The source of randomness is implementation-defined, but the function `std::rand` is often used.
2. The source of randomness is the function object `r`.
@@ If any of the following conditions is satisfied, the behavior is undefined:
* The return type of `r` is not convertible to `std::iterator_traits<RandomIt>::difference_type`.
* Given a positive value `n` of type `std::iterator_traits<RandomIt>::difference_type`, the result of `r(n)` is not a randomly chosen value in the interval [0, n).
3. The source of randomness is the object `g`.
@@ Given the type `T` as `std::remove_reference_t<URBG>`, if any of the following conditions is satisfied, the behavior is undefined:
* `T` is not a *UniformRandomBitGenerator*.
rrev|until=c++20|
* `T::result_type` is not convertible to `std::iterator_traits<RandomIt>::difference_type`.
If <sup>(until C++11)</sup> the type of `*first` is not *Swappable*<sup>(since C++11)</sup> `RandomIt` is not *ValueSwappable*, the behavior is undefined.

## Parameters


### Parameters

- `r` - function object returning a randomly chosen value
- `g` - generator object returning a randomly chosen value

**Type requirements:**

- `RandomIt`

## Complexity

Exactly `std::distance(first, last) - 1` swaps.

## Possible implementation

See also the implementations in [https://github.com/gcc-mirror/gcc/blob/d9375e490072d1aae73a93949aa158fcd2a27018/libstdc%2B%2B-v3/include/bits/stl_algo.h#L4551 libstdc++] and [https://github.com/llvm-mirror/libcxx/blob/a12cb9d211019d99b5875b6d8034617cbc24c2cc/include/algorithm#L3066 libc++].
eq impl
|title1=random_shuffle (1)|ver1=1|1=
template<class RandomIt>
void random_shuffle(RandomIt first, RandomIt last)
{
typedef typename std::iterator_traits<RandomIt>::difference_type diff_t;
for (diff_t i = last - first - 1; i > 0; --i)
{
using std::swap;
swap(first[i], first[std::rand() % (i + 1)]);
// rand() % (i + 1) is not actually correct, because the generated number is
// not uniformly distributed for most values of i. The correct code would be
// a variation of the C++11 std::uniform_int_distribution implementation.
}
}
|title2=random_shuffle (2)|ver2=2|2=
template<class RandomIt, class RandomFunc>
void random_shuffle(RandomIt first, RandomIt last, RandomFunc&& r)
{
typedef typename std::iterator_traits<RandomIt>::difference_type diff_t;
for (diff_t i = last - first - 1; i > 0; --i)
{
using std::swap;
swap(first[i], first[r(i + 1)]);
}
}
|title3=shuffle (3)|ver3=3|3=
template<class RandomIt, class URBG>
void shuffle(RandomIt first, RandomIt last, URBG&& g)
{
typedef typename std::iterator_traits<RandomIt>::difference_type diff_t;
typedef std::uniform_int_distribution<diff_t> distr_t;
typedef typename distr_t::param_type param_t;
distr_t D;
for (diff_t i = last - first - 1; i > 0; --i)
{
using std::swap;
swap(first[i], first[D(g, param_t(0, i))]);
}
}

## Notes

Note that the implementation is not dictated by the standard, so even if you use exactly the same `RandomFunc` or `URBG` (Uniform Random Number Generator) you may get different results with different standard library implementations.
The reason for removing `std::random_shuffle` in C++17 is that the iterator-only version usually depends on `std::rand`, which is now also discussed for deprecation. (`std::rand` should be replaced with the classes of the  header, as `std::rand` is ''considered harmful''.) In addition, the iterator-only `std::random_shuffle` version usually depends on a global state. The `std::shuffle`'s shuffle algorithm is the preferred replacement, as it uses a `URBG` as its 3rd parameter.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <random>
#include <vector>

int main()
{
    std::vector<int> v{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    std::random_device rd;
    std::mt19937 g(rd());

    std::shuffle(v.begin(), v.end(), g);

    std::copy(v.begin(), v.end(), std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';
}
```


**Output:**
```
8 6 10 4 2 3 7 1 9 5
```


## Defect reports


## See also


| cpp/algorithm/dsc next_permutation | (see dedicated page) |
| cpp/algorithm/dsc prev_permutation | (see dedicated page) |
| cpp/algorithm/ranges/dsc shuffle | (see dedicated page) |

