---
title: std::tuple_cat
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/tuple/tuple_cat
---


```cpp
**Header:** `<`tuple`>`
dcl rev multi|since1=c++11|until1=c++14|dcl1=
template< class... Tuples >
std::tuple</* CTypes */...> tuple_cat( Tuples&&... args );
|until2=c++23|dcl2=
template< class... Tuples >
constexpr std::tuple</* CTypes */...> tuple_cat( Tuples&&... args );
|dcl3=
template< tuple-like... Tuples >
constexpr std::tuple</* CTypes */...> tuple_cat( Tuples&&... args );
```

Constructs a tuple that is a concatenation of all tuples in `args`. The element types `/* CTypes */ ` of the returned tuple is formed by concatenating the elements type packs of all <sup>(until C++23)</sup> `std::tuple`<sup>(since C++23)</sup>  types in `Tuples` in order.
rrev multi|until1=c++23
|rev1=
The behavior is undefined if any type in `std::decay_t<Tuples>...` is not a specialization of `std::tuple`. However, an implementation may choose to support types (such as `std::array` and `std::pair`) that follow the tuple-like protocol.
|rev2=
The types `std::decay_t<Tuples>...` are constrained to be tuple-like, i.e. each type therein is required to be a specialization of `std::tuple` or another type (such as `std::array` and `std::pair`) that models .
If any type in `/* CTypes */` is not constructible from the type of the corresponding element in the sequence of elements concatenated from `args`, <sup>(until C++23)</sup> the behavior is undefined<sup>(since C++23)</sup> the program is ill-formed.

## Parameters


### Parameters

- `args` - zero or more tuples to concatenate

## Return value

A `std::tuple` object composed of all elements of all argument tuples constructed from `std::get<j>(std::forward<Ti>(arg))` for each individual element.

## Example


### Example

```cpp
#include <iostream>
#include <string>
#include <tuple>

// helper function to print a tuple of any size
template<class Tuple, std::size_t N>
struct TuplePrinter
{
    static void print(const Tuple& t)
    {
        TuplePrinter<Tuple, N - 1>::print(t);
        std::cout << ", " << std::get<N-1>(t);
    }
};

template<class Tuple>
struct TuplePrinter<Tuple, 1>
{
    static void print(const Tuple& t)
    {
        std::cout << std::get<0>(t);
    }
};

template<typename... Args, std::enable_if_t<sizeof...(Args) == 0, int> = 0>
void print(const std::tuple<Args...>& t)
{
    std::cout << "()\n";
}

template<typename... Args, std::enable_if_t<sizeof...(Args) != 0, int> = 0>
void print(const std::tuple<Args...>& t)
{
    std::cout << "(";
    TuplePrinter<decltype(t), sizeof...(Args)>::print(t);
    std::cout << ")\n";
}
// end helper function

int main()
{
    std::tuple<int, std::string, float> t1(10, "Test", 3.14);
    int n = 7;
    auto t2 = std::tuple_cat(t1, std::make_tuple("Foo", "bar"), t1, std::tie(n));
    n = 42;
    print(t2);
}
```


**Output:**
```
(10, Test, 3.14, Foo, bar, 10, Test, 3.14, 42)
```


## See also


| cpp/utility/tuple/dsc make_tuple | (see dedicated page) |
| cpp/utility/tuple/dsc tie | (see dedicated page) |
| cpp/utility/tuple/dsc forward_as_tuple | (see dedicated page) |

