---
title: std::ios_base::ios_base
type: Input/output
source: https://en.cppreference.com/w/cpp/io/ios_base/ios_base
---


```cpp
dcl rev multi|num=1|until1=c++11|dcl1=
private:
ios_base( const ios_base& );
|dcl2=
public:
ios_base( const ios_base& ) = delete;
dcl|num=2|
protected:
ios_base();
```

1. The copy constructor is <sup>(until C++11)</sup> private<sup>(since C++11)</sup> deleted: streams are not copyable.
2. The default constructor is protected: only derived classes may construct `std::ios_base`. The internal state is undefined after the construction. The derived class must call  to complete initialization before first use or before destructor; otherwise the behavior is undefined.

## Notes

The same applies to the constructors of the next class in the I/O hierarchy, `std::basic_ios`. Further-derived classes (`std::istream` and `std::ostream`) are always constructed with a concrete stream buffer object and call , possibly more than once, to complete initialization of their virtual base.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-50 | C++98 | the copy constructor was not specified | specified as private |
| lwg-1249 | C++98 | initialization did not need to be completed before first use | also needs to be completed |

