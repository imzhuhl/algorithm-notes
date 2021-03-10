
## 数字

```c++
#include <climits>
INT_MAX  // 最大 int
INT_MIN
```

## 字符串操作

```c++
#include <cctype>

isspace(str[i]);  // 是否空白字符: ' ', '\n', '\t' 等
isdigit(str[i]);  // 判断是否数字

```

## 基本用法

### vector

初始化：

```c++
vector<T> v1;                 // default initialization, v1 is empty
vector<T> v2(v1);             // v2 has a copy of each element in v1
vector<T> v2 = v1;            // equivalent to v2(v1)
vector<T> v1(n, val);         // v1 has n elements with value val
vector<T> v1(n);              // v1 has n elements with default-value
vector<T> v1{a, b, c, ...};   // v1 has many elements with a, b, c ...
vector<T> v1 = {a, b, c, ...} // equivalent to v1{a, b, c, ...}
```

基本操作：

```c++
v.push_back(i);  // append an element to end of v
v.empty(); // return ture if v is empyt, otherwise return false
v.size();  // return the number of elements in v
v1 == v2;  // return true if v1.size() == v2.size() and each element is equivalent
```

迭代：

```c++
for (unsigned int i = 0; i < v.size(); ++i) {
    cout << v[i] << endl;
}

for (auto it = v.begin(); it != v.end(); ++it) {
    cout << *it << endl;
}
```

### set

```c++
/// 初始化
unordered_set<int> s;
unordered_set<int> s(v.begin(), v.end());  // 迭代器初始化

/// 基本操作
int a = 1;
s.insert(a);  // 插入元素
s.count(a);  // 返回元素的数量，只会是 0 或 1
s.erase(a);  // 删除元素
```

其他线性容器：

* deque：双端队列
* list：双端链表
* forward_list：单方向的链表
* array：固定数组
* string：字符串

### algorithm library

```c++
#include <algorithm>
```

* find
* accumulate
* fill
* copy
* replace
* sort
* stable_sort

自定义 sort

```c++
bool Shorter(const string &s1, const string &s2) {
    return s1.size() < s2.size();
}
sort(words.begin(), words.end(), Shorter);  // sort by length in ascending order
```

判断最大最小：

```c++
int a, b, c = ...;
min({a, b, c});
min(min(a, b), c);
```



### lambda

```c++
[capture list] (parameter list) -> return type { function body }

// example
sort(words.begin(), words.end(), 
     [] (const string &s1, const string &s2) {return s1.size()<s2.size();});
```

capture list 表示使用的局部变量：

```c++
// capture by value
int x = 42;
auto f = [x] () {return x;}
x = 0;
f();  // return 42, f stored a copy of x when we created it

// capture by reference
int x = 42;
auto f = [&x] () {return x;}
x = 0;
f();  // return 0, f refer to x

// implicit captures, compiler infers which variables we use from body
[&] () {}  // by reference
[=] () {}  // by value
```
