---
title: std::tuple
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/tuple
---


```cpp
**Header:** `<`tuple`>`
dcl|since=c++11|1=
template< class... Types >
class tuple;
```

Class template `std::tuple` is a fixed-size collection of heterogeneous values. It is a generalization of `std::pair`.
If `std::is_trivially_destructible<Ti>::value` is `true` for every `Ti` in `Types`, the destructor of `std::tuple` is trivial.
If a program declares an explicit or partial specialization of `std::tuple`, the program is ill-formed, no diagnostic required.

## Template parameters


### Parameters

- `Types...` - the types of the elements that the tuple stores. Empty list is supported.

## Member functions


| cpp/utility/tuple/dsc constructor | (see dedicated page) |
| cpp/utility/tuple/dsc operator{{= | (see dedicated page) |
| cpp/utility/tuple/dsc swap | (see dedicated page) |


## Non-member functions


| cpp/utility/tuple/dsc make_tuple | (see dedicated page) |
| cpp/utility/tuple/dsc tie | (see dedicated page) |
| cpp/utility/tuple/dsc forward_as_tuple | (see dedicated page) |
| cpp/utility/tuple/dsc tuple_cat | (see dedicated page) |
| cpp/utility/tuple/dsc get | (see dedicated page) |
| cpp/utility/tuple/dsc operator_cmp | (see dedicated page) |
| cpp/utility/tuple/dsc swap2 | (see dedicated page) |


## Helper concepts


| cpp/utility/tuple/dsc tuple-like | (see dedicated page) |


## Helper classes


| cpp/utility/tuple/dsc tuple_size | (see dedicated page) |
| cpp/utility/tuple/dsc tuple_element | (see dedicated page) |
| cpp/utility/tuple/dsc uses_allocator | (see dedicated page) |
| cpp/utility/tuple/dsc basic_common_reference | (see dedicated page) |
| cpp/utility/tuple/dsc common_type | (see dedicated page) |
| cpp/utility/format/dsc tuple_formatter|tuple | (see dedicated page) |
| cpp/utility/tuple/dsc ignore | (see dedicated page) |


## Helper specializations


```cpp
dcl|since=c++23|1=
template< class... Ts >
constexpr bool enable_nonlocking_formatter_optimization<std::tuple<Ts...>>
= (enable_nonlocking_formatter_optimization<Ts> && ...);
```

This specialization of  enables efficient implementation of  and  for printing a `tuple` object when each element type enables it.

## <sup>(C++17)</sup>


## Notes

Since the "shape" of a tuple – its size, the types of its elements, and the ordering of those types – are part of its type signature, they must all be available at compile time and can only depend on other compile-time information. This means that many conditional operations on tuples – in particular, conditional prepend/append and filter – are only possible if the conditions can be evaluated at compile time. For example, given a `std::tuple<int, double, int>`, it is possible to filter on types – e.g. returning a `std::tuple<int, int>` – but not to filter on whether or not each element is positive (which would have a different type signature depending on runtime values of the tuple), unless all the elements were themselves `constexpr`.
As a workaround, one can work with tuples of `std::optional`, but there is still no way to adjust the size based on runtime information.
Until  (applied as a defect report for C++11), a function could not return a tuple using copy-list-initialization:

```cpp
std::tuple<int, int> foo_tuple()
{
    return {1, -1};  // Error until N4387
    return std::tuple<int, int>{1, -1}; // Always works
    return std::make_tuple(1, -1); // Always works
}
```


## Example


### Example

```cpp
#include <iostream>
#include <stdexcept>
#include <string>
#include <tuple>

std::tuple<double, char, std::string> get_student(int id)
{
    switch (id)
    {
        case 0: return {3.8, 'A', "Lisa Simpson"};
        case 1: return {2.9, 'C', "Milhouse Van Houten"};
        case 2: return {1.7, 'D', "Ralph Wiggum"};
        case 3: return {0.6, 'F', "Bart Simpson"};
    }

    throw std::invalid_argument("id");
}

int main()
{
    const auto student0 = get_student(0);
    std::cout << "ID: 0, "
              << "GPA: " << std::get<0>(student0) << ", "
              << "grade: " << std::get<1>(student0) << ", "
              << "name: " << std::get<2>(student0) << '\n';

    const auto student1 = get_student(1);
    std::cout << "ID: 1, "
              << "GPA: " << std::get<double>(student1) << ", "
              << "grade: " << std::get<char>(student1) << ", "
              << "name: " << std::get<std::string>(student1) << '\n';

    double gpa2;
    char grade2;
    std::string name2;
    std::tie(gpa2, grade2, name2) = get_student(2);
    std::cout << "ID: 2, "
              << "GPA: " << gpa2 << ", "
              << "grade: " << grade2 << ", "
              << "name: " << name2 << '\n';

    // C++17 structured binding:
    const auto [gpa3, grade3, name3] = get_student(3);
    std::cout << "ID: 3, "
              << "GPA: " << gpa3 << ", "
              << "grade: " << grade3 << ", "
              << "name: " << name3 << '\n';
}
```


**Output:**
```
ID: 0, GPA: 3.8, grade: A, name: Lisa Simpson
ID: 1, GPA: 2.9, grade: C, name: Milhouse Van Houten
ID: 2, GPA: 1.7, grade: D, name: Ralph Wiggum
ID: 3, GPA: 0.6, grade: F, name: Bart Simpson
```


## Defect reports


## References


## See also


| cpp/utility/dsc pair | (see dedicated page) |

