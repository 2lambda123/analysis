import haloutils
from caterpillaranalysis import *
from caterpillarplot import *
import pylab as plt

if __name__=="__main__":
    Nvmax      = NvmaxPlugin()
    SHMF       = SHMFPlugin()
    intSHMF    = IntegrableSHMFPlugin()
    Profile    = ProfilePlugin()
    VelProfile = VelocityProfilePlugin()
    MassAccr   = MassAccrPlugin()
    SubPhase   = SubPhaseContourPlugin()

    SubProfile     = SubProfilePlugin()
    SubVelProfile  = SubVelocityProfilePlugin()
    SubRad         = SubhaloRadialPlugin()
    intSubRad      = IntegrableSubhaloRadialPlugin()
    SubRadMass     = SubhaloRadialMassPlugin()
    SubRadByMass   = SubhaloRadialByMassPlugin()
    intSubRadByMass= IntegrableSubhaloRadialByMassPlugin()
    SubRadMassFrac = SubhaloRadialMassFracPlugin()

    myrecalc = False
    #convergeplot(1,Nvmax,lw=2,figfilename='NvmaxLX_s1.png',recalc=myrecalc)
    #convergeplot(1,Nvmax,lw=2,figfilename='normNvmaxLX_s1.png',recalc=myrecalc)
    #convergeplot(1,SHMF,lw=2,figfilename='SHMFLX_s1.png',recalc=myrecalc)
    #convergeplot(1,SHMF,lw=2,figfilename='normSHMFLX_s1.png',recalc=myrecalc,normtohost=True)
    #convergeplot(1,intSHMF,lw=2,figfilename='intSHMFLX_s1.png',recalc=myrecalc)
    #convergeplot(1,Profile,figfilename='rhor2LX_s1.png',recalc=myrecalc)
    #convergeplot(1,VelProfile,figfilename='velprofLX_s1.png',recalc=myrecalc)
    #convergeplot(1,VelProfile,figfilename='normvelprofLX_s1.png',recalc=myrecalc,normtohost=True)
    #convergeplot(1,MassAccr,figfilename='massaccrLX_s1.png',recalc=myrecalc)
    #convergeplot(1,MassAccr,figfilename='normmassaccrLX_s1.png',recalc=myrecalc,normtohost=True)
    #convergeplot(1,SubPhase,whichlx=[13,14],figfilename='subphaseLX_s1.png',recalc=myrecalc)
    #convergeplot(1,SubProfile,whichlx=[12],figfilename='subprofLX12_s1.png',recalc=myrecalc)
    #convergeplot(1,SubProfile,whichlx=[13],figfilename='subprofLX13_s1.png',recalc=myrecalc)
    #convergeplot(1,SubProfile,whichlx=[14],figfilename='subprofLX14_s1.png',recalc=myrecalc)
    #convergeplot(1,SubVelProfile,whichlx=[12],figfilename='subvelprofLX12_s1.png',recalc=myrecalc)
    #convergeplot(1,SubVelProfile,whichlx=[13],figfilename='subvelprofLX13_s1.png',recalc=myrecalc)
    #convergeplot(1,SubVelProfile,whichlx=[14],figfilename='subvelprofLX14_s1.png',recalc=myrecalc)
    #convergeplot(1,SubVelProfile,whichlx=[14],figfilename='normsubvelprofLX14_s1.png',recalc=myrecalc,normtohost=True)
    convergeplot(1,SubRad,figfilename='subradLX_s1.png',recalc=myrecalc)
    convergeplot(1,intSubRad,whichlx=[14],figfilename='intsubradLX14_s1.png',recalc=myrecalc)
    convergeplot(1,SubRadByMass,whichlx=[14],figfilename='subradbymassLX14_s1.png',recalc=myrecalc)
    convergeplot(1,intSubRadByMass,whichlx=[14],figfilename='intsubradbymassLX14_s1.png',recalc=myrecalc)
    #convergeplot(1,SubRadMass,whichlx=[14],figfilename='subradmassLX14_s1.png',recalc=myrecalc)
    #convergeplot(1,SubRadMassFrac,figfilename='subradmassfracLX_s1.png',recalc=myrecalc)

    firsttwelve = get_haloidlist(1)
    #stackplot(firsttwelve,14,SHMF,color='k',alpha=.2,recalc=myrecalc)
    
    testhid = firsttwelve[2]
    #haloplot(testhid,12,pluglist=[Nvmax,SHMF,Profile,MassAccr],recalc=myrecalc)
    #haloplot(testhid,14,pluglist=[SubPhase],recalc=myrecalc)
    #haloplot(testhid,12,pluglist=[SubProfile],recalc=myrecalc)
    #haloplot(1130025,14,pluglist=[SubVelProfile])

    plt.close('all')
