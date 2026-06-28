---
title: cerrno
type: Standard headers
source: https://en.cppreference.com/w/cpp/header/cerrno
---

This header is part of the error handling library.

## Macros


| cpp/error/dsc errno | (see dedicated page) |


## Notes

Although the header `<cerrno>` is based on the C standard library header , the majority of the macros defined by `<cerrno>` were adopted by C++ from the POSIX standard, rather than the C standard library.

## Synopsis


```cpp
#define errno /* see description */
#define E2BIG /* see description */           // freestanding
#define EACCES /* see description */          // freestanding
#define EADDRINUSE /* see description */      // freestanding
#define EADDRNOTAVAIL /* see description */   // freestanding
#define EAFNOSUPPORT /* see description */    // freestanding
#define EAGAIN /* see description */          // freestanding
#define EALREADY /* see description */        // freestanding
#define EBADF /* see description */           // freestanding
#define EBADMSG /* see description */         // freestanding
#define EBUSY /* see description */           // freestanding
#define ECANCELED /* see description */       // freestanding
#define ECHILD /* see description */          // freestanding
#define ECONNABORTED /* see description */    // freestanding
#define ECONNREFUSED /* see description */    // freestanding
#define ECONNRESET /* see description */      // freestanding
#define EDEADLK /* see description */         // freestanding
#define EDESTADDRREQ /* see description */    // freestanding
#define EDOM /* see description */            // freestanding
#define EEXIST /* see description */          // freestanding
#define EFAULT /* see description */          // freestanding
#define EFBIG /* see description */           // freestanding
#define EHOSTUNREACH /* see description */    // freestanding
#define EIDRM /* see description */           // freestanding
#define EILSEQ /* see description */          // freestanding
#define EINPROGRESS /* see description */     // freestanding
#define EINTR /* see description */           // freestanding
#define EINVAL /* see description */          // freestanding
#define EIO /* see description */             // freestanding
#define EISCONN /* see description */         // freestanding
#define EISDIR /* see description */          // freestanding
#define ELOOP /* see description */           // freestanding
#define EMFILE /* see description */          // freestanding
#define EMLINK /* see description */          // freestanding
#define EMSGSIZE /* see description */        // freestanding
#define ENAMETOOLONG /* see description */    // freestanding
#define ENETDOWN /* see description */        // freestanding
#define ENETRESET /* see description */       // freestanding
#define ENETUNREACH /* see description */     // freestanding
#define ENFILE /* see description */          // freestanding
#define ENOBUFS /* see description */         // freestanding
#define ENODEV /* see description */          // freestanding
#define ENOENT /* see description */          // freestanding
#define ENOEXEC /* see description */         // freestanding
#define ENOLCK /* see description */          // freestanding
#define ENOLINK /* see description */         // freestanding
#define ENOMEM /* see description */          // freestanding
#define ENOMSG /* see description */          // freestanding
#define ENOPROTOOPT /* see description */     // freestanding
#define ENOSPC /* see description */          // freestanding
#define ENOSYS /* see description */          // freestanding
#define ENOTCONN /* see description */        // freestanding
#define ENOTDIR /* see description */         // freestanding
#define ENOTEMPTY /* see description */       // freestanding
#define ENOTRECOVERABLE /* see description */ // freestanding
#define ENOTSOCK /* see description */        // freestanding
#define ENOTSUP /* see description */         // freestanding
#define ENOTTY /* see description */          // freestanding
#define ENXIO /* see description */           // freestanding
#define EOPNOTSUPP /* see description */      // freestanding
#define EOVERFLOW /* see description */       // freestanding
#define EOWNERDEAD /* see description */      // freestanding
#define EPERM /* see description */           // freestanding
#define EPIPE /* see description */           // freestanding
#define EPROTO /* see description */          // freestanding
#define EPROTONOSUPPORT /* see description */ // freestanding
#define EPROTOTYPE /* see description */      // freestanding
#define ERANGE /* see description */          // freestanding
#define EROFS /* see description */           // freestanding
#define ESPIPE /* see description */          // freestanding
#define ESRCH /* see description */           // freestanding
#define ETIMEDOUT /* see description */       // freestanding
#define ETXTBSY /* see description */         // freestanding
#define EWOULDBLOCK /* see description */     // freestanding
#define EXDEV /* see description */           // freestanding
```


## Defect reports


## See also

* Description for the error number values
