import brian
import numpy as np
import os, sys

nruns = int(sys.argv[1])

for nrun in xrange(1, nruns+1):
    brian.seed(nrun)
    print 'RUN: ' + str(nrun)
    brian.reinit(states = True)
    brian.clear(erase   = True, all = True)
    rate = int(sys.argv[2])
    foldername = 'rate'+str(rate)+'/run_'+str(nrun)
    os.system('mkdir -p -v '+foldername)
    
    N  = 1000
    time_input = 23000 * brian.ms
    P  = brian.PoissonGroup(N)
    S = brian.SpikeMonitor(P)
    
    P.rate = rate * brian.Hz
    brian.run(time_input, report='text', report_period = 10 * brian.second)
    
    fname = 'noise_'    
    for s in xrange(len(S.spiketimes)):
        spiketimes = [round(1000*x,1)+50 for x in list(S.spiketimes[s])]
        np.savetxt(foldername+'/'+fname+str(s)+'.txt',spiketimes,fmt='%10.1f',newline='\n')
    
    

