---
title: std::tuple::operator=
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/tuple/operator=
---


```cpp
dcla|num=1|since=c++11|constexpr=c++20|1=
tuple& operator=( const tuple& other );
dcl|num=2|since=c++23|1=
constexpr const tuple& operator=( const tuple& other ) const;
dcla|num=3|since=c++11|constexpr=c++20|1=
tuple& operator=( tuple&& other ) noexcept(/* see below */);
dcl|num=4|since=c++23|1=
constexpr const tuple& operator=( tuple&& other ) const;
dcla|num=5|since=c++11|constexpr=c++20|1=
template< class... UTypes >
tuple& operator=( const tuple<UTypes...>& other );
dcl|num=6|since=c++23|1=
template< class... UTypes >
constexpr const tuple& operator=( const tuple<UTypes...>& other ) const;
dcla|num=7|since=c++11|constexpr=c++20|1=
template< class... UTypes >
tuple& operator=( tuple<UTypes...>&& other );
dcl|num=8|since=c++23|1=
template< class... UTypes >
constexpr const tuple& operator=( tuple<UTypes...>&& other ) const;
dcla|num=9|since=c++11|constexpr=c++20|1=
template< class E1, class E2 >
tuple& operator=( const std::pair<E1, E2>& p );
dcl|num=10|since=c++23|1=
template< class E1, class E2 >
constexpr const tuple& operator=( const std::pair<E1, E2>& p ) const;
dcla|num=11|since=c++11|constexpr=c++20|1=
template< class E1, class E2 >
tuple& operator=( std::pair<E1, E2>&& p );
dcl|num=12|since=c++23|1=
template< class E1, class E2 >
constexpr const tuple& operator=( std::pair<E1, E2>&& p ) const;
dcl|num=13|since=c++23|1=
template< tuple-like UTuple >
constexpr tuple& operator=( UTuple&& u );
dcl|num=14|since=c++23|1=
template< tuple-like UTuple >
constexpr const tuple& operator=( UTuple&& u ) const;
```

Replaces the contents of the tuple with the contents of another tuple-like object.
In the descriptions that follow, let
* `i` be in the range [​0​, sizeof...(Types)) in order,
* `Ti` be the `i`th type in the class template parameter pack `Types`, and
* `Ui` be the `i`th type in a function template parameter pack named `UTypes`,
where indexing is zero-based.
1. Copy assignment operator. Assigns each element of `other` to the corresponding element of `*this`.
@@ This overload is defined as deleted unless `std::is_copy_assignable<Ti>::value` is `true` for all `Ti`.
2. Copy assignment operator for const-qualified operand. Assigns each element of `other` to the corresponding element of `*this`.
@@
3. Move assignment operator. For all `i`, assigns `std::forward<Ti>(std::get<i>(other))` to `std::get<i>(*this)`.
@@
4. Move assignment operator for const-qualified operand. For all `i`, assigns `std::forward<Ti>(std::get<i>(other))` to `std::get<i>(*this)`.
@@
5. For all `i`, assigns `std::get<i>(other)` to `std::get<i>(*this)`.
@@
6. For all `i`, assigns `std::get<i>(other)` to `std::get<i>(*this)`.
@@
7. For all `i`, assigns `std::forward<Ui>(std::get<i>(other))` to `std::get<i>(*this)`.
@@
8. For all `i`, assigns `std::forward<Ui>(std::get<i>(other))` to `std::get<i>(*this)`.
@@
9. Assigns `p.first` to the first element of `*this` and `p.second` to the second element of `*this`.
@@ cpp/enable if|
* `1=sizeof...(Types) == 2`,
* `std::is_assignable<T0&, const E1&>::value` is `true`, and
* `std::is_assignable<T1&, const E2&>::value` is `true`.
10. Assigns `p.first` to the first element and `p.second` to the second element.
@@ cpp/enable if|
* `1=sizeof...(Types) == 2`,
* `std::is_assignable_v<const T0&, const E1&>` is `true`, and
* `std::is_assignable_v<const T1&, const E2&>` is `true`.
11. Assigns `std::forward<E1>(p.first)` to the first element of `*this` and `std::forward<E2>(p.second)` to the second element of `*this`.
@@ cpp/enable if|
* `1=sizeof...(Types) == 2`,
* `std::is_assignable_v<T0&, E1>` is `true`, and
* `std::is_assignable_v<T1&, E2>` is `true`.
12. Assigns `std::forward<E1>(p.first)` to the first element and `std::forward<E2>(p.second)` to the second element.
@@ cpp/enable if|
* `1=sizeof...(Types) == 2`,
* `std::is_assignable_v<const T0&, E1>` is `true`, and
* `std::is_assignable_v<const T1&, E2>` is `true`.
13. For all `i`, assigns `std::get<i>(std::forward<UTuple>(u))` to `std::get<i>(*this)`.
@@ cpp/enable if|
* `std::same_as<std::remove_cvref_t<UTuple>, std::tuple>` is `false`,
* `std::remove_cvref_t<UTuple>` is not a specialization of `std::ranges::subrange`,
* `sizeof...(Types)` equals `std::tuple_size_v<std::remove_cvref_t<UTuple>>`, and
* `std::is_assignable_v<Ti&, decltype(std::get<i>(std::forward<UTuple>(u)))>` is `true` for all `i`.
14. For all `i`, assigns `std::get<i>(std::forward<UTuple>(u))` to `std::get<i>(*this)`.
@@ cpp/enable if|
* `std::same_as<std::remove_cvref_t<UTuple>, std::tuple>` is `false`,
* `std::remove_cvref_t<UTuple>` is not a specialization of `std::ranges::subrange`,
* `sizeof...(Types)` equals `std::tuple_size_v<std::remove_cvref_t<UTuple>>`, and
* `std::is_assignable_v<const Ti&, decltype(std::get<i>(std::forward<UTuple>(u)))>` is `true` for all `i`.

