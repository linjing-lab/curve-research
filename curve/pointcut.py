# 圆的切线求解方案（pointcut_line - circle）
def Circle(center, r, initial_point):
    """
    Parameters
    ----------
    center : tuple
        圆心.
        
    r : float
        半径.
        
    initial_point : tuple
        给定点.

    Returns
    -------
    string : 
        解决方案构建是否成功

    """
    from curve.maker import judge_circle, point_tangent_circle, legend_get
    import matplotlib.pyplot as plt
    from curve.draw import initial, circle
    result = judge_circle(center, r, initial_point)
    if result == -1:
        return "Failed!"
    elif result == 0:
        delta_y = initial_point[1] - center[1]
        delta_x = initial_point[0] - center[0]
        const = delta_x*initial_point[0] + delta_y*initial_point[1]
        initial("pointcut_line - circle")
        ln1, x = circle(center, r, True)
        ln2, fun = legend_get(delta_y, delta_x, const, x)
        plt.legend([ln1, ln2], ["circle", fun])
        plt.show()
        print("pointcut：", initial_point)
        return 'Success！'
    else:
        t1, t2 = point_tangent_circle(center, r, initial_point)
        initial("pointcut_line - circle")
        ln1, x1 = circle(center, r, True)
        ln_list = [ln1]
        fun_list = ["circle"]
        for i in [t1, t2]:
            print("pointcut: ", i)
            delta_y = i[0] - initial_point[0]
            delta_x = i[1] - initial_point[1]
            const = initial_point[1]*delta_y - initial_point[0]*delta_x
            ln, fun = legend_get(delta_y, -delta_x, const, x1)
            ln_list.append(ln)
            fun_list.append(fun)
        plt.legend(ln_list, fun_list)
        plt.show()
        return 'Success！'
    
# 椭圆切线求解方案（pointcut_line - Ellipse）
def Ellipse(center, a, b, initial_point):
    """
    Parameters
    ----------
    center : tuple
        圆心.
        
    a : float
        长轴.

    b : float
        短轴.
        
    initial_point : tuple
        给定点.

    Returns
    -------
    string : 
        解决方案构建是否成功

    """
    from curve.maker import judge_ellipse, point_tangent_ellipse, legend_get
    import matplotlib.pyplot as plt
    from curve.draw import initial, ellipse
    result = judge_ellipse(center, a, b, initial_point)
    if result == -1:
        return "Failed!"
    elif result == 0:
        delta_x = (b**2)*(initial_point[0] - center[0])
        delta_y = (a**2)*(initial_point[1] - center[1])
        const = (a**2)*(b**2) + delta_y*center[1] + delta_x*center[0]
        initial("pointcut_line - Ellipse")
        ln1, x = ellipse(center, a, b, True)
        ln2, fun = legend_get(delta_y, delta_x, const, x)
        plt.legend([ln1, ln2], ["Ellipse", fun])
        plt.show()
        print("pointcut：", initial_point)
        return 'Success！'
    else:
        t1, t2 = point_tangent_ellipse(center, a, b, initial_point)
        initial("pointcut_line - Ellipse")
        ln1, x1 = ellipse(center, a, b, True)
        ln_list = [ln1]
        fun_list = ["Ellipse"]
        for i in [t1, t2]:
            print("pointcut: ", i)
            delta_y = i[0] - initial_point[0]
            delta_x = i[1] - initial_point[1]
            const = initial_point[1]*delta_y - initial_point[0]*delta_x
            ln, fun = legend_get(delta_y, -delta_x, const, x1)
            ln_list.append(ln)
            fun_list.append(fun)
        plt.legend(ln_list, fun_list)
        plt.show()
        return 'Success！'
    
# 抛物线切线求解解决方案（pointcut_line - parabola）

# 双曲线切线求解解决方案（pointcut_line - hyperbola）

# 高次曲线切线求解解决方案（pointcut_line - implicit_curve）