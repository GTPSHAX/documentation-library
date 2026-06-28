---
title: operators (std::unique_ptr)
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/unique_ptr/operator_cmp
---


# 1=operator==,!=,<,<=,>,>=,<=><small>(std::unique_ptr)</small>


```cpp
**Header:** `<`memory`>`
dcla|num=1|since=c++11|constexpr=c++23|1=
template< class T1, class D1, class T2, class D2 >
bool operator==( const unique_ptr<T1, D1>& x, const unique_ptr<T2, D2>& y );
dcl|num=2|since=c++11|until=c++20|1=
template< class T1, class D1, class T2, class D2 >
bool operator!=( const unique_ptr<T1, D1>& x, const unique_ptr<T2, D2>& y );
dcla|num=3|since=c++11|constexpr=c++26|1=
template< class T1, class D1, class T2, class D2 >
bool operator<( const unique_ptr<T1, D1>& x, const unique_ptr<T2, D2>& y );
dcla|num=4|since=c++11|constexpr=c++26|1=
template< class T1, class D1, class T2, class D2 >
bool operator<=( const unique_ptr<T1, D1>& x, const unique_ptr<T2, D2>& y );
dcla|num=5|since=c++11|constexpr=c++26|1=
template< class T1, class D1, class T2, class D2 >
bool operator>( const unique_ptr<T1, D1>& x, const unique_ptr<T2, D2>& y );
dcla|num=6|since=c++11|constexpr=c++26|1=
template< class T1, class D1, class T2, class D2 >
bool operator>=( const unique_ptr<T1, D1>& x, const unique_ptr<T2, D2>& y );
dcla|num=7|since=c++20|constexpr=c++26|1=
template< class T1, class D1, class T2, class D2 >
requires std::three_way_comparable_with<
typename unique_ptr<T1, D1>::pointer,
typename unique_ptr<T2, D2>::pointer>
std::compare_three_way_result_t<typename unique_ptr<T1, D1>::pointer,
typename unique_ptr<T2, D2>::pointer>
operator<=>( const unique_ptr<T1, D1>& x, const unique_ptr<T2, D2>& y );
dcla|num=8|since=c++11|constexpr=c++23|1=
template< class T, class D >
bool operator==( const unique_ptr<T, D>& x, std::nullptr_t ) noexcept;
dcl|num=9|since=c++11|until=c++20|1=
template< class T, class D >
bool operator==( std::nullptr_t, const unique_ptr<T, D>& x ) noexcept;
dcl|num=10|since=c++11|until=c++20|1=
template< class T, class D >
bool operator!=( const unique_ptr<T, D>& x, std::nullptr_t ) noexcept;
dcl|num=11|since=c++11|until=c++20|1=
template< class T, class D >
bool operator!=( std::nullptr_t, const unique_ptr<T, D>& x ) noexcept;
dcla|num=12|since=c++11|constexpr=c++23|1=
template< class T, class D >
bool operator<( const unique_ptr<T, D>& x, std::nullptr_t );
dcla|num=13|since=c++11|constexpr=c++23|1=
template< class T, class D >
bool operator<( std::nullptr_t, const unique_ptr<T, D>& y );
dcla|num=14|since=c++11|constexpr=c++23|1=
template< class T, class D >
bool operator<=( const unique_ptr<T, D>& x, std::nullptr_t );
dcla|num=15|since=c++11|constexpr=c++23|1=
template< class T, class D >
bool operator<=( std::nullptr_t, const unique_ptr<T, D>& y );
dcla|num=16|since=c++11|constexpr=c++23|1=
template< class T, class D >
bool operator>( const unique_ptr<T, D>& x, std::nullptr_t );
dcla|num=17|since=c++11|constexpr=c++23|1=
template< class T, class D >
bool operator>( std::nullptr_t, const unique_ptr<T, D>& y );
dcla|num=18|since=c++11|constexpr=c++23|1=
template< class T, class D >
bool operator>=( const unique_ptr<T, D>& x, std::nullptr_t );
dcla|num=19|since=c++11|constexpr=c++23|1=
template< class T, class D >
bool operator>=( std::nullptr_t, const unique_ptr<T, D>& y );
dcla|num=20|since=c++20|constexpr=c++23|1=
template< class T, class D >
requires std::three_way_comparable<typename unique_ptr<T, D>::pointer>
std::compare_three_way_result_t<typename unique_ptr<T, D>::pointer>
operator<=>( const unique_ptr<T, D>& x, std::nullptr_t );
```

Compares the pointer values of two `unique_ptr`s, or a `unique_ptr` and `nullptr`.
@1-7@ Compares two `unique_ptr`s.
@8-20@ Compares a `unique_ptr` and `nullptr`.
rrev|since=c++20|

## Parameters


### Parameters

- `x, y` - `unique_ptr`s to compare

## Return value

1. `x.get()
2. `x.get() !
3. `std::less<CT>()(x.get(), y.get())`, where `CT` is `std::common_type<unique_ptr<T1, D1>::pointer, unique_ptr<T2, D2>::pointer>::type`.
4. `!(y < x)`
5. `y < x`
6. `!(x < y)`
7. }
@8,9@ `!x`
@10,11@ `(bool)x`
12. `std::less<unique_ptr<T,D>::pointer>()(x.get(), nullptr)`
13. `std::less<unique_ptr<T,D>::pointer>()(nullptr, y.get())`
14. `!(nullptr < x)`
15. `!(y < nullptr)`
16. `nullptr < x`
17. `y < nullptr`
18. `!(x < nullptr)`
19. `!(nullptr < y)`
20. }

## Example


### Example

```cpp
#include <iostream>
#include <memory>

int main()
{
    std::unique_ptr<int> p1(new int(42));
    std::unique_ptr<int> p2(new int(42));

    std::cout << std::boolalpha
        << "(p1 == p1)       : " << (p1 == p1) << '\n'
        << "(p1 <=> p1) == 0 : " << ((p1 <=> p1) == 0) << '\n' // Since C++20

    // p1 and p2 point to different memory locations, so p1 != p2
        << "(p1 == p2)       : " << (p1 == p2) << '\n'
        << "(p1 < p2)        : " << (p1 < p2) << '\n'
        << "(p1 <=> p2) < 0  : " << ((p1 <=> p2) < 0) << '\n'   // Since C++20
        << "(p1 <=> p2) == 0 : " << ((p1 <=> p2) == 0) << '\n'; // Since C++20
}
```


**Output:**
```
(p1 == p1)       : true
(p1 <=> p1) == 0 : true
(p1 == p2)       : false
(p1 < p2)        : true
(p1 <=> p2) < 0  : true
(p1 <=> p2) == 0 : false
```


## Defect reports


## See also


| cpp/memory/unique_ptr/dsc get | (see dedicated page) |

