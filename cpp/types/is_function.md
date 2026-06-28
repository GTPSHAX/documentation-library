---
title: std::is_function
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_function
---

cpp/types/traits/is|1=is_function
|description=
Checks whether `T` is a function type. Types like `std::function`, lambdas, classes with overloaded `operator()` and pointers to functions don't count as function types. Provides the member constant `value` which is equal to `true`, if `T` is a function type. Otherwise, `value` is equal to `false`.
|inherit_desc=`T` is a function type

## Notes

`std::is_function` can be implemented in much simpler ways. Implementations similar to the following one are used by new versions of [https://github.com/llvm-mirror/libcxx/blob/master/include/type_traits#L889 libc++], [https://github.com/gcc-mirror/gcc/blob/master/libstdc%2B%2B-v3/include/std/type_traits#L538 libstdc++] and [https://github.com/microsoft/STL/pull/460 MS STL]:

```cpp
template<class T>
struct is_function : std::integral_constant<
    bool,
    !std::is_const<const T>::value && !std::is_reference<T>::value
> {};
```

The implementation shown below is for pedagogical purposes, since it exhibits the myriad kinds of function types.

## Possible implementation

eq fun
|1=
// primary template
template<class>
struct is_function : std::false_type {};
// specialization for regular functions
template<class Ret, class... Args>
struct is_function<Ret(Args...)> : std::true_type {};
// specialization for variadic functions such as std::printf
template<class Ret, class... Args>
struct is_function<Ret(Args......)> : std::true_type {};
// specialization for function types that have cv-qualifiers
template<class Ret, class... Args>
struct is_function<Ret(Args...) const> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args...) volatile> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args...) const volatile> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) const> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) volatile> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) const volatile> : std::true_type {};
// specialization for function types that have ref-qualifiers
template<class Ret, class... Args>
struct is_function<Ret(Args...) &> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args...) const &> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args...) volatile &> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args...) const volatile &> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) &> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) const &> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) volatile &> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) const volatile &> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args...) &&> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args...) const &&> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args...) volatile &&> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args...) const volatile &&> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) &&> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) const &&> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) volatile &&> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) const volatile &&> : std::true_type {};
// specializations for noexcept versions of all the above (C++17 and later)
template<class Ret, class... Args>
struct is_function<Ret(Args...) noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args...) const noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args...) volatile noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args...) const volatile noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) const noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) volatile noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) const volatile noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args...) & noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args...) const & noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args...) volatile & noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args...) const volatile & noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) & noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) const & noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) volatile & noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) const volatile & noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args...) && noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args...) const && noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args...) volatile && noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args...) const volatile && noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) && noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) const && noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) volatile && noexcept> : std::true_type {};
template<class Ret, class... Args>
struct is_function<Ret(Args......) const volatile && noexcept> : std::true_type {};

## Example


### Example

```cpp
#include <functional>
#include <type_traits>

int f();
static_assert(std::is_function_v<decltype(f)>);

static_assert(std::is_function_v<int(int)>);
static_assert(!std::is_function_v<int>);
static_assert(!std::is_function_v<decltype([]{})>);
static_assert(!std::is_function_v<std::function<void()>>);

struct O { void operator()() {} };
static_assert(std::is_function_v<O()>);

struct A
{
    static int foo();
    int fun() const&;
};
static_assert(!std::is_function_v<A>);
static_assert(std::is_function_v<decltype(A::foo)>);
static_assert(!std::is_function_v<decltype(&A::fun)>);

template<typename>
struct PM_traits {};
template<class T, class U>
struct PM_traits<U T::*> { using member_type = U; };

int main()
{
    using T = PM_traits<decltype(&A::fun)>::member_type; // T is int() const&
    static_assert(std::is_function_v<T>);
}
```


## See also


| cpp/types/dsc is_invocable | (see dedicated page) |
| cpp/types/dsc is_object | (see dedicated page) |
| cpp/types/dsc is_class | (see dedicated page) |

