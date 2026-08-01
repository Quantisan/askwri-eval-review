---
doc_id: 2022_decarbonizing-chinas-road-transport-sector_2101
source_pdf: kp-docs/askwri-kps/2022_decarbonizing-chinas-road-transport-sector_2101.pdf
extraction_method: cache-plaintext
char_count: 240913
title: "Decarbonizing China's road transport sector: strategies towards carbon neutrality"
authors: Xue, Lulu; Liu, Daizong
date_published: 5/25/2022
article_type: Report
sub_tag: Transport decarbonization
wri_primary_office: WRI China
wri_programs: Cities
language: English
url: "https://www.wri.org/research/decarbonizing-chinas-road-transport-sector-strategies-toward-carbon-neutrality"
doi: "https://doi.org/10.46830/wrirpt.21.00145"
summary: "Decarbonizing China's road transport sector is crucial for achieving carbon neutrality by 2060, with potential GHG emissions reductions of 50-95% from 2020 levels depending on policy implementation. Utilizing the Low Emissions Analysis Platform (LEAP) model, the study identifies that vehicle electrification offers the greatest long-term decarbonization potential, while structural changes are more effective in the near term. Significant investments of 39-83 trillion CNY are required to transition effectively, emphasizing the need for enhanced structural changes and electrification strategies. The findings highlight the importance of ambitious policy measures to align with national carbon peaking and neutrality goals, particularly in freight transport, which could yield substantial emissions reductions."
---

# Decarbonizing China's road transport sector: strategies towards carbon neutrality

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
1
WRI.ORG.CN
LULU XUE   DAIZONG LIU
DECARBONIZING CHINA’S 
ROAD TRANSPORT SECTOR: 
STRATEGIES TOWARD 
CARBON NEUTRALITY

2
WRI.org.cn
Design and Layout by:
Harry Zhang  harryzy5204@gmail.com
ACKNOWLEDGEMENTS 
This project is part of the International Climate Initiative. 
The German Federal Ministry for Economic Affairs and 
Climate Action supports this initiative on the basis of a 
decision adopted by the Bundestag.
The authors would like to thank the Vehicle Emission 
Control Center (VECC) of the Ministry of Ecology and 
Environment of the People’s Republic of China for its 
tremendous support of this study. We would like to 
thank our World Resources Institute internal reviewers, 
Stephanie Ly, Erika Myers, Ben Welle, Amit Bhatt, Ang 
Li, and Xiaoqian Jiang. We would also like to thank our 
external reviewers, Dong Ma (VECC), Huanhuan Ren (China 
Automotive Technology and Research Center), Jie Guo 
(China Academy of Transportation Sciences), Wenjing 
Yi (Energy Research Institute of National Development 
and Reform Commission), Ye Wu (Tsinghua University), 
Yonghong Liu (Sun Yat-Sen University), Holger Dalkmann 
(Sustain2030), Jen Jungeun Oh (the World Bank), Yang 
Chen (the World Bank), Katharina Göckeler (Oeko-Institut), 
and Malithi Fernando (International Transport Forum), for 
their helpful comments and suggestions. We also thank 
three exceptional interns for wonderful support on model 
development and desktop research: Isabel Qi, Wenwei Bao, 
and Xiaohuan Zeng. 
Thank you also to Li Fang, Zhe Liu, Sarah DeLucia, Ye 
Zhang, Romain Warnault, Emilia Suarez, and Lauri Scherer 
for advisory, editing, design, and administrative support. 
https://doi.org/10.46830/wrirpt.21.00145

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
I
TABLE OF CONTENTS
III Executive Summary
1 Chapter 1.  Background
7 Chapter 2.  Forecast Methodology
8  Scope of the Analysis
10  Modelling Methodology
19 Chapter 3.  Scenario Design
20  Influencing Factors
20  Decarbonization Measures
43 Chapter 4.  Model Results
44  Base Year Calibration
46  Scenario Projections
55  Attribution Analysis
64  GHG Emissions and Air Pollutant Co-control 
Potentials
69 Chapter 5.  Conclusion and Discussion
73  Appendix A. Socioeconomic 
Assumptions and Demand Forecasting 
Methods
74  Appendix B. Lifetime Total Cost of 
Ownership Projection
79 Appendix C. Biofuel Considerations
80 Abbreviations
80 Endnotes
81 References

II
WRI.org.cn

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
III
EXECUTIVE SUMMARY
HIGHLIGHTS
 ▪ China’s road transport greenhouse gas (GHG) emissions will continue growing. However, if China 
implements its stated policies, road transport emissions could peak before 2030 and petroleum 
consumption before 2027 . The peaking timeline for GHG emissions could be further advanced to 2025 
and that for petroleum consumption to 2024 if China takes more proactive structural change measures 
(including mode shift and vehicle occupancy improvements). 
 ▪ If China implements all its stated policies, road transport’s GHG emissions in 2060 would decline by 50 
percent from the 2020 level. Further, if radical structural changes and vehicle electrification occur, road 
transport’s GHG emissions in 2060 would reduce by 95 percent from 2020’s level, fulfilling China’s 2060 
carbon neutrality commitment.  
 ▪ Over the long term, vehicle electrification offers the largest decarbonization potential, followed by 
structural changes, fuel efficiency improvements, and the decarbonization of power and hydrogen 
generation sectors. However, structural changes have the largest decarbonization potential in the near 
term (from now until 2035). 
 ▪ Public and private investments of 39–83 trillion Chinese yuan (CNY) cumulatively are needed from 2020 to 
2060 to decarbonize China’s road transport sector. 
 ▪ Air pollutant emissions from China’s road transport sector will decouple from GHG emission trajectories, 
demonstrating a steady declining trend.

IV
WRI.org.cn
Research Problem
Decarbonizing the transport sector globally is 
necessary to meet the Paris Climate Agreement 
goal of limiting warming to below 2 degrees Celsius 
(°C) or the more ambitious 1.5°C target. For China, 
doing so is also critical for meeting the country’s 
goals of peaking carbon dioxide emissions before 
2030 and being carbon neutral by 2060. Further, 
historical and projected trends for growth in 
China’s road transport sector demand have raised 
concerns over national energy security and local 
air pollution. 
At present, transport sectoral emission reduction 
targets and mitigation actions compatible with 
the carbon neutrality target have not yet been 
established. As indicated by the Action Plan for 
Carbon Dioxide Peaking before 2030, released 
by China’s State Council on October 26, 2021, 
petroleum consumption from the road transport 
sector should peak before 2030, with a goal to 
“keep the growth of carbon emissions in the 
transportation domain within an appropriate range” 
(NDRC 2021). This indicates that China’s transport 
emissions probably will not peak before 2030. 
However, existing modelling studies suggest that 
to meet the 2-degree (or 1.5-degree) goal, global 
transport emissions need to peak around 2020–25 
(IEA 2021a; Gota et al. 2018; Fransen et al. 2019). 
Within the transport sector, road transport 
represented the largest share—84.1 percent—of 
transport-related GHG emissions in China in 
2014 (MEE 2020a). To meet its carbon neutrality 
goal, China’s road transport sector needs explicit 
sectoral emission reduction targets, actionable 
strategies, and cost-effective policy instruments. 
This study examines how the sector might be 
decarbonized to inform the following: 
 ▪ The road transport sector’s target setting to help 
achieve China’s carbon peaking and neutrality 
goals  
 ▪ Identification of cost-effective measures that 
deliver on the sectoral emission reduction 
targets, facilitate low-carbon investments, and 
drive technological innovation 
 ▪ Identification of decarbonization measures with 
air pollution reduction co-benefits 
Using the Low Emissions Analysis Platform 
(LEAP) model, we constructed and analyzed the 
results of the following five forecasting scenarios 
(Table ES-1): 
 ▪ The Business as Usual (BAU) scenario is a 
counterfactual scenario, representing no 
improvement in energy efficiency and limited 
degrees of vehicle electrification to help evaluate 
the emissions reduction potential of China’s 
stated policies and the consequences of not 
meeting these targets.    
 ▪ The Stated Policy scenario (“Stated_policy”) is 
based on the stated policies announced by the 
national government and intended actions from 
industrial associations.  
 ▪ The Structural Change scenario (“Low_stock”) 
assumes greater degrees of transport structural 
changes (through two measures—mode shift 
and vehicle occupancy improvements), thereby 
featured by smaller vehicle stocks. 
 ▪ The Deep Electrification scenario (“DeepELE”) 
assumes more rapid diffusion of new energy 
vehiclesi (NEVs), with NEV passenger cars rep-
resenting 100 percent of passenger car sales by 
2035 and NEV medium- and heavy-duty trucks 
(HDTs) representing 100 percent of HDT sales 
by 2050.   
 ▪ The Deep Decarbonization scenario 
(“DeepDecarb”) integrates the Low_stock 
and DeepELE scenarios. Therefore, the 
scenario represents the most ambitious case 
that is compatible with China’s 2060 carbon 
neutrality target.

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
V
Table ES-1  |  Key Parameters in the Five Forecasting Scenarios
Abbreviations: tkm = tonne-kilometer; HDT = heavy-duty truck; NEV = new energy vehicle; ICE = internal combustion engine; L = liter; km = kilometer. 
Source: WRI authors’ assumptions. 
2020
BUSINESS 
AS USUAL
(BAU)
STATED POLICY
(Stated_policy)
STRUCTURAL 
CHANGE
(Low_stock)
DEEP 
ELECTRIFICATION
(DeepELE)
DEEP 
DECARBONIZATION
(DeepDecarb)
Demand and Structural Change 
Passenger car stock  
in 2020 and 2060 
(million vehicles)
239 
(170 cars per 
1,000 persons)
506 
(425 cars per 
1,000 persons)
506 
381 
 (300 cars per 1,000 
persons)
506 381 
Freight tkm  
in 2020 and 2060 
(trillion tkm)
11.2 25.9 
Freight mode share  
in 2020 and 2060
(% of road freight in 
domestic tkm)
54% 50% 50% 40% 50% 40%
Freight average load  
in 2020 and 2060
(tonnes per vehicle 
kilometer)
9.5 9.5 9.5 11.5 9.5 11.5
HDT stock  
in 2020 and 2060 
(million vehicles)
9.5 20 20 12 20 12
Vehicle electrification
Passenger car 
electrification  
in 2020 and 2035
(% of NEVs  
in passenger car sales)
15.7% 30% 50% 50% 100% 100% 
HDT electrification  
in 2020 and 2050
(% of NEVs in HDT 
sales)
0.6% 12% 
50% 
(only HDTs operating 
in urban deliveries, 
drayage, and 
regional delivery 
duty cycles)
50% 
(only HDTs operating 
in urban deliveries, 
drayage, and 
regional delivery 
duty cycles)
100% 
(all HDTs, including 
long-haul and 
refrigerated HDTs)
100% 
(all HDTs, including 
long-haul and 
refrigerated HDTs)
Fuel efficiency 
ICE passenger cars
Fleet average: 5.6 
L/100 km
Hybrid: 2.6% of car 
sales
No 
improvement
Fleet average: 4 L/100 km
Hybrid: 60% of car sales in 2025, 100% in 2035
ICE HDTs (Depends on gross 
vehicle weight)
No 
improvement HDTs: 20% improvement in 2035
NEVs (Depends on gross 
vehicle weight)
No 
improvement (Various degrees of improvement based on gross vehicle weight)
Grid and hydrogen decarbonization
Power mix 
 in 2020 and 2050
(% of non-fossil fuels  
in power mix)
32% 75% 92% 
Hydrogen mix  
 in 2020 and 2050
(% of gray hydrogen  
in production mix)
99% 35% 15%

VI
WRI.org.cn
Figure  ES-1  |   GHG Emission Projections under Different Scenarios
Research Findings 
Our models indicate the following: First, road 
transport GHG emissions in China would peak 
during 2025–35, and petroleum demand would 
peak during 2024–30 under all scenarios except 
for Business as Usual. Driven by increasing travel 
demand, China’s road transport GHG emissions 
would continue growing. Nonetheless, if China 
implements its stated policies (the Stated_
policy scenario), road transport emissions 
could peak before 2030 and petroleum 
consumption before 2027 (Figure ES-1). The 
peaking timeline for GHG emissions would 
be advanced to 2025 and that for petroleum 
consumption to 2024 at the earliest if China 
takes more proactive structural change 
measures that include mode shifting to 
low-emitting modes as well as increasing 
vehicle occupancy (DeepELE, Low_stock, and 
DeepDecarb scenarios). In the near term, structural 
changes are more effective at peaking emissions 
earlier and reducing emissions to a greater extent 
than vehicle electrification.
Second, over the long term, under different policy 
scenarios, the country can reduce road transport 
GHG emissions in 2060 by about 50–95 percent 
from the base year (2020). Specifically, if China 
implements its stated policies, its road 
transport GHG emissions in 2060 would 
decline by 50 percent from 2020’s level 
(the Stated_policy scenario). Further, if 
a radical shift in vehicle technologies and 
structural changes is made, road transport 
GHG emissions in 2060 would be reduced 
by 95 percent from the 2020 level, realizing 
China’s 2060 carbon neutrality commitment 
(the DeepDecarb scenario) (Figure ES-1). 
To achieve the largest emission reduction 
potential of 95 percent by 2060 in the 
DeepDecarb scenario, four measures—
namely, vehicle electrification, structural 
changes, fuel efficiency improvements, and 
power and hydrogen decarbonization—are 
critical (Figure ES-2 and Table ES-2):
 ▪ Vehicle electrification has the largest de-
carbonization potential, contributing 48 
percent of the cumulative GHG emission 
reduction from the BAU scenario to the Deep-
Decarb scenario during 2020–60. If the decar-
bonization of the power and hydrogen-related sec-
tors follows the roadmaps outlined by the national 
government and industrial associations, vehicle 
electrification could yield a cumulative 60 percent 
emission reduction. 
 ▪ Structural changes have the second-
largest mitigation potential and can cut 
cumulative GHG emissions from 2020 to 
2060 by 23 percent. Of note, in the near 
term (2020–35), structural changes have 
the largest mitigation potential because 
vehicle electrification is not likely to reach the 
tipping point during this time frame. 
Note: Greenhouse gases include carbon dioxide, nitrous oxide (N20), and methane (CH4). N2O and CH4 use 20-year global warming potential (GWP) values from IPCC (2014).  
Abbreviation: Mt CO2eq = million tonnes of carbon dioxide equivalent. 
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model. 
Low_stock
DeepELE
DeepDecarb
Stated_policy
BAU
20252020 20602050 20552030 2035 2040 2045
Mt CO2eq
0
500
2,000
1,500
1,000

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
VII
Figure  ES-2  |   GHG Reduction Potentials of Key Decarbonization Interventions
 ▪ Fuel efficiency improvements can generate 
17 percent of the cumulative emission re-
duction during 2020–60. Further, tightening 
the fleet-wide fuel efficiency standard is instru-
mental to stimulating NEV production, while NEV 
energy efficiency improvements help improve 
NEVs’ driving ranges as well as reduce vehicle 
weights and costs.
Whether natural gas (NG) vehicles should be 
treated as a viable decarbonization solution 
is worth further scrutiny. Although the carbon 
dioxide (CO2) emissions from NG vehicles are 
around 20 percent lower than those of diesel- and 
gasoline-powered vehicles, they have limited GHG 
emissions savings due to methane escape from NG 
vehicles (such as crankcase emissions or dynamic 
venting of the fuel system). This study shows that 
because of large methane leakage, an NG heavy-duty 
truck meeting the China 5 emission standard would 
tend to have higher tank-to-wheel GHG emissions 
than its diesel counterpart. Only when the China 
6 emission standard is stringently enforced would 
a China 6 NG heavy-duty truck reduce tank-to-
wheel GHG emissions by up to 12 percent. In the 
scenario analysis, when the market share of China 
6 NG heavy-duty trucks rises to 50 percent in 2050 
in the Stated_policy scenario (compared with the 
original 15 percent), the wider adoption of NG 
trucks would lead to an additional 7 percent GHG 
emission reduction in 2060 and less than a 3 percent 
cumulative GHG emission reduction from 2020 to 
2060, compared with the Stated_policy scenario. 
Abbreviations: Mt CO2eq = million tonnes of carbon dioxide equivalent; DeepDecarb = Deep Decarbonization scenario; H 2 = hydrogen; BAU = Business as Usual scenario.
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model. 
This study further reveals that for China to 
achieve its carbon neutrality goal, its stated 
policies need to include increased 
ambition on structural changes and vehicle 
electrification (Table ES-2):
 ▪ For structural changes, a 75–85 percent green 
transport mode share for passenger transport, 
40 percent road freight in the mode split for do-
mestic tonne-kilometers (tkm), and an average 
11.5 tonne load per truck-kilometer
 ▪ For vehicle electrification, NEVs would repre-
sent 100 percent of passenger car sales by 2035 
and 100 percent of HDT sales by 2050 
Reaching China’s carbon neutrality target 
has more pronounced implications for 
freight transport than it does for passenger 
transport. The DeepDecarb scenario shows 
that road freight transport could reduce GHG 
emissions by a cumulative 19,367 million tonnes 
of carbon dioxide equivalent (Mt CO 2eq) from 
2020 to 2060 compared with the BAU scenario, 
over two times the cumulative emission reduction 
associated with road passenger transport 
(9,250 Mt CO 2eq). To unlock road freight’s 
decarbonization potential, China needs to 
make technology advances in long-haul HDTs 
and refrigerated HDTs, promote freight mode 
shifts to railways and waterways, and improve 
freight logistic efficiency. China also needs to 
significantly improve its freight statistical data 
DeepDecarb
BAU
Mt CO2eq
20252020 20602050 20552030 2035 2040 2045
0
500
2,000
1,500
1,000
Passenger structural change
Freight structural change
Passenger electrification
Freight electrification
Fuel efficiency
Clean power/H2

VIII
WRI.org.cn
STRUCTURAL CHANGES VEHICLE ELECTRIFICATION FUEL EFFICIENCY 
IMPROVEMENTS
POWER AND HYDROGEN 
DECARBONIZATION
Targets in the Stated_policy scenario 
Passenger
transport
Targets:
425 cars per 1,000 persons, 70% green 
transport mode share in 2060a 
Targets:
By 2035: NEVs represent 50% of 
passenger car salesb 
By 2060: NEVs represent 100% of 
car salesc
Targets:
By 2025: Fleet-average fuel 
consumption for passenger cars 
of 4 L/100 km; hybrid vehicles 
represent 60% of passenger car 
sales (100% in 2035)d
By 2025: NEVs’ energy efficiency 
of 12 kWh/100 kme
Targets:
By 2050: 92% of non-fossil 
fuel in power mixf
Freight 
transport
Targets:
50% of road freight in domestic tkm; 
average load: 9.5 tonnes per vehicle-
kilometerg 
Targets:
By 2050: NEVs represent 50% 
of HDT sales (that is, the HDTs 
operating in urban deliveries, 
drayage, and regional delivery 
duty cycles)h 
Targets:
By 2035: 20% improvement in 
HDTs’ fuel consumptioni 
Continuous improvement in NEVs’ 
energy efficiency 
Targets:
By 2050: 15% of gray 
hydrogen in production mixj
Targets and policies in the DeepDecarb scenario
Passenger
transport
Targets:
300 cars per 1,000 persons, 75–85% 
green transport mode share in 2060
Targets:
NEVs represent 100% of 
passenger car sales in 2035
Same targets as the  
Stated_policy scenario
Same targets as the  
Stated_policy scenario
Tactics:
• Shift transit service paradigm with 
intelligent demand responsive services
• Increase the share of infrastructure 
investments in transit, active mobility, 
and railway 
• Pursue travel demand management 
and carbon pricing
• Promote Mobility-as-a-Service and ride 
sharing  
Tactics:
• Enhance fleet-wide fuel 
consumption standard
• Provide road access privileges 
to NEVs
• Increase infrastructure 
accessibility
• Introduce carbon taxes
Freight 
transport
Targets:
40% of road freight in domestic tkm; 
average load = 11.5 tonnes per HDT 
vehicle-kilometer
Targets:
NEVs represent 100% of HDT sales 
in 2050 (HDTs for short-range and 
long-range duty cycles)
Same targets as the  
Stated_policy scenario
Same targets as the  
Stated_policy scenario
Tactics:
• Shift bulk commodities to railways and 
waterways and promote intermodal 
freight for high-value freight
• Invest in intermodal infrastructure 
and equipment, improve service 
connectivity, rationalize pricing and 
scheduling, and enhance first-/last-
mile truck delivery
• Encourage the use of non-truck 
operating carriers and facilitate drop-
and-hook operations
• Employ fuel taxes and road charges
Tactics:
• Increase vehicle acquisition and 
introduce operation subsidies 
• Introduce fleet-wide fuel 
consumption standard for HDTs
• Introduce CO2-emission indexed 
road pricing 
• Provide road access privileges
• Increase infrastructure 
accessibility
Table ES-2  |  Key Targets and Policy Interventions to Realize the Carbon Neutrality Commitment
Note:  a. Extrapolated by the authors based on NDRC (2021). b. China SAE 2020. c. Extrapolated by the authors. d. MIIT 2019, 2021; China SAE 2020. e. State Council 2020. f. ICCSD 2020.  
g. Extrapolated by the authors based on NDRC (2021). h. Extrapolated by the authors. i. China SAE 2020. j. CHA 2019.

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
IX
collection system to support evidence-based 
policymaking in the above areas. 
The results show that low-carbon investments 
amounting to 39–83 trillion CNY 
cumulatively are needed from 2020 to 2060 
to decarbonize China’s road transport sector. 
The investment demand is the largest from now till 
2035 and will steadily decline over time. Among all 
the scenarios, the Low_stock scenario is the 
lowest-cost pathway, with an average abatement 
cost of 675 CNY per tonne of CO2eq reduced thanks 
to an associated smaller vehicle fleet (Figure ES-3). 
Structural changes are the least-expensive 
measure among all the decarbonization measures 
because a smaller vehicle fleet size reduces needed 
investments in installed capacities for power and 
Stated_policy DeepELE Low_stock DeepDecarb
Cumulative low-carbon investments
(billion CNY, 2020 value) 39,503 83,896 22,070 54,226
Average abatement cost
(CNY per tonne of CO 2eq reduced) 1,852 2,510 675 1,331
hydrogen generation and transmission as well as 
investments in vehicle acquisition and charging 
(and refueling) infrastructure expansion. 
Vehicle electrification’s abatement costs vary 
significantly over time. Only after the total cost 
of ownership parity for NEV heavy-duty trucks is 
reached (around 2030–35) will NEVs exhibit net 
cost savings compared with internal combustion 
engine (ICE) vehicles. However, the high 
abatement costs of vehicle electrification should 
not deter relevant investments.
After the introduction of the China 6 emission 
standardii (hereafter referred to as the China 6 
standard), road transport’s air pollutant 
emissions would decouple from GHG 
emissions trajectories, showing a steady 
Figure  ES-3  |   Low-Carbon Investments (2020–60) under Different Scenarios
 Abbreviations:  CNY = Chinese yuan; CO2eq = carbon dioxide equivalent; Stated_policy = Stated Policy scenario; DeepELE = Deep Electrification scenario;  
Low_stock = Structural Change scenario; DeepDecarb = Deep Decarbonization scenario.
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model. 
Low_stockDeepELE DeepDecarbStated_policybillion CNY, 2020 value
20252020 20602050 20552030 2035 2040 2045
0
500
4,000
3,500
3,000
2,000
1,500
2,500
1,000

X
WRI.org.cn
declining trend (Figure ES-4). Despite this 
achievement, air pollution abatement 
efforts should be sustained because non-road 
transport sectors such as inland waterways and 
non-road machinery also contribute significant 
amounts of air pollutants, and the next-generation 
China exhaust emission standard (such as a Euro 
7 equivalent standard) would be conducive to 
accelerating NEV adoption. This study further 
shows that for the aforementioned decarbonization 
measures to produce air pollution reduction 
co-benefits, additional measures are necessary, 
including improving railways and waterways’ 
freight operational efficiency, promoting railway 
electrification, tightening the China 6 standard, 
and improving in-use vehicles’ inspection/
maintenance programs (Table ES-3). 
Figure  ES-4  |   Air Pollutant Emissions from the Road Transport Sector
 Abbreviations: CO = carbon monoxide; NOx = nitrogen oxides; PM2.5 = particulate matter 2.5 micrometers or less in diameter; NMHC = non-methane hydrocarbons.
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model. 
CO
PM2.5
NOx
NMHC
Low_stockDeepELE DeepDecarbStated_policyBAU
million tonnes
million tonnes
million tonnes
million tonnes
2025 2025
2025 2025
2020 2020
2020 2020
2060 2060
2060 2060
2050 2050
2050 2050
2055 2055
2055 2055
2030 2030
2030 2030
2035 2035
2035 2035
2040 2040
2040 2040
2045 2045
2045 2045
0 0
0 0
6 6
0.14 4
4 4
0.12
0.10
0.08
0.06
3
2 2
0.04
0.02
2
1

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
XI
RESEARCH CO-CONTROL EFFECTS POLICY IMPLICATIONS
Fuel efficiency 
standards
This study General fuel efficiency measures: 
Reduce GHG emissions, neutral to air 
pollutants
--
O’Driscoll et al. 2018 Hybrid (gasoline) vehicles:  
Reduce GHG emissions and air pollutants
Promote hybrid (gasoline) 
vehicles
Liang et al. 2012
Saliba et al. 2017
O’Driscoll et al. 2018
Gasoline direct injection:  
Reduce GHG emissions but increase air 
pollutants
Enforce China 6 standard 
and enhance inspection/ 
maintenance programs for in-use 
vehicles
NG vehicle  
promotion
This study
Mottschall et al. 2020
T&E 2020a
NG vehicles:  
Possibly increase GHG emissions, 
reduce/ neutral to air pollutants
Tighten China 6 standard on non-
tailpipe CH 4 emissions from NG 
vehicles, enhance inspection/
maintenance programs
NEV promotion
This study NEV promotion:  
Reduce GHG emissions and air pollutants --
Peng et al. 2021 NEVs and upstream emissions:  
Reduce GHG emissions, increase 
upstream air pollutants
Couple NEV promotion with the 
decarbonization of the upstream 
power and industrial sector
Passenger structural 
changes
This study Passenger structural changes:  
Reduce GHG emissions and air pollutants --
Freight structural 
changes
This study Freight structural changes:  
Reduce GHG emissions and air pollutants --
Shao 2020 Freight structural changes  
(mode shift to railways):  
Reduce GHG emissions, increase 
upstream air pollutants
Decarbonize the upstream 
power sector, promote railway 
electrification, and reduce 
railway backhauls 
Table ES-3  |  The Co-control Effects of Different Decarbonization Measures
Note:  Green cells  indicate that the measure can reduce both GHG emissions and air pollutants, and yellow cells  mean that the measure can reduce only GHG/ air pollutant 
emissions. 
Abbreviations: GHG = greenhouse gas; CH4 = methane; NG = natural gas; NEV = new energy vehicle. 
Source: WRI authors, based on this study and existing literature.

XII
WRI.org.cn

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
1
BACKGROUND
Decarbonizing the transport sector globally is necessary to meet the 
Paris Climate Agreement goal of limiting warming to below 2 degrees 
Celsius (°C) or the more ambitious 1.5°C target. For China, doing so is 
also critical for meeting the country’s goals of peaking carbon dioxide 
emissions before 2030 and being carbon neutral by 2060.
CHAPTER 1

2
WRI.org.cn
Residential, 6%
Commercial, 7%
Agriculture, 10%
Industry, 23%
U.S. territories, 0%
Transport, 29%
Electricity 
generation, 25%
Waste, 3%
Agriculture, 13%
Residential and 
commercial, 13%
Transport, 24%
Energy supply, 26%
Industry, 21%
Residential, 5%
Waste, 4%
Commercial, 7%
Agriculture, 11%
Agriculture, 9%
Residential and 
commercial, 13%
Industry, 26%
Transport, 14%
U.S. territories, 0%
Transport, 24%
Electricity 
generation, 29%
Energy supply, 33%
Industry, 25%
Transport, 4% Transport, 7%
Others, 96% Others, 93%
In China, transport sector greenhouse gas (GHG) 
emissions equated to 828 million tonnes of carbon 
dioxide equivalent (Mt CO2eq) in 2014, representing 
6.7 percent of the country’s GHG emissions, 
excluding land use, land-use change, and forestry 
(LULUCF) emissions (MEE 2018a). However, if the 
sectoral emissions continue their upward growth 
trend, this share will enlarge. In fact, even in the 
developed world, such as the 27 members of the 
European Union (EU 27) plus the United Kingdom 
(UK) and the United States, transport-related GHG 
emissions have been increasing since 1990, in 
contrast to the general decreasing emissions trends 
in the power and industrial sectors. In 2019, the 
transport sector accounted for 28.6 percent and 23.6 
percent of total GHG emissions (excluding LULUCF 
emissions) in the United States and EU, respectively, 
rising to become the largest emitter in the United 
States and second-largest emitter in the EU (EEA 
2020; EPA 2020) (Figure 1). 
Figure  1  |   Transport Emissions Growth Trajectories and the Shares of Transport Emissions in Total Greenhouse 
Gas Emissions (excluding LULUCF) in the United States, EU 27 plus UK, and China
U.S. GHG emissions in 1990 U.S. GHG emissions in 2019
EU 27 plus UK GHG emissions in 1990 EU 27 plus UK GHG emissions in 2019
Chinese GHG emissions in 1994 Chinese GHG emissions in 2014
Note:  The most recent official record of China’s transport GHG emissions is from 2014—the country needs to improve the frequency of its national GHG emission reporting to keep pace 
with the rapid growth in emissions. China’s emission trajectory is a linear extrapolation of the emission data points in 1994, 2005, 2010, 2012, and 2014.
Abbreviations:  GHG = greenhouse gas; LULUCF = land use, land-use change and forestry; EU 27 = the 27 members of the European Union; UK = United Kingdom;  
Mt CO2eq = million tonnes of carbon dioxide equivalent.
Sources: EPA 2020; EEA 2020; NDRC 2004, 2012, 2016; MEE 2018a, 2018b. 
United States
EU 27+UK
China
Mt CO2eq
201920112005 2008 2014 201719991991 1993 1996 2002
0
500
2,500
2,000
1,500
1,000

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
3
China’s transport GHG emissions contribute 
significantly to global transport GHG emissions.  
They accounted for 11.1 percent of the world’s 
transport GHG emissions in 2018 (Climate 
Watch 2020), following only the United States 
(21.3 percent) and EU 27 plus UK (11.2 percent). 
In the future, China’s transport sector’s global 
contribution could be even greater: It is projected 
that China will have the most road freight activities 
in the world by 2050 (Mulholland et al. 2018) and 
that China and India combined will experience 
the most rapid growth in car ownership, six times 
greater than in 2015, standing in contrast to 16 
percent growth in Organisation for Economic 
Co-operation and Development (OECD) countries 
(ITF 2019). Historical and projected growth trends 
for travel demand in China’s road transport sector 
have raised concerns over national energy security, 
local air pollution, and GHG emissions (Yin et al. 
2015; Hao et al. 2015).
Within the transport sector, mitigating road 
transport emissions is critical to achieving 
China’s 2060 carbon neutrality target. In 2014, 
GHG emissions from road transport represented 
84.1 percent of China’s transport-related GHG 
emissions. Further, unlike aviation and maritime 
shipping where decarbonization efforts are hindered 
by immature technologies and high abatement 
costs, major technology breakthroughs such as 
electric powertrains and hydrogen fuel cells already 
exist for road transport (BloombergNEF 2021).  
In China, sectoral emission reduction targets 
and decarbonization strategies compatible with 
the carbon neutrality target have not yet been 
established. As indicated by the Action Plan for 
Carbon Dioxide Peaking before 2030, released 
by China’s State Council on October 26, 2021, 
petroleum consumption from the road transport 
sector should peak before 2030, with a goal to 
“keep the growth of carbon emissions in the 
transportation domain within an appropriate 
range” (NDRC 2021). This indicates that Chinese 
transport emissions probably will not peak 
before 2030. However, existing modelling studies 
suggest that to meet the 2°C (or more ambitious 
1.5°C) target, global transport emissions need 
to peak around 2020–25 (IEA 2021a; Gota et al. 
2018; Fransen et al. 2019). To that end, China’s 
road transport sector needs explicit sectoral 
emission-reduction targets, actionable strategies, 
and cost-effective policy instruments. Therefore, 
this study aims to inform the following: 
 ▪ The road transport sector’s target setting to help 
