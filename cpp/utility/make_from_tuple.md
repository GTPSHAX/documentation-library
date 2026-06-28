---
title: std::make_from_tuple
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/make_from_tuple
---


```cpp
**Header:** `<`tuple`>`
dcl rev multi
|since1=c++17|dcl1=
template< class T, class Tuple >
constexpr T make_from_tuple( Tuple&& t );
|since2=c++23|dcl2=
template< class T, tuple-like Tuple >
constexpr T make_from_tuple( Tuple&& t );
```

Construct an object of type `T`, using the elements of the tuple `t` as the arguments to the constructor.
Given the exposition-only function `/*make-from-tuple-impl*/` defined as follows:<br>
box|
`template<class T,``Tuple, std::size_t... I> // no constraint on Tuple before C++23`<br>
`constexpr T /*make-from-tuple-impl*/(Tuple&& t, std::index_sequence<I...>)`<br>
`{`<br>
`return T(std::get<I>(std::forward<Tuple>(t))...);`<br>
}
The effect is equivalent to:<br>c multi
|return /*make-from-tuple-impl*/<T>(
|    std::forward<Tuple>(t),
|    std::make_index_sequence<std::tuple_size_v<std::remove_reference_t<Tuple>>>{}
|);
.
If
rrev|since=c++23|
* `std::tuple_size_v<std::remove_reference_t<Tuple>>` is `1` and c multi
|std::reference_constructs_from_temporary_v<
|    T, decltype(std::get<0>(std::declval<Tuple>()))> is `true`, or
* `std::is_constructible_v<T, decltype(std::get<I>(std::declval<Tuple>()))...>` is `false`,
the program is ill-formed.

## Parameters


### Parameters

- `t` - tuple whose elements to be used as arguments to the constructor of `T`

## Return value

The constructed `T` object or reference.

## Notes

rev|until=c++23|
`Tuple` need not be `std::tuple`, and instead may be anything that supports  and ; in particular, `std::array` and `std::pair` may be used.
rev|since=c++23|
`Tuple` is constrained to be tuple-like, i.e. each type therein is required to be a specialization of `std::tuple` or another type (such as `std::array` and `std::pair`) that models .
Due to guaranteed copy elision, `T` need not be movable.

## Example


### Example

```cpp
#include <iostream>
#include <tuple>

struct Foo
{
    Foo(int first, float second, int third)
    {
        std::cout << first << ", " << second << ", " << third << '\n';
    }
};

int main()
{
    auto tuple = std::make_tuple(42, 3.14f, 0);
    std::make_from_tuple<Foo>(std::move(tuple));
}
```


**Output:**
```
42, 3.14, 0
```


## Defect reports


## See also


| cpp/utility/tuple/dsc make_tuple | (see dedicated page) |
| cpp/utility/tuple/dsc forward_as_tuple | (see dedicated page) |
| cpp/utility/dsc apply | (see dedicated page) |

