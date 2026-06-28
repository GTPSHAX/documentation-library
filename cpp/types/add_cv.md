---
title: std::add_const
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/add_cv
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++11|num=1|
template< class T >
struct add_cv;
dcl|since=c++11|num=2|
template< class T >
struct add_const;
dcl|since=c++11|num=3|
template< class T >
struct add_volatile;
```

Provides the member typedef `type` which is the same as `T`, except it has a cv-qualifier added (unless `T` is a function, a reference, or already has this cv-qualifier)
1. adds both `const` and `volatile`
2. adds `const`
3. adds `volatile`

## Member types


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Helper types


```cpp
dcl|since=c++14|1=
template< class T >
using add_cv_t       = typename add_cv<T>::type;
dcl|since=c++14|1=
template< class T >
using add_const_t    = typename add_const<T>::type;
dcl|since=c++14|1=
template< class T >
using add_volatile_t = typename add_volatile<T>::type;
```


## Possible implementation

eq fun
|1=
template<class T> struct add_cv { typedef const volatile T type; };
template<class T> struct add_const { typedef const T type; };
template<class T> struct add_volatile { typedef volatile T type; };

## Notes

These transformation traits can be used to establish  in template argument deduction:

```cpp
template<class T>
void f(const T&, const T&);

template<class T>
void g(const T&, std::add_const_t<T>&);

f(4.2, 0); // error, deduced conflicting types for 'T'
g(4.2, 0); // OK, calls g<double>
```


## Example


### Example

```cpp
#include <iostream>
#include <type_traits>

struct foo
{
    void m() { std::cout << "Non-cv\n"; }
    void m() const { std::cout << "Const\n"; }
    void m() volatile { std::cout << "Volatile\n"; }
    void m() const volatile { std::cout << "Const-volatile\n"; }
};

int main()
{
    foo{}.m();
    std::add_const<foo>::type{}.m();
    std::add_volatile<foo>::type{}.m();
    std::add_cv<foo>::type{}.m();
}
```


**Output:**
```
Non-cv
Const
Volatile
Const-volatile
```


## See also


| cpp/types/dsc is_const | (see dedicated page) |
| cpp/types/dsc is_volatile | (see dedicated page) |
| cpp/types/dsc remove_cv | (see dedicated page) |
| cpp/utility/dsc as_const | (see dedicated page) |

