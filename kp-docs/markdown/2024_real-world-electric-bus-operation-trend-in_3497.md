---
doc_id: 2024_real-world-electric-bus-operation-trend-in_3497
source_pdf: kp-docs/askwri-kps/2024_real-world-electric-bus-operation-trend-in_3497.pdf
extraction_method: cache-plaintext
char_count: 117184
title: "Real-world Electric Bus Operation: Trend in Technology, Performance, Degradation, and Lifespan of Batteries"
authors: Kumar, Dr Parveen; Mulukutla, Pawan; Doshi, Priyansh
date_published: 12/1/2024
article_type: Working Paper
sub_tag: Transport decarbonization
wri_primary_office: WRI India
wri_programs: Cities
language: English
url: "https://wri-india.org/research/real-world-electric-bus-operation-trend-technology-performance-degradation-and-lifespan"
doi: "https://doi.org/10.46830/wriwp.22.00097"
summary: Battery lifespan in electric buses (e-buses) is significantly affected by external conditions, with accelerated degradation under high temperatures and improper charging practices leading to reduced operational capacity and increased total cost of ownership. This working paper analyzes real-world data and experimental findings on battery technologies, particularly lithium-ion variants, to assess their performance under varying climates, especially in India. Recommendations include optimizing battery sizing, implementing efficient thermal management systems, and adopting advanced battery management systems for real-time monitoring. The findings emphasize the need for tailored strategies and policies to enhance battery longevity and economic viability in the growing e-bus market.
---

# Real-world Electric Bus Operation: Trend in Technology, Performance, Degradation, and Lifespan of Batteries

WORKING PAPER  |  Version 1.0  |  January 2024   |  1
CONTENTS
Executive summary ..................... 2
Intro
duction. . . . . . . . . . . . . . . . . . . . . . . . . . . . .4
Research design and methodology . . . . .5
Battery technologies for e-buses. . . . . . . .6
Battery life in e-buses . . . . . . . . . . . . . . . . . . .11
Impact of high battery degradation .... 20
Su
mmary and way forward ............ 22
Ann
ex A. Basic technical details. . . . . . . .25
Annex B. Battery life analysis: 
Data collection template. . . . . . . . . . . . . . .27
Ab
breviations .......................... 30
En
dnotes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .30
References ............................. 31
Ac
knowledgments ..................... 36
Abo
ut the authors. . . . . . . . . . . . . . . . . . . . . .36
About WRI India ....................... 36
Working Papers contain preliminary research, 
analysis, findings, and recommendations. They are  
circulated to stimulate timely discussion and critical 
feedback, and to influence ongoing debate on 
emerging issues.
Suggested Citation: Kumar, P.,  Mulukutla P., 
and Doshi P., 2023. “Real-world electric bus 
operation: Trend in technology, performance, 
degradation, and lifespan of batteries” Working 
Paper. WRI India. Available online at 
doi.org/10.46830/wriwp.22.00097
WORKING PAPER
Real-world electric bus operation: 
Trend in technology, performance, 
degradation, and lifespan of batteries
Dr. Parveen Kumar, Pawan Mulukutla, and Priyansh Doshi
HIGHLIGHTS
▪ The pace of bus electrification is increasing in order to decarbonize the
public transportation system. Lithium-ion batteries form the most valu-
able component of an electric bus from a cost and performance point
of view.
▪ The lifespan of an e-bus battery is reduced due to accelerated battery
degradation under non-optimal operating conditions. Temperature
extremes induce battery ageing, impacting the e-bus operational
capacity, safety, and replacement ratio. This can spike the total cost of
ownership, compromising the economic viability of e-buses.
▪ Availability of real-world operational data for e-buses is limited globally,
and almost absent in India. This paper analyzes cell-level experimental
data for popular battery technology on degradation under variable
conditions and compares it with real-world case studies, to deduce
scenarios for best performance under Indian climatic conditions.
▪ For a given route, the battery sizing and charging strategy should con-
sider the energy consumption requirement and efficiency of an e-bus.
The battery pack must be equipped with an efficient thermal manage-
ment system to maintain optimum battery temperature.
▪ In batteries, an advanced battery management system must be used for
real-time monitoring and data collection. Data availability will be crucial
for developing required standards, regulations, and testing ecosystems
to ensure the adoption of best practices.

2  |  
  
EXECUTIVE SUMMARY
Context
The transport sector is one of the fastest-growing carbon 
emitters and a leading cause of air pollution in major cities 
and in need of interventions for decarbonization. Electrifica-
tion of buses is necessary for eliminating tailpipe emissions, 
and building a clean and low-carbon public transportation 
system. Several countries across the world are accelerating 
e-bus adoption through enabling policies, tax incentives, 
and subvention. However, challenges such as upfront cost 
of e-buses being twice or thrice that of internal combustion 
engine (ICE) buses, range issues, bottlenecks in the supply 
chain, and under-developed charging infrastructure stand in 
the way of large-scale adoption of e-buses across the world.
In e-buses, batteries account for 40–50 percent of the total 
upfront purchase cost and form the most critical component 
of the e-bus powertrain. The performance of e-buses also 
depends on the batteries, which  degrade faster under non-
optimal usage. For example, the ideal lifespan of lithium-ion 
batteries (LIBs) in the e-bus application should be 5–7 years. 
However, the batteries’ lifespan is affected tremendously by 
non-optimal conditions of temperature, state of charge (SoC), 
charging rate (C-rate), and depth of discharge (DoD). Factors, 
such as driving behavior, auxiliary consumption, road quality, 
passenger load, speed, topography, and climate, influence the 
energy consumption per kilometer, which in turn impacts the 
driving range per charge of the e-bus. While stakeholders 
are already planning to overcome bottlenecks associated with 
range and energy consumption, accelerated battery degrada-
tion will affect battery capacity, further reducing the driving 
range per charge of the e-bus. This would lead to frequent 
charging requirements to achieve the desired daily trip length. 
Moreover, rapid degradation will push an e-bus battery to 
complete its automotive life (i.e., 20 percent capacity loss 
compared to its rated/original capacity) much before its ideal 
lifespan, requiring a higher number of battery replacements 
per service life. As the e-bus market develops across the world, 
a high-level assessment of the reduction of battery life and 
efficiency due to accelerated battery degradation in e-buses 
running under non-optimal conditions is necessary for 
improving their feasibility.
About this paper 
With this paper, we aim to familiarize original equipment 
manufacturers (OEMs), state road transport undertakings 
(SRTUs), and other key stakeholders with the factors that 
accelerate battery degradation and its impact on the perfor-
mance and economic viability of e-buses. This understanding 
will help stakeholders to optimize the e-bus operation, mini-
mize battery degradation, and improve the energy efficiency 
per kilometer (km) of travel. This will further help in selecting 
the best operating scenarios, optimizing battery sizing and 
charging requirements, and improving battery life.
In this working paper, we identify specific battery technolo-
gies preferred for powering e-buses in different geographical 
locations across the world and assess their performance under 
different environmental conditions. The paper studies how 
different stress factors contribute to ageing of batteries and 
their overall impact on the automotive life of e-bus batter-
ies. This paper also assesses how this battery degradation can 
affect the battery and e-bus performance in the near term, and 
the battery life and economic viability of the e-bus in the long 
term. This analysis is followed by a series of recommendations 
to adopt best practices, improve planning, and devise policy, 
which will be instrumental in improving battery lifespan in 
countries like India, which are planning for large-scale adop-
tion of e-buses for public transport.
The e-bus ecosystem is still developing in India; therefore, the 
local battery pack-level data on the impact of different stress 
factors on battery life is unavailable in the public domain. 
Hence, we have adopted a literature review and desk research 
path to analyze global data on e-bus battery degradation at the 
cell level (taken from experimental and simulation-based stud-
ies) and have correlated the same with the available pack-level 
real-world case studies from different geographical regions 
with varying operating conditions. As the global real-world 
scenarios can be different from those in India, we recommend 
collecting region-specific pack-level data to develop custom-
ized strategies to improve battery life.
Key findings 
 ▪ Globally, battery chemistries, such as lithium iron phos-
phate (LFP), lithium nickel manganese cobalt (NMC), 
lithium titanium oxide (L TO), and lithium manganese 
oxide (LMO) have found space in e-bus applications 
where LFP and NMC variants are most widely used. 
Globally, NMC batteries are preferred for regions with 
long duty cycles, whereas LFP batteries are chosen in 
regions with shorter duty cycles.
 ▪ NMC batteries have high energy density but are sensitive 
to high C-rates, where fast charging can reduce their life- 
span by 10 percent compared to overnight slow charging. 
LFP batteries have high cycle-life, high DoD tolerance, 
and thermal stability but lower energy density than NMC 
batteries. L TO batteries show higher stability for flash and 
fast charging. The desirable range of an e-bus is achieved 
by sizing a battery optimally and choosing a suitable 
charging strategy to meet bus route energy consump-
tion requirement.

WORKING PAPER  |  January 2024  |  3
Real-world electric bus operation: Trend in technology, performance, degradation, and lifespan of batteries
 ▪ The lifespan of e-bus batteries depends on calendar ageing 
and cyclic ageing, which in turn lead to capacity  
fade and power fade. While high ambient temperature (> 
30°C) and high SoC (> 80 %) accelerate calendar ageing, 
high depth of discharge (>80 %), the extreme operating 
temperature of the batteries, and high C-rates acceler-
ate cyclic ageing.
 ▪ The degradation trend of batteries suggests that a battery 
degrades the most during the initial years due to initial 
high calendar ageing, especially in regions that experi-
ence high-temperature extremes. Degradation rate due to 
cyclic ageing is affected by both high and low temperature 
extremes and is consistent throughout the battery lifespan. 
The capacity of the LFP battery degrades to 80 percent 
(i.e., end of automotive life) in 4,000 cycles at 25°C and in 
2,000 cycles at 45°C. Similarly, the NMC battery com-
pletes its automotive life in 1,200 cycles at 34°C and in 
500 cycles at 46°C.
 ▪ Drive range per charge of an e-bus depends on both 
traction and auxiliary power requirements where external 
factors like temperature, topography, and driving behavior 
affect the energy efficiency. Battery degradation induces 
capacity fade, which reduces e-bus drive range by 26 per-
cent over its automotive life. This in turn requires frequent 
charging to finish the desired trip, further increasing 
energy demand on a route.
 ▪ Increase in the charge time in a day will reduce the service 
time of e-buses, affecting the operational efficiency. This 
will lead to a requirement of larger number of e-buses to 
reach the operational efficiency of diesel buses, unbalanc-
ing the replacement ratio at a city level.
 ▪ A 20 percent reduction in battery life due to accelerated 
battery degradation leads to an increase in the total cost 
of ownership (TCO) of an e-bus by 2.2 percent. Further, 
the TCO of an e-bus increased by 13–30 percent as the 
distance the e-bus could travel decreased by 10–30 percent 
(due to reduced battery life).
Key recommendations 
Based upon observations made and insights obtained, we have 
developed the guidance on maintaining optimal battery life. 
Operational recommendations 
 ▪ State of charge and temperature management to reduce 
calendar ageing:  The e-bus should not be parked for a 
long time under high ambient temperature (>30°C), espe-
cially when under a high SoC of the battery (>50%).
 ▪ Charging and discharging strategy to reduce cyclic 
ageing: The battery pack should neither be overcharged 
(>80% SoC) nor over-discharged (<20% SoC) and must be 
charged at an optimum C-rate and temperature, which can 
be ensured by implementing a charging strategy suitable 
for the battery chemistry.
 ▪ Adopting the right charging technique: Except for L TO 
variants of LIB, fast charging should be avoided for other 
commercial variants of LIBs when possible, especially 
when charging in low-temperature conditions.
Planning recommendations 
 ▪ Battery sizing and charging strategy: Using param-
eters such as energy consumption per km and route 
length for optimum battery sizing for e-buses. 
Planning adequate opportunity charging infra-
structure along with depot charging can help in 
maintaining the SoC and DoD of batteries at optimal 
levels, thereby improving their lifespan.
 ▪ Degradation cost in TCO estimation: Battery wear cost 
and opportunity charging cost contribute to the opera-
tional cost of an e-bus and therefore should be included 
in the TCO estimation.
 ▪ Circular economy in e-bus business models: After the 
end of the automotive life of the battery, the battery 
should go for reuse and recycling to generate additional 
profits, reducing the TCO per km of e-buses, and ensur-
ing the efficient utilization of resources.
 ▪ Driver training: Drivers must be trained for energy-
efficient driving. The training must include equipping the 
drivers with the basic knowledge of the technology, driver 
simulator training, and on-road training. This will reduce 
trip energy consumption and ensure good battery health 
in the e-bus application.
Technical recommendations
 ▪ Efficient BMS and TMS for battery: In tropical and 
subtropical regions, an efficient battery thermal man-
agement system (TMS) must be deployed to maintain 
the battery temperature under optimal range. Also, an 
advanced battery management system (BMS) must be 
installed for real-time monitoring of battery health and 
recording of data for detailed analysis.
 ▪ Regenerative braking system adoption: Drive range 
uncertainty can be reduced with optimized energy con-
sumption for traction in an e-bus drive cycle. Adoption 
of a regenerative braking system will cover the energy 
loss during deceleration in a driving cycle and transfer it 
to the powertrain to recharge the battery, improving the 
energy efficiency per km (10–15%).

4  |  
  
 ▪ T echnical performance and efficiency: The e-bus must 
be equipped with an intelligent energy management 
system (IEMS) to monitor and regulate auxiliary energy 
demands, and an eco-driving assistance system (EDAS) 
to ensure energy-efficient driving.
Policy recommendations 
 ▪ Battery data collection and management: A policy and 
regulatory framework to facilitate an active collabora-
tion among stakeholders for battery data collection, 
management, and sharing can help researchers, e-bus 
operators, and OEMs,  analyze e-bus battery operational 
data, devise best operating practices, and come up with 
innovate solutions to minimize battery degradation under 
different operating conditions.  
 ▪ Standards, regulation, and testing: With the availability 
