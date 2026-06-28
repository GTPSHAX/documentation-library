---
title: std::ranges::view_interface
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/view_interface
---

ddcl|header=ranges|since=c++20|1=
template< class D >
requires std::is_class_v<D> && std::same_as<D, std::remove_cv_t<D>>
class view_interface;
`std::ranges::view_interface` is a helper class template for defining a view interface.
`view_interface` is typically used with CRTP:

```cpp
class my_view : public std::ranges::view_interface<my_view>
{
public:
    auto begin() const { /*...*/ }
    auto end() const { /*...*/ }
    // empty() is provided if begin() returns a forward iterator
    // and end() returns a sentinel for it.
};
```


## Member functions


| cpp/ranges/view_interface/dsc empty | (see dedicated page) |
| cpp/ranges/view_interface/dsc cbegin | (see dedicated page) |
| cpp/ranges/view_interface/dsc cend | (see dedicated page) |
| cpp/ranges/view_interface/dsc operator bool | (see dedicated page) |
| cpp/ranges/view_interface/dsc data | (see dedicated page) |
| cpp/ranges/view_interface/dsc size | (see dedicated page) |
| cpp/ranges/view_interface/dsc front | (see dedicated page) |
| cpp/ranges/view_interface/dsc back | (see dedicated page) |
| cpp/ranges/view_interface/dsc operator at | (see dedicated page) |


## Example


### Example

```cpp
#include <iostream>
#include <ranges>
#include <vector>

template<class T, class A>
class VectorView : public std::ranges::view_interface<VectorView<T, A>>
{
public:
    VectorView() = default;

    VectorView(const std::vector<T, A>& vec) :
        m_begin(vec.cbegin()), m_end(vec.cend())
    {}

    auto begin() const { return m_begin; }

    auto end() const { return m_end; }

private:
    typename std::vector<T, A>::const_iterator m_begin{}, m_end{};
};

int main()
{
    std::vector<int> v = {1, 4, 9, 16};

    VectorView view_over_v{v};

    // We can iterate with begin() and end().
    for (int n : view_over_v)
        std::cout << n << ' ';
    std::cout << '\n';

    // We get operator[] for free when inheriting from view_interface
    // since we satisfy the random_access_range concept.
    for (std::ptrdiff_t i = 0; i != view_over_v.size(); ++i)
        std::cout << "v[" << i << "] = " << view_over_v[i] << '\n';
}
```


**Output:**
```
1 4 9 16
v[0] = 1
v[1] = 4
v[2] = 9
v[3] = 16
```


## Defect reports


## See also


| cpp/ranges/dsc subrange | (see dedicated page) |

