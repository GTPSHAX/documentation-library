---
title: std::apply
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/apply
---


```cpp
**Header:** `<`tuple`>`
dcl rev multi
|since1=c++17|dcl1=
template< class F, class Tuple >
constexpr decltype(auto) apply( F&& f, Tuple&& t );
|since2=c++23|dcl2=
template< class F, tuple-like Tuple >
constexpr decltype(auto) apply( F&& f, Tuple&& t ) noexcept(/* see below */);
```

Invoke the *Callable* object `f` with the elements of `t` as arguments.
Given the exposition-only function  defined as follows:
box|
`template<class F,class Tuple, std::size_t... I>`<br>
`constexpr decltype(auto)`<br>
`(F&& f, Tuple&& t, std::index_sequence<I...>) // exposition only`<br>
`{`<br>
`return``(std::forward<F>(f), std::get<I>(std::forward<Tuple>(t))...);`<br>
}
The effect is equivalent to:
box|
`return``(std::forward<F>(f), std::forward<Tuple>(t),`<br>
`std::make_index_sequence<`<br>
}
.

## Parameters


### Parameters

- `f` - *Callable* object to be invoked
- `t` - tuple whose elements to be used as arguments to `f`

## Return value

The value returned by `f`.

## Exceptions

rrev multi|since2=c++23
|rev1=(none)
|rev2=
noexcept|
noexcept(std::invoke(std::forward<F>(f),
std::get<Is>(std::forward<Tuple>(t))...))
where `Is...` denotes the pack:
* `0, 1, ..., std::tuple_size_v<std::remove_reference_t<Tuple>> - 1`.

## Notes

rev|until=c++23|
`Tuple` need not be `std::tuple`, and instead may be anything that supports  and ; in particular, `std::array` and `std::pair` may be used.
rev|since=c++23|
`Tuple` is constrained to be tuple-like, i.e. each type therein is required to be a specialization of `std::tuple` or another type (such as `std::array` and `std::pair`) that models .

## Example


### Example

```cpp
#include <iostream>
#include <tuple>
#include <utility>

int add(int first, int second) { return first + second; }

template<typename T>
T add_generic(T first, T second) { return first + second; }

auto add_lambda = [](auto first, auto second) { return first + second; };

template<typename... Ts>
std::ostream& operator<<(std::ostream& os, std::tuple<Ts...> const& theTuple)
{
    std::apply
    (
        [&os](Ts const&... tupleArgs)
        {
            os << '[';
            std::size_t n{0};
            ((os << tupleArgs << (++n != sizeof...(Ts) ? ", " : "")), ...);
            os << ']';
        }, theTuple
    );
    return os;
}

int main()
{
    // OK
    std::cout << std::apply(add, std::pair(1, 2)) << '\n';

    // Error: can't deduce the function type
    // std::cout << std::apply(add_generic, std::make_pair(2.0f, 3.0f)) << '\n'; 

    // OK
    std::cout << std::apply(add_lambda, std::pair(2.0f, 3.0f)) << '\n'; 

    // advanced example
    std::tuple myTuple{25, "Hello", 9.31f, 'c'};
    std::cout << myTuple << '\n';
}
```


**Output:**
```
3
5
[25, Hello, 9.31, c]
```


## See also


| cpp/utility/tuple/dsc make_tuple | (see dedicated page) |
| cpp/utility/tuple/dsc forward_as_tuple | (see dedicated page) |
| cpp/utility/dsc make_from_tuple | (see dedicated page) |
| cpp/utility/functional/dsc invoke | (see dedicated page) |

