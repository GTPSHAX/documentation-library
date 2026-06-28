---
title: std::bind_front
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/bind_front
---


```cpp
**Header:** `<`functional`>`
dcla|num=1|since=c++20|
template< class F, class... Args >
constexpr /* unspecified */ bind_front( F&& f, Args&&... args );
dcla|num=2|since=c++26|
template< auto ConstFn, class... Args >
constexpr /* unspecified */ bind_front( Args&&... args );
dcla|num=3|since=c++23|
template< class F, class... Args >
constexpr /* unspecified */ bind_back( F&& f, Args&&... args );
dcla|num=4|since=c++26|
template< auto ConstFn, class... Args >
constexpr /* unspecified */ bind_back( Args&&... args );
```

Function templates `std::bind_front` and `std::bind_back` generate a perfect forwarding call wrapper which allows to invoke the callable target with its  first or  last `sizeof...(Args)` parameters bound to `args`.
@1,3@ The call wrapper holds a copy of the target callable object `f`.
@2,4@ The call wrapper does not hold a callable target (it is statically determined).
1. `std::bind_front(f, bound_args...)(call_args...)` is expression-equivalent to
@@ `std::invoke(f, bound_args..., call_args...)`.
2. `std::bind_front<ConstFn>(bound_args...)(call_args...)` is expression-equivalent to
@@ `std::invoke(ConstFn, bound_args..., call_args...)`.
3. `std::bind_back(f, bound_args...)(call_args...)` is expression-equivalent to
@@ `std::invoke(f, call_args..., bound_args...)`.
4. `std::bind_back<ConstFn>(bound_args...)(call_args...)` is expression-equivalent to
@@ `std::invoke(ConstFn, call_args..., bound_args...)`.
The following conditions must be `true`, otherwise the program is ill-formed:
*  `std::is_constructible_v<std::decay_t<F>, F>`,
*  `std::is_move_constructible_v<std::decay_t<F>>`,
*  If `decltype(ConstFn)` is a pointer or a pointer-to-member then `ConstFn` is not a null pointer,
* `(std::is_constructible_v<std::decay_t<Args>, Args> && ...)`,
* `(std::is_move_constructible_v<std::decay_t<Args>> && ...)`.

## Parameters


### Parameters

- `f` - *Callable* object (function object, pointer to function, reference to function, pointer to member function, or pointer to data member) that will be bound to some arguments
- `args` - list of the arguments to bind to the  first or  last `sizeof...(Args)` parameters of the callable target

**Type requirements:**

- `{{c`
- `{{c`
- `{{c`

## Return value

A function object (the call wrapper) of type `T` that is unspecified, except that the types of objects returned by two calls to `std::bind_front` or `std::bind_back` with the same arguments are the same.
Let  be either `std::bind_front` or `std::bind_back`.
The returned object has the following properties:
member|'' return type''|2=

### Member objects

The returned object behaves as if it holds:
@1,3@ A member object `fd` of type `std::decay_t<F>` direct-non-list-initialized from `std::forward<F>(f)`, and
@1-4@ An `std::tuple` object `tup` constructed with `std::tuple<std::decay_t<Args>...>(std::forward<Args>(args)...)`, except that the returned object's assignment behavior is unspecified and the names are for exposition only.

### Constructors

The return type of  behaves as if its copy/move constructors perform a memberwise copy/move. It is *CopyConstructible* if all of its member objects (specified above) are , and is *MoveConstructible* otherwise.

### Member function `operator()`

Given an object `G` obtained from an earlier call to  `''bind-partial''(f, args...)` or  `''bind-partial''<ConstFn>(args...)`, when a glvalue `g` designating `G` is invoked in a function call expression `g(call_args...)`, an invocation of the stored object takes place, as if by:
1. `std::invoke(g.fd, std::get<Ns>(g.tup)..., call_args...)`, when  is `std::bind_front`,
2. `std::invoke(ConstFn, std::get<Ns>(g.tup)..., call_args...)`, when  is `std::bind_front`,
3. `std::invoke(g.fd, call_args..., std::get<Ns>(g.tup)...)`, when  is `std::bind_back`,
4. `std::invoke(ConstFn, call_args..., std::get<Ns>(g.tup)...)`, when  is `std::bind_back`,
where
:* `Ns` is an integer pack `0, 1, ..., (sizeof...(Args) - 1)`,
:* `g` is an lvalue in the `std::invoke` expression if it is an lvalue in the call expression, and is an rvalue otherwise. Thus `std::move(g)(call_args...)` can move the bound arguments into the call, where `g(call_args...)` would copy.
The program is ill-formed if `g` has volatile-qualified type.
The member `operator()` is `cpp/language/noexcept` if the `std::invoke` expression it calls is noexcept (in other words, it preserves the exception specification of the underlying call operator).

## Exceptions

@1,3@ Throw any exception thrown by calling the constructor of the stored function object.
@1-4@ Throw any exception thrown by calling the constructor of any of the bound arguments.

## Notes

