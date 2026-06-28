---
title: std::is_const
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_const
---

cpp/types/traits/is|1=is_const
|description=If `T` is a const-qualified type (that is, `const`, or `const volatile`), provides the member constant `value` equal to `true`. For any other type, `value` is `false`.
|inherit_desc= `T` is a const-qualified type

## Notes

If `T` is a reference type then `is_const<T>::value` is always `false`. The proper way to check a potentially-reference type for constness is to remove the reference:
`is_const<typename remove_reference<T>::type>`.

## Possible implementation

eq fun
|1=
template<class T> struct is_const          : std::false_type {};
template<class T> struct is_const<const T> : std::true_type {};

## Example


### Example

```cpp
#include <type_traits>

static_assert(std::is_same_v<const int*, int const*>,
    "Remember, constness binds tightly inside pointers.");
static_assert(!std::is_const_v<int>);
static_assert(std::is_const_v<const int>);
static_assert(!std::is_const_v<int*>);
static_assert(std::is_const_v<int* const>,
    "Because the pointer itself can't be changed but the int pointed at can.");
static_assert(!std::is_const_v<const int*>,
    "Because the pointer itself can be changed but not the int pointed at.");
static_assert(!std::is_const_v<const int&>);
static_assert(std::is_const_v<std::remove_reference_t<const int&>>);

struct S
{
    void foo() const {}
    void bar() const {}
};

int main()
{
    // A const member function is const in a different way:

    static_assert(!std::is_const_v<decltype(&S::foo)>,
        "Because &S::foo is a pointer.");

    using S_mem_fun_ptr = void(S::*)() const;

    S_mem_fun_ptr sfp = &S::foo;
    sfp = &S::bar; // OK, can be re-pointed
    static_assert(!std::is_const_v<decltype(sfp)>,
        "Because sfp is the same pointer type and thus can be re-pointed.");

    const S_mem_fun_ptr csfp = &S::foo;
    // csfp = &S::bar; // Error
    static_assert(std::is_const_v<decltype(csfp)>,
        "Because csfp cannot be re-pointed.");
}
```


## See also


| cpp/types/dsc is_volatile | (see dedicated page) |
| cpp/utility/dsc as_const | (see dedicated page) |

