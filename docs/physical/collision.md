##物理效果

### 碰撞

所有图形类都有一个方法collide，接受一个参数，必须是另外一个图形类实例，如果两个图形相互碰撞，那么返回碰撞点坐标。否则返回`false`

```javascript
rect.collide(circle);
```

坐标点是一个对象，因此可以直接使用if来判断是否发生碰撞。

在图形进行旋转、翻转、平移后，碰撞仍可以进行判断。

### 图像的碰撞

为了提高执行的效率，不提供像素级别的碰撞判断，图片的碰撞体积默认为图像宽高的0.8（80%），可以通过`setCollisionScale`来设定碰撞宽高的比例。
