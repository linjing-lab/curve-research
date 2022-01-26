# Gauss-Newton
def gauss_newton(funcr, args, x_0, epsilon=1e-10, k=0):
    """

    Parameters
    ----------
    funcr : sympy.matrices.dense.MutableDenseMatrix
        当前目标残差方程
        
    args : sympy.matrices.dense.MutableDenseMatrix
        参数列表
        
    x_0 : list
        初始迭代点列表
        
    epsilon : float
        迭代停机准则
        
    k : int
        迭代次数
        

    Returns
    -------
    tuple
        最终收敛点, 迭代次数
        
    """
    
    import sympy as sp
    import numpy as np
    def linear_search(funcs, args, x_0, d, c1=0.3, c2=0.5, alphas=0, alphae=2, eps=1e-3):
        '''
        Parameters
        ----------
        funcs : sympy.matrices.dense.MutableDenseMatrix
            当前目标方程
            
        args : sympy.matrices.dense.MutableDenseMatrix
            参数列表
            
        x_0 : list
            初始迭代点列表
            
        d : numpy.array
            当前下降方向
            
        c1 : float
            常数
            
        c2 : float
            常数
            
        alphas : float
            起始搜索区间
            
        alphae : float
            终止搜索区间
            
        eps : float
            终止参数
            

        Returns
        -------
        float
            最优步长
            
        '''
        import numpy as np
        assert c1 > 0
        assert c1 < 1
        assert c2 > 0
        assert c2 < 1
        assert c1 < c2
        assert alphas < alphae
        alpha = 1
        res = funcs.jacobian(args)
        reps = dict(zip(args, x_0))
        f0 = np.array(funcs.subs(reps)).astype(np.float64)
        res0 = np.array(res.subs(reps)).astype(np.float64)
        while alphas < alphae:
            x = x_0 + (alpha*d)[0]
            f1 = np.array(funcs.subs(dict(zip(args, x)))).astype(np.float64)
            if f1 <= f0 + c1*alpha*res0.dot(d.T):
                res1 = np.array(res.subs(dict(zip(args, x)))).astype(np.float64)
                if res1.dot(d.T) >= c2*res0.dot(d.T):
                    break;
                else:
                    alphas = alpha
                    alpha = 0.5 * (alphas + alphae)
            else:
                alphae = alpha
                alpha = 0.5 * (alphas + alphae)
            if np.abs(alphas-alphae) < eps:
                break;
        return alpha
    
    res = funcr.jacobian(args)
    funcs = sp.Matrix([(1/2)*funcr.T*funcr])
    while True:
        reps = dict(zip(args, x_0))
        rk = np.array(funcr.subs(reps)).astype(np.float64)
        jk = np.array(res.subs(reps)).astype(np.float64)
        q, r = np.linalg.qr(jk)
        dk = np.linalg.inv(r).dot(-(q.T).dot(rk)).reshape(1,-1)
        if np.linalg.norm(dk) > epsilon:
            alpha = linear_search(funcs, args, x_0, dk)
            x_0 = x_0 + alpha * dk[0]
            k = k + 1
        else:
            break
    return x_0, k

def levenberg_marquardt(funcr, args, x_0, m=100, lamk=1, eta=0.2, p1=0.4, p2=0.9, gamma1=0.7, gamma2=1.3, epsilon=1e-10, k=0):
    '''
    Parameters
    ----------
    funcr : sympy.matrices.dense.MutableDenseMatrix
        当前目标残差方程
        
    args : sympy.matrices.dense.MutableDenseMatrix
        参数列表
        
    x_0 : list
        初始迭代点列表
        
    m : float
        海瑟矩阵条件数阈值
        
    lamk : int
        修正常数
        
    eta : float
        常数
        
    p1 : float 
        常数
        
    p2 : float
        常数
        
    gamma1 : float
        常数
        
    gamma2 : float
        常数
        
    epsilon : float
        迭代停机准则
        
    k : int
        迭代次数
        

    Returns
    -------
    tuple
        最终收敛点, 迭代次数, (迭代函数值列表)
        
    '''
    import sympy as sp
    import numpy as np
    def modify_hessian(hessian, m, pk=1):
        '''
        Parameters
        ----------
        hessian : numpy.array
            未修正的海瑟矩阵值
            
        m : float
            条件数阈值
            
        pk : int
            常数
            

        Returns
        -------
        numpy.array
            修正后的海瑟矩阵
            
        '''
        import numpy as np
        l = hessian.shape[0]
        while True:
            values, _ = np.linalg.eig(hessian)
            flag = (all(values) > 0) & (np.linalg.cond(hessian) <= m)
            if flag:
                break
            else:
                hessian = hessian + pk * np.identity(l)
                pk = pk + 1
        return hessian
    
    def CG_gradient(A, b, dk, epsilon=1e-6, k=0):
        '''
        Parameters
        ----------
        A : numpy.array
            矩阵
            
        b : numpy.array
            行向量
            
        dk : numpy.array
            初始梯度下降方向（列向量）
            
        epsilon : float
            精度
            
        k : int
            迭代次数
            

        Returns
        -------
        tuple
            当前梯度（行向量）, 迭代次数
            
        '''
        import numpy as np
        rk = b.T - A.dot(dk)
        pk = rk
        while True:
            if np.linalg.norm(pk) < epsilon:
                break
            else:
                ak = (rk.T).dot(rk) / ((pk.T).dot(A)).dot(pk)
                dk = dk + ak * pk
                bk_down = (rk.T).dot(rk)
                rk = rk - ak * A.dot(pk)
                bk = (rk.T).dot(rk) / bk_down
                pk = rk + bk * pk
            k = k + 1
        return dk.reshape(1, -1), k
    
    assert eta >= 0
    assert eta < p1
    assert p1 < p2
    assert p2 < 1
    assert gamma1 < 1
    assert gamma2 > 1
    res = funcr.jacobian(args)
    funcs = sp.Matrix([(1/2)*funcr.T*funcr])
    resf = funcs.jacobian(args)
    hess = resf.jacobian(args)
    dk0 = np.zeros((args.shape[0], 1))
    while True:
        reps = dict(zip(args, x_0))
        rk = np.array(funcr.subs(reps)).astype(np.float64)
        jk = np.array(res.subs(reps)).astype(np.float64)
        dk, _ = CG_gradient((jk.T).dot(jk) + lamk, -((jk.T).dot(rk)).reshape(1, -1), dk0)
        pk_up = np.array(funcs.subs(reps)).astype(np.float64) - np.array(funcs.subs(dict(zip(args, x_0 + dk[0])))).astype(np.float64)
        grad_f = np.array(resf.subs(reps)).astype(np.float64)
        hess_f = np.array(hess.subs(reps)).astype(np.float64)
        hess_f = modify_hessian(hess_f, m)
        pk_down = - (grad_f.dot(dk.T) + 0.5*((dk.dot(hess_f)).dot(dk.T)))
        pk = pk_up / pk_down
        if np.linalg.norm(dk) >= epsilon:
            if pk < p1:
                lamk = gamma2 * lamk
            else:
                if pk > p2:
                    lamk = gamma1 * lamk
                else:
                    lamk = lamk
            if pk > eta:
                x_0 = x_0 + dk[0]
            else:
                x_0 = x_0
            k = k + 1
        else:
            break
    return x_0, k