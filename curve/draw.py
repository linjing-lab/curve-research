# initial
def initial(title):
    """
    

    Parameters
    ----------
    title : string
        绘图标题.

    Returns
    -------
    fig 
        窗体.

    """
    
    import matplotlib.pyplot as plt
    fig = plt.figure()
    plt.title(title)
    plt.ylabel('y')
    plt.xlabel('x')
    return fig

# circle
def circle(center, r, con=False):
    """
    

    Parameters
    ----------
    center : tuple
        圆心.
        
    r : float
        半径.
        
    con : bool, optional
        是否需要绘制在一张图中. The default is False.

    Returns
    -------
    ln
        图例.
    x1
        直线绘图区间.

    """
    
    import numpy as np
    x = np.linspace(center[0] - r, center[0] + r, 5000)
    y1 = np.sqrt(r**2 - (x-center[0])**2) + center[1]
    y2 = -np.sqrt(r**2 - (x-center[0])**2) + center[1]
    import matplotlib.pyplot as plt
    plt.plot(x, y1, c="teal", linestyle="dashed")
    ln, = plt.plot(x, y2, c="teal", linestyle="dashed")
    plt.axis("equal")
    if con is False:
        plt.show()
        return None
    else:
        x1 = np.linspace(min(x) - 2, max(x) + 2, 5000)
        return ln, x1
    
# ellipse
def ellipse(center, a, b, con=False):
    import numpy as np
    x = np.linspace(center[0] - a, center[0] + a, 5000)
    c = (a**2)*(b**2)
    y1 = np.sqrt(c - (b**2)*((x - center[0])**2)) / a + center[1]
    y2 = - np.sqrt(c - (b**2)*((x - center[0])**2)) / a + center[1]
    if a > b:
        mi = min(x)
        ma = max(x)
    else:
        mi = min(y2)
        ma = max(y1)
    import matplotlib.pyplot as plt
    plt.plot(x, y1, c="teal", linestyle="dashed")
    ln, = plt.plot(x, y2, c="teal", linestyle="dashed")
    plt.axis("equal")
    if con is False:
        plt.show()
        return None
    else:
        x1 = np.linspace(mi - 2, ma + 2, 5000)
        return ln, x1