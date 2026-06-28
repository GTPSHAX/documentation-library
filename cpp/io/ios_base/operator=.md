---
title: std::ios_base::operator=
type: Input/output
source: https://en.cppreference.com/w/cpp/io/ios_base/operator=
---


```cpp
dcl rev multi|until1=c++11|dcl1=
private:
ios_base& operator=( const ios_base& );
|dcl2=
public:
ios_base& operator=( const ios_base& ) = delete;
```

The copy assignment operator is <sup>(until C++11)</sup> private<sup>(since C++11)</sup> deleted: streams are not copy-assignable.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-50 | C++98 | the copy assignment operator was not specified | specified as private |

