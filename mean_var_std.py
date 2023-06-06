import numpy as np

def calculate(list):

  my_array = np.array(list)

  if my_array.size != 9:
    return "Elements size must be 9."

  else:
    my_matrix = my_array.reshape(3,3)
   

  

    v_mean_list=[]
    h_mean_list=[]
    f_mean = my_matrix.mean()

    v_var_list=[]
    h_var_list=[]
    f_var = my_matrix.var()

    v_std_list=[]
    h_std_list=[]
    f_std = my_matrix.std()

    v_max_list=[]
    h_max_list=[]
    f_max = my_matrix.max()

    v_min_list=[]
    h_min_list=[]
    f_min = my_matrix.min()

    v_sum_list=[]
    h_sum_list=[]
    f_sum = my_matrix.sum()
    sum_list=[v_sum_list,h_sum_list, f_sum]  

    helper1=my_matrix.mean(axis=1)
    helper2=my_matrix.var(axis=1)
    helper3=my_matrix.std(axis=1)
    helper4=my_matrix.max(axis=1)
    helper5=my_matrix.min(axis=1)
    helper6=my_matrix.sum(axis=1)

    h_mean_list.append(helper1.tolist())
    h_var_list.append(helper2.tolist())
    h_std_list.append(helper3.tolist())
    h_max_list.append(helper4.tolist())
    h_min_list.append(helper5.tolist())
    h_sum_list.append(helper6.tolist())


    helper1=my_matrix.mean(axis=0)
    helper2=my_matrix.var(axis=0)
    helper3=my_matrix.std(axis=0)
    helper4=my_matrix.max(axis=0)
    helper5=my_matrix.min(axis=0)
    helper6=my_matrix.sum(axis=0)

    v_mean_list.append(helper1.tolist())
    v_var_list.append(helper2.tolist())
    v_std_list.append(helper3.tolist())
    v_max_list.append(helper4.tolist())
    v_min_list.append(helper5.tolist())
    v_sum_list.append(helper6.tolist())
    


    
    mean_list=[v_mean_list,h_mean_list, f_mean]
    variance_list=[v_var_list,h_var_list, f_var]
    std_list=[v_std_list,h_std_list, f_std]
    max_list=[v_max_list,h_max_list, f_max]  
    min_list=[v_min_list,h_min_list, f_min]  
    sum_list=[v_sum_list,h_sum_list, f_sum]  

    
    result = {'mean': mean_list,
              'variance': variance_list,
              'standard deviation':std_list,
              'max': max_list,
              'min': min_list,
              'sum': sum_list
    }

  
    
  return result 
  

