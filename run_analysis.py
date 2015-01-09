import haloutils
from caterpillaranalysis import *
from subradplugin import *
from caterpillarplot import *
from tbtfplugin import *
import pylab as plt
from optparse import OptionParser

if __name__=="__main__":
    parser = OptionParser()
    parser.add_option("--recalc",action="store_true",dest='recalc',default=False)
    (options,args) = parser.parse_args()
    firsttwelve = get_haloidlist(1)
    ### Use this section for quick testing scripts 
    if len(args) == 0:
        #plug = SubhaloRadialSubmassFracPlugin()
        #convergeplot(1,plug,figfilename='subradsubmassfracLX_s1.png',stop_on_error=True)
        arg = None
    else:
        assert len(args)==1
        arg = int(args[0])

    ### Use this section for essentially finalized analysis plots
    myrecalc = options.recalc
    if arg == 1:
        Nvmax      = NvmaxPlugin()
        convergeplot(1,Nvmax,lw=2,figfilename='NvmaxLX_s1.png',recalc=myrecalc)
        convergeplot(1,Nvmax,lw=2,figfilename='normNvmaxLX_s1.png',normtohost=True)
        paper_stackplot(14,Nvmax,figfilename='stackLX14_normNvmax_s1.png',lw=2,normtohost=True)
    if arg == 2:
        SHMF       = SHMFPlugin()
        intSHMF    = IntegrableSHMFPlugin()
        convergeplot(1,SHMF,lw=2,figfilename='SHMFLX_s1.png',recalc=myrecalc)
        convergeplot(1,SHMF,lw=2,figfilename='normSHMFLX_s1.png',normtohost=True)
        convergeplot(1,intSHMF,lw=2,figfilename='intSHMFLX_s1.png')
        paper_stackplot(14,SHMF,figfilename='stackLX14_normSHMF_s1.png',lw=2,normtohost=True)
    if arg == 3:
        Profile    = ProfilePlugin()
        VelProfile = VelocityProfilePlugin()
        convergeplot(1,Profile,figfilename='rhor2LX_s1.png',recalc=myrecalc)
        convergeplot(1,VelProfile,figfilename='velprofLX_s1.png')
        convergeplot(1,VelProfile,figfilename='normvelprofLX_s1.png',normtohost=True)
        paper_stackplot(14,VelProfile,figfilename='stackLX14_normvelprof_s1.png',normtohost=True)
    if arg == 4:
        MassAccr   = MassAccrPlugin()
        LinMassAccr= LinearMassAccrPlugin()
        convergeplot(1,MassAccr,figfilename='massaccrLX_s1.png',recalc=myrecalc)
        convergeplot(1,MassAccr,figfilename='normmassaccrLX_s1.png',normtohost=True)
        paper_stackplot(14,MassAccr,figfilename='stackLX14_massaccr_s1.png',lw=2)
        paper_stackplot(14,MassAccr,figfilename='stackLX14_normmassaccr_s1.png',lw=2,normtohost=True)
        convergeplot(1,LinMassAccr,figfilename='linmassaccrLX_s1.png')
        convergeplot(1,LinMassAccr,figfilename='normlinmassaccrLX_s1.png',normtohost=True)
        paper_stackplot(14,LinMassAccr,figfilename='stackLX14_linmassaccr_s1.png',lw=2)
        paper_stackplot(14,LinMassAccr,figfilename='stackLX14_normlinmassaccr_s1.png',lw=2,normtohost=True)
    if arg == 5:
        SubPhase   = SubPhaseContourPlugin()
        convergeplot(1,SubPhase,whichlx=[13,14],figfilename='subphaseLX_s1.png',recalc=myrecalc)
    if arg == 6:
        SubProfile     = SubProfilePlugin()
        SubVelProfile  = SubVelocityProfilePlugin()
        for lx in [12,13,14]:
            convergeplot(1,SubProfile,whichlx=[lx],figfilename='subprofLX'+str(lx)+'_s1.png',recalc=myrecalc)
            convergeplot(1,SubVelProfile,whichlx=[lx],figfilename='subvelprofLX'+str(lx)+'_s1.png')
            convergeplot(1,SubVelProfile,whichlx=[lx],figfilename='normsubvelprofLX'+str(lx)+'_s1.png',normtohost=True)

        TBTF = TBTFPlugin()
        convergeplot(1,TBTF,whichlx=[14],figfilename='tbtfLX14_s1.png')
    if arg == 7:
        SubRad         = SubhaloRadialPlugin()
        intSubRad      = IntegrableSubhaloRadialPlugin()
        SubRadByMass   = SubhaloRadialByMassPlugin()
        intSubRadByMass= IntegrableSubhaloRadialByMassPlugin()
        convergeplot(1,SubRad,figfilename='subradLX_s1.png',recalc=myrecalc)
        convergeplot(1,intSubRad,whichlx=[14],figfilename='intsubradLX14_s1.png')
        convergeplot(1,SubRadByMass,whichlx=[14],figfilename='subradbymassLX14_s1.png')
        convergeplot(1,intSubRadByMass,whichlx=[14],figfilename='intsubradbymassLX14_s1.png')

        SubRadSubmassFrac = SubhaloRadialSubmassFracPlugin()
        convergeplot(1,SubRadSubmassFrac,figfilename='subradsubmassfracLX_s1.png',recalc=myrecalc)
        paper_stackplot(14,SubRadSubmassFrac,figfilename='stackLX14_subradsubmassfrac_s1.png')
        ## these are now defunct
        #SubRadMass     = SubhaloRadialMassPlugin()
        #SubRadMassFrac = SubhaloRadialMassFracPlugin()
        #convergeplot(1,SubRadMass,figfilename='subradmassLX_s1.png',recalc=myrecalc)
        #convergeplot(1,SubRadMassFrac,figfilename='subradmassfracLX_s1.png')
        #stackplot(firsttwelve,14,SubRadMassFrac,figfilename='stackLX14_subradmassfrac_s1.png',color='k',alpha=.2)

    #testhid = firsttwelve[2]
    #haloplot(testhid,12,pluglist=[Nvmax,SHMF,Profile,MassAccr],recalc=myrecalc)
    #haloplot(testhid,14,pluglist=[SubPhase],recalc=myrecalc)
    #haloplot(testhid,12,pluglist=[SubProfile],recalc=myrecalc)
    #haloplot(1130025,14,pluglist=[SubVelProfile])

    plt.close('all')