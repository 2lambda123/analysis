import haloutils as htils
import sys,os
import numpy as np
import pylab as plt
import pandas as pd
import subprocess as sub
import MTanalysis2 as MTA
 
hpaths = htils.get_paper_paths_lx(14)
N=20


#hpaths = [htils.get_hpath_lx(hid,14) for hid in [447649, 95289, 1354437, 5320, 581141, 1130025, 1725139, 581180, 1232164, 1387186, 1292085, 94687, 1599988, 388476]]
hpaths = [htils.get_hpath_lx(hid,14) for hid in [1232164, 1387186, 1292085, 1599988, 388476]]

hpath = htils.get_hpath_lx(1387186,14)
print htils.get_parent_hid(hpath)
for hpath in hpaths:
    minihalos = np.load(hpath+"/analysis/minihalo_array.npy")
    mtc = htils.load_mtc(hpath, indexbyrsid=True) #haloids=[]
    print 'loaded mtc', htils.hpath_name(hpath)
    # create mapping to trees
    tree_id_map = {}
    for value,key in enumerate(minihalos['base_rsid']):
        tree_id_map.setdefault(key, []).append(value)

    next_ids = [[]]*len(minihalos)
    merger = [-1]*len(minihalos)
    form_snap=[-1]*len(minihalos)
    merge_snap=[-1]*len(minihalos)
    for i,key in enumerate(tree_id_map.iterkeys()):
        tree=mtc.Trees[key]
        desc_map = tree.get_desc_map()
        for minirow in tree_id_map[key]:
            minihalo = minihalos[minirow]
            form_snap[minirow] = minihalo['snap']
            desc=tree.getDescBranch(minihalo['row'],desc_map)
            next_ids[minirow] = desc['origid'][1:1+N]
            mask = desc['mmp']!=1
            if np.sum(mask)==0:
                merge_snap[minirow]=desc[-1]['snap']+1
            else:
                merge_snap[minirow] = desc[mask][0]['snap']+1
        if i%500==0:
            print i
    np.save(hpath+'/analysis/minihalo_descendants', next_ids)
    np.save(hpath+'/analysis/form_snap', form_snap)
    np.save(hpath+'/analysis/merge_snap', merge_snap)


#newdata=np.load(hpath+'/analysis/minihalo_descendants.npy')


"""
for minihalo,i in zip(minihalos,range(len(minihalos))):
    print get_next_N_ids(mtc,minihalo,N=20)
"""

#next_ids = []
#next_ids = np.ndarray((len(minihalos),20),dtype=np.int32)
#next_ids = [[-1]*20]*len(minihalos)

#def get_next_N_ids(mtc, minihalo, N,desc_map=None):
#    tree = mtc.Trees[minihalo['base_rsid']]
#    row = minihalo['row']
#    return tree.getDescBranch(row,desc_map)['origid'][1:1+N]  
# make this function faster by only going N steps in getDescBranch

