---
title: std::reference_wrapper
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/reference_wrapper
---


```cpp
**Header:** `<`functional`>`
dcl|since=c++11|
template< class T >
class reference_wrapper;
```

`std::reference_wrapper` is a class template that wraps a reference in a copyable, assignable object.
Specifically, `std::reference_wrapper` is a *CopyConstructible* and *CopyAssignable* wrapper around a reference to object or reference to function of type `T`. Instances of `std::reference_wrapper` are objects (they can be copied or stored in containers) but they are implicitly convertible to `T&`, so that they can be used as arguments with the functions that take the underlying type by reference.
If the stored reference is *Callable*, `std::reference_wrapper` is callable with the same arguments.
Helper functions `std::ref` and `std::cref` are often used to generate `std::reference_wrapper` objects.
`std::reference_wrapper` is used to pass objects by reference to `std::bind`, the constructor of `std::thread`, or the helper functions `std::make_pair` and `std::make_tuple`. It can also be used as a mechanism to store references inside standard containers (like `std::vector`) that cannot normally hold references.
rrev|since=c++17|
`std::reference_wrapper` is guaranteed to be *TriviallyCopyable*.
rrev|since=c++20|
`T` may be an incomplete type.

## Member types


| Item | Description |
|------|-------------|
| **type** | definition |
| dsc|`argument_type`<br>| | |
| * if `T` is a function or pointer to function that takes one argument of type `A1`, then `argument_type` is `A1`<br> | |
| * if `T` is a pointer to member function of class `T0` that takes no arguments, then `argument_type` is `T0*`, possibly cv-qualified<br> | |
| * if `T` is a class type with a member type `T::argument_type`, then `argument_type` is an alias of that | |
| dsc|`first_argument_type`<br>| | |
| * if `T` is a function or pointer to function that takes two arguments of types `A1` and `A2`, then `first_argument_type` is `A1`<br> | |
| * if `T` is a pointer to member function of class `T0` that takes one argument, then `first_argument_type` is `T0*`, possibly cv-qualified<br> | |
| * if `T` is a class type with a member type `T::first_argument_type`, then `first_argument_type` is an alias of that | |
| dsc|`second_argument_type`<br>| | |
| * if `T` is a function or pointer to function that takes two arguments of type s `A1` and `A2`, then `second_argument_type` is `A2`<br> | |
| * if `T` is a pointer to member function of class `T0` that takes one argument `A1`, then `second_argument_type` is `A1`, possibly cv-qualified<br> | |
| * if `T` is a class type with a member type `T::second_argument_type`, then `second_argument_type` is an alias of that | |


## Member functions


| cpp/utility/functional/reference_wrapper/dsc constructor | (see dedicated page) |
| cpp/utility/functional/reference_wrapper/dsc operator{{= | (see dedicated page) |
| cpp/utility/functional/reference_wrapper/dsc get | (see dedicated page) |
| cpp/utility/functional/reference_wrapper/dsc operator() | (see dedicated page) |


## Non-member functions


| cpp/utility/functional/reference_wrapper/dsc operator_cmp | (see dedicated page) |


## <sup>(C++17)</sup>


## Helper classes


| cpp/utility/functional/reference_wrapper/dsc basic_common_reference | (see dedicated page) |


## Possible implementation

eq fun
|1=
namespace detail
{
template<class T> constexpr T& FUN(T& t) noexcept { return t; }
template<class T> void FUN(T&&) = delete;
}
template<class T>
class reference_wrapper
{
public:
// types
using type = T;
// construct/copy/destroy
template<class U, class = decltype(
detail::FUN<T>(std::declval<U>()),
std::enable_if_t<!std::is_same_v<reference_wrapper, std::remove_cvref_t<U>>>()
)>
constexpr reference_wrapper(U&& u)
noexcept(noexcept(detail::FUN<T>(std::forward<U>(u))))
: _ptr(std::addressof(detail::FUN<T>(std::forward<U>(u)))) {}
reference_wrapper(const reference_wrapper&) noexcept = default;
// assignment
reference_wrapper& operator=(const reference_wrapper& x) noexcept = default;
// access
constexpr operator T& () const noexcept { return *_ptr; }
constexpr T& get() const noexcept { return *_ptr; }
template<class... ArgTypes>
constexpr std::invoke_result_t<T&, ArgTypes...>
operator() (ArgTypes&&... args ) const
noexcept(std::is_nothrow_invocable_v<T&, ArgTypes...>)
{
return std::invoke(get(), std::forward<ArgTypes>(args)...);
}
private:
T* _ptr;
};
// deduction guides
template<class T>
reference_wrapper(T&) -> reference_wrapper<T>;

## Example


### Example

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <list>
#include <numeric>
#include <random>
#include <vector>

void println(auto const rem, std::ranges::range auto const& v)
{
    for (std::cout << rem; auto const& e : v)
        std::cout << e << ' ';
    std::cout << '\n';
}

int main()
{
    std::list<int> l(10);
    std::iota(l.begin(), l.end(), -4);

    // can't use shuffle on a list (requires random access), but can use it on a vector
    std::vector<std::reference_wrapper<int>> v(l.begin(), l.end());

    std::ranges::shuffle(v, std::mt19937{std::random_device{}()});

    println("Contents of the list: ", l);
    println("Contents of the list, as seen through a shuffled vector: ", v);

    std::cout << "Doubling the values in the initial list...\n";
    std::ranges::for_each(l, [](int& i) { i *= 2; });

    println("Contents of the list, as seen through a shuffled vector: ", v);
}
```


**Output:**
```
Contents of the list: -4 -3 -2 -1 0 1 2 3 4 5
Contents of the list, as seen through a shuffled vector: -1 2 -2 1 5 0 3 -3 -4 4
Doubling the values in the initial list...
Contents of the list, as seen through a shuffled vector: -2 4 -4 2 10 0 6 -6 -8 8
```


## See also


| cpp/utility/functional/dsc ref | (see dedicated page) |
| cpp/utility/functional/dsc bind | (see dedicated page) |
| cpp/utility/functional/dsc unwrap_reference | (see dedicated page) |