achieve China’s carbon peaking and neutrality 
targets 
 ▪ Identification of cost-effective measures that de-
liver on the sectoral target, facilitate low-carbon 
investments, and drive technology innovation
 ▪ Identification of decarbonization measures with 
air pollution reduction co-benefits (see Box 1).

4
WRI.org.cn
Box  1  |   Transport-Related Air Pollutant Emissions in China
The transport sector is a major contributor to air pollution in 
China, accounting for about 20–50 percent of emissions of 
particulate matter 2.5 micrometers or less in diameter (PM2.5) 
in Chinese cities; in some cities such as Shenzhen, Beijing, and 
Guangzhou, the transport sector is the largest source of PM2.5 
emissions, representing 52 percent, 45 percent, and 22 percent 
of local PM2.5 emissions in those cities, respectively.a 
Although unlike GHG emissions, road transport does not 
dominate air pollutant emissions, it emits more hydrocarbons 
(HC) and nitrogen oxides (NOx) than the non-road transport 
sectors do. 
Figure  B1.1  |   Emissions from the Road and Non-road Transport Sectors 
GHG emissions (2014) 
Hydrocarbon emissions (2020) 
 NOx emissions (2020)
PM emissions (2020)  
Note: The non-road transport sector includes the domestic shipping, domestic aviation, and non-road machinery sectors.
Abbreviations: GHG = greenhouse gas; NOx = nitrogen oxides; PM = particulate matter.
Source: MEE 2018a, 2021. 
Box Notes: a. MEE 2018c.  
Non-road 
transport 
43%
Non-road 
transport 
78%
Non-road 
transport 
18%
Shipping 
9%
Aviation 
6%
Rail 
1%
Road 
transport 
 57%
Road 
transport 
 22%
Road 
transport 
 82%
Road 
transport 
 84%
Other 
 0%

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
5
Box  1  |   Transport-Related Air Pollutant Emissions in China (Cont.) 
Since China rolled out its Three-Year Action Plan to Win the 
Blue-Sky Defence Battle in 2018, road transport–related air 
pollutants have been dropping (see Figure B1.2).b For annual 
concentrations of air pollutants to meet the National Ambient 
Air Quality Standard, the country has taken decisive actions, 
including introducing a China 6 emission standard, promoting 
the adoption of new energy vehicles, improving fuel quality, and 
facilitating the freight mode shift from roadways to railways and 
waterways. However, these measures have not corresponded 
to a commensurate impact on decarbonization—although road 
transport–related air pollutant emissions have begun to decline, 
GHG emissions are still growing (Figure B1.2). 
As China increases its public investments to curb environmental 
degradation and improve air quality (from 880.6 billion CNY in 
2015 to 1,063.9 billion CNY in 2020), the cost effectiveness of 
the investments could be improved.c At present, the Ministry of 
Ecology and Environment is responsible for reducing pollution, 
while the National Development and Reform Commission 
is tasked with reducing carbon dioxide emissions. The 
counterbalancing effects between decarbonization measures 
and pollution reduction measures can be overcome through 
interdepartmental coordination and coordinated policymaking. 
Figure  B1.2  |  Annual Air Pollutant Emissions from China’s Road Transport Sector (2011–20) 
Figure Notes: The sudden shifts in pollutants in 2019 were due to changes in pollutant accounting methods and updates to emission surveys. 
Figure Abbreviations: CO/10 = CO emissions divided by 10; HC = hydrocarbon; NOx = nitrogen oxides; PM*10 = particulate matter times 10. 
Figure Sources: MEE 2011, 2012, 2013, 2014a, 2015, 2016, 2017 , 2018c, 2019, 2020a, 2021; NBS 2011, 2012, 2013, 2014, 2015, 2016, 2017 , 2018, 2019, 2020, 2021.  
Box Notes: b. MEE 2018d. c. NBS 2017 , 2020.
NOx PM*10 Vehicle stocksHCCO/10
10,000 tonne emissions
100 million vehicles
20122011 20202013 2014 2015 2016 2017 2018 2019
0 0
700
2
300
1,000 3
900
2.5
600
800
400
500 1.5
200
1
0.5
100

6
WRI.org.cn

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
7
FORECAST 
METHODOLOGY 
This study examines how China's road transport sector might be 
decarbonized by modelling five scenarios using the Low Emissions 
Analysis Platform (LEAP) model. This chapter describes the vehicle 
classification, the emission scopes, and the methods used for 
transport emission accounting and abatement cost estimation.  
CHAPTER 2

8
WRI.org.cn
2.1 Scope of the Analysis
In this study, the road transport sector includes 
passenger carriers, goods carriers, and motorcycles. 
Non-road transport sectors such as aviation, shipping, 
pipelines, and off-road machinery are not covered. 
Table 1 provides an overview of China-specific vehicle 
classification. Given different activity levels and 
driving cycles, buses and taxies are separated from 
“large coaches” and “cars” as independent classes. 
The distribution of various vehicle types in 2020 is 
shown in Figure 2.  
CLASS DESCRIPTION THIS STUDY
Passenger 
carriers 
Large coaches Automobiles used to transport more than 20 people (vehicle length above 6 meters). 
Medium coaches Automobiles used to transport 10 to 19 people (vehicle length below 6 meters).
Cars Automobiles used to transport 9 people or fewer (vehicle length above 3.5 
meters and below 6 meters). 
Mini cars Automobiles used to transport 9 people or fewer (vehicle length of no more 
than 3.5 meters and engine cylinder capacity of no more than 1 liter).
Goods
carriers
Heavy-duty trucks GVW over 12 tonnes and below 49 tonnes 
Medium-duty trucks GVW above 4.5 tonnes and below 12 tonnes
Light-duty trucks GVW above 1.8 tonnes and below 4.5 tonnes
Mini-duty trucks GVW below 1.8 tonnes
Other
carriers
Special purpose 
vehicles
Special purpose vehicles such as street-sweeping vehicles, cranes, cement 
mixer trucks, and refuse haulers, with the exclusion of those used for 
passengers or goods shipments  
Low-speed vehicles Three- or four-wheelers with a maximum speed of no higher than 70 km per hour
Motorcycles Motorcycles Motorcycles powered by fossil fuels or electricity with a max speed over 25 
km per hour  
Trailers Trailers Trailers are unpowered vehicles, designed for carrying goods 
Table 1  |   Vehicle Classification Based on the Standard on Road Traffic Management—Types of Motor Vehicles 
(GA802–2019)
Abbreviations: GVW = gross vehicle weight; km = kilometer. 
Source: MPS 2019.

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
9
Note:  According to the China Bicycle Association, China has 0.3 billion motorcycles (including e-scooters) (Xinhua News 2020)—a larger fleet size than passenger cars. However, because 
many motorcycles are unregistered, research relying on official statistics, which count only 68 million, would underrepresent motorcycles.  
Sources: NBS 2021.
Figure  2  |   Distribution of Vehicle Types in China in 2020
The scope of GHG emissions in this study includes 
well-to-wheel (WTW) emissions—including 
well-to-tank (WTT) emissions, especially from 
electricity/hydrogen generation—and tank-to-
wheel (TTW) emissions from vehicle operations. 
Although this approach differs from the 
Intergovernmental Panel on Climate Change’s 
(IPCC’s) guidelines on national GHG inventories 
(IPCC 2006) where transport’s WTT emissions are 
counted toward the power and industrial sectors 
(and NEVsiii count as zero emissions), our approach 
enables us to evaluate whether the large-scale 
adoption of NEVs could actually cut emissions. 
Further, the emissions from the production and 
maintenance of vehicles and construction and 
maintenance of infrastructure are not included. 
The GHG emissions covered in this study include 
CO2, methane (CH4), and nitrous oxide (N2O). 
 ▪ CO2 is primarily released through fuel combus-
tion and upstream electricity/hydrogen gen-
eration. Since it represents the largest share of 
transport-related GHG emissions, it falls within 
the scope of this study. 
 ▪ CH4 is emitted via fuel combustion from motor 
vehicles and methane leaked from natural gas 
(NG) vehicles (Mottschall et al. 2020). Recent 
research shows that for lean burn NG vehicles—
a type of engine common in China that relies 
on a high air-to-fuel ratio—methane leakage is 
considerable: The CH4 emission factor for China 
5 NG vehicles is eight times higher than the 
IPCC’s default value (Pan et al. 2020). As NG 
vehicles are widely used in China, we included 
CH4 emissions in this study.    
 ▪ N2O is emitted via fuel combustion and after-re-
treatment of exhaust gases. In particular, higher 
emissions of N2O are found in diesel vehicles 
in compliance with higher emission standards 
such as China 5 and China 6. This is because 
the use of advanced aftertreatment systems to 
reduce NOx emissions leads to increased N2O 
emissions (Clairotte et al. 2020). With the roll-
out of the China 6 emission standard, N2O emis-
sions are likely to increase and so are included 
in this study.  
 ▪ Hydrofluorocarbons (HFCs) such as HFC-134a 
(1,1,1,2-tetrafluoroethane) result from leaks and 
the end-of-life disposal of air conditioners used 
in vehicles (EPA 2015). Although HFC-134a 
has a low ozone-depleting potential, its global 
warming potential (GWP) is large. But due to 
Mini cars and cars, 
8 7. 5 %
Medium 
coaches, 
0.3%
Large 
coaches, 
0.3%
Medium- and 
heavy-duty 
trucks, 3.5%
Mini- and 
light-duty 
trucks, 7 .7%
Taxis, 0.5%
Buses, 0.3%
Trailers, 6% 12.5%
Motorcycles, 19%
Passenger carriers 
and goods carriers, 
75%

10
WRI.org.cn
limited data availability, we did not include 
HFC emissions in this study.
Air pollutants in this study include only TTW 
emissions since the major health impact from 
transport air pollutants is on the tailpipe side 
(TTW). In this study, TTW emissions include 
exhaust emissions and evaporative emissions; tire 
and brake wear emissions are not covered due to a 
lack of localized emission factors (Table 2).  
The air pollutants considered in this study are the 
pollutants regulated in the China 1–6 vehicle emissions 
standards including carbon monoxide (CO), nitrogen 
oxides (NOx), non-methane hydrocarbons (NMHC), 
CH4, N2O, fine particulate matter (PM2.5), and coarse 
particulate matter (PM10, particulate matter 10 
micrometers or less in diameter). Notably, there are 
overlaps between air pollutants and GHG emissions. 
For example, PM10 also includes black carbon, a type 
of short-lived climate pollutant with significant GWP, 
while GHG emissions like CH4 and N2O are also air 
pollutants. For simplicity, the GHG emissions in this 
study include only CO2, CH4, and N2O (hence, CH4 and 
N2O are not treated as air pollutants).    
2.2 Modelling Methodology
2.2.1 Emissions accounting and forecasting
We modelled current and future GHG and air 
pollutant emissions mostly using the Low Emissions 
Analysis Platform (LEAP) (Heaps 2022). As an 
integrated assessment model, LEAP can capture the 
interactions between supply sectors (e.g., power) 
and demand sectors (e.g., transport), such as the 
impact of energy demand on energy prices (Yeh 
et al. 2017). For simplicity, this study focuses on 
the transport sector alone, without endogenous 
interactions with supply sectors.
To estimate base-year GHG emissions, we 
used the bottom-up method in LEAP (Equation 1). 
To estimate air pollutants, we used MEE (2014b) to 
Notes:  a. Emissions were calculated but not analyzed in-depth for decarbonization measures. 
b.  Carbon dioxide emissions from urea consumption in the selective catalytic reduction system—a type of pollutant aftertreatment device to reduce nitrogen oxides—are not 
considered due to limited emissions.
c. Evaporative emissions include hot soak, diurnal, and running loss emissions; refueling emissions are not accounted for. 
Abbreviations: WTT = well to tank; TTW = tank to wheel; GHG = greenhouse gas.
Sources: Text: WRI authors. Graphics: HPK 2019.
Table 2  |  The Scopes of Greenhouse Gas and Air Pollutant Emissions in This Study
WELL-TO-TANK EMISSIONS TANK-TO-WHEEL EMISSIONS
electrical charge
refueling
power generation
oil refining
GHG 
emissions
GHG 
emissions
Air 
pollutants
Air 
pollutants
TYPES OF WTT EMISSIONS THIS STUDY
•   Emissions from raw material extraction 
(and/or land use changes) 
•   Emissions from oil refineriesa
•   Emissions from electricity/hydrogen 
generation
•   Emissions from raw material 
extraction (and/or land use changes)
•   Emissions from oil refineries and 
electricity/hydrogen generation
TYPES OF WTT EMISSIONS THIS STUDY
•  Fuel combustion emissions 
•  Methane leakage emissions 
•   Emissions from urea-based catalytic 
converters b
•  Fuel combustion emissions
•  Evaporative emissionsc 
•   Tire and brake wear emissions
driving a vehicle 
(combustion engine)
driving a vehicle 
(electric)

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
11
calculate both exhaust emissions (Equation 2) and 
evaporative emissions (Equation 3).  
 ▪ For CO2 emissions: 
       E=∑i Pi×FEi×VKTi×EFi   (Equation 1)
where, 
E represents CO2 emissions (kilograms; kg)
Pi  is the vehicle stock of vehicle segment i (number 
of vehicles)
FEi  is the fleet-average fuel efficiency of vehicle 
segment i (in liters per 100 kilometers [L/100 
km] for diesel and gasoline, megajoules per 
100 kilometers [MJ/100 km] for natural gas, 
kilowatt-hours per 100 kilometers [kWh/100 
km] for electricity, and kilograms per 100 
kilometers [kg/100 km] for hydrogen) 
VKTi  is the average annual vehicle kilometers 
travelled of vehicle segment i (km) 
EFi  is the CO2 emission factor of different energies 
(kg/L, kg/MJ, kg/kWh). For electricity and 
hydrogen, EFi is the upstream WTT emission 
factors for power and hydrogen generation and 
distribution. For electricity distribution, an 8 
percent transmission and distribution loss and 
charging efficiency loss is assumed.
 ▪ For exhaust air pollutants, CH4, and N2O:
       E=∑i Pi×EFi×VKTi (Equation 2)
where, 
E  represents exhaust air pollutant, CH4, or N2O 
emissions (kg)
EFi  represents the emission factors for air 
pollutants, CH4, and N2O for vehicle segment i 
(kg/km) 
 ▪ For evaporative air pollutants:
       E=(EFrunning×  VKT  +EFsoak+diurnal×365)×Pi         
 (Equation 3)
where, 
E is evaporative pollutant emissions (kg)
EFrunning  is the emission factor for running losses 
(kg/hour) 
EFsoak+diurnal  is the emission factor for hot soak and 
diurnal emissions (kg/day) 
V is the average vehicle speed (km/hour) 
To forecast future emissions, we employed 
the vehicle fleet turnover model in LEAP. For each 
year, we projected the total number of vehicle 
stocks. Then we calculated annual vehicle sales 
based on vehicles’ survival rates and the annual 
growth (or decrease) in vehicle stocks. We applied 
the market shares of different vehicle technologies 
to the new sales to obtain the fleet composition by 
vehicle technology. We used the latter for emission 
forecasting following Equations 1, 2, and 3.   
As a technology-rich model, LEAP is capable 
of modelling the decarbonization potentials of 
low-carbon technology deployment. However, it 
does not model the effects of structural changes 
(including mode shift and vehicle occupancy 
improvements) well. To make up for this weakness, 
we developed a Microsoft Excel–based model to 
forecast future travel demand and vehicle stocks 
affected by structural changes. Because of varying 
degrees of data availability, we used a tonne-
kilometer (tkm) method for freight transport and a 
vehicle-centric method for passenger transport (see 
Figures 3 and 4 and Appendix A).
Using the tkm method, we projected future freight 
vehicle stocks based on the growth in domestic 
freight tkm, mode share of road freight, and truck 
load improvements. Therefore, the effects of 
structural changes were explicitly modelled for 
freight transport. However, applying the same 
method to passenger transport was challenging 
because data on the total passenger kilometers 
travelled (pkm) and vehicle occupancy rates were 
not available—China’s official statistical system 
does not cover the travel activities of private cars. 
Therefore, we used the vehicle-centric method 
for passenger transport, where passenger vehicle 
stocks were projected based on historical trends and 
qualitative evaluations of the impacts of structural 
changes based on a literature review. 
We localized the model inputs based on official 
statistical data, model estimates, a literature review, 
and expert consultations. See Table 3 for a qualitative 
assessment of the quality of the data inputs. As the 
emission estimates from bottom-up approaches 
are affected by the limited data quality of vehicle 
kilometers travelled (VKTs), we validated the bottom-
up emission estimate in the base year with the top-
down estimate using national energy balances. 
N
N
V

12
WRI.org.cn
Figure  3  |   Emission Forecasting for Freight Transport
Figure  4  |   Emission Forecasting for Passenger Transport
Notes:  The dotted box areas represent the calculations performed in the authors’ Microsoft Excel–based model. The unshaded areas represent the work performed in the Low Emissions 
Analysis Platform model. 
Abbreviations:  GDP = gross domestic product; tech. = technology; VKT = vehicle kilometers travelled; GHG = greenhouse gas; TTW = tank to wheel; WTT = well to tank;  
COPERT = A software program used to calculate air pollutant and GHG emission factors for the road transport sector (Ntziachristos et al. 2009).
Source: WRI authors.
Notes:  The dotted box areas represent calculations performed in the authors’ Microsoft Excel–based model. The unshaded areas represent the work performed in the Low Emissions 
Analysis Platform model. 
Abbreviations:  GDP = gross domestic product; tech. = technology; VKT = vehicle kilometers travelled; GHG = greenhouse gas; TTW = tank to wheel; WTT = well to tank;  
COPERT = A software program used to calculate air pollutant and GHG emission factors for the road transport sector (Ntziachristos et al. 2009).
Source: WRI authors.
Tonne-
kilometers
•  Policy review 
•  Empirical evidence
•  Policy review 
•  COPERT estimates
•  Policy review 
•  Empirical evidence
•  Policy review 
•  Empirical evidence
•  Policy review 
•  COPERT estimates
• Elasticity 
estimates
Road
tonne-
kilometers
Total 
vehicle 
stock
Vehicle 
stocks by 
tech.
GHGs 
and air 
pollutants
Fuel 
consumption
Vehicle-
kilometers
Vehicle-
kilometers
Vehicle 
sales
Vehicle survival 
rates and scrappage
TTW emission 
factors
Population 
and GDP
Freight 
mode 
shares
Load 
factor
VKT per 
vehicle
VKT per 
vehicle
Vehicle fuel 
efficiency
Vehicle tech. 
market shares
WTT emission 
factors
Total vehicle 
stocks
•  Policy review 
•  Empirical evidence
•  Policy review 
•  COPERT estimates
•  Policy review 
•  Empirical evidence
•  Policy review 
•  Empirical evidence
•  Policy review 
•  COPERT estimates
• Gompertz 
curves
Vehicle 
sales
GHGs and air 
pollutants
Fuel 
consumption
Vehicle 
stocks by 
tech.
Vehicle-
kilometers
Vehicle survival 
rates and scrappage
TTW emission 
factors
Population 
and GDP
VKT per 
vehicle
Vehicle fuel 
efficiency
Vehicle tech. 
market shares
WTT emission 
factors

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
13
Notes:   a.  represents a high level of confidence,  represents moderate confidence, and  represents a low level of confidence. b. Song 2017 .
Abbreviations: VKTs = vehicle kilometers travelled; ICE = internal combustion engine; A/C = air conditioning; NEV = new energy vehicle; CH4 = methane; N2O = nitrous oxide; TTW = tank to wheel. 
Table 3  |   Qualitative Assessment of the Data Sources Used to Estimate Emissions 
VARIABLES SOURCES DATA QUALITY
Vehicle stocks  
in base year NBS 2021  High a
Vehicle  
age profiles  
in base year
NBS 2005, 2006, 2007 , 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017 , 2018, 
2019, 2020, 2021
CAAM 2012, 2013, 2014, 2015, 2016, 2017 , 2018, 2019, 2020
 High
Vehicle survival 
rates ANL 2018 
Medium
Zero-emission vehicles’ survival 
rates are assumed to be the same 
as those for ICE vehicles. 
Freight  
tonne-kilometers 
in base year 
NBS 2021 High
Penetration 
of different 
technologies in 
vehicle stocks
NBS 2021
Expert consultations High
Vehicle 
kilometers 
travelled (VKTs)
MEE 2014b
RIOH and Sinoiov 2021
WRI authors’ adjustments
(Annual VKTs are fixed throughout a vehicle’s lifetime; degradation in 
VKTs as the vehicle ages is not considered. Further, the VKTs of NEVs are 
assumed to be the same as the VKTs of ICE vehicles.)
Low
VKTs are sample-dependent, 
and the variation is large across 
sources. b 
Fleet-average  
fuel efficiency  
in base year
This study’s estimation using the COPERT model (Ntziachristos et al. 2009), 
using China-specific driving cycles such as the China Light-Duty Vehicle 
Test Cycle (CLTC) and China Heavy-Duty Commercial Vehicle Test Cycle, 
and assuming four-month A/C usage, and 50% vehicle load. 
Medium
Real-world fuel consumption is 
affected by a basket of factors 
such as travel speeds, slopes, A/C 
usage, and loads that would be 
challenging to capture in a single 
value. Further, the fleet mix also 
affects fleet-average fuel efficiency. 
Load factors in 
base year
This study’s calculations are based on the statistics for freight tonne-
kilometers, vehicle stocks, and VKTs. 
Low
The limited quality of VKT data has 
ripple effects on load factors. 
Market shares of 
NEVs in annual sales 
by vehicle segment
The base year’s market shares are from the China Automotive Technology 
and Research Center in-house database. For projections, values are based 
on the authors’ literature and policy document reviews. 
High
Air pollutant,  
CH4, and N2O 
emission  
factors
Air pollutant emission factors come from the following sources:
•  MEE 2014b. 
•   This study’s estimation using the COPERT model (Ntziachristos et al. 
2009), for the emission factors of hybrid vehicles and the vehicles in 
compliance with the China 6 emission standard. 
•   NG vehicles’ TTW CH4 emission factors are based on Pan et al. (2020). 
(Emission factors are fixed throughout a vehicle’s lifetime; degradation of 
aftertreatment systems as the vehicle ages is not considered.) 
Medium
Like fuel consumption, air pollutant 
emissions factors are affected by 
multiple factors such as weather, 
fuel quality, loads, and degradation 
of aftertreatment devices, which 
would be challenging to capture in 
a single value.    
Power generation 
emission factor  
in base year
CEC 2020 High
Hydrogen generation 
emission factor in 
base year
This study’s estimation using the Greenhouse Gases, Regulated Emissions, 
and Energy Use in Technologies (GREET 2.0) Model (ANL 2014), based on 
the current hydrogen generation mix (CSI 2018).
High

14
WRI.org.cn
2.2.2 Abatement cost calculation
We estimated the marginal abatement cost—the 
abatement cost per unit of emissions reduced in a 
given year (Equation 4)— for different mitigation 
policies and technologies to evaluate their cost-
effectiveness. 
Marginal abatement cost
=     Abatement cost
      Emissions abated      (Equation 4)
As depicted in Equation 5, abatement costs 
are the net present values of the costs (such as 
expenses related to infrastructure investments) 
and savings (such as fuel cost savings) associated 
with the mitigation measures. These costs or 
savings could be assessed from the perspective of 
the end users or that of the society. When taking 
the societal perspective, taxes and subsidies are 
excluded as they are transfers between entities 
within a society, while taxes and subsidies are 
included when calculating from the end-user 
perspective (Schroten et al. 2012). This study took 
a societal perspective and excluded tax rebates 
and subsidies from the analysis. Therefore, the 
following costs are societal costs, including both 
public and private investments.
Abatement cost
=   Total cost-total savings
        (1+discount rate)year t       (Equation 5)
The estimation of abatement costs is distinguished 
by the mitigation measures:   
 ▪ The abatement cost of alternative vehicle tech-
nologies: Taking electric vehicles (EVs) as an 
example, the abatement cost is the difference 
between the total cost of EV ownership and the 
total cost of internal combustion engine (ICE) 
vehicle ownership (Equation 6). The total cost 
of EV ownership in a given year is the EV’s life-
time total cost of ownership (TCO) iv multiplied 
by the annual sale volume of EVs. The lifetime 
TCO of EVs consists of upfront vehicle pur-
chase costs, energy costs, and levelized costs 
of charging/refueling throughout the vehicle’s 
useful life. The levelized costs of charging/
refueling denote the total capital expenses 
(CAPEX) and operating expenses (OPEX) of 
charging/refueling infrastructure v amortized 
to the EV’s total energy demand. As explained 
earlier, we excluded taxes and subsidies from 
the study.
Abatement cost
=  (EVcapital,t+EVoperation,t)×Salest-ICEcostt× Salest
                                    (1+r)year t 
 (Equation 6)
where,
EVcapital,t  is the EV’s purchase cost without taxes 
and subsidies in year t 
EVoperationt  includes lifetime electricity or hydrogen 
costs of the EV purchased in year t 
ICEcostt  is the lifetime TCO of a new ICE vehicle 
in year t 
Salest  is the sales volume of EVs in year t 
r  is the annual social discount rate (3 percent in 
this study)

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
15
 ▪ The abatement cost of structural changes includes CAPEX and OPEX investments in transit, ac-
tive mobility, and railway infrastructure as well as the cost savings from owning a smaller vehicle 
fleet under the effect of structural changes. Specifically, in a given year, structural change measures 
quantified by infrastructure investments lead to fewer vehicle sales (Sales t) than the vehicle sales 
in the baseline scenario (Sales t,no_shift ) without the effect of structural change measures (that is, no 
infrastructure investment). The difference in the total cost of vehicle ownership resulting from dif-
ferent sales volumes is attributed to the deployment of structural change measures. In this study, 
we did the calculation for passenger transport (Equation 7-1) and freight transport (Equation 7-2).   
where,
Costinfrastructure,t is the investment in transit and active mobility infrastructure in year t  
Salest is the sales volume of private cars by technology in year t with the effects of structural changes  
Salest,no_shift  is the sales volume of private cars by technology in year t without the influence of structural 
change measures  
r is the annual social discount rate (3 percent in this study) 
where,
Costinfrastructure,t is the investment in railway infrastructure in year t  
Salest is the sales volume of trucks by technology in year t with the effects of structural changes  
Salest,no_shift  is the sales volume of trucks by technology in year t without the influence of structural changes  
r is the annual social discount rate (3 percent in this study) 
Abatement costpassenger
= Costtransit_infrastructure,t+(Costcapital,t+Costoperation,t)×Salest-(Costcapital,t+Costoperation,t)×Salest,no_shift)
      (1+r) year t  (Equation 7-1)
Abatement costfreight
= Costrailway_infrastructure,t+(Costcapital,t+Costoperation,t)×Salest-(Costcapital,t+Costoperation,t)×Salest,no_shift
      (1+r) year t  (Equation 7-2)

16
WRI.org.cn
The cost inputs are based on official statistical data, 
a literature review, and expert consultations. See 
Table 4 for a qualitative assessment of the data 
sources used to evaluate abatement costs. 
Table 4  |   Qualitative Assessment of the Data Sources Used to Estimate Abatement Costs 
VARIABLES DATA AND SOURCES DATA QUALITY
Vehicle purchase 
cost 
Vehicle prices are from car dealer websites Diandong.com, Yiche.net, and 360che.
com. Methods to project future vehicle costs are elaborated in Appendix B.   
 High a
Energy prices
Diesel: 6.5 CNY/Lb 
Gasoline: 7 .1 CNY/Lc
NG: 4.5 CNY/m3 (2020) to 6 CNY/m3 (2060)d
Electricity: 0.6 CNY/kWhe 
(Energy prices are fixed despite market fluctuations and regional disparities.)
 Medium
Levelized cost of 
charging stations’ 
capital and O&M 
investments
0.5 CNY/kWh f 
(Levelized costs are fixed despite varying levels of investment)  Medium
Levelized cost of 
hydrogeng
2025: 40 CNY/kg (90–95% gray hydrogen in the production mix) h
2035: 30 CNY/kg (65–70% gray hydrogen in the production mix) 
2050: 20 CNY/kg (15–35% gray hydrogen in the production mix) i
 Medium
CAPEX and 
OPEX on freight 
railways 
Assume that China’s future freight infrastructure investments are linearly 
related to freight tkm growth and that a quarter of the freight investment 
goes to railways. j 
Low
The magnitude of investment 
varies by the actual demand for 
infrastructure.
CAPEX and 
OPEX on public 
transit and active 
mobility 
Based on historical trends, k we assume that 700 km of subway is 
constructed each year until 2035. l The CAPEX of subways is fixed at 0.7 
billion CNY/km. Due to their trivial amounts, we omitted investments in 
active mobility in this study. 
Low
The magnitude of investment 
varies by the type of 
infrastructure under discussion 
and the actual demand for 
infrastructure.
Notes:   a.  represents a high level of confidence,  represents moderate confidence, and  represents a low level of confidence. 
b. Diesel prices are based on rough historical price trends from the past decade using CEIC Data (www.ceicdata.com).
c. Gasoline prices are based on rough historical price trends from the past decade using CEIC Data (www.ceicdata.com).
d. The current natural gas price is based on information from www.in-en.com. Future natural gas prices are projected based on WRI authors’ assumptions.
e. Xue et al. 2020.
f. China EV 100 and NRDC 2019.
g.  For fuel cell vehicles, this study assumes hydrogen production, transportation, distribution, capital expenses, and operating expenses of hydrogen refueling stations are 
altogether recouped by at-pump hydrogen costs, known as the levelized cost of refueling.
h. The hydrogen production mix is based on the authors’ assumptions for different scenarios based on CHA (2019).
i. CHA 2019.
j. OECD 2018.
k. CAM 2017 , 2018, 2019, 2020.
l. The assumed annual increase of 700 km of subway is consistent with the national target of increasing the subway length by 3,400 km over the 14th five-year period (2021–25).  
Abbreviations:  CNY = Chinese yuan; L = liter; m3 = cubic meter; CAPEX = capital expenses; OPEX = operating expenses; kWh = kilowatt-hour; kg = kilogram;  
O&M = operations and maintenance.

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
17

