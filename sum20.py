#!/usr/bin/python
import csv
import glob
import sys
def findLargest(folder):
    #allF = glob.glob(folder).sort()
    allF = glob.glob(folder+'*')
    allF.sort()
    #print allF
    return allF[-2]

nodes=20
throughSum=0;

ff = open('avgs.txt', 'w');
for i in range(25,25+nodes):
    larger = findLargest('files-%d/var/log/'%i)
   # print "larger=%d"%i
    #with open('files-0/var/log/46638/stdout', 'r') as csvfile:
    with open(larger+'/stdout', 'r') as csvfile:
        r = csv.reader(csvfile, delimiter=',',
                                quotechar='|')
        sum =0;
        nrows = 0;
        f = open('%d.txt'%i, 'w');
        for rr in r:
            sum = sum + float(rr[8])
            f.write(rr[8]+"\n");
            nrows = nrows +1;
           # print rr[8]
        if(nrows != 0):
            avg = sum / (nrows * 1000000)
            #print "nodes %d, avg = %.4f"%(i, avg)
            print "%d  %.4f"%(i, avg)
            ff.write("%d  %.4f\n"%(i, avg))
            throughSum += avg;
        else:
            print "%d N/A"%(i)
            #print "%d  %.4f"%(i, avg)
ff.close()


print "%d %.4f"%(nodes, throughSum / nodes)
f = open('overallAvg.txt','w')
f.write("%d %.4f\n"%(nodes, throughSum / nodes))
f.close();
f = open('overallSum.txt','w')
f.write("%d %.4f\n"%(nodes, throughSum))
f.close();