## Parameters


### Parameters

- `other` - tuple to replace the contents of this tuple
- `p` - pair to replace the contents of this 2-tuple
- `u` -  object to replace the contents of this tuple

## Return value

`*this`

## Exceptions

@1,2@
3. noexcept|
std::is_nothrow_move_assignable<T0>::value &&
std::is_nothrow_move_assignable<T1>::value &&
std::is_nothrow_move_assignable<T2>::value &&
...
@4-14@

## Example


### Example

```cpp
#include <iostream>
#include <string>
#include <string_view>
#include <tuple>
#include <utility>
#include <vector>

// helper function to print std::vector<int>
std::ostream& operator<<(std::ostream& os, std::vector<int> const& v)
{
    os << '{';
    for (std::size_t t = 0; t != v.size(); ++t)
        os << v[t] << (t + 1 < v.size() ? ", " : "");
    return os << '}';
}

// helpers to print a tuple of any size
template<class... Args>
void print_tuple(std::string_view name, const std::tuple<Args...>& t)
{
    std::cout << name << " = {";
    std::apply([&](auto&& arg, auto&&... args)
    {
        std::cout << arg;
        ((std::cout << ", " << args), ...);
    }, t);
    std::cout << '}';
}

template<class Tuple1, class Tuple2>
void print_tuples(std::string_view name1, const Tuple1& t1,
                  std::string_view name2, const Tuple2& t2)
{
    print_tuple(name1, t1);
    std::cout << ", ";
    print_tuple(name2, std::tuple(t2));
    std::cout << "\n\n";
}

int main()
{
    // Tuple to tuple examples //
    std::tuple<int, std::string, std::vector<int>>
        t1{1, "alpha", {1, 2, 3}<!---->},
        t2{2, "beta", {4, 5}<!---->};
    print_tuples("1) t1", t1, "t2", t2);

    // Normal copy assignment
    // operator=( const tuple& other );
    t1 = t2;
    print_tuples("2) t1 = t2;\n   t1", t1, "t2", t2);

    // Normal move assignment
    // operator=( tuple&& other );
    t1 = std::move(t2);
    print_tuples("3) t1 = std::move(t2);\n   t1", t1, "t2", t2);

    // Converting copy assignment
    // operator=( const tuple<UTypes...>& other );
    std::tuple<short, const char*, std::vector<int>> t3{3, "gamma", {6, 7, 8}<!---->};
    t1 = t3;
    print_tuples("4) t1 = t3;\n   t1", t1, "t3", t3);

    // Converting move assignment
    // operator=( tuple<UTypes...>&& other );
    t1 = std::move(t3);
    print_tuples("5) t1 = std::move(t3);\n   t1", t1, "t3", t3);

    // Pair to tuple examples //
    std::tuple<std::string, std::vector<int>> t4{"delta", {10, 11, 12}<!---->};
    std::pair<const char*, std::vector<int>> p1{"epsilon", {14, 15, 16}<!---->};
    print_tuples("6) t4", t4, "p1", p1);

    // Converting copy assignment from std::pair
    // operator=( const std::pair<U1, U2>& p );
    t4 = p1;
    print_tuples("7) t4 = p1;\n   t4", t4, "p1", p1);

    // Converting move assignment from std::pair
    // operator=( std::pair<U1, U2>&& p );
    t4 = std::move(p1);
    print_tuples("8) t4 = std::move(p1);\n   t4", t4, "p1", p1);
}
```


**Output:**
```
1) t1 = {1, alpha, {1, 2, 3}<!---->}, t2 = {2, beta, {4, 5}<!---->}

2) t1 = t2;
   t1 = {2, beta, {4, 5}<!---->}, t2 = {2, beta, {4, 5}<!---->}

3) t1 = std::move(t2);
   t1 = {2, beta, {4, 5}<!---->}, t2 = {2, , {}<!---->}

4) t1 = t3;
   t1 = {3, gamma, {6, 7, 8}<!---->}, t3 = {3, gamma, {6, 7, 8}<!---->}

5) t1 = std::move(t3);
   t1 = {3, gamma, {6, 7, 8}<!---->}, t3 = {3, gamma, {}<!---->}

6) t4 = {delta, {10, 11, 12}<!---->}, p1 = {epsilon, {14, 15, 16}<!---->}

7) t4 = p1;
   t4 = {epsilon, {14, 15, 16}<!---->}, p1 = {epsilon, {14, 15, 16}<!---->}

8) t4 = std::move(p1);
   t4 = {epsilon, {14, 15, 16}<!---->}, p1 = {epsilon, {}<!---->}
```


## Defect reports


## See also


| cpp/utility/tuple/dsc constructor | (see dedicated page) |
| cpp/utility/pair/dsc operator{{= | (see dedicated page) |

