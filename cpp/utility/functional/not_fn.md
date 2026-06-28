---
title: std::not_fn
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/not_fn
---


```cpp
**Header:** `<`functional`>`
dcla|num=1|since=c++17|notes=<sup>(constexpr C++20)</sup>|
template< class F >
/* unspecified */ not_fn( F&& f );
dcla|num=2|since=c++26|
template< auto ConstFn >
constexpr /* unspecified */ not_fn() noexcept;
```

1. Creates a forwarding call wrapper that returns the negation of the callable object it holds.
2. Creates a forwarding call wrapper that returns the negation of the statically determined callable target. The program is ill-formed if `ConstFn` is a null pointer or null pointer-to-member.

## Parameters


### Parameters

- `f` - the object from which the *Callable* object held by the wrapper is constructed

**Type requirements:**

- `{{c/core`

## Return value

1. A function object of unspecified type `T`. It has the following members.
member| ''return type''|2=

### Member objects

The return type of `std::not_fn` holds a member object of type `std::decay_t<F>`.

### Constructors


```cpp
<br>|1=
explicit T( F&& f );
dcl|num=2|since=c++17|1=
T( T&& f ) = default;
T( const T& f ) = default;
```

1. The constructor direct-non-list-initializes the member object (of type `std::decay_t<F>`) from `std::forward<F>(f)`. Throws any exception thrown by the constructor selected.
2. Because `std::decay_t<F>` is required to be *MoveConstructible*, the returned call wrapper is always *MoveConstructible*, and is *CopyConstructible* if `std::decay_t<F>` is *CopyConstructible*.
rrev multi|rev1=
The explicitly defaulted definitions make the return type not assignable.
|since2=c++20|rev2=
It is unspecified whether these constructors are explicitly defaulted and whether the return type is assignable.

### Member function `operator()`


```cpp
dcl rev multi|num=1|since1=c++17|dcl1=
template< class... Args >
auto operator()( Args&&... args ) &
-> decltype(!std::declval<
std::invoke_result_t<std::decay_t<F>&, Args...>>());
template< class... Args >
auto operator()( Args&&... args ) const&
-> decltype(!std::declval<
std::invoke_result_t<std::decay_t<F> const&, Args...>>());
|since2=c++20|dcl2=
template< class... Args >
constexpr auto operator()( Args&&... args ) &
noexcept(/* see below */)
-> decltype(!std::invoke(
std::declval<std::decay_t<F>&>(), std::declval<Args>()...));
template< class... Args >
constexpr auto operator()( Args&&... args ) const&
noexcept(/* see below */)
-> decltype(!std::invoke(
std::declval<std::decay_t<F> const&>(), std::declval<Args>()...));
dcl rev multi|num=2|since1=c++17|dcl1=
template< class... Args >
auto operator()( Args&&... args ) &&
-> decltype(!std::declval<
std::invoke_result_t<std::decay_t<F>, Args...>>());
template< class... Args >
auto operator()( Args&&... args ) const&&
-> decltype(!std::declval<
std::invoke_result_t<std::decay_t<F> const, Args...>>());
|since2=c++20|dcl2=
template< class... Args >
constexpr auto operator()( Args&&... args ) &&
noexcept(/* see below */)
-> decltype(!std::invoke(
std::declval<std::decay_t<F>>(), std::declval<Args>()...));
template< class... Args >
constexpr auto operator()( Args&&... args ) const&&
noexcept(/* see below */)
-> decltype(!std::invoke(
std::declval<std::decay_t<F> const>(), std::declval<Args>()...));
```

Let `fd` be the member object of type `std::decay_t<F>`.
rrev multi
|since1=c++17|rev1=
1. Equivalent to `return !std::invoke(fd, std::forward<Args>(args)...);`
2. Equivalent to `return !std::invoke(std::move(fd), std::forward<Args>(args)...);`
While invoking the result, if the substitution into the return type of the originally selected `operator()` overload fails, another overload may be selected.
|since2=c++20|rev2=
1. Expression-equivalent to `!std::invoke(fd, std::forward<Args>(args)...)`
2. Expression-equivalent to `!std::invoke(std::move(fd), std::forward<Args>(args)...)`
While invoking the result, if the substitution into the return type of the originally selected `operator()` overload fails, the invocation is ill-formed, which can also be a substitution failure.
2. A value of the following type.
member| ''stateless return type''|2=
The return type is a *CopyConstructible* stateless class. It is unspecified whether the return type is assignable.

### Member function `operator()`

ddcl|since=c++26|
template< class... Args >
constexpr auto operator()( Args&&... args ) const
noexcept(/* see below */)
-> decltype(!std::invoke(ConstFn, std::declval<Args>()...));
Expression-equivalent to `!std::invoke(ConstFn, std::forward<Args>(args)...)`.

## Exceptions

1. Throws no exceptions, unless the construction of `fd` throws.

## Possible implementation