of India-specific data, fit-for-purpose standards can be 
adopted where C-rates, DoD, and temperature match the 
local operating conditions. The battery durability test-
ing under these conditions will estimate battery ageing 
and impact on cycle-life of the e-bus batteries in specific 
regions with higher precision.
INTRODUCTION
Over the last few years, multiple sectors across the world have 
pledged various decarbonization initiatives in a race to achieve 
net-zero goals. Development of a low-carbon transportation 
system has emerged as one of the top priorities for all major 
economies of the world in their fight against climate change 
and air pollution. For the low-carbon movement of passen-
gers, switching to electric mass-transit vehicles such as electric 
buses (e-buses), which offer zero tailpipe emissions and 35 
percent (ITF 2023) lower lifecycle emissions than diesel buses, 
is gaining significant attention. 
E-buses account for 18 percent of the global bus fleet (IEA 
2022), with China dominating the space, followed by Europe, 
India, Southeast Asia, and the USA (IEA 2023). Govern-
ments across the world have laid out support in the form of 
policies, incentives, and subsidies for faster penetration of 
electric buses in the public transportation system. China has 
introduced a slew of initiatives, including New Electric Vehi-
cle (NEV) subsidy programme, NEV credit mandate, policies 
promoting EV charging infrastructure, and city-specific 
targets for accelerating e-bus adoption. Europe has set opti-
mistic targets for e-mobility under the European Green Deal, 
and is accelerating e-bus adoption under the EU Sustainable 
and Smart Mobility Strategy and Action Plan to achieve 
the target of 100 percent zero-emission buses. India targets 
to achieve 40 percent annual e-bus sales by 2030 with flag-
ship initiatives such as Faster Adoption and Manufacturing 
of (Hybrid &) Electric Vehicles (FAME) II scheme as part 
of the National Electric Mobility Mission Plan (NEMMP) 
2020. After announcing the world’s largest e-bus procurement 
tender for deploying 5,450 units under the Grand Challenge 
(an initiative to create homogenized demand across nine 
cities), the state-run Convergence Energy Services Limited 
(CESL),  is further developing a roadmap to expand the e-bus 
network in tier-II cities under the National Electric Bus Pro-
gram (NEBP) to roll out 50,000 units in the next 7–10 years. 
In this direction, CESL has floated its first tender for procure-
ment of 5,690 buses under NEBP . Moreover, with the onset 
of the scheme named Prime Minister E-bus Sewa, govern-
ment is planning to deploy 10,000 e-buses in the regions with 
underdeveloped organized bus services (PIB 2023).
Despite the policy support, e-bus adoption is still limited in 
India due to capex costs being two to three times higher than 
internal combustion engine (ICE) buses, under-developed 
charging facility, range uncertainty, and the gap between theo-
retical and actual service life of e-buses. As the operational 
costs are significantly lower in e-buses, the total cost of owner-
ship can be reduced with the adoption of business models 
that reduce these capex costs; lower technical and financial 
barriers associated with the vehicle, battery, and charging 
infrastructure; and introduce risk-sharing mechanisms among 
stakeholders. The leasing model is developing as an alterna-
tive to the outright purchase model for e-bus procurement 
to address the bottlenecks associated with the e-bus and its 
battery component. For example, in the battery subscription 
model, lithium-ion batteries (LIBs), which form 40–50 per-
cent of the e-bus cost, are leased out separately, to reduce the 
upfront cost of the e-bus. It should be noted that the sustain-
ability of these business models depends on the performance 
and lifespan of the battery, which further depends on multiple 
attributes. Typically, an e-bus battery has a lifespan of 5–7 
years but when subjected to non-optimal operating condi-
tions, including ambient temperature extremes, aggressive 
driving, and charging behaviors, these batteries can undergo 
rapid degradation, reducing their life and efficiency. Therefore, 
having an in-depth knowledge of the impact of these external 
stress factors, such as temperature, state of charge (SoC), 
depth of discharge (DoD), and charging rate (C-rate) on 
battery ageing, is necessary to reduce degradation and improve 
battery life. This requires region-specific real-world pack-level 
operating data of an e-bus battery.
While real-world data on battery operation are fragmented 
in countries such as China, Europe, and the USA, which are 
leading in e-bus adoption, data are unavailable in India due to 
the nascent stage of the domestic ecosystem and inhibitions 
around sharing data. Here, assessing  the laboratory-based 
research about the performance and life of batteries under 
different stress conditions and comparing the results with 
available real-world global data can help in identifying the

WORKING PAPER  |  January 2024  |  5
Real-world electric bus operation: Trend in technology, performance, degradation, and lifespan of batteries
optimum conditions to achieve the ideal life span of the 
battery in e-buses.  In this working paper, we have analyzed 
the emerging global trend in battery technology for e-bus 
application, and the cell-level degradation trend in selected 
battery chemistries and reviewed case studies from across the 
world to understand accelerated e-bus battery degradation 
under non-optimal conditions and its consequent impacts on 
e-bus operation and economic feasibility. Further, we have 
identified the best scenario for the optimum battery life in 
e-bus applications, especially for e-buses operating in tropical 
environments like India’s. Finally, we have suggested strate-
gies to achieve optimal battery life in e-buses, emphasizing on 
real-world local data collection to further optimize the e-bus 
operational strategies in India and across the world.
RESEARCH DESIGN AND 
METHODOLOGY
In this study, we have conducted an in-depth literature 
review and data analysis to identify the impact of various 
stress factors on the battery life and performance of an e-bus. 
Further, we have analyzed the potential implications of battery 
degradation on different stakeholders in the ecosystem, 
including SRTUs, OEMs, e-bus operators, and e-bus users. 
Overall, we explore the following research questions for 
developing this working paper:
 ▪ Which battery technologies are preferred for pow-
ering e-buses in different geographical locations 
across the world?
 ▪ How do different e-bus batteries function in different 
environmental and operating conditions, and what is their 
impact on energy consumption and battery life?
 ▪ What is the role of different degradation mechanisms in 
the overall battery degradation rate in e-buses? 
 ▪ What are the short-term impacts of battery degradation 
on e-buses and how do they affect a business model’s 
economic viability in the long run?
 ▪ What kind of planning and policy-level interventions can 
help in achieving the optimal battery life for sustainable 
e-bus business models?
Review of battery technologies in 
e-bus applications 
Multiple variants of lithium batteries are available for electric 
vehicle (EV) applications globally. We adopted a literature 
review and desk research path to collect secondary data from 
reports, technical papers, scholarly articles, magazines, and 
blogs. We conducted a search using academic search engines 
such as Google Scholar with several combinations of key-
words such as ‘battery type in e-bus’, ‘battery cell form factor’, 
‘cell design’, ‘battery degradation’, and so on, along with a 
deep Google search for other online content. We collated data 
on battery chemistries used by e-bus companies in different 
regions leading e-bus adoption across the globe. 
We have encapsulated qualitative data from studies such as 
the one by Olsson, Grauers, and Pettersson (2016) on the 
trade-offs between battery size (large and small) and charger 
utilization (slow charging and frequent high-power charging). 
Finally, we have identified factors affecting energy consump-
tion in an e-bus, which is important for selecting a suitable 
battery size and charging strategy for an e-bus.
Battery degradation data analysis 
In battery packs, multiple cells are packed together to achieve 
the required capacity of an e-bus, where these cells are avail-
able in different chemistries and form factors. These battery 
packs undergo degradation on both cell level and pack level 
over time. Although cell-level degradation data, both experi-
mental and simulation, for different battery chemistries used 
in e-buses are available in scholarly articles, the availability of 
real-world pack-level battery degradation data is limited due 
to the nascent stage of the e-bus ecosystem globally. Therefore, 
quantitative and qualitative data were analyzed for cell-level 
degradation analysis, while qualitative data were used for 
pack-level analysis. To get an insight into the degradation 
mechanism in different battery chemistries, we analyzed the  
experimental, simulation, and mathematical model-based 
research data at the cell level. 
We could comprehend the cell-level interplay between stress 
factors such as temperature and SoCs, and an overall degrada-
tion in different battery chemistries by analyzing data available 
in multiple research articles (Keil et al. 2016; Saxena et al. 
2015; Ouyang et al. 2016). For the lifespan of battery packs 
with different chemistries, we analyzed the data reported in 
various reports and research articles. For example, we reviewed 
a case study by Al-Saadi et al. (2022), which uses simulation 
data, both qualitative and quantitative, from three cities in 
Europe; namely, Barcelona, Osnabrück, and Gothenburg. 
Based on the above analyses, we have given insights into the 
best and worst scenarios for battery life, and possible strategies 
to achieve optimum battery life in e-bus applications in the 
latter sections.
Assessing impacts of battery 
degradations 
Due to the lack of real-world data specific to Indian operat-
ing conditions for identifying the barriers in the operation 
of e-buses, we have reviewed qualitative data from different

6  |  
  
Table 1  |  Comparison of electrical parameters of lithium-ion cell variants used in e-buses  
PARAMETERS LFP NMC LTO
Cell voltage (V) 3.2 3.6 2.3
Energy density (Wh/kg) 115–146 165–175 76–77
Charge rate (C-rate) 1C 0.7–1C 4C–10C
Cycle life (at 100% DoD) 3,600 3,000 10,000–20,000
Discharging temperature (°C) -30–55 -20–55 -30–55
Charging temperature (°C) -20–55 0–55 -20–55
Safety (thermal runaway) High (270°C) Low (210°C) Highest (280°C)
Battery cost per kWh Low Medium High
Source: Baumann et al. 2017; Göhlich et al. 2019.
regions of the world about the immediate impacts of high 
battery degradation on battery sizing, energy efficiency of 
e-buses, range estimation, vehicle downtime, and replacement 
ratio. For example, we have reviewed the observations of a 
study by Mcgrath et al. (2022), which assesses the conse-
quence of degradation on the range, charger utilization, and 
e-bus battery sizing in the United Kingdom (UK).
To get an insight into the long-term impacts of battery deg-
radation, we reviewed studies and analyses related to the total 
cost of ownership (TCO) of e-buses. A TCO analysis helps in 
determining the operating cost of the vehicle per km, taking 
into consideration various parameters such as the capital cost 
of the vehicle including taxes, the lifetime operating cost, 
and battery replacement cost. We have used our previously 
reported TCO method (Kumar and Chakrabarty 2020) to 
evaluate the effect of upfront battery cost on TCO per km of 
e-buses, and its comparison with the diesel bus variants. 
Limitations of the study 
We have gathered reported data on impact of operating 
conditions on battery life from lab-based research and case 
studies. In some cases, we have extrapolated the data to under-
stand the trend in battery life. The case studies on operating 
conditions for various battery chemistries in different states 
of the USA (Yang et al. 2018), Chinese cities of Zhengzhou 
and Shenzen (Li et al. 2020, Applied Energy) and European 
cities of Barcelona, Osnabrück, and Gothenburg (Al-Saadi 
et al. 2022) compare battery degradation at pack level under 
various temperature ranges and SoC. We have used both these 
cell-level data and pack-level case studies to understand the 
possible trends of degradation, which can aid in the develop-
ment of best e-bus operating conditions in India. Due to lack 
of reported data for battery degradation in India, the effect of 
actual usage of e-buses on battery degradation can be dissimi-
lar to what the study has noted, requiring detailed analysis to 
assess the exact picture of battery life and degradation in the 
Indian operating conditions.
BATTERY TECHNOLOGIES FOR 
E-BUSES
This section highlights the performance trends of different 
battery technologies used for e-buses operating in different 
geographical regions.
Battery technologies for e-bus 
application 
Over the years, rapid technological advancements in lithium-
ion batteries (LIBs) have made them a preferred choice for 
EV applications. LIB performance and energy efficiency can 
vary based on battery cell chemistry, battery cell format, and 
cell-to-battery packaging. 
Battery cell chemistry 
Based on cathode chemistry, LIBs come in different variants, 
such as lithium iron phosphate (LFP), lithium nickel manga-
nese cobalt (NMC), lithium manganese oxide (LMO), and 
lithium nickel cobalt aluminium oxide (NCA) or anode chem-
istries like graphite or lithium titanium oxide (L TO). While 
these battery chemistries are competing to find applications 
in various EV segments, LFP , NMC, and L TO variants are 
emerging as suitable options for e-buses due to their relatively 
better performance.

WORKING PAPER  |  January 2024  |  7
Real-world electric bus operation: Trend in technology, performance, degradation, and lifespan of batteries
Among LFP , NMC, and L TO variants (Table 1, Figure 1), 
NMC cells offer high energy density, providing a relatively 
higher drive range per charge, resulting in smaller and lighter 
battery packs. L TO chemistry on the other hand has the low-
est energy density, requiring bigger and heavier battery packs 
to achieve the desirable range. NMC cells have lower thermal 
endurance and the high cobalt content makes them relatively 
less environmentally friendly and expensive compared to LFP 
cells. Among the three LIB variants, the cycle life of L TO 
cells is the highest, and that of NMC cells is the lowest. The 
high C-rates and excellent thermal stability characteristics 
of L TO cells make them feasible for frequent opportunity 
charging and ultra-fast charging, which in turn can help in 
substantial reduction of charging time. Moreover, stability to 
high C-rates makes L TO batteries more suitable for regen-
erative braking1, improving their energy efficiency. Also, the 
better cold-temperature performance of L TO battery com-
pared to LFP and NMC batteries makes L TO a good choice 
of battery in regions where cold start-ups are required. Despite 
their superior performance, the high material cost of L TO 
batteries is among the major challenges in their large-scale 
adoption in the e-bus market. LFP batteries have the least 
material criticality of the three options and offer promising 
energy density, cycle life, and thermal stability at an economi-
cal price tag, making them popular in cost-sensitive markets 
like India (Carrilero et al. 2018).
Figure 1  |  Comparison of different types of Li-ion 
batteries used in e-buses  
Source: Miao et al. 2019.
LFP LTO NMC
Specific
energy
Specific
power
Performance
SafetyLifespan
Cost
0
1
2
3
4
Figure 2  |  Comparison of different cell designs  
Source: Authors’ analysis.
Prismatic Pouch Cylindrical
Mechanical
strength
Energy
density
Cost per
energy capacity
Heat
management
Performance
on the cell
Power
density
Specific
energy
5
4
3
2
1
0
Battery cell design 
Battery cells can further be distinguished into pouch, pris-
matic, and cylindrical cells, based on form factor and casing 
material (Figure 2). Prismatic cells store the highest energy 
density at present, have better packaging efficiency due to 
their compact size, bear high mechanical stresses from their 
cover, and have a simpler battery management system design. 
These features make them the most suitable cell format for 
e-buses. Among other popular cell designs, pouch cells do not 
have a strong, hard case, but the weight is 20 percent lower 
than that of prismatic cells of the same capacity, and the 
capacity is ~50 percent higher than prismatic cells of the same 
volume (Chen 2022). Cylindrical cells are easy to manufac-
ture, and their design is transitioning from lower volume 
18,650 cells (18mm diameter x 65mm length) to higher 
volume 21,700 (21mm diameter x 70mm length) battery cells, 
which increases energy density by 30 percent at the cell level 
and 20 percent at the pack level. Further, introduction of the 
46,800 cylindrical cells will increase the cell capacity by five 
times and power by six times, compared to the 18,650 cells, 
which could popularize them in e-bus application in future. In 
2021, prismatic cells dominated the LIB cell manufacturing 
in China, pouch cells dominated the LIB cell manufacturing 
in Europe and Korea, whereas cylindrical cells accounted for 
the majority share in LIB cells manufactured in USA and 
Japan (Neef 2022).

