# CE_for_C

A compiler and executer for C

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

## 使用說明

### 指令

|指令名稱|範例|輸出|
|-|-|-|
|輸出數字運算|cout<<2+3*4-10/5;|12|
|儲存整數|int a=123;||
|輸出整數|cout<<a<<endl;|123\n|
|儲存整數|int aa=1023;||
|輸出整數運算|cout<<a<<" "<<aa<<" "<<a+aa<<" "<<aa<<" "<<a/2<<endl;|123 1023 1146 1023 61.5\n|
|儲存負小數|double b = -123.456;||
|輸出負小數|cout<<b<<endl;|-123.456\n|
|儲存負小數|double bb=-23.444;||
|輸出負小數運算|cout<<b<<" "<<bb<<" "<<b+bb<<" "<<bb<<" "<<b/2<<endl;|-123.456 -23.444 -146.9 -23.444 -61.728\n|
|輸出整數&負小數運算|cout<<a+b<<endl;|-0.456\n|
|儲存字串|string c="hello";||
|輸出字串&整數&負小數|cout<<c<<" "<<a<<" "<<b<<" "<<c<<endl;|hello 123 -123.456 hello\n|
|輸出 \t |cout<<"\tadc"<<endl;|\tadc\n|
|輸出 \n|cout<<"ad\nc"<<endl;|ad\nc|
|輸出 \0 (end of string) |cout<<"ad\0c"<<endl;|ab\0\n|
|輸出 \ |cout<<"\\\\"<<endl;|\\\\n|
|輸出 " |cout<<"\\""<<endl;|"\n|
|輸出 ' |cout<<"\\'"<<endl;|'\n
|${log_{10}}X$|cout<<log(2);|0.30103|
|if|if(3>2){cout << 2222 << endl;}|2222|
|if|if(3<2){cout << 2222 << endl;}|換行|
|sqrt|cout << sqrt(4) << endl;|2|
|cos|cout << cos(1) << endl;|0.54|
|sin|cout << sin(1) << endl;|0.841|
|tan|cout << tan(1) << endl;|1.5571|
|^|cout << 2^3 << endl;|8|
|%|cout << 3%2 << endl;|1|
|>|cout << (3>2) << endl;|1|
|<|cout << (3<4) << endl;|1|
|>=|cout << (3>=2) << endl;|1|
|<=|cout << (3<=4) << endl;|1|
|==|cout << (2==2) << endl;|1|

### 錯誤處理

|error type|command example|command output|
|-|-|-|
|語法錯誤|cout<<;|error:syntax error\nAn error occurred. Please try again.|
|變數錯誤|cout<<a;|error: a is not defined\nAn error occurred. Please try again.|
|變數錯誤|cout<<a<<b;|error: a is not defined\nerror: b is not defined\nAn error occurred. Please try again.|
|語法錯誤|a=1;|error:syntax error\nAn error occurred. Please try again.|
|語法錯誤|double a = "123";|error:syntax error\nAn error occurred. Please try again.|
|語法錯誤|string b = 123;|error:syntax error\nAn error occurred. Please try again.|
|語法錯誤|if(){cout<<123;}|error:syntax error\nAn error occurred. Please try again.|
|語法錯誤|i(1){cout<<123;}|error:syntax error\nAn error occurred. Please try again.|
|語法錯誤|out<<123;|error:syntax error\nAn error occurred. Please try again.|
|輸出錯誤|cout<<;|missing variable / string / number\nerror:syntax error\nAn error occurred. Please try again.|
|輸出錯誤|int a=10; cout<<a<<;|10missing variable / string / number\nerror:syntax error\nAn error occurred. Please try again.|

## 分工

|name|work|
|-|-|
|[張銀軒](https://github.com/Argentum11)|負數、cout錯誤處理、所有的 pytest 測試、github project 管理|
|[林佳何](https://github.com/0-ch)|宣告int、double、string型態變數、變數運算、輸出變數、字串、跳脫字元、cout & 所有的錯誤處理|
|[王丞頤](https://github.com/WCY91)|三角函數、餘數、次方、開根號、if/else、 $\leq$ 、 $\geq$ 、 > 、 < 、 ==|

