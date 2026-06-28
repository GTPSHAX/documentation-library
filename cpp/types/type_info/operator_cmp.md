---
title: std::type_info::operators
type: Utilities
source: https://en.cppreference.com/w/cpp/types/type_info/operator_cmp
---


```cpp
dcla|anchor=no|num=1|noexcept=c++11|constexpr=c++23|1=
bool operator==( const type_info& rhs ) const;
dcla|anchor=no|num=2|noexcept=c++11|until=c++20|1=
bool operator!=( const type_info& rhs ) const;
```

Checks if the objects refer to the same types.
rrev|since=c++20|

## Parameters


### Parameters

- `rhs` - another type information object to compare to

## Return value

`true` if the comparison operation holds true, `false` otherwise.

## Notes


## Example


### Example

```cpp
#include <iostream>
#include <string>
#include <typeinfo>
#include <utility>

class person
{
public:
    explicit person(std::string n) : name_(std::move(n)) {}
    virtual const std::string& name() const { return name_; }

private:
    std::string name_;
};

class employee : public person
{
public:
    employee(std::string n, std::string p)
        : person(std::move(n)), profession_(std::move(p)) {}

    const std::string& profession() const { return profession_; }

private:
    std::string profession_;
};

void print_info(const person& p)
{
    if (typeid(person) == typeid(p))
        std::cout << p.name() << " is not an employee\n";
    else if (typeid(employee) == typeid(p))
    {
        std::cout << p.name() << " is an employee ";
        auto& emp = dynamic_cast<const employee&>(p);
        std::cout << "who works in " << emp.profession() << '\n';
    }
}

int main()
{
    print_info(employee{"Paul","Economics"});
    print_info(person{"Kate"});

#if __cpp_lib_constexpr_typeinfo
    if constexpr (typeid(employee) != typeid(person)) // C++23
        std::cout << "class `employee` != class `person`\n";
#endif
}
```


**Output:**
```
Paul is an employee who works in Economics
Kate is not an employee
class `employee` != class `person`
```


## See also


| cpp/types/type_info/dsc before | (see dedicated page) |