8  |  
  
Battery pack design 
Batteries are made of multiple individual cells packed together 
in different configurations. Inefficient packaging leads to a 
reduction of specific energy density (Wh/kg) from cell to pack 
level (Figure 3), leading to a reduction in range and increase in 
the volume of battery packs. It’s observed that the LFP battery 
pack allows a better cell-to-pack level efficiency compared to 
the NMC battery variant (approximately 28 percent and 33.3 
percent reduction in energy density from cell-to-pack level for 
LFP and NMC cells, respectively). This is due to the enhanced 
safety of LFP cell chemistry allowing battery packs to be 
constructed with more densely packed cells (QuantumScape 
2021). Innovative blade batteries, introduced by EV manufac-
turer BYD Motors, increase space utilization by 50 percent 
(due to the unique cell-to-pack design), resulting in better 
cell-to-pack efficiency compared to the conventional LFP 
batteries (BYD. n.d.A).
In brief, battery cell chemistry can be selected based on desired 
key performance indicators (KPIs), cost factor, lifespan, and 
charging requirements (Annex A). Further, cell-to-packaging 
efficiency can be improved by optimizing battery space utiliza-
tion. This is critical for limiting the reduction in a battery’s 
energy density.
Figure 3  |   Comparison of specific energy density from cell to pack level  
Source: Sustainable Bus 2021 A.
0
50
100
150
200
250
300
2014 2015 2016 2017 2019 2020 2021 202220182013 2023
Energy density (Wh/kg)
Year
NMC cell level
NMC pack level
(estimated)
LFP cell level
LFP pack level
(estimated)
LTO cell level
LTO pack level
(estimated)
Emerging trends in battery 
technology selection 
The global trends for popular battery technologies suggest 
that NMC and LFP variants are favorable to e-bus OEMs. 
A snapshot of trends in major global markets for e-buses 
is given below:
China
China dominates the global e-bus market, with an annual 
sales share of around 85 percent as of 2022 (IEA 2023), 
with cities like Shenzhen, Tianjin, and Zhengzhou having 
achieved 100 percent bus fleet electrification (Yiyang and 
Fremery 2022).  
In China, the e-buses tend to operate on a shorter duty cycle,  
averaging 174.4 km (Xiao 2019, ITDP 2018), compared to 
the USA (200–250 km), due to its densely populated cities. 
This helps in prioritizing the cost factor over energy density, 
resulting in the predominant use of LFP battery packs. The 
average mileage of running an e-bus in the Chinese city of 
Macao is 1.73 kWh/km (Al-Ogaili et al. 2021), which is 
crucial for sizing a battery and charging infrastructure suitable

WORKING PAPER  |  January 2024  |  9
Real-world electric bus operation: Trend in technology, performance, degradation, and lifespan of batteries
Table 2  |  Battery type and specifications used by manufacturers in China  
BUS MANUFACTURER BATTERY TYPE BATTERY SIZE ( kWh) RANGE ( km)
Yutong LFP 295 220
BYD LFP 324 (C9) 250
Source: Yutong; BYD 2022.
for the vehicle operation. Moreover, the higher safety factor 
compared to that of NMC batteries makes LFP batteries the 
choice in heavy-duty e-buses in this region. 
Table 2 shows two of the largest e-bus manufacturers in 
China in terms of market share, accounting for 41 percent of 
the sales share in 2020 (Sustainable Bus 2021 B). These manu-
facturers use LFP batteries in their buses, suggesting that the 
LFP battery is the dominant variant used in China. In 2018, 
the two biggest battery manufacturers, BYD Motors and 
Contemporary Amperex Technology Co. Limited (CATL), 
together sold 78 percent of the e-bus batteries containing LFP 
variants (Sustainable Bus 2021 B).
North America
The USA is the biggest market in the North American region, 
with 3,533 e-buses operating as of 2021 whose deployments 
are largely reflective of policies in California (aiming for 
bus sales to be 100 percent electric by 2029) (IEA 2023). 
Canada accounted for a total stock of 850 e-buses as of 2022 
(IEA 2023). With sparsely populated cities and towns, states 
like Ohio need large duty cycles and consume 1.35 kWh of 
energy per km (Al-Ogaili et al. 2021). Hence, NMC batteries, 
which have high energy density compared to LFP and L TO 
batteries, dominate the market. Table 3 shows some of the 
major e-bus manufacturers in North America. New Flyer's 
indicates that an e-bus can allow a battery capacity of up to 
818 kWh using NMC batteries. These are the best suited to 
provide the required range in sparsely populated cities and 
towns of the USA. 
Europe
As of 2022, over 11,000 e-buses ply in Europe, with the 
Netherlands, France, Germany, and the United Kingdom 
dominating the e-bus markets, accounting for more than half 
of the total e-buses in the region (IEA 2023).
European cities have high population density, and bus routes  
are often shorter, with more frequent stops and starts  
(Sustainable Bus 2019), requiring higher energy consumption 
of up to 1.9 kWh, depending on weather (Graurs et al. 2015). 
The need to maximize energy recuperation requires a battery 
with a higher C-rate, leading to the predominant use of LFP 
batteries in this region, as shown in Table 4. Apart from the 
conventional LIBs, Europe e-bus manufacturer Irizar uses a 
sodium nickel chloride (also known as zebra) battery for the 
traction application. It’s a low-cost alternative for LIBs and 
can be completely discharged without causing any stress on 
Table 3  |  Battery type and specifications used by manufacturers in North America  
BUS MANUFACTURER REGION BATTERY TYPE BATTERY SIZE ( kWh) RANGE ( km)
BYD Los Angeles LFP 215 (K 7m)
446 (K9MD)
254
326
Proterra California, Southern California, 
Washington DC, Dallas
LTO/NMC 79–105
450
675
80–100
386
529
New Flyer Industries Canada, California, New York NMC 350
440
525
280
342
404
Source: Johnson et al. 2020; BYD 2022.

10  |  
  
Table 4  |  Battery type and specifications used by manufacturers in Europe  
BUS MANUFACTURER REGION BATTERY TYPE BATTERY SIZE ( kWh) RANGE ( km)
BYD (and ADL) UK LFP 348 257
Volvo Sweden, Netherlands, Oslo LFP 250 -
VDL Bus and Coach Belgium, Amsterdam, Scandinavia LFP 216-420 -
EBUSCO Netherlands LFP 400 350
Solaris Poland, France, Italy, Germany, Lithuania LFP 250 -
Irizar Spain, Luxembourg, Italy, Frankfurt, Orléans Sodium nickel technology 376 (i2e 12m) 220
Source: BYD 2021; Pagliaro and Meneguzzo 2019.
Table 5  |  Battery type and specifications used by manufacturers in India  
BUS MANUFACTURER BUS TYPE BATTERY TYPE BATTERY SIZE ( kWh) DECLARED RANGE ( km)
Olectra BYD Standard
Midi
Mini
LFP 342
200
135
300
200
200
PMI Foton Standard
Midi
Mini
LFP 150
150
102
144
168
-
Tata Motors Standard
Midi
NMC 260-350
176
160-220
150
JBM Solaris Standard
Midi
NMC 200
196
200
250
Switch Mobility Standard LFP 389 390
Source: TUMI and C40 Cities 2023; Pandya 2023; Switch Mobility 2022.
the health of the batteries compared to LIBs. However, the 
zebra battery has comparatively less energy density than LIBs, 
uses its own capacity to maintain internal temperature, and 
has a higher environmental footprint, making it less popular 
(Sawle and Thirunavukkarasu 2021; Battery University 2010)
India
The Indian e-bus market is particularly cost sensitive, requir-
ing batteries to deliver high KPIs and safety parameters 
while being affordable. This makes LFP and NMC batteries 
popular choices among other LIB variants. Moreover, the 
better thermal stability of the LFP battery pack under the 
hot and humid conditions of this region makes it a favor-
able choice. Table 5 shows some of the key players in India’s 
e-bus manufacturing space and the respective battery tech-
nologies they use.
In short, our analysis suggests that in various regions across 
the world, e-buses running on longer routes are generally 
equipped with NMC batteries due to their higher specific 
energy density and driving range, while those plying shorter 
distances use LFP or L TO batteries (also suitable for fast/flash 
charging) due to their higher C-rate capability (Biczel and 
Kwiatkowski 2018). Therefore, one way for India to incor-
porate diverse battery chemistries in its e-buses can be based 
on duty cycles. 
Battery sizing planning
Planning optimal battery sizing is vital for an e-bus to 
complete its scheduled service in a day. Several trade-offs are 
associated with battery sizing, cost, and charging requirements 
in an e-bus. Figure 4 shows the layout of battery sizing with

WORKING PAPER  |  January 2024  |  11
Real-world electric bus operation: Trend in technology, performance, degradation, and lifespan of batteries
Figure 4  |  Total charge power installed (I) and charger 
utilization per day (II) as a function of battery size  
Source: Olsson et al. 2016.
Charge power per bus line
Battery size
HighLow
BigSmall
HighLow
Usage of charging infrastructure
Battery size
BigSmall
(I)
(II)
Charging at
bus stop
Charging 
during
movement
Charging at
end station
Charging 
at depot
respect to charging power and charger utilization per day. 
Buses with smaller batteries have lower costs and high energy 
efficiency but fall short of the desirable range, increasing both 
vehicle downtime and charging requirements. Oversized 
battery packs provide a higher driving range per charge under 
optimal conditions but increase the curb weight, reducing the 
energy efficiency by 6–8 percent per ton increase in weight 
(Hodge et al. 2019), reducing payload capacity, and increas-
ing vehicle cost. Moreover, the energy consumption of an 
e-bus largely depends on traction (route length, drive cycle, 
driver behavior, topography) and auxiliary power used for 
heating, ventilation, and air-conditioning (HVAC) system 
requirements during the trip, which must be considered when 
sizing a battery.
OEMs should decide on a battery size for a desired drive 
range and suitable charging requirements for different routes 
based on these factors. Overnight slow charging at the depot 
is economical, requiring minimum charging infrastructure. The 
usage of fast chargers for a large number of e-buses with small 
battery packs at the depot may strain the grid in future, due to 
the aggregated load, necessitating a shift towards an alternate 
charging strategy. Therefore, to maintain optimal SoC for 
travel, overnight slow charging is suitable for shorter routes. 
For longer routes and routes with higher power requirements, 
they can use a combination of overnight slow charging at the 
depot and opportunity charging (at a controlled C-rate) at the 
terminal to achieve a desired range.
BATTERY LIFE IN E-BUSES 
It is well established that EV battery life depends on various 
factors, such as battery chemistry, driving patterns, and ageing 
under the influence of different stress factors. This section, 
therefore, presents degradation trends for lithium battery vari-
ants under different stress conditions.  
Factors affecting battery life
Batteries tend to age during the use phase of EVs as the 
irreversible physical and chemical changes occur due to 
environmental conditions, operational conditions, driving 
habits, and charging speed. Batteries degrade with time and 
usage, where the loss of capacity occurs during both standby 
(calendar ageing) and charging/discharging (cyclic ageing) 
conditions. Battery capacity fade and power fade are the two 
measurable quantities to assess battery degradation. Capacity 
fade, which means the decrease in charge storing capacity of a 
battery after every charging cycle, leads to EVs losing driving 
range capability over their lifetime. Power fade, which means 
a decrease in the amount of power a battery can provide due 
to an increase in internal resistance, results in a decrease in 
the performance of EVs, including acceleration, gradeability, 
and regenerative braking capabilities (Saxena et al. 2015). The 
battery life can be understood in three different yet coupled 
conditions as shown in Figure 5.

12  |  
  
Calendar ageing 
In a battery, calendar ageing occurs all the time but pre-
dominantly when the battery is idle, that is when the vehicle 
is parked and there is no flow of current through the LIBs 
(Beltran et al. 2022). The rate of battery degradation due to 
calendar ageing shows a very steady trend (Sui et al. 2021), 
wherein the rate of increase in capacity fade and internal 
resistance gradually subsides as the ageing advances.
Factors affecting calendar ageing
Factors such as state of charge (SoC) and battery temperature 
affect calendar ageing. From Figure 6 it is observed that a 
higher battery temperature along with high levels of SoC 
increases the rate of capacity loss. Here, the relative capacity is 
a measure of the battery capacity relative to its initial capac-
ity. Comparing the effects of the two stress factors causing 
calendar ageing, it has been found that temperature has a 
more detrimental effect on the rate of degradation than SoC 
levels (Grolleau et al. 2014). In addition, the rate of degrada-
tion does not increase steadily with increasing SoC levels, 
as seen in Figure 6, that is the capacity loss remains almost 
the same for SoC levels, ranging between 40 and 70 percent 
(Keil et al. 2016).
Figure 6  |   Effect of temperature and SoC on LFP battery capacity (cell level)  
Source: Keil et al. 2016.
100 20 30 40 50 60 70 80 90 100
Storage SoC (%)
Before storage 25/o.supsC 
9 months
40/o.supsC 
9 months
50/o.supsC
9 months
0.80
0.85
0.90
0.95
1.00
1.05
Relative capacity
Figure 5  |  Different conditions affecting battery life  
Battery life
Parking/StandbyDriving Charging
Temperature
State of charge
(SoC)
Depth of discharge
(DoD)
Charge/discharge
rate (C-rate)
Temperature
Charging rate
(C-rate)
State of charge
(SoC)

