---
title: std::list::splice
type: Containers
source: https://en.cppreference.com/w/cpp/container/list/splice
---


```cpp
dcl|num=1|
void splice( const_iterator pos, list& other );
dcl|num=2|since=c++11|
void splice( const_iterator pos, list&& other );
dcl|num=3|
void splice( const_iterator pos, list& other, const_iterator it );
dcl|num=4|since=c++11|
void splice( const_iterator pos, list&& other, const_iterator it );
dcl|num=5|
void splice( const_iterator pos, list& other,
const_iterator first, const_iterator last);
dcl|num=6|since=c++11|
void splice( const_iterator pos, list&& other,
const_iterator first, const_iterator last );
```

Transfers elements from one list to another.
No elements are copied or moved, only the internal pointers of the list nodes are re-pointed. No iterators or references become invalidated, the iterators to moved elements remain valid, but now refer into `*this`, not into `other`.
@1,2@ Transfers all elements from `other` into `*this`. The elements are inserted before the element pointed to by `pos`. The container `other` becomes empty after the operation.
@3,4@ Transfers the element pointed to by `it` from `other` into `*this`. The element is inserted before the element pointed to by `pos`.
@5,6@ Transfers the elements in the range [first, last) from `other` into `*this`. The elements are inserted before the element pointed to by `pos`.
The behavior is undefined if
* `1=get_allocator() != other.get_allocator()`,
* for overloads , `*this` and `other` refer to the same object,
* for overloads , `it` is not a dereferenceable iterator into `other`, or
* for overloads ,
:* [first, last) is not a valid range in `other`, or
:* `pos` is in [first, last).

## Parameters


### Parameters

- `pos` - element before which the content will be inserted
- `other` - another container to transfer the content from
- `it` - the element to transfer from `other` to `*this`
- `[3=to transfer from {{c, other}} to {{c)` - 

## Return value

(none)

## Exceptions

Throws nothing.

## Complexity

@1-4@ Constant.
@5,6@ Constant if `other` refers to the same object as `*this`, otherwise linear in `std::distance(first, last)`.

## Example


### Example

```cpp
#include <iostream>
#include <list>

std::ostream& operator<<(std::ostream& ostr, const std::list<int>& list)
{
    for (auto& i : list)
        ostr << ' ' << i;

    return ostr;
}

int main ()
{
    std::list<int> list1{1, 2, 3, 4, 5};
    std::list<int> list2{10, 20, 30, 40, 50};

    auto it = list1.begin();
    std::advance(it, 2);

    list1.splice(it, list2);

    std::cout << "list1:" << list1 << '\n';
    std::cout << "list2:" << list2 << '\n';

    list2.splice(list2.begin(), list1, it, list1.end());

    std::cout << "list1:" << list1 << '\n';
    std::cout << "list2:" << list2 << '\n';
}
```


**Output:**
```
list1: 1 2 10 20 30 40 50 3 4 5
list2:
list1: 1 2 10 20 30 40 50
list2: 3 4 5
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-250 | C++98 | references and iterators to the moved<br>element(s) were all invalidated | they refer or point to the<br>same element(s) in c |


## See also


| cpp/container/dsc merge|list | (see dedicated page) |
| cpp/container/dsc remove|list | (see dedicated page) |

