import sys

class Logger:
    init_flag_=False

    @staticmethod
    def _init():
        #将输出缓冲区大小设置为1,实时输出
        sys.stdout=open(sys.stdout.fileno(),mode='w',buffering=1)
        return True

    def __init__(self,head_string=""):
        self.head_=head_string

    def print(self,*args,**kwargs):
        print(*args,**kwargs,sep="",end="")
        return self

    def println(self,*args,**kwargs):
        print(*args,**kwargs,sep="",end="\n")
        return self

    def print_with_head(self,*args,**kwargs):
        self.print(self.head_)
        self.print(*args,**kwargs)
        return self

    def println_with_head(self,*args,**kwargs):
        self.print(self.head_)
        self.println(*args,**kwargs)
        return self

Logger.init_flag_=Logger._init()