WORKING PAPER  |  January 2024  |  13
Real-world electric bus operation: Trend in technology, performance, degradation, and lifespan of batteries
Cyclic ageing
The degradation occurring in batteries when they are being 
charged (during charging condition) or discharged (during 
EV usage) causes cyclic ageing. The rate of this degradation 
varies depending upon factors such as charge/discharge rates 
(C-rate), the temperature of the battery during usage, and the 
depth of discharge (DoD). 
Factors affecting cyclic ageing during charging 
During charging conditions, the rate of charging and tem-
perature become key factors for cyclic degradation. Fast 
charging of the batteries (high C-rate) leads to higher rates 
of cyclic degradation. In NMC batteries, fast charging can 
reduce battery life by 10 percent (Bhagavathy et al. 2021). 
The impact of fast charging on the distance that the e-buses 
can travel before the battery`s end-of-life (EoL) is shown 
in Figure 7. The reduction in drivable distance before EoL 
is due to large capacity loss (a measure of high degradation) 
caused by fast charging. It’s also observed that charging EV 
batteries at extreme temperatures accelerates cyclic degrada-
tion. Ouyang et al. (2016) observed that among the two stress 
factors mentioned, low temperature had a greater impact on 
cyclic ageing compared to high C-rates, as the uniformity of 
the battery deteriorates due to differences in temperature and 
voltage rates (Ouyang et al. 2019). In addition, although a bat-
tery with a higher SoC variation (0–100%) provides a higher 
drive range per charge in the short term than one charged to 
optimal SoC level, the degradation increases drastically with 
an increase in the range of SoC variation or over-discharge of 
the battery, as seen in Figure 8. 
Factors affecting cyclic ageing during driving 
According to a laboratory-accelerated ageing test, the 
internal temperature of the battery increases with a high 
rate of charge/discharge —caused due to driving speed and 
acceleration—leading to faster cyclic ageing of the battery 
Figure 7  |   Effect of temperature and charging type on total drivable distance before end of life of an NMC battery 
(pack level)  
Source: Liu et al. 2020.
0
20
40
60
80
100
0 10 20 30 40
Distance before EoL (in 1000km)
Ambient temperature (°C)
Fast charging Slow charging

14  |  
  
Figure 8  |   Battery life of an LFP variant at different SoC windows (pack level)  
Source: Jiang et al. 2013
0
4
8
12
16
20
0 100 200 300 400 500 600
Degradation (%)
Cycle life
Over discharge
0-20%
Optimal
20-80%
High SoC
80-100%
0-100%
batteries, as observed by Chinese e-bus manufacturers Yutong 
group, falls drastically with increasing temperature; that is it 
takes 4,000 cycles for the battery to reach its end of first life 
at 25°C while only around 2,000 cycles to reach end of first 
life (i.e., 80 percent capacity) at 45°C. In an NMC battery, the 
number of cycles before the end of the first life decreases from 
1,200 cycles at a temperature of 34°C to 500 cycles at 46°C 
(C40 Cities 2021).
Batteries in EVs have a risk of high degradation in opera-
tional conditions like higher temperatures, dynamic loads, 
and overcharging and discharging patterns, posing concerns 
about battery life and safety. These factors in a tropical region 
generate a large amount of heat in a battery with up to 10°C 
variations between the core and surface levels, triggering bat-
tery ageing and thermal runaway (Samanta and Williamson 
2021). Recent evidences suggest that such uncontrollable 
thermal runaways can lead to EV batteries catching fire (Shah 
2022). To regulate the temperature within the optimal range 
(Tomaszewska et al. 2019). In addition, over-discharging 
of the battery (high DoD) leads to an accelerated rate of 
degradation and capacity loss as shown in Figure 8. A 
regenerative braking system (RBS) is introduced to improve 
energy efficiency in e-buses, maintaining optimum SoC level, 
and avoiding deep DoD or frequent charging requirements. In 
contrast, high charging currents and longer duration of current 
flow due to RBS can lead to lithium plating, which increases 
ageing (Chidambaram et al. 2023). Therefore, the ratio of 
regenerative braking must be controlled to optimize benefits, 
increasing both energy efficiency and battery lifespan. 
Battery life in a tropical environment 
Lithium-ion battery variants are highly temperature sensitive, 
which means the degree of variability between the ambient 
and the ideal operating temperature of the battery plays a 
major role in the total rate of degradation. Figure 9 shows 
the effect of temperature on battery life. The cycle life of LFP

WORKING PAPER  |  January 2024  |  15
Real-world electric bus operation: Trend in technology, performance, degradation, and lifespan of batteries
Figure 9  |   Effect of temperature on LFP battery life (pack level)  
Source: Yutong n.d.
80
85
90
95
100
0 1000 2000 3000 4000
SoH (%)
Cycle no.
45/o.supsC 25/o.supsC
of 15–35°C, (Ma et al. 2018) an efficient battery thermal man-
agement system (BTMS) that operates on the commands of 
the battery management system (BMS) is required for either 
heating or cooling the battery, which is important for increas-
ing the lifetime of a battery.
Among the various BTMSs, a combined liquid cooling system 
is more suitable for tropical regions to control the battery 
temperature, as shown in Figure 10 (Bhatia 2020). It utilizes 
active as well as passive cooling systems to maintain the 
optimal battery temperature under extreme conditions with 
minimum energy consumed (Li and Zhu 2014). Piao et al. 
Figure 10  |   Comparison of different types of battery thermal management systems  
Source: Piao et al. 2020.
30
29
31
32
0 500 1000 1500 2000 2500 3000
Battery temperature (/o.supsC) 
Time (sec.)
No cooling Passive liquid
cooling
Combined liquid
cooling

16  |  
  
Figure 11  |   Annual battery capacity loss of an LMO battery pack in the USA   
Source: Yang et al. 2018.
2
0
4
6
8
Annual degradation (%) 
Years
1 2 3 4 5 6 7 8 9 10
Calendar loss Cyclic loss
tion due to calendar ageing is dominant in the first year and 
keeps reducing over time whereas degradation due to cyclic 
ageing reduces marginally through the life of the battery (seen 
in Figure 11). The degradation trend followed by calendar 
ageing is due to the formation of a solid electrolyte interphase 
(SEI) layer (SEI layer  is formed due to an electrochemical 
reaction between the electrode and the electrolyte), which 
initially causes high capacity fading but protects the electrodes 
from faster degradation in the later stages, reducing the 
share of calendar ageing in the subsequent years (Molaei-
manesh et al. 2021).
Another study by Yang et al. (2018) presents the year-wise 
degradation of an e-car battery due to both cyclic and calendar 
ageing in different states of the USA. The study concludes that 
calendar ageing in a low-temperature region like Alaska is just 
18.02 percent over 10 years, whereas in a high-temperature 
state like Hawaii, it is 39 percent. This shows that there’s a 
correlation between ambient temperature and the rate of 
calendar ageing in LMO batteries.
LFP battery pack 
The degradation trend of an LFP battery variant can be 
understood by analyzing e-buses deployed in China, as shown 
in Figure 12. These battery packs operate in different geo-
graphical regions with varying temperature conditions. It can 
be observed that in an e-bus operating in Zhengzhou where 
the average ambient temperature ranges between 0 and 30°C, 
(2020) revealed that combined liquid cooling saved twice the 
amount of energy against using only active cooling and main-
tained the battery’s temperature under desired range. Despite 
reduced battery degradation, the BTMS requires technologi-
cal innovation to contain space consumption, increase in EV 
weight, and reduction in battery pack energy (Wankhede et al. 
2022). It is noteworthy that though the BTMS can increase 
the battery pack costs by 3–7 percent, it decreases the life cycle 
costs by 27 percent (Lander et al. 2021).
Battery degradation trends in different 
LIB variants 
The thermolabile nature of batteries can be understood by 
assessing the pack-level behavior of different battery variants 
under different scenarios. Taking inspiration from available 
data on the LMO variant, we assessed the contribution of 
calendar and cyclic ageing in battery degradation. We also 
studied real-world and extrapolated data to infer degradation 
trends of LFP , NMC, and L TO batteries. Later in this section, 
we examine the life of these battery variants being operated in 
the same external conditions to understand their suitability—
best to worst—in e-buses.
LMO battery pack
A case study by Yang et al. (2018) presents the trend of annual  
battery capacity loss of the LMO battery variant in real-world 
operating scenarios. The study highlights that the degrada-

WORKING PAPER  |  January 2024  |  17
Real-world electric bus operation: Trend in technology, performance, degradation, and lifespan of batteries
Figure 12  |   Battery degradation trend of LFP battery pack in e-buses  
Source: Li et al. 2020 ( Applied Energy ); Li et al. 2020 ( ACM Digital Library ).
10
5
0
15
20
25
0 200 400 600 800 1000 1200 1400 1600 1800 2000
Degradation (%) 
Days
Shenzhen
15-30/o.supsC
Linear extrapolation 
(Shenzhen 15-30/zero.numrC)
Linear extrapolation
(Zhengzhou 0-30/zero.numrC)
Zhengzhou
0-30/o.supsC
the battery pack reaches its end of life within approximately 
900 cycles or 2.5 years (Li et al. 2020, Applied Energy), falling 
short compared to the life claimed by the manufacturers. On 
the contrary, in the e-buses operating in Shenzhen where the 
average temperature ranges between 15 and 30°C (battery 
optimal temperature) (Climates to Travel 2022), batteries 
have an average life of five years (Li et al. 2020, ACM Digital 
Library), inferring that lower ambient temperature than the 
operable range has a large impact on LFP battery degradation. 
Cyclic ageing is one of the key reasons for such degradation at 
lower temperatures.
NMC and LTO battery packs 
A 310 kWh NMC battery pack and a 90 kWh L TO battery 
pack by battery manufacturer BMZ, Poland, were analyzed 
and the rate of degradation was compared in both the vari-
ants (Sustainable Bus 2021 A). It is observed that the NMC 
battery pack reaches 80 percent of its capacity in around eight 
years compared to the L TO battery pack which lasts beyond 
10 years, indicating that the L TO variant has comparatively 
higher battery life. In addition, from Figure 13 it can be 
observed that like other LIB variants, the degradation rate 
is highest in the initial years of the automotive life of NMC 
and L TO batteries.
While the obtained degradation curves may help in develop-
ing battery life models, one cannot compare the battery life of 
these three variants solely on the degradation curves as these 
battery packs have been used under dissimilar stress condi-
tions that were not disclosed by the manufacturer.
Comparison of LIB variants under the 
same conditions
Operational data under similar conditions are needed for 
comparing different battery chemistries. A case study was 
carried out by Al-Saadi et al. (2022) in Europe, based on a 
simulation of real driving cycles of e-buses with LFP , NMC, 
and L TO battery variants used in three European cities. Three 
cities with different temperatures, charging frequencies, and 
load demands were considered for analyzing and compar-
ing the rate of degradation in these variants. In addition, the 
study also highlights the stress factor causing the highest 
degradation. The three cities with their specific conditions are 
given in Table 6.

18  |  
  
Figure 13  |   Comparison of battery degradation trends of NMC and LTO battery packs  
Source: Sustainable Bus 2021 A.
15
10
5
0
20
25
30
0 1 2 3 4 5 6 7 8 9 10
Degradation (%) 
Years
NMC LTO
Table 6  |  Different study conditions for analyzing battery behavior  
SPECIFICATION BARCELONA (BCN)
SCENARIO A
OSNABRUCK (OSN)
SCENARIO B
GOTHENBURG (GOT)
SCENARIO C
Bus line L33 N5 R55
Average operational trip distance/day (km) 155 195 167
Maximum/Minimum temperature (°C) 29/9 23/0 22/-2
Characteristics Low demand
Low charging frequency
Warm climate
High demand
Medium charging frequency
Cool climate
High demand
High charging frequency 
Cool climate
Source: Al-Saadi et al. 2022.
The degradation rate obtained after the first year for different 
battery variants operating under the above-mentioned condi-
tions and varying C-rates is shown in Table 7. 
From Table 7, the following observations are made:
 ▪ NMC batteries suffer the highest degradation in scenario 
A where the batteries are deep discharged to utilize low 
charging frequency, implying that NMC batteries are 
the most sensitive to DoD. Therefore, an NMC bat-
tery pack should be operated at a lower DoD than a 
comparable LFP .
 ▪ Compared to other chemistries, C-rate contributes more 
to the degradation of NMC variants. For instance, a 
2.25 times increase in the degradation rate of NMCs is 
observed in scenario A while the change is negligible in 
the LFP and L TO variants.
 ▪ Under moderate temperatures, reduction in DoD due 
to the introduction of en-route charging (high fre-
quency charging) improved battery life. This can be 
seen in scenario C, which experiences frequent charg-
ing requirements.

WORKING PAPER  |  January 2024  |  19
Real-world electric bus operation: Trend in technology, performance, degradation, and lifespan of batteries
Table 7  |  Degradation results of different lithium-ion battery variants with varying C-rates  
SCENARIOS 1C 2C 3C
Degradation after 1-year (%)
LFP NMC LTO LFP NMC LTO LFP NMC LTO
Scenario A 2.76 4.00 1.00 2.76 6.59 1.10 2.76 9.00 1.20
Scenario B 2.97 5.10 1.10 2.97 6.30 1.20 2.97 7.90 1.30
Scenario C 2.49 4.90 0.98 2.49 5.49 1.00 2.50 6.50 1.1
Source: Al-Saadi et al. 2022.
Figure 14  |   Battery life in e-bus application at 80% SoH at different degradation rates  
Source: Authors' analysis.
84
80
88
92
96
100
0 1 2 3 4 5 6 7 8 9 10
Remaining capacity (%) 
Years
DR=1% DR=3% DR=5% DR=7% DR=9%
 ▪ Under the given scenarios, L TO batteries lasted the lon-
gest before reaching its EoL, followed by the LFP , with 
NMC batteries having the shortest lifespan.
In e-buses, once the batteries degrade by 20 percent of their 
initial capacity and have more than 5 percent self-discharge 
over 24 hours, they are no longer suitable for automotive 
applications. Given that batteries degrade over their lifespan, it 
is imperative to find out the degradation rate under which the 
ideal battery life can be achieved. Figure 14 shows the life of 
a battery at different average annual battery degradation rates. 
The trend suggests that approximately seven years of battery 
life can be achieved at an average of 3 percent annual degra-
dation rate, whereas a 9 percent average annual degradation 
rate can limit the battery life to less than three years. Having 
established that the degradation rate is highly susceptible to 
external factors, it is important to limit the battery’s exposure 
to them to achieve optimum battery life for e-bus applications.
Key observations for Indian operating 
conditions
As discussed, India experiences varied climatic conditions 
ranging from a hot tropical climate to cold and sub-zero 
temperatures. In order to limit the average annual degradation 
rate to less than 3 percent, factors contributing to degradation 
in a particular region must be identified and best practices

20  |  
  
must be implemented to maintain good battery health. 
Calendar ageing will be more dominant in regions with higher 
ambient temperatures, especially in the e-buses running at a 
higher SoC. Since temperature is a major stress factor for the 
degradation of batteries in tropical regions, a combined liquid 
cooling BTMS must be installed to maintain the optimal bat-
tery temperature range. In regions with ambient temperatures 
lower than optimum, cyclic ageing will cause lithium plating 
and loss in lithium inventory, leading to battery degradation 
(Lander et al. 2021). Wrapping the batteries with insulation 
material will help batteries warm up faster, reducing battery 
degradation at lower temperatures. Cyclic ageing is further 
triggered by high charging rates, high DoD (100 to 0 percent), 
and extreme operating temperatures. Degradation due to 
calendar ageing after the initial years of EV operation reduces 
substantially for batteries due to the formation of a protective 
SEI layer, whereas degradation due to cyclic ageing sees only a 
slight reduction over the years.
LFP and NMC variants are the popular batteries for EV 
applications in India. Degradation in the LFP variants is 
temperature driven to an extent while degradation in NMC 
batteries is highly impacted by C-rate. Compared to LFP , 
NMC variants under the same operating conditions degrade 
faster when operated at higher DoD, higher temperatures, and 
high C-rates.  While LFP variants are suitable for shorter dis-
tances with opportunity charging facilities, NMCs are suitable 
for longer distances with overnight slow charging.
IMPACT OF HIGH BATTERY 
DEGRADATION 
This section discusses the impact of degradation on opera-
tional factors such as battery sizing and range estimation, 
operational efficiency, and replacement ratio, and how it affects 
economic viability and sustainability of e-bus business models.
Short-term impact of battery 
degradation
The usage of an e-bus battery under non-optimal conditions 
of temperature, SoC, DoD, and charge/discharge rate (C-rate) 
leads to fast degradation in the original capacity of e-buses, 
affecting the planned operational schedule of an e-bus. High 
battery degradation will have an immediate impact on the 
following components:
Battery sizing and range estimation
A bus operator selects an e-bus technical specification, 
including battery capacity, based on the route requirement 
and charging strategy. For instance, an e-bus operator would 
choose a large battery size with an overnight charging strategy 
that is adequate to cover the planned trip over a small battery 
pack to cover the same route. Adequate range estimation can 
be hindered by higher degradation as it leads to reduction in 
the battery capacity, which makes it inadequate to complete 
the planned trip. 
The usable capacity of an e-bus is set at 70–80 percent of 
the nameplate capacity to avoid degradation due to aggres-
sive DoD. The energy consumption of an e-bus, as quoted 
by Indian OEMs, ranges between 0.8 and 2 kWh/km (Das 
et al. 2019). It must be noted that these values can change in 
regions with high and low temperature extremes due to the 
change in auxiliary power requirements for air-conditioning, 
heating, etc. Due to the variation in mileage, the operational 
range per charge changes compared to scheduled trip distance. 
Additionally, as the battery capacity fades due to accelerated 
degradation, driving range per charge is further reduced, 
requiring an additional number of charging cycles to finish 
a day’s trip. This was observed in a study done by McGrath 
et al. (2022) that concluded that the e-bus drive range per 
charge decreased by 26 percent during its automotive life 
due to accelerated capacity fade. The study also concluded 
that the energy required to cover the same route increased 
by 7 percent, suggesting a decline in energy efficiency. Under 
such conditions, along with the increased charging require-
ments, the batteries may require replacement long before the 
ideal time, which will further worsen the economic viability 
of the e-buses.
Operational efficiency (city level) 
E-buses with high battery degradation become less service-
able due to increased charging requirements. This has a major 
impact on the operational efficiency of the fleet. Moreover, 
routes with lower passenger movement don’t have backup 
vehicles deployed. Therefore any reduction in the range or 
high energy demand due to high battery degradation will lead 
to the unavailability of buses, directly impacting the e-bus 
scheduling process for a given route. 
Replacement ratio of conventional buses to 
e-buses (route level) 
Replacement ratio in this context refers to the share of e-buses 
required to obtain the same fleet operational efficiency as 
that of a diesel bus fleet. Cities must be able to achieve a 
replacement ratio close to 1:1 for better economic viability of 
e-bus fleets. The replacement ratio is based on the operational 
efficiency of e-buses, which is influenced by battery size, drive 
range estimation, and charging strategy (Xue et al. 2019). As 
established, high battery degradation impacts these factors, 
requiring the deployment of more e-buses by the opera-
tor than the replacement ratio set while planning the fleet 
electrification. Apart from controlling the degradation rate

WORKING PAPER  |  January 2024  |  21
Real-world electric bus operation: Trend in technology, performance, degradation, and lifespan of batteries
Figure 15  |   Effect of battery size on TCO per km  
Source: Kumar and Chakrabarty 2020.
20
0
40
60
80
TCO (Rs/km) 
Bus type
12m, AC, BB 12m, AC, SB AC, High-end AC, Low-end
7 7. 75
53.77
78.57
61.64
E-bus Diesel bus
in batteries, the San Tiago model for improvement in opera-
tional efficiency can be explored for achieving 1:1 replacement 
ratio. The city improved its operational efficiency by identify-
ing the right charging strategy, which included adoption of 
faster combined charging systems (CCSs) and development of 
e-bus corridors with bus-terminal charging facilities, in addi-
tion  to taking city-specific technical specification of range, 
charging speed, and vehicle downtime into consideration ( Jin 
2020; Allan et al. 2021). 
Long-term impact of battery 
degradation 
The long-term impact of battery degradation is directly linked 
to the economic viability and sustainability of the e-bus busi-
ness model discussed below:
Economic viability of the e-buses 
A financial analysis is of key importance to determine future 
savings and enable the e-bus fleet managers to understand the 
return on investment despite higher upfront costs compared 
to that of conventional buses ( Johnson et al. 2020). The TCO 
analysis is one of the methods to assess the financial viability 
of e-buses. On determining the TCO per km, fleet managers 
will be able to analyze the net earnings per km by transition-
ing to e-buses.   
Figure 15 shows that the TCO per km of a 12 meter AC 
e-bus with a big battery pack (12 m_AC_BB) is less than the 
high-cost diesel counterpart but higher than the low-cost 
diesel variant for the average daily travel distance of 200 km. 
With nearly a 40 percent reduction in the battery pack size 
(320 kWh to 125 kWh), the TCO per km of 12 meter AC 
e-bus with a small battery pack (12m_AC_SB) becomes even 
less than the low-cost diesel variant, showing the impact of 
battery cost on the economic viability of e-buses. Higher 
degradation rates can lead to the battery reaching its end of 
first life faster, causing frequent battery replacements to meet 
operational efficiency.
Another study carried out by MOBI Electromobility Research 
Centre, Brussels, compared the impact of the reduced battery 
life of public e-bus on the TCO for 10 years. They concluded 
that as the battery lifespan reduced by 40 percent, the TCO of 
the e-bus increased by 4.3 percent, compared to the TCO for 
rated capacity of the e-bus battery. Moreover, the impact of 
degradation on TCO of e-buses using depot charging strategy 
was found to be higher than those using opportunity charging. 
(Nils et al. 2019). The increase in TCO due to high degrada-
tion (reduced battery lifetime) impacts the economic viability 
and the sustainability of the e-bus business model.

22  |  
  
Operational cost 
At the route level, fuel efficiency and the distance traveled 
per day largely impact the TCO per km of an e-bus. A case 
study carried out by Nurhadi et al. (2014) on a public e-bus in 
Sweden concluded that the TCO increased by 13–30 percent 
as the driving range of the e-bus decreased by 10–30 percent. 
Moreover, higher degradation impacted the operational  
efficiency at the route level, incurring additional costs to 
purchase more buses to meet the operational efficiency of the 
diesel bus counterpart.  
Zhang et al. (2022) observed that considering only charging 
costs resulted in an unsustainable charging strategy solution, 
as the e-bus operator would wait for the time when the cost 
of charging is lower in the power supply grids. This resulted 
in e-buses reaching very low levels of SoC (high DoD), 
leading to high wear costs (due to high degradation) and 
frequent battery replacement. Ineffective charging scheduling 
increases battery wear, further increasing the operational cost 
of e-buses by 21.79 percent, compared to the case where an 
optimal charging strategy was adopted to reduce battery wear 
cost. From the above observations, it can be concluded that 
battery wear cost is an integral part of the operational cost 
of the e-buses and thereby the economic viability of e-buses. 
For e-buses having big battery packs with high flexibility for 
overnight charging (depot charging) durations, the com-
bined consideration of charging costs and battery wear costs 
provide enhanced outcomes. The cost of battery replacement 
and the affected operational cost (city and route level) due to 
the immediate impact of battery degradation will affect the 
sustainability of the business model in the long run, making it 
difficult for fleet owners to hit the break-even point. 
SUMMARY AND WAY 
FORWARD 
The battery life of an e-bus plays a significant role in its 
performance, economic viability, and sustainability of the 
business model. Batteries undergo degradation due to calendar 
and cyclic ageing which is accelerated by various operat-
ing conditions like temperature extremes, high charge rate 
and DoD, and load demands. In order to obtain an optimal 
battery life in e-buses, the following selected recommenda-
tions are proposed:
Operational recommendations 
State of charge and temperature management
T o reduce degradation during standby/parking or storage 
conditions: Calendar ageing in batteries is accelerated at high 
SoC levels (>50 percent) and elevated temperatures (beyond 
35°C). Hence, fully charged e-buses should not be parked for 
a long time in high-temperature conditions. Parking charged 
e-buses under shade during long halts can help keep the 
battery temperature close to optimum conditions. Moreover, 
while storing charged batteries, exposure to sunlight and 
extreme temperature fluctuations must be avoided.
Charging and discharging strategy
T o reduce battery ageing during driving conditions: Cyclic 
ageing during operation is accelerated by deep DoD and 
temperature extremes. Ensuring partial discharge of the 
battery during operation, which is around the SoC range of 
20–80 percent, and the lowest average SoC can reduce the 
rate of cyclic ageing. Factors such as aggressive driving and 
high payload capacity accelerate cyclic ageing, wearing out the 
batteries faster, and hence must be avoided. 
Reducing ageing during charging conditions: An e-bus 
battery should always be charged at the optimum temperature 
range (15–30°C) to avoid cyclic ageing. Prolonged charging at 
lower temperatures leads to high heat generation, increasing 
battery degradation. Therefore, batteries should be charged 
at a lower C-rate for lower temperature conditions (0–15°C), 
and below-freezing point charging should be avoided for 
enhanced battery life.
As cyclic losses almost double when the battery is overcharged 
(beyond 80 percent SoC), the e-bus should be charged 
between 20 and 80 percent SoC. Moreover, frequent direct 
current (DC) fast charging generates more heat than slow 
charging, increasing battery wear and tear. Avoiding frequent 
DC fast charging preserves the battery life by 10 percent. 
Depot charging combined with opportunity charging is 
recommended for e-buses operating for longer distances, as it 
helps avoid cycling of batteries outside optimal SoC and DoD 
levels, thus reducing the rate of cyclic degradation.
Planning recommendations 
Battery sizing and charging strategy: The battery must 
be sized for a required average daily driving distance on a 
single charge, considering the specific energy consumption 
(estimated) of the bus route of the city of operation. To avoid 
oversizing of battery pack for meeting the route require-
ment, overnight depot charging and optimal scheduling can 
be adopted for short distances (e.g., 150 km/day). Overnight 
charging with opportunity charging (at the terminal) can be 
adopted for longer distances to ensure the smallest SoC varia-
tion or low average SoC level of battery packs.  
Degradation and opportunity charging cost in TCO estima-
tion: Battery wear costs and opportunity charging costs must 
be considered instead of charging cost alone when determin-
ing an ideal and financially sound charging strategy.

WORKING PAPER  |  January 2024  |  23
Real-world electric bus operation: Trend in technology, performance, degradation, and lifespan of batteries
Circular economy in e-bus business models: E-bus batteries 
are unfit for automotive use after losing 20 percent of their 
initial capacity but have sufficient capacity for other energy 
storage applications. OEMs should improve data collec-
tion for precise residual value calculation of these batteries 
to identify their fitness for various second-life applications. 
Refurbishing and recycling of the retired batteries will not 
only improve the environmental impact of the batteries but 
will also add a revenue stream to the business model, reducing 
the TCO per km of e-buses.
Driver training: EVs have limited driving range, where 
aggressive driving accelerates energy consumption. An 
increase in top-up (fast) charging requirements to finish the 
desired trips by e-bus due to high energy demand can increase 
battery capacity fade and charging costs. Intelligent fleet 
monitoring and optimal driver behavior during operation can 
play a critical role in promoting economical driving. 
Given e-buses are relatively new technology for drivers, 
OEMs must give systematic training to build the drivers’ 
knowledge about e-buses and their components. Moreover, 
eco-driving trainings have proved to improve energy efficiency, 
maintain battery health, and reduce opex. With respect to the 
route drive cycle, bus operators can build training modules 
on optimal management of speed, acceleration, deceleration, 
use of regenerative brakes, and charging en-route and at the 
depot. Drivers must also be trained in maintaining the optimal 
SoC during standby and charging, DoD during opera-
tion, and charge with desired C-rate to avoid loss of cycle 
life of batteries.
Technical recommendations 
Efficient BMS and TMS for battery: Given the high impact 
of non-optimal temperature on battery life, e-bus battery 
packs must be equipped with the intelligent BMS. This will 
help monitor and protect cells and battery pack. Intelligent 
BMS will help minimize safety concerns and will help moni-
tor and record the change in the battery health (i.e., SoH) of 
the battery due to various external factors.  
In regions that experience high temperatures, a combined 
cooling liquid battery thermal management system (BTMS) 
must be adopted to maintain battery temperature in the 
optimal range (i.e., 15–35°C) to reduce battery degradation. In 
low-temperature regions, the use of insulation material (IM) 
can help in warming up the batteries with a reduced decay 
rate and improve the discharging performance. This can help 
in achieving lower cell and pack-level degradation. Optimiza-
tion at the cell design level to promote better heat dissipation 
and thermal management can reduce battery degradation, 
which could extend the battery life, and hence reduce bat-
tery wear costs.
Regenerative braking system adoption: In an e-bus, efficient 
utilization of the regenerative braking system (RBS) can be 
one of the solutions to manage the uncertainty in the energy 
consumption per km due to varying operating conditions. 
RBS in an e-bus, especially in congested cities with frequent 
braking requirements, can help recharge the battery using 
kinetic energy generated during deceleration. It is to be noted 
that regenerative braking alone cannot bring down a speeding 
vehicle to zero speed. Therefore, it should be coupled with 
friction brakes to bring the vehicle to zero speed. RBS must 
be designed to minimize battery capacity loss due to cyclic 
ageing under the high rate of current delivered to the battery 
by regenerative braking.
T echnical performance and efficiency: In e-buses, auxiliary 
requirements account for almost 50 percent of the total energy 
consumption per km and contribute significantly to the uncer-
tainty of the energy consumption per km due to variations 
in the local operating conditions. To optimize energy usage 
for auxiliary requirements, the e-bus must be equipped with 
an intelligent energy management system to monitor and 
regulate energy demands with changing temperatures. Also, 
an energy-efficient heating, ventilation, and air-conditioning 
(HVAC) system must be used in e-buses. 
E-buses must be equipped with an eco-driving assistance 
system (EDAS), which can help to extend the range up to 30 
percent by efficient energy utilization. Along with the regen-
erative braking system (RBS), e-buses should adopt a smart 
control strategy for the efficient utilization of the recovered 
energy. Improving energy efficiency will help avoid high 
DoD during trips, reducing the need for top-up charging and 
reducing battery degradation.
Policy recommendations 
Battery data collection and management: A major limitation 
for developing various battery ageing management strategies 
is the unavailability of region-specific, pack-level, real-world 
operational data on e-bus batteries. Different regions have 
different temperature conditions, driving behaviors, and other 
external conditions, which can affect battery life differently. 
Region-specific multi-stakeholder partnerships need to be 
developed for gathering and transferring real-world data. 
To overcome the data gap in India, e-bus OEMs and opera-
tors need to develop a mechanism for collecting and securely 
sharing real-time data for analysis, in order to identify 
region-specific battery issues. Annex B suggests a template 
for data collection, where the data collection frequency can be 
fixed based on the trade-off between cost and benefit analysis 
of data collection and management. Some of the possible 
analysis and its benefits are listed below:

24  |  
  
 ▪ Battery life assessment: The availability of data will 
improve understanding of the various battery health 
indicators for different chemistries during their automo-
tive lifetime. This will help in assessing the role of various 
external stress factors in catalyzing degradation by both 
calendar ageing and cyclic ageing in different bat-
tery chemistries.
 ▪ Efficient planning for operation: A better understanding 
of battery life can lead to the development of best operat-
ing practices and innovative solutions to minimize battery 
degradation in various operating situations. 
 ▪ T echnology development: An understanding of region-
specific factors of e-bus battery degradation, which can  
foster technical innovation such as best-suited temp- 
erature controllers for maintaining the health of differ-
ent battery packs.
 ▪ Residual value and second life: Availability of data 
about cell and pack health will help estimate precisely the 
end-of-life residual value of the e-bus battery. This will 
play a crucial role in estimating the intrinsic value of the 
battery and its suitability for either second life application 
or EoL recycling.
Standards, regulation, and testing: With the availability of 
region-specific data on major factors affecting battery degra-
dation, fit-for-purpose standards can be introduced in place 
of current battery standards. For example, in batteries manu-
factured for e-buses operating in India, the fit-for-purpose 
standards will match the environmental conditions (tem-
perature, humidity) and abuse conditions (aggressive C-rates, 
DoD, physical damage), and actual operating circumstances 
in the country. 
Battery durability testing under these standards can precisely 
estimate battery ageing and impact on cycle-life of the e-bus 
batteries in specific regions. Durability testing will yield 
further data on possible battery-related accidents, helping 
manufacturers take adequate safety measures.

WORKING PAPER  |  January 2024  |  25
Real-world electric bus operation: Trend in technology, performance, degradation, and lifespan of batteries
ANNEX A. BASIC TECHNICAL 
DETAILS
List of key performance indicators (KPIs) 
 ▪ Battery capacity (Ampere.hour):  The total amount of 
electricity produced from the electrochemical reactions that 
occur inside a battery throughout its lifetime determine its 
total capacity.
 ▪ Specific energy density (kWh/kg): It is the amount of 
energy a battery contains per kilogram of its weight.
 ▪ Charge/discharge rate (C-rate):  It refers to the rate at 
which current is being drawn from or to the battery, whereas 
the depth of discharge refers to the extent to which a fully 
charged battery is being discharged.
 ▪ Cycle life:  Cycle life is the number of full charge and 
discharge cycles a battery can go through before dropping to 
80 percent state of health (SoH).
 ▪ Driving range:  Driving range depicts the distance an e-bus 
can drive per charge cycle.
 ▪ Operable temperature range:  It is the range of ambient 
temperature in which a battery can operate optimally.
Factors affecting battery degradation 
External factors play a major role in battery degradation as they 
lead to various side reactions (degradation mechanisms) resulting 
in either of the three degradation modes leading to quantifiable 
effects on battery in terms of either capacity or power fade as 
shown in Figure A1.
Causes of degradation 
Temperature: High temperature results in thermal decomposition 
of the electrode and the electrolyte, leading to increase in thickness 
of SEI film on the anode. This results in an increase in consumption 
of lithium ions, leading to capacity fade. A study by Xiong (2019) 
suggests that 25°C increase in temperature from 0–25°C resulted in 
just 2 percent capacity fade, whereas increase in temperature from 
25–40 °C resulted in an additional 10 percent capacity fade. Lower 
temperature results in side reaction due to lithium deposition, 
resulting in capacity fade and safety concerns (Xiong 2019).
State of charge (SoC): High SoC levels lead to an increase in 
the open circuit voltage, resulting in lower anode potential and 
higher cathode potential. Lower anode potential here leads to an 
Figure A1  |   Effect of factors leading to battery degradation  
Source: Birkl et al. 2017.
Time
High Temperature
Current Load
Low Temperature
Stoichiometry
Mechanical Stress
High V cell /SOC cell
Low V cell /SOC cell
Cause Degradation Mechanism Degradation Mode Eﬀect
SEI Growth
SEI Decomposition
Electrolyte 
Decomposition
Binder Decomposition
Graphite Exfoliation
Structural Disordering
Loss of Electric Contact
Electrode Particle 
Cracking
Transition Metal
Dissolution
Corrosion of Current
Collectors
Lithium Plating/
Dendrite Formation
Loss of Lithium
Inventory
Loss of Active
Anode Material
Loss of Active
Cathode Material
Capacity Fade
Power Fade

26  |  
  
increase in SEI growth and electrolytic oxidation, thereby resulting 
in a capacity fade. However, a very low SoC level also results in an 
increase in capacity fade and internal resistance of the cell, leading 
to power fade (Xiong 2019).
Depth of discharge (DoD):  Higher DoD or a deep discharge 
(DoD>50 percent) damages the negative electrode site, and the 
electrodes start to undergo phase change, resulting in structural 
and volume change. This then results in capacity loss (Xiong 2019).
Charge/discharge rate (C-rate):  High charge voltages increase 
the battery runtime while resulting in lithium plating and loss of 
lithium due to formation of metallic lithium on the anode. This 
causes capacity loss with a greater risk of fire within the cell due to 
internal short circuiting (Xiong 2019).
Degradation modes 
Loss of lithium-ion inventory:  Parasitic reactions such as SEI  
growth, decomposition reaction such as SEI and electrolyte 
decomposition, and lithium plating may lead to the unavailability of 
lithium ions cycling between the electrodes, resulting in a capacity 
fade (Birkl et al. 2017). 
Loss of active material of anode: This mode of degradation may 
result in capacity loss as well as power loss. Blocking of active 
site due to formation of resistive surface layer or loss of electrical 
contact and particle cracking may result in the unavailability of 
active mass of anode (Birkl et al. 2017).
Loss of active material of cathode: Loss of electrical contact 
or particle cracking and structural disordering may lead to this 
mode of degradation resulting in capacity as well as power loss 
(Birkl et al. 2017).
Counting battery cycle 
Battery warranty is mentioned in terms of number of battery 
cycles (full equivalent cycles) or years. Here, the battery cycles are 
calculated when the battery is subjected to a repetitive discharge-
and-charge cycle at a given DoD, C-rate, and temperature.
As we know, for realistic load profiles, a discharge/charge cycle 
may not always start/end with a battery SoC of 100 percent, so 
the concept of equivalent number of cycles is introduced. The 
equivalent number of cycles for a given DoD is defined as the 
number of cycles equivalent to the scenario where the SoC at the 
beginning and end of cycle is 100 percent (Motapon et al. 2020). 
For example, if the battery is discharged from 80 percent SoC 
(20 percent DoD) to 40 percent SoC (60 percent DoD) and then 
recharged to 60 percent SoC (40 percent DoD), the cycle’s DoD is 
60 percent and the equivalent number of cycles can be calculated 
by the formula given below:
Charge/discharge rate (C-rate)
The charge rate of batteries is calculated by taking into 
account the charger power and the battery capacity using the 
formula given below:
Figure A2  |  Calculating equivalent number of cycles   
Source: Motapon et al. 2020.
Partial discharge/charge
0
0
40
60
80
100
20
SoC (%)
Cycles
Time(s)
60% DoD
40% DoD
20% DoD
0% DoD
0.5
Neq
t1 t2
1.0
60% DoD discharge/charge
For example, consider a 15 kWh battery pack:
 ▪ 1C rate refers to pumping in 15 kW of charge resulting in a 
full charge in 1 hour. Here a charger power rating of 15 kW is 
required to charge at 1C.
 ▪ 2C rate refers to pumping in twice the charge—i.e., 30 kW. 
Therefore, the battery will be charged in 0.5 hours. Here, 
charger power rating of 30 kW is required to charge at 2C.
Charging at C-rate < 1C is termed slow charging, whereas charging 
at C-rate ≥ 1C is termed fast charging.

WORKING PAPER  |  January 2024  |  27
Real-world electric bus operation: Trend in technology, performance, degradation, and lifespan of batteries
Similarly, the discharge rate of batteries is calculated taking into 
account the power drawn by the vehicle and the battery capacity.
For example, consider a 15 kWh battery pack:
 ▪ If the vehicle requires 15 kW of power, it means that the 
battery is being discharged at a 1C rate. The battery would be 
completely discharged in 1 hour. 
 ▪ If the vehicle requires 60 kW of power, it means that the 
battery is being discharged at 4C. Therefore, the battery will 
be discharged in 0.25 hours.
ANNEX B. BATTERY LIFE 
ANALYSIS: DATA COLLECTION 
TEMPLATE
The performance and safety of electric vehicles (EVs) are 
greatly influenced by the state of their battery. Monitoring and 
understanding the battery performance under the influence of 
local driving, usage, and environmental conditions can help in 
developing a strategy to improve battery life and the economic 
viability of the vehicle. Following are templates to collect data for 
the battery life analysis. Note that the frequency of data collection 
can be decided based on the trade-off between the cost and 
benefit analysis of data collection and management.  
Table B1  |  Technical details  
TECHNICAL SPECIFICATION
Vehicle
Vehicle number/e-bus ID:
Bus type & dimension:
Assured range (km):
Battery
Capacity & chemistry:
BMS & TMS details:
Assured cycle life (n):
Charger
Charging standard: 
Number of chargers per bus (slow & fast):
Slow charger (kW):
Opportunity charger (kW):
Source: Authors’ analysis.
Table B2  |  Vehicle operational details  
MONTHS NO. OF DAYS AVERAGE AMBIENT
TEMPERATURE (°C) 
DISTANCE COVERED ( km) DRIVE CYCLE
Average/day Max/day Average speed  
(km/h)
Max speed
(km/h)
Stop time  
(en-route*)(hh:mm)
January
February
March
April
May
June
July
August

28  |  
  
MONTHS NO. OF DAYS AVERAGE AMBIENT
TEMPERATURE (°C) 
DISTANCE COVERED ( km) DRIVE CYCLE
Average/day Max/day Average speed  
(km/h)
Max speed
(km/h)
Stop time  
(en-route*)(hh:mm)
September
October
November
December
Note: *Stop time includes scheduled halts and the time for which vehicle attains ~0 km/hr speed due to braking when driving. 
Source: Authors’ analysis.
Table B3  |  Battery energy details  
MONTHS ENERGY ( kWh) SOC (%) BATTERY CAPACITY ( kWh) SOH (%)
Consumption
by battery
Generated 
from RB*
Average Maximum Minimum @100% SoC
January
February
March
April
May
June
July
August
September
October
November
December
Note: *Regenerative braking. 
Source: Authors’ analysis.
Table B4  |  Battery operational details  
MONTHS BATTERY POWER ( kW) BATTERY TEMPERATURE (°C) CHARGE RATE (C-RATE)
Average power Max. power Average Maximum Minimum Slow charging Opp. charging
January
February
March
April
May

WORKING PAPER  |  January 2024  |  29
Real-world electric bus operation: Trend in technology, performance, degradation, and lifespan of batteries
MONTHS BATTERY POWER ( kW) BATTERY TEMPERATURE (°C) CHARGE RATE (C-RATE)
Average power Max. power Average Maximum Minimum Slow charging Opp. charging
June
July
August
September
October
November
December
Source: Authors’ analysis.
Table B5  |  Charging details 
MONTHS AVERAGE CHARGING SESSION PER DAY ( HH:MM) AVERAGE ELECTRICITY CONSUMPTION PER BUS ( kWh)
Slow charging Opp. charging
January
February
March
April
May
June
July
August
September
October
November
December
Source: Authors’ analysis.

30  |  
  
ABBREVIATIONS
BCN  Barcelona
BMS  Battery Management System
BTMS  Battery Thermal Management System
CAGR  Compound Annual Growth Rate
C-rate  Charge/Discharge Rate
CTP  Cell to Pack
DoD  Depth of Discharge
E-bus  Electric Bus
EV  electric vehicle 
EDAS  Eco-Driving Assistance System
EoL  End of Life
EV  Electric Vehicle 
FAME  Faster Adoption and Manufacturing of  
                                (Hybrid &) Electric Vehicles 
GoI  Government of India 
GOT  Gothenburg
IEMS  Intelligent Energy Management System
ITDP  Institute for Transport and Development Policy
KPI  Key Performance Indicator
LFP  Lithium Iron Phosphate
LIB  Lithium-ion Battery 
LMO  Lithium Manganese Oxide
LTO  Lithium Titanium Oxide
NEBP  National Electric Bus Program
NMC  Lithium Nickel Manganese Cobalt
OEM  Original Equipment Manufacturer
OSN  Osnabrück 
PIB  Press Information Bureau
RBS  Regenerative Braking System
SEI  Solid Electrolyte Interphase 
SoC  State of Charge
SoH  State of Health
SRTUs  State Road Transport Undertakings
TCO  Total Cost of Ownership 
TMS  Thermal Management System
ENDNOTES
1. Regenerative braking converts a substantial portion of the kinetic 
energy lost during deceleration into stored energy of EVs by using 
the motor of the vehicle as a generator. This energy can be used in 
the future, improving the efficiency of a vehicle.

WORKING PAPER  |  January 2024  |  31
Real-world electric bus operation: Trend in technology, performance, degradation, and lifespan of batteries
REFERENCES
Allan, M., S. Turner, and T. Eisenberg. 2021. From Santiago to Shen -
zhen: How Electric Buses Are Moving Cities . Institute for Transporta -
tion and Development Policy. New York: ITDP. 
Al-Ogaili, A.S., A.Q. Al-Shetwi, H.M.K. Al-Masri, T.S. Babu, Y. Hoon, K. 
Alzaareer, and N.V.P. Babu. 2021. “Review of the Estimation Methods 
of Energy Consumption for Battery Electric Buses.” Energies  14 (22): 
7578. https://doi.org/10.3390/en14227578.
Al-Saadi, M., J. Olmos, A. Saez-de-Ibarra, J.V. Mierlo, and M. 
Berecibar. 2022. “Fast Charging Impact on the Lithium-Ion Bat -
teries’ Lifetime and Cost-Effective Battery Sizing in Heavy-Duty 
Electric Vehicles Applications.” Energies  15 (4): 1278. https://doi.
org/10.3390/en15041278.
Battery University. 2010. “BU-212: Future Batteries.” Battery 
University. September 4. https://batteryuniversity.com/article/bu-
212-future-batteries.
Baumann, M., J.F. Peters, M. Weil, and A. Grunwald. 2017. “CO 2 
Footprint and Life-Cycle Costs of Electrochemical Energy Storage 
for Stationary Grid Applications.” Energy Technology  5 (7): 1071–83. 
https://doi.org/10.1002/ente.201600622.
Beltran, H., P. Ayuso, N. Vicente, B. Beltrán-Pitarch, J. García-Caña -
das, and E. Pérez. 2022. “Equivalent Circuit Definition and Calendar 
Aging Analysis of Commercial Li(Ni xMnyCoz)O2/Graphite Pouch 
Cells.” Journal of Energy Storage 52 (A) (August).
Bhagavathy, S.M., H. Budnitz, T. Schwanen, and M. McCulloch. 2021. 
“Impact of Charging Rates on Electric Vehicle Battery Life.” Findings 
(March). https://doi.org/10.32866/001c.21459.
Bhatia, Shubhangi. 2020. “Tapping on EV Thermal Management 
Solutions for India.” ETAuto. June 23. https://auto.economictimes.
indiatimes.com/news/auto-technology/etautoevc-tapping-on-ev-
thermal-management-solutions-for-india/76529629.
Biczel, P.J., and M. Kwiatkowski. 2018. “Batteries in a Vehicle—
Conditions, Capabilities and Limitations.” Edited by A. Szeląg, K. 
Karwowski, H. Gold, and A. Żurkowski. MATEC Web of Conferences 
180: 03001. https://doi.org/10.1051/matecconf/201818003001.
Birkl, C.R., M.R. Roberts, E. McTurk, P.G. Bruce, and D.A. Howey. 
2017. “Degradation Diagnostics for Lithium Ion Cells.” Journal of 
Power Sources 341 (February): 373–86. https://doi.org/10.1016/j.
jpowsour.2016.12.011.
BYD. 2021. “BYD ADL Enviro200EV.” https://www.evbus.co.uk/wp-
content/uploads/2021/03/BYD-ADL-Enviro200EV.pdf.
BYD. 2022 ‘Bus: K7M - BYD USA’, https://en.byd.com/. Available at: 
https://en.byd.com/bus/k7m/
BYD. n.d. A. “BYD’s New Blade Battery Set to Redefine EV Safety 
Standards—BYD USA.” BYD USA. https://en.byd.com/?s=BYD%E2
%80%99s+New+Blade+Battery+Set+to+Redefine+EV+Safety+Sta
ndards. Accessed 2022. 
BYD. n.d. B. “BYD Receives Largest Battery-Electric Bus Order in 
U.S. History—BYD USA.” BYD USA. https://en.byd.com/?s=BYD
+Receives+Largest+Battery-Electric+Bus+Order+in+U.S.+Hist
ory. Accessed 2023
C40 Cities Finance Facility. 2021. Procurement of E-Buses (BRT 
Routes) by TransJakarta. Germany: C40 Cities Finance Facility. 
https://cff-prod.s3.amazonaws.com/storage/files/GMYXvg2BuYx -
wtf7gLh3X0RRfZq2oulLeEPjQ1r53.pdf.
Carrilero, I., M. González, D. Anseán, J.C. Viera, J. Chacón, and 
P.G. Pereirinha. 2018. “Redesigning European Public Transport: 
Impact of New Battery Technologies in the Design of Electric Bus 
Fleets.” Transportation Research Procedia  33: 195–202. https://doi.
org/10.1016/j.trpro.2018.10.092.
Chen, R. 2022. “Battery Pack Design of Cylindrical Lithium-Ion 
Cells and Modelling of Prismatic Lithium-Ion Battery Based on 
Characterization Tests.” https://macsphere.mcmaster.ca/bit -
stream/11375/27797/2/Chen_Ruiwen_202208_MASc.pdf.
Chidambaram, R.K., D. Chatterjee, B. Barman, P.P. Das, D. Taler, J. Ta -
ler, and T. Sobota. 2023. “Effect of Regenerative Braking on Battery 
Life.” Energies 16 (14): 5303. https://doi.org/10.3390/en16145303.
Climates to Travel. n.d. “Shenzhen Climate: Average Weather, Tem -
perature, Rainfall, Sunshine Hours.” https://www.climatestotravel.
com/climate/china/shenzhen.
Das, S., C. Sasidharan, and A. Ray. 2019. Charging India’s Bus 
Transport—a Guide for Planning Charging Infrastructure for Intra-
city Public Bus Fleet . New Delhi: Sustainable Energy Foundation. 
https://shaktifoundation.in/wp-content/uploads/2019/07/Full-
Report_Charging-Indias-Bus-Transport.pdf.
Dubarry, M., Q. Nan, and P. Brooker. 2018. “Calendar Aging of Com -
mercial Li-Ion Cells of Different Chemistries—A review.” Current 
Opinion in Electrochemistry  9: 106–13. https://doi.org/10.1016/j.
coelec.2018.05.023. 
Göhlich, D., T. Fay, and S. Park. 2019. “Conceptual Design of Urban 
E-Bus Systems with Special Focus on Battery Technology.”  
Proceedings of the Design Society: International Conference on  
Engineering Design 1 (1): 2823–32. http://dx.doi.org/10.1017/dsi.  
2019.289.

32  |  
  
Graurs, I., A. Laizans, P. Rajeckis, and A. Rubenis. 2015. “Public Bus 
Energy Consumption Investigation for Transition to Electric Power 
and Semi-dynamic Charging.” Engineering for Rural Development .  
https://www.tf.lbtu.lv/conference/proceedings2015/Pa -
pers/060_Graurs.pdf.
Grolleau, S., A. Delaille, H. Gualous, P. Gyan, R. Revel, J. Bernard, E. 
Redondo-Iglesias, J. Peter, and SIMCAL Network. 2014. “Calendar 
Aging of Commercial Graphite/LiFePO 4 Cell—Predicting Capac -
ity Fade under Time Dependent Storage Conditions.” J ournal of 
Power Sources 225 (June): 450–58. https://doi.org/10.1016/j.jpow -
sour.2013.11.098.
Hodge, C., M.A. Jeffers, J.D. Desai, E.S. Miller, and V. Shah. 2019. “Su -
rat Municipal Corporation Bus Electrification Assessment.” Office 
of Scientific and Technical Information, US Department of Energy. 
May 17. https://www.osti.gov/biblio/1515398.
Hooftman. N., M. Messagie, and T. Coosemans. 2019. “Analysis of 
the Potential for Electric Buses,” May 21.  https://www.slideshare.
net/sustenergy/analysis-of-the-potential-for-electric-buses.
IEA. 2022. Global Electric Vehicle Outlook 2022 . France: IEA. https://
iea.blob.core.windows.net/assets/ad8fb04c-4f75-42fc-973a-
6e54c8a4449a/GlobalElectricVehicleOutlook2022.pdf.
IEA (International Energy Agency). 2023. Global EV Outlook 
2023: Catching Up with Climate Ambitions . France: IEA. https://
iea.blob.core.windows.net/assets/dacf14d2-eabc-498a-8263-
9f97fd5dc327/GEVO2023.pdf.
ITDP (Institute for Transportation and Development Policy). 2018. 
“China Tackles Climate Change with Electric Buses.” Institute for 
Transportation and Development Policy. September 11. https://
www.itdp.org/2018/09/11/electric-buses-china/.
ITF (International Transport Forum). 2023. “Lifecycle Assessment of 
Passenger Transport—An Indian Case Study.” https://www.itf-oecd.
org/sites/default/files/docs/life-cycle-assessment-passenger-
transport-india.pdf.
Jiang, J., W. Shi, J. Zheng, P. Zuo, J. Xiao, X. Chen, W. Xu, and J-G. 
Zhang. 2013. “Optimized Operating Range for Large-Format 
LiFePO4/Graphite Batteries.” Journal of the Electrochemical Society  
161 A336 (December). DOI 10.1149/2.052403jes.
Jin, L. 2020. “Preparing to Succeed: Fleet-Wide Planning Is Key in 
the Transition to Electric Buses.” International Council on Clean 
Transportation. July 15. https://theicct.org/preparing-to-succeed-
fleet-wide-planning-is-key-in-the-transition-to-electric-buses/.
Johnson, C., E. Nobler, L. Eudy, and M. Jeffers. 2020. “Financial 
Analysis of Battery Electric Transit Buses.” National Renewable 
Energy Laboratory. https://afdc.energy.gov/files/u/publication/
financial_analysis_be_transit_buses.pdf.
Keil, P., S.F. Schuster, J. Wilhelm, J. Travi, A. Hauser, R.C. Karl, and A. 
Jossen. 2016. “Calendar Aging of Lithium-Ion Batteries.”  
Journal of The Electrochemical Society 163 A1872 (July). DOI 
10.1149/2.0411609jes.
Kumar, P., and S. Chakrabarty. 2020. “Total Cost of Ownership 
Analysis of the Impact of Vehicle Usage on the Economic Viabil -
ity of Electric Vehicles in India.” Transportation Research Record: 
Journal of the Transportation Research Board 2674 (11). https://doi.
org/10.1177/0361198120947089. 
Lander, L., E. Kallitsis, A. Hales, J.S. Edge, A. Korre, and G. Offer. 
2021. “Cost and Carbon Footprint Reduction of Electric Vehicle 
Lithium-Ion Batteries through Efficient Thermal Management.” 
Applied Energy 289 (May): 116737. https://doi.org/10.1016/j.apen -
ergy.2021.116737.
Li, J., and Z. Zhu. 2022. “Battery Thermal Management Systems of 
Electric Vehicles Space for Picture.” https://publications.lib.chalm -
ers.se/records/fulltext/200046/200046.pdf.
Li, S., He S., Wang S., He T., Chen J., 2020. ACM Digital Library.  “Data 
Driven Battery-Lifetime- Aware Scheduling of Electric Bus Fleets” 
https://dl.acm.org/doi/abs/10.1145/3369810
Li, S., H. Hongwen, C. Su, and P. Zhao. 2020. “Data Driven Battery 
Modeling and Management Method with Aging Phenomenon 
Considered.” Applied Energy (October) 275:115340. http://dx.doi.
org/10.1016/j.apenergy.2020.115340.
Liu, H., F. Chen, Y. Tong, Z. Wang, X. Yu, and R. Huang. 2020. 
“Impacts of Driving Conditions on EV Battery Pack Life 
Cycle.” World Electric Vehicle Journal 11 (1): 17. https://doi.
org/10.3390/wevj11010017.
Ma, S., M. Jiang, P. Tao, C. Song, J. Wu, J. Wang, T. Deng, and W. 
Shang. 2018. “Temperature Effect and Thermal Impact in Lithium-
Ion Batteries: A Review.” Progress in Natural Science: Materials  
International 28 (6): 653–66. https://doi.org/10.1016/j.pnsc.2018.  
11.002.
McGrath, T., L. Blades, J. Early, and A. Harris. 2022. “UK Battery 
Electric Bus Operation: Examining Battery Degradation, Carbon 
Emissions and Cost.” Transportation Research Part D: Transport 
and Environment 109 (August): 103373. https://doi.org/10.1016/j.
trd.2022.103373.
Miao, Y., P. Hynan, A. von Jouanne, and A. Yokochi. 2019. “Cur -
rent Li-Ion Battery Technologies in Electric Vehicles and Op -
portunities for Advancements.” Energies  12(6): 1074. https://doi.
org/10.3390/en12061074.
MoEFCC (Ministry of Environment, Forest and Climate Change, 
Government of India).  2021. India Third Biennial Update Report to 
the United Nations Framework Convention on Climate Change . New 
Delhi: MoEFCC. https://unfccc.int/sites/default/files/resource/IN -
DIA_%20BUR-3_20.02.2021_High.pdf.

WORKING PAPER  |  January 2024  |  33
Real-world electric bus operation: Trend in technology, performance, degradation, and lifespan of batteries
Molaeimanesh, G.R., S.M. Mousavi-Khoshdel, and A.B. Nemati. 
2020. “Experimental Analysis of Commercial LiFePO 4 Battery Life 
Span Used in Electric Vehicle under Extremely Cold and Hot Ther -
mal Conditions.” Journal of Thermal Analysis and Calorimetry 143: 
3137–46. https://doi.org/10.1007/s10973-020-09272-z.
Mookherjee, P., and K. Mitra. 2022. Electric Buses in India: Emerging 
Issues and Policy Lessons . New Delhi: Observer Research Founda -
tion. https://www.orfonline.org/wp-content/uploads/2022/03/
ORF_PolicyReport_Electric-Buses.pdf.
MoP (Ministry of Power). 2022. “CESL Discovers Lowest Ever Prices 
for 5450 Buses under the FAME II Scheme.” April 26. https://pib.
gov.in/PressReleaseIframePage.aspx?PRID=1820225. 
MoRTH (Ministry of Road Transport and Highways). 2021. Road 
Transport Year Book, Ministry of Road Transport and Highways . 
New Delhi: MoRTH. https://morth.nic.in/sites/default/files/RTYB-
2017-18-2018-19.pdf.
Motapon, S.N., E. Lachance, L-A. Dessaint, and K. Al-Haddad. 2020. 
“A Generic Cycle Life Model for Lithium-Ion Batteries Based on 
Fatigue Theory and Equivalent Cycle Counting.” IEEE Open Journal 
of the Industrial Electronics Society 1: 207–17. https://doi.org/10.1109/
ojies.2020.3015396.
Mueller, S., S. Rohr, W. Schmid, and M. Lienkamp. 2017. “Analys -
ing the Influence of Driver Behaviour and Tuning Measures on 
Battery Aging and Residual Value of Electric Vehicles.” EVS30 
International Battery, Hybrid and Fuel Cell Electric Vehicle Sym -
posium, Germany, October 9–11. https://mediatum.ub.tum.de/
doc/1403367/1403367.pdf.
Neef, C. 2022. “Development Perspectives for Lithium-Ion Battery 
Cell Formats.” Fraunhofer Institute for Systems and Innovation 
Research. December 13.
Nils, H., M. Messagie, and T. Coosemans. 2019. "Analysis of the Po -
tential for Electric Buses." Available at: https://www.slideshare.net/
sustenergy/analysis-of-the-potential-for-electric-buses
Nurhadi, L., S. Borén, and H. Ny. 2014. “A Sensitivity Analysis of Total 
Cost of Ownership for Electric Public Bus Transport Systems in 
Swedish Medium Sized Cities.” Transportation Research Procedia  3: 
818–27. https://doi.org/10.1016/j.trpro.2014.10.058.
Olsson, O., A. Grauers, and S. Pettersson. 2016. “Method to Analyze 
Cost Effectiveness of Different Electric Bus Systems.” Paper pre -
sented at EVS29 International Battery, Hybrid and Fuel Cell Electric 
Vehicle Symposium, Quebec, June 19–22. https://www.diva-portal.
org/smash/get/diva2:1159796/FULLTEXT01.pdf.
Ouyang, D., Y. He, J. Weng, J. Liu, M. Chen, and J. Wang. 2019. 
“Influence of Low Temperature Conditions on Lithium-Ion Batter -
ies and the Application of an Insulation Material.” RSC Advances  9: 
9053–66. https://doi.org/10.1039/C9RA00490D.
Ouyang, M., X. Feng, X. Han, L. Lu, Z. Li, and X. He. 2016. “A Dynamic 
Capacity Degradation Model and Its Applications Considering 
Varying Load for a Large Format Li-Ion Battery.” Applied Energy  165 
(March): 48–59. https://doi.org/10.1016/j.apenergy.2015.12.063.
Pagliaro, M., and F. Meneguzzo. 2019. “Electric Bus: A Critical Over -
view on the Dawn of Its Widespread Uptake.” Advanced Sustainable 
Systems 3 (6): 1800151. https://doi.org/10.1002/adsu.201800151.
Pandya, V.M. 2023. “Top 5 Electric Buses in India 2023.” E-Vehicle -
info. February 3.  https://e-vehicleinfo.com/top-5-best-electric-
buses-in-india-2023/#.
Piao, C., T. Chen, A. Zhou, P. Wang, and J. Chen. 2020. “Research 
on Electric Vehicle Cooling System Based on Active and Passive 
Liquid Cooling.” Journal of Physics: Conference Series 1549: 042146. 
DOI 10.1088/1742-6596/1549/4/042146.
PIB (Press Information Bureau). 2023. “Cabinet Approves ‘PM-eBus 
Sewa’ for Augmenting City Bus Operations; Priority to Cities Having 
No Organized Bus Service.” August 16. https://pib.gov.in/PressRe -
leaseIframePage.aspx?PRID=1949429. 
Pozzato, G., and M. Corno. 2020. “Closed-Loop Battery Aging 
Management for Electric Vehicles.” IFAC-PapersOnLine  53 (2): 
14199–204. https://doi.org/10.1016/j.ifacol.2020.12.1051.
QuantumScape. “Lithium Iron Phosphate on the QuantumScape 
Solid-State Lithium-Metal Platform.” 2021. September 7. https://
www.quantumscape.com/resources/blog/lithium-iron-phosphate-
on-the-quantumscape-solid-state-lithium-metal-platform/.
Rothgang, S., M. Rogge, J. Becker, and D.U. Sauer. 2015. “Battery 
Design for Successful Electrification in Public Transport.” Energies  
8 (7): 6715–37. https://doi.org/10.3390/en8076715.
Samanta, A., and S.S. Williamson. 2021. “A Comprehensive Re -
view of Lithium-Ion Cell Temperature Estimation Techniques 
Applicable to Health-Conscious Fast Charging and Smart Bat -
tery Management Systems.” Energies 14 (18): 5960. https://doi.
org/10.3390/en14185960.
Sawle, Y., and M. Thirunavukkarasu. 2021. “Techno-Economic 
Comparative Assessment of an Off-Grid Hybrid Renewable Energy 
System for Electrification of Remote Area.” In Design, Analysis, and 
Applications of Renewable Energy Systems , edited by Azar, A.T., and 
N.A. Kamal, 199–247. Academic Press.  https://doi.org/10.1016/B978-
0-12-824555-2.00027-7.
Saxena, S., C. Le Floch, J. MacDonald, and S. Moura. 2015. “Quanti -
fying EV Battery End-of-Life through Analysis of Travel Needs with 
Vehicle Powertrain Models.” Journal of Power Sources  282 (May): 
265–76. https://doi.org/10.1016/j.jpowsour.2015.01.072.

34  |  
  
Sclar, R., C. Gorguinpour, S. Castellanos, and X. Li. 2019. Barriers to 
Adopting Electric Buses . Washington, DC: WRI. https://wrirosscities.
org/sites/default/files/barriers-to-adopting-electric-buses.pdf. 
Shah, J. 2022. “The Top 5 Lithium-Ion Battery Mishaps and Les -
sons Therein.” Saur Energy. April 21. https://www.saurenergy.
com/ev-storage/the-top-5-lithium-ion-battery-mishaps-and-
lessons-therein. 
Shah, M. 2023. “Top 10 Electric Bus Manufacturers in India 2023 | 
Electric Bus.” E-Vehicleinfo. February 14. https://e-vehicleinfo.com/
top-10-electric-bus-manufacturers-in-india-electric-bus/.
Sustainable Bus. 2021 A. “Lithium-Ion Battery Technology in E-
Buses, according to BMZ.” Sustainable Bus. April 15, 2021. https://
www.sustainable-bus.com/news/bmz-poland-lithium-ion-battery-
technology-electric-buses/.
Sustainable Bus. 2021 B. “Over 61,000 E-Buses Sold by Chinese Bus 
Makers in 2020. Production Went Down 20%.” Sustainable Bus. 
January 15, 2021. https://www.sustainable-bus.com/electric-bus/
chinese-new-energy-bus-market-2020/.
Sui, X., M. Świerczyński, R. Teodorescu, and D. Stroe. 2021. 
“The Degradation Behavior of LiFePO4/C Batteries during 
Long-Term Calendar Aging.” Energies 14 (6): 1732. https://doi.
org/10.3390/en14061732.
Switch Mobility. 2022. “Switch Mobility Ltd. Launches All New, 
‘SWITCH E1’ 12m Bus. | Switchmobility.” Www.switchmobilityev.com. 
2022. https://www.switchmobilityev.com/en/news/switch-mobility-
ltd-launches-all-new-switch-e1-12m-bus#:~:text=With%20a%20
389kWh%20battery%20capacity.
Tomaszewska, A., Z. Chu, X. Feng, S. O’Kane, X. Liu, J. Chen, C. Ji, 
E. Endler, R. Li, L. Liu, Y. Li, S. Zheng, S. Vetterlein, M. Gao, J. Du, 
M. Parkes, M. Ouyang, M. Marinescu, G. Offer, and B. Wu. 2019. 
“Lithium-ion battery fast charging: A review”, eTransportation 1 
(August): 100011. https://doi.org/10.1016/j.etran.2019.100011. TUMI 
and C40 Cities. 2023. “Development of the India Zero Emission 
Bus Market Investor’s Guide.” Transformative-Mobility.org. https://
transformative-mobility.org/wp-content/uploads/2023/04/C40-
India-ZE-Bus-Investor-guide.pdf.
Wankhede, S., P. Thorat, S. Shisode, S. Sonawane, and R. 
Wankhade. 2022. “A Study of Different Battery Thermal Manage -
ment Systems for Battery Pack Cooling in Electric Vehicles.” Heat 
Transfer 51 (8): 7487–539. https://doi.org/10.1002/htj.22653.
Xiao, M. 2019. “The Lithium-Ion Battery and the Electric Vehicle .” 
https://www.interactanalysis.com/wp-content/uploads/2019/10/
The-Lithium-Ion-Battery-and-the-Electric-Vehicle-Whitepaper.pdf.
Xiong, S. 2019. “A Study of the Factors that Affect Lithium Ion 
Battery Degradation.”  https://mospace.umsystem.edu/xmlui/
handle/10355/73777.
Xue, L., D. Liu, W. Wei, and P. Liu. 2019. “Overcoming the Operational 
Challenges of Electric Buses: Lessons Learnt from China.” World 
Resources Institute. https://wri.org.cn/en/research/overcoming-
operational-challenges-electric-buses.
Yang, F., Y. Xie, Y. Deng, and C. Yuan. 2018. “Predictive Modeling 
of Battery Degradation and Greenhouse Gas Emissions from U.S. 
State-Level Electric Vehicle Operation.” Nature Communications  9 
(1). https://doi.org/10.1038/s41467-018-04826-0.
Yang, X-G., T. Liu, and C-Y Wang. 2021. “Thermally Modulated 
Lithium Iron Phosphate Batteries for Mass-Market Electric 
Vehicles.” Nature Energy 6 (2): 176–85. https://doi.org/10.1038/
s41560-020-00757-7.
Yiyang, C., and V. Fremery. 2022. “E-Bus Development in China: 
From Fleet Electrification to Refined Management—SUSTAINABLE 
TRANSITION CHINA.” Mobility Transition in China. January 29. 
https://transition-china.org/mobilityposts/e-bus-development-in-
china-from-fleet-electrification-to-refined-management/.
Yutong. n.d. “New Energy Buses & Solutions—YUTONG.” En.yutong.
com. https://en.yutong.com/z/newenergybus/. Accessed 
October 16, 2023.
Zeng, Z., D. Daniels, and X. Qu. 2022. “Limitations and Suggestions 
of Electric Transit Charge Scheduling.” Progress in Energy  4 (2): 
023001. DOI 10.1088/2516-1083/ac6112.
Zhang, L., Z. Zeng, and X. Qu. 2021. “On the Role of Battery Capacity 
Fading Mechanism in the Lifecycle Cost of Electric Bus Fleet.” IEEE 
Transactions on Intelligent Transportation Systems  22 (4): 2371–80. 
https://doi.org/10.1109/TITS.2020.3014097.

WORKING PAPER  |  January 2024  |  35
Real-world electric bus operation: Trend in technology, performance, degradation, and lifespan of batteries
This page is intentionally left blank

Copyright 2023 World Resources Institute. This work is licensed under the Creative Commons Attribution 4.0 International License.  
To view a copy of the license, visit http://creativecommons.org/licenses/by/4.0/
  
LGF, AADI, 2 Balbir Saxena Marg, Hauz Khas, New Delhi 110016, India  |  WRI-INDIA.ORG
ACKNOWLEDGMENTS
We would like to thank Mr. Madhav Pai, CEO of WRI India, for his 
support. We would also like to extend our thanks to Dr. Shahana 
Chattaraj, Director of Research Data and Innovation, and Dr. 
Sudeshna Chatterjee, Program Director for Sustainable Cities 
and Transport at WRI India, for their guidance in developing the 
paper. We also thank Yash Khandelwal for his help in developing 
the battery data collection template and for providing discerning 
insights during this work. We express sincere gratitude to our 
reviewers for their valuable suggestions for enhancing the paper’s 
content, and also  Lalit Mudholkar, Junior Program Associate, WRI 
India, for his help and support. We also appreciate the efforts of 
our colleagues Rama Thoopal, Anindita Bhattacharjee, Manasi 
Nandakumar, and Karthikeyan Shanmugam for their editorial and 
design support.
ABOUT THE AUTHORS
Dr. Parveen Kumar is Senior Program Manager in Electric 
Mobility, Sustainable Cities and Transport, Cities Program,  
WRI India.
Pawan Mulukutla  is Executive Program Director, Integrated 
Transport, Clean Air and Hydrogen, WRI India.
Priyansh Doshi  worked as Junior Program Associate in Electric 
Mobility, Sustainable Cities and Transport, Cities Program, at WRI 
India. Now he works as Junior Technical Manager at Smart Freight 
Centre, the Netherlands.
ABOUT WRI INDIA
WRI India, an independent charity legally registered as the India 
Resources Trust, provides objective information and practical 
proposals to foster environmentally sound and socially equitable 
development. Our work focuses on building sustainable and livable 
cities and working towards a low-carbon economy. Through 
research, analysis, and recommendations, WRI India puts ideas 
into action to build transformative solutions to protect the earth, 
promote livelihoods, and enhance human well-being. 
We are inspired by and associated with World Resources Institute 
(WRI), a global research organization with more than 1,000 experts 
around the world. World Resources Institute began in Washington, 
DC, in 1982 to provide cutting edge analysis to address global 
environment and development challenges. WRI spans more 
than 60 countries, with offices in Brazil, China, Europe, Mexico, 
India, Indonesia, and the United States. In all these locations, 
WRI works with government, business, and civil society to drive 
ambitious action based on high-quality data and objective analysis. 
The India Resources Trust has a license from WRI to use the 
trademark “WRI India.”
