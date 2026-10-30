from html import escape 

class M:
    """ monad accepts children monads (mm) 
                      tag (t)
                      void (v)
                      attributes (aa)
    """
    def __init__(self,  *mm, t="div", v=False, **aa):
        if v and mm:
            raise ValueError("A VOID MONAD CANNOT HAVE CHILDREN")
        
        # children 
        self.mm = mm
        # tags
        self.t = t
        # void 
        self.v = v
        # attributes 
        self.aa = aa 
    
    def mon(self, *mm, **options):
        """ creates and adds new monad"""
        node = M(*mm, **options)
        self.ad(node)
        return node 
    def ad(self, *mm):
        """ adds existing monad as child"""
        if self.v and mm:
            raise ValueError("A VOID MONAD CANNOT HAVE CHILDREN")
        self.mm += mm 
        return self 



    def render(self): 
        """ 
        render opening, recursivelt render children, render close. 

        class_ = class 
        data_name = data-name 
        aria_label = aria-label 
        ...
        """

        aaa = ""

        for x, y in self.aa.items():
            x = x.rstrip("_").replace("_", "-")
            if y is None or y is False:
                continue 
            if y is True:
                aaa += f" {x}"
            else:
                aaa += f' {x}={escape(str(y), quote=True)}'

        B = []

        for m in self.mm:
            if isinstance(m, M):
                B.append(m.render())
            else:
                B.append(escape(str(m)))

        A = f"<{self.t}{aaa}>"
        B = f"".join(B)
        C = "" if self.v else f"</{self.t}>"

        return A + B + C



