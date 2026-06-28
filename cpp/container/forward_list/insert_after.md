---
title: std::forward_list::insert_after
type: Containers
source: https://en.cppreference.com/w/cpp/container/forward_list/insert_after
---


```cpp
dcl|num=1|since=c++11|
iterator insert_after( const_iterator pos, const T& value );
dcl|num=2|since=c++11|
iterator insert_after( const_iterator pos, T&& value );
dcl|num=3|since=c++11|
iterator insert_after( const_iterator pos, size_type count, const T& value );
dcl|num=4|since=c++11|
template< class InputIt >
iterator insert_after( const_iterator pos, InputIt first, InputIt last );
dcl|num=5|since=c++11|
iterator insert_after( const_iterator pos, std::initializer_list<T> ilist );
```

Inserts elements after the specified position in the container.
@1,2@ Inserts `value` after the element pointed to by `pos`.
3. Inserts `count` copies of the `value` after the element pointed to by `pos`.
4. Inserts elements from range [first, last) after the element pointed to by `pos`.
The behavior is undefined if `first` and `last` are iterators into `*this`.
5. Inserts elements from initializer list `ilist`.

## Parameters


### Parameters

- `pos` - iterator after which the content will be inserted
- `value` - element value to insert
- `count` - number of copies to insert
- `[3=to insert, range=source}})` - 
- `ilist` - initializer list to insert the values from

**Type requirements:**

- `InputIt`

## Return value

@1,2@ Iterator to the inserted element.
3. Iterator to the last element inserted, or `pos` if `1=count == 0`.
4. Iterator to the last element inserted, or `pos` if `1=first == last`.
5. Iterator to the last element inserted, or `pos` if `ilist` is empty.

## Exceptions


## Complexity

@1,2@ Constant.
3. Linear in `count`.
4. Linear in `std::distance(first, last)`.
5. Linear in `ilist.size()`.

## Example


### Example

```cpp
#include <forward_list>
#include <iostream>
#include <string>
#include <vector>

void print(const std::forward_list<int>& list)
{
    std::cout << "list: {";
    for (char comma[3] = {'\0', ' ', '\0'}; int i : list)
    {
        std::cout << comma << i;
        comma[0] = ',';
    }
    std::cout << "}\n";
}

int main()
{
    std::forward_list<int> ints{1, 2, 3, 4, 5};
    print(ints);

    // insert_after (2)
    auto beginIt = ints.begin();
    ints.insert_after(beginIt, -6);
    print(ints);

    // insert_after (3)
    auto anotherIt = beginIt;
    ++anotherIt;
    anotherIt = ints.insert_after(anotherIt, 2, -7);
    print(ints);

    // insert_after (4)
    const std::vector<int> v = {-8, -9, -10};
    anotherIt = ints.insert_after(anotherIt, v.cbegin(), v.cend());
    print(ints);

    // insert_after (5)
    ints.insert_after(anotherIt, {-11, -12, -13, -14});
    print(ints);
}
```


**Output:**
```
list: {1, 2, 3, 4, 5}
list: {1, -6, 2, 3, 4, 5}
list: {1, -6, -7, -7, 2, 3, 4, 5}
list: {1, -6, -7, -7, -8, -9, -10, 2, 3, 4, 5}
list: {1, -6, -7, -7, -8, -9, -10, -11, -12, -13, -14, 2, 3, 4, 5}
```


## See also


| cpp/container/dsc emplace after|forward_list | (see dedicated page) |
| cpp/container/dsc push_front|forward_list | (see dedicated page) |

