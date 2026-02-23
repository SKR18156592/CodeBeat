import time
import inspect
from math import *
import statistics
class code_tracker:
    def __init__(self,function_object,no_of_iterations=10,namespace={}):
        self.namespace={'time':time}
        self.function_object=function_object
        self.no_of_iterations=no_of_iterations
        self.outputstring=self.modify_function()
        self.func_name=function_object.__name__
        self.exec_func=self.get_executable()
    
    def get_executable(self):
        exec(self.outputstring,self.namespace)
        return self.namespace[self.func_name]

    def __call__(self,x,y):
        self.display(self.exec_func,x,y)


    def display(self,k,x,y):
        dt1={}
        for _ in range(self.no_of_iterations):
            nf=k(x,y)
            f1 = nf[1]
            for i,line in enumerate(f1):
                lst1=[]
                if i==len(f1)-1:
                    break
                lst1.append(f1[i+1][3])
                if line[1] not in dt1:
                    dt1[line[1]]=lst1
                else:
                    dt1[line[1]]+=lst1 
                            
        dtmean={}
        dtsd={}
        for key,value in dt1.items():
            dtmean[key]=statistics.mean(value)
            dtsd[key]=statistics.stdev(value)

        dt2={}
        for key,value in dt1.items():
            for i in range(10):
                if str(i) not in dt2:
                    dt2[str(i)]=value[i]
                else:
                    dt2[str(i)]+=value[i]
        
        lst=[]
        for value in dt2.values():
            lst.append(value)
        mean_time=statistics.mean(lst)
        std_time=statistics.stdev(lst)
    
        max_len=len("mean_time(in ms)      ")
        max_word_count=0
        for line in f1:
            word_count=len(line[1])
            if word_count>max_word_count:
                max_word_count=word_count
        lst=[]
        print("="*len("line No")*(max_word_count))
        for i,line in enumerate(f1):
            word_count=len(line[1])
            indent=" "*(max_word_count-word_count) 
            if i==0:
                print(f"|> Function Name: fun, #iter:10, mean_time(in ms):{mean_time*1000:.3f}, std_time(in ms):{std_time*1000:.3f}")
                print(f"{'='*len('line No')*(max_word_count)} ")
                print(f"| line No | Line{' '*(word_count-len('Line'))}{indent}| mean_time(in ms){' '*(max_len-len('mean_time(in ms)'))} | std_time(in ms)")
                print(f"{'='*len('line No')*(max_word_count)} ")    
            if i==len(f1)-1:
                print(f"| {i} {(len('line No')-1)*' '}|{line[1]}{indent} | nan{' '*(max_len-len('nan'))} | nan")
                break
            t=dtmean[line[1]]*1000
            nt=f"{t:.3g}"
            spaces=' '*(max_len-len(nt))
            # print(f"| {i} {' '*(len('line No')-1)}|{line[1]}{indent} | {nt}{spaces} | {dtsd[line[1]]*1000:.3g}")
            print(f"| {i} {' '*(len('line No')-1)}|{line[1]}{indent} | {f'{t:.3f}'}{' '*(max_len-len(f'{t:.3f}'))} | {dtsd[line[1]]*1000:.3f}")    
        print(f"{'-'*len('line No')*(max_word_count)}")


        
    def modify_function(self):
        s=inspect.getsource(self.function_object)
        x = s.split('\n')
        time_addedlist=[]
        time_addedlist.append(x[0])
        y= x[1:-1]
        i=0
        indent_lst=[]
        for l,line in enumerate(y):
            indent=" " *(len(line)-len(line.lstrip()))
            indent_lst.append(indent)
            if i>1:
                if indent_lst[i]<indent_lst[i-1]:
                    time_addedlist.append(f"{indent_lst[i-1]}time_watcher_{i}=time.time()")
                    time_addedlist.append(f"{indent_lst[i-1]}max_watcher_{i}=max(max_watcher_{i},time_watcher_{i} - time_watcher_{i-1})")
                    i+=1   
            time_addedlist.append(f"{indent}time_watcher_{i}=time.time()")
            if i==0:
                time_addedlist.append(f"{indent}max_watcher_{i}=time.time()")
            if i>0:
                time_addedlist.append(f"{indent}max_watcher_{i}=max(max_watcher_{i},time_watcher_{i} - time_watcher_{i-1})")    
            time_addedlist.append(line)  
            i+=1 
        for j in range(len(y)+1):
            indent=" " *(len(y[0])-len(y[0].lstrip()))
            time_addedlist.insert(1,f"{indent}time_watcher_{len(y)-j}=0")
            time_addedlist.insert(1,f"{indent}max_watcher_{len(y)-j}=0")
        # if "return" not in y[-1]:
        #     time_addedlist.append(f"{indent}t{i}=time.time()")
        #     time_addedlist.append(f"{indent}print(t{i}-t{i-1})") 
        d=',['
        for a,line in enumerate(y):
            d+=f"({a},'{line}',time_watcher_{a},max_watcher_{a})"
            if a<len(y)-1:
                d+=','
        d+=']'
        time_addedlist[-1]+=d   
    
        return "\n".join(time_addedlist) 
    


    



        
        


    