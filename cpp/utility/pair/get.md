---
title: std::get(std::pair)
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/pair/get
---


# getpetty|(std::pair)


```cpp
**Header:** `<`utility`>`
dcla|anchor=no|num=1|since=c++11|constexpr=c++14|
template< std::size_t I, class T1, class T2 >
typename std::tuple_element<I, std::pair<T1,T2> >::type&
get( std::pair<T1, T2>& p ) noexcept;
dcla|anchor=no|num=2|since=c++11|constexpr=c++14|
template< std::size_t I, class T1, class T2 >
const typename std::tuple_element<I, std::pair<T1,T2> >::type&
get( const std::pair<T1,T2>& p ) noexcept;
dcla|anchor=no|num=3|since=c++11|constexpr=c++14|
template< std::size_t I, class T1, class T2 >
typename std::tuple_element<I, std::pair<T1,T2> >::type&&
get( std::pair<T1,T2>&& p ) noexcept;
dcla|anchor=no|num=4|since=c++11|constexpr=c++14|
template< std::size_t I, class T1, class T2 >
const typename std::tuple_element<I, std::pair<T1,T2> >::type&&
get( const std::pair<T1,T2>&& p ) noexcept;
dcl|num=5|since=c++14|
template< class T, class U >
constexpr T& get( std::pair<T, U>& p ) noexcept;
dcl|num=6|since=c++14|
template< class T, class U >
constexpr const T& get( const std::pair<T, U>& p ) noexcept;
dcl|num=7|since=c++14|
template< class T, class U >
constexpr T&& get( std::pair<T, U>&& p ) noexcept;
dcl|num=8|since=c++14|
template< class T, class U >
constexpr const T&& get( const std::pair<T, U>&& p ) noexcept;
dcl|num=9|since=c++14|
template< class T, class U >
constexpr T& get( std::pair<U, T>& p ) noexcept;
dcl|num=10|since=c++14|
template< class T, class U >
constexpr const T& get( const std::pair<U, T>& p ) noexcept;
dcl|num=11|since=c++14|
template< class T, class U >
constexpr T&& get( std::pair<U, T>&& p ) noexcept;
dcl|num=12|since=c++14|
template< class T, class U >
constexpr const T&& get( const std::pair<U, T>&& p ) noexcept;
```

Extracts an element from the pair using  interface.
@1-4@ The index-based overloads fail to compile if the index `I` is neither `0` nor `1`.
@5-12@ The type-based overloads fail to compile if the types `T` and `U` are the same.

## Parameters


### Parameters

- `p` - pair whose contents to extract

## Return value

@1-4@ Returns a reference to `p.first` if `1=I == 0` and a reference to `p.second` if `1=I == 1`.
@5-8@ Returns a reference to `p.first`.
@9-12@ Returns a reference to `p.second`.

## Example


### Example

```cpp
#include <iostream>
#include <utility>

int main()
{
    auto p = std::make_pair(1, 3.14);
    std::cout << '(' << std::get<0>(p) << ", " << std::get<1>(p) << ")\n";
    std::cout << '(' << std::get<int>(p) << ", " << std::get<double>(p) << ")\n";
}
```


**Output:**
```
(1, 3.14)
(1, 3.14)
```


## Defect reports


## See also


| cpp/language/dsc structured binding | (see dedicated page) |
| cpp/utility/tuple/dsc get | (see dedicated page) |
| cpp/container/array/dsc get | (see dedicated page) |
| cpp/utility/variant/dsc get | (see dedicated page) |
| cpp/ranges/subrange/dsc get | (see dedicated page) |
| cpp/numeric/complex/dsc get | (see dedicated page) |

