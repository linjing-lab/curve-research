# judge_circle
def judge_circle(center, r, initial_point):
    import sympy as sp
    x, y = sp.symbols("x y")
    funcs = (x - center[0])**2 + (y - center[1])**2 - r**2
    args = sp.Matrix([x, y])
    value = funcs.subs(dict(zip(args, initial_point)))
    if value > 0:
        return 1
    elif value == 0:
        return 0
    else:
        return -1

# point_tangent
def point_tangent_circle(center, r, initial_point):
    import sympy as sp
    c1 = (initial_point[1] - center[1])
    c2 = r**2
    c3 = initial_point[0] - center[0]
    x, y = sp.symbols("x y")
    funcs = (c1**2)*(x - center[0])**2 + (c2 - c3*(x - center[0]))**2 - (c1**2)*c2
    m = sp.solve(funcs)
    n = []
    for i in m:
        n.append(sp.solve(c3*(i - center[0]) + c1*(y - center[1]) - c2)[0])
    return (round(m[0], 1), round(n[0], 1)), (round(m[1], 1), round(n[1], 1))

# judge_ellipse
def judge_ellipse(center, a, b, initial_point):
    import sympy as sp
    x, y = sp.symbols("x y")
    funcs = (b**2)*((x - center[0])**2) + (a**2)*((y - center[1])**2) - (a**2)*(b**2)
    args = sp.Matrix([x, y])
    value = funcs.subs(dict(zip(args, initial_point)))
    if value > 0:
        return 1
    elif value == 0:
        return 0
    else:
        return -1
    
# point_tangent_ellipse
def point_tangent_ellipse(center, a, b, initial_point):
    import sympy as sp
    c1 = (a**2)*((initial_point[1] - center[1])**2)
    c2 = b**2
    c3 = (a**2)*(b**2)
    x, y = sp.symbols("x y")
    funcs = c1*c2*((x - center[0])**2) + (c3 - c2*(initial_point[0] - center[0])*(x - center[0]))**2 - c3*c1
    m = sp.solve(funcs)
    n = []
    for i in m:
        n.append(sp.solve(c2*(initial_point[0] - center[0])*(i - center[0]) + (a**2)*(initial_point[1] - center[1])*(y - center[1]) - c3)[0])
    return (round(m[0], 1), round(n[0], 1)), (round(m[1], 1), round(n[1], 1))
    
# lengend_get
def legend_get(delta_y, delta_x, const, xln):
    import matplotlib.pyplot as plt
    import sympy as sp
    final = []
    if delta_y != 0:
        final.append(- delta_x / delta_y)
        final.append(const / delta_y)
        # drawing interface
        ln, = plt.plot(xln, final[0]*xln + final[1], c="maroon", linestyle="dashed")
        final_output = [round(i, 1) for i in final]
        x = sp.symbols("x")
        fun = final_output[0]*x + final_output[1]
        print('m: '+str(final_output[0])+', n: '+str(final_output[1]))
    else:
        final_x = const / delta_x
        xx = [final_x for i in range(xln.shape[0])]
        ln, = plt.plot(xx, xln, c="maroon", linestyle="dashed")
        x = sp.symbols("x")
        fun = final_x
    return ln, fun