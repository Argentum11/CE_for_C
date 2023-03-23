# CFE_for_C
A compiler, formatter and executer for C

## Environments
To use this repository, you need 
 * gcc 4.6.1
 * flex 2.5.4
 * bison 2.4.1
 
WARNING: Please don't install flex and bison under a path that has any empty space (ex: C:\Program Files (x86) ), select a path without empty space (ex: C:\compiler)

Run the following commands to test if gcc, flex and bison are installed
```
gcc -v
flex -V
bison -V
```
You should see the following result
![image](https://user-images.githubusercontent.com/92793837/220815692-7b47de4e-008e-4019-8b3d-65f6f2f6196c.png)

## How to use

### Calculator

1. Just enter the numbers that you want to calculate (ex: 1+5, 10*399..etc)
     - Warning: While entering negative numbers, please use parentheses, look at the following example
     ```
     9+(-5)
     1-(-55)
     ```
