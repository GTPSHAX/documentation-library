---
title: std::decay
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/decay
---

ddcl|header=type_traits|since=c++11|
template< class T >
struct decay;
Performs the type conversions equivalent to the ones performed when passing function arguments by value. Formally:
* If `T` is “array of `U`” or reference to it, the member typedef `type` is `U*`.
* Otherwise, if `T` is a function type `F` or reference to one, the member typedef `type` is `std::add_pointer<F>::type`.
* Otherwise, the member typedef `type` is `std::remove_cv<std::remove_reference<T>::type>::type`.

## Member types


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Helper types

ddcl|since=c++14|1=
template< class T >
using decay_t = typename decay<T>::type;

## Possible implementation

eq fun|1=
template<class T>
struct decay
{
private:
typedef typename std::remove_reference<T>::type U;
public:
typedef typename std::conditional<
std::is_array<U>::value,
typename std::add_pointer<typename std::remove_extent<U>::type>::type,
typename std::conditional<
std::is_function<U>::value,
typename std::add_pointer<U>::type,
typename std::remove_cv<U>::type
>::type
>::type type;
};

## Example


### Example

```cpp
#include <type_traits>

template<typename T, typename U>
constexpr bool is_decay_equ = std::is_same_v<std::decay_t<T>, U>;

static_assert
(
    is_decay_equ<int, int> &&
    ! is_decay_equ<int, float> &&
    is_decay_equ<int&, int> &&
    is_decay_equ<int&&, int> &&
    is_decay_equ<const int&, int> &&
    is_decay_equ<int[2], int*> &&
    ! is_decay_equ<int[4][2], int*> &&
    ! is_decay_equ<int[4][2], int**> &&
    is_decay_equ<int[4][2], int(*)[2]> &&
    is_decay_equ<int(int), int(*)(int)>
);

int main() {}
```


## See also


| cpp/types/dsc remove_cvref | (see dedicated page) |

