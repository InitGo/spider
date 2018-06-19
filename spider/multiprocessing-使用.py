from multiprocessing import Pool    #导入模块
import re
import  requests



pool = Pool(processes=4)            #创建进程池 设置进程个数
pool.map(func,iterable[,chunksize]) #

