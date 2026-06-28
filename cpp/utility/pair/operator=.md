---
title: std::pair::operator=
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/pair/operator=
---


```cpp
dcla|num=1|constexpr=c++20|1=
pair& operator=( const pair& other );
dcl|num=2|since=c++23|1=
constexpr const pair& operator=( const pair& other ) const;
dcla|num=3|constexpr=c++20|1=
template< class U1, class U2 >
pair& operator=( const pair<U1, U2>& other );
dcl|num=4|since=c++23|1=
template< class U1, class U2 >
constexpr const pair& operator=( const pair<U1, U2>& other ) const;
dcla|num=5|since=c++11|constexpr=c++20|1=
pair& operator=( pair&& other ) noexcept(/* see below */);
dcl|num=6
|since=c++23|1=
constexpr const pair& operator=( pair&& other ) const;
dcla|num=7|since=c++11|constexpr=c++20|1=
template< class U1, class U2 >
pair& operator=( pair<U1, U2>&& p );
dcl|num=8
|since=c++23|1=
template< class U1, class U2 >
constexpr const pair& operator=( pair<U1, U2>&& p ) const;
dcl|num=9|since=c++23|1=
template< pair-like P >
constexpr pair& operator=( P&& u );
dcl|num=10|since=c++23|1=
template< pair-like P >
constexpr const pair& operator=( P&& u ) const;
```

Replaces the contents of the pair.
1. Copy assignment operator. Replaces the contents with a copy of the contents of `other`.
rrev multi|until1=c++11|rev1=
The assignment operator is implicitly declared. Using this assignment operator makes the program ill-formed if either `T1` or `T2` is a const-qualified type, or a reference type, or a class type with an inaccessible copy assignment operator, or an array type of such class.
|rev2=
This overload is defined as deleted if either `std::is_copy_assignable<T1>::value` or `std::is_copy_assignable<T2>::value` is `false`.
2. Copy assignment operator for const-qualified operand.
@@ .
3. Assigns `other.first` to `first` and `other.second` to `second`.
rrev|since=c++11|
.
4. Assigns `other.first` to `first` and `other.second` to `second`.
@@ .
5. Move assignment operator. Replaces the contents with those of `other` using move semantics.
@@ .
6. Move assignment operator for const-qualified operand.
@@ .
7. Assigns `std::forward<U1>(p.first)` to `first` and `std::forward<U2>(p.second)` to `second`.
@@ .
8. Assigns `std::forward<U1>(p.first)` to `first` and `std::forward<U2>(p.second)` to `second`.
@@ .
9. Assigns `std::get<0>(std::forward<P>(u))` to `first` and `std::get<1>(std::forward<P>(u))` to `second`.
@@ cpp/enable if|
* `std::same_as<std::remove_cvref_t<P>, std::pair>` is `false`,
* `std::remove_cvref_t<P>` is not a specialization of `std::ranges::subrange`,
* `std::is_assignable_v<T1&, decltype(std::get<0>(std::forward<P>(p)))>` is `true`, and
* `std::is_assignable_v<T1&, decltype(std::get<1>(std::forward<P>(p)))>` is `true`.
10. Assigns `std::get<0>(std::forward<P>(u))` to `first` and `std::get<1>(std::forward<P>(u))` to `second`.
@@ cpp/enable if|
* `std::same_as<std::remove_cvref_t<P>, std::pair>` is `false`,
* `std::remove_cvref_t<P>` is not a specialization of `std::ranges::subrange`,
* `std::is_assignable_v<const T1&, decltype(std::get<0>(std::forward<P>(p)))>` is `true`, and
* `std::is_assignable_v<const T1&, decltype(std::get<1>(std::forward<P>(p)))>` is `true`.

## Parameters


### Parameters

- `other` - pair of values to replace the contents of this pair
- `p` - pair of values of possibly different types to replace the contents of this pair
- `u` -  object of values to replace the contents of this pair

**Type requirements:**


## Return value

`*this`

## Exceptions

@1-4@
5. noexcept|
std::is_nothrow_move_assignable<T1>::value &&
std::is_nothrow_move_assignable<T2>::value
@6-10@

## Example


### Example

```cpp
#include <cstddef>
#include <iomanip>
#include <iostream>
#include <utility>
#include <vector>

template<class Os, class T>
Os& operator<<(Os& os, const std::vector<T>& v)
{
    os << '{';
    for (std::size_t t = 0; t != v.size(); ++t)
        os << v[t] << (t + 1 < v.size() ? ", " : "");
    return os << '}';
}

template<class Os, class U1, class U2>
Os& operator<<(Os& os, const std::pair<U1, U2>& pair)
{
    return os << '{' << pair.first << ", " << pair.second << '}';
}

int main()
{
    std::pair<int, std::vector<int>> p{1, {2}<!---->}, q{2, {5, 6}<!---->};

    p = q; // (1) operator=(const pair& other);
    std::cout << std::setw(23) << std::left
              << "(1) p = q;"
              << "p: " << p << "     q: " << q << '\n';

    std::pair<short, std::vector<int>> r{4, {7, 8, 9}<!---->};
    p = r; // (3) operator=(const pair<U1, U2>& other);
    std::cout << std::setw(23)
              << "(3) p = r;"
              << "p: " << p << "  r: " << r << '\n';

    p = std::pair<int, std::vector<int>>{3, {4}<!---->};
    p = std::move(q); // (5) operator=(pair&& other);
    std::cout << std::setw(23)
              << "(5) p = std::move(q);"
              << "p: " << p << "     q: " << q << '\n';

    p = std::pair<int, std::vector<int>>{5, {6}<!---->};
    p = std::move(r); // (7) operator=(pair<U1, U2>&& other);
    std::cout << std::setw(23)
              << "(7) p = std::move(r);"
              << "p: " << p << "  r: " << r << '\n';
}
```


**Output:**
```
<nowiki>
(1) p = q;             p: {2, {5, 6
```

(3) p = r;             p: {4, {7, 8, 9  r: {4, {7, 8, 9
(5) p = std::move(q);  p: {2, {5, 6     q: {2, {
(7) p = std::move(r);  p: {4, {7, 8, 9  r: {4, {
</nowiki>

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-885 | C++98 | missing heterogeneous copy assignment | added (as overload vl |


## See also


| cpp/utility/tuple/dsc operator{{= | (see dedicated page) |