eq impl
|title1=(1) not_fn|ver1=1|1=
namespace detail
{
template<class V, class F, class... Args>
constexpr bool negate_invocable_impl = false;
template<class F, class... Args>
constexpr bool negate_invocable_impl<std::void_t<decltype(
!std::invoke(std::declval<F>(), std::declval<Args>()...))>, F, Args...> = true;
template<class F, class... Args>
constexpr bool negate_invocable_v = negate_invocable_impl<void, F, Args...>;
template<class F>
struct not_fn_t
{
F f;
template<class... Args,
std::enable_if_t<negate_invocable_v<F&, Args...>, int> = 0>
constexpr decltype(auto) operator()(Args&&... args) &
noexcept(noexcept(!std::invoke(f, std::forward<Args>(args)...)))
{
return !std::invoke(f, std::forward<Args>(args)...);
}
template<class... Args,
std::enable_if_t<negate_invocable_v<const F&, Args...>, int> = 0>
constexpr decltype(auto) operator()(Args&&... args) const&
noexcept(noexcept(!std::invoke(f, std::forward<Args>(args)...)))
{
return !std::invoke(f, std::forward<Args>(args)...);
}
template<class... Args,
std::enable_if_t<negate_invocable_v<F, Args...>, int> = 0>
constexpr decltype(auto) operator()(Args&&... args) &&
noexcept(noexcept(!std::invoke(std::move(f), std::forward<Args>(args)...)))
{
return !std::invoke(std::move(f), std::forward<Args>(args)...);
}
template<class... Args,
std::enable_if_t<negate_invocable_v<const F, Args...>, int> = 0>
constexpr decltype(auto) operator()(Args&&... args) const&&
noexcept(noexcept(!std::invoke(std::move(f), std::forward<Args>(args)...)))
{
return !std::invoke(std::move(f), std::forward<Args>(args)...);
}
// Deleted overloads are needed since C++20
// for preventing a non-equivalent but well-formed overload to be selected.
template<class... Args,
std::enable_if_t<!negate_invocable_v<F&, Args...>, int> = 0>
void operator()(Args&&...) & = delete;
template<class... Args,
std::enable_if_t<!negate_invocable_v<const F&, Args...>, int> = 0>
void operator()(Args&&...) const& = delete;
template<class... Args,
std::enable_if_t<!negate_invocable_v<F, Args...>, int> = 0>
void operator()(Args&&...) && = delete;
template<class... Args,
std::enable_if_t<!negate_invocable_v<const F, Args...>, int> = 0>
void operator()(Args&&...) const&& = delete;
};
}
template<class F>
constexpr detail::not_fn_t<std::decay_t<F>> not_fn(F&& f)
{
return {std::forward<F>(f)};
}
|title2=(2) not_fn|ver2=2|2=
namespace detail
{
template<auto ConstFn>
struct stateless_not_fn
{
template<class... Args>
constexpr auto operator()(Args&&... args) const
noexcept(noexcept(!std::invoke(ConstFn, std::forward<Args>(args)...)))
-> decltype(!std::invoke(ConstFn, std::forward<Args>(args)...))
{
return !std::invoke(ConstFn, std::forward<Args>(args)...);
}
};
}
template<auto ConstFn>
constexpr detail::stateless_not_fn<ConstFn> not_fn() noexcept
{
if constexpr (std::is_pointer_v<decltype(ConstFn)>
std::is_member_pointer_v<decltype(ConstFn)>)
static_assert(ConstFn != nullptr);
return {};
}

## Notes

`std::not_fn` is intended to replace the C++03-era negators `std::not1` and `std::not2`.

## Example


### Example

```cpp
#include <cassert>
#include <functional>

bool is_same(int a, int b) noexcept
{
    return a == b;
}

struct S
{
    int val;
    bool is_same(int arg) const noexcept { return val == arg; }
};

int main()
{
    // Using with a free function:
    auto is_differ = std::not_fn(is_same);
    assert(is_differ(8, 8) == false); // equivalent to: !is_same(8, 8) == false
    assert(is_differ(6, 9) == true); // equivalent to: !is_same(8, 0) == true

    // Using with a member function:
    auto member_differ = std::not_fn(&S::is_same);
    assert(member_differ(S{3}, 3) == false); //: S tmp{6}; !tmp.is_same(6) == false

    // Noexcept-specification is preserved:
    static_assert(noexcept(is_differ) == noexcept(is_same));
    static_assert(noexcept(member_differ) == noexcept(&S::is_same));

    // Using with a function object:
    auto same = [](int a, int b) { return a == b; };
    auto differ = std::not_fn(same);
    assert(differ(1, 2) == true); //: !same(1, 2) == true
    assert(differ(2, 2) == false); //: !same(2, 2) == false

#if __cpp_lib_not_fn >= 202306L
    auto is_differ_cpp26 = std::not_fn<is_same>();
    assert(is_differ_cpp26(8, 8) == false);
    assert(is_differ_cpp26(6, 9) == true);

    auto member_differ_cpp26 = std::not_fn<&S::is_same>();
    assert(member_differ_cpp26(S{3}, 3) == false);

    auto differ_cpp26 = std::not_fn<same>();
    static_assert(differ_cpp26(1, 2) == true);
    static_assert(differ_cpp26(2, 2) == false);
#endif
}
```


## See also


| cpp/utility/functional/dsc not1 | (see dedicated page) |
| cpp/utility/functional/dsc not2 | (see dedicated page) |