18
WRI.org.cn

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
19
SCENARIO 
DESIGN
Future emissions from the road transport sector are affected 
by factors such as service demand growth, structural changes, 
technology deployment, and upstream power and hydrogen 
sector decarbonization. The scenarios modelled in this study are 
based on existing policies and a literature review.
CHAPTER 3

20
WRI.org.cn
3.1 Influencing Factors 
In general, future emissions from the road transport 
sector are affected by factors such as service 
demand growth, structural changes, technology 
deployment, and upstream power (and hydrogen) 
sector decarbonization (see Table 5). However, 
not all decarbonization measures are applicable to 
China (such as low-carbon fuels) or can be modelled 
by this study (such as carbon pricing). This section 
explains how we considered different measures. 
Further, because uncertainties remain large 
with autonomous driving, we did not cover that 
technology in this study. 
3.2 Decarbonization Measures
The scenarios modelled in this study are based on 
existing policies and a literature review.
3.2.1 Service demand 
In contrast to the modest expected increases in 
travel demand in OECD countries over the next 
30 years (Teske et al. 2021), China is expected to 
have strong growth in service demand during this 
period. In fact, the country experienced drastic 
growth in passenger and freight demand from 
2005 to 2020 (Figure 5):
Table 5  |   Comprehensive Decarbonization Measures to Mitigate Road Transport Emissions 
SERVICE DEMAND STRUCTURAL 
CHANGES
TECHNOLOGY  
DEPLOYMENT
POWER AND HYDROGEN 
DECARBONIZATION
Decarbonization
measures
•   Compact development 
and land-use planning
•   Fuel pricing and/or 
carbon pricing
•  Mode shift 
•   Vehicle occupancy 
improvements
•   Vehicle electrification 
•   Fuel efficiency 
improvements 
•  Low-carbon fuels
•   Power sector 
decarbonization
•   Hydrogen production 
decarbonization
Variables
•  Vehicle stocks  
•  Domestic tkm 
•   Vehicle kilometers 
travelled
•  Mode shares
•   Load factors (tkm/vkm)
•   Market shares of vehicle 
technologies
•   Percent of fuel blends and 
carbon intensity in fuels
•  Fuel efficiency 
•  Power mix 
•   Hydrogen production mix
Abbreviations: tkm = tonne-kilometer; vkm = vehicle-kilometer. 
Source: WRI authors.
Note:  The decreases in the freight tonne-kilometers (tkm) during 2018 and 2020 were due to an adjustment in China’s statistical system to exclude light-duty trucks’ tkm; and the impacts 
of COVID-19 on waterway tkm. 
Source: NBS 2021. 
Figure  5  |   Growth in Passenger Car Ownership, Freight Tonne-Kilometers, and Gross Domestic Product per 
Capita (2005–20)
Freight tkm
GDP per capita
Number of 
passenger cars
Gross domestic 
product per capita 
(constant 2017 
international $ per 
person)/ 
billion freight 
tonne-kilometers/
10,000 passenger 
cars
2005 20202010 2015
0
5,000
20,000
25,000
15,000
10,000

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
21
 ▪ The number of passenger cars in China 
increased 12 times from 19 to 239 million 
(compound annual growth rate, or CAGR, of 18 
percent) (NBS 2005, 2006, 2007, 2008, 2009, 
2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 
2018, 2019, 2020).
 ▪ Significant increases also occurred for China’s 
domestic freight demand. The tonne-kilometers 
(tkm) (including domestic road, railway, 
waterway, aviation, and pipeline, but excluding 
international maritime shipping and aviation) 
were 15.2 trillion tkm in 2018, increasing more 
than three times (CAGR = 10.5 percent). 
Future growth in passenger cars 
Despite tremendous growth, the passenger car 
ownership rate in China—170 cars per 1,000 persons 
in 2020—is relatively low compared with Japan’s 
493, the EU’s 540, and the United States’ 592 (NBS 
2020; MLITT 2021; Eurostat 2021a; BTS 2021a). 
To project China’s passenger car ownership up to 
2060, we employed the Gompertz model, where the 
growth in car stocks follows an S-shaped curve—the 
growth in car ownership is rapid as gross domestic 
product (GDP) per capita increases but slows 
when approaching the saturation level. Our GDP 
and population forecasts are based on the Shared 
Socioeconomic Pathways (Riahi et al. 2012; see 
Appendix A). We cross-validated the result with 
existing studies. 
The forecasts show that China’s motorization 
will continue until a maximum saturation level is 
reached, though the saturation level for China’s 
passenger cars will be lower than those in developed 
countries (Figures 6 and 7):
 ▪ Existing studies show that if no additional 
policy interventions are pursued, China’s 
passenger car saturation will be likely around 
350–450 passenger cars per 1,000 persons 
by 2050 (Gilbert 2017; ANL 2018; Huo et al. 
2012a), amounting to 450–600 million car 
stocks. In the Stated Policy scenario of this 
study, the saturation level of passenger cars is 
set to 425 cars per 1,000 persons, with total 
passenger car ownership peaking in 2045 at 506 
million vehicles. 
 ▪ Existing studies also reveal that if mode shift 
measures and compact urban planning are 
undertaken, the saturation level can be lowered 
to 260–350 passenger cars per 1,000 persons 
by 2050, amounting to 330–450 million car 
stocks (Gilbert 2017; ANL 2018; Huo et al. 
2012a). In the Structural Change scenario of 
this study, the saturation level is lowered to 
300 cars per 1,000 persons, with car ownership 
peaking in 2040 at 381 million vehicles.  
Note:  European Union (EU) and United States vehicle and passenger car ownership data are from 2019; data for other countries are from 2020. 
Sources: NBS 2021; LTA 2021; BTS 2021a; Eurostat 2021a; MLITT 2021. Population data come from the World Bank database: https://data.worldbank.org. 
Figure  6  |   Vehicle and Passenger Car Ownership per 1,000 Persons in China and Other Regions
Stated Policy scenario_this study Structural Change scenario_this study
194 170
Number of vehicles/cars per 1,000 persons
China EU United StatesSingapore Japan
0
300
200
100
800
700
900
600
500
400
Passenger car ownership per 1,000 personsVehicle ownership per 1,000 persons
146
654 616
842
112
493 540
592

22
WRI.org.cn
Future growth in freight demand (in tkm)  
Driven by economic growth, China’s freight demand 
should continue growing; however, the growth rate is 
confounded by many uncertainties, including supply 
chain relocation, an economic structural shift to the 
less transport-intensive service sector (H. Wang et al. 
2021),vi and long-term oil price changes. Therefore, 
views are divided on whether China’s freight demand 
growth will be maintained (Figure 8). 
 ▪ Some modelling studies (Fu et al. 2019; ICCSD 
2020) have concluded that with the economic 
shift to less transport-intensive sectors and the 
expected decline in bulk commodity shipments 
(such as of coal and mineral ore), China’s freight 
demand growth will slow starting in 2030 (CAGR 
= 0.6 percent) and plateau during 2040–45 at 
around 18.6–19.8 trillion tkm. Peak demand 
would be only 1.7–1.8 times the demand in 2020.
 ▪ Other research indicates that freight demand is 
affected by both transported tonnes and travel 
distances. Though transported tonnes—like 
bulk commodities—could drop, the distances 
travelled will likely grow given more frequent 
shipments and increases in shipment lengths, 
as in the case of Germany (Frey et al. 2014). 
Sources: NBS 2019; Gilbert 2017; ANL 2018; Huo et al. 2012b; and author assumptions. 
Figure  7  |   Predictions for Car Saturation Levels by Existing Research and This Study
Figure  8  |   Existing Projections for China’s Domestic Freight Tonne-Kilometers
Note: Domestic freight demand includes domestic roads, railways, waterways, aviation, and pipelines, but excludes international shipping (maritime), aviation, and railways. 
Abbreviations: tkm = tonne-kilometer; int’l = international.
Sources: J.L. Liu et al. 2018; ICCSD 2020; Pan et al. 2018; Wang et al. 2017; Yin et al. 2015; Hao et al. 2015; Fu et al. 2019; WRI authors. 
China historic data (2002-19)
Huo et al. (2012)_Scenario2
Gilbert (2017)_Forecaster 2
ANL (2018)_Highest
Gilbert (2017)_Forecaster 1
ANL (2018)_Lowest
Huo et al. (2012)_Scenario1
Stated Policy scenario_this study
Hao et al. (2015)_DM Pan et al. (2018)_1.5Cneg Pan et al. (2018)_2Czero
Pan et al. (2018)_REF Wang et al. (2017)_EEI Wang et al. (2017)_CPR
Wang et al. (2017)_ATI Fu et al. (2019)_Lowcarbon Fu et al. (2019)_BAU
Hao et al. (2015)_BAU
ICCSD (2020)
Wang et al. (2017)_REF
Liu et al. (2018)
Wang et al. (2017)_PEV
Yin et al. (2015)_REF
Domestic freight demand 
(trillion tkm)
0 10 20 30 40 50 60 70 80 90
Domestic + int'l freight demand 
(trillion tkm)
Cars per 1,000 persons
0
300
200
100
700
600
500
400
2000 2010 2050 20602020 20402030
Structual Change scenario_this study

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
23
Therefore, to be comparable with the growth 
trends in developed countries, vii China’s 
domestic freight demand in 2050 would be two 
to three times (25.2–32.5 trillion tkm) the level 
in 2020 (Yin et al. 2015; Wang et al. 2017).
This study takes an optimistic view on China’s 
future freight demand given the promising demand 
forecasts in other regions. For example, according to 
Freight Analysis Framework, U.S. domestic freight 
demand will grow to 7.6 trillion ton-miles in 2045, 
only 1.5 times the tkm in 2015 (BTS and FHWA 
2016). Germany’s freight demand is projected to 
reach 896 billion tkm in 2050, 1.4 times the tkm in 
2016 (Agora Energiewende 2020a). Using GDP per 
capita and fuel price elasticities—measurements of 
how freight demand responds to the growth of GDP 
per capita and fuel price increases (see Appendix A; 
Edelenbosch et al. 2017)—we project that China’s 
domestic freight demand will reach 25.9 trillion tkm 
in 2060, 2.5 times the 2020 level. 
3.2.2 Structural changes
Because of high occupancy rates and low emission 
intensity per tkm or pkm, passenger and freight mode 
shifts are essential to reducing carbon footprints and 
alleviating traffic congestion (see Figure 9). 
However, shifts to high-emitting modes are 
occurring in China (Figure 10): 
 ▪ Passenger transport: Due to rapid urban 
expansion, large cities have witnessed increases 
Figure  9  |   Energy/Emission Intensities of Different Modes
Figure  10  |   Changes in Passenger Transport Mode Share in China
Abbreviations: CO2 = carbon dioxide; kg = kilogram; g = gram; tkm = tonne-kilometer; pkm = passenger kilometers travelled; NOx = nitrogen oxides; g = gram; PM = particulate matter. 
Sources:  Energy consumption data for freight modes are from MOT (2016). Air pollutants from freight modes are calculated by the authors using MEE (2020b). Passenger modes are 
calculated by the authors using Shenzhen’s vehicle occupancy rates. The CO2 emission factor for metro is based on Jiang et al. (2019).
Notes: Walking is not included in Beijing’s mode share. 
Abbreviations: pkm = passenger kilometers travelled; NMT = non-motorized transit.
Source: Fu et al. 2019; NBS 2021.
a. Mode share of intracity trips: Beijing b. Mode share of intercity pkm: China
a. Freight transport b. Urban passenger transport
Inland waterway
NMT Road
BusRailway
Private car Waterway Aviation
MetroRoadway
Transit Railway
Private car Walk & bike
Energy consumption 
(g standard coal/tkm)
CO2 (kg CO2/pkm)
0 010 0.15 0.0515 0.1520 0.250.2
NOx (g/tkm) NOx (g/pkm)
PM (100 g/tkm) PM (g/pkm)
1999 20012004 20042009 2007 2010 2013 20162017 2019
0 0
60% 60%
40% 40%
20% 20%
80% 80%
100% 100%

24
WRI.org.cn
in motorized trips (private car and transit), 
leading to reduced non-motorized trips (such 
as biking and e-scootering). For example, the 
mode share by bike, e-scooter, and motorcycle 
in Beijing dropped from 90 percent in 1999 to 
18 percent in 2017 (Fu et al. 2019), while the 
mode share of private cars (including ride-
hailing) increased from 1 percent in 1999 to 36 
percent in 2017. 
The situation is mixed for intercity travel. From 
2001 to 2020, the share of intercity pkm by car 
decreased from 55 to 24 percent, while the share 
of railways grew slightly from 36 to 43 percent. 
However, of note is that an increasing number of 
intercity travel is being undertaken by air, with 
aviation’s mode share rising four times from 8 to 
33 percent.     
 ▪ Freight transport: Due to underpriced 
roadway freight, viii limited track access, and 
undesirable railway service quality from 1990 
to 2020 (Agenbroad et al. 2016), the share 
of railways in domestic tonne-kilometers in 
China shrank drastically over that period 
from 59 to 27 percent (although the rail 
tkm increased almost threefold), while the 
share of road freight increased from 19 to 
54 percent due to strong economic growth 
(Figure 11). During the same period, domestic 
waterways experienced a slight drop from 19 
to 14 percent. 
Compared with North America, Europe, and 
India, China is more reliant on roadways and 
waterways for freight shipments, with roadway 
and waterway tkm increasing by seventeen-fold 
and thirteen-fold, respectively, from 1990 to 
2019. Nonetheless, compared with the United 
States’ recent increase in domestic railway 
activities—resulting from the transition from 
railway-based coal shipments to intermodal 
freight, China’s rail activities have not grown 
since 2010 (Kaak et al. 2018).        
Figure  11  |   Freight Mode Share of Domestic Tonne-Kilometers in China and Comparisons with North America, 
Europe, and India
Notes: Domestic freight mode share includes roads, railways, waterways, aviation, and pipelines, but excludes maritime. Abbreviation: tkm = tonne-kilometer. 
Sources: NBS 2021; Kaak et al. 2018. 
Road Rail Domestic water
Railway Road Waterway Aviation Pipeline
1990
2000 2000 2000
0 0 0
1,000 1,000 1,000
2,000 2,000 2,000
6,000
China
China
China
North America
North America
North America
Europe
Europe Europe
India India
6,000 6,000
4,000 4,000 4,000
1995
2005 2005 2005
2000
2015 2015 20152010 2010 2010
20102005 2015 2020
0
60%
40%
20%
80%
100%
Freight activity (billion tkm)
Freight activity (billion tkm)
Freight activity (billion tkm)

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
25
Passenger transport mode shift
Unlike countries like the United States where 
interventions like mode shift and increasing vehicle 
occupancy are less effective due to the lock-in 
effect resulting from an already-high dependency 
on private cars (Teske et al. 2021), high-density 
Chinese cities are likely to reverse the ongoing 
passenger mode shift to private cars. This is 
particularly the case considering many small cities 
in China still have a private car mode share of 
around 10–15 percent (ZTB 2017).
This study assumes that in the Stated Policy 
scenario—which is based on NDRC (2021)—that by 
2030, major Chinese cities will have over 70 percent 
green transport mode share in which public transit 
accounts for 45 percent of the total mode share 
(ICCSD 2020). In the Structural Change scenario, 
to keep car ownership (and usage) at a reasonably 
low level, the green transport mode share should be 
elevated to about 75–85 percent, and public transit 
should represent over 50 percent of the total mode 
share (ICCSD 2020). These targets are achievable: By 
prioritizing cycling and walking and strengthening 
modal integration, Shenzhen’s and Beijing city 
center’s green transport mode shares reached 77 
percent and 73 percent, respectively, in 2020 (China 
Transport News 2021; Xinhua News 2021). 
To achieve the elevated targets in the Structural 
Change scenario, the country should embrace 
a paradigm shift from provider-oriented green 
transport services to user-oriented services (Figure 
12; Enoch 2018). Although shared rides (such as 
ride-hailing and carsharing) are integral to this 
paradigm shift, additional measures should be 
taken to avoid their competition with public transit 
and increased “deadhead” miles (Kong et al. 2020; 
Schaller 2021; Zhang et al. 2020). These measures, 
including Mobility-as-a-Service (MaaS), should 
enable ride-sharing to supplement transit services 
in places of limited transit accessibility and allow for 
better journey matches to reduce deadhead miles 
(ERTICO 2019). 
Freight transport mode shift 
Although the movement up the value chain and new 
logistics requirements (increasing shipments of 
smaller parcels and just-in-time delivery) inherently 
favors roadways, China has an untapped potential 
to increase rail freight’s mode share. Research 
shows countries with large land coverage and good 
railway networks such as Russia, Australia, and 
Figure  12  |   Paradigm Shift in Transit Services: From Provider-Oriented Services to User-Oriented Services
Source: Enoch 2018.
Scheduled 
operations
Demand 
is not 
managed
Supply-side management
Demand-side management
Supply reacts to 
demand
Demand 
is actively 
managed Intelligent
Mobility
Transport 
Demand
Management
Traditional 
Transport
Services
Demand 
Responsive
Transport Services

26
WRI.org.cn
Canada tend to have higher rail shares than the 
world’s average of road and rail mode split—61:39 
(Kaak et al. 2018), with China as an exception. This 
is mainly due to uncompetitive railway pricing,ix 
underdeveloped intermodal services, and limited 
rail service quality in China (Agenbroad et al. 
2016). For example, for shipment distances over 
400 kilometers, bulk unit trains were about 2–20 
CNY per tonne more expensive than roadways 
in 2018 (H.H. Liu 2018). Further, intermodal 
(containerized) rail services are underdeveloped in 
China: Only 5.4 percent of the rail shipments (by 
weight) were intermodal containers in 2016 (Fu et 
al. 2019), compared with 19 percent in European 
countries (Eurostat 2021b). 
Because China lacks a national freight mode shift 
target and a statistical system to evaluate future 
mode shift potential, this study relies on existing 
research to project freight mode share. However, 
we recommend making substantial improvements 
to the country’s freight statistical system to 
incorporate surveys on commodity flows (by mode, 
distance, and origin/destination pairs), which would 
allow for mode shift target setting and policymaking 
based on commodity-specific evaluations. 
For simplicity, this study assumes under the 
Stated Policy scenario that a larger shift to road 
transport could be prevented (Table 6), whereby 
road transport would represent 50 percent of the 
domestic tkm in 2060 (about 2020’s level). This 
is consistent with the median value of the existing 
predictions (J.L. Liu et al. 2021; ICCSD 2020; Pan 
et al. 2018; Wang et al. 2017; Zhang et al. 2016; 
Yin et al. 2015; Hao et al. 2015; Huo et al. 2012a) 
(Figure 13). 
Under the Structural Change scenario, this study 
assumes that an explicit mode shift target—40 
percent road transport in domestic tkm in 2060—will 
be established (Figure 13). To achieve this target, 
Figure  13  |   Projections of China’s Future Freight (Railway and Roadway) Mode Shares out of Total Domestic 
Tonne-Kilometers in Existing Studies
Note: China’s freight mode share includes roads, railways, waterways, aviation, and pipelines, but excludes maritime.  
Sources: Historic mode share data for road freight and rail freight are from NBS (2021). Further projections are based on ICCSD (2020); Xue et al. (2019); Fu et al. (2019); Yin et al. (2015).
Road freight mode share Rail freight mode share Fu et al. (2019)_BAU(road) Fu et al. (2019)_BAU(rail)
Xue et al. (2019)_1.5 degree(road)
ICCSD 2020_SP(rail) YIn et al 2015(road) ICCSD 2020_1.5 degree(road)
Fu et al. (2019)_Lowcarbon(road) Fu et al. (2019)_Lowcarbon(rail) ICCSD (2020)_SP(road)
ICCSD 2020_1.5 degree(rail) ICCSD 2020_2 degree(road)
ICCSD 2020_2 degree(rail)
20152005 2010 20502020 20352025 20402030 2045
0
10%
30%
70%
60%
50%
20%
40%

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
27
RAILWAYS AND WATERWAYS ROADWAYS
Reduce shipping time.b Avoid vehicle overloading.d 
Invest in railways, waterways, and intermodal connectivity.a Manage oversupply, underbidding, and thin margins in the 
truck industry. c 
•   By 2035, increase the mode 
share of intermodal freight, 
and reduce intermodal 
handling/transit time. 
•   Promote standardization 
of intermodal handling 
equipment and data 
exchanges.
•   By 2025, the volume of containerized 
intermodal railway shipments will 
increase by 15%; 85% of major container 
ports must be equipped with on-dock 
rail services; and 85% of new logistic 
parks and large industrial enterprises 
must have rail track access.   
•   Promote internet freight 
platforms for better load 
matching and more high-
value services (such as 
supply chain and inventory 
management). 
•   Prohibit internet freight 
platforms from encouraging 
shippers to lower shipping 
prices and drivers to 
underbid. 
•   Tighten the scale of 
enforcement on truck 
overloading. 
•   Avoid illegal adaptations 
to vehicles or mislabeled 
gross vehicle weights. 
•   Accelerate 
the expansion 
of high-
grade inland 
waterways. 
systematic measures will need to be undertaken: 
 ▪ For the rail sector: In the near term, the country 
could shift more bulk commodities to railways 
and waterways, considering roadways still 
dominate shipments of steel, cement, and gravel 
(Fu et al. 2019). Over the long term, as the country 
moves up the value chain, and the volumes of 
bulk commodity shipments drop, transitioning 
to intermodal freight for high-value products 
will be necessary. This transition would mean 
new geographical patterns of rail activities, 
new investment needs, and higher service 
requirements (SFC n.d.; Kaak et al. 2018) for 
railway companies. The railroad industry, which 
has been monopolized by state-owned enterprises, 
will need to enhance service connectivity among 
rail segments, rationalize pricing, improve 
scheduling and on-time performance, automate 
freight (un)loading, avoid loss/breakage, and 
reinforce first-/last-mile truck delivery. 
 ▪ For the road sector: Interventions are needed 
to tackle China-specific challenges including 
truck capacity oversupply, underpriced road 
shipments, and thin profit margins that are 
crucial to improving the cost-competitiveness 
of rail services (for concrete interventions, see 
Vehicle occupancy rate improvements). 
Vehicle occupancy rate improvements 
Improving vehicle occupancy rates is critical to 
reducing vehicular emissions because the same 
demand can be fulfilled with fewer vehicles. 
For passenger transport, although ride sharing is 
an important measure to increase the occupancy 
rate for private cars, priority should be given to 
increasing occupancy rates for public transit. 
This is particularly the case when many Chinese 
cities have witnessed declining bus ridership and 
low bus occupancy: For example, the average 
occupancy rate of buses was 22 percent in Shenzhen 
in recent years (in terms of the carrying capacity 
for a mainstreamed 10-meter bus), smaller than 
Hong Kong’s roughly 30–85 percent (in terms 
of the carrying capacity for a mainstreamed 
three-axle double-decker) (Lai n.d.). To increase 
ridership, rationalization of traditional bus services, 
introduction of demand-responsive services, 
and comprehensive travel demand management 
measures are necessary.     
For road freight transport, operational 
efficiency needs to be significantly improved. 
With tightened controls over truck overloading 
(MOT 2017a), x the average load of road freight 
(quantified by dividing annual tonne-kilometers 
Note: a. NDRC 2021; State Council 2021a.  b. State Council 2021b.  c. MOT 2019.  d. MOT 2017a, 2017b.
Source: WRI authors, summarized based on policy documents. 
Table 6  |   Policies and Announced Targets in the Stated Policy Scenario

28
WRI.org.cn
by total vehicle-kilometers) had declined to 
9.8 tonnes in 2020, lower than the EU’s 11.5 
tonnes (Eurostat 2021c). Further, 40 percent of 
China’s vehicle-kilometers were empty running, 
compared with the EU’s and United States’ 20 
percent (Yang et al. 2019; ATRI 2020). 
Due to operational inefficiency, the size of the 
heavy-duty truck fleet is excessively large in 
China: Though China’s road freight tkm were 
two to three times higher than those in the EU 
27 and the United States in 2020, the number 
of heavy-duty trucks in China was three to five 
times higher than those in the EU 27 and the 
United States in the same year (Table 7). If the 
issues with truck underutilization and oversupply 
persist, they will intensify the unhealthy 
competition (such as underbidding of roadway 
prices) within the trucking industry and deter 
freight mode shift to low-carbon modes.  
Underutilized trucks, inefficient operations, and 
a dependency on road freight will further boost 
future truck fleet sizes. By this study’s estimates, 
in the Stated Policy scenario where trucks 
remain inefficiently operated (with an average 
load of 9.5 tonnes) and roadways consist of 50 
percent freight tkm, China’s future fleet size of 
medium- and heavy-duty trucks (GVWs above 
4.5 tonnes) will double from 9.5 million in 2020 
to 20 million in 2060. However, in the Structural 
Change scenario, with operational efficiency 
improvements (average load = 11.5 tonnes) and 
freight mode shift, the future fleet size of HDTs 
will be maintained at 12 million in 2060, only 
a modest 26 percent increase from the 2020 
level and half the fleet size in the Stated Policy 
scenario (Table 14). 
Although there is an upper limit to logistic 
efficiency improvements—given a geographical 
imbalance in freight flows; growing lightweight 
and low-density freight (McKinnon 2010); and 
the increasing adoption of NEV trucks (Qiu et 
al. 2020), which will affect HDTs’ operational 
efficiency—it is possible to achieve the level of 
operational efficiency in the Structural Change 
scenario. For example, Mulholland et al. (2018) 
show that average loads of HDTs increase with 
a country’s average income due to the shift from 
straight trucks to tractor trailers and combination 
trucks for long-haul transportation. Additional 
Table 7  |   Operational Efficiency of the Truck Industry in China, the European Union, and the United States
Note:  Light-duty trucks’ tonne-kilometers (tkm) are not included in China’s statistics for road freight tkm. The number of trucks includes both light-duty trucks (for China, light-duty trucks 
are those with gross vehicle weights [GVWs] below 4.5 tonnes; for the European Union [EU], light-duty trucks are those with GVWs below 3.5 tonnes) and heavy-duty trucks. In 
China and the EU, heavy-duty trucks refer to trucks with GVWs over 12 tonnes; in the United States, heavy-duty trucks include only combination trucks (class 8 tractor trailers).      
Abbreviations: EU 27 = the 27 members of the European Union.
Sources:  a. NBS 2021. b. Eurostat 2021d. c. BTS 2021a.  d. RIOH and Sinoiov 2021. e. CATARC 2018. f. Gnann et al. 2017 . g. FHWA 2021. h. Authors’ calculation based on the method outlined in Table 3.  
i. Eurostat 2021c. j. Yang et al. 2019. k. Yang et al. 2019. l. ATRI 2020. m. NBS 2021. n. Eurostat 2021e. o. BTS 2021a. p. NBS 2021. q. Eurostat 2021e. r. BTS 2021a.
CHINA
(2020)
EU 27
(2020)
UNITED STATES
(2018)
Tonne-kilometers of road freight 6,017 billion a 1,803 billion b 2,969 billion c
Annual VKTs of heavy-duty trucks
(kilometers)
46,808d or
65,171,e depending on source 74,000–114,000f 96,446 (combination trucks) g
Average load  9.5 tonnes h 11.5 tonnes i --
Empty running 40%j 20% k 20%l (for hire)
Number of trucks 30.4 million m 31.5 million n 13.1 million o
Number of heavy-duty trucks 8.4 million p 1.7 million q 2.9 million r (combination trucks)

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
29
measures China could use to improve road freight 
operational efficiency include encouraging the 
use of non-truck operating carriers, facilitating 
drop-and-hook operations, and promoting 
standardization of trucks and pallets (Agenbroad 
et al. 2016).  
3.2.3 Technology deployment
Low-carbon vehicle technologies (or fuels)
The low-carbon transition in China’s vehicle fleet is 
rapidly underway (Table 8 and Figure 15). 
New energy vehicles (NEVs)—including 
battery electric vehicles, plug-in electric 
vehicles (PHEVs), and fuel cell electric 
vehicles (FCEVs)—are becoming mainstream 
technologies in buses and being increasingly 
adopted for use in private cars. 
 ▪ NEV buses had a 55 percent fleet penetration 
by the end of 2020, rising rapidly from 
2012’s 3 percent. NEV taxis are also gaining 
market momentum, representing 9 percent 
of fleet penetration. 
 ▪ Although NEV private cars had a 1 percent fleet 
penetration by the end of 2020, the market share 
Sources:  Historic data are based on NBS (2021). Projections are WRI authors’ calculations.
Figure  14  |   China’s Heavy-Duty Truck Fleet Size Projections (2020–60) under Different Scenarios 
of NEV sales soared: NEVs accounted for 15.7 
percent of passenger car retail sales in 2021, more 
than double 2020’s 6 percent (CAAM 2022). 
 ▪ By contrast, the fleet penetrations and market 
shares of NEVs remain low for light-duty and 
heavy-duty trucks: NEVs account for 0–1 
percent of heavy-duty truck and light-duty truck 
fleet penetration, and 1 percent market share in 
their respective annual sales.   
NG vehicles are common for commercial fleets: 
They have 55 percent of the taxi fleet penetration 
and 18 percent of the bus fleet penetration. They 
are increasingly adopted by the trucking industry 
(5 percent of the heavy-duty fleet penetration in 
2020), and the market share of liquefied natural 
gas (LNG) trucks in heavy-duty truck sales tripled 
from 2.4 percent in 2015 to 8.5 percent in 2020 
(Autoinfo 2021).   
Not all alternative vehicles/fuels are popular, 
especially biofuels. Unlike in the United States 
where most of the gasoline sold is blended with 
10–15 percent ethanol (by volume), biofuels 
are the least-adopted type of fuel in China. At 
present, biofuels—especially ethanol—are applied 
mostly to the taxi fleet, with 11 percent of the fleet 
powered by ethanol. 
Structual Change scenario Historic dataStated Policy scenario10,000 vehicles
20152005 2010 20602050 20552020 20352025 20402030 2045
0
500
2,500
2,000
1,500
1,000

30
WRI.org.cn
Table 8  |   Fleet Penetration of Alternative Vehicles/Fuels in 2020
Figure 15  |   Market Share of New Energy Vehicles in Annual Sales of Respective Vehicle Segments  
(2012–November 2021)
Note:  Because of the data constraint regarding the technology breakdown for motorcycles, the study assumes 100 percent of the registered motorcycles are powered by fossil fuels, and 
unregistered motorcycles (and e-scooters) are electric.   
Abbreviations: NEV = new energy vehicle; LPG = liquefied petroleum gas.
Sources:  Data on private cars, coaches, light-duty trucks, and heavy-duty trucks are from a China Automotive Technology and Research Center (CATARC) database (accessed November 
2021). Data on taxis and buses are from MOT (2020). The breakdown of motorcycle technology is based on WRI authors’ assumptions. 
Abbreviations: NEV = new energy vehicle. 
Source: Data are from a China Automotive Technology and Research Center (CATARC) database (accessed November 2021).
SHARE OF 
THE TOTAL 
STOCK
GASOLINE DIESEL HYBRID NATURAL 
GAS NEV
OTHERS 
(ethanol, 
LPG)
SUBTOTAL
Private cars 70% 98% 0% 1% 0% 1% 0% 100%
Taxis 0% 22% 0% 1% 55% 9% 13% 100%
Buses 0% 0% 14% 12% 18% 55% 1% 100%
Coaches 1% 3% 87% 0% 6% 4% 0% 100%
Light-duty trucks 6% 42% 56% 0% 1% 1% 0% 100%
Heavy-duty 
trucks 3% 0% 95% 0% 5% 0% 0% 100%
Motorcycles 20% 100% 0% 0% 0% 0% 0% 100%
NEV buses NEV medium- and heavy-duty trucksNEV passenger cars NEV light-duty trucks
20142012 2013 2021
Jan-Nov
2015 20182016 20192017 2020
0
20%
100%
80%
60%
40%

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
31
First, the future technology pathways are country-
specific and vehicle segment-specific. Particularly, 
controversies lie in the plausibility of using 
“transitional technologies.” For example, some 
studies argue that despite their inferior environmental 
performance, the transitional technologies are 
necessary near-term options for China: 
 ▪ LNG trucks: 50 percent fleet penetration in 
