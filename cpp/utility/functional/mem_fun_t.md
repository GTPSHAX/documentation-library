---
title: std::mem_fun_t
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/mem_fun_t
---


```cpp
dcl | deprecated=c++11 | until=c++17  | num=1 |
template< class S, class T >
class mem_fun_t : public unary_function<T*,S> {
public:
explicit mem_fun_t(S (T::*p)());
S operator()(T* p) const;
};
dcl | deprecated=c++11 | until=c++17  | num=2 |
template< class S, class T >
class const_mem_fun_t : public unary_function<const T*,S> {
public:
explicit const_mem_fun_t(S (T::*p)() const);
S operator()(const T* p) const;
};
dcl | deprecated=c++11 | until=c++17  | num=3 |
template< class S, class T, class A >
class mem_fun1_t : public binary_function<T*,A,S> {
public:
explicit mem_fun1_t(S (T::*p)(A));
S operator()(T* p, A x) const;
};
dcl | deprecated=c++11 | until=c++17  | num=4 |
template< class S, class T, class A >
class const_mem_fun1_t : public binary_function<const T*,A,S> {
public:
explicit const_mem_fun1_t(S (T::*p)(A) const);
S operator()(const T* p, A x) const;
};
```

Wrapper around a member function pointer. The class instance whose member function to call is passed as a pointer to the `operator()`.
1. Wraps a non-const member function with no parameters.
2. Wraps a const member function with no parameters.
3. Wraps a non-const member function with a single parameter.
4. Wraps a const member function with a single parameter.

## See also

de:cpp/utility/functional/mem fun t
es:cpp/utility/functional/mem fun t
fr:cpp/utility/functional/mem fun t
it:cpp/utility/functional/mem fun t
ja:cpp/utility/functional/mem fun t
pt:cpp/utility/functional/mem fun t
ru:cpp/utility/functional/mem fun t
zh:cpp/utility/functional/mem fun t
