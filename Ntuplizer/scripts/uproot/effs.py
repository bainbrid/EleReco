import re
import pickle 

file = open('effs.pkl','r')
efficiencies = pickle.load(file)
file.close()

keys = efficiencies.keys()
filters=["genEles_gsfEles(.*)"] 
keys = [ k for k in keys for f in filters if len(re.findall(f,k)) > 0 ]

print "Key legend:"
for ikey,key in enumerate(keys) : 
    print ikey,key.rjust(20," ")

pts = efficiencies[keys[0]][0]
for ipt,pt in enumerate(pts) : 
    if ipt == 0 : 
        print "Bin".rjust(3," "),
        print "pT [GeV]".rjust(9," "),
        for ikey,key in enumerate(keys) : print str(ikey).rjust(4," "),
        print 
    print "{:2.0f}".format(ipt).rjust(3," " ),
    print "{:7.3f}".format(pt).rjust(9," "),
    for key in keys : 
        print "{:4.2f}".format(efficiencies[key][1][ipt]).rjust(4," "),
    print 
