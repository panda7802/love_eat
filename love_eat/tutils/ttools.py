# coding=utf-8
'''
@author: pangt
'''
from tutils.t_log import tlog


# 字典转到�?
def tDict2Obj(d_dict, cls):
    
    if None is d_dict or None is cls :
        return None
    
    ins = cls()
    for k, v in d_dict.items() :
        if None is v :
            continue
        
        old_v = getattr(ins, k)
        if type == type(old_v):
            continue
        elif list == type(old_v) :
            sun_cls = getattr(cls  , "_get_" + k + "_arr_type")
            tmp_list = tDicts2List(v, sun_cls)
            setattr(ins, k, tmp_list);
        elif dict == type(old_v) :
            sun_cls = type(getattr(ins, k))
            sun_ins = tDict2Obj(v, sun_cls)
            setattr(ins, k, sun_ins);
        else : 
            setattr(ins, k , v)
            
    return ins

# 字典转列�?
def tDicts2List(d_list, cls):
    
    if None is d_list or None is cls :
        return None

    resL = []
    for item in d_list:
        tmp_item = tDict2Obj(item, cls)
        resL.append(tmp_item)
    return resL