These function templates are intended to replace `std::bind`. Unlike `std::bind`, they do not support arbitrary argument rearrangement and have no special treatment for nested bind-expressions or `std::reference_wrapper`s. On the other hand, they pay attention to the value category of the call wrapper object and propagate exception specification of the underlying call operator.
As described in `std::invoke`, when invoking a pointer to non-static member function or pointer to non-static data member, the first argument has to be a reference or pointer (including, possibly, smart pointer such as `std::shared_ptr` and `std::unique_ptr`) to an object whose member will be accessed.
The arguments to `std::bind_front` or `std::bind_back` are copied or moved, and are never passed by reference unless wrapped in `std::ref` or `std::cref`.
Typically, binding arguments to a function or a member function using  `std::bind_front` and  `std::bind_back` requires storing a function pointer along with the arguments, even though the language knows precisely which function to call without a need to dereference the pointer. To guarantee "zero cost" in those cases, C++26 introduces the versions  (that accept the callable object as an argument for ).

## Possible implementation

eq impl
|title1=(2) bind_front|ver1=2|1=
namespace detail
{
template<class T, class U>
struct copy_const
: std::conditional<std::is_const_v<T>, U const, U> {};
template<class T, class U,
class X = typename copy_const<std::remove_reference_t<T>, U>::type>
struct copy_value_category
: std::conditional<std::is_lvalue_reference_v<T&&>, X&, X&&> {};
template <class T, class U>
struct type_forward_like
: copy_value_category<T, std::remove_reference_t<U>> {};
template <class T, class U>
using type_forward_like_t = typename type_forward_like<T, U>::type;
}
template<auto ConstFn, class... Args>
constexpr auto bind_front(Args&&... args)
{
using F = decltype(ConstFn);
if constexpr (std::is_pointer_v<F> or std::is_member_pointer_v<F>)
static_assert(ConstFn != nullptr);
return
[... bound_args(std::forward<Args>(args))]<class Self, class... T>
(
this Self&&, T&&... call_args
)
noexcept
(
std::is_nothrow_invocable_v<F,
detail::type_forward_like_t<Self, std::decay_t<Args>>..., T...>
)
-> std::invoke_result_t<F,
detail::type_forward_like_t<Self, std::decay_t<Args>>..., T...>
{
return std::invoke(ConstFn, std::forward_like<Self>(bound_args)...,
std::forward<T>(call_args)...);
};
}
|title2=(4) bind_back|ver2=4|2=
namespace detail { /* is the same as above */ }
template<auto ConstFn, class... Args>
constexpr auto bind_back(Args&&... args)
{
using F = decltype(ConstFn);
if constexpr (std::is_pointer_v<F> or std::is_member_pointer_v<F>)
static_assert(ConstFn != nullptr);
return
[... bound_args(std::forward<Args>(args))]<class Self, class... T>
(
this Self&&, T&&... call_args
)
noexcept
(
std::is_nothrow_invocable_v<F,
detail::type_forward_like_t<Self, T..., std::decay_t<Args>>...>
)
-> std::invoke_result_t<F,
detail::type_forward_like_t<Self, T..., std::decay_t<Args>>...>
{
return std::invoke(ConstFn, std::forward<T>(call_args)...,
std::forward_like<Self>(bound_args)...);
};
}

## Example


### Example

```cpp
#include <cassert>
#include <functional>

int minus(int a, int b)
{
    return a - b;
}

struct S
{
    int val;
    int minus(int arg) const noexcept { return val - arg; }
};

int main()
{
    auto fifty_minus = std::bind_front(minus, 50);
    assert(fifty_minus(3) == 47); // equivalent to: minus(50, 3) == 47

    auto member_minus = std::bind_front(&S::minus, S{50});
    assert(member_minus(3) == 47); //: S tmp{50}; tmp.minus(3) == 47

    // Noexcept-specification is preserved:
    static_assert(!noexcept(fifty_minus(3)));
    static_assert(noexcept(member_minus(3)));

    // Binding of a lambda:
    auto plus = [](int a, int b) { return a + b; };
    auto forty_plus = std::bind_front(plus, 40);
    assert(forty_plus(7) == 47); // equivalent to: plus(40, 7) == 47

#if __cpp_lib_bind_front >= 202306L
    auto fifty_minus_cpp26 = std::bind_front<minus>(50);
    assert(fifty_minus_cpp26(3) == 47);

    auto member_minus_cpp26 = std::bind_front<&S::minus>(S{50});
    assert(member_minus_cpp26(3) == 47);

    auto forty_plus_cpp26 = std::bind_front<plus>(40);
    assert(forty_plus(7) == 47);
#endif

#if __cpp_lib_bind_back >= 202202L
    auto madd = [](int a, int b, int c) { return a * b + c; };
    auto mul_plus_seven = std::bind_back(madd, 7);
    assert(mul_plus_seven(4, 10) == 47); //: madd(4, 10, 7) == 47
#endif

#if __cpp_lib_bind_back >= 202306L
    auto mul_plus_seven_cpp26 = std::bind_back<madd>(7);
    assert(mul_plus_seven_cpp26(4, 10) == 47);
#endif
}
```


## References


## See also


| cpp/utility/functional/dsc bind | (see dedicated page) |
| cpp/utility/functional/dsc mem_fn | (see dedicated page) |