2050 (LBNL 2021) 
 ▪ Biofuels: 32 percent of transport energy 
consumption in 2050 (Pan et al. 2018)
 ▪ Hybrid trucks: 40 percent of annual sales by 
2060 (iCET 2021) 
Considering the infrastructure investment needs 
and useful lives of vehicles, this study gave only 
limited consideration to transitional technologies: 
 ▪ For passenger cars and light-duty trucks, we 
focused on battery electric vehicles (BEVs) because 
of the dominance of BEVs in market shares. For 
passenger cars, China’s ratio of BEVs in passenger 
NEV sales has been around 80 percent since 
2016, higher than the EU’s 45–51 percent (ACEA 
2021) and the United States’ 54–78 percent (BTS 
2021b). For trucks, BEVs are more predominant, 
accounting for 99.1 percent of NEV truck sales 
in 2020. Increasing numbers of regions such as 
the United Kingdom; California, United States; 
and Hong Kong have placed PHEVs together 
with ICE vehicles to be phased out because of 
their suboptimal environmental performance 
(Wappelhorst 2021). Following the same rationale, 
PHEVs receive less focus in this study. 
 ▪ For heavy-duty trucks, this study covers LNG 
trucks given their increasing market popularity. 
Hybrid heavy-duty trucks are not considered 
because the fuel economy advantage of hybrid 
heavy-duty trucks is not evident for long-haul 
HDTs. In China, 47 percent of the daily VKTs of 
long-haul HDTs were fulfilled on highways (RIOH 
and Sinoiov 2021) with an average speed of 57 km 
per hour. The fuel savings of HDTs over highway 
cycles were only 3–6 percent compared with 30 
percent fuel savings over city driving cycles (Gao 
et al. 2015). Further, limited hybrid models are 
available in China’s market: There were only three 
hybrid models sold in 2020 (iCET 2021).   
 ▪ For all the vehicle segments, biofuels are not 
considered. See Appendix C to learn why.
Second, the projected growth in NEV sales is 
likely to follow an S-curve (Abramczyk et al. 2017) 
whereby growth is slow when the technology is 
new, but as costs fall and infrastructure expands, 
a tipping point is reached and sales then grow 
exponentially. The S-curves differ by vehicle 
segment, with NEV buses reaching the tipping point 
and other segments still situated at the early stages 
of their S-curves (Table 10). This study uses the 
timing of total cost of ownership parity and public 
incentives to derive the possible tipping points for 
NEVs by vehicle segment.

32
WRI.org.cn
PROGRESSION OF NEVs ALONG THE S-CURVE UNDER THE 
STATED POLICY SCENARIO
POLICY INCENTIVES FOR 
NEV ADOPTION
POLICY INCENTIVES FOR 
CHARGING/REFUELING 
INFRASTRUCTURE
Passenger 
cars
By 2025: NEVs will represent 20% of annual sales a 
By 2030: Clean-energy vehicles will represent 40% of annual salesb 
By 2035: NEV cars will account for 50–60% of annual car sales c 
• National NEV 
procurement 
subsidies; waived NEV 
purchase tax
• Fleet-average fuel 
consumption standard
• Waived demand 
charges for electric 
vehicle charging 
nationwide
• Local subsidies on 
charging facilities’ 
CAPEX and/or O&M
Buses
From 2021: For air pollution control and ecological civilization 
pilot regions, no less than 80% of annual newly added or 
replaced buses should be NEVs d
• National NEV 
procurement 
subsidies; waived NEV 
purchase tax
• National operation 
subsidies for e-buses
• Waived demand 
charges for electric 
vehicle charging 
nationwide
• Local subsidies on 
charging/hydrogen 
refueling facilities’ 
CAPEX and/or O&M
Light-duty 
trucks 
From 2021: For air pollution control and ecological civilization 
pilot regions, no less than 80% of annual newly added or 
replaced light-duty trucks should be NEVs e
• National NEV 
procurement 
subsidies; waived NEV 
purchase tax
• Local operation 
subsidies in selected 
cities such as 
Shenzhen and Beijing
• Preferential city 
access policies in 
selected cities
• Waived demand 
charges for ele ctric 
vehicle charging 
nationwide
• Local subsidies on 
charging/ hydrogen 
refueling facilities’ 
CAPEX and/or O&M
HDTs
By 2030: Clean-energy vehicles will represent 40% of annual salesf 
By 2030: NEV trucks will account for more than 12% of annual 
truck sales g 
• National NEV 
procurement 
subsidies; waived NEV 
purchase tax
• Preferential access 
policies in some ports 
and industrial parks
• Waived demand 
charges for electric 
vehicle charging 
nationwide
• Local subsidies on 
charging/hydrogen 
refueling facilities’ 
CAPEX and/or O&M
Table 9  |   Progression along the S-Curve under the Stated Policy Scenario
Notes:  Although motorcycles are not classified as NEVs in China, this study assumes gasoline-powered motorcycles will be completely electric by 2035. 
                    a. State Council 2020.  b. NDRC 2021.  c. China SAE 2020.  d. State Council 2020.  e. State Council 2020.  f. NDRC 2021.  g. China SAE 2020.
Abbreviations: NEV = new electric vehicle; CAPEX = capital expenses; O&M = operations and maintenance; HDT = heavy-duty truck; e-buses = NEV buses.   
Source: WRI authors, based on existing policies. 
targeted market sharehistoric market share
2010 2020 2030
0
20%
40%
60%
80%
100%
Share of NEVs in 
annual sales
2010 2015 20252020 2030
0
20%
40%
60%
80%
100%
Share of NEVs in 
annual sales
2010 2015 20252020 2030
0
20%
40%
60%
80%
100%
Share of NEVs in 
annual sales
2010 2015 20252020 2030
0
20%
40%
60%
80%
100%
Share of NEVs in 
annual sales
203520252015

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
33
For passenger cars, evidence shows that the 
tipping point is approaching. For example, NEVs 
accounted for 20 percent of China’s passenger car 
sales in November 2021 (CAAM 2021b), meeting 
the 20 percent target set in China’s New Energy 
Vehicle Industrial Development Plan for 2021 
to 2035 five years early (State Council 2020). 
Further, without public subsidies, the TCO parity 
of BEVs and ICE private cars would be reached 
between 2024 and 2030, xi where compact cars 
would reach parity earlier (in 2024–25) and sport 
utility vehicles (SUVs) with large battery sizes 
would reach parity during 2025–30 (Lutsey et al. 
2021; see Appendix B). 
This study assumes the following: 
 ▪ The growth curve of the NEV market share 
in the Stated Policy scenario aligns with the 
nonbinding targets set in China’s Technology 
Roadmap for Energy-Saving and New Energy 
Vehicles 2.0 (the Roadmap; China SAE 2020), 
where NEVs will account for 40 percent of 
passenger car sales by 2030, 50 percent by 
2035, and 100 percent by 2060. 
 ▪ The growth curve of the NEV market share in 
the Deep Electrification scenario aligns with 
the Paris Climate Agreement–compatible 
sectoral target, where BEVs are targeted to 
account for 100 percent of passenger car 
sales by 2035 (NCI and CA 2020). To achieve 
the Paris Agreement–compatible sectoral 
target, policy interventions such as enhanced 
fleet-wide fuel consumption standards, road 
access privileges, and increased infrastructure 
accessibility are necessary.  
For buses, with tremendous public subsidies, 
even though the TCO of BEV buses has not 
achieved cost parity with diesel buses (World 
Bank 2021), NEV buses have gained momentum 
in the country, accounting for over 90 percent 
of the annual bus sales since 2016. Therefore, 
this study assumes NEV buses will account for 
100 percent of the market share starting in 2021 
across all scenarios.
For light-duty trucks: Although the current 1 
percent market share of NEV light-duty trucks 
is far from the 80 percent target set in China’s 
NEV Industrial Development Plan 2021–2035, 
light-duty trucks are edging toward the tipping 
point. The return-to-base nature and limited 
daily mileage of light-duty trucks used for urban 
deliveries make them ideal for electrification 
following buses. For example, with subsidies and 
preferential road access policies, 100 percent of the 
annually registered light-duty trucks are now NEVs 
in Shenzhen. Even without subsidies, the TCO 
parity of BEV light-duty trucks and ICE light-duty 
trucks will be reached in 2024–25 (see Appendix 
B). Therefore, this study assumes 100 percent 
market share of NEVs would be possible from 2035 
across all scenarios.
For heavy-duty trucks: Due to technology 
constraints, xii a fragmented trucking industry 
(Qiu et al. 2020), relatively late timelines for 
TCO parity (Mao et al. 2021), and a lack of policy 
incentives (Xue et al. 2019), NEV HDTs should 
reach the market tipping point later than other 
vehicle segments.  
Within HDTs, vehicles of different payloads and 
applied in different duty cycles have varying 
decarbonization paces: Straight trucks and dump 
trucks commonly used for urban deliveries, drayage, 
and regional operations with daily mileages below 
200 kilometers could be sooner transitioned to 
zero emissions (reaching TCO parity by 2023–25 
in China), and for these types of trucks and duty 
cycles, BEV technology is sufficient. However, for 
long-haul HDTs (with daily mileages over 200 
kilometers and sometimes up to 1,000 kilometers) 
and temperature-controlled refrigerated HDTs, 
the transition would occur more slowly (reaching 
TCO parity by 2030–35). For these types of trucks 
and duty cycles, FCEV technology would be needed 
(Mao et al. 2021; DOT 2021; Agora Energiewende 
2020a; Ledna et al. 2022). 
At present, China’s statistical system does not 
classify HDTs by operational duty cycle. For 
simplicity, this study assumes that all tractor 
trailers weighing above 30 tonnes are long-haul 
vehicles, though straight trucks are also used 
for long-haul shipments in China. Given this 
assumption, long-haul HDTs and refrigerated 
HDTs represent about 50 percent of the current 
HDT fleet, while straight trucks and dump trucks 
used in short-range duty cycles represent the

34
WRI.org.cn
remaining 50 percent (Figure 16). This fleet mix is 
assumed to be stable over time. 
In the Stated Policy scenario, although NDRC (2021) 
(the Action Plan) sets a mandatory target that 
clean-energy vehicles, which include NEVs and NG 
vehicles, represent 40 percent of annual vehicle sales 
in 2030, this target is ambiguous as to the specific 
share of NEVs for the truck segment. Therefore, the 
nonbinding targets set in the Roadmap, which were 
based on consultations with the truck manufacturing 
industry, are used in this study, where NEV trucks 
account for 17 percent of annual truck sales in 2030. 
This study further assumes that starting in 2050, all 
new HDTs operating in urban deliveries, drayage, 
and regional delivery duty cycles will be zero-
emission vehicles, comprising 50 percent of HDT 
sales and 49 percent of the HDT stock.  
In the Deep Electrification scenario, considering 
HDTs have 4–10 years of useful life (Mao et al. 
2021), to achieve net zero by 2060, ICE HDTs 
(including diesel trucks and NG trucks) should stop 
being sold no later than 2050. This means not only 
100 percent of the new HDTs operating in the urban 
delivery, drayage, and regional delivery duty cycles 
will be zero emissions, but also 100 percent of the 
new long-haul HDTs and refrigerated HDTs will be 
zero emissions from 2050 (Figure 17). For the latter, 
FCEV technology would be necessary. This ambitious 
Figure 16  |   Fleet Mix of Heavy-Duty Trucks by Gross Vehicle Weight and Type
Abbreviation: t= tonne.
Source: Data are from a China Automotive Technology and Research Center (CATARC) database (accessed November 2021).
Figure 17  |   Projections for NEV Market Share and Fleet Penetration in Existing Studies
Source: WRI authors; Agora Energiewende 2020a; IEA 2021b; LBNL 2021; UK DfT 2021; ICCSD 2020; CARB 2020. 
a. Market share (%) of NEVs in annual HDT sales b. NEV penetration (%) in the HDT stock
4.5-12 t 12-20 t unknown20-30 t over 30 t
Straight trucks Dump trucks Tractor trailers Cold chain trucks
0
100
200
300
400
Mllion vehicles
ICCSD (2020)_Stated policy ICCSD (2020)_Enhanced policy
ICCSD (2020)_2 degree ICCSD (2020)_1.5 degree
LBNL (2021)_Late NEV strategies LBNL (2021)_Early NEV strategies
This study_Stated policyIEA (2021b)
This study_Deep electrification
2010 205020302020 20602040
0
60%
80%
40%
20%
100%
This study_Stated policy
Agora Energiewende (2020a)
CARB (2020)
This study_Deep decarbonization
UK DfT (2021)_above 26 tonnes
2015 2035 204520252020 2030 2040 2050
0
60%
80%
40%
20%
100%

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
35
target could be achieved through measures such as 
increasing vehicle acquisition subsidies (although 
China aims to phase out the national NEV purchase 
subsidies from 2023, subsidies to NEV HDTs 
should be maintained), introducing HDT operation 
subsidies, establishing fleet-wide fuel consumption 
standards for HDTs, adopting CO2 emission–based 
road pricing, providing road access privileges 
for NEV HDTs, and improving infrastructure 
accessibility and convenience.
Fuel efficiency improvements
China is among the few developing countries with 
comprehensive and stringent requirements for 
vehicle fuel consumption (Table 10): Every vehicle 
manufactured in or imported to China is subject to 
the fuel consumption limits; further, vehicle original 
equipment manufacturers (OEMs) must meet the 
corporate average fuel consumption (CAFC) targets, 
where the accrued CAFC (and NEV) credits can be 
traded among OEMs under the Parallel Management 
Regulation for CAFC and NEV Credits. 
Abbreviations:  CAFC = corporate average fuel consumption; NEV = new energy vehicle; ICE = internal combustion engine; NG = natural gas; BEV = battery electric vehicle;  
NEDC = New European Driving Cycle; WLTP = Worldwide Harmonized Light Vehicles Test Procedure; kWh = kilowatt-hour; km = kilometer; L = liter.
Source: WRI authors, based on existing policies and standards. 
With stricter requirements, China’s fleet-average 
fuel consumption—that is, the average fuel 
consumption of all the cars registered in China 
including ICE vehicles and NEVs—has been 
improving. The fleet-average fuel consumption 
for passenger cars declined from 6.5 L/100 km 
(New European Driving Cycle) in 2016 to 5.61 
L/100 km in 2020, approaching the 5 L/100 km 
target for 2020 (CATARC 2021). With the Phase V 
fleet-average fuel consumption target of 4 L/100 
km for 2025—95 grams of CO 2 per kilometer (g/
km) (Worldwide Harmonized Light Vehicles Test 
Procedure; WLTP)—China’s fleet-average fuel 
consumption for passenger cars will be catching up 
with the EU’s 95 g/km (WLTP) target for 2024 (EU 
P&C 2019).
Despite the improvement in fleet-average fuel 
consumption (including NEVs), the average 
fuel consumption for ICE vehicles alone has not 
significantly improved. This is because fleet-
average fuel consumption is discounted by the 
increased NEV production, where OEMs meet the 
VEHICLE FUEL CONSUMPTION LIMIT CAFC TARGET NEV AND CAFC CREDITS
Passenger cars 
ICE vehicles
4 L/100 km in 2025 (ICE vehicles and NEVs, WLTP)
(As one of the Phase V fuel consumption standards for passenger 
cars, Fuel Consumption Limits for Passenger Cars [GB19578-2021])
4 L/100 km in 2025  
(ICE vehicles and NEVs, WLTP)
(As one of the Phase V fuel consumption 
standards for passenger cars,  
Fuel Consumption Evaluation Methods and 
Targets for Passenger Cars [GB 27999-2019])
18% credits are NEV credits 
(Phase 2 Parallel Management  
Regulation for CAFC  
and NEV Credits)
NEVs 12 kWh/100 km in 2025 (BEVs, NEDC)
(Electric Vehicles’ Energy Consumption Limits [GB/T 36980-2018])
NG vehicles (None) (None) (None)
 Light-duty commercial vehicles
