# CFE_for_C

A compiler, formatter and executer for C

## Environments

To use this repository, you need 

* gcc 4.6.1
* flex 2.5.4
* bison 2.4.1

WARNING: Please don't install flex and bison under a path that has any empty space (ex: C:\Program Files (x86) ), select a path without empty space (ex: C:\compiler)

Run the following commands to test if gcc, flex and bison are installed

```bash
gcc -v
flex -V
bison -V
```

You should see the following result
![gcc, flex, bison version check result](https://user-images.githubusercontent.com/92793837/220815692-7b47de4e-008e-4019-8b3d-65f6f2f6196c.png)

### Error while executing

1. While executing

     ```bash
     bison -d CFE.y
     ```

     => bison: m4: Invalid argument

     Solution: Move your bison path (C:\GnuWin32\bin) to the top of the environment path variable list

## How to use

### Calculator

1. Just enter the numbers that you want to calculate (ex: 1+5, 10*399..etc)
     * Warning: While entering negative numbers, please use parentheses, look at the following example

     ```bash
     9+(-5)
     1-(-55)
     ```

     |name|command|output|
     |-|-|-|
     |add|1+5|=6|

## Division of work

|name|work|
|-|-|
|[張銀軒](https://github.com/Argentum11)|負數、所有的 pytest 測試、github project 管理|
|[林佳何](https://github.com/0-ch)|多個變數|
|[王丞頤](https://github.com/WCY91)|小數、單一變數、sin, cos...|
