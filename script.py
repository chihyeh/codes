import ROOT
import MannWhitneyUtest
import sys
from ROOT import TFile, TH1F, gDirectory, TCanvas, TPad, TProfile,TGraph, TGraphAsymmErrors
from ROOT import TH1D, TH1, TH1I
from ROOT import gStyle
from ROOT import gROOT
from ROOT import TStyle
from ROOT import TLegend
from ROOT import TMath
from ROOT import TPaveText
from ROOT import TLatex
from array import array

f1 = ROOT.TFile.Open(sys.argv[1], 'r')
f2 = ROOT.TFile.Open(sys.argv[2], 'r')

h1 = f1.Get("h_tau21_b1") #change the names of the histograms to the TH1's present in f1 and f2
h2 = f2.Get("h_tau21_b1")

#h1.Sumw2()
#h2.Sumw2()
#h1.Scale(1.0/h1.Integral())
#h2.Scale(1.0/h2.Integral())

#U = MannWhitneyUtest.mannWU(h1, h2)
#U_print = min (1-U, U)
#U_print_2_decimal=round(U_print,2)
#a=str(U_print_2_decimal)

a=h1.Integral()
b=h2.Integral()

xarray=array("f",[])
for i in range(25):
    xarray.append(h1.Integral(0+i,25)/a)
print xarray

yarray=array("f",[])
for j in range(25):
    yarray.append(1-h2.Integral(0+j,25)/b)
print yarray

#xarray=array("f",[h1.Integral(2,25)/a,h1.Integral(3,25)/a,h1.Integral(4,25)/a,h1.Integral(5,25)/a,h1.Integral(6,25)/a,h1.Integral(7,25)/a,h1.Integral(8,25)/a,h1.Integral(9,25)/a,h1.Integral(10,25)/a,h1.Integral(11,25)/a,h1.Integral(12,25)/a,h1.Integral(13,25)/a,h1.Integral(14,25)/a,h1.Integral(15,25)/a,h1.Integral(16,25)/a,h1.Integral(17,25)/a,h1.Integral(18,25)/a,h1.Integral(19,25)/a,h1.Integral(20,25)/a,h1.Integral(21,25)/a,h1.Integral(22,25)/a,h1.Integral(23,25)/a,h1.Integral(24,25)/a,h1.Integral(25,25)/a])
#yarray=array("f",[1-h2.Integral(2,25)/b,1-h2.Integral(3,25)/b,1-h2.Integral(4,25)/b,1-h2.Integral(5,25)/b,1-h2.Integral(6,25)/b,1-h2.Integral(7,25)/b,1-h2.Integral(8,25)/b,1-h2.Integral(9,25)/b,1-h2.Integral(10,25)/b,1-h2.Integral(11,25)/b,1-h2.Integral(12,25)/b,1-h2.Integral(13,25)/b,1-h2.Integral(14,25)/b,1-h2.Integral(15,25)/b,1-h2.Integral(16,25)/b,1-h2.Integral(17,25)/b,1-h2.Integral(18,25)/b,1-h2.Integral(19,25)/b,1-h2.Integral(20,25)/b,1-h2.Integral(21,25)/b,1-h2.Integral(22,25)/b,1-h2.Integral(23,25)/b,1-h2.Integral(24,25)/b,1-h2.Integral(25,25)/b])


c = TCanvas("c1", "c1",0,0,500,500)
#gStyle.SetOptStat(0)
#h1.SetLineColor(2)
#h1.SetLineWidth(3)
#h2.SetLineColor(1)
#h2.SetLineWidth(3)
#leg.AddEntry("","#sqrt{s}=40TeV","")
#leg.AddEntry(h1,"z'->qq","l")
#leg.AddEntry(h2,"z'->ww","l")

#if(h1.GetBinContent(h1.GetMaximumBin())>h2.GetBinContent(h2.GetMaximumBin())):
#        h1.Draw("hist")
#        h2.Draw("histsame")
#else:
#        h2.Draw("hist")
#        h1.Draw("histsame")

n=25
gr = TGraph(n,xarray,yarray)
gr.SetLineColor(2)
gr.SetLineWidth(5)
gr.SetLineStyle(2)
gr.SetMarkerColor(2)
gr.SetMarkerStyle(21)
gr.SetTitle("r009_tau21b1_5tev_eff")
gr.GetXaxis().SetTitle("signal_efficiency")
gr.GetXaxis().SetTitleColor(4)
gr.GetYaxis().SetTitle("1-background_efficiency")
gr.Draw()


#leg.AddEntry("","MannWhitneyUtest:","")
#leg.AddEntry("",a,"")
#leg.Draw()
c.Draw()


c.Print("r009_tau21_5tev_04_eff.pdf")
c.Print("r009_tau21_5tev_04_eff.root")
#where h1 and h2 are TH1s