ICE vehicles 20% reduction from Stage 2’s level
(Stage 3 Fuel Consumption Standard for  
Commercial Light-duty Vehicles [GB 20997-2015])
(None) (None)
NEVs (None) (None) (None)
NG vehicles (None (None) (None)
Heavy-duty commercial vehicles
ICE vehicles
15% reduction from Stage 2’s level
(Stage 3 Fuel Consumption Standard for  
Commercial Heavy-duty Vehicles [GB 30510-2018])
(None) (None)
NEVs (None) (None) (None)
NG vehicles (None) (None) (None)
Table 10  |  Compulsory Energy Efficiency Standards and Regulations in China

36
WRI.org.cn
CAFC target by increasing the production of NEVs 
while not greatly improving ICE vehicles’ fuel 
consumption levels (ICCT 2019). Consequently, 
although the fleet-average fuel consumption for 
passenger cars (including NEVs) in China dropped 
13 percent from 2016 to 2020, the average fuel 
consumption for ICE vehicles decreased by only 7 
percent (CATARC 2016, 2021).   
In fact, ICE vehicles have an untapped potential 
for fuel consumption improvements. For 
passenger cars, the 4 L/100 km fleet-average 
target can be met by ICE vehicles alone. 
Particularly, hybrid vehicle adoption could be 
accelerated in China: In 2020, hybrid vehicles 
represented only 2.6 percent of car sales in 
China, behind the EU’s 11.9 percent (ACEA 2021). 
According to the targets in the Roadmap set by 
industrial experts, hybrid cars would account 
for 50–60 percent of ICE car sales in 2025 and 
100 percent in 2035 in China. For ICE HDTs, 
as predicted in the Roadmap, China can further 
reduce HDTs’ fuel consumption by 20 percent in 
2035 by improving aerodynamics and the thermal 
efficiency of engines, among other measures 
(Figure 18). 
Energy efficiency improvements for NEVs are 
equally crucial (Gao et al. 2019). Although 
China established the world’s first standard on 
electric vehicles’ energy consumption limits 
for passenger NEVs, the energy efficiency 
of the commercial NEV fleet is unregulated. 
With increased gross vehicle weights (GVWs), 
some commercial NEVs have seen increases in 
energy consumption. For example, according 
to the Annual Report on the Big Data of New 
Energy Vehicles in China (2021) (Z.P. Wang et 
al. 2021), the fleet-average energy consumption 
of BEV buses in China increased by 10 percent 
from 2018 to 2020. Therefore, this study 
assumes future efficiency improvements will 
occur for commercial NEVs, with the degree of 
improvement based on a literature review—that 
is, the median values of energy consumption 
rates in existing studies (see Figure 19). 
Figure 18  |   Fuel Consumption Improvement Targets in the Roadmap (2020–35)
Abbreviations:  HDT = heavy-duty truck; L = liter; km = kilometer; CLTC = China Light-Duty Vehicle Test Cycle; ICE = internal combustion engine;  
Roadmap = China’s Technology Roadmap for Energy-Saving and New Energy Vehicles 2.0.
Source: China SAE 2020.
a. Passenger cars
HybridICE Market share of hybrids in ICEs
2020 20282024 20322022 20302026 2034 2036
0
7
4
1
2
40%
0%
20%
8
5
3
60%
9
6
80%
10 100%
Fuel consumption (L/100 km, CLTC)
Hybrid out of ICE vehicles (%)
b. HDTs (tractor trailers as an example)
HDT (% reduction)
2020 20282024 20322022 20302026 2034 2036
0
25
10
-60%
-100%
-80%
30
15
5
-40%
35
20
-20%
40
-10%
-15%
-20%
0%
Fuel consumption (L/100 km)

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
37
Coal gasification,  
62%
Steam 
methane 
reforming, 
19%
Industrial by 
products, 
18%
Hydro, 18%Solar, 3%
Electrolysis, 1%
Wind, 6%
Nuclear, 5%
Thermal  
(coal, natural gas), 
68%
In this study, we used the nonbinding targets 
for ICE vehicles in the Stated Policy scenario. 
Considering the targets in the Stated Policy scenario 
are already ambitious, we developed the BAU 
scenario—with no fuel consumption improvements 
for ICE vehicles or NEVs—to reflect the case when 
the targets in the Stated Policy scenario are not met. 
For this study, we used real-world fuel consumption 
instead of certified fuel consumption. Because 
type-approval driving cyclesxiii differ from real-world 
driving conditions and vehicles with larger GVWsxiv 
are increasing in the fleet mix, the real-world fleet-
average fuel consumption of ICE vehicles is larger 
than certified fuel consumption. From 2008 to 2017, 
China’s real-world fleet-average fuel consumption 
for ICE cars was 8.6 L/100 km (iCET 2017), meaning 
that not only did real-world fuel consumption not 
improve over the past decade, but it was also 30% 
higher than certificated consumption. Therefore, to 
capture true fuel use, the study used the real-world 
fuel consumption estimated in COPERT (see Section 
2.2.1) for the base year and assumed that, in the 
future, the gap between real-world fuel consumption 
and certified fuel consumption will close.    
3.2.4 Grid and hydrogen decarbonization   
Because coal is the major feedstock for electricity 
and hydrogen generation in China, how electricity 
and hydrogen are generated play a role in road 
transport decarbonization. According to the China 
Electricity Council, nearly 61 percent of China’s 
electricity generation was sourced from coal in 
Figure 19  |   Energy Efficiency of New Energy Vehicle Tractor Trailers with Gross Vehicle Weights above 36 
Tonnes in 2020 and 2030
Figure 20  |   Current Power Mix and Hydrogen 
Production Mix in China
a. BEVs b. FCEVs
 Abbreviations: GVW = gross vehicle weight; kWh = kilowatt-hour; km = kilometer; H2 = hydrogen; BEV = battery electric vehicles; FCEV = fuel cell electric vehicles. 
Sources: Mareev et al. 2018; Phadke et al. 2021; Liimatainen et al. 2019; T&E 2020b; F.Q. Liu et al. 2021; Mao et al. 2021.
2020 (CEC 2020), compared with 37 percent of 
the power mix sourced from fossil fuelsxv in the EU 
in the same year (Agora Energiewende 2020b); 62 
percent of hydrogen was sourced from high-emitting 
coal gasification in 2018, compared with 95 percent 
of U.S. hydrogen production coming from steam 
methane reforming (DOE 2020; see Figure 20).
Source: CEC 2020; CSI 2018. 
Power generation mix in 2020
Hydrogen production mix in 2018
2020 20202030 2030
0 0
40
120
80
3
100 4
60
2
140 6
160 7
120 5
180 8
200 9
kWh/100 km
kg H2/100 km

38
WRI.org.cn
Coal, 6%
Natural gas, 3%
Because of China’s heavy reliance on coal for 
power and hydrogen generation, the current 
decarbonization potential of NEVs is limited, 
particularly for the energy-intensive heavy-duty 
NEVs. Taking a 40-tonne tractor trailer as an 
example (see Figure 21), a BEV tractor trailer 
saves 25 percent WTW CO2 emissions per 100 km 
travelled compared with the WTW emissions of 
ICE vehicles. These emissions savings are less than 
the 59 percent savings from a NEV passenger car 
versus an ICE passenger car. Further, the emissions 
savings for FCEVs are more insignificant: The WTW 
emissions from a FCEV tractor trailer are almost 
identical to the WTW emissions of an ICE tractor 
trailer and even 11 percent higher than the tailpipe 
emissions of an ICE tractor trailer.  
To decarbonize the transport sector, the power sector 
and hydrogen-related industry must be decarbonized 
simultaneously. In the Stated Policy scenario, 
we used the existing decarbonization roadmaps 
announced in China’s policy directives and those 
proposed by industrial alliances (Figure 22):
 ▪ Power sector decarbonization roadmap: In 
the near term, according to NDRC (2021), 
Figure 21  |   WTW Emissions (TTW + WTT Emissions) of Different Powertrains by Vehicle Segment under the 
Current Power Mix (2020) and Hydrogen Production Mix (2018) 
Note:  •   The energy consumption of tractor trailers is 34 L/100 km for ICE vehicles, 150 kWh/100 km for BEVs, and 8.5 kg/100 km for FCEVs. That of passenger cars (sport utility vehicles) is 
8.6 L/100 km for ICE vehicles and 16.5 kWh/100 km for BEVs, and the energy consumption of buses is 38 L/100 km for ICE vehicles and 109 kWh/100 km for BEVs.   
          •   WRI authors calculated WTT emission factors for petroleum and different hydrogen production processes based on the Greenhouse Gases, Regulated Emissions, and Energy Use 
in Technologies (GREET 2.0) Model (ANL 2014). Emissions from transportation and distribution of hydrogen are not included. An 8 percent electricity transmission and distribution 
loss and charging loss is assumed for BEVs.
Abbreviations:  WTW = well to wheel; TTW = tank to wheel; WTT = well to tank; CO 2 = carbon dioxide; km = kilometer; t = tonne; ICE = internal combustion engine;  
FCEL = fuel cell electric vehicle; BEV = battery electric vehicle; kWh = kilowatt-hour; kg = kilogram; L = liter. 
Source: WRI authors’ calculations. 
Figure 22  |   Power Mix and Hydrogen Production Mix 
Based on China’s Current Commitments
Abbreviation: CCS = carbon capture and storage.
Source: ICCSD 2020; CHA 2019.
Power generation mix in 2020
Hydrogen production mix in 2018
TTW emissions WTT emissions
Tractor trailer (40 t) Bus (10-meter) Passenger car (SUV)
0
60
30
90
120
150
kg CO2 per 100 km travelled
ICE ICE ICEFCEV
1%
25%
40%
59%
BEV BEV BEV
Nuclear, 18%
Hydro, 11%
Steam methane 
reforming,
10%
Industrial by-
products,
5%
Wind, 37%
Electrolysis, 70%
Fossil fuels + 
CCS, 15%
Solar, 23%
Other, 2%

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
39
China’s coal consumption will peak in the 14 th 
five-year period (2021–25), and the installed 
capacities of wind and solar will reach over 
1,200 gigawatts. Over the long term, based on 
China’s Long-Term Low-Carbon Development 
Strategies and Pathways (ICCSD 2020), coal 
should represent 6.5 percent of China’s power 
generation by 2050.  
 ▪ Hydrogen generation decarbonization 
roadmap: As outlined in the White Paper 
on China’s Hydrogen Energy Carrier and 
Fuel Cell Stack Industry (CHA 2019), the 
market share of China’s domestic green 
hydrogen (water electrolysis using 100 
percent renewable energy) production will 
grow from 1 percent in 2020 to 70 percent in 
2050. The share of domestic gray hydrogen 
production will drop to 15 percent, in which 
Notes:  WRI authors calculated WTT emission factors for different hydrogen production processes using the Greenhouse Gases, Regulated Emissions, and Energy Use in Technologies 
(GREET 2.0) Model (ANL 2014).
Abbreviations:  kg CO2 = kilograms of carbon dioxide; ICE = internal combustion engine; FCEV = fuel cell electric vehicle; BEV = battery electric vehicle; t = tonne;  
SUV = sport utility vehicle; TTW = tank to wheel; WTT = well to tank. 
Source: WRI authors’ calculations. 
Figure 23  |   Emissions of Different Powertrains by Vehicle Segment under the Power Mix and Hydrogen 
Production Mix in the Stated Policy Scenario
steam methane reforming and industrial 
by-products will respectively represent 10 
percent and 5 percent. Coal gasification 
facilities will be completely decommissioned 
before 2050. 
The stated policies are already ambitious. If these 
targets for power mix and hydrogen production 
mix can be met, WTW emissions of NEVs will 
drop to nearly zero in 2050 (see Figure 23). As 
a benchmark, a less-ambitious BAU scenario 
(see Table 11) helps us evaluate the emission 
reduction potential of the stated policies and the 
consequences of not meeting these targets. In 
the BAU scenario, a fraction of fossil fuels would 
remain in power generation (25 percent) and 
hydrogen production processes (50 percent) (F.Q. 
Liu et al. 2021).    
TTW emissions WTT emissions
Tractor trailer (40 t) Bus (10-meter) Passenger car (SUV)
0
90
30
120
60
kg CO2 per 100 km travelled
ICE ICE ICEFCEV
98%
98%97%97%
BEV BEV BEV

40
WRI.org.cn
3.2.5 Summary
We modelled five scenarios in this study: the 
Business as Usual scenario, the Stated Policy 
scenario, and three enhanced scenarios—
Structural Change, Deep Electrification, and Deep 
Decarbonization (Table 12).  
The BAU scenario is a counterfactual scenario, 
featured by no improvements in energy efficiency 
and limited degrees of vehicle electrification. 
This scenario helps evaluate the decarbonization 
potential of the country’s stated policies by revealing 
the consequences of not achieving them.   
The Stated Policy scenario projects emissions based 
on the intermediary targets and policies planned 
by the national government and nonbinding 
targets proposed by industrial associations. As 
demonstrated in Sections 3.2.3 and 3.2.4, the 
stated policies are ambitious for fuel efficiency 
improvement measures and power-sector and 
hydrogen-related-sector decarbonization, but 
less ambitious for structural changes and vehicle 
electrification. Therefore, in addition to the Stated 
Policy scenario (“Stated_policy”), we constructed 
three forecasting scenarios: 
 ▪ The Structural Change scenario (“Low_
stock”) is based on the Stated_policy scenario 
but assumes greater degrees of mode shift 
and vehicle occupancy improvements. As a 
result, the scenario is characterized by smaller 
vehicle stocks. 
 ▪ The Deep Electrification scenario (“DeepELE”) 
is based on the Stated_policy scenario but 
involves a more rapid diffusion of NEVs—that 
is, NEVs will represent 100 percent of passenger 
car sales by 2035 and 100 percent of HDT sales 
(including long-haul HDTs and refrigerated 
HDTs) by 2050.  
 ▪ The Deep Decarbonization scenario 
(“DeepDecarb”) is based on the Stated_policy 
scenario but integrates the Low_stock and 
DeepELE scenarios. Therefore, the scenario 
represents the most ambitious case that 
is conducive to attaining China’s carbon 
neutrality target.  
Source: Hydrogen production mix for the Business as Usual scenario is based on WRI authors’ assumptions. The rest of the values come from ICCSD (2020) and CHA (2019).   
Table 11  |   Power Mix and Hydrogen Production Mix under Different Scenarios
2050
BUSINESS AS USUAL STATED POLICY
Power 
generation mix
•  Coal and natural gas (25%)
•  Non-fossil fuel (75%)
•  Coal and natural gas (9%)
•  Non-fossil fuel (92%)
Hydrogen 
production mix
•   Gray hydrogen: coal gasification (15%), steam methane 
reforming (SMR) (15%), industrial by-products (5%)
•   Blue hydrogen: fossil fuels, carbon capture and storage 
(CCS) (15%)
•   Green hydrogen: renewable energy electrolysis (50%)
•   Gray hydrogen: SMR (10%) and industrial by-
products (5%)
•   Blue hydrogen: fossil fuels and CCS (15%)
•   Green hydrogen: renewable energy electrolysis 
(70%)

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
41
Source: WRI authors’ assumptions. 
2020
BUSINESS AS 
USUAL
(BAU)
STATED POLICY
(Stated_policy)
STRUCTURAL 
CHANGE
(Low_stock)
DEEP 
ELECTRIFICATION
(DeepELE)
DEEP 
DECARBONIZATION
(DeepDecarb)
Demand and structural change
Passenger car stock  
in 2020 and 2060 
(million vehicles)
239 
 (170 cars per  
1,000 persons)
506 
(425 cars per 
1,000 persons)
506 
381 
 (300 cars per 1,000 
persons)
506 381 
Freight tkm 
 in 2020 and 2060 
(trillion tkm)
11.2 25.9 
Freight mode share  
in 2020 and 2060
(% of road freight in 
domestic tkm)
54% 50% 50% 40% 50% 40%
Freight average load  
in 2020 and 2060
(tonnes per vehicle 
kilometer)
9.5 9.5 9.5 11.5 9.5 11.5
HDT stock 
 in 2020 and 2060 
(million vehicles)
9.5 20 20 12 20 12
Vehicle electrification
Passenger car 
electrification  
 in 2020 and 2035
(% of NEVs in 
passenger car sales)
15.7% 30% 50% 50% 100% 100% 
HDT electrification  
in 2020 and 2050
(% of NEVs in HDT 
sales)
0.6% 12% 
50% 
(only the HDTs 
operating in urban 
deliveries, drayage, 
and regional 
delivery duty cycles)
50% 
(only the HDTs 
operating in urban 
deliveries, drayage, 
and regional 
delivery duty cycles)
100% 
(all the HDTs, 
including 
long-haul and 
refrigerated HDTs)
100% 
(all the HDTs, 
including 
long-haul and 
refrigerated HDTs)
Fuel efficiency
ICE passenger cars
Fleet average: 5.6 
L/100 km
Hybrid: 2.6% of car 
sales
No 
improvement
Fleet average: 4 L/100 km
Hybrid: 60% of car sales in 2025, 100% in 2035
ICE HDTs (Depends on gross 
vehicle weight)
No 
improvement HDTs: 20% improvement in 2035
NEVs (Depends on gross 
vehicle weight)
No 
improvement (Various degrees of improvement based on gross vehicle weight)
Grid and hydrogen decarbonization
Power mix 
 in 2020 and 2050
(% of non-fossil fuels  
 in power mix)
32% 75% 92% 
Hydrogen mix 
 in 2020 and 2050
(% of gray hydrogen 
 in production mix)
99% 35% 15%
Table 12  |  Key Parameters in the Five Scenarios

42
WRI.org.cn

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
43
MODEL 
RESULTS
CHAPTER 4
This chapter includes our projections for China road 
transport's GHG emissions, energy usage, petroleum 
consumption, and air pollutant emissions up to 2060 under 
different scenarios. It also evaluates the decarbonization 
and air pollution reduction potentials of different measures 
and identifies what policies are cost effective to meet 
China's 2060 carbon neutrality commitment.

44
WRI.org.cn
4.1 Base Year Calibration 
The base year of the study is 2020, when the most 
recent statistical data are available. Despite the decrease 
in transport activities and emissions during the forced 
lockdown period for COVID-19 from February to April 
2020 (Le Quéré 2020), China experienced only slightly 
affected road freight volumes, increased private car 
purchases, and temporarily lower transit ridership 
during that time (Zhou et al. 2020).    
Using the bottom-up approach (see Section 2.2), 
we estimated the base year’s GHG emissions. 
We verified the results with the top-down 
estimates that were derived based on the fossil 
fuel consumption from China’s energy balance 
using the methodology outlined in Su (2017). We 
reconciled the difference between the top-down 
and bottom-up estimates by adjusting vehicle 
kilometers travelled, following the recommended 
procedure in IPCC (2006). 
For the base year, we calculated and compared 
the GHG emissions of three emissions scopes: 
TTW GHG emissions (the emissions from vehicle 
operations), WTW_ele emissions (the TTW 
emissions and upstream emissions from the 
production of electricity and hydrogen), and the 
full scope of WTW emissions. 
The results show the following: TTW GHG emissions 
were 1,168 Mt CO2eq in 2020, almost identical to 
the WTW_ele emissions (1,186 Mt CO2eq) (Figure 
24). This is due to limited NEV penetration now. In 
contrast, the full scope of WTW GHG emissions was 
19 percent higher than TTW emissions as emissions 
from the oil refinery and gas processing industries 
are included in WTW emissions. Regardless of the 
emissions scope, CO2 accounted for the majority 
(96–97 percent) of the GHG emissions.
Contributions to GHG emissions and air pollutants 
varied across vehicle segments (see Figure 25):
 ▪ CO2 emissions: With a large fleet size (70 percent 
of the vehicle stock), private cars contributed the 
largest share of WTW_ele CO2 emissions (40 
percent). Following private cars were heavy-
duty trucks (35 percent of CO2 emissions) and 
light-duty trucks (17 percent of CO2 emissions). 
Notably, heavy-duty trucks’ 35 percent CO2 
emissions contribution is disproportionate to its 
relatively small fleet size (3 percent of the vehicle 
Figure 24  |   GHG Emissions from China’s Road Transport Sector in 2020
Notes: Greenhouse gases include carbon dioxide, nitrous oxide (N20), and methane (CH4). N2O and CH4 use 20-year global warming potential (GWP) values from IPCC (2014).
Abbreviations:  Mt CO2eq = million tonnes of carbon dioxide equivalent; TTW = tank to wheel; WTW_ele = TTW emissions and upstream emissions from the production of electricity and 
hydrogen; WTW = well to wheel.
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model. 
CH4 (20-year GWP) CO2N2O (20-year GWP)
0
500
1,000
1,500
Mt CO2eq
1,168
TTW
1,186
WTW_ele
1,389
WTW
1,131 1,149
1,340

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
45
Figure 25  |  Breakdowns of Vehicle Stocks, GHG Emissions, and Air Pollutants in 2020
Notes:  Abbreviations: CO2 = carbon dioxide; LDT = light-duty truck; HDT = heavy-duty truck; WTW_ele = tank to wheel emissions and upstream emissions from the production of 
electricity and hydrogen; CH4 = methane; N2O = nitrous oxide; NOx = nitrogen oxides; PM = particulate matter; NMHC = non-methane hydrocarbons; CO = carbon monoxide.
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model.
Vehicle stock CO2 (WTW_ele)
CH4 (WTW_ele)
NOx
NMHC
N2O (WTW_ele)
PM
CO
Private cars, 70%
HDTs, 3%
LDTs, 6%
Motorcycles, 20%
Coaches, 1%
Buses, 0%
Taxis, 0%
Private cars, 14%
Buses, 18%
Taxis, 15%
Motorcycles, 1%
Coaches, 0%
HDTs, 51%
LDTs, 1%
Buses, 3%Private cars, 3%
LDTs, 16%
Motorcycles, 
0%
Coaches, 10%
Taxis, 0%
HDTs, 68%
HDTs, 11%
LDTs, 13%
Buses, 0%
Private cars, 60%
Motorcycles, 13%
Coaches, 1%
Taxis, 2%
HDTs, 25% Private cars, 40%
LDTs, 18%
Motorcycles, 9%
Taxis, 3%
Coaches, 4%
Buses, 1%
Private cars, 40%
Coaches, 3%
Taxis, 2%
Buses, 2%
HDTs, 35%
LDTs, 17%
Motorcycles, 1%
Private cars, 21%
LDTs, 21%
Coaches, 4%
Taxis, 1%
Buses, 1%
HDTs, 51%
Motorcycles, 1%
Private cars, 10%
Taxis, 0%
LDTs, 5%
Buses, 2%
Coaches, 10%
HDTs, 72% Motorcycles,
1%

46
WRI.org.cn
stock). Although motorcycles represented 20 
percent of the vehicle stock, their corresponding 
CO2 emissions were insignificant.
 ▪ CH4 emissions: High methane emissions were 
observed for fleets with relatively large shares 
of NG vehicles, including heavy-duty trucks 
(51 percent), buses (18 percent), and taxis (15 
percent). This is because of the high methane 
emissions typically associated with NG vehicles 
(Pan et al. 2020). 
 ▪ N2O emissions were primarily attributable to 
diesel vehicles—heavy-duty trucks (51 percent) 
and light-duty trucks (21 percent).  
 ▪ Air pollutants: Private cars contributed the 
largest share of CO (40 percent) and NMHC (60 
percent) emissions, and fossil fuel–powered 
motorcycles’ NMHC emissions were also 
considerable (13 percent). Heavy-duty trucks 
and light-duty trucks were the major sources of 
toxic NOx and PM emissions.     
4.2 Scenario Projections
This section includes our projections for WTW_
ele GHG emissions, energy usage, petroleum 
consumption, and air pollutant emissions up to 
2060 under different scenarios. 
We did not consider the full scope of WTW emissions 
because decarbonizing the oil refinery and gas 
processing industries is difficult and involves 
different policy recommendations. However, we did 
consider emissions from the production of electricity 
and hydrogen because it is still unclear if switching 
to electricity and hydrogen should count as low 
carbon when power and hydrogen production is not 
decarbonized (Gustafsson et al. 2021). 
4.2.1 GHG emissions 
Results from the scenario analysis suggest the 
following (see Figure 26 and Table 13):
In the near term, the growth in road transport 
GHG emissions should continue. The likely peak 
Figure 26  |   Carbon Dioxide and Greenhouse Gas Emission Projections under Different Scenarios 
Note: Greenhouse gases include carbon dioxide, nitrous oxide, and methane. Nitrous oxide and methane use 20-year global warming potential values from IPCC (2014).
Abbreviations:  Mt CO2eq = million tonnes of carbon dioxide equivalent; CO2 = carbon dioxide; GHGs = greenhouse gases; BAU = Business as Usual scenario; Stated_policy = Stated 
Policy scenario; DeepELE = Deep Electrification scenario; Low_stock = Structural Change scenario; DeepDecarb = Deep Decarbonization scenario.
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model.
CO2
GHGs
Low_stock
DeepELE
DeepDecarb
Stated_policy
BAU
Mt CO2eq Mt CO2
20252020 20602050 20552030 2035 2040 2045
0
500
2,000
1,500
1,000
20252020 20602050 20552030 2035 2040 2045
0
500
2,000
1,500
1,000

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
47
years of road transport’s GHG emissions are 
between 2025 and 2035, with peak GHG emissions 
ranging from 1,340 Mt CO2eq (13 percent increase 
from 2020) to 1,909 Mt CO2eq (61 percent increase 
from 2020). The Stated_policy scenario suggests 
that if China implements the stated policies outlined 
by the government and targets set by industrial 
associations, the road transport sector’s GHG 
emissions are likely to peak by 2030 at 1,638 Mt 
CO2eq. The Low_stock and DeepELE scenarios 
indicate that with enhanced measures such as 
structural changes and vehicle electrification, the 
peak year would be advanced to 2026 and 2028, 
respectively, and peak GHG emissions would 
be lower—1,358 Mt CO 2eq and 1,585 Mt CO2eq, 
respectively. Of note is that in the near term, 
structural changes are more effective at peaking 
emissions earlier and reducing emissions to a 
greater extent than vehicle electrification.   
In the long term, GHG emissions in 2060 vary 
widely based on the scenario, ranging from 63 
Mt CO2eq (a 95 percent decrease from 2020) to 
1,495 Mt CO2eq (a 26 percent increase from 2020). 
Among the policy scenarios, the Stated_policy 
scenario shows that if the stated policies are 
effectively implemented over time, China’s road 
transport GHG emissions would be 50 percent 
lower than in 2020. If additional measures 
such as structural changes and higher degrees 
of vehicle electrification are taken, as assumed 
with the DeepDecarb scenario, road transport 
emissions could be mitigated by 95 percent 
compared with 2020’s level. Over the long term, 
vehicle electrification would surpass structural 
changes to become the measure with the highest 
decarbonization potential. 
CH4 and N2O demonstrate slightly different 
pathways because both CH 4 and N2O are not 
only GHG emissions, but also regulated air 
pollutants, subject to China’s vehicle exhaust 
emission standards. Unlike other pollutants (See 
Section 4.2.3 and Figure 27), in the BAU scenario, 
neither CH 4 emissions nor N 2O emissions decline 
significantly after the implementation of the 
Table 13  |   Carbon Dioxide Emissions and Greenhouse Gas Emissions in the Peak Year and in 2060 under 
Different Scenarios 
Notes:    a.  Parentheses denote the change in emissions compared with the level in 2020. Color green denotes the emissions are lower than the 2020's level, while red denotes the 
emissions are higher than the 2020's level. 
Abbreviations:  CO2 = carbon dioxide; GHG = greenhouse gas; Mt CO2eq = million tonnes of carbon dioxide equivalent; BAU = Business as Usual scenario;  
Stated_policy = Stated Policy scenario; DeepELE = Deep Electrification scenario; Low_stock = Structural Change scenario; DeepDecarb = Deep Decarbonization scenario.
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model.
PEAK YEAR PEAK EMISSIONS
(Mt CO2eq)
2060 EMISSIONS
(Mt CO2eq)
CUMULATIVE EMISSIONS
(2020–60)
(Mt CO2eq)
CO2 GHGs CO2 GHGs CO2 GHGs CO2 GHGs
BAU 2035 2035 1,867
(63%)a
1,909
(61%)
1,455
(27%)
1,495
(26%) 68,228 69,947
Stated_policy 2030 2030 1,598
(39%)
1,638
(38%)
556
(-52%)
595
(-50%) 46,910 48,615
DeepELE 2028 2028 1,546
(35%)
1,585
(34%)
88
(-92%)
88
(-93%) 35,818 36,518
Low_stock 2026 2026 1,322
(15%)
1,358
(15%)
360
(-69%)
384
(-68%) 36,080 3 7, 2 6 8
DeepDecarb 2025 2025 1,301
(13%)
1,340
(13%)
63
(-95%)
63
(-95%) 28,643 29,205

48
WRI.org.cn
China 6 standard in 2020: CH 4 emissions initially 
drop from 2020 to 2030 due to the enforcement 
of China 6 but rebound after 2030 because 
the increasing adoption of NG vehicles offsets 
the decrease in per-vehicle NG emissions; the 
limited drop in N 2O emissions occurs because the 
deployment of aftertreatment systems in diesel 
vehicles to meet China 6’s NOx emissions limit 
would lead to increased N 2O emissions (Clairotte 
et al. 2020). Therefore, as suggested by the 
DeepELE and DeepDecarb scenarios, in addition 
to relying on tightening emission exhaust 
standards, vehicle electrification can control CH 4 
and N2O emissions.
4.2.2 Energy demand 
Energy demand in the road transport sector will 
experience drastic changes, both in terms of 
absolute energy volumes and the energy mix.  
The increased penetration of NEVs will 
substantially cut road transport’s demand for fossil 
fuels (gasoline, diesel, and natural gas) (see Figures 
28 and 29):
 ▪ Petroleum demand could peak earlier than the 
2030 target set in NDRC (2021). In the Stated_
policy scenario, the country’s petroleum demand 
will peak in 2027, the same peak year for global 
petroleum demand forecasted by BloombergNEF 
(2021). The peak year would occur even sooner 
(2024–25) in the Low_stock, Deep_ELE, 
and DeepDecarb scenarios with reinforced 
decarbonization measures such as structural 
changes and vehicle electrification. In all the 
policy scenarios, petroleum consumption in 2060 
would be 66–100 percent lower than in 2020, 
showing that the country’s road transport sector 
will be less dependent on petroleum (petroleum 
use would be fully eliminated in 2060 in the 
Deep_ELE and DeepDecarb scenarios). 
Figure 27  |   Methane and Nitrous Oxide Emissions Projections under Different Scenarios 
Notes: Nitrous oxide and methane use 20-year global warming potential values in IPCC (2014).
Abbreviations:  Mt CO2eq = million tonnes of carbon dioxide equivalent; CH4 = methane; N20 = nitrous oxide; BAU = Business as Usual scenario; Stated_policy = Stated Policy scenario; 
DeepELE = Deep Electrification scenario; Low_stock = Structural Change scenario; DeepDecarb = Deep Decarbonization scenario.
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model. 
CH4
N2O
Low_stockDeepELE DeepDecarbStated_policyBAU
20252020 20602050 20552030 2035 2040 2045
0
5
20
15
10
Mt CO2eq
20252020 20602050 20552030 2035 2040 2045
0
10
40
30
20
Mt CO2eq

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
49
 ▪ Future demand for natural gas is more 
precarious: If NG vehicles play a significant role 
in meeting the clean energy vehicle sales target 
of 40 percent in 2030, the demand for natural 
gas will peak in 2060, with peak demand a 
179 percent increase over 2020’s level (see the 
Stated_policy and Low_stock scenarios); if NG 
vehicles are not recommended and are soon 
displaced by NEVs, the demand for natural gas 
would peak in 2024–26 and follow petroleum’s 
path to be eliminated in 2060 (see the Deep_
ELE and DeepDecarb scenarios). 
By contrast, the growth in electricity and hydrogen 
demand would follow a strong upward trend. The 
electricity demand in 2060 varies between 2.8 
billion gigajoules (GJ) and 6.2 billion GJ, and 
hydrogen demand between 0.4 billion GJ and 3.3 
billion GJ (Figure 30). 
Noteworthy is that a smaller NEV fleet would lead 
to less electricity and hydrogen demand. In the 
DeepDecarb scenario, electricity consumption in 
2060 would be 24 percent lower and hydrogen 
demand 39 percent lower than in the DeepELE 
Figure 28  |   Total Energy and Petroleum Consumption in the Road Transport Sector 
Figure 29  |   Petroleum Consumption in the Road Transport Sector
Abbreviations:  BAU = Business as Usual scenario; Stated_policy = Stated Policy scenario; DeepELE = Deep Electrification scenario; Low_stock = Structural Change scenario; 
DeepDecarb = Deep Decarbonization scenario.
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model.
 Abbreviations:  BAU = Business as Usual scenario; Stated_policy = Stated Policy scenario; DeepELE = Deep Electrification scenario; Low_stock = Structural Change scenario; 
DeepDecarb = Deep Decarbonization scenario.
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model.
Low_stock
Low_stock
DeepELE
DeepELE
DeepDecarb
DeepDecarb
Stated_policy
Stated_policy
BAU
BAU
2025
2025
2020
2020
2060
2060
2050
2050
2055
2055
2030
2030
2035
2035
2040
2040
2045
2045
0
0
5
5
30
25
30
25
20
20
15
15
10
10
billion gigajoules billion gigajoules

50
WRI.org.cn
Figure 30  |   Energy Demand Breakdowns under Different Scenarios
Abbreviations:  BAU = Business as Usual scenario; Stated_policy = Stated Policy scenario; DeepELE = Deep Electrification scenario; Low_stock = Structural Change scenario; 
DeepDecarb = Deep Decarbonization scenario.
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model
BAU Stated_policy
DeepELE Low_stock
DeepDecarb
Gasoline Diesel Natural gas Electricity Hydrogen
2025
2025
2025
2025
2025
2020
2020
2020
2020
2020
2060
2060
2060
2060
2060
2050
2050
2050
2050
2050
2055
2055
2055
2055
2055
2030
2030
2030
2030
2030
2035
2035
2035
2035
2035
2040
2040
2040
2040
2040
2045
2045
2045
2045
2045
0
0
0
0
0
5
5
5
5
5
20
20
20
20
20
30
30
30
30
30
15
15
15
15
15
25
25
25
25
25
10
10
10
10
10
billion gigajoulesbillion gigajoulesbillion gigajoules
billion gigajoulesbillion gigajoules

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
51
scenario (see Table 14). Therefore, managing 
vehicle ownership and usage is critical to lessening 
investments in installed capacity for power and 
hydrogen generation. 
4.2.3 Air pollutants
Unlike GHG emissions and energy consumption, 
future emissions from air pollutants would keep 
declining across all the scenarios that decouple from 
GHG emission trajectories (see Figure 31). 
Even under the BAU scenario, all the regulated air 
pollutants exhibit varying degrees of reduction, 
in which NOx emissions in 2060 decline by 73 
percent from the 2020 level, PM by 84 percent, 
NMHC by 90 percent, and CO by 41 percent. This 
is mainly attributable to the enforcement of the 
China 6 standard for all vehicles starting in 2021 
and the increasing adoption of end-of-pipe control 
measures (see Box 2). If the China 6 standard is 
not enforced, China will experience growing NOx, 
NMHC, and CO emissions (Figure 32).   
Although nationwide, air pollutants from the road 
transport sector will be effectively controlled, 
sustained pollution abatement efforts are needed 
for a few reasons. First, air pollutants are local, 
and it is likely that regions with dense populations 
would still be exposed to significant vehicular 
emissions and high health risks. With the World 
Health Organization’s new and stricter Global Air 
Quality Guidelines (WHO 2021), China’s battle 
against air pollution is expected to continue. 
Second, besides the road transport sector, non-
road transport sectors such as shipping and non-
road machinery are also primary sources of air 
pollutants that require attention (Feng et al. 2019; 
Shao 2021). Third, although we did not consider 
any next-generation China exhaust emission 
standard (such as a Euro 7 equivalent) or an ultra-
low emissions requirement for NOx emissions (see 
Box 2), the benefits of a tougher standard on NEV 
promotion and air quality improvement should not 
be underrated by policymakers (ACEA 2022). 
Table 14  |   Energy Demand in the Peak Year and in 2060 under Different Scenarios 
Notes:  Fossil fuels include gasoline, diesel, and natural gas. The peak years for petroleum (gasoline and diesel) are the same as the peak years for fossil fuels. The percentage denotes the level 
of emissions in comparison to that in 2020. Color green denotes the emissions are lower than the 2020's level, while red denotes the emissions are higher than the 2020's level.   
Abbreviations:  GJ = gigajoules; BAU = Business as Usual scenario; Stated_policy = Stated Policy scenario; DeepELE = Deep Electrification scenario; Low_stock = Structural Change 
scenario; DeepDecarb = Deep Decarbonization scenario.
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model.
PEAK 
YEAR FOR 
PETROLEUM
PEAK 
YEAR FOR 
NATURAL 
GAS
PETROLEUM
(billion GJ)
NATURAL GAS
(billion GJ)
ELECTRICITY
(billion GJ)
HYDROGEN
(billion GJ)
PEAK 2060 PEAK 2060 2060 2060
BAU 2035 2060
24.7 1 7. 4 1.4 1.4 2.8 0.4
+52% +7% +97% +97% +2,500% +401,400%
Stated_policy 2027 2060
20.4 5.49 2.0 2.0 5.0 0.7
+26% -66% +179% +179% +4,500% +659,900%
DeepELE 2025 2026
19.7 0.0 1.1 0.0 6.2 3.3
+22% -100% +52% -100% +5,600% +3,299,900%
Low_stock 2025 2060
1 7. 7 3.5 1.3 1.3 3.9 0.4
+9% -78% +71% +71% +3,500% +399,900%
DeepDecarb 2024 2024
1 7. 5 0.0 0.0 0.0 4.7 2.0
+8% -100% -100% -100% +4,200% +2,019,900%

52
WRI.org.cn
Figure 31  |   Air Pollutant Emissions from the Road Transport Sector
Abbreviations:  CO = carbon monoxide; NOx = nitrogen oxides; PM2.5 = particulate matter 2.5 micrometers or less in diameter; PM10 = particulate matter 10 micrometers or less in 
diameter; NMHC = non-methane hydrocarbons; BAU = Business as Usual scenario; Stated_policy = Stated Policy scenario; DeepELE = Deep Electrification scenario; 
Low_stock = Structural Change scenario; DeepDecarb = Deep Decarbonization scenario.
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model.
CO NOx
PM2.5 PM10
NMHC
2025
2025
2025
2025
2025
2020
2020
2020
2020
2020
2060
2060
2060
2060
2060
2050
2050
2050
2050
2050
2055
2055
2055
2055
2055
2030
2030
2030
2030
2030
2035
2035
2035
2035
2035
2040
2040
2040
2040
2040
2045
2045
2045
2045
2045
0
0
0
0
0
1 1
4
0.05
2
4
0.10
6
0.15
4
6
0.15
3
1
3
5
0.10
3
5
2 2
0.05
million tonnesmillion tonnesmillion tonnes
million tonnesmillion tonnes
Low_stockDeepELE DeepDecarbStated_policyBAU

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
53
2
1
5
7
4
6
3
Figure 32  |   Air Pollutant Reductions Resulting from the Introduction of China 6 Standard 
 Abbreviations:  CO = carbon monoxide; NOx = nitrogen oxides; PM2.5 = particulate matter 2.5 micrometers or less in diameter; PM10 = particulate matter 10 micrometers or less in 
diameter; NMHC = non-methane hydrocarbons; BAU = Business as Usual scenario.
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model.
CO NOx
PM2.5 PM10
NMHC
BAU China6_Not enforced
2025
2025
2025
2025
2025
2020
2020
2020
2020
2020
2060
2060
2060
2060
2060
2050
2050
2050
2050
2050
2055
2055
2055
2055
2055
2030
2030
2030
2030
2030
2035
2035
2035
2035
2035
2040
2040
2040
2040
2040
2045
2045
2045
2045
2045
0
0
0
0
0
2
1
1
5
0.2 0.2
4
7
0.3 0.3
7
4
3
6
5
6
3
0.1 0.1
2
million tonnesmillion tonnesmillion tonnes
million tonnesmillion tonnes

54
WRI.org.cn
Box  2  |   China’s End-of-Pipe Emission Control Standards
China’s vehicle exhaust emission standards have evolved rapidly 
over the past 20 years from China 1 to China 6. Now, China 6 is 
one of the most stringent emission standards in the world, with 
the air pollutant limits in China 6a (the standard for light-duty 
vehicles was effective as of 2020, and that for heavy-duty trucks 
as of 2021) equating to those of Euro 6 (see Figure B2.1 for an 
example of limits for diesel HDTs). After China 6b becomes 
effective in 2023, the emission limits will be even lower than 
those in Euro 6.a 
However, other global emission regulations show that there is 
still room for improvement in China’s emission standard. For 
example, compared with the NOx limit (0.27 g/kWh) mandated 
by the United States’ 2010 emission standard for HDTs, China 
6’s limit (0.4 g/kWh) is still on the higher end. Further, with 
California’s adoption of the Heavy-Duty Engine and Vehicle 
Omnibus Regulation in 2020, which mandates a further 90 
percent reduction of NOx emissions from HDTs from 2024 to 2027 , 
the difference in NOx limits will be widened. 
Figure source: Wei et al. 2020.
Unit: grams/kilowatt-hour
Box Notes: a. ICCT 2017 .  
Figure  B2.1  |   Limits on Nitrogen Oxide and Particulate Matter Emissions from Diesel Heavy-Duty Trucks in China, the 
European Union, and the United States 
PMPMPM NOxNOxNOx
EUUnited States China
2001 2005 2009 20132002 2006 2010 2014 20172003 2007 2011 2015 20182004 2008 2012 2016 2019 2020
China I
8.0
Euro III
5.0
US 1998
5.44
Euro IV
3.5
Euro VI
0.4
US 2010
0.27
US 2014
China II
7. 0 China III
5.0 China IV
3.5
China VI
0.4
0.010.020.10.15
0.36
0.10 0.02
0.134
0.01
0.013
China V
2.0
Euro V
2.0
US 2004
2.7
US 2007~09 ABT
1.6

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
55
4.3   Attribution Analysis of Road 
Transport Decarbonization
4.3.1  Decarbonization potentials of different 
measures
This section evaluates the decarbonization 
potentials of different measures and identifies 
what policies are needed to meet the 2060 carbon 
neutrality commitment. 
Attribution analysis 1: From BAU to Stated_
policy  
The model results reveal that compared with the 
BAU scenario, stated policies would offer a 21,404 
Mt CO2eq cumulative emission reduction from 2020 
to 2060. Among these policies, vehicle electrification 
measures offer the largest emission reduction 
(10,092 Mt CO2eq), followed by improvements to 
vehicle fuel efficiency (7,003 Mt CO2eq) and power 
(and hydrogen) sector decarbonization (4,309 Mt 
CO2eq). Realizing these decarbonization potentials 
is contingent upon successfully implementing the 
stated policies (Figure 33 and Table 15). 
Figure 33  |   Greenhouse Gas Reduction Potentials of Key Decarbonization Interventions: From the BAU to 
Stated_policy Scenarios 
 Abbreviations:  BAU = Business as Usual scenario; Stated_policy = Stated Policy scenario; Mt CO2eq = million tonnes of carbon dioxide equivalent; H2 = hydrogen.
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model.
Notes:   a. Extrapolated by WRI authors based on NDRC (2021). b. China SAE 2020. c. Extrapolated by WRI authors. d. MIIT 2019, 2021; China SAE 2020. e. MIIT 2019, 2021; China SAE 2020. f. State 
Council 2020. g. ICCSD 2020. h. Extrapolated by WRI authors based on NDRC (2021). i. China SAE 2020. j. China SAE 2020. k. Extrapolated by WRI authors. l. China SAE 2020. m. CHA 2019.
Abbreviations: NEV = new energy vehicle; L = liter; km = kilometer; kWh = kilowatt-hour; tkm = tonne-kilometers; HDT = heavy-duty truck.
STRUCTURAL 
CHANGES
VEHICLE 
ELECTRIFICATION FUEL EFFICIENCY IMPROVEMENTS POWER AND HYDROGEN 
DECARBONIZATION
Passenger
transport
Targets:
425 cars per 1,000 
persons, 70% green 
transport mode share 
in 2060a
Targets:
By 2035: NEVs represent 50% 
of passenger car salesb 
By 2060: NEVs represent 100% 
of passenger car salesc
Targets:
By 2025: fleet-average fuel consumption for 
passenger cars of 4 L/100 km; hybrid vehicles 
represent 60% of passenger car salesd 
By 2035: hybrid vehicles represent 100% of 
passenger car salese
By 2025: NEV energy efficiency of 12 kWh/100 kmf
Targets:
By 2050: 92% non-fossil fuels 
in power mixg
Freight 
transport
Targets:
50% of road freight in 
domestic tkm; average 
load: 9.5 tonnes per 
vehicle-kilometerh
Targets:
By 2030: NEV trucks represent 
12% of truck salesi 
By 2050: NEVs represent 50% 
of HDT salesj
Targets:
By 2035: 20% improvement in HDTs’ fuel 
consumptionk 
Continuous improvement in NEVs’ energy 
efficiency 
Targets:
By 2050: 15% gray hydrogen in 
production mixl 
2020–60
Cumulative emission reduction
(Mt CO2eq)
Fuel efficiency 7 ,003
Passenger transport 
electrification 3,601
Road freight
electrification 6,491
Clean power/H 2 4,309
Table 15  |   Key Targets in the Stated Policy Scenario
BAU Stated_policyClean power/H2Passenger electrification Freight electrificationFuel efficiency
20252020 20602050 20552030 2035 2040 2045
0
500
2,000
1,500
1,000
Mt CO2eq

56
WRI.org.cn
Attribution analysis 2: From Stated_policy 
to DeepDecarb  
To further cut emissions from the level in the Stated_
policy scenario to that in the DeepDecarb scenario, 
this study shows that China’s road transport sector 
needs more ambitious targets on vehicle electrification 
and structural changes (see Figure 34 and Table 16). 
Compared with the Stated_policy scenario,
 ▪ higher vehicle electrification targets—including 
100 percent NEVs in passenger car sales by 2035 
and 100 percent NEVs in long-haul HDT sales 
and refrigerated HDT sales by 2050—would be 
instrumental to delivering an additional 11,007 
Mt CO2eq cumulative emission reduction; and 
 ▪ explicit and radical structural change targets—
including 40 percent of road freight in the total tkm 
and an average 11.5 tonne load per HDT vehicle-
kilometer—would be key to delivering an additional 
7,175 Mt CO2eq cumulative emission reduction. 
Altogether, decarbonizing the freight sector offers 
the largest emission reduction potential of 12,568 
Mt CO2eq.     
Figure 34  |   Greenhouse Gas Reduction Potentials of Key Decarbonization Interventions: From Stated_policy to 
DeepDecarb Scenarios 
 Abbreviations:  BAU = Business as Usual scenario; Stated_policy = Stated Policy scenario; Mt CO2eq = million tonnes of carbon dioxide equivalent; H2 = hydrogen.
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model.
2020–60
Cumulative emission reduction
(Mt CO2eq)
Passenger transport 
electrification 3,768
Road freight
electrification 7, 2 3 9
Passenger structural 
change 1,846
Freight structural 
change 5,329
DeepDecarb Stated_policyFreight structural changePassenger structural changePassenger electrification Freight electrification
20252020 20602050 20552030 2035 2040 2045
0
500
2,000
1,500
1,000
Mt CO2eq

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
57
Attribution analysis 3: From BAU to 
DeepDecarb  
To bend the emission curve from that in the BAU 
scenario to that in the DeepDecarb scenario, 
three decarbonization measures must occur in the 
country’s road transport sector (see Figure 35):
 ▪ Vehicle electrification—especially for heavy- 
and light-duty trucks—has the largest 
decarbonization potential over the long term, 
contributing to 48 percent of the cumulative 
GHG emission reduction from 2020 to 2060. 
If the carbon intensity of upstream power/
hydrogen generation is reduced simultaneously, 
vehicle electrification could result in a 60 
percent cumulative emission reduction.    
 ▪ Structural changes and fuel efficiency 
improvements are the second- and third-
most effective measures to be undertaken, 
respectively. Structural change measures 
have the second-largest mitigation potential 
over the long term—by managing vehicle fleet 
growth and kilometers travelled, cumulative 
GHG emissions from 2020 to 2060 could 
be cut by 23 percent. Energy efficiency 
improvements could generate a 17 percent 
cumulative emission reduction; tightening 
the fleet-wide fuel efficiency standard also has 
the benefit of stimulating NEV production 
(Wappelhorst et al. 2021). 
Abbreviations: NEV = new energy vehicle; tkm = tonne-kilometer; HDT = heavy-duty truck; CO 2 = carbon dioxide. 
Source: WRI authors’ recommendations. 
Table 16  |   Key Targets and Policy Interventions to Achieve Deep Decarbonization
STRUCTURAL CHANGES VEHICLE ELECTRIFICATION FUEL EFFICIENCY 
IMPROVEMENTS
POWER AND HYDROGEN 
DECARBONIZATION
Passenger
transport
Targets:
300 cars per 1,000 persons, 75–85% green transport 
mode share in 2060
Targets:
NEVs represent 100% of 
passenger car sales in 2035
Same targets as the  
Stated_policy scenario
Same targets as the  
Stated_policy scenario
Tactics:
• Shift transit service paradigm with intelligent 
demand responsive services
• Increase the share of infrastructure investments 
in transit, active mobility, and railway 
• Pursue travel demand management and carbon 
pricing
• Promote Mobility-as-a-Service and ride sharing  
Tactics:
• Enhance fleet-wide fuel 
consumption standard
• Provide road access privileges 
to NEVs
• Increase infrastructure 
accessibility
• Introduce carbon taxes
Freight 
transport
Targets:
40% of road freight in domestic tkm; average 
load = 11.5 tonnes per HDT vehicle-kilometer
Targets:
NEVs represent 100% of HDT sales 
in 2050 (HDTs for short-range and 
long-range duty cycles)
Same targets as the  
Stated_policy scenario
Same targets as the  
Stated_policy scenario
Tactics:
• Shift bulk commodities to railways and 
waterways and promote intermodal freight for 
high-value freight
• Invest in intermodal infrastructure and 
equipment, improve service connectivity, 
rationalize pricing and scheduling, and enhance 
first-/last-mile truck delivery
• Encourage the use of non-truck operating 
carriers and facilitate drop-and-hook operations
• Employ fuel taxes and road charges
Tactics:
• Increase vehicle acquisition and 
introduce operation subsidies 
• Introduce fleet-wide fuel 
consumption standard for HDTs
• Introduce CO2-emission indexed 
road pricing 
• Provide road access privileges
• Increase infrastructure 
accessibility

58
WRI.org.cn
However, these instruments have varying mitigation 
potentials over time:
 ▪ In the near term (2020–35), structural changes 
have the largest mitigation potential because 
the adoption of NEVs will have not yet reached 
a tipping point. 
 ▪ Over the long term (2035–60), the uptake 
of NEVs will overtake structural changes 
to have the largest mitigation potential. To 
unlock the long-term abatement potential of 
vehicle electrification, technology advances 
are necessary, particularly the development of 
zero-emission technologies on long-haul HDTs 
and refrigerated HDTs (currently, two to five 
times more expensive than ICE HDTs) as well 
as low-cost technologies for green hydrogen 
production and distribution (currently, three to 
four times more expensive than gray hydrogen) 
(IRENA 2020). 
From a sectoral perspective, freight transport 
would play a more important role than passenger 
transport. Concretely, attaining the carbon 
neutrality goal requires a radical shift in truck fleet 
technologies and freight structures:
 ▪ Truck electrification (both light- and 
heavy-duty trucks) would need to result 
in a reduction of 12,524 Mt of cumulative 
emissions—nearly two times the emission 
Figure 35  |   GHG Reduction Potentials of Key Decarbonization Interventions: From Business as Usual to Deep 
Decarbonization
Abbreviations: Mt CO2eq = million tonnes of carbon dioxide equivalent; H2 = hydrogen; BAU = Business as Usual scenario; DeepDecarb = Deep Decarbonization scenario. 
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model. 
2020–35 2035–60
AVERAGE ANNUAL 
EMISSION REDUCTION
(Mt CO2eq/year)
CUMULATIVE 
EMISSION REDUCTION 
(Mt CO2eq)
AVERAGE ANNUAL 
EMISSION REDUCTION
(Mt CO2eq/year)
CUMULATIVE 
EMISSION REDUCTION 
(Mt CO2eq)
Fuel efficiency 65 1,036 240 6,003  
Passenger transport 
electrification 61 982 239 5,970  
Road freight electrification 51 821 468 11,703  
Passenger structural change 62  996  52 1,302
Freight structural change 167 2,679 167 4,165
Clean power/H 2 12 187 196 4,899
DeepDecarb BAU
Mt CO2eq
20252020 20602050 20552030 2035 2040 2045
0
500
2,000
1,500
1,000
Passenger structural change Freight structural changePassenger electrification Freight electrificationFuel efficiency
Clean power/H2

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
59
reduction associated with passenger vehicle 
electrification. Particularly, technologies and 
policies need to tackle the hard-to-abate long-
haul HDTs and refrigerated HDTs. 
 ▪ Freight transport’s structural changes would need 
to result in a reduction of 6,844 Mt of cumulative 
GHG emissions—nearly three times the emission 
reduction associated with passenger transport’s 
structural changes. Particularly, explicit freight 
structural change targets and coordinated policies 
are needed to facilitate the transition. 
Further, to inform decarbonization policymaking in 
the freight sector, China needs better statistical data 
systems on commodity flows (by mode, distance, 
and origin/destination pairs) as well as HDT fleet 
breakdowns by operational duty cycles.
Attribution analysis 4: Decarbonization 
potential of NG vehicles
NG vehicles account for a considerable fraction 
of China’s vehicle fleet. This study assumes that 
the CH4 TTW emission factor for China 5 heavy-
duty trucks is 3 percent of NG consumption, and 
the emission factor for China 6 heavy-duty trucks 
ranges from 0.4 to 1 percent of NG consumption 
based on on-road testing results (Pan et al. 2020). 
The estimated per-vehicle emissions show that the 
CO2 emissions from an LNG heavy-duty vehicle are 
20 percent lower than those from a diesel vehicle, 
but the GHG emission reduction potential of an 
LNG heavy-duty vehicle is less significant:
 ▪ For China 6 LNG heavy-duty vehicles, the TTW 
GHG emissions (20-year GWP) are 12 percent 
lower than those from a diesel vehicle when the 
TTW CH4 emission factor is 0.4 percent of NG 
consumption, and the GHG emissions are about 
the same as those of diesel vehicles when the 
TTW CH4 emission factor is 1 percent. 
 ▪ For China 5 LNG heavy-duty vehicles, the 
TTW GHG emissions are even higher than 
those from diesel vehicles as larger amounts 
of methane escape from China 5 vehicles (such 
as crankcase emissions and dynamic venting 
of the fuel system) that outweigh the CO 2 
emissions savings (Pan et al. 2020; Mottschall 
et al. 2020).
To evaluate the GHG emission implications of the 
expected promotion of NG vehicles, we compared 
the Stated_policy scenario with an NG scenario 
(see Figure 36). In the NG scenario, LNG heavy-
duty trucks meeting the China 6 emission standard 
represent 20 percent of the annual heavy-duty 
truck sales in 2030 (higher than the 15 percent 
in the Stated_policy scenario), and 50 percent in 
2050 (compared with the constant 15 percent in 
the Stated_policy scenario). The results show the 
following (see Figure 37):
 ▪ In 2060, a larger NG fleet in the NG scenario 
would result in an 11 percent further reduction 
in CO2 emissions and a less than 7 percent 
further reduction in GHG emissions compared 
with the Stated_policy scenario.  
 ▪ For cumulative emissions reductions from 2020 
to 2060, a larger fleet of LNG heavy-duty trucks 
in the NG scenario would lead to a 3 percent 
cumulative CO2 emission reduction compared 
with the Stated_policy scenario; the cumulative 
GHG emission reduction would be even lower, 
at less than 3 percent. 
In summary, the above analysis indicates that when 
the China 6 standard is stringently enforced and the 
real-world emissions of NG vehicles meet (or are 
lower than) the CH4 emission limit, an LNG heavy-
duty truck would result in an up to 20 percent CO2 
emission reduction and 12 percent GHG emission 
reduction compared with the emissions from a 
diesel truck. In the scenario analysis, when the 
market share of LNG heavy-duty trucks rises to 
50 percent in 2050 in the Stated_policy scenario 
(compared with the original 15 percent), the wider 
adoption of LNG trucks leads to 7 percent GHG 
emission reduction in 2060 and to a less than 3 
percent cumulative GHG emission reduction from 
2020 to 2060 compared with the Stated_policy 
scenario. If the upstream WTT emissions associated 
with NG processing are taken into account, the 
GHG emission reduction potential of NG vehicles 
would possibly further shrink (Pan et al. 2020).   
Apart from the limited environmental benefit, 
the widespread uptake of NG vehicles also raises 
concerns over NG import dependency, NG price 
affordability, and newly added NG infrastructure 
such as pipelines and storage reservoirs that could

60
WRI.org.cn
soon become stranded assets when NEVs take hold. 
Therefore, China needs to scrutinize its 2030 clean 
energy vehicle target (40 percent) in the Action 
Plan to determine whether and to what extent NG 
vehicles should be promoted. 
Figure 36  |   Annual Sales in the Stated_policy and Natural Gas Scenarios
Figure 37  |   Comparison of Carbon Dioxide and Greenhouse Gas Emissions in the Stated_policy  
and Natural Gas Scenarios 
Stated_policy
CO2
NG
GHGs GHGs
Abbreviations: NG = natural gas; BEV = battery electric vehicle; FCEV = fuel cell electric vehicle; LNG = liquefied natural gas.
Source: WRI authors’ assumptions.
Notes:  The methane tank-to-wheel emission factor for China 5 heavy-duty trucks is 3 percent of NG consumption, and the emission factor for China 6 heavy-duty trucks ranges from 0.4–1 
percent of NG consumption depending on on-road testing results (Pan et al. 2020). Methane uses 20-year global warming potential values from IPCC (2014).
Abbreviations: Mt CO2eq = million tonnes of carbon dioxide equivalent; GHGs = greenhouse gases; NG = natural gas; CH4 = methane; EF = emission factor. 
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model. 
NGStated_policy NG (CH4 EF=1%)Stated_policy NG (CH4 EF=0.4%)Stated_policy
Diesel_shareLNG_ShareBEV_share FCEV_share
2025 20252020 20202060 20602050 20502055 20552030 20302035 20352040 20402045 2045
0 0
40% 40%
20% 20%
100% 100%
80% 80%
60% 60%
Mt CO2eq
2020 206020502030 2040
0
500
2,000
1,500
1,000
Mt CO2eq
2020 206020502030 2040
0
500
2,000
1,500
1,000
Mt CO2eq
2020 206020502030 2040
0
500
2,000
1,500
1,000

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
61
4.3.2 Marginal abatement cost analysis 
Decarbonizing the transport sector requires 
making large investments in both traditional and 
emerging fields—from making railway and street 
improvements to acquiring NEVs and expanding 
the charging/refueling network. Studies suggest 
that to enable China’s net-zero transition, 90–174 
trillion CNY in cumulative low-carbon investments 
will need to be mobilized from 2020 to 2050 (BCG 
2020; ICCSD 2020; Goldman Sachs 2021). Across 
all sectors, the transport sector will attract the most 
investment according to BCG (2020), or the second 
most—following the power sector—according to 
ICCSD (2020). 
This study first evaluates the levels of low-carbon 
investment required to achieve the GHG emissions 
reduction in the different scenarios compared 
with those in the BAU scenario, using the method 
outlined in Section 2.2.2. Two types of low-carbon 
investments are considered, namely NEV promotion 
and infrastructure investments to facilitate 
structural changes. 
The results show that large low-carbon investments 
amounting to 39–83 trillion CNY cumulatively are 
needed from 2020 to 2060 (compared with the BAU 
scenario) to decarbonize China’s road transport 
sector. The levels of investment are greater than 
those found in BCG (2020), ICCSD (2020), and 
Goldman Sachs (2021) because we used a longer 
time frame and broader coverage of investments 
(Figure 38).xvi The investment demand is the largest 
from now till 2035 and will steadily decline over 
time. Among all the scenarios, the Low_stock 
scenario provides the lowest-cost mitigation 
pathway due to a smaller vehicle fleet (the average 
abatement cost is 675 CNY per tonne of CO2eq 
reduced). The DeepELE scenario is the highest-cost 
mitigation pathway, with an average abatement cost 
of about three times (2,510 CNY per tonne CO2eq 
reduced) the cost in the Low_stock scenario.  
Figure 38  |   Low-Carbon Investments (2020–60) under Different Scenarios
Abbreviations:  CNY = Chinese yuan; CO2eq = carbon dioxide equivalent, Stated_policy = Stated Policy scenario; DeepELE = Deep Electrification scenario;  
Low-stock = Structural Change scenario; DeepDecarb = Deep Decarbonization scenario.
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model. 
Stated_policy DeepELE Low_stock DeepDecarb
Cumulative low-carbon 
investments
(billion CNY, 2020 value)
39,503 83,896 22,070 54,226
Average abatement cost
(CNY per tonne CO 2eq reduced) 1,852 2,510 675 1,331
Low_stockDeepELE DeepDecarbStated_policybillion CNY, 2020 value
20252020 20602050 20552030 2035 2040 2045
0
500
4,000
3,500
3,000
2,000
1,500
2,500
1,000

62
WRI.org.cn
Further, we constructed marginal abatement cost 
curves (MACCs) to evaluate the cost-effectiveness of 
the mitigation measures in the DeepDecarb scenario 
in comparison to the BAU scenario. As the abatement 
costs evolve rapidly over time, we chose to look at 
three snapshots—2025 (that is, the 14th five-year 
period), 2030, and 2050 (see Figures 39, 40, and 41, 
respectively). The three MACCs indicate the following:
 ▪ Structural changes and fuel efficiency 
improvements are consistently low-cost 
options. Compared with the BAU scenario, 
both measures offer considerable net cost 
savings. For example, although public transit 
and freight infrastructure are expensive, 
structural changes can lead to considerable 
cost savings for vehicle acquisition, operation, 
and charging/hydrogen infrastructure 
installation, owing to a smaller vehicle fleet. 
Consequently, the unit abatement costs of 
passenger and freight structural changes 
in 2030 are -14.7 CNY and -4.1 CNY per 
kilogram of GHG reduced, respectively (Figure 
40). Making fuel efficiency improvements 
is another cost-saving option, with a unit 
abatement cost of -4.0 CNY per kilogram 
in 2030. This is because cost-efficient ICE 
technologies to reduce fuel consumption (such 
as hybridization, new engine technologies, 
and vehicle downsizing) will have yet to be 
deployed at scale. The future fuel savings from 
ICE vehicles would be large enough to offset 
the rise in vehicle prices (to meet stricter fuel 
consumption standards) (Yang and Cui 2020). 
 ▪ Abatement costs change significantly for 
vehicle electrification. For example, the unit 
abatement cost of freight vehicle electrification 
declines from 81.9 CNY per kilogram in 2025 
to 5.8 CNY in 2030 and -0.6 CNY in 2050 
(Figures 39, 40, and 41, respectively). This is 
because from now until 2030, the lifetime TCO 
of NEV HDTs will remain high. Only after TCO 
parity is reached around 2030–35 will NEVs 
become an affordable option, exhibiting net 
cost savings compared with ICE vehicles.  
The following is noteworthy: 
 ▪ Although needed investments in public transit 
and freight railways are lower, investments 
alone do not lead to mode shift. Without 
complementary measures, solely making 
infrastructure investments would have the 
associated risk of leading to infrastructure 
underutilization, which would result in 
higher emissions than having highly utilized 
infrastructure (Spielmann et al. 2010; ITF 
2013). Therefore, comprehensive instruments 
such as travel demand management, MaaS, 
emission-based road pricing, and service quality 
improvements should be employed. 
 ▪ The high abatement costs of vehicle electrification 
should not deter relevant investments. In 
fact, investments in vehicle acquisition and 
infrastructure expansion are critical because only 
through economies of scale (as NEVs become 
more widely adopted) would NEV costs drop. 
Figure 39  |   Annual Marginal Abatement Cost Curve for 2025
Abbreviations: CNY = Chinese yuan; tCO2eq = tonnes of carbon dioxide equivalent; Mt = million tonnes.
Source: WRI authors’ calculations.
Structural changeVehicle electrification Fuel efficiency
1,000 CNY/tCO2eq
0 600400
Freight electrification
Mt CO2eq in 2025
Fuel efficiencyFreight structural change
Passenger structural change
Passenger electrification
200 650550350150 45025050 500300100
0
30
-30
90
60

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
63
Figure 40  |   Annual Marginal Abatement Cost Curve for 2030
Figure 41  |   Annual Marginal Abatement Cost Curve for 2050
Abbreviations: CNY = Chinese yuan; tCO2eq = tonnes of carbon dioxide equivalent; Mt = million tonnes.
Source: WRI authors’ calculations.
Abbreviations: CNY = Chinese yuan; tCO2eq = tonnes of carbon dioxide equivalent; Mt = million tonnes.
Source: WRI authors’ calculations.
Structural changeVehicle electrification Fuel efficiency
Structural changeVehicle electrification Fuel efficiency
1,000 CNY/tCO2eq
Mt CO2eq in 2050
Fuel efficiency Passenger electrification
Freight structural change
Passenger structural change
Freight electrification
0 24,00016,000 26,00022,00014,000 18,00010,0002,000 6,000 20,00012,0004,000 8,000
0
-7. 0
-6.0
-5.0
-4.0
-3.0
-2.0
-1.0
1,000 CNY/tCO2eq
Freight electrification
Mt CO2eq in 2030
Fuel efficiencyFreight structural change
Passenger structural change
Passenger electrification
0 2,4001,600 2,6002,2001,400 1,8001,000200 600 2,0001,200400 800
0
2
-16
-14
-12
-10
-8
-6
-4
-2
6
4

64
WRI.org.cn
4.4  GHG Emissions and Air 
Pollutant Co-control 
Potentials
Measures with large decarbonization potentials at 
low cost do not necessarily produce air quality co-
benefits. 
To evaluate mitigation measures’ co-control 
potentials in reducing GHGs and air pollutants, we 
employed a “co-control effect coordinate system” 
(Hu et al. 2020). In the coordination system (see 
Figure 42), the vertical axis and the horizontal 
axis, respectively, represent the cumulative GHG 
emission reduction and cumulative air pollutant 
reduction compared with the BAU scenario. 
Mitigation measures falling in the third quadrant 
are the measures with co-control potential. We 
investigated cumulative emission reductions under 
two time frames—the near term (2020–35) and the 
long term (2035–60).
As shown in Figure 42, vehicle electrification 
and structural changes not only have the largest 
decarbonization potentials, but also the greatest 
potential to curb air pollution. However, not all 
GHG mitigation measures would deliver air quality 
co-benefits (Table 17): 
Figure 42  |   Co-control Potentials of Different Decarbonization Measures Compared with the Business as  
Usual Scenario
Note:  Abbreviations: CO = carbon monoxide; GHG = greenhouse gas; NOx = nitrogen oxides; PM2.5 = particular matter less than 2.5 micrometers in diameter; PM10 = particular matter 
less than 10 micrometers in diameter; NMHC = non-methane hydrocarbons; Mt CO2eq = million tonnes of carbon dioxide equivalent; D_ELE_T = freight vehicle electrification in the 
DeepELE scenario; D_ELE_P = passenger vehicle electrification in the DeepELE scenario; ELE_T = freight vehicle electrification in the Stated_policy sceniario; ELE_T = passenger 
vehicle electrification in the Stated_policy scenario; FE =  fuel efficiency improvement in the Stated_policy scenario; SHIFT_T = freight structural change in the Low_stock 
scenario; SHIFT_P = passenger structural change in the Low_stock scenario; NG_T = natural gas vehicle adoption in the Stated_policy scenario.
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model. 
Interactions between CO and GHGs: 2020-35
Interactions between NOx and GHGs: 2020-35
Interactions between CO and GHGs: 2035-60
Interactions between NOx and GHGs: 2035-60
-2,500 0-500
0
-0.1
-0.2
-0.3
-0.4
-0.5
-0.6
-1,000
FE
SHIFT_P D_ELE_P
ELE_T
D_ELE_T
SHIFT_T
NG_T
-1,500-2,000
GHGs (Mt CO2eq)
CO (Mt)
-15,000 -10,000 -5,000 0
0
-0.2
-0.4
-0.6
-0.8
-1
-1.4
-1.2
FED_ELE_P
ELE_T
D_ELE_T
SHIFT_P
SHIFT_T
ELE_P NG_T
GHGs (Mt CO2eq)
MOx (Mt)
-15,000 0
0
-0.1
-0.2
-0.3
-0.4
-0.5
-0.6
D_ELE_P
ELE_T
D_ELE_T
SHIFT_T
ELE_P
NG_T
-5,000-10,000
GHGs (Mt CO2eq)
CO (Mt)
SHIFT_P
-2,500 0-500
0
-0.05
-0.1
-0.15
-0.2
-0.25
-0.3
ELE_T
SHIFT_T
-1,000-1,500-2,000
GHGs (Mt CO2eq)
NOx (Mt)
SHIFT_P
D_ELE_P
D_ELE_T
ELE_P NG_T

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
65
-2,500 0-500
0
-0.0005
-0.001
-0.0015
-0.002
-0.0025
-1,000
FE
SHIFT_P
D_ELE_P
ELE_P
ELE_T
D_ELE_TSHIFT_T
NG_T
-1,500-2,000
GHGs (Mt CO2eq)
PM2.5 (Mt)
Figure 42  |   Co-control Potentials of Different Decarbonization Measures Compared with the Business as  
Usual Scenario
 Abbreviations:  CO = carbon monoxide; GHG = greenhouse gas; NOx = nitrogen oxides; PM2.5 = particular matter less than 2.5 micrometers in diameter; PM10 = particular matter less than 
10 micrometers in diameter; NMHC = non-methane hydrocarbons; Mt CO2eq = million tonnes of carbon dioxide equivalent; D_ELE_T = freight vehicle electrification in the 
DeepELE scenario; D_ELE_P = passenger vehicle electrification in the DeepELE scenario; ELE_T = freight vehicle electrification in the Stated_policy sceniario; ELE_T = 
passenger vehicle electrification in the Stated_policy scenario; FE =  fuel efficiency improvement in the Stated_policy scenario; SHIFT_T = freight structural change in the 
Low_stock scenario; SHIFT_P = passenger structural change in the Low_stock scenario; NG_T = natural gas vehicle adoption in the Stated_policy scenario.
Source: WRI authors’ calculations using the Low Emissions Analysis Platform model. 
Interactions between PM2.5 and GHGs: 2020-35
Interactions between PM10 and GHGs: 2020-35
Interactions between NMHC and GHGs: 2020-35
Interactions between PM2.5 and GHGs: 2035-60
Interactions between PM10 and GHGs: 2035-60
Interactions between NMHC and GHGs: 2035-60
-2,500 0-500
0
-0.0005
-0.001
-0.0015
-0.002
-0.0025
ELE_T
SHIFT_T
-1,000-1,500-2,000
GHGs (Mt CO2eq)
PM10 (Mt)
SHIFT_P
D_ELE_P
D_ELE_T
ELE_P
NG_TFE
-1,500 0-500
0
-0.1
-0.2
-0.3
-0.4
-0.5
-0.6
ELE_T
FE
SHIFT_T
-1,000
GHGs (Mt CO2eq)
MNVOC (Mt)
SHIFT_P
D_ELE_P
D_ELE_T
ELE_P
NG_T
-15,000 -10,000 -5,000 0
0
-0.05
-0.1
-0.15
-0.2
D_ELE_P
ELE_T
D_ELE_T
SHIFT_P
FE
SHIFT_T
ELE_P
NG_T
GHGs (Mt CO2eq)
MNVOC (Mt)
-16,000 -14,000 0
0
-0.005
-0.01
-0.015
D_ELE_P
ELE_T
SHIFT_T ELE_P
FE NG_T
-8,000 -6,000 -4,000 -2,000-12,000 -10,000
GHGs (Mt CO2eq)
PM2.5 (Mt)
SHIFT_P
D_ELE_T
-16,000 -10,000-14,000 -12,000 -4,000 -2,000-8,000 -6,000 0
0
-0.005
-0.01
-0.015
GHGs (Mt CO2eq)
PM10 (Mt)
FE
D_ELE_P
ELE_T
SHIFT_T
NG_T
SHIFT_P
ELE_P
D_ELE_T

66
WRI.org.cn
RESEARCH CO-CONTROL EFFECTS POLICY IMPLICATIONS
Fuel efficiency 
standards
This study General fuel efficiency measures: 
Reduce GHG emissions, neutral to air 
pollutants
--
O’Driscoll et al. 2018 Hybrid (gasoline) vehicles:  
Reduce GHG and air pollutants
Promote hybrid (gasoline) 
vehicles
Liang et al. 2012
Saliba et al. 2017
O’Driscoll et al. 2018
Gasoline direct injection:  
Reduce GHG emissions but increase air 
pollutants
Enforce China 6 standard and 
enhance inspection/ maintenance 
programs for in-use vehicles
NG vehicle  
promotion
This study
Mottschall et al. 2020
T&E 2020a
NG vehicles:  
Possibly increase GHG emissions, reduce/
neutral to air pollutants
Tighten China 6 standard on 
non-tailpipe CH4 emissions from 
NG vehicles, enhance inspection/
maintenance programs
NEV promotion
This study NEV promotion:  
Reduce GHG emissions and air pollutants --
Peng et al. 2021 NEVs and upstream emissions:  
Reduce GHG emissions, increase 
upstream air pollutants
Couple NEV promotion with the 
decarbonization of the upstream 
power and industrial sector
Passenger structural 
changes
This study Passenger structural changes:  
Reduce GHG emissions and air pollutants --
Freight structural 
changes
This study Freight structural changes:  
Reduce GHG emissions and air pollutants --
Shao 2020 Freight structural changes  
(mode shift to railways):  
Reduce GHG emissions, increase 
upstream air pollutants
Decarbonize the upstream 
power sector, promote railway 
electrification, and reduce 
railway backhauls 
Table 17  |  The Co-control Effects of Different Decarbonization Measures
Notes:  Green cells  indicate that the measure can reduce both GHG emissions and air pollutants, and yellow cells  mean that the measure can reduce only GHG/ air pollutant 
emissions. 
Abbreviations: GHG = greenhouse gas; CH4 = methane; NG = natural gas; NEV = new energy vehicle. 
Source: WRI authors, based on this study and existing literature.

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
67
 ▪ Limited co-control effects were found for 
fuel efficiency improvement measures—fuel 
efficiency improvements lead to GHG emission 
reductions but are neutral to air pollution 
control. In fact, in the real world, different 
energy-efficiency technologies lead to varying 
co-control effects. For example, hybrid 
(gasoline) vehicle technologies emit less GHG 
emissions and air pollutants, especially in urban 
driving conditions (O’Driscoll et al. 2018). By 
contrast, gasoline direct injection (GDI) engine 
technology as an emerging fuel-efficiency 
measure (Saliba et al. 2017; O’Driscoll et al. 
2018) generates more particulate masses and 
numbers than traditional technologies (Liang 
et al. 2012; O’Driscoll et al. 2018). Although 
remedy measures such as gasoline particulate 
filters help mitigate GDI vehicles’ particulate 
emissions (Saliba et al. 2017), they tend to lead 
to fuel economy penalties and CO2 emission 
increases (Mamakos 2011).xvii  
 ▪ For tailpipe emissions, NEV promotion and 
structural changes have co-control potential. 
Nonetheless, for WTW emissions, some 
studies suggest NEV promotion would increase 
GHG emissions and air pollutants when 
electricity generation uses the 2015 power 
mix and hydrogen is produced from coal 
gasification and steam methane reforming 
(Peng et al. 2021). Likewise, due to coal-
dependent electricity generation and the 
use of diesel trains and empty backhauls 
of railway shipments, freight mode shift 
from road transport to electric trains tends 
to emit more GHGs, PM, and NOx (Shao 
2020). Therefore, for NEV promotion and 
freight mode shift to yield air quality and 
climate co-benefits, the measures must be 
coupled with decarbonization of the upstream 
power and industrial sectors as well as 
railway electrification and improvements in 
operational efficiency.

68
WRI.org.cn

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
69
CONCLUSION  
AND DISCUSSION
Although this study examines how China's road transport 
sector might be decarbonized, it also has limitations such as 
the unidimensional goal of GHG emission mitigation, the lack 
of causal links between interventions and policy targets, and 
the underestimation of certain emissions. 
CHAPTER 5

70
WRI.org.cn
China’s road transport sector plays an important 
role in meeting carbon early peaking and carbon 
neutrality goals. This study examines how the 
sector might be decarbonized by modelling five 
scenarios using the LEAP model. The results 
indicate the following:
First, in the medium term, the peaking timeline for 
GHG emissions from China’s road transport sector 
would be during 2025–35 and that for petroleum 
demand would be during 2024–30 under all 
scenarios except Business as Usual. If the country’s 
stated policies are effectively implemented over 
time, China could peak road transport emissions 
before 2030 and petroleum consumption before 
2027. The peaking timeline could be further 
advanced to 2025 for GHG emissions and 2024 for 
petroleum consumption by employing structural 
change measures. 
Second, over the long term, with policy 
interventions, it would be possible to reduce 
road transport GHG emissions in 2060 by 50–95 
percent from 2020’s level. To achieve the largest 
emission reduction potential of 95 percent, 
vehicle electrification, structural changes, fuel 
efficiency improvements, and power and hydrogen 
decarbonization are critical. 
This study has the following limitations: 
 ▪ First, we designed the scenarios to meet 
the unidimensional goal of GHG emission 
mitigation, which may not ensure that other 
sustainable development goals will also be met. 
For example, to alleviate traffic congestion, 
promote social equity, reduce road safety risks, 
and lessen public expenditure, more proactive 
structural change measures would be required.
 ▪ Second, the causal links between policy 
interventions (such as public subsidies and road 
pricing) and the attainment of policy targets 
(such as vehicle electrification and structural 
changes) are weak. Future quantitative analysis 
is necessary to strengthen the causal links and 
inform better policymaking.
 ▪ Third, air pollutants from motor vehicles 
vary significantly depending on the extent of 
aftertreatment device degradation, driving 
cycles, vehicle loads, weather conditions, 
and more. Without taking these factors into 
consideration, this study may overstate the 
effectiveness of the China 6 emission standard. 
Over the long term, with policy 
interventions, it would be possible to 
reduce road transport GHG emissions 
in 2060 by 50–95 percent from 
2020’s level.

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
71

72
WRI.org.cn

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
73
APPENDIX A.  
SOCIOECONOMIC 
ASSUMPTIONS AND 
DEMAND FORECASTING 
METHODS
The socioeconomic assumptions of this study 
are based on the Shared Socioeconomic 
Pathways (SSPs) (Riahi et al. 2012), which are 
a set of socioeconomic projections (including 
for population and GDP) widely adopted by 
the integrated assessment model community. 
Among six SSP pathways, SSP2 was adopted 
for this analysis because it is designed to extend 
historical trends. In the SSP2 pathway (Figure 
A1), China’s population is forecast to peak 
Figure A1  |   Population and GDP Projections in the Shared Socioeconomic Pathway 2
POPULATION PEAK YEAR PEAK POPULATION POPULATION IN 2060 GDP PEAK YEAR GDP AS OF 2060 
SSP2 2025–30 1.39 billion 1.16 billion Not yet for 2060 US$52,145 billion 
(2005 dollars)
Abbreviations: SSP2 = Shared Socioeconomic Pathway 2; GDP = gross domestic product; PPP = purchasing power parity.
Source: WRI authors’ calculations.
a. Population projection (millions)  
2025 20602050 20552030 2035 2040 20452010 20202015
1,050
1,250
1,350
1,450
1,150
b. GDP/PPP projection (US$ billions, 2005 dollars)
2025 20602050 20552030 2035 2040 20452010 20202015
0
20,000
40,000
60,000
50,000
10,000
30,000

74
WRI.org.cn
around 2025–30 at 1.39 billion. The GDP projection 
follows China’s “New Normal,” and per capita GDP is 
expected to increase to US$44,806 (in 2005 constant 
dollars) in 2060, almost seven times the 2010 level.
Passenger car ownership 
forecasting method
We used the Gompertz model (Equation 8) to model 
the long-term relationship between passenger car 
stocks and GDP per capita and to forecast China’s 
future passenger car ownership. 
V(x)=γe αe βx
 (Equation 8)
where, 
V(x) is the estimated vehicles per 1,000 persons
x is GDP per capita
γ is the future vehicle saturation level
α and β  are the coefficients to be estimated using the 
equation 
Equation 8 is transformed into Equation 9, which 
can be solved by linear regression: 
ln(ln(V(x)-lnγ)=ln(α)+ βx (Equation 9)
We estimated the Gompertz curve using historical 
data on China’s GDP per capita and vehicles per 
1,000 persons (NBS 2002, 2003, 2004, 2005, 
2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 
2014, 2015, 2016, 2017, 2018, 2019) as well as the 
assumed future car saturation levels. Based on 
the literature reviewed in Section 3.2.1, this study 
assumes that the saturation levels for car ownership 
would be 300 cars per 1,000 persons in the BAU 
scenario and 425 cars per 1,000 persons in the 
Structural Change scenario in 2060. The empirical 
results are shown in Figure A2. The results are 
statistically significant and indicate that China’s car 
ownership is situated in the rapid growth stage and 
future maximum car ownership could range from 
381 to 506 million.  
Figure A2  |   China’s Passenger Car Ownership Projection (2020–60) under Different Car Saturation Levels
LN(α) β MAXIMUM CAR OWNERSHIP
300 cars 
per 1,000 persons
-2.03060***
(-147)
-0.00015***
(-109)
381 million
(2040)
425 cars 
per 1,000 persons
-1.98078***
(-195)
-0.00012***
(-122)
506 million
(2045)
Notes: T-statistics are shown in parentheses: * p < 0.05; ** p < 0.01; *** p < 0.001.
Source: WRI authors’ calculations. 
Historic data300 cars per 1,000 persons 425 cars per 1,000 persons
10,000 Vehicles
20252020 20602050 20552030 2035 2040 2045
0
30,000
20,000
10,000
60,000
50,000
40,000

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
75
Domestic freight tkm forecasting 
method 
We employed the elasticity method that is 
commonly used in integrated assessment models to 
model the long-term nonlinear relationship among 
freight tkm, GDP per capita, and fuel (carbon) 
prices. 
D(x)=α∙x β
         ∙ x price  (Equation 10)
where,
D(x) is the estimated freight demand
x income and x price   are the indexes for income per capita 
and fuel (carbon) prices compared 
with the starting year (1990)
α is the starting year’s calibrated coefficient
β and γ  are the long-term income elasticity and 
price elasticity, respectively, to be estimated 
using the equation
Figure A3  |   China’s Domestic Freight Demand Forecast
Table A1  |   Long-Term Income Elasticities for Freight Demand in China, the United States, and Germany
2020–30 2030–60
Income elasticity 0.99 0.99
Fuel (carbon) price elasticity -0.2–-0.5 -0.5–-0.7
CHINA (1990–2020) UNITED STATES (1980–2018) Germany (1990–2020)
0.99 0.40 1.01
Abbreviation: tkm = tonne-kilometer.
Source: WRI authors’ calculations. 
Source: Freight demand data are from NBS (2021); BTS (2021a); and OECD (n.d.). Population and GDP data come from the World Bank database: https://data.worldbank.org.  
income
γ
β γ
Based on historical observations (1990–2020), we 
estimated China’s long-term income elasticity for 
freight tkm. The result shows that the elasticity is 
higher than that in the United States (from 1980 to 
2018) but slightly lower than that in Germany (from 
1990 to 2020) (see Table A1). Using Germany as 
a benchmark, this study assumes China’s income 
elasticity will remain fixed at 0.99.
For price elasticity, this study assumes the effect 
of fuel prices on freight demand was limited in the 
past but will become significant in the future. Using 
existing modelled elasticities in Edelenbosch et al. 
(2017), the study assumes China’s long-term price 
elasticity will vary from -0.2 to -0.5 between 2020 and 
2030, and from -0.5 to -0.7 between 2030 and 2060.
The projected result shows that China’s freight 
demand is situated at the rapid growth stage and 
that future freight demand will plateau at 25.9 
trillion tkm in 2055–60.  
Historic dataFixed income elasticity Fixed income elasticity and varying price effect
billion tkm
20252020 20602050 20552030 2035 2040 2045
0
30,000
20,000
10,000
50,000
40,000

76
WRI.org.cn
APPENDIX B.  
LIFETIME TOTAL 
COST OF OWNERSHIP 
PROJECTION
The TCO of zero-emission vehicles is 
anticipated to decline rapidly due to 
continuous reductions in battery pack costs, 
research and development (R&D) expenses, 
warranty costs (i.e., cost of failure), and 
energy efficiency improvements. Further, 
this study assumes that the capital cost of 
ICE vehicles will experience a slight increase 
over time with tightened fuel efficiency and 
exhaust emission standards. The rest of the 
costs are assumed to be constant. 
 ▪ The reduction in battery pack costs  
is attributed to two factors—a lower 
unit cost for battery packs and smaller 
battery capacities due to an improved 
energy intensity of electric vehicles. 
The decline in the unit cost for battery 
packs is captured by the “learning curve” 
that describes the reduction in unit 
production costs of battery packs as a 
function of accumulated production 
volumes, approximated by electric 
vehicle sales volumes in this study. Using 
data on China’s battery pack prices and 
production volumes to perform the 
regression, we estimated the learning 
coefficient of unit production costs of 
battery packs to be -0.26 (learning rate 
= 17 percent). Our projection for future 
energy intensity improvements is based 
on a literature review.
Unit_Costbattery pack,t
=Unit_Costbattery pack,0×(  Vt  )b  
 (Equation 11)
Battery sizet=Energy intensityt×Range 
Costbattery pack,t
=Unit_Costbattery pack,t×Battery sizet  
where, 
b is the learning coefficient 
Vt is the production volume in year t
Vo  is the production volume in year 0 (the 
base year of the study)
 ▪ The reduction in the indirect costs 
for R&D and warranty expenses are 
reflected in the falling values of indirect 
cost multipliers over time. Specifically, we 
inferred the indirect costs based on the 
V0

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
77
linear extrapolation between the short- and 
long-term indirect cost multipliers used by EPA 
(2009) (Table B1, Equation 12). 
CostDMC,t =Cost battery pack,t +Cost others   
Costretail,t =Cost DMC,t ×ICMt  
 (Equation 12)
We applied the above methods to all the vehicle 
segments without considering subsidies or taxes. 
The TCO results were triangled and adjusted based 
on existing studies (Mao et al. 2021; Lutsey 2021). 
The final TCO curves are shown in Figure B1.  
Table B1  |   Indirect Cost Multiplier for High Technology Complexity
SHORT-TERM
INDIRECT COST MULTIPLIER
LONG-TERM
INDIRECT COST MULTIPLIER
Direct manufacturing cost,  
including battery packs 1 1
Production overhead
Warranty 0.12 0.03
R&D 0.2 0.02
Others (e.g., depreciation) 0.1 0.1
Corporate overhead 0.04 0.04
Selling and dealer 0.15 0.07
ICM sum 1.45 1.27
Abbreviations: R&D = research and development; ICM = indirect cost multiplier.
Source: EPA 2009.

78
WRI.org.cn
Figure B1  |   Lifetime Total Cost of Ownership Projections for the Mainstreamed Vehicle Models of Different 
Vehicle Segments
a. Private car: compact car, 400-km range
 (parity year 2024–25)   
c. Bus: 10-meter bus, 300-km range 
 (parity year 2025–26)
b. Taxi: compact car, 400-km range
 (parity year 2021–23) 
d. Intercity coach: 500-km range
 (parity year 2029–30)  
BEV HydrogenHybrid Natural gasGasoline Diesel
Notes: The 2020 total cost of ownership (TCO) values for ICE vehicles for different segments are scaled to 100, and the rest of the TCO values are scaled accordingly.  
Abbreviations: km = kilometer; BEV = battery electric vehicle.
Source: WRI authors’ calculation.
e. Light-duty truck: 4.5-tonne truck, 280-km range
 (parity year 2024–25)  
f. HDTs: 49-tonne tractor trailer, 500-km range
 (parity year 2030–35)   
2022
2022
2022
2022
2022
2022
2020
2020
2020
2020
2020
2020
2030
2030
2030
2030
20322030 2034
20322030 2034
2024
2024
2024
2024
2024
2024
2026
2026
2026
2026
2026
2026
2028
2028
2028
2028
2028
2028
0
0
0
0
0
0
20
20
20
20
20
200
100
80
80
80
80
80
350
140
140
120
120
160
140
120
450
120
120
60
60
60
60
60
300
100
100
100
100
100
400
40
40
40
40
40
250
150
50
price indexprice indexprice index
price indexprice indexprice index

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
79
APPENDIX C.  
BIOFUEL CONSIDERATIONS
Biofuels are not considered in the 
research because their supply, cost, and 
environmental performance will restrict their 
future adoption. 
First, there are bottlenecks in biofuel 
feedstock supplies. For example, because 
of the supply shortage in crops and 
food security concerns, China’s ethanol 
production was 2.84 million tonnes in 
2019, unable to meet the demand of 13 
million tonnes if all the gasoline were to be 
10 percent blended with ethanol (QDIBBT 
2019). Second-generation biofuels xviii with 
different sources of feedstock—mainly from 
waste and plant cellulose—have similar 
challenges. By one estimate, the total waste 
in the United States (including agricultural 
residue, food waste, sewer sludge, and 
manure) would generate 22.3 gigaliters/year 
of biocrude oil and meet only 23.9 percent 
of current U.S. aviation kerosene demand 
(Skaggs et al. 2018). 
Further, in the absence of policy incentives, the 
uptake of biofuels would be unlikely to occur. 
Biofuels are more expensive than fossil fuels: The 
production cost of biofuels in China is around 
5,000–6,000 CNY per ton, about the same as 
the wholesale price of gasoline/diesel (around 
5,200–6,300 CNY).xix Strong policy supports 
would therefore be necessary to promote 
its adoption. However, a national subsidy 
to oil refineries for biofuel production 
(1,883 CNY per tonne in 2005) ended in 
2016 due to concern that the large demand 
for biofuel feedstocks would threaten food 
security. Further, China has no intention of 
imposing a quota obligation like the EU’s 
Renewable Energy Directive or the United 
States’ Renewable Fuel Standard, which 
mandate a minimum share of biofuels (or 
low-carbon fuels) sold. Last but not the least, 
the environmental performance of biofuels 
may not justify public supports. Studies 
show biodiesel (20 percent blend) increases 
hydrocarbon and carbon monoxide emissions 
by 7 percent and 10 percent, respectively 
(O’Malley and Searle 2021).

80
WRI.org.cn
ABBREVIATIONS
BEV battery electric vehicle
CCS carbon capture and storage
CH4 methane
CO carbon monoxide
CNY Chinese yuan
FCEV fuel cell electric vehicle 
GHG greenhouse gas
GWP global warming potential
HDT heavy-duty and medium-duty truck
HFC hydroﬂuorocarbon 
IAM integrated assessment model
ICE  internal combustion engine
LNG liqueﬁed natural gas
N2O nitrous oxide
NEV new energy vehicle
NG natural gas
NMHC non-methane hydrocarbons
NOx nitrogen oxides 
PM particulate matter
SMR steam methane reforming
TTW tank to wheel
WTW well to wheel 
WTT well to tank
ENDNOTES
i. NEVs include battery electric vehicles (BEVs), plug-in hybrid 
electric vehicles (PHEVs), and fuel cell electric vehicles (FCEVs).
ii. The China 6 emission standard refers to the Stage 6 Limits and 
Measurement Methods for Emissions from Light-Duty Vehicles 
(GB18352.6–2016) and the Stage VI Limits and Measurement 
Methods for Emissions from Heavy-Duty Vehicles (GB17691–2018). 
China 6 is China ’s most up-to-date vehicle exhaust emission 
standard with the air pollutant limits equating to those of Euro 6.  
iii. China’s NEV policies target passenger carriers, goods carriers, 
and special purpose vehicles; motorcycles are not included. 
iv. Other forms of TCO include the ﬁrst-owner TCO and second-
owner TCO, among others. 
v. For charging infrastructure CAPEX, we excluded the expensive 
grid upgrade investments in the calculation.  
vi. A less transport-intensive service sector could play a role in 
decoupling freight demand from GDP growth.
vii. China’s per capita freight demand was 8,000 tkm in 2020, and 
less than 22,900 tkm per capita in the United States, Australia, 
and Canada (ITF 2012).
viii. Partly because of the truck industry’s overloading and underbidding.
ix. Partly because of the truck industry’s overloading and underbidding.
x. Two to three times maximum loading capacity.
xi. The large range is due to different deﬁnitions and scopes of TCO 
in the literature, from ﬁrst-owner TCO (ﬁrst 5 to 6 years of useful 
life) to lifetime TCO (10 to 15 years of useful life). 
xii. BEVs are unable to carry high loads over long distances. FCEVs 
are expensive and fuel cell systems have limited cycle lives. 
xiii. New European Driving Cycle (NEDC) (Phases I–IV) and WLTP 
(Phase V) for passenger cars. C-WTVC for commercial vehicles. 
xiv. In 2020, SUVs and multiple purpose vehicles comprised 52 per -
cent of passenger car sales (increasing from 15 percent in 2010) 
and tractor trailers comprised 45 percent of HDT sales (increasing 
from 15 percent in 2012).   
xv. Fossil fuels include coal, natural gas, and oil products. 
xvi. In this study, we considered investments in commercial NEV ac -
quisition and operations as well as capital investments in transit, 
active mobility, and freight railway infrastructure, all of which are 
absent in other studies.
xvii. Gasoline particulate ﬁlters’ overall global warming effect was 
found to be neutral as the reduction in black carbon (classiﬁed 
as PM10) could counteract the increase in fuel consumption (CO 2 
emissions).  
xviii. Second-generation biofuels are produced from waste and plant 
cellulose (such as crop residues) compared with ﬁrst-generation 
biofuels, which were produced from crops. The advanced biofuels 
have many beneﬁts, such as a higher decarbonization potential 
and alleviation of food-security risks. 
xix. For local reﬁneries ’ wholesale prices in Shandong Province, see 
https://www.bilibili.com/read/cv12220483.

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
81
REFERENCES
Abramczyk, M., M. Campbell, A. Chitkara, M. Diawara, A. Lerch, and J. 
Newcomb. 2017 . Positive Disruption: Limiting Global Temperature Rise 
to Well below 2 Degrees. 
ACEA (European Automobile Manufacturers’ Association). 2021. Mak -
ing the Transition to Zero Emission Mobility. Progress Report. Brussels: 
ACEA.
ACEA. 2022. “ACEA Proposals for Euro 7 and Euro VII Emission Stan -
dards.” https://www.acea.auto/publication/acea-proposals-for-euro-
7-and-euro-vii-emission-standards/.
Agenbroad, J., J. Creyts, D. Mullaney, J. Song, and Z. Wang. 2016. Im -
proving Efficiency in Chinese Trucking and Logistics: Proceeding and 
Insights from the Design Charrette on Chinese Logistics and Trucking 
Efficiency Held April 26–27, 2016, in Shenzhen, PRC. Rocky Mountain 
Institute. 
Agora Energiewende. 2020a. Towards a Climate-Neutral Germany. 
Three Steps for Achieving Climate Neutrality by 2050 and an Inter -
mediate Target of -65% in 2030 as Part of the EU Green Deal. Berlin: 
Agora Energiewende.
Agora Energiewende. 2020b. The European Power Sector in 2020: 
Up-to-Date Analysis on the Electricity Transition. Berlin: Agora Ener -
giewende.
ANL (Argonne National Laboratory). 2014. “Greenhouse Gases, Regu-
lated Emissions, and Energy Use in Transportation (GREET) Model.” 
Lemont, IL: Argonne National Laboratory. 
ANL (Argonne National Laboratory). 2018. China Vehicle Fleet Model: 
Estimation of Vehicle Stocks, Usage, Emissions, and Energy Use—
Model Description, Technical Documentation, and User Guide. Lemont, 
IL: Argonne National Laboratory.
ATRI (American Transportation Research Institute). 2020. An Analysis 
of the Operational Costs of Trucking: 2020 Update. Arlington, VA: 
American Transportation Research Institute.
Autoinfo. 2021. “China Natural Gas Heavy-Duty Vehicle Market Analy -
sis.” In Chinese. https://www.autoinfo.org.cn/autoinfo_cn/content/
news/20210508/3033391.html. 
BCG (Boston Consulting Group). 2020. Climate Plan for China. Boston: 
Boston Consulting Group.
BloombergNEF. 2021. Electric Vehicle Outlook 2021. New York: Bloom -
bergNEF.
BTS (Bureau of Transportation Statistics, United States). 2021a. 
National Transportation Statistics 2021. Washington, DC: Bureau of 
Transportation Statistics.
BTS. 2021b. Hybrid-Electric, Plug-In Hybrid-Electric and Electric Vehicle 
Sales. Washington, DC: Bureau of Transportation Statistics.
BTS and FHWA (Federal Highway Administration, United States). 
2016. The 4 th Generation Freight Analysis Framework (FAF4) for Freight 
Volume Forecast for 2020 through 2045. Washington, DC: Bureau of 
Transportation Statistics and Federal Highway Administration.
CAAM (China Association of Automobile Manufacturers). 2012. 2011 
Progress Report on China’s Automobile Industry. Beijing: China As-
sociation of Automobile Manufacturers.
CAAM. 2013. 2012 Progress Report on China’s Automobile Industry.  
Beijing: China Association of Automobile Manufacturers.
CAAM. 2014. 2013 Progress Report on China’s Automobile Industry.  
Beijing: China Association of Automobile Manufacturers.
CAAM. 2015. 2014 Progress Report on China’s Automobile Industry.  
Beijing: China Association of Automobile Manufacturers.
CAAM. 2016. 2015 Progress Report on China’s Automobile Industry.  
Beijing: China Association of Automobile Manufacturers.
CAAM. 2017 . 2016 Progress Report on China’s Automobile Industry.  
Beijing: China Association of Automobile Manufacturers.
CAAM. 2018. 2017 Progress Report on China’s Automobile Industry.  
Beijing: China Association of Automobile Manufacturers.
CAAM. 2019. 2018 Progress Report on China’s Automobile Industry.  
Beijing: China Association of Automobile Manufacturers.
CAAM. 2020. 2019 Progress Report on China’s Automobile Industry.  
Beijing: China Association of Automobile Manufacturers.
CAAM. 2021a. 2020 Progress Report on China’s Automobile Industry.  
Beijing: China Association of Automobile Manufacturers.
CAAM. 2021b. Monthly Report on Automobile Industry Operation—No -
vember of 2021. Beijing: China Association of Automobile Manufactur -
ers.
CAAM. 2022. 2021 Progress Report on China’s Automobile Industry.  
Beijing: China Association of Automobile Manufacturers.
CAM (China Association of Metros). 2017 . China Urban Rail Transit An -
nual Statistics and Analysis 2017. Beijing: China Association of Metros.
CAM. 2018. China Urban Rail Transit Annual Statistics and Analysis 
2018. Beijing: China Association of Metros.
CAM. 2019. China Urban Rail Transit Annual Statistics and Analysis 
2019. Beijing: China Association of Metros.
CAM. 2020. China Urban Rail Transit Annual Statistics and Analysis 
2020.  Beijing: China Association of Metros.
CARB (California Air Resources Board). 2020. Advanced Clean Trucks 
Regulation. Sacramento, CA: CARB.
CATARC (China Automotive Technology and Research Center). 2016. 
Annual Report on Energy-Saving and New Energy Vehicles in China 
2016. Tianjin, China: China Automotive Technology and Research 
Center.
CATARC. 2018. Annual Report on Energy-Saving and New Energy 
Vehicles in China 2018. Tianjin, China: China Automotive Technology 
and Research Center.
CATARC. 2021. Annual Report on Energy-Saving and New Energy 
Vehicles in China 2021. Tianjin, China: China Automotive Technology 
and Research Center.
CEC (China Electricity Council). 2020. China 2020 Electricity and 
Industry Operation Bulletin. Beijing: CEC.

82
WRI.org.cn
CHA (China Hydrogen Alliance). 2019. White Paper on China Hydro -
gen Energy Carrier and Fuel Cell Stack Industry 2019. Beijing: China 
Hydrogen Alliance. 
China EV 100 and NRDC (Natural Resources Defense Council). 2019. 
How to Enable the Healthy Development of the Electric Vehicle Charg -
ing Market in China?  
China SAE (China Society of Automotive Engineers). 2020. Technol-
ogy Roadmap for Energy-Saving and New Energy Vehicles 2.0 (The 
Roadmap). Beijing: China Machine Press. 
China Transport News. 2021. “Shenzhen Prioritizes Green Transport and 
Revitalize the City.” https://www.mot.gov.cn/jiaotongyaowen/202112/
t20211207_3630018.html. 
Clairotte, M., R. Suarez-Bertoa, A.A. Zardini, B. Giechaskiel, J. Pavlovic, 
V. Valverde, B. Ciuffo, et al. 2020. “Exhaust Emission Factors of Green -
house Gases (GHGs) from European Road Vehicles.” Environ Sci Eur 32 
(125). https://doi.org/10.1186/s12302-020-00407-5.
Climate Watch. 2020. (Database.) “Global Historical GHG Emissions-
CAIT.”  Washington, DC: World Resources Institute. https://www.
climatewatchdata.org.
CSI (China Standardization Institute). 2018. China Hydrogen Industry 
Infrastructure Development Bluebook (2016). Beijing: China Quality 
and Standard Publishing. 
DOE (United States Department of Energy). 2020. Hydrogen Strategy: 
Enabling a Low-Carbon Economy. Washington, DC: DOE.
DOT (United Kingdom Department of Transport). 2021. Consultation on 
When to Phase Out the Sale of New, Non-zero Emission Heavy Goods 
Vehicles. London: United Kingdom Department of Transport.
Edelenbosch, O.Y., D.P. van Vuuren, C. Bertram, S. Carrara, J. Emmer -
ling, H. Daly, A. Kitous, et al. 2017 . “Transport Fuel Demand Responses 
to Fuel Price and Income Projections: Comparison of Integrated 
Assessment Models.” Transportation Research Part D—Transport and 
Environment 55: 310–21.
EEA (European Environment Agency). 2020. “EEA Greenhouse Gases—
Data Viewer.” Copenhagen: EEA.
Enoch, M. 2018. Mobility as a Service (MaaS) in the UK: Change and Its 
Implications. Loughborough, United Kingdom: School of Architecture, 
Building and Civil Engineering, Loughborough University.
EPA (United States Environmental Protection Agency). 2009. Auto -
mobile Industry Retail Price Equivalent and Indirect Cost Multipliers.  
Washington, DC: EPA.
EPA. 2015. Transitioning to Low-GWP Alternatives in Passenger Vehicle 
Air Conditioners. Washington, DC: EPA.
EPA. 2020. “Greenhouse Gas Inventory Data Explorer.” Washington, DC: 
EPA. https://cfpub.epa.gov/ghgdata/inventoryexplorer/.
ERTICO (ERTICO – ITS Europe, Editor). 2019. Mobility as a Service 
(MaaS) and Sustainable Urban Mobility Planning.
EU P&C (European Union Parliament and Council). 2019. Regulation 
(Eu) 2019/631 of the European Parliament and of the Council. Setting 
CO2 Emission Performance Standards for New Passenger Cars and for 
New Light Commercial Vehicles, and Repealing Regulations (EC) No 
443/2009 and (EU) No 510/2011.
Eurostat. 2021a. “Stock of Vehicles by Category and NUTS 2 Regions.” 
Luxembourg City: Eurostat.
Eurostat. 2021b. “Freight Transported in Containers — Statistics on 
Unitisation.” Luxembourg City: Eurostat.
Eurostat. 2021c. “Annual Road Freight Transport by Load Capacity of 
Vehicle.” Luxembourg City: Eurostat.
Eurostat. 2021d. “Road Freight Transport Statistics.” Luxembourg City: 
Eurostat.
Eurostat. 2021e. “Lorries and Lorries (Excluding Light Goods Road 
Vehicles).” Luxembourg City: Eurostat.
Feng, J., Y. Zhang, S. Li, J. Mao, A.P. Patton, Y. Zhou, W. Ma, et al. 2019. 
“The Influence of Spatiality on Shipping Emissions, Air Quality and 
Potential Human Exposure in the Yangtze River Delta/Shanghai, 
China.” Atmos. Chem. Phys. 19 (9): 6167–83. https://doi.org/10.5194/
acp-19-6167-2019.
FHWA (Federal Highway Administration, United States). 2021. “High -
way Statistics 2019—Annual Vehicle Distance Traveled in Miles and 
Related Data by Highway Category and Vehicle Type.” Washington, 
DC: FHWA.
Fransen, T., B. Welle, C. Gorguinpour, M. McCall, R. Song, and A. Tankou. 
2019. “Enhancing NDCs: Opportunities in Transport.” Working Paper. 
Washington, DC: World Resources Institute.
Frey, K., J. Hartwig, and C. Doll. 2014. “Accelerating a Shift from Road 
to Rail Freight Transport in Germany: Three Scenarios.” Transport 
Research Arena 2014, Paris.
Fu, Z.H., et al. 2019. Strategy Research on Transportation Power. Bei-
jing: China Communications Press. Co. Ltd.  
Gao, Z.M., T.J. LaClair, D.E. Smith, and C. Stuart Daw. 2015. “Exploring 
Fuel-Saving Potential of Long-Haul Truck Hybridization.” Transporta -
tion Research Record 2502 (2502): doi:10.3141/2502-12.
Gao, Z., T. Laclair, S. Ou, S. Huff, G. Wu, P. Hao, K. Boriboonsomsin, et 
al. 2019. “Evaluation of Electric Vehicle Component Performance over 
Eco-driving Cycles.” Energy 172: 823–39. https://doi.org/10.1016/j.
energy.2019.02.017 .
Gilbert, C. 2017 . Global Passenger Car Penetration: Grid Lock! Legal & 
General Investment Management Limited. 
Gnann, T., P. Plötz, A. Kühn, and M. Wietschel. 2017 . How to Decarbon -
ize Heavy Road Transport? ECEEE 2017 Summer Study—Consumption, 
Efficiency & Limits.
Goldman Sachs. 2021. Carbonomics—China Net Zero: The Clean Tech 
Revolution. New York: Goldman Sachs.
Gota, S., C. Huizenga, K. Peet, N. Medimorec, and S. Bakker. 2018. 
“Decarbonising Transport to Achieve Paris Agreement Targets.” Energy  
Efficiency 12: 363–86. https://doi.org/10/gfpm72.
Gustafsson, M., N. Svensson, M. Eklund, J. Dahl Öberg, and A. Vehabo -
vic. 2021. “Well-to-Wheel Greenhouse Gas Emissions of Heavy-Duty 
Transports: Influence of Electricity Carbon Intensity.” Transportation 
Research Part D: Transport and Environment 93: 102757 . ISSN 1361-
9209. https://doi.org/10.1016/j.trd.2021.102757 .

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
83
Hao, H., Y. Geng, W.Q. Li, and B. Guo. 2015. “Energy Consumption and 
GHG Emissions from China’s Freight Transport Sector: Scenarios 
through 2050.” Energy Policy 85: 94–101. ISSN 0301-4215. https://doi.
org/10.1016/j.enpol.2015.05.016.
Heaps, C.G. 2022. LEAP: The Low Emissions Analysis Platform. 
[Software version: 2020.1.56]. Somerville, MA: Stockholm Environment 
Institute. https://leap.sei.org.
HPK. 2019. “Efficiency and CO 2 Emission Analysis of Internal Combus-
tion Engines (ICE) and Electric Vehicles (EV) on WTT and TTW Emis-
sions.” Future #SmartMobility Needs Sustainable #CleanEnergy Blog. 
https://kleebinder.net/en/tag/lifecycle-assessment/.
Hu, T., X.Q. Mao, X.D. Lu, and P. Gerilla-Teknomo. 2020. Air Pollutants 
and Greenhouse Gas Emissions Co-control Evaluation in the People’s 
Republic of China. ADB East-Asia Working Paper Series. Manila: Asian 
Development Bank. 
Huo, H., M. Wang, X.L. Zhang, K. He, H. Gong, K. Jiang, Y. Jing, et al. 
2012a. “Projection of Energy Use and Greenhouse Gas Emissions by 
Motor Vehicles in China: Policy Options and Impacts.” Energy Policy 43 
(C): 37–48.
Huo, H., Q. Zhang, K.B. He, Z.Z. Yao, and M. Wang. 2012b. “Vehicle-Use 
Intensity in China: Current Status and Future Trend.” Energy Policy 43 
(C): 6–16.
ICCSD (Institute of Climate Change and Sustainable Development of 
Tsinghua University). 2020. China’s Long-Term Low-Carbon Develop -
ment Strategies and Pathways: Comprehensive Report. Beijing: China 
Environment Press.
ICCT (International Council on Clean Transportation). 2017 . China’s 
Stage 6 Emission Standard for New Light-Duty Vehicles (Final Rule).  
ICCT 2017 Policy Update. Beijing: ICCT.
ICCT. 2019. “Comments on China’s Proposed 2021–2025 Fuel Consump -
tion Limits, Evaluation Methods, and Targets for Passenger Cars.” 
Beijing: ICCT.
iCET (Innovation Center for Energy and Transportation). 2017 . Annual 
Report on the Differences between Real-World Fuel Consumption and 
Certified Fuel Consumption for Passenger Cars. Beijing: iCET.
iCET. 2021. Report on China’s Commercial Vehicle Electrification Poten -
tials. Beijing: iCET.
IEA (International Energy Agency). 2021a. World Energy Outlook 2021. 
Paris: IEA.
IEA. 2021b. An Energy Sector Roadmap to Carbon Neutrality in China. 
Paris: IEA.
IPCC (Intergovernmental Panel on Climate Change). 2006. Guidelines 
for National Greenhouse Gas Inventories. Geneva: IPCC.
IPCC. 2014. Climate Change 2014: Synthesis Report. Contribution of 
Working Groups I, II, and III to the Fifth Assessment Report of the 
Intergovernmental Panel on Climate Change. [Core Writing Team: R.K. 
Pachauri and L.A. Meyer (Eds.)]. Geneva: IPCC. 
IRENA (International Renewable Energy Agency). 2020. Green Hydro -
gen Cost Reduction: Scaling Up Electrolysers to Meet the 1.5°C Climate 
Goal. Abu Dhabi: IRENA.
ITF (International Transport Forum). 2012. (Database.) OECD. Stat.  
Paris: ITF. http://stats.oecd.org/index.aspx.
ITF. 2013. Railway Efficiency: An Overview and a Look at Opportunities 
for Improvement. ITF Discussion Paper No. 201312. Paris: ITF. https://
www.itf-oecd.org/sites/default/files/docs/dp201312.pdf. 
ITF. 2019. ITF Transport Outlook 2019. Paris: ITF.
MLITT (Ministry of Land Infrastructure Transport and Tourism, Japan). 
2021. 統計情報. https://www.mlit.go.jp/statistics/details/jido -
sha_list.html.
Jiang, X.Q., W.Y. Xi, W.K. Fong, J.Y. Song, and Z. Wang. 2019. Wuhan 
Transport Sector Carbon Emissions Roadmap Study. Washington, DC: 
World Resources Institute. 
Kaak, L.H., P. Vaishanav, M.G. Morgan, I. Azevedo, and S. Rai. 2018. 
“Decarbonizing Intraregional Freight Systems with a Focus on Modal 
Shift.” Environmental Research Letters 13 (8). 
Kong, H., X.H. Zhang, and J.H. Zhao. 2020. “How Does Ridesourcing 
Substitute for Public Transit? A Geospatial Perspective in Chengdu, 
China.” Journal of Transport Geography 86: 102769. ISSN 0966-6923. 
https://doi.org/10.1016/j.jtrangeo.2020.102769.
Lai, J. n.d. “Bus Rationalization in Hong Kong.” Presentation. Metropo -
lis. https://www.metropolis.org/sites/default/files/hong-kong_bus-
rationalization.pdf.
LBNL (Lawrence Berkeley National Laboratory). 2021. Assessment of 
Energy Strategies for China’s Heavy-Duty Trucks and the Potential for 
Electrification. Berkeley, CA: Lawrence Berkeley National Laboratory.
Ledna, C., M. Muratori, A. Yip, P. Jadun, and C. Hoehne. 2022. “Decar -
bonizing Medium- and Heavy-Duty On-Road Vehicles: Zero Emission 
Vehicles Cost Analysis.” Presentation. Golden, CO: National Renewable 
Energy Laboratory.
Le Quéré, C., R.B. Jackson, M.W. Jones, A.J.P. Smith, S. Abernethy, R.M. 
Andrew, A.J. De-Gol, et al. 2020. “Temporary Reduction in Daily Global 
CO2 Emissions during the COVID-19 Forced Confinement.” Nat. Clim. 
Chang. 10: 647–53. https://doi.org/10.1038/s41558-020-0797-x.
Liang, B., Y. Ge, J. Tan, X. Han, L. Gao, L. Hao, W. Ye, and P. Dai. 2012. 
“Comparison of PM Emissions from a Gasoline Direct Injected (GDI) 
Vehicle and a Port Fuel Injected (PFI) Vehicle Measured by Electri-
cal Low Pressure Impactor (ELPI) with Two Fuels: Gasoline and M15 
Methanol Gasoline.” Journal of Aerosol Science 57: 22–31.
Liimatainen, H., O. Vliet, and D. Aplyn. 2019. “The Potential of Electric 
Trucks—An International Commodity-Level Analysis.” Applied Energy  
236: 804–14. 
Liu, F.Q., D.L. Mauzerall, F. Zhao, and H. Hao. 2021. “Deployment of Fuel 
Cell Vehicles in China: Greenhouse Gas Emission Reductions from 
Converting the Heavy-Duty Truck Fleet from Diesel and Natural Gas to 
Hydrogen.” International Journal of Hydrogen Energy 46 (34): 17982–97 . 
https://doi.org/10.1016/j.ijhydene.2021.02.198.
Liu, H.H. 2018. “China Railway Beijing Group’s Reflections on Price 
Signals to Facilitate Freight Mode Shift from Roadways to Railways.” 
Railway Economic Research 05: 5–10.
Liu, J.L., Y.H. Sun, K. Wang, J. Zou, and Y. Kong. 2018. “Study on Mid- and 
Long-Term Low Carbon Development Pathway for China’s Transport 
Sector.” Climate Change Research 14 (5): 513–21.

84
WRI.org.cn
Liu, J.L., M. Yin, Q. Xia-Hou, K. Wang, and J. Zou. 2021. “Comparison of 
Sectoral Low-Carbon Transition Pathways in China under the Nation -
ally Determined Contribution and 2 °C Targets.” Renewable and Sus-
tainable Energy Reviews 149. ISSN 1364-0321. https://doi.org/10.1016/j.
rser.2021.111336.
LTA (Singapore Land Transport Authority Singapore). 2021. “Annual 
Vehicle Statistics 2021 (Motor Vehicle Population by Vehicle Type).” 
Lutsey, N., H.Y. Cui, and R.J. Yu. 2021. Evaluating Electric Vehicle Costs 
and Benefits in China in the 2020–2035 Time Frame. White Paper. 
Beijing: International Council on Clean Transportation.
Mamakos, A. 2011. Feasibility of Introducing Particulate Filters on 
Gasoline Direct Injection Vehicles: A Cost Benefit Analysis. JRC 
Scientific and Policy Reports. Luxembourg: Publications Office of the 
European Union.
Mao, S., H. Basma, P.–L. Ragon, Y. Zhou, and F. Rodríguez. 2021. Total 
Cost of Ownership for Heavy Trucks in China: Battery Electric, Fuel Cell 
Electric and Diesel Trucks. White Paper. Beijing: International Council 
on Clean Transportation.
Mareev, I., J. Becker, and D. Sauer. 2018. “Battery Dimensioning and Life 
Cycle Costs Analysis for a Heavy-Duty Truck Considering the Require -
ments of Long-Haul Transportation.” Energies 11 (1): 55.
McKinnon, A. 2010. European Freight Transport Statistics: Limitations, 
Misinterpretations, and Aspirations. Report prepared for the 15th 
European Automobile Manufacturers’ Association Scientific Advisory 
Group Meeting. Brussels, September 8.
MEE (Ministry of Ecology and Environment, China). 2011. China Vehicle 
Environmental Management Annual Report 2011. Beijing: China Minis-
try of Ecology and Environment.
MEE. 2012. China Vehicle Environmental Management Annual Report 
2012.  Beijing: China Ministry of Ecology and Environment.
MEE. 2013. China Vehicle Environmental Management Annual Report 
2013.  Beijing: China Ministry of Ecology and Environment.
MEE. 2014a. China Vehicle Environmental Management Annual Report 
2014. Beijing: China Ministry of Ecology and Environment.
MEE. 2014b. China’s National Guide on Road Transport Air Pollutant 
Inventory Development (Test Version). Beijing: China Ministry of Ecol-
ogy and Environment.
MEE. 2015. China Vehicle Environmental Management Annual Report 
2015.  Beijing: China Ministry of Ecology and Environment.
MEE. 2016. China Vehicle Environmental Management Annual Report 
2016. Beijing: China Ministry of Ecology and Environment.
MEE. 2017 . China Vehicle Environmental Management Annual Report 
2017. Beijing: China Ministry of Ecology and Environment.
MEE. 2018a. China’s Second Biennial Update Report on Climate 
Change. Beijing: China Ministry of Ecology and Environment.
MEE. 2018b. The People’s Republic of China Third National Commu-
nication on Climate Change. Beijing: China Ministry of Ecology and 
Environment.
MEE. 2018c. China Vehicle Environmental Management Annual Report 
2018. Beijing: China Ministry of Ecology and Environment.
MEE. 2018d. “The State Council Rolls Out a Three-Year Action Plan 
for Clean Air.” https://english.mee.gov.cn/News_service/news_re -
lease/201807/t20180713_446624.shtml. 
MEE. 2019. China Vehicle Environmental Management Annual Report 
2019. Beijing: China Ministry of Ecology and Environment.
MEE. 2020a. China Vehicle Environmental Management Annual Report 
2020.  Beijing: China Ministry of Ecology and Environment.
MEE. 2020b. Bulletin on the Second National Census of Pollution 
Source. Beijing: China Ministry of Ecology and Environment.
MEE. 2021. China Vehicle Environmental Management Annual Report 
2021. Beijing: China Ministry of Ecology and Environment.
MIIT (Ministry of Industry and Information Technology, China). 2019. 
Fuel Consumption Evaluation Methods and Targets for Passenger Cars 
(GB 27999-2019). Beijing: China Ministry of Industry and Information 
Technology.   
MIIT. 2021. Fuel Consumption Limits for Passenger Cars (GB19578-
2021). Beijing: China Ministry of Industry and Information Technology.   
MOT (Ministry of Transport of China). 2015. The 13 th Five-Year Plan on 
Comprehensive Transport Development. Beijing: Ministry of Transport 
of China.
MOT. 2016. China Annual Transport Statistical Bulletin 2016. Beijing: 
Ministry of Transport of China.
MOT. 2017a. Regularity of the Enforcement on Vehicle Overloading. 
Beijing: Ministry of Transport of China.
MOT. 2017b. Guideline on Management of Illegal Adaptations to Ve -
hicles and Vehicle Overloading. Beijing: Ministry of Transport of China.
MOT. 2019. Interim Measures for the Operation and Administration of 
Road Freight Transport Based on Internet Platforms. Beijing: Ministry 
of Transport of China.
Mottschall, M., P. Kasten, and F. Rodriguez. 2020. Decarbonization of 
On-Road Freight Transport and the Role of LNG from a German Per -
spective.  Beijing: International Council on Clean Transportation.
MPS (Ministry of Public Security, China). 2019. “Road Traffic Manage -
ment—Types of Motor Vehicles (GA802–2019).” China Public Security 
Sectoral Standard. Beijing: Ministry of Public Security.
Mulholland, E., J. Teter, P. Cazzola, Z. McDonald, and B.P. Ó Gallachóir. 
2018. “The Long Haul towards Decarbonising Road Freight—A Global 
Assessment to 2050.” Applied Energy 216 (C): 678–93.
NBS (National Bureau of Statistics of China). 2002. China Statistical 
Yearbook 2002 . Beijing: National Bureau of Statistics of China.
NBS. 2003. China Statistical Yearbook 2003. Beijing: National Bureau 
of Statistics of China.
NBS. 2004. China Statistical Yearbook 2004. Beijing: National Bureau 
of Statistics of China.
NBS. 2005. China Statistical Yearbook 2005. Beijing: National Bureau 
of Statistics of China.
NBS. 2006. China Statistical Yearbook 2006. Beijing: National Bureau 
of Statistics of China.
NBS. 2007 . China Statistical Yearbook 2007. Beijing: National Bureau of 
Statistics of China.

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
85
NBS. 2008. China Statistical Yearbook 2008. Beijing: National Bureau 
of Statistics of China.
NBS. 2009. China Statistical Yearbook 2009. Beijing: National Bureau 
of Statistics of China.
NBS. 2010. China Statistical Yearbook 2010. Beijing: National Bureau of 
Statistics of China.
NBS. 2011. China Statistical Yearbook 2011. Beijing: National Bureau of 
Statistics of China.
NBS. 2012. China Statistical Yearbook 2012. Beijing: National Bureau of 
Statistics of China.
NBS. 2013. China Statistical Yearbook 2013. Beijing: National Bureau of 
Statistics of China.
NBS. 2014. China Statistical Yearbook 2014. Beijing: National Bureau of 
Statistics of China.
NBS. 2015. China Statistical Yearbook 2015. Beijing: National Bureau of 
Statistics of China.
NBS. 2016. China Statistical Yearbook 2016. Beijing: National Bureau of 
Statistics of China.
NBS. 2017 . China Statistical Yearbook 2017. Beijing: National Bureau of 
Statistics of China.
NBS. 2018. China Statistical Yearbook 2018. Beijing: National Bureau of 
Statistics of China.
NBS. 2019. China Statistical Yearbook 2019. Beijing: National Bureau of 
Statistics of China.
NBS. 2020. China Statistical Yearbook 2020. Beijing: National Bureau 
of Statistics of China.
NBS. 2021. China Statistical Yearbook 2021. Beijing: National Bureau of 
Statistics of China.
NCI and CA (New Climate Institute and Climate Analytics). 2020. 
Climate Action Tracker: Paris Agreement Compatible Sectoral Bench -
marks. Methods Report on Elaborating the Decarbonisation Roadmap.
NDRC (National Development and Reform Commission, China). 2004. 
The People’s Republic of China Initial National Communication on 
Climate Change. Beijing: China National Development and Reform 
Commission.
NDRC. 2012. The People’s Republic of China Second National Com -
munication on Climate Change. Beijing: China National Development 
and Reform Commission.
NDRC. 2016. China’s First Biennial Update Report on Climate Change. 
Beijing: China National Development and Reform Commission.
NDRC. 2021. Action Plan for Carbon Dioxide Peaking before 2030. Bei-
jing: China National Development and Reform Commission. https://
en.ndrc.gov.cn/policies/202110/t20211027_1301020.html.
Ntziachristos, L., D. Gkatzoflias, C. Kouridis, and Z. Samaras. 2009. 
“COPERT: A European Road Transport Emission Inventory Model.” In 
I.N. Athanasiadis, A.E. Rizzoli, P.A. Mitkas, J.M. Gómez (Eds.). Infor -
mation Technologies in Environmental Engineering. Environmental 
Science and Engineering. Berlin, Heidelberg: Springer.
O’Driscoll, R., M. Stettler, N. Molden, T. Oxley, and H.M. ApSimon. 2018. 
“Real World CO 2 and NOx Emissions from 149 Euro 5 and 6 Diesel, 
Gasoline and Hybrid Passenger Cars.” Science of the Total Environ -
ment 621: 282–90.
OECD (Organisation for Economic Co-operation and Development). 
n.d. “Freight Transport (Indicator).” Paris: OECD. doi: 10.1787/708eda32-
en. Accessed April 20, 2022.
OECD. 2018. Total Inland Transport Infrastructure Investment per GDP . 
Paris: OECD.
O'Malley, J., and S. Searle. 2021. Air Quality Impacts of Biodiesel in the 
U.S. White Paper. Beijing: International Council on Clean Transporta -
tion.
Pan, D., L. Tao, K. Sun, L.M. Golston, D.J. Miller, T. Zhu, Y. Qin, et al. 2020. 
“Methane Emissions from Natural Gas Vehicles in China.” Nature Com -
munication 11 (4588). https://doi.org/10.1038/s41467-020-18141-0.
Pan, X., H.L. Wang, L.N. Wang, and W. Chen. 2018. “Decarbonization of 
China’s Transportation Sector: In Light of National Mitigation toward 
the Paris Agreement Goals.” Energy 155: 853–64. ISSN 0360-5442. 
https://doi.org/10.1016/j.energy.2018.04.144.
Peng, L.Q., F.Q. Liu, M. Zhou, M. Li, Q. Zhang, and D.L. Mauzerall. 2021. 
“Alternative-Energy-Vehicles Deployment Delivers Climate, Air Quality, 
and Health Co-benefits when Coupled with Decarbonizing Power 
Generation in China.” One Earth 4: 1127–40.
Phadke, A., A. Khandekar, N. Abhyankar, D. Wooley, and D. Rajagopal. 
2021. “Why Regional and Long-Haul Trucks Are Primed for Electrifica -
tion Now.” Berkeley, CA: Lawrence Berkeley National Laboratory.
QDIBBT (Qindao Institute of BioEnergy and Bioprocess Technology, 
China Academy of Sciences). 2019. “Not Living Up to Expectations: 
China Has Ethanol Supply Gaps.” http://www.qibebt.cas.cn/xwzx/
kydt/201903/t20190316_5257518.html.
Qiu, S.Y., L.L. Xue, J. Cai, J.Q. Chen, L.Y. Song, and Z. Wu. 2020. “Zero-
Emission Logistic Vehicles Promotion Challenges and Experiences: 
Beijing Case Study.” Working Paper. Beijing: WRI China. 
Riahi, K., F. Dentener, D. Gielen, A. Grubler, J. Jewell, Z. Klimont, V. 
Krey, et al. 2012. “Energy Pathways for Sustainable Development.” In 
Global Energy Assessment: Toward a Sustainable Future, edited by T.B. 
Johansson, N. Nakicenovic, A. Patwardhan, and L. Gomez-Echeverri. 
Cambridge: Cambridge University Press.
RIOH and Sinoiov (Research Institute of Highway of China and 
Sinoiov). 2021. Big Data Based China Road Freight Industry Operation 
Analysis Report (2020). Beijing: Research Institute of Highway of 
China and Sinoiov.
Saliba, G., R. Saleh, Y. Zhao, A.A. Presto, A.T. Lambe, B. Frodin, S. Sardar, 
et al. 2017 . “Comparison of Gasoline Direct-Injection (GDI) and Port 
Fuel Injection (PFI) Vehicle Emissions: Emission Certification Stan -
dards, Cold-Start, Secondary Organic Aerosol Formation Potential, 
and Potential Climate Impacts.” Environment Science Technology 51 
(11): 6542–52.
Schaller, B. 2021. “Can Sharing a Ride Make for Less Traffic? Evidence 
from Uber and Lyft and Implications for Cities.” Transport Policy 102: 
1–10. ISSN 0967-070X. https://doi.org/10.1016/j.tranpol.2020.12.015.

86
WRI.org.cn
Schroten, A., G. Warringa, and M. Bles. 2012. Marginal Abatement Cost 
Curves for Heavy Duty Vehicles. Background Report. Delft, Nether -
lands: CE Delft.
SFC (Smart Freight Center). n.d. Smart Freight Forum: China Modal 
Shift from Truck to Rail Summary Report.
Shao, Y.Z. 2020. “Environmental Impacts of Modal Shift to Rail in 
Tangshan.” Working Paper. Beijing: International Council on Clean 
Transportation.
Shao, Y.Z. 2021. The Updated China IV Non-road Emission Standards. 
Policy Update. Beijing: International Council on Clean Transporta -
tion. https://theicct.org/publications/china-iv-non-road-emission-
standards-jul2021. 
Skaggs, R.L., A.M. Coleman, T.E. Seiple, and A.R. Milbrandt. 2018. 
“Waste-to-Energy Biofuel Production Potential for Selected Feed-
stocks in the Conterminous United States.” Renewable and Sustain -
able Energy Reviews 82 (3): 2640–51. ISSN 1364-0321. https://doi.
org/10.1016/j.rser.2017 .09.107 .
Song, S. 2017 . The Transport Emissions & Social Cost Assessment.  
Washington, DC: World Resources Institute. 
Spielmann, M., M. Faltenbacher, A. Stoffregen, and D. Eichhorn. 2010. 
Comparison of Energy Demand and Emissions from Road, Rail and 
Waterway Transport in Long-Distance Freight Transport. Leinfelden-
Echterdingen, Germany: PE International.  
State Council (State Council, the People’s Republic of China). 2020. 
NEV Industrial Development Plan 2021–35. Beijing: State Council.
State Council. 2021a. Guideline on Further Prevention and Control of 
Pollution (2021–25). Beijing: State Council. 
State Council. 2021b. National Comprehensive Three-Dimensional 
Transportation Network (2021–35). Beijing: State Council.
T&E (Transport & Environment). 2020a. Compressed Natural Gas 
Vehicles Are Not a Clean Solution for Transport: Review of the Latest 
Evidence Shows High Levels of Particle Emissions. Brussels: Transport 
& Environment. https://www.transportenvironment.org/wp-content/
uploads/2021/07/2020_06_TE_CNG_particle_report.pdf.
T&E. 2020b. How to Decarbonize the UK’s Freight Sector by 2050. 
Brussels: Transport & Environment.  
Teske, S., S. Niklas, and R. Langdon. 2021. TUMI Transport Outlook 1.5°C: 
A Global Scenario to Decarbonize Transport. Bonn, Germany: Transfor -
mative Urban Mobility Initiative.
UK DfT (Department for Transport, United Kingdom). 2021. Decarbon -
izing Transport: A Better, Greener Britain. London: Department for 
Transport. 
Wang, H.L., X.M. Ou, and X.L. Zhang. 2017 . “Mode, Technology, Energy 
Consumption, and Resulting CO 2 Emissions in China’s Transport Sec -
tor up to 2050.” Energy Policy 109: 719–33. ISSN 0301-4215. https://doi.
org/10.1016/j.enpol.2017 .07 .010.
Wang, H., J.Y. Han, M. Su, S.L. Wan, and Z.C. Zhang. 2021. “The Relation -
ship between Freight Transport and Economic Development: A Case 
Study of China.” Research in Transportation Economics 85: 100885. 
ISSN 0739-8859. https://doi.org/10.1016/j.retrec.2020.100885.
Wang, Z.P., Z.W. Yao, et al. 2021. Annual Report on the Big Data of New 
Energy Vehicles in China (2021). Beijing: China Machine Press. 
Wappelhorst, S. 2021. “Update on Government Targets for Phasing Out 
New Sales of Internal Combustion Engine Passenger Cars.” Briefing. 
Beijing: International Council on Clean Transportation.
Wappelhorst, S., U. Tietge, G. Bieker, and P. Mock. 2021. “Europe’s CO 2 
Emission Performance Standards for New Passenger Cars: Lessons 
from 2020 and Future Prospects.” Working Paper. Beijing: Interna -
tional Council on Clean Transportation.
Wei, H.Y., H. Zhou, Y. Yan, et al. 2020. “The Development of Diesel Fu-
eled Heavy-Duty Vehicle Emission Standards in China.” Small Internal 
Combustion Engine and Vehicle Technique 49 (06):79–87 .
WHO (World Health Organization). 2021. WHO Global Air Quality Guide -
lines: Particulate Matter (PM2.5 and PM10), Ozone, Nitrogen Dioxide, 
Sulfur Dioxide and Carbon Monoxide. Geneva: WHO. https://apps.who.
int/iris/handle/10665/345329. License: CC BY-NC-SA 3.0 IGO.
World Bank. 2021. Electrification of Public Transport: A Case Study 
of the Shenzhen Bus Group. Mobility and Transport Connectivity. 
Washington, DC: World Bank. https://openknowledge.worldbank.org/
handle/10986/35935 License: CC BY 3.0 IGO.
Xinhua News. 2020. “China E-scooters’ Stock Approaching 300 Million.” 
http://www.gov.cn/xinwen/2020-11/20/content_5562997 .htm.
Xinhua News. 2021. “Beijing City Center’s Green Transport Mode Share 
over 73%.” http://www.gov.cn/xinwen/2020-11/20/content_5562997 .
htm.
Xue, L.L., J. Liu, Y. Wang, X.S. Liu, and X. Ying. 2020. Action Plans and 
Policy Recommendations on Vehicle Grid Integration in China. Wash -
ington, DC: World Resources Institute. 
Xue, L.L., Y.N. Jin, R.J. Yu, Y. Liu, and H. Ren. 2019. “Toward ‘Net Zero’ 
Emissions in the Road Transport Sector in China.” Working Paper. 
Washington, DC: World Resources Institute.
Yang, L.H., O. Delgado, and R. Muncrief. 2019. “Barriers and Opportuni-
ties for Improving Long-Haul Freight Efficiency in China.” Beijing: 
International Council on Clean Transportation.
Yang, Z.F., and H.Y. Cui. 2020. Technology Roadmap and Costs for Fuel 
Efficiency Increase and CO 2 Reduction from Chinese New Passenger 
Cars in 2030. Beijing: International Council on Clean Transportation.
Yeh, S., G.S. Mishra, L. Fulton, P. Kyle, D. McCollum, J. Miller, P. Cazzola,  
et al. 2017 . “Detailed Assessment of Global Transport-Energy Models’ 
Structures and Projections.” Transportation Research Part D: 
Transport and Environment 55: 294–309. ISSN 1361-9209. https://doi.
org/10.1016/j.trd.2016.11.001.
Yin, X., W.Y. Chen, Y.J. Eom, L.E. Clarke, S.H. Kim, P.L. Patel, S. Yu, et al. 
2015. “China’s Transportation Energy Consumption and CO 2 Emissions 
from a Global Perspective.” Energy Policy 82: 233–48. ISSN 0301-4215. 
https://doi.org/10.1016/j.enpol.2015.03.021.
Zhang, H.J., W.Y. Chen, and W.L. Huang. 2016. “TIMES Modelling of 
Transport Sector in China and USA: Comparisons from a Decarboniza -
tion Perspective.” Applied Energy 162: 1505-1514.
Zhang, H., J. Chen, W. Li, X. Song, and R. Shibasaki. 2020. “Mobile 
Phone GPS Data in Urban Ride-Sharing: An Assessment Method for 
Emission Reduction Potential.” Applied Energy 269: 115038. https://doi.
org/10.1016/j.apenergy.2020.115038.

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
87
Zhou, H.Y., Y.C. Wang, and J.R. Huscroft. 2020. “Impacts of COVID-19 on 
the Transportation Sector: A Report on China.” SSRN. http://dx.doi.
org/10.2139/ssrn.3679662. 
ZTB (Zhuzhou Transport Bureau). 2017 . Zhuzhou Annual Transport 
Development Report. Zhuzhou, China: Zhuzhou Transport Bureau.   
ABOUT THE AUTHORS 
Lulu Xue, China Mobility Manager, WRI China. Contact: Lxue@wri.org
Daizong Liu, China Sustainable Cities Director, WRI China.

88
WRI.org.cn
PHOTO CREDITS 
Cover Harry Zhang; pg. i Unsplash/JJ Ying; pg. ii Harry Zhang;  
pg. iv Harry Zhang; pg. x Unsplash/David Veksler; pg. x Harry Zhang;  
pg. xi Harry Zhang; pg.xi Unsplash/Decry.Yae; pg.xii, Harry Zhang;  
pg. 3 Unsplash/Zhang gc; pg. 6 Unsplash/Kevin Grieve; pg. 14 Harry Zhang;  
pg. 15 Zhao Yanrong; pg. 17 Harry Zhang; pg. 18 Unsplash/zhang kaiyv;  
pg. 31 Harry Zhang; pg. 42 Unsplash/Jerry Wang;  
pg. 67 Unsplash/LUFANG CAO; pg. 68 Unsplash/Luca Deasti;  
pg. 71 Unsplash/billow926; pg. 72 Unsplash/Decry.Yae.
ABOUT WRI 
World Resources Institute is a global research organization that turns big 
ideas into action at the nexus of environment, economic opportunity, and 
human well-being.
Our Challenge
Natural resources are at the foundation of economic opportunity and 
human well-being. But today, we are depleting Earth’s resources at rates 
that are not sustainable, endangering economies and people’s lives. 
People depend on clean water, fertile land, healthy forests, and a stable 
climate. Livable cities and clean energy are essential for a sustainable 
planet. We must address these urgent, global challenges this decade.
Our Vision
We envision an equitable and prosperous planet driven by the wise 
management of natural resources. We aspire to create a world where the 
actions of government, business, and communities combine to eliminate 
poverty and sustain the natural environment for all people.
Our Approach
COUNT IT
We start with data. We conduct independent research and draw on the 
latest technology to develop new insights and recommendations. Our 
rigorous analysis identifies risks, unveils opportunities, and informs smart 
strategies. We focus our efforts on influential and emerging economies 
where the future of sustainability will be determined.
CHANGE IT
We use our research to influence government policies, business 
strategies, and civil society action. We test projects with communities, 
companies, and government agencies to build a strong evidence base. 
Then, we work with partners to deliver change on the ground that allevi-
ates poverty and strengthens society. We hold ourselves accountable to 
ensure our outcomes will be bold and enduring.
SCALE IT
We don’t think small. Once tested, we work with partners to adopt and 
expand our efforts regionally and globally. We engage with decision-mak-
ers to carry out our ideas and elevate our impact. We measure success 
through government and business actions that improve people’s lives 
and sustain a healthy environment.

Decarbonizing China’s Road Transport Sector: Strategies toward Carbon Neutrality
89
Each World Resources Institute report represents a timely, scholarly treatment of a subject of public concern. WRI takes responsibility for choosing the study 
topics and guaranteeing its authors and researchers freedom of inquiry. It also solicits and responds to the guidance of advisory panels and expert reviewers. 
Unless otherwise stated, however, all the interpretation and findings set forth in WRI publications are those of the authors.
Copyright 2022 World Resources Institute. This work is licensed under the Creative Commons Attribution 4.0 International License.
To view a copy of the license, visit http://creativecommons.org/licenses/by/4.0/

90
WRI.org.cn
WRI CHINA
RM K-M, 7/F, TOWER A, THE EAST GATE PLAZA,  
#9 DONGZHONG STREET, BEIJING, CHINA, 100027
PHONE: 86 10 6416 5697
FAX:86 10 6416 7567
WWW.WRI.ORG.CN
