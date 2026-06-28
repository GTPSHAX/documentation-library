---
title: ctime
type: Standard headers
source: https://en.cppreference.com/w/cpp/header/ctime
---

This header is part of the C-style date and time library.


| cpp/chrono/c/dsc CLOCKS_PER_SEC | (see dedicated page) |
| cpp/types/dsc NULL | (see dedicated page) |
| cpp/chrono/c/dsc clock_t | (see dedicated page) |
| cpp/types/dsc size_t | (see dedicated page) |
| cpp/chrono/c/dsc time_t | (see dedicated page) |
| cpp/chrono/c/dsc tm | (see dedicated page) |
| cpp/chrono/c/dsc timespec | (see dedicated page) |

#### Time manipulation

| cpp/chrono/c/dsc clock | (see dedicated page) |
| cpp/chrono/c/dsc time | (see dedicated page) |
| cpp/chrono/c/dsc difftime | (see dedicated page) |
| cpp/chrono/c/dsc timespec_get | (see dedicated page) |
| cpp/chrono/c/dsc timespec_getres | (see dedicated page) |

#### Format conversions

| cpp/chrono/c/dsc asctime | (see dedicated page) |
| cpp/chrono/c/dsc ctime | (see dedicated page) |
| cpp/chrono/c/dsc strftime | (see dedicated page) |
| cpp/chrono/c/dsc gmtime | (see dedicated page) |
| cpp/chrono/c/dsc localtime | (see dedicated page) |
| cpp/chrono/c/dsc mktime | (see dedicated page) |
| cpp/chrono/c/dsc timegm | (see dedicated page) |


## Synopsis


```cpp
#define __STDC_VERSION_TIME_H__ 202311L

#define NULL               /* implementation-defined */
#define CLOCKS_PER_SEC     /* see description */
#define TIME_UTC           /* see description */
#define TIME_MONOTONIC     /* see description */  // optional
#define TIME_ACTIVE        /* see description */  // optional
#define TIME_THREAD_ACTIVE /* see description */  // optional

namespace std {
  using size_t = /* implementation-defined */;
  using clock_t = /* see description */;
  using time_t = /* see description */;

  struct timespec;
  struct tm;

  clock_t clock();
  double difftime(time_t time1, time_t time0);
  time_t mktime(tm* timeptr);
  time_t timegm(tm* timeptr);
  time_t time(time_t* timer);
  int timespec_get(timespec* ts, int base);
  int timespec_getres(timespec* ts, int base);
  // char* asctime(const tm* timeptr);
  // char* ctime(const time_t* timer);
  tm* gmtime(const time_t* timer);
  tm* gmtime_r(const time_t* timer, tm* buf);
  tm* localtime(const time_t* timer);
  tm* localtime_r(const time_t* timer, tm* buf);
  size_t strftime(char* s, size_t maxsize, const char* format, const tm* timeptr);
}
```


## Class `std::timespec`


```cpp
struct timespec {
  std::time_t tv_sec;
  long tv_nsec;
};
```


## Class `std::tm`


```cpp
struct tm {
  int tm_sec;
  int tm_min;
  int tm_hour;
  int tm_mday;
  int tm_mon;
  int tm_year;
  int tm_wday;
  int tm_yday;
  int tm_isdst;
};
```

