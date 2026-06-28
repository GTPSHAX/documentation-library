---
title: std::unique_ptr::operator[]
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/unique_ptr/operator_at
---


```cpp
|1=
T& operator[]( std::size_t i ) const;
```

`operator[]` provides access to elements of an array managed by a `unique_ptr`.
The parameter `i` shall be less than the number of elements in the array; otherwise, the behavior is undefined.
This member function is only provided for specializations for array types.

## Parameters


### Parameters

- `i` - the index of the element to be returned

## Return value

Returns the element at index `i`, i.e. `get()[i]`.

## Example


### Example

```cpp
#include <iostream>
#include <memory>

int main() 
{
    const int size = 10; 
    std::unique_ptr<int[]> fact(new int[size]);

    for (int i = 0; i < size; ++i)
        fact[i] = (i == 0) ? 1 : i * fact[i - 1];

    for (int i = 0; i < size; ++i)
        std::cout << i << "! = " << fact[i] << '\n';
}
```


**Output:**
```
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040
8! = 40320
9! = 362880
```


## See also


| cpp/memory/unique_ptr/dsc get | (see dedicated page) |

