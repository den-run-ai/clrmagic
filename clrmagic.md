

```python
%reload_ext clrmagic
```


```python
%%CS mypower System.dll
public static double mypower(double x, double y)
{
    if (y == 0) return 1.0 ;
    return System.Math.Pow(x,y) ;
}
```




    <function clrmagic.create_cs_function.<locals>.<lambda>>




```python
mypower(3.0,3.0)
```




    27.0




```python

```
