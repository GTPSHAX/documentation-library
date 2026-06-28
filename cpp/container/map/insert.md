---
title: std::map::insert
type: Containers
source: https://en.cppreference.com/w/cpp/container/map/insert
---


```cpp
dcl|num=1|
std::pair<iterator, bool> insert( const value_type& value );
dcl|num=2|since=c++11|
template< class P >
std::pair<iterator, bool> insert( P&& value );
dcl|num=3|since=c++17|
std::pair<iterator, bool> insert( value_type&& value );
dcl rev multi|num=4|until1=c++11|
|dcl1=
iterator insert( iterator pos, const value_type& value );
|dcl2=
iterator insert( const_iterator pos, const value_type& value );
dcl|num=5|since=c++11|
template< class P >
iterator insert( const_iterator pos, P&& value );
dcl|num=6|since=c++17|
iterator insert( const_iterator pos, value_type&& value );
dcl|num=7|
template< class InputIt >
void insert( InputIt first, InputIt last );
dcl|num=8|since=c++11|
void insert( std::initializer_list<value_type> ilist );
dcl|num=9|since=c++17|
insert_return_type insert( node_type&& nh );
dcl|num=10|since=c++17|
iterator insert( const_iterator pos, node_type&& nh );
```

Inserts element(s) into the container, if the container doesn't already contain an element with an equivalent key.
@1-3@ Inserts `value`.
@@ Overload  is equivalent to `emplace(std::forward<P>(value))` and only participates in overload resolution if `1=std::is_constructible<value_type, P&&>::value == true`.
@4-6@ Inserts `value` in the position as close as possible to the position just prior to `pos`.
@@ Overload  is equivalent to `emplace_hint(hint, std::forward<P>(value))` and only participates in overload resolution if `1=std::is_constructible<value_type, P&&>::value == true`.
7. Inserts elements from range [first, last).
8. Inserts elements from initializer list `ilist`.

## Parameters


### Parameters

- `pos` - iterator to the position before which the new element will be inserted
- `value` - element value to insert
- `ilist` - initializer list to insert the values from
- `nh` - a compatible node handle

**Type requirements:**

- `InputIt`

## Return value

@1-3@
@4-6@
@7,8@ (none)

## Exceptions

@1-6@ If an exception is thrown by any operation, the insertion has no effect.

## Complexity

@1-3@ Logarithmic in the size of the container, `O(log(size()))`.
@4-6@ Amortized constant if the insertion happens in the position just <sup>(until C++11)</sup> ''after''<sup>(since C++11)</sup> ''before'' `pos`, logarithmic in the size of the container otherwise.
@7,8@ `O(N&middot;log(size() + N))`, where `N` is the number of elements to insert.
9. Logarithmic in the size of the container, `O(log(size()))`.
10. Amortized constant if the insertion happens in the position just ''before'' `pos`, logarithmic in the size of the container otherwise.

## Notes


## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <map>
#include <string>
using namespace std::literals;

template<typename It>
void print_insertion_status(It it, bool success)
{
    std::cout << "Insertion of " << it->first
              << (success ? " succeeded\n" : " failed\n");
}

int main()
{
    std::map<std::string, float> heights;

    // Overload 3: insert from rvalue reference
    const auto [it_hinata, success] = heights.insert({"Hinata"s, 162.8});
    print_insertion_status(it_hinata, success);

    {
        // Overload 1: insert from lvalue reference
        const auto [it, success2] = heights.insert(*it_hinata);
        print_insertion_status(it, success2);
    }
    {
        // Overload 2: insert via forwarding to emplace
        const auto [it, success] = heights.insert(std::pair{"Kageyama", 180.6});
        print_insertion_status(it, success);
    }
    {
        // Overload 6: insert from rvalue reference with positional hint
        const std::size_t n = std::size(heights);
        const auto it = heights.insert(it_hinata, {"Azumane"s, 184.7});
        print_insertion_status(it, std::size(heights) != n);
    }
    {
        // Overload 4: insert from lvalue reference with positional hint
        const std::size_t n = std::size(heights);
        const auto it = heights.insert(it_hinata, *it_hinata);
        print_insertion_status(it, std::size(heights) != n);
    }
    {
        // Overload 5: insert via forwarding to emplace with positional hint
        const std::size_t n = std::size(heights);
        const auto it = heights.insert(it_hinata, std::pair{"Tsukishima", 188.3});
        print_insertion_status(it, std::size(heights) != n);
    }

    auto node_hinata = heights.extract(it_hinata);
    std::map<std::string, float> heights2;

    // Overload 7: insert from iterator range
    heights2.insert(std::begin(heights), std::end(heights));

    // Overload 8: insert from initializer_list
    heights2.insert({{"Kozume"s, 169.2}, {"Kuroo", 187.7
```

// Overload 9: insert node
const auto status = heights2.insert(std::move(node_hinata));
print_insertion_status(status.position, status.inserted);
node_hinata = heights2.extract(status.position);
{
// Overload 10: insert node with positional hint
const std::size_t n = std::size(heights2);
const auto it = heights2.insert(std::begin(heights2), std::move(node_hinata));
print_insertion_status(it, std::size(heights2) != n);
}
// Print resulting map
std::cout << std::left << '\n';
for (const auto& [name, height] : heights2)
std::cout << std::setw(10) << name << " | " << height << "cm\n";
}
|output=
Insertion of Hinata succeeded
Insertion of Hinata failed
Insertion of Kageyama succeeded
Insertion of Azumane succeeded
Insertion of Hinata failed
Insertion of Tsukishima succeeded
Insertion of Hinata succeeded
Insertion of Hinata succeeded
Azumane    | 184.7cm
Hinata     | 162.8cm
Kageyama   | 180.6cm
Kozume     | 169.2cm
Kuroo      | 187.7cm
Tsukishima | 188.3cm

## Defect reports


## See also


| cpp/container/dsc emplace|map | (see dedicated page) |
| cpp/container/dsc emplace_hint|map | (see dedicated page) |
| cpp/container/dsc insert_or_assign|map | (see dedicated page) |
| cpp/iterator/dsc inserter | (see dedicated page) |

