---
title: std::weak_ptr::~weak_ptr
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/weak_ptr/~weak_ptr
---

ddcla|since=c++11|constexpr=c++26|
~weak_ptr();
Destroys the `weak_ptr` object. Results in no effect to the managed object.

## Example


### Example

```cpp
#include <iostream>
#include <memory>
#include <variant>

class Node
{
    char id;
    std::variant<std::weak_ptr<Node>, std::shared_ptr<Node>> ptr;
public:
    Node(char id) : id{id} {}
    ~Node() { std::cout << "  '" << id << "' reclaimed\n"; }
    /*...*/
    void assign(std::weak_ptr<Node> p) { ptr = p; }
    void assign(std::shared_ptr<Node> p) { ptr = p; }
};

enum class shared { all, some };

void test_cyclic_graph(const shared x)
{
    auto A = std::make_shared<Node>('A');
    auto B = std::make_shared<Node>('B');
    auto C = std::make_shared<Node>('C');

    A->assign(B);
    B->assign(C);

    if (shared::all == x)
    {
        C->assign(A);
        std::cout << "All links are shared pointers";
    }
    else
    {
        C->assign(std::weak_ptr<Node>(A));
        std::cout << "One link is a weak_ptr";
    }
    /*...*/
    std::cout << "\nLeaving...\n";
}

int main()
{
    test_cyclic_graph(shared::some);
    test_cyclic_graph(shared::all); // produces a memory leak
}
```


**Output:**
```
One link is a weak_ptr
Leaving...
  'A' reclaimed
  'B' reclaimed
  'C' reclaimed
All links are shared pointers
Leaving...
```


## See also


| cpp/memory/shared_ptr/dsc destructor | (see dedicated page) |

