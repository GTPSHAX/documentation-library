---
title: constinit specifier
type: Language
source: https://en.cppreference.com/w/cpp/language/constinit
---


# tt|constinit

:* **`constinit`** - asserts that a variable has static initialization, i.e. `zero initialization` and `constant initialization`, otherwise the program is ill-formed.

## Explanation

The `constinit` specifier declares a variable with static or thread `storage duration`.
rrev|since=c++26|
The `constinit` specifier can also be applied to `structured binding` declarations. In this case, `constinit` is also applied to the `uniquely-named variable` introduced by the declaration.
If a variable is declared with `constinit`, its `initializing declaration` must be applied with `constinit`. If a variable declared with `constinit` has `dynamic initialization` (even if it is `performed as static initialization`), the program is ill-formed.
If no `constinit` declaration is reachable at the point of the initializing declaration, the program is ill-formed, no diagnostic required.
`constinit` cannot be used together with `constexpr`. When the declared variable is a reference, `constinit` is equivalent to `constexpr`. When the declared variable is an object, `constexpr` mandates that the object must have static initialization and constant destruction and makes the object const-qualified, however, `constinit` does not mandate constant destruction and const-qualification. As a result, an object of a type which has constexpr constructors and no constexpr destructor (e.g. `std::shared_ptr<T>`) might be declared with `constinit` but not `constexpr`.

```cpp
const char* g() { return "dynamic initialization"; }
constexpr const char* f(bool p) { return p ? "constant initializer" : g(); }

constinit const char* c = f(true);     // OK
// constinit const char* d = f(false); // error
```

`constinit` can also be used in a non-initializing declaration to tell the compiler that a `thread_local` variable is already initialized, `reducing overhead` that would otherwise be incurred by a hidden guard variable.

```cpp
extern thread_local constinit int x;
int f() { return x; } // no check of a guard variable needed
```


## Notes


## Keywords

`cpp/keyword/constinit`

## Example


### Example

```cpp
#include <cassert>

constexpr int square(int i)
{
    return i * i;
}

int twice(int i)
{
    return i + i;
}

constinit int sq = square(2);    // OK: initialization is done at compile time
// constinit int x_x = twice(2); // Error: compile time initializer required

int square_4_gen()
{
    static constinit int pow = square(4);

    // constinit int prev = pow; // Error: constinit can only be applied to a
                                 // variable with static or thread storage duration
    int prev = pow;
    pow = pow * pow;
    return prev;
}

int main()
{
    assert(sq == 4);
    sq = twice(1); // Unlike constexpr this value can be changed later at runtime
    assert(sq == 2);

    assert(square_4_gen() == 16);
    assert(square_4_gen() == 256);
    assert(square_4_gen() == 65536);
}
```


## Defect reports


## See also


| cpp/language/dsc consteval | (see dedicated page) |
| cpp/language/dsc constexpr | (see dedicated page) |

