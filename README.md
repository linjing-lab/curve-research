# curve〽

<p align="center">
    <img src="./asserts/logo.jfif">
</p>

## 项目初衷
&emsp;&emsp;该项目建立的目的，在于为不同类型的曲线（主要是平面曲线）建立高效的解决方案，便于后续研究人员拓展研究。 根据曲线的性质不同，该项目可能涉及平面几何，高等数学，最优化方法，微分几何等课程的学习，我们希望对几何这一领域有兴趣的各界人士可以加入我们，提出新的设计思想，成为里程碑中的一员。

&emsp;&emsp;目前只有曲线与固定点间切线的解决方案，如果有别的好的方案（可以通过编程实现的），请先在[linjing-lab](https://github.com/linjing-lab)主页联系我。

## 项目大纲

## 解决方案
`基本设计思路`：对于平面中的任何点，需要得到从该点到给定类型曲线的切线。如果存在此切线，则绘制曲线和切线。 如果切线不存在，则返回`False`。
> PR要求：所设计的绘图程序必须能够与前两个曲线（圆与椭圆）的求解方案的绘图可视化效果一致。

### 圆（Circle）
给定圆的圆心（center）与半径（r），一个固定点（initial_point），求解由该定点引出的直线是否存在与圆相切的情况。 若有，给出切点与直线方程；若没有，则返回`False`.

### 椭圆（Ellipse）
给定椭圆的中心（center），长轴（a），短轴（b），一个固定点（initial_point），求解由该定点引出的直线是否存在与椭圆相切的情况。 若有，给出切点与直线方程；若没有，则返回`False`.

### 抛物线（Parabola）

### 双曲线（Hyperbola）

### 高次曲线（Implicit Curve）

## 参考资料
* [matplotlib](https://matplotlib.org/) 官网
* [numpy](https://www.numpy.org.cn/) 中文文档
* [sympy](https://www.sympy.org/en/index.html) 官网
* [优化方法](https://github.com/linjing-lab/optimtool)

## LICENSE
[MIT LICENSE](./LICENSE)