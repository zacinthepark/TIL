### `*args`, `**kwargs`

```python
# *args, **kwargs

# parameter: 여러 개의 arguments를 하나의 parameter(tuple, dict)로 받는 방법
# argument: 하나의 collection data(list, tuple, dict)를 여러 개의 argument로 사용하는 방법
```

```python
def plus(*args, **kwargs):  # parameter: 1개
    print(type(args), args)
    print(type(kwargs), kwargs)
    print(sum(args) + sum(kwargs.values()))

plus(1, 2, 3, n4=10, n5=20)  # args: 5개
```

<pre>
<class 'tuple'> (1, 2, 3)
<class 'dict'> {'n4': 10, 'n5': 20}
36
</pre>

```python
def echo(*args, **kwargs):
    print(type(args), args)
    print(type(kwargs), kwargs)
```

```python
data1 = [1, 2, 3]
echo(data1)  # echo([1, 2, 3])
echo(*data1)  # echo(1, 2, 3)
```

<pre>
<class 'tuple'> ([1, 2, 3],)
<class 'dict'> {}
<class 'tuple'> (1, 2, 3)
<class 'dict'> {}
</pre>

```python
data2 = {'n4': 10, 'n5': 20}
echo(data2)  # echo({'n4': 10, 'n5': 20})
echo(**data2)  # echo(n4=10, n5=20)
```

<pre>
<class 'tuple'> ({'n4': 10, 'n5': 20},)
<class 'dict'> {}
<class 'tuple'> ()
<class 'dict'> {'n4': 10, 'n5': 20}
</pre>

```python
def connect(host, user, pw):
    print(host, user, pw)

data = {'host': '1.2.3.6', 
        'user': 'kt', 
        'pw': '1234'}

connect('1.2.3.5', 'kt', '1234')
connect(host=data['host'], user=data['user'], pw=data['pw'])
connect(**data)
```

<pre>
1.2.3.5 kt 1234
1.2.3.6 kt 1234
1.2.3.6 kt 1234
</pre>
