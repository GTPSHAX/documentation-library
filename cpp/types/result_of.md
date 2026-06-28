---
title: std::invoke_result
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/result_of
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++11|deprecated=c++17|removed=c++20|num=1|
template< class >
class result_of; // not defined
template< class F, class... ArgTypes >
class result_of<F(ArgTypes...)>;
dcl|since=c++17|num=2|
template< class F, class... ArgTypes >
class invoke_result;
```

Deduces the return type of an  expression at compile time.
rrev multi|since1=c++11|rev1=
`F` must be a callable type, reference to function, or reference to callable type. Invoking `F` with `ArgTypes...` must be a well-formed expression.
|since2=c++14|rev2=
`F` and all types in `ArgTypes` can be any complete type, array of unknown bound, or (possibly cv-qualified) `void`.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Helper types


```cpp
dcl|since=c++14|num=1|deprecated=c++17|removed=c++20|1=
template< class T >
using result_of_t = typename result_of<T>::type;
dcl|since=c++17|num=2|1=
template< class F, class... ArgTypes >
using invoke_result_t = typename invoke_result<F, ArgTypes...>::type;
```


## Possible implementation


```cpp
namespace detail
{
    template<class T>
    struct is_reference_wrapper : std::false_type {};
    template<class U>
    struct is_reference_wrapper<std::reference_wrapper<U>> : std::true_type {};

    template<class T>
    struct invoke_impl
    {
        template<class F, class... Args>
        static auto call(F&& f, Args&&... args)
            -> decltype(std::forward<F>(f)(std::forward<Args>(args)...));
    };

    template<class B, class MT>
    struct invoke_impl<MT B::*>
    {
        template<class T, class Td = typename std::decay<T>::type,
            class = typename std::enable_if<std::is_base_of<B, Td>::value>::type>
        static auto get(T&& t) -> T&&;

        template<class T, class Td = typename std::decay<T>::type,
            class = typename std::enable_if<is_reference_wrapper<Td>::value>::type>
        static auto get(T&& t) -> decltype(t.get());

        template<class T, class Td = typename std::decay<T>::type,
            class = typename std::enable_if<!std::is_base_of<B, Td>::value>::type,
            class = typename std::enable_if<!is_reference_wrapper<Td>::value>::type>
        static auto get(T&& t) -> decltype(*std::forward<T>(t));

        template<class T, class... Args, class MT1,
            class = typename std::enable_if<std::is_function<MT1>::value>::type>
        static auto call(MT1 B::*pmf, T&& t, Args&&... args)
            -> decltype((invoke_impl::get(
                std::forward<T>(t)).*pmf)(std::forward<Args>(args)...));

        template<class T>
        static auto call(MT B::*pmd, T&& t)
            -> decltype(invoke_impl::get(std::forward<T>(t)).*pmd);
    };

    template<class F, class... Args, class Fd = typename std::decay<F>::type>
    auto INVOKE(F&& f, Args&&... args)
        -> decltype(invoke_impl<Fd>::call(std::forward<F>(f),
            std::forward<Args>(args)...));
} // namespace detail

// Minimal C++11 implementation:
template<class> struct result_of;
template<class F, class... ArgTypes>
struct result_of<F(ArgTypes...)>
{
    using type = decltype(detail::INVOKE(std::declval<F>(), std::declval<ArgTypes>()...));
};

// Conforming C++14 implementation (is also a valid C++11 implementation):
namespace detail
{
    template<typename AlwaysVoid, typename, typename...>
    struct invoke_result {};
    template<typename F, typename...Args>
    struct invoke_result<
        decltype(void(detail::INVOKE(std::declval<F>(), std::declval<Args>()...))),
            F, Args...>
    {
        using type = decltype(detail::INVOKE(std::declval<F>(), std::declval<Args>()...));
    };
} // namespace detail

template<class> struct result_of;
template<class F, class... ArgTypes>
struct result_of<F(ArgTypes...)> : detail::invoke_result<void, F, ArgTypes...> {};

template<class F, class... ArgTypes>
struct invoke_result : detail::invoke_result<void, F, ArgTypes...> {};
```


## Notes

As formulated in C++11, the behavior of `std::result_of` is undefined when `INVOKE(std::declval<F>(), std::declval<ArgTypes>()...)` is ill-formed (e.g. when F is not a callable type at all). C++14 changes that to a SFINAE (when F is not callable, `std::result_of<F(ArgTypes...)>` simply doesn't have the `type` member).
The motivation behind `std::result_of` is to determine the result of invoking a *Callable*, in particular if that result type is different for different sets of arguments.
`F(Args...)` is a function type with `Args...` being the argument types and `F` being the return type. As such, `std::result_of` suffers from several quirks that led to its deprecation in favor of `std::invoke_result` in C++17:
* `F` cannot be a function type or an array type (but can be a reference to them);
* if any of the `Args` has type "array of `T`" or a function type `T`, it is automatically adjusted to `T*`;
* neither `F` nor any of `Args...` can be an abstract class type;
* if any of `Args...` has a top-level cv-qualifier, it is discarded;
* none of `Args...` may be of type `void`.
To avoid these quirks, `result_of` is often used with reference types as `F` and `Args...`. For example:

```cpp
template<class F, class... Args>
std::result_of_t<F&&(Args&&...)> // instead of std::result_of_t<F(Args...)>, which is wrong
    my_invoke(F&& f, Args&&... args)
    {
        /* implementation */
    }
```


## Notes


## Examples


### Example

```cpp
#include <iostream>
#include <type_traits>

struct S
{
    double operator()(char, int&);
    float operator()(int) { return 1.0; }
};

template<class T>
typename std::result_of<T(int)>::type f(T& t)
{
    std::cout << "overload of f for callable T\n";
    return t(0);
}

template<class T, class U>
int f(U u)
{
    std::cout << "overload of f for non-callable T\n";
    return u;
}

int main()
{
    // the result of invoking S with char and int& arguments is double
    std::result_of<S(char, int&)>::type d = 3.14; // d has type double
    static_assert(std::is_same<decltype(d), double>::value, "");

    // std::invoke_result uses different syntax (no parentheses)
    std::invoke_result<S,char,int&>::type b = 3.14;
    static_assert(std::is_same<decltype(b), double>::value, "");

    // the result of invoking S with int argument is float
    std::result_of<S(int)>::type x = 3.14; // x has type float
    static_assert(std::is_same<decltype(x), float>::value, "");

    // result_of can be used with a pointer to member function as follows
    struct C { double Func(char, int&); };
    std::result_of<decltype(&C::Func)(C, char, int&)>::type g = 3.14;
    static_assert(std::is_same<decltype(g), double>::value, "");

    f<C>(1); // may fail to compile in C++11; calls the non-callable overload in C++14
<!-- TODO: make this work using argument deduction: f(C{}) and f(S{}) should both run -->
}
```


**Output:**
```
overload of f for non-callable T
```


## See also


| cpp/utility/functional/dsc invoke | (see dedicated page) |
| cpp/types/dsc is_invocable | (see dedicated page) |
| cpp/utility/dsc declval | (see dedicated page) |

