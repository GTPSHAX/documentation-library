---
title: std::generator
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/generator
---


```cpp
**Header:** `<`generator`>`
dcl|num=1|since=c++23|1=
template<
class Ref,
class V = void,
class Allocator = void >
class generator
: public ranges::view_interface<generator<Ref, V, Allocator>>
dcl|num=2|since=c++23|1=
namespace pmr {
template< class Ref, class V = void >
using generator =
std::generator<Ref, V, std::pmr::polymorphic_allocator<>>;
}
```

1. The class template `std::generator` presents a  of the elements yielded by the evaluation of a .
2. Convenience alias template for the `generator` using the .
A `std::generator` generates a sequence of elements by repeatedly resuming the coroutine from which it was returned.
Each time a `co_yield` statement is evaluated, the coroutine produces one element of the sequence.
When the `co_yield` statement is of the form `co_yield ranges::elements_of(rng)`, each element of the  `rng` is successively produced as an element of the sequence.
`std::generator` models  and .
The behavior of a program that adds a specialization for `std::generator` is undefined.

## Template parameters


### Parameters

- `Ref` - the reference type (`ranges::range_reference_t`) of the generator. If `V` is `void`, both the reference type and the value type are inferred from `Ref`
- `V` - the value type (`ranges::range_value_t`) of the generator, or `void`
- `Allocator` - an allocator type or `void`
If `Allocator` is not `void`, then the behavior is undefined if `Allocator` does not meet the *Allocator* requirements.

## Member types


| Item | Description |
|------|-------------|
| **Member** | Definition |


### Parameters


**Type requirements:**

- *  is modeled.
- *  is modeled.
- *  is modeled.
The program is ill-formed if any of these type requirements is not satisfied.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |
| dsc expos mem obj|active_|id=active|private=yes| | |
| Internally, each active instance of `std::generator` is associated with a stack (handled as if by object of type `std::unique_ptr<std::stack<std::coroutine_handle<>>>`). | |
| * When  is called, a new stack is created and the generator is added to the stack. | |
| * When `co_yield ranges::elements_of(rng)` is evaluated in a generator body, `rng` is converted to a generator and added to the stack that contains the enclosing generator. | |
| * When a generator iterator is , the coroutine at the top of the associated stack is resumed. | |
| * When a generator finishes (i.e. when  is called), it is removed from the stack. | |


## Member functions


| cpp/coroutine/generator/dsc constructor | (see dedicated page) |
| cpp/coroutine/generator/dsc destructor | (see dedicated page) |
| cpp/coroutine/generator/dsc operator{{= | (see dedicated page) |
| cpp/coroutine/generator/dsc begin | (see dedicated page) |
| cpp/coroutine/generator/dsc end | (see dedicated page) |


## Nested classes


## Notes


## Example


### Example

```cpp
#include <generator>
#include <iostream>

template<typename T>
struct Tree
{
    T value;
    Tree *left{}, *right{};

    std::generator<const T&> traverse_inorder() const
    {
        if (left)
            co_yield std::ranges::elements_of(left->traverse_inorder());

        co_yield value;

        if (right)
            co_yield std::ranges::elements_of(right->traverse_inorder());
    }
};

int main()
{
    Tree<char> tree[]
    {
                                    {'D', tree + 1, tree + 2},
        //                            │
        //            ┌───────────────┴────────────────┐
        //            │                                │
                    {'B', tree + 3, tree + 4},       {'F', tree + 5, tree + 6},
        //            │                                │
        //  ┌─────────┴─────────────┐      ┌───────────┴─────────────┐
        //  │                       │      │                         │
          {'A'},                  {'C'}, {'E'},                    {'G'}
    };

    for (char x : tree->traverse_inorder())
        std::cout << x << ' ';
    std::cout << '\n';
}
```


**Output:**
```
A B C D E F G
```


## References


## See also


| cpp/coroutine/dsc noop_coroutine | (see dedicated page) |

