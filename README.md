# 曲线科学研究（curve）

![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=2bbc8a)&emsp;![](https://img.shields.io/badge/Community-PyPi-informational?style=flat&logo=pypi&logoColor=white&color=2bbc8a)&emsp;![](https://img.shields.io/badge/Tool-Anaconda-informational?style=flat&logo=anaconda&logoColor=white&color=2bbc8a)&emsp;![](https://img.shields.io/badge/Tool-Git-informational?style=flat&logo=git&logoColor=white&color=2bbc8a)

## 1. 项目初衷
&emsp;&emsp;该项目建立的目的，在于为不同类型的曲线（主要是平面曲线）建立高效的解决方案，便于后续研究人员拓展研究。 根据曲线的性质不同，该项目可能涉及平面几何，高等数学，最优化方法，微分几何等课程的学习，我们希望对几何这一领域有兴趣的各界人士可以加入我们，提出新的设计思想，成为里程碑中的一员。

&emsp;&emsp;目前只有曲线与固定点间切线的解决方案，如果有别的好的方案（可以通过编程实现的），请先在`linjing-lab`主页联系我。

`基本设计思路`：对于平面中的任何点，需要得到从该点到给定类型曲线的切线。如果存在此切线，则绘制曲线和切线。 如果切线不存在，则返回`False`。

> PR要求：所设计的绘图程序必须能够与前两个曲线（圆与椭圆）的求解方案的绘图可视化效果一致。

## 2. 解决方案
### 2.1 圆（Circle）
给定圆的圆心（center）与半径（r），一个固定点（initial_point），求解由该定点引出的直线是否存在与圆相切的情况。 若有，给出切点与直线方程；若没有，则返回`False`.

### 2.2 椭圆（Ellipse）
给定椭圆的中心（center），长轴（a），短轴（b），一个固定点（initial_point），求解由该定点引出的直线是否存在与椭圆相切的情况。 若有，给出切点与直线方程；若没有，则返回`False`.

### 2.3 抛物线（Parabola）

### 2.4 双曲线（Hyperbola）

### 2.5 高次曲线（Implicit Curve）

## LICENSE
[MIT LICENSE](./LICENSE)