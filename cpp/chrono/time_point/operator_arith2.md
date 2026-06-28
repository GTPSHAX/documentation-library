---
title: operators (std::chrono::time_point)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/time_point/operator_arith2
---


# operator+, operator-dsc small|(std::chrono::time_point)


```cpp
**Header:** `<`chrono`>`
dcl rev multi|num=1|since1=c++11|until1=c++14|dcl1=
template< class C, class D1, class R2, class P2 >
time_point<C, typename std::common_type<D1, duration<R2,P2>>::type>
operator+( const time_point<C,D1>& pt,
const duration<R2,P2>& d );
|dcl2=
template< class C, class D1, class R2, class P2 >
constexpr time_point<C, std::common_type_t<D1, duration<R2,P2>>>
operator+( const time_point<C,D1>& pt,
const duration<R2,P2>& d );
dcl rev multi|num=2|since1=c++11|until1=c++14|dcl1=
template< class R1, class P1, class C, class D2 >
time_point<C, typename std::common_type<duration<R1,P1>,D2>::type>
operator+( const duration<R1,P1>& d,
const time_point<C,D2>& pt );
|dcl2=
template< class R1, class P1, class C, class D2 >
constexpr time_point<C, std::common_type_t<duration<R1,P1>,D2>>
operator+( const duration<R1,P1>& d,
const time_point<C,D2>& pt );
dcl rev multi|num=3|since1=c++11|until1=c++14|dcl1=
template< class C, class D1, class R2, class P2 >
time_point<C, typename std::common_type<D1, duration<R2,P2>>::type>
operator-( const time_point<C,D1>& pt,
const duration<R2,P2>& d );
|dcl2=
template< class C, class D1, class R2, class P2 >
constexpr time_point<C, std::common_type_t<D1, duration<R2,P2>>>
operator-( const time_point<C,D1>& pt,
const duration<R2,P2>& d );
dcl rev multi|num=4|since1=c++11|until1=c++14|dcl1=
template< class C, class D1, class D2 >
typename std::common_type<D1,D2>::type
operator-( const time_point<C,D1>& pt_lhs,
const time_point<C,D2>& pt_rhs );
|dcl2=
template< class C, class D1, class D2 >
constexpr std::common_type_t<D1,D2>
operator-( const time_point<C,D1>& pt_lhs,
const time_point<C,D2>& pt_rhs );
```

Performs add and subtract operations involving a `time_point`.
@1,2@ Applies the offset `d` to `pt`. Effectively returns `CT(pt.time_since_epoch() + d)`, where `CT` is the return type.
3. Applies the offset `d` to `pt` in negative direction. Effectively returns `CT(pt.time_since_epoch() - d)`, where `CT` is the return type.
4. Computes the difference between `pt_lhs` and `pt_rhs`.

## Parameters


### Parameters

- `pt` - a time point to apply the offset to
- `d` - a time offset
- `pt_lhs, pt_rhs` - time points to extract difference from

## Return value

@1-3@ The time point that resulted from applying the offset `d`.
4. The duration between the time points.

## Example


## Defect reports


## See also


| cpp/chrono/time_point/dsc operator_arith | (see dedicated page) |

