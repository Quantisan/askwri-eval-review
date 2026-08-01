---
doc_id: 2021_simulator-to-quantify-and-manage-electric-vehicle_1145
source_pdf: kp-docs/askwri-kps/2021_simulator-to-quantify-and-manage-electric-vehicle_1145.pdf
extraction_method: cache-plaintext
char_count: 83768
title: Simulator to Quantify and Manage Electric Vehicle Load Impacts on Low-voltage Distribution Grids
authors: Xue, Lulu; Xia, Junrong
date_published: 6/1/2021
article_type: Technical Note
sub_tag: Transport decarbonization
wri_primary_office: WRI China
wri_programs: Cities
language: English
url: "https://www.wri.org/research/simulator-quantify-and-manage-electric-vehicle-load-impacts-low-voltage-distribution-grids"
doi: "https://doi.org/10.46830/writn.20.00009"
summary: The Electric Vehicles on the Grid Simulator enables users to assess the load impacts of electric vehicles (EVs) on low-voltage distribution grids, facilitating informed planning for capacity upgrades. Utilizing Monte Carlo simulations and linear programming, the tool predicts EV charging profiles while accounting for various factors such as user behavior and charging infrastructure. It supports both unmanaged and managed charging scenarios, allowing for optimization of EV load to reduce costs and enhance grid reliability. This simulator is particularly beneficial for utility companies and facility managers aiming to mitigate potential overloads and integrate renewable energy sources effectively.
---

# Simulator to Quantify and Manage Electric Vehicle Load Impacts on Low-voltage Distribution Grids

TECHNICAL NOTE  |  December 2020  |  1
TECHNICAL NOTE
Technical notes document the research or analytical 
methodology underpinning a publication, interactive 
application, or tool.
Suggested Citation: Xue, Lulu, and Junrong Xia. 
2020. “Simulator to Quantify and Manage Electric 
Vehicle Load Impacts on Low-Voltage Distribution 
Grids.” Technical Note. Washington, DC: World 
Resources Institute. Available online at: https://www.
wri.org/publication/.
LULU XUE AND JUNRONG XIA 
SIMULATOR TO QUANTIFY AND MANAGE ELECTRIC VEHICLE 
LOAD IMPACTS ON LOW-VOLTAGE DISTRIBUTION GRIDS
ABSTRACT
The Electric Vehicles on the Grid Simulator (https://
ev-simulator.wri.org) is intended to help individual 
building energy managers, facility owners, distribution 
service operators, charging point operators, and fleet 
operators. This model-based simulator enables users to 
evaluate the potential electric vehicle (EV) load impacts 
on the low-voltage distribution grid at specific sites and 
plan for future capacity upgrades. Additionally, the tool 
can be used to quantify the effects of different vehicle-
grid integration technologies to alleviate the peak 
capacity stress.  
The Monte Carlo simulation and linear programming 
are deployed to predict the EV charging and 
discharging load profiles and load impacts at specific 
sites, with the consideration of future EV penetration, 
EV charging and traveling behaviors, availability 
of charging facility availability, and site loads. 
Based on existing studies conducted in the United 
States, Europe, and China, the default EV charging 
and traveling behaviors are predefined for a quick 
assessment. Users are encouraged to modify the model 
inputs for the specific site to derive more accurate and 
contextualized results. This tool can also help manage 
an EV fleet’s smart charging and discharging at the 
low-voltage distribution grid.
CONTENTS
Abstract ......................................................................... 1
1. Introduction ............................................................... 2
2. Motivation ................................................................. 3
3. Model Scope and Applicability .................................. 4
4. Model Description ..................................................... 5
5. How to Use the Model ............................................... 24
6. Limitations ................................................................ 32
Appendix A.  Model Variables ........................................ 33
Appendix B.  Model Key Assumptions ........................... 35
Appendix C.  Extended Functions of the Python Scripts ... 36
Abbreviations ................................................................ 37
Endnotes ....................................................................... 37
References ..................................................................... 38
Acknowledgments ......................................................... 39

2  |  
1. INTRODUCTION
The increasing penetration of plug-in electric 
vehicles (EVs), including battery EVs and plug-in 
hybrid EVs, imposes a significant load on the low-
voltage distribution grid, which consists of the low-
voltage transformers and substations at a specific 
site. Accommodating the charging demands of EVs 
will involve expensive upgrades to local distribution 
systems. Nonetheless, vehicle-grid integration (VGI), 
as used in this study, enables EVs to provide grid 
services such as peak load shaving and to maintain 
an affordable and reliable distribution grid. To 
achieve this goal, EVs must have capabilities to 
manage charging or support two-way interaction 
between vehicles and the grid, which are referred to as 
“managed charging” and “vehicle-to-grid” (V2G). 
The Electric Vehicles on the Grid Simulator (https://
ev-simulator.wri.org) is a model-based simulator that 
provides two main functions, as shown in Figure 1: 
 ▪ It helps individual building energy managers, 
facility owners, 1 distribution service operators, 
charging point operators, and fleet operators 
quantify the future EV load impacts on 
transformers or substations 2 at a specific site—
for example, a residential neighborhood or an 
office building. It will also inform future low-
voltage network upgrades, ensuring that EV load 
impacts do not exceed the current capacities of 
transformers and substations.  
 ▪ It helps individual building energy managers, 
facility owners, distribution service operators, and 
charging point operators manage and optimize 
individual EV charging and discharging profiles 
through VGI measures to delay or possibly 
avoid expensive network upgrades (known as 
“distribution deferral”), reduce overall costs for 
electricity (known as “retail energy time shift” 3), 
or consume on-site solar by leveraging EVs as a 
behind-the-meter energy storage system. In this 
case, the optimized EV charging and discharging 
profiles generated from the tool can be sent to 
charging points to directly manage the charging (or 
discharging) time and power of each EV.
The tool is not capable of modeling stationary storages 
or demand flexibility in buildings. 
Figure 1  |  Purposes of the Simulator
Notes:  EV = electric vehicle. Yellow chargers are unmanaged chargers that will probably incur large investments in distribution grid upgrades. Green chargers are managed chargers capable of 
retiming the charging sessions to off-peak hours, thereby reducing the investment in distribution upgrades and also enhancing on-site solar consumption. 
Source: WRI China authors.
Optimization of EV loads
• Distribution deferral          
• Retail energy time shift           
• On-site solar consumption
Without dynamic load balancing and with a costly upgrade of the grid connection
With dynamic load balancing
Quantification of 
EV impacts

Simulator to Quantify and Manage Electric Vehicle Load Impacts on Low-Voltage Distribution Grids
TECHNICAL NOTE  |  December 2020  |  3
2. MOTIVATION
The simulator was developed to assist utility companies 
and businesses to determine at what threshold EV 
adoption rates will overload the existing capacity of a 
transformer, a substation, or multiple substations in 
an area. Conventional methods of forecasting the peak 
loads of non-EV customers (such as commercial or 
industrial peak loads) on a transformer (or substation) 
are not suitable due to the variety of EV charging 
profiles. These conventional practices primarily include 
load surveys and the diversity factor method. 
 ▪ Site load surveys rely on using the load profiles of 
similar facilities plus extra capacity allowances to 
project peak demands—an approach that is useful to 
forecast the demand of large users such as industrial 
or commercial customers (Munasinghe 1990).  
 ▪ The diversity factor method builds on the fact that 
the maximum demands of individual customers 
or electrical appliances will not occur at the same 
time; thus, this demand is diversified (Bayliss 
and Hardy 2007; Smith and Parmenter 2016). 
The diverse nature of load demands motivates 
the use of the diversity factor—the reciprocal 
of the coincidence factor—and is important to 
utility companies in planning distribution grid 
expansion. Utility companies use empirical 
evidence to determine the diversity factors (or 
coincidence factors) for different types and sizes 
of customers. These companies then estimate peak 
load by applying this predefined diversity factor to 
discount the sum of individual maximum demands 
(Equation 1). 
Equation 1
Because EVs present a new type of custom load that has 
no historic records, and the current number of EVs has 
not yet reached a critical mass for utility companies to 
capture its load characteristics or diversity factors, the 
above two approaches encounter limitations. 
The simulator adopts an end user approach to 
forecast the future EV daily load that accounts for the 
randomness of EV charging and traveling behaviors. In 
the model, EV charging and traveling behaviors should 
be defined by the user based on the best available 
data. Defaults in this tool are based on existing studies 
carried out in the United States, Europe, and China 
(Stephens et al. 2012; INL 2015; Sadeghianpourhamami 
et al. 2017; California Energy Commission 2018; Gnann 
et al. 2018; and Xue et al. 2020). However, whenever 
the data are available, the user should make location-
specific updates to these behavioral inputs to derive 
more accurate and contextualized results. The defaults 
only apply to the circumstances where the user has 
no data but is in need of a quick, rough assessment or 
where the user wants to understand the data needed to 
forecast potential EV load impacts and strives to set up 
a data collection system.  
Whereas the Vehicle-to-Grid Simulator (V2G-
Sim) developed by the Lawrence Berkeley National 
Laboratory 4 evaluates EV grid impacts at various 
levels, from distribution to transmission and wholesale 
market, the Electric Vehicles on the Grid Simulator 
focuses on EV grid impacts on the distribution level. 
Overall, this tool is a simplified version of V2G-Sim. 
With predefined use cases such as residential, office, 
and public, it is comprehensible to beginners and is 
therefore accessible for developing countries that are 
not familiar with the idea of VGI.  
   Max load = 
∑i max individual demand i
= ∑i max individual demand i ×coincidence factor
Diversity factor

4  |  
3. MODEL SCOPE AND APPLICABILITY
In the simulator, the grid impact is confined to the 
load demand impacts that are critical for distribution 
infrastructure planning and operational decisions 
(Table 1). Although EV charging also causes energy 
losses, voltage drops, and harmonic imbalance, these 
impacts can be mitigated with existing distribution grid 
equipment. Therefore, the simulator will focus only on 
the load demand impacts. 
Different user groups with various concerns may focus 
on different aspects of the load curves. For example, 
utility companies are interested in peak demand when 
determining the capacity of the equipment needed to 
meet the customer’s power requirements. They are 
interested in the near-peak load when setting utility 
tariffs to shift the load demands to off-peak hours. This 
simulator focuses on the entire load curve; therefore, it 
enables a whole spectrum of applications (Table 1).   
Table 1  |  Load Curve Focus by User Group
Entity Applications Focus
Distribution system 
operators (DSOs), facility 
owners
• Determine the capacity of distribution grid, 
as a result of increased electric vehicle (EV) 
penetration
• Lower the expenses on demand charges
a
 for 
facility owners
Peak load
Regulators, utility 
companies
• Understand charging behavior over a time 
period to determine utility tariff 
Near-peak load
Charging point operators, 
DSOs, facility owners, 
customers
• Optimize EV load impacts to maintain an 
affordable and reliable electricity system and to 
support on-site solar integration
• Reduce cost for electricity for customers
Entire load profiles
Notes:  a A regular utility tariff is imposed on energy consumption (measured in kilowatt-hours) whereas a demand charge is imposed on peak power demand (measured in kilowatts; and 
sometimes energy consumption is combined) to reduce the stress on the generation, transmission, and distribution capacities. Demand charges are often applied to commercial and 
industrial users, which often have high peak power demands.    
Source: WRI China authors.
Time of day: hour
250 5 10 15 20
0
12,000
14,000
10,000
6,000
4,000
2,000
8,000
Load: kW
Time of day: hour
250 5 10 15 20
0
12,000
14,000
10,000
6,000
4,000
2,000
8,000
Load: kW
Time of day: hour
250 5 10 15 20
0
12,000
14,000
10,000
6,000
4,000
2,000
8,000
Load: kW

Simulator to Quantify and Manage Electric Vehicle Load Impacts on Low-Voltage Distribution Grids
TECHNICAL NOTE  |  December 2020  |  5
EV load is the energy consumed by EVs throughout 
a day. Although load profiles can be characterized at 
different temporal resolutions and spatial scopes, the 
simulator deals with the following aspects:
 ▪ Time resolution.  The simulator adopts the daily 
load at a one-hour interval because this interval helps 
to reduce the computational complexity for managed 
charging and V2G. However, compared with 15-minute 
or 30-minute intervals, a one-hour interval also loses 
the time granularity and accuracy needed in some 
applications, including the estimation of demand 
charge reduction (usually demand charges are metered 
at 15-minute intervals). 
 ▪ Spatial resolution.  The simulator is set on the 
transformer (ratings are available from 200 to 
1,500 kilovolt-amperes) and the substation level 
(a set of transformers). Therefore, the simulator 
is able to examine the impacts from increased 
EV deployment on an individual transformer or 
substation at a specific site, such as a residential 
neighborhood or an office complex.       
 ▪ Time horizon of projection.  Although the 
simulator is able to evaluate the current status of 
EV load impacts, it is also capable of projecting 
medium-term or long-term load demand as a result 
of increases in EVs or improved vehicle performance. 
The medium or long term is usually more than three 
years, which corresponds to the lead time required for 
major distribution upgrades. 
Transformers (or substations) at different 
locations, such as industries, offices, and residential 
neighborhoods, serve different customer groups. Each 
customer group has unique demands and load curves. 
For example, in residential neighborhoods, energy 
consumption often occurs in the evening, whereas in 
offices most of the energy consumption occurs during 
the day. The simulator provides three predefined use 
cases that are common for EVs:
 ▪ Residential Use Case.  Home charging is the most 
common charging location. In the United States, EV 
users perform 84 percent of charging at home (INL 
2015); in China, EV users perform nearly 40 percent 
of charging at home (CATARC 2018). 
 ▪ Office Use Case.  Workplace charging either 
complements home charging—providing range 
extension to daily commuting (or long-range 
travel)—or substitutes for home charging. In the 
simulator, office charging is treated as a substitute 
for home charging rather than for range extension. 
Doing so could lead to an overestimation of EV grid 
impacts in the Office Use Case. 
 ▪ Public Use Case.  Compared to private home 
chargers and workplace chargers, public chargers 
are least used. At different venues, parking time 
and charging behaviors also differ. For example, at 
airport parking lots, EVs park for longer periods of 
time, whereas at direct current (DC) fast charging 
stations, EVs simply charge and go. The simulator 
takes the latter case as the default, but users can 
adapt the inputs to their needs.     
Besides these three use cases, the simulator also allows 
for user-defined cases and for operating fleets such as 
electric freight vehicles. If the studied area is large and 
covers mixed uses, users can split customer segments 
and run the use cases separately.    
4. MODEL DESCRIPTION 
4.1 Model Structure
The simulator consists of three modules corresponding 
to the three ways that an EV can interact with the 
grid—namely, unmanaged charging, managed charging, 
and V2G (Figure 2).  
Unmanaged charging module. This module 
evaluates the EV load impacts from the most common 
charging method, unmanaged charging, in which EVs 
are charged at full power rates as soon as they plug in 
until the batteries are full or the vehicles have to leave.
Managed charging module. Managed charging 
relies on a time-of-use (TOU) tariff or remote 
automatic control to shift EV charging loads to off-
peak hours or align with renewable energy generation 
curves. The tool only models managed charging 
through remote automatic control by charging point 
operators or distribution service operators. Although 
TOU tariffs will incentivize EV drivers to charge 
at off-peak hours, how EV drivers will respond to 
peak-hour tariffs is an intricate research topic that is 
beyond this model. However, the simulator can model 
the optimized charging load through the combined

6  |  
approaches of remote control and TOU tariffs. For 
example, the simulator can derive optimal charging 
profiles that minimize the drivers’ utility costs through 
automatic control. 
V2G module. V2G allows for bidirectional power 
flows between the vehicle and the grid. The V2G module 
simulates how V2G optimizes EV charging or discharging 
load profiles without compromising the vehicles’ travel 
demands or fully depleting the batteries. 5 
It is worth mentioning that managed charging and V2G 
technologies by nature have limited applicability—this 
has nothing to do with the tool:
 ▪ VGI technologies may not work well for Level 1 
chargers (charging power rate between about 1.4 
and 3.4 kilowatts) because they are slow and require 
many hours to charge fully, usually leaving little time 
flexibility for VGI. 
 ▪ VGI technologies also may not work well for short 
parking times in the Public Use Case because the short 
dwell time does not allow for vehicle-grid interactions. 
The three modules are realized in both an online 
web application and an offline Python script. The 
unmanaged charging module and managed charging 
module are available both online (in the web 
application) and offline (in the Python script), whereas 
the V2G module, which requires a longer running time, 
is available only in the Python script. Furthermore, 
the online web application allows for simplified model 
inputs for easy maneuvers, whereas the Python script 
provides adaptation options to the model inputs and the 
functions. The differences between the web application 
and the Python script are summarized in Section 5.1. 
Notes:  EV = electric vehicle; PEV = plug-in electric vehicle; V2G = vehicle-to-grid.
Source: WRI China authors.
Figure 2  |  Model Structure
Use cases
Model inputs
Models
Model outputs
Grid inputs
• Unmanaged charging load
• Overloading & utilization efficiency analysis
• Optimized EV charging or discharging profile
Vehicle inputs:
• PEV stocks
• Battery energy capacity
• Energy efficiency
Charging 
infrastructure lnputs:
• Number of chargers
• Charging power
Grid inputs:
• Base load
• Transformer's capacity
• Distributed solar outputCharging 
frequency
(Dis)charging 
power
Starting state 
of charge 
(Probability 
distribution )
Daily mileage 
(Probability 
distribution )
Starting time 
(Probability 
distribution )
Parking 
duration
Charging and travel behaviors:
Residential Use Case Office Use Case Public Use Case Other use cases
Vehicle-grid 
integration
Managed charging module:
(Monte Carlo simulation +  
linear programming )
V2G module:
(Monte Carlo simulation +  
linear programming )
Unmanaged charging 
module:
(Monte Carlo simulation )

Simulator to Quantify and Manage Electric Vehicle Load Impacts on Low-Voltage Distribution Grids
TECHNICAL NOTE  |  December 2020  |  7
Notes:  EV = electric vehicle; SOC = state of charge.
Source: WRI China authors.
Figure 3  |  Model Inputs
4.2 Model Inputs
The simulator evaluates EV load impacts based on two 
types of load profiles: base load (non-EV load) and EV 
load. If distributed solar photovoltaic systems are installed 
on site, the solar output curve can also be included in the 
simulator to offset the EV load or base load.  
The base load is taken as the daily load curve of a 
typical day collected from local meters or predicted 
using the methods outlined in Section 2. Since the tool 
only focuses on EV loads, the prediction of the base 
load is beyond the scope of the tool.  
EV load curves are model results that use the following 
information as inputs (Figures 3 and 4): 
 ▪ EV inputs, including EV penetration rates, and 
technical performances such as battery energy capacity 
and energy efficiency.6 A site may have multiple EV 
brands and models characterized by different technical 
performances. To reduce the model input workload, 
the online application only asks users to put in a typical 
and prevailing vehicle model. The Python script can 
be tweaked to allow users to specify multiple vehicle 
models and their numbers and technical performances. 
 ▪ Charging facility inputs, including the number and 
types of chargers, and charging power ratings. 
 ▪ Travel patterns, such as arrival time and departure 
time (that is, parking duration), to the parking lot. 
 ▪ Charging patterns, such as the starting state of charge 
(SOC), and charging frequency. 
To account for the stochastic nature of these travel and 
charging behaviors, behavioral inputs, such as travel 
Travel behavior
• Arrival time
• Parking duration
• Daily mileage
EV inputs
• EV penetration
• Battery capacity
• Energy efficiency
Grid inputs
• Base load
• On-site solar output
• Rated capacity
EV load
Charging behavior
• Charging frequency
• Starting SOC
Charging facilities
• Charging power
• Number of chargers

8  |  
Figure 4  |  Model Inputs for the Online Tool
Grid inputs
 Vehicle inputs
Charging facility inputs
Travel and charging behaviors
Notes: kVa = kilovolt-ampere; SOC = state of charge.
Source: WRI China authors.

Simulator to Quantify and Manage Electric Vehicle Load Impacts on Low-Voltage Distribution Grids
TECHNICAL NOTE  |  December 2020  |  9
and charging patterns, are expressed in randomly 
distributed variables.  
EV charging loads are generally computed based on 
charging starting time (the time when a charging 
session starts), the duration of the charging session, 
and the average charging power used throughout the 
charging session. The ways to specify or derive these 
three variables differ between the unmanaged charging 
module and the two VGI modules (Table 2). 
Charging starting time. The arrival time model 
input, collected from travel surveys or charging station 
observations, is a key input to derive the charging starting 
time (Figure 4). The arrival time of the EV fleet to the 
site is described in probability distributions to enable the 
Monte Carlo simulation. Arrival times in different use cases 
are characterized by different probability distributions 
(Figure 5). Users can make site-specific adaptations: the 
web application only allows users to define arrival time 
in the normal distribution by varying the means and the 
deviations or discrete distribution by specifying the number 
Table 2  |  Charging Starting Time, Charging Duration, and Charging Power Specifications
Unmanaged Charging Module Managed Charging Module, 
V2G Module
Charging starting time Intermediary result derived from the arrival time 
and number of chargers available Model input: arrival time
Charging duration
Intermediary result derived from starting state of 
charge (that can be further broken down to daily 
mileage, charging frequency, and battery range) Model input: parking duration
Charging power Model input: charging power Model input: upper limit of charging (or discharging) power
Model input: lower limit of charging (or discharging) power 
of EVs arriving at the site at each hour; the Python script 
allows for any type of distribution (continuous distribution, 
such as beta, and discrete distribution).    
Besides arrival time, the calculation of charging starting 
time also depends on the charging strategies deployed: 
 ▪ For unmanaged charging, the charging starting time 
is calculated by inferring the waiting time for charge 
points to become available, based on each vehicle’s 
arrival time, the number of vehicles, and the number 
of chargers installed. For example, the fewer the 
chargers installed on-site, the longer the queue of 
vehicles that will be formed. Hence, the charging 
starting time will be delayed to a later time.  
 ▪ For managed charging and V2G, the charging starting 
time is defined as the time when the charger is 
plugged in (but the charging or discharging session 
is not necessarily started); for simplicity, the model 
assumes the arrival time is a proxy of the charging 
starting time for EVs.
Note: V2G = vehicle-to-grid.
Source: WRI China authors.

10  |  
Figure 5  |  Examples of Arrival Time Distribution for the Three Use Cases
Use Case Residential Office Public and User-Defined
Model 
default
Normal distribution
(mean 20:00, deviation 2 hours)
Lognormal distribution
(mean 9:00)
Predetermined discrete distribution
Web 
application Normal distribution Normal distribution
Normal distribution or
discrete distribution
Notes:  Based on existing studies—including Stephens et al. (2012), Sadeghianpourhamami et al. (2017), California Energy Commission (2018), Gnann et al. (2018), and Xue et al. (2020)—
arrival times at homes, offices, and public venues in the United States, the Netherlands, and China exhibit regularities on weekdays due to similar commuting schedules. For example, 
arrival time shows a likely normal distribution pattern in residential neighborhoods, with a mean value around 17:00–20:00 and a possible lognormal distribution at workplaces with a 
mean value around 07:00–10:00. However, this model input can be tailored to the prevalent travel schedule of the specific site. Further, the y values are normalized so that the maximum y 
values across use cases are comparable in the same chart.
Source: The authors summarized data from the California Energy Commission (2018) and Gnann et al. (2018).
Oﬀice Residential Public
Number of charging sessions
Time of day
240 82 4 6 1610 12 14 18 20 22
0
800
600
700
400
500
200
100
300
Time of day Time of day Time of day
24 24 240 0 08 8 82 2 24 4 46 6 616 16 1610 10 1012 12 1214 14 1418 18 1820 20 2022 22 22
0 0 0
800 600
600
400
500
400
400
300
200
200
100
200
Number of charging sessions
Number of charging sessions
Number of charging sessions

Simulator to Quantify and Manage Electric Vehicle Load Impacts on Low-Voltage Distribution Grids
TECHNICAL NOTE  |  December 2020  |  11
Charging duration.  Charging duration is a key 
intermediary model result to produce EV charging and 
discharging profiles. It is derived from model inputs 
such as starting SOC or parking duration. 
For unmanaged charging, the estimation of charging 
duration follows Equation 2—that is, the energy 
request divided by the charging power. 7 Since the 
starting SOC is a key indicator of the energy requested 
for each charging session, it is an important input to 
derive the charging duration.
Equation 2
Ti  is EV i’s charging duration ( i indicates the i-th EV 
on the site)
E  is the energy request for one charging session 
(kilowatt-hours [kWh])
C is the energy capacity of batteries (kWh)
Pc  is charging power (kW)
φ  is charging efficiency (counting in energy loss 
during charging, fixed at 90 percent)
Because decisions on the amount of energy left in 
vehicles when charging  (the charging starting SOC) 
vary greatly across use cases and have uncertainties in 
the future, the model provides three ways to estimate 
starting SOC: 
1. Daily mileage estimation. When Level 1 slow 
charging is used in the Residential Use Case, private 
vehicles tend to be charged on a daily basis. As a 
result, starting SOC is determined by daily mileage 
traveled (see Equation 3 and Box 1). 
Equation 3
di is EV i’s daily mileage (kilometers [km])
R is the battery range (km) 
2. Multiple-day estimation.  As fast chargers become 
prevalent and battery ranges increase, EV drivers 
will opt to charge their cars less frequently (more 
than one-day intervals; Amsterdam Roundtable 
Foundation and McKinsey 2014; Charilaos et al. 
2017; Van den Hoed et al. 2019; Vermeulen et al. 
2019). In this case, charging starting SOC can be 
estimated by multiplying daily mileage by charging 
frequency—the number of days traveled since the 
last charge (see Equation 4)—to derive the energy 
demand. The value of charging frequencies can be 
obtained by surveys or a vehicle’s onboard diagnostic 
(OBD) system (Table 3).   
Equation 4
di is EV i’s daily mileage (km) 
F  is charging frequency (the number of days since 
last charge)
R is the battery range (km) 
3. DC fast charging estimation. When DC fast 
chargers or ultra-fast chargers in public charging 
stations are used, the vehicle’s SOC is likely to be 
dropped to a low level, compared with the previous 
two cases. The model default input uses a beta 
distribution with the mean SOC value setting at 20 
percent. Xue et al. (2020) examined the charging 
sessions of 70,375 private EVs in Beijing that use 
DC fast chargers based on OBD data and discovered 
that the distribution of the SOC fit a beta distribution 
with a mean of 20 percent. Empirical surveys of the 
charging habits of 8,300 EVs in the United States also 
show that the starting SOC for DC fast chargers peak 
around 20–30 percent (INL 2015).
Figure 6 shows the probability distributions of starting 
SOC using different estimation approaches. Significant 
variations exist: using 30 km as the average daily mileage 
(see Box 1), starting SOC is around 70–90 percent for 
one to three days per charge and 45–65 percent for 
five days per charge, and a mean of 20–30 percent is 
found for DC fast charging. As a rule of thumb, the daily 
mileage estimation and multiday estimation approaches 
are common for the Residential and Office Use Cases; the 
DC fast charging estimation is best applied to the Public 
Use Case in which DC fast chargers are used (INL 2015; 
Morrissey et al. 2016; Xue et al. 2020). 
However, besides the three starting SOC estimation 
methods, the model also allows users to directly specify 
any possible distribution for charging starting SOC 
through surveys or OBD data analysis (Table 4).   
ETi= (Pc×φ) = (100% -  StartSOC i ) × C/(P c×φ)
diStartingSOC i = 100% -  R
F×diStartingSOC i = 100% -    R

12  |  
Figure 6  |  The Probability Distributions of Starting SOC Using Different Approaches
Use Case Residential Office Public
SOC 
estimation 
method
•  Daily mileage estimation
•  Multiday estimation
•  Daily mileage estimation
•  Multiday estimation
•  DC fast charging estimation
•  Multiday estimation
Notes: DC = direct current; SOC = state of charge.
Source: WRI China authors.
For managed charging and V2G, the charging duration 
is defined the same as the parking duration (that is, a 
model input). This provides enough time flexibility for 
managed charging or V2G control, but VGI may not 
work well for short parking durations. Since the EV’s 
arrival time is a model input, parking duration is a 
proxy of the EV’s departure time. If an EV is timed to 
leave early, it will have a shorter parking duration than 
other EVs. In the web application, to reduce the model 
input burdens for users, a constant parking duration 
for all EVs is applied, but users can tailor each EV’s 
parking duration in the Python script.
One day per charge Three days per charge Five days per charge DC fast charge
Number of charging sessions
Starting SOC
1000 20 40 60 80
0
10
8
6
4
2

Simulator to Quantify and Manage Electric Vehicle Load Impacts on Low-Voltage Distribution Grids
TECHNICAL NOTE  |  December 2020  |  13
Box 1  |  Electric Vehicle Kilometers Traveled per Year
Because of factors such as battery range, charging facilities shortages, range anxiety, and the self-selection of those choosing to use 
electric vehicles (EVs), the EV kilometers traveled (eVKT) per year is lower than the annual VKT of internal combustion engine (ICE) 
vehicles (Speidel and Bräunl 2014). According to the Idaho National Laboratory (2015), the annual average eVKT in the United States was 
around 15,366–15,606 kilometers (km; a daily distance of approximately 42 km), whereas the annual VKT for ICE vehicles was 18,259 km (a 
daily distance of approximately 50 km). 
Besides distinctions between vehicle technologies, annual VKT also varies by country and city. Because of the differences in built 
environment, vehicle ownership, and travel demand management requirements, China’s annual VKT for ICE vehicles averaged around 
13,000–13,500 km in 2016 (a daily distance of around 35 km) (Ou 2019), lower than the U.S. average of 18,259 km (a daily distance of around 
50 km). Based on the onboard diagnostic analysis of 230,000 private EVs in selected Chinese cities in 2018 (Xue et al. 2020), the annual 
eVKT is around 10,950 km (a daily distance of approximately 30 km). 
As manufacturers continue to increase battery ranges, the daily mileage of EVs is also expected to increase, becoming comparable to 
that of ICE vehicles. The simulator uses the VKT distribution of ICE vehicles in China as the default eVKT. However, users can tweak the 
deviation of the VKT distribution to the specific context in the Python script.   
Figure B1.1  |  A Comparison of eVKT and VKT in China
Notes:  For a city, region, or country, the vehicle kilometers traveled (VKT) and electric vehicle kilometers traveled (eVKT) of all private cars follow a lognormal distribution 
with different means and deviations (Plotz et al. 2014). In the above chart, eVKT distribution is lognormal (μ=3.44,σ=0.532) and VKT distribution is lognormal 
(μ=3.67,σ=0.532).
Source: WRI China authors.
Daily mileage of fossil fuel vehicles Daily mileage of plug-in electric vehicles
Percent of vehicle days driven
Daily VKT (km)
1000 20 40 60 80
0
30
25
20
15
10
5

14  |  
Charging power.  Charging power rates are 
differentiated between user-specified charging power 
rates (in the case of unmanaged charging) and controlled 
charging power rates (managed charging or V2G). 
For unmanaged charging, charging power is the power 
rate of the charging facilities. Different use cases have 
different types of charging facilities (see Table 3). For 
some use cases, such as the residential setting, where 
multiple types of chargers are available (Level 1 and 
Level 2), the tool allows users to specify up to two 
types of chargers and the number of EVs that use each 
type of charger.  
For managed charging or V2G, (dis)charging power 
is controlled by a second party, such as a charging 
point operator or distribution system operator, and 
the power rates are assigned dynamically to vehicles, 
depending on the load demand and the capacity of the 
transformer (or substation); model users only need to 
specify the upper and lower limits of the (dis)charging 
power allowed by the vehicle (Table 3). For example, 
a Nissan Leaf can only take the lower limit of 1.3–1.5 
kW; otherwise, it will be locked out and disconnected 
from the charging. 
All of the model inputs can be tailored by users to 
reflect the situation at the specific location. Tailored 
model inputs for current travel and charging behaviors 
can be obtained in three ways (Table 4):
 ▪ Charging point operators can provide detailed 
charging session information for sites. Such data 
often include EV arrival times and charging powers. 
However, each EV’s charging frequencies, starting 
SOC, daily mileage, and parking duration are not 
traceable from this approach. 
 ▪ OBD data, which monitor battery performance 
almost in real time, can provide insights into charging 
starting SOC and daily mileage from sampled vehicles 
or all the vehicles visiting the site. Upon agreement 
with the EV owner, the OBD data are transported via 
the vehicle’s telematic systems.
 ▪ Community-level travel surveys conducted by 
model users or site owners can sample EV owners or 
all EV owners visiting a site. Typical surveys include, 
but are not limited to, questions about how often the 
owner charges the car at the site; the typical SOC when 
starting a charging session; the average daily mileage; 
and how long, on average, the car is parked at the site.
Table 3  |  Types of Chargers Used in Different Modules and Use Cases
Residential Office Public
Unmanaged charging module:
Types of chargers and power 
ranges
• Level 1
• Level 2
• Level 2 •   Level 2 and direct current (DC) 
fast charging 
Vehicle-grid integration modules:
Types of chargers and power 
ranges • Level 2 •  Level 2 •  Level 2 and DC fast charging
Lower limit of charging power The lower charging power limits allowed by electric vehicles
Notes: Level 1: 1.4–3.4 kW; Level 2: 3.4–19.2 kW; DC fast charging >20 kW.
Source: WRI China authors.

Simulator to Quantify and Manage Electric Vehicle Load Impacts on Low-Voltage Distribution Grids
TECHNICAL NOTE  |  December 2020  |  15
The model inputs can be predictive, such as when 
users conduct a scenario analysis to project the future 
load impacts of EV charging on the distribution grid. 
Predictions require assumptions about charging 
behaviors—whether they will remain the same or 
change in the future. For example, at present, in the 
residential setting, EV owners tend to charge the 
vehicles on a daily basis. But this behavioral pattern 
could evolve into multiple days between charges 
as battery ranges increase over time (Amsterdam 
Roundtable Foundation and McKinsey 2014; Charilaos 
et al. 2017; Van den Hoed et al. 2019; Vermeulen et 
al. 2019). Because the evolution of future charging 
behavior is uncertain, users can run the model multiple 
times, each time with different inputs, to assess the EV 
load impacts of different charging behaviors.   
Table 4  |  Comparison of Three Collection Methods for Model Inputs 
Data Collection from Charging 
Point Operators
Vehicle OBD and Telematic 
System Community-Level Travel Survey
Arrival time √ √ √
Charging starting SOC  √ √
Charging frequencies  √ √
Daily mileage  √ √
Charging power √ √ √
Parking duration √ √
Notes: OBD = onboard diagnostic; SOC = state of charge. “√” indicates the input is available through the indicated approach. 
Source: WRI China authors.
4.3  Model Methodology
4.3.1  The Unmanaged Charging Module 
The unmanaged charging module employs the Monte 
Carlo simulation to evaluate the grid impacts of 
unmanaged charging. The Monte Carlo simulation 
is used to initiate the beginning state of each EV, 
including arrival time, charging starting SOC, and 
daily mileage, by randomly drawing values from the 
probability distributions. Then, using the method 
and equations outlined in Section 4.2, the module 
calculates each EV charging profile and sums up to 
obtain the total EV charging load. The Monte Carlo 
simulation repeats the above process until a targeted 
number of iterations is met (iterations = 25; see 
Figure 7). The total load is the final EV charging load 
(that is, the average of EV loads generated from each 
iteration) plus the base load. By summing up the final 
EV charging load and the base load, the total load can 
be obtained to evaluate EV grid impacts.

16  |  
Figure 7  |  The Unmanaged Charging Module Flowchart
Notes: EV = electric vehicle; SOC = state of charge.
Source: WRI China authors.
Number of EVs in each
use case and EV performance
EV travel and charging behaviors  
in each use case
No
No
Yes
Yes
Monte Carlo simulation
Each EV i = 1:N
Total load profile
Initialization: sample plug-in time,
daily mileage (or starting SOC)
Sum EV charge profiles across the fleet
Pt = ∑i=1:N Pi,t
Base load for 
each use case
Unmanaged charge:
•  Plug-in time = start charging; end charging 
SOC = 100%; constant charging power
•  Calculate charging duration, and populate 
charging  profile Pi,t
i = N?
Iteration numbers achieved?

Simulator to Quantify and Manage Electric Vehicle Load Impacts on Low-Voltage Distribution Grids
TECHNICAL NOTE  |  December 2020  |  17
4.3.2  The Managed Charging and V2G Modules
As stated in Section 4.1, the managed charging and V2G 
technologies have limited applicability—mainly in the 
use cases with relatively short charging durations and 
long parking dwell times.    
The two VGI modules employ both the Monte Carlo 
simulation and linear programming to derive optimal 
charging (or discharging) profiles that meet specific 
grid service objectives and EV travel demands. These 
objectives include avoiding large investments for 
distribution grid upgrades and ensuring that EVs are 
sufficiently charged (or sufficiently recharged after 
discharging) so that EV owners are ready for the next 
day’s travel.  
The flow of the two VGI modules is as follows: First, the 
Monte Carlo simulation is used to initiate the beginning 
state of each EV in the site. Then, the linear programming 
function creates an empty charging (or discharging) 
profile as the variable to be optimized (that is, singleEV_
charge_profilei,t and singleEV_discharge_profilei,t, as in 
Appendix C), and the charging (or discharging) profile 
for each EV (i) is determined at each time interval (t) 
within the arrival time and departure time, based on an 
optimization procedure. In other words, the optimization 
procedure of linear programming will dynamically 
control when individual EVs charge (or discharge) and 
how much power they use to charge (or discharge), 
including delaying or prioritizing an EV to charge later 
or earlier given each EVs specific travel demand. Figure 
8 shows different possible charging profiles generated by 
the optimization procedure. By summing up all the EV 
loads, the total EV load and the impact on the grid can be 
obtained (Figure 9).
To create an optimization procedure, the linear 
programming function needs to establish one optimization 
objective function and a series of constraints. It also must 
employ a linear programming optimizer to solve for the 
optimized charging (or discharging) profile of each EV: 
 ▪ The default objective function in the model is to 
minimize the difference between peak load and valley 
load on the transformer or the substation—that is, to 
flatten the total load curves by shaving the peak load 
and filling the valley load. As a result, not only can the 
distribution grid expansion be avoided due to peak 
shaving, but the costs for utilities and customers can 
be reduced because EVs are charging at the relatively 
cheap (valley) hours. But users can specify their own 
Figure 8  |  Managed Charging Profiles for Individual EVs
Notes: Hybrid includes the three different managed charging profiles combined—postpone, cut and divide, and lower power. 
Source: WRI China authors.
Unmanaged charging Managed charging: postpone Managed charging: hybridManaged charging: cut and divide Managed charging: lower power
Charging profile (kW)
Time of day: hour
00:00 1:00 2:00 3:00 4:00 5:00 6:00 7:00 8:00 9:00 10:00 11:00 12:00 13:00 14:00 15:00 16:00 17:00 18:00 19:00 20:00 21:00 22:00 23:00
0
8
7
6
5
4
3
2
1

18  |  
objective function in the Python script; for example, 
if the objective of managed charging is to minimize 
utility costs, then the objective function can be 
specified to minimize the sum of the hourly utility cost 
(that is, the hourly load multiplied by the hourly utility 
rate) (Table 5).  
 ▪ The model constraints applied to each EV help the 
optimizer search for the best VGI control strategy for 
the vehicle that will both meet the objective function 
and avoid interfering with the EV owner’s travel 
demand. For example, if an EV has to leave earlier 
than usual, its parking duration (as specified by the 
model user) will be shorter, so the optimizer will 
automatically prioritize the car to charge early and 
Table 5  |  Objective Functions to Be Selected by Different Stakeholders
Stakeholders  Objective Functions
Transmission system operator 
Least increases in system peak load  
(Base load: system loads)
•  Minimize difference between peak load and valley load              
•  Minimize peak load 
Distribution system operator 
Least investments on distribution upgrade
(Base load: distribution loads)
•  Minimize local peak-valley load difference                                
•  Minimize local peak load
EV user
Least cost on utility tariffs
•  Minimize utility cost = ∑ t=1:24 hourly load profilet × hourly utility tariff
a
•  Minimize demand charge = peak load × demand charge
Notes: a The utility tariff can be fixed rate or time-of-use rate. 
Source: WRI China authors.
possibly at a full power rating to meet its parking 
duration constraint.8 Also, for managed charging and 
V2G, it is assumed that there is an infinite number 
of smart chargers (or V2G chargers) provided on the 
site; therefore, charger availability is not considered 
a constraint. The default model constraints are listed 
and explained in Table 6. 
Only the Python script version of the simulator allows for 
tailoring the objective function and the constraints to a 
specific site (for an example, see Appendix C). When the 
tool is being used to control the charging of each car at a 
site (as opposed to being used as a simulator to estimate 
load), different arrival and departure times can be 
specified for individual cars in the Python script.

Simulator to Quantify and Manage Electric Vehicle Load Impacts on Low-Voltage Distribution Grids
TECHNICAL NOTE  |  December 2020  |  19
Table 6  |  List of Constraints for Linear Programming 
No. Purpose of the Constraint Equation and Defaults Modules Adaptability
1 Define EV’s parking duration
a
 t ∈ [starttime(i), starttime(i)+Parkingduration] Managed 
charging, V2G
√
(redefine parking 
duration)
2
Define upper and lower limits 
of charging (or discharging) 
power
singleEV_charge_profilei,t ∈ [3kW,7kW],   
singleEV_discharge_profilei,t ∈ [-7kW,-3kW]
Managed 
charging, V2G
√
(redefine upper and 
lower limits)
3 Define charging starting state 
of charge (SOC) SOCi,starttime(i) = StartSOCi  Managed 
charging, V2G --
4 Update SOC at each time 
interval 
SOCi,t = SOCi,t-1 + single_charge_profilei,t-1 × (φ/C) 
+ single_discharge_profilei,t-1 * (k/C)   
Managed 
charging, V2G --
5 Define charging end SOC SOCi,endtime(i) = 100% Managed 
charging, V2G ◦
6 Define maximal depth of 
discharging SOCi,t ≥30% V2G ◦
7
Require that an EV cannot 
charge and discharge at the 
same time
singleEV_charge_profilei,t × singleEV_discharge_profilei,t = 0 V2G --
Notes:  “√” indicates the constraint is tweakable in both the online application and the Python script. “◦” indicates the constraint is only tweakable in the Python script. “--” indicates the 
constraint should be kept unchanged.   
a A constant parking duration for all EVs is applied to reduce the model input burdens for users, but users can alter each EV’s parking duration in the Python script.
Source: WRI China authors.

20  |  
Figure 9  |  Flowchart of the Two VGI Modules
Notes: EV = electric vehicle; LP = linear programming; VGI = vehicle-grid integration.
Source: WRI China authors.
Number of EVs in each
use case and EV performance
EV travel and charging behaviors  
in each use case
No
No
Yes
Yes
Monte Carlo simulation
Each EV i = 1:N
Total load profile
Initialization: sample plug-in time,
plug-out time, and daily mileage
Sum EV profiles across the fleet
Pt = ∑i=1:N Pi,t
Base load for 
each use case
Smart Charge:
•  Construct the charge profile for the vehicle i, Pchargei,t
•  Formulate objective function and constraints
•  Optimize EV profile (Pi,t ) using linear programming
V2G:
•  Construct the charge (and discharge) profile for the 
vehicle i, Pchargei,t  , Pdischargei,t
•  Formulate objective function and constraints
•  Optimize EV profile (Pi,t ) using linear programming
i = N?
Which VGI 
strategies
Iteration numbers achieved?

Simulator to Quantify and Manage Electric Vehicle Load Impacts on Low-Voltage Distribution Grids
TECHNICAL NOTE  |  December 2020  |  21
Figure 10  |  Relationships among EV Load, Coincidence Factor, and Charging Starting Time
Notes:  EV = electric vehicle; St. Dev. = standard deviation. “EV load: total” is the sum of the unmanaged charging load, managed charging load, and V2G load. In the unmanaged charging module, 
the “EV load” equals the unmanaged charging load. The model assumes that the charging starting time in the Residential Use Case by default follows the normal distribution. Therefore, 
there is no charging event occurring during daytime hours. 
Source: WRI China authors.
4.4  Model Outputs 
The model outputs include EV load and total load 
profiles. 
4.4.1 EV Load Profiles 
EV loads at different locations and times of day provide 
insights into the features of this new customer load.   
For utility companies, EV peak loads calculated using 
the coincidence factor (Equation 1) are sufficient 
to inform infrastructure expansion decisions. The 
coincidence factor, the reciprocal of the diversity 
factor, reflects the maximal number of EVs that 
can charge simultaneously in different use cases. 
The higher the coincidence factor, the greater the 
impact EVs are likely to exert on the electric grid. 
Since EV loads are a new type of customer load, the 
coincidence factors of existing customer loads may 
not apply. The coincidence factors derived from this 
model are instrumental for determining their values. 
For example, preliminary results show that the 
coincidence factors of EV charging are highly variable 
and are particularly correlated with travel behaviors 
such as arrival time. If EV arrival times to the site 
are concentrated within 2 hours, the coincidence 
factor could be as high as 35–40 percent (Figure 10). 
However, if the arrival times for most of the EVs are 
spread within 6 hours, the coincidence factor could 
drop to around 14 percent.  
St. Dev. of charging starting time: 3hours 
Coincidence factor: 14%
Peak EV load: 780 kW
St. Dev. of charging starting time: 1hour 
Coincidence factor: 37%
Peak EV load: 2,067 kW
Residential Use Case: 800 EVs
Load: kW
Load: kW
Time of day: hour Time of day: hour
0 05 510 1015 1520 20
0 0
2,500 2,500
2,000 2,000
1,500 1,500
1,000 1,000
500 500
EV load: unmanaged chargingEV load: total

22  |  
4.4.2 EV Load Impacts 
The total load profile—the sum of the EV charging 
load and the base load—provides a full picture of EV 
load impacts. Based on the total load profiles, the key 
concerns of utility companies, such as the overloading 
problem and the utilization efficiency of transformers 
(or substations), can be answered (Table 7):
 ▪ Overloading. Output indicators, such as peak 
load and the utilization factor, are instrumental for 
examining if the peak load demand exceeds the rated 
capacity of the transformer (or substation). In fact, 
the limit set for grid expansion varies from country 
to country. For example, China would usually cap 
the limit at 80 percent of the rated capacity, whereas 
other countries would cap at 100 percent of the rated 
capacity. In the model output, besides the rated 
capacity, the model output gives a warning at 80 
percent of the rated capacity to alert users that the 
transformers are approaching the point for expansion.    
 ▪ Utilization efficiency. The output indicator for the 
peak-valley load difference is used to evaluate if the 
investments on electrical resources (from generation, 
transmission, and distribution) are utilized efficiently. 
The higher the difference, the more capacity is 
required for the transformer (or substation) to 
accommodate the same energy demand. Also, it 
becomes less cost-effective to operate the grid system; 
hence, the utilization of the devices is inefficient. 
Figure 11 presents an example of the Residential Use Case. 
The charts in the first row display EV loads under different 
charging strategies, and those in the second row show the 
overall load impacts on the substation. Under unmanaged 
charging, the peak load is 234 kW over the rated capacity 
(4,000 kW) of the substation. Not only will the substation 
be overloaded, but the higher load demand will also lead to 
inefficient use of the transformers in the substation. This is 
because the peak power demand occurs for only one to two 
hours a day, and then the demand drops to and maintains 
a very low level for the rest of the day. However, with 60 
percent of the EVs participating in managed charging (the 
other 40 percent keep performing unmanaged charging9), 
the peak load is flattened, and some EV charging load is 
shifted to the off-peak night hours.      
Table 7  |  Model Output Indicators and Calculation Equations
Output Indicator Explanation Equation Limit for Grid Expansion
Overloading
Peak load
(maximum hourly load) Maximum hourly total load peak load = max t=1:24  ( total_load t ) 80–100% 
× rated capacity 
Utilization factor Ratio of peak load to the 
capacity of the transformer(s) utilization = peak load / rated capacity 80–100%
EV ratio in peak load Ratio of EV load in the peak 
load EVratio = EV_loadmax_t / peak load --
Utilization
inefficiency 
Peak-valley load 
difference
Difference between peak total 
load and valley total load
valley load = mint=1:24 ( total_load t)
diff = peak - valley --
Source: WRI China authors.

Simulator to Quantify and Manage Electric Vehicle Load Impacts on Low-Voltage Distribution Grids
TECHNICAL NOTE  |  December 2020  |  23
Figure 11  |  An Example of EV Load Impacts in a Residential Use Case
Notes:  EV = electric vehicle; V2G = vehicle-to-grid. “EV load: total” is the sum of the unmanaged charging load, managed charging load, and V2G load. In the unmanaged charging module, the 
“EV load” equals the unmanaged charging load.
Source: WRI China authors.
Unmanaged Charging Managed Charging V2G
EV enrollment •  Unmanaged charging: 800 EVs •  Unmanaged charging: 480 EVs
•  Managed charging: 320 EVs 
•  Unmanaged charging: 640 EVs
•  V2G: 160 EVs
Utilization factor (%) 106 76 53
Peak load (kW) 4,234 3,044 2,127
EV ratio in peak load (%) 49 -- --
Peak-valley difference (kW) 3,034 1,610 693
Residential Use Case: 800 EVs, 800 chargers
Unmanaged charging
Unmanaged charging
Managed charging
Managed charging
V2G
V2G
EV load: total EV load: unmanaged charging EV load: managed charging
EV load:
Total load:
EV load: V2G
EV load Base load Total load/EVRated capacity 800 of rated capacity
Load: kWLoad: kW
Load: kWLoad: kW
Load: kWLoad: kW
Time of day: hour
Time of day: hour
Time of day: hour
Time of day: hour
Time of day: hour
Time of day: hour
0
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
5
10
10
10
10
10
10
15
15
15
15
15
15
20
20
20
20
20
20
-1,000
-1,000
0
0
-1,000
-1,000
0
0
-1,000
-1,000
0
0
5,000
5,000
5,000
5,000
5,000
5,000
4,000
4,000
4,000
4,000
4,000
4,000
3,000
3,000
3,000
3,000
3,000
3,000
2,000
2,000
2,000
2,000
2,000
2,000
1,000
1,000
1,000
1,000
1,000
1,000

24  |  
5. HOW TO USE THE MODEL 
5.1 Model Input and Function Updates
Although the simulator offers default inputs, location-
specific updates are necessary to contextualize the 
model. The following provides tiered options to update 
the model (Figure 12):
 ▪ If users do not have information on daily EV travel 
and charging patterns, the model’s default values 
are sufficient to perform a rough estimation of EV 
load impacts. The bare-minimum updates required 
for the model include the number of EVs, vehicle 
technical specifications, the number of chargers, 
charging power rates, and local transformer (or 
substation) information (including daily base load 
and rated capacity). 
 ▪ If users have access to rough estimates of charging 
and travel patterns through charging point operators, 
vehicle OBD systems, or community surveys (see 
Section 4.2), additional updates can be made. These 
updates include tailoring vehicle arrival times and 
the charging starting SOC.  
 ▪ If users have thorough information on charging 
and travel behavior and would prefer additional 
functions beyond what are offered by the web 
application, they can work with the Python script 
to redefine the behavioral inputs (e.g., respecifying 
the daily mileage distribution, changing the 
normal arrival time distribution into other best-
fit distributions, or refining an individual EV’s 
departure time), change the model assumptions, 
or improve the model functions by revising the 
optimization objective and constraints. 
To demonstrate how to use the online tool to perform 
both the bare-minimum and advanced updates, two 
examples are given here. Users who are interested in 
tweaking the Python scripts for extended functions and 
better flexibility, please refer to Appendix C. 
Figure 12  |  Tiered Updates on the Simulator
Source: WRI China authors.
Systematic updates
(Python script only)
Bare-minimum updates
•   Basic updates: Transformer information 
(such as rated capacity or base load), 
number of EVs and charge points, vehicle 
performance, charging powers
•   Fine-tune behavioral inputs:  Charging and 
travel behaviors (arrival time, starting state of 
charge)
•   Update model inputs, assumptions, and 
functions: Respecify the probability distribution 
of charging and travel behaviors, revise underlying 
assumption, or update optimization objectives
Advanced updates

Simulator to Quantify and Manage Electric Vehicle Load Impacts on Low-Voltage Distribution Grids
TECHNICAL NOTE  |  December 2020  |  25
Table 8  |  Functional Differences between the Web Application and the Python Script
Notes:  SOC = state of charge; V2G = vehicle-to-grid. 
a  For simplicity, the web application allows for the tailoring of a single parking duration value applied to all electric vehicles. If more fine-grained parking duration information can be 
gathered, the constraint should be revised in the Python script. 
Source: WRI China authors.
Web Application Python Script
Modules
Modules •  Unmanaged charging 
•  Managed charging
•  Unmanaged charging
•  Managed charging
•  V2G
Model inputs
Distribution of daily mileage Fixed lognormal distribution that cannot be 
changed
Any type of probability distribution defined by 
model users
Distribution of arrival time and starting 
state of charge (SOC)
Normal distribution; users can change the 
means and the deviations
Any type of probability distribution defined by 
model users
Parking duration One value defined by model users
a Any value defined by model users or any type of 
probability distribution defined by model users
Model assumptions
End SOC 100%
Any value defined by model users or
any type of probability distribution defined by 
model users
Charging or discharging efficiency 90% Any value defined by model users
Maximum depth of discharging 30% Any value defined by model users
Number of managed chargers or V2G 
chargers Indefinite Subject to model users’ specifications
Functions
Optimization objective Fixed (minimize peak-valley difference) Subject to model users’ specifications
Constraints Fixed Subject to model users’ specifications

26  |  
5.1.1   Example 1: Bare-Minimum Updates Using the 
Web Application 
With the increasing adoption of EVs in residential 
neighborhoods, distribution substations risk being 
overloaded. Distribution system operators who 
are responsible for planning grid expansion need 
to understand when the capacity of distribution 
substations will become insufficient. To solve the 
problem, users need to use the unmanaged charging 
module in the Residential Use Case.  
To ease the input burdens for users, the model inputs are 
simplified into the features of an average EV. For example, 
the online tool assumes that the average EV battery capacity 
in a neighborhood setting is around 45 kWh and the 
average efficiency is 15 kWh/100 km in 2020. The arrival 
time and the time range are the mean and deviation used to 
fit a normal distribution—that is, assuming the arrival times 
of the EVs follow the normal distribution with the mean 
time at 18:00 and one-hour deviation in 2020. 
Numerous uncertainties exist in the future. Users 
can assume that in 2025 the number of EVs in the 
neighborhood will increase to 400 and average battery 
capacity and energy efficiency will change to 50 kWh 
and 13 kWh/100 km, respectively. Other potential 
future changes are listed in Figure 13.  
Figure 13  |  Model Inputs for Example 1
Note: EV = electric vehicle; kVa = kilovolt-ampere. 
Source: WRI China authors.
2020 2025
Number of EVs 10 400
Vehicle battery capacity 45 kWh 50 kWh
Energy efficiency 15 kWh/100 km 13 kWh/100 km
Charging frequency 2 days per charge 4 days per charge
Arrival time 18:00 19:00
Time range of arrival time 2 hours 2 hours
a. Inputs for 2020   b. Inputs for 2025

Simulator to Quantify and Manage Electric Vehicle Load Impacts on Low-Voltage Distribution Grids
TECHNICAL NOTE  |  December 2020  |  27
Figure 14 shows the results from using the above inputs 
to run the model twice and comparing the results from 
these two runs. With the increase in EV stocks in 2025, 
the EV charging load will become the major residential 
load, especially from 17:00 to 00:00. This increase in 
EV charging load will overload the substation, with the 
4,658 kW peak load exceeding the current rated capacity 
of 4,000 kVa. If no managed charging strategies are 
deployed, the substation will require a capacity increase 
of 658 kW to accommodate the EV charging load.    
Figure 14  |  Model Outputs of Example 1
Note:  EV = electric vehicle. The model assumes that the charging starting time in the Residential Use Case by default follows the normal distribution. Therefore, there is no charging session 
occurring during daytime hours.  
Source: WRI China authors.
5.1.2   Example 2: Premium Updates Using the Web 
Application
For freight operators, the electrification of freight fleets 
could lead to costly upgrades of the distribution grid because 
most EVs tend to return to a depot and be charged at the 
same time. However, if using managed charging to stagger 
the charging time and optimize the charging power of the 
electric fleet, the costly grid expansion can be avoided. This 
corresponds to a new use case: unmanaged charging and 
managed charging in the User-Defined Use Case.   
To create a new use case for the freight operator 
example, the following inputs need updates (Figure 15). 
Total Load Total Load
Load: kW
Load: kW
Time of day: hour Time of day: hour
0 05 510 1015 1520 20
0 0
4,000 5,000
4,5003,500
3,000
3,500
4,000
3,0002,500
2,000
2,000
2,500
1,500
1,500
1,000
500
1,000
500
EV load Base load Total load/EVRated capacity 800 of rated capacity

28  |  
The arrival time and starting charging SOC of the fleet 
will need to be revised based on the operation schedule. 
Here, this example assumes the arrival time of the fleet 
is concentrated around 18:00 and follows a normal 
distribution with a two-hour deviation. The mean of the 
starting charging SOC for the fleet is 40 percent, with a 
20 percent deviation. Furthermore, the use case assumes 
that the fleet depot has dedicated transformers (base 
load = 0) and the rated capacity of the transformers can 
accommodate no more than 60 charging points, with a 
maximum charging power output of 40 kW. The number 
of charging points is lacking in comparison to the 
150-vehicle fleet size. 
To compare the effects of managed charging, users need 
to run the tool under both unmanaged charging and 
managed charging and compare the results from the 
two runs. 
Figure 15  |  Model Inputs of Example 2
Unmanaged Charging Managed Charging
Vehicle battery capacity 150 kWh 150 kWh
Energy efficiency 75 kWh/100 km 75 kWh/100 km
Number of EVs 150 150
Number of chargers 60 60
Charging power 40 kW --
Average charging starting SOC 40% 40%
Range of starting SOC 40% 40%
Arrival time 18:00 18:00
Time range of arrival time 4 hours 4 hours
Vehicles participating in managed charging -- 80%
Parking duration -- 8 hours
Charging power upper limit -- 40 kW
Charging power lower limit -- 10 kW

Simulator to Quantify and Manage Electric Vehicle Load Impacts on Low-Voltage Distribution Grids
TECHNICAL NOTE  |  December 2020  |  29
Figure 15  |  Model Inputs of Example 2: (cont.)
Note:  EV = electric vehicle; SOC = state of charge; St. Dev. = standard deviation.  
Source: WRI China authors.
Arrival time  
Normal distribution
Charging starting SOC 
Normal distribution
Mean: 18:00, St. Dev.: 2hours Mean: 40%, St. Dev.: 20%
Number of vehicle trips
Number of charging sessions per day
Time of day: hour Starting SOC: %
1000 20 40 60 800 5 10 15 20
0 0
200 200
175 175
150 150
125 125
100 100
75 75
50 50
25 25

30  |  
Under unmanaged charging, the modeled peak load 
is 2,396 kW, exceeding the 2,000 kVa rated capacity 
of the transformer. Because of the lack of charging 
facilities, the average waiting time for each freight 
vehicle to be charged is nearly five hours. However, 
if deploying managed charging, the peak load can be 
reduced. Considering that public acceptance of managed 
charging and V2G is still limited at the early stage of the 
adoption, users are encouraged to specify a fraction of 
EVs to participate in managed charging or V2G in the 
VGI modules (the default value is set at 10 percent), 
Figure 16  |  Model Outputs of Example 2
with the rest of the EVs continuing to use unmanaged 
charging. In this example, assuming 80 percent of the 
fleet participates in managed charging, the managed 
charging power fluctuates between 10 kW and 40 kW, the 
model results show that the peak load is shaved to 1,094 
kW (Figure 16). Compared to the unmanaged charging, 
the peak load reduces by 53 percent, and the optimized 
load curve is flattened. This occurs without affecting the 
daily operation of the fleet. 
Note:  EV = electric vehicle.  
Source: WRI China authors.
Unmanaged Charging Managed Charging
Peak load 2,369 kW 1,094 kW
Utilization factor 120% 55%
User-Defined Use Case: 150 EVs, rated capacity: 2,000 kVa
Load: kW
Load: kW
Total Load Total Load
Time of day (hour) Time of day (hour)
0 05 510 1015 1520 20
0 0
2,500 2,000
2,000
1,500
1,500
1,000
1,000
500
500
Unmanaged Charging Managed Charging
EV load Base load Total load/EVRated capacity 800 of rated capacity

Simulator to Quantify and Manage Electric Vehicle Load Impacts on Low-Voltage Distribution Grids
TECHNICAL NOTE  |  December 2020  |  31
Figure 17  |   Sensitivity Analysis of Vehicle Energy Efficiency, Charging Frequencies, and the Number of 
Chargers under Unmanaged Charging
Note:  EV = electric vehicle.  
Source: WRI China authors.
Note:  Charging frequency is three days per charge; energy efficiency = 17.4 kWh/100 km. Note:  Charging frequency is three days per charge; energy efficiency = 17.4 kWh/100 km.
5.2 Sensitivity of Model Inputs 
Numerous model inputs have a bearing on EV load 
impacts. For users who aim to forecast long-term 
EV load impacts, the following shows how the future 
technology advances or behavior changes in selected 
variables will affect EV charging loads (Figure 17).
 ▪ Vehicle electrification. The increased number 
of EVs will be the key influencing factor on EV grid 
impacts. 
 ▪ Number of chargers. The shortage of charging 
facilities will cap EV charging loads and reduce EV 
grid impacts (but will also slow the rate of vehicle 
electrification).     
 ▪ Vehicle energy efficiency. When EVs become 
more energy efficient, the energy they draw from the 
grid will be less, and the overall EV loads will drop.  
 ▪ Charging frequency.  When EV battery ranges 
increase and drivers charge EVs less often, EVs will 
tend to draw more energy from the grid at each 
charging session. If the coincidence factor keeps 
constant, the EV load will grow significantly.
c. Vehicle Energy Efficiency (EF) d. Charging Frequency
b. Number of Chargers
EV load (kW) EV load (kW) 
EV load (kW) EV load (kW) 
a. Number of EVs
Residential Use Case: 800 EVs
Time of day
Time of day Time of day
Time of day
22
22 22
220
0 0
02
2 2
24
4 4
46
6 6
68
8 8
810
10 10
1012
12 12
1214
14 14
1416
16 16
1618
18 18
1820
20 20
20
0
0 0
0
2,000
2,000 2,000
2,000
1,600
1,600 1,600
1,600
1,200
1,200 1,200
1,200
800
800 800
800
400
400 400
400
1,000 EVs 1,200 EVs400 EVs
EF = 17 .4 kWh/100 km 1 day per chargeEF=14.2 kWh/100 km 3 days per chargeEF=10 kWh/100 km 5 days per charge
800 chargers 150 chargers 100 chargers400 chargers 200 chargers800 EVs

32  |  
6. LIMITATIONS 
Although the simulator can capture and model most of 
the use cases, it has a number of limitations.
The simulator is inadequate to model vehicles that 
charge more than once a day. This is because it is 
difficult to characterize model inputs such as arrival 
time and charging starting SOC when EVs charge 
frequently within a day. The EVs that charge more than 
once a day are typically operating fleets, and because 
fleet operators follow strict operation schedules, their 
grid impacts can be calculated based on the operation 
schedules. Also, to obtain optimal load results for some 
operating fleets, operational schedules will need to 
be adjusted to optimize vehicle arrival and departure 
times. Users can refer to dedicated software like 
HASTUS to perform this type of optimization.

Simulator to Quantify and Manage Electric Vehicle Load Impacts on Low-Voltage Distribution Grids
TECHNICAL NOTE  |  December 2020  |  33
APPENDIX A.  MODEL VARIABLES 
Table A1 shows the matrix of the model input variables. 
It is noteworthy that all of the model variables listed in 
the table are tailorable by users. The model variables 
also vary by use cases and charging strategies; for 
example, Level 1 chargers (slow chargers) are not 
common for the Office and Public Use Cases.  
Table A1  |  Model Inputs by Use Cases and Modules
Variable Unit Data Type Applicability Residential Office Public User-Defined
Base load kW 24-item array All the modules √ √ √ √
Rated capacity kVa Single number All the modules √ √ √ √
Battery capacity of the 
vehicle kWh Single number All the modules √ √ √ √
Vehicle energy 
efficiency kWh/100 km Single number All the modules √ √ √ √
Number of electric 
vehicles (EVs) Single number All the modules √ √ √ √
Percentage of fast 
charging vehicles % Single number All the modules √ -- -- --
Number of fast 
chargers (Level 2 and 
above)
N/A Single number All the modules √ √ √
√
(Includes all 
types of chargers)
Number of slow 
chargers (Level 1) N/A Single number All the modules √ -- -- --
Fast charging power kW Single number All the modules √ √ √
√
(Includes all 
types of chargers)

34  |  
Variable Unit Data Type Applicability Residential Office Public User-Defined
Slow charging power kW Single number All the modules √
Charging frequency Days Single number All the modules √ √
Arrival time Time Normal distribution: average 
and deviation; 24-item array All the modules √ √ √ √
Charging starting 
state of charge % Normal distribution: average 
and deviation; 24-item array All the modules -- -- √ √
Daily mileage km Single number All the modules ◦ ◦ -- --
Solar curve kW 24-item array All the modules √ √ √ √
Percentage of EVs 
that participated in 
managed charging/
V2G
% Single number VGI modules only √ √ √ √
Parking duration Hours Single number VGI modules only √ √ √ √
Charging power 
upper limit kW Single number VGI modules only √ √ √ √
Charging power lower 
limit kW Single number VGI modules only √ √ √ √
Table A1  |  Model Inputs by Use Cases and Modules (cont.)
Note:  kVa = kilovolt-ampere; VGI = vehicle-grid integration; V2G = vehicle-to-grid. “√” indicates the variable is the required input; “◦” indicates the variable is an optional input and is only 
tweakable in the Python script; “--” indicates the variable is nonexistent in the use case. 
Source: WRI China authors.

Simulator to Quantify and Manage Electric Vehicle Load Impacts on Low-Voltage Distribution Grids
TECHNICAL NOTE  |  December 2020  |  35
Source: WRI China authors.
APPENDIX B.  MODEL KEY ASSUMPTIONS 
Table B1  |  Model Assumptions (or Fixed Variables)
Variable Unit
Charging ending state of charge 100%
Charging energy efficiency 90%
Discharging energy efficiency 90%
Maximum depth of discharging 30%
Number of managed chargers or 
vehicle-to-grid (V2G) chargers Indefinite
The model also relies on the following assumptions 
(Table B1) based on existing studies (INL 2015; Xue et 
al. 2020). However, users can also tweak the values of 
the variables in the Python script.

36  |  
APPENDIX C.  EXTENDED FUNCTIONS OF THE PYTHON SCRIPTS
The Python script offers greater flexibility. Model 
users can simulate V2G’s load-shifting effects and also 
tailor all the model inputs, the model assumption, and 
specific functions in the Python script.   
The following presents an example of how to revise 
the objective function and constraints under the V2G 
strategy in the Python script.  
First, the objective function is revised from “minimize 
the peak-valley differences” to “minimize the demand 
charge.” A common demand charge scheme is applied 
here in which the demand charge is imposed on the 
peak load with a fixed rate of US$15/kW ( singleEV_
charge_profile i,t and singleEV_discharge_profile i,t are 
the optimized variables).
Minimize demand charges = local peak load × $15/kW
    Local peak load 
=  maxt=0:24  (base load t + EV_charge_load t  
+ EV_discharge_load t)
    EV_charge_load t 
=   ∑   singleEV_charge_profile i,t
    EV_discharge_load t
= k ×   ∑    singleEV_discharge_profile i,t
N     is 24 hours in a day with 1-hour intervals
Veh      is the total number of EVs in the use case 
singleEV  _charge_profile i,t and singleEV_discharge_
profile i,t are, respectively, charge power and 
discharge load of vehicle i at time t
k   is discharge efficiency (90 percent)
Second, the constraints are updated, including 
modifying the end SOC from 100 percent to 80 percent 
and adding a new constraint—the shortage in the 
number of V2G chargers. 
Subject to
1)  SOCi,starttime(i)  = StartSOC i  
2)   SOCi,t =  SOCi,t-1  + single_charge_profile i,t-1  × (φ/C)  
+ single_discharge_profile i,t-1  × (k/C)   
3)  SOCi,t ≥ 30%
4)  SOCi,endtime(i)  = 80% 
5)   singleEV_charge_profile i,t  
× singleEV_discharge_profile i,t = 0 
6)   t∈[starttime(i), endtime(i)]
7)   singleEV_charge_profile i,t ∈ [3kW,7kW],   
singleEV_discharge_profile i,t ∈ [-7kW,-3kW] 
8)   for each time t, ∑ i SingleEV_chargestate i,t  
≤ n_V2G_chargers (the number of V2G chargers is 
imposed as a constraint)
where starttime(i),  endtime(i)  are, respectively, vehicle 
i’s arrival time and departure time; SOCi,t is vehicle i’s 
SOC state at time t; φ is charging efficiency; and k is 
discharge efficiency.
i=1:Veh
i=1:Veh

Simulator to Quantify and Manage Electric Vehicle Load Impacts on Low-Voltage Distribution Grids
TECHNICAL NOTE  |  December 2020  |  37
ENDNOTES
1. Facility owners refers to energy managers of parking lots, industrial 
zones, commercial and office properties, or bus/logistic vehicle parking 
depots.  
2. A distribution substation often includes a set of transformers.  
3. EVs can charge during off-peak time periods, when the retail electric 
energy price is low, and discharge the energy during peak time periods, 
thereby reducing the costs of electricity.  
4. For more about the V2G-Sim model structure, see http://v2gsim.lbl.gov/
overview/model-structure.  
5. EV batteries are commonly discharged to about 10–30 percent of the 
state of charge (SOC); fully depleting the batteries for each discharge 
cycle will accelerate battery degradation.  
6. The energy efficiency of an EV is expressed as energy consumed per 100 
kilometers traveled.  
7. For managed charging and V2G, charging duration is enveloped by park -
ing duration. 
8. However, if the departure time is too early to allow for the vehicle to be 
fully charged, the constraint should be modified from 100 percent end 
SOC to less than 100 percent by the model user—the vehicle will not 
be charged fully given the limited parking duration. Alternatively, the EV 
owner could also opt out of the VGI measures, not to be included in the 
optimization process. 
9. Considering that public acceptance of managed charging and V2G is 
limited at the early stage, the VGI modules allow users to specify a frac -
tion of EVs to participate in managed charging or V2G, and the rest of the 
EVs remain using unmanaged charging. 
ABBREVIATIONS 
DC      direct current 
DSO    distribution system operator
EV    electric vehicle
eVKT    electric vehicle kilometers traveled
ICE    internal combustion engine
kVa    kilovolt-ampere
kWh    kilowatt-hour
OBD    onboard diagnostic
SOC    state of charge
TOU    time of use
VGI    vehicle-grid integration
VKT    vehicle kilometers traveled
V2G    vehicle-to-grid
V2G-Sim    Vehicle-to-Grid Simulator

38  |  
Smith, C.B., and K.E. Parmenter. 2016. Energy Management Principles. 2nd 
ed. Amsterdam: Elsevier.
Speidel, S., and T. Bräunl. 2014. “Driving and Charging Patterns of Electric 
Vehicles for Energy Usage.” Renewable and Sustainable Energy Reviews 40 
(December): 97–110. https://doi.org/10.1016/j.rser.2014.07.177. 
Stephens, T., J.L. Sullivan, and G.A. Keoleian. 2012. “A Microsimulation of 
Energy Demand and Greenhouse Gas Emissions from Plug-in Hybrid Electric 
Vehicle Use.” World Electric Vehicle Journal 5 (3): 789–99. https://doi.
org/10.3390/wevj5030789. 
Van den Hoed, R., S. Maase, J. Helmus, R. Wolbertus, Y. el Bouhassani, J. 
Dam, M. Tamis, and B. Jabloska. 2019. E-mobility: Getting Smart with Data. 
Amsterdam: Amsterdam University of Applied Science. 
Vermeulen, I., J.R. Helmus, M. Lees, and R. van den Hoed. 2019. “Simulation 
of Future Electric Vehicle Charging Behaviors—Effects of Transition 
from PHEV to FEV.” World Electric Vehicle Journal 10 (2): 42. https://doi.
org/10.3390/wevj10020042.
Xue, L., J Xia, R. Yu, H. Ren, Y. Liu, W. Wei, and P. Liu. 2020. Quantifying the 
Grid Impacts from Large Adoption of Electric Vehicles in China. Beijing: World 
Resources Institute. 
REFERENCES 
Amsterdam Roundtable Foundation and McKinsey. 2014. Electric Vehicles in 
Europe: Gearing Up for a New Phase? Amsterdam: Amsterdam Roundtable 
Foundation. https://www.mckinsey.com/featured-insights/europe/electric-
vehicles-in-europe-gearing-up-for-a-new-phase.
Bayliss, C.R., and B.J. Hardy. 2007. Transmission and Distribution Electrical 
Engineering. 3rd ed. Oxford, UK: Newnes.
California Energy Commission. 2018. California Plug-in Electric Vehicle 
Infrastructure Projections 2017–2025: Future Infrastructure Needs for 
Reaching the State’s Zero-Emission-Vehicle Deployment Goals. Staff Report. 
Sacramento: California Energy Commission. https://www.nrel.gov/docs/
fy18osti/70893.pdf.
CATARC (China Automotive Technology and Research Center). 2018. Annual 
Report on New Energy Vehicle Industry in China. Tianjin, China: CATARC. 
Charilaos, L., A. Sivakumar, and J. Polak. 2017. “Modeling Electric Vehicle 
Charging Behaviour:  What Is the Relationship between Charging Location, 
Driving Distance, and Range Anxiety?” Paper prepared for the 96th Annual 
Meeting of the Transportation Research Board, Washington, DC, January 
8–12. 
Gnann, T., A.L. Klingler, and M. Kühnback. 2018. “The Load Shift Potential of 
Plug-in Electric Vehicles with Different Amounts of Charging Infrastructure.” 
Journal of Power Sources 390 (June): 20–29. https://doi.org/10.1016/j.
jpowsour.2018.04.029.
INL (Idaho National Laboratory). 2015. Plugged In: How Americans Charge 
Their Electric Vehicles—Findings from the Largest Plug-in Electric Vehicle 
Infrastructure Demonstration in the World. Idaho Falls, ID: INL. https://avt.inl.
gov/sites/default/files/pdf/arra/PluggedInSummaryReport.pdf.
Morrissey, P., P. Weldon, and M. O’Mahony. 2016. “Future Standard and Fast 
Charging Infrastructure Planning:  An Analysis of Electric Vehicle Charging 
Behavior.” Energy Policy 89 (February): 257–70.
 
Munasinghe, M. 1990. Energy Analysis and Policy. Oxford, UK: Butterworth-
Heinemann.
 
Ou, S., R. Yu, Z. Lin, H. Ren, X. He, S.V. Przesmitzki, and J. Bouchard. 2019. 
“Intensity and Daily Pattern of Passenger Vehicle Use by Region and Class 
in China: Estimation and Implications for Energy Use and Electrification.” 
Mitigation and Adaptation Strategies for Global Change 24: 1607214. https://
doi.org/10.1007/s11027-019-09887-0.
Plotz, P., N. Jakobsson, F. Sprei, and S. Karlsson. 2014. “On the Distribution 
of Individual Daily Vehicle Driving Distances.” Paper prepared for the 
European Electric Vehicle Congress, Brussels, December 3–5. 
Sadeghianpourhamami, N., N. Refa, M. Strobbe, and C. Develder. 2017. 
“Quantitative Analysis of Electric Vehicle Flexibility: A Data-Driven Approach.” 
Journal of Electrical Power and Energy Systems 95 (February): 451–62. 
https://doi.org/10.1016/j.ijepes.2017.09.007.

Simulator to Quantify and Manage Electric Vehicle Load Impacts on Low-Voltage Distribution Grids
TECHNICAL NOTE  |  December 2020  |  39
ACKNOWLEDGMENTS 
We are pleased to acknowledge our institutional strategic partners, who provide 
core funding to WRI: Netherlands Ministry of Foreign Affairs, Royal Danish 
Ministry of Foreign Affairs, and Swedish International Development Cooperation 
Agency.
We are also pleased to acknowledge our strategic partner, the UPS Foundation, 
who sponsors the research.  
We would like to thank our World Resources Institute (WRI) internal reviewers, 
Emmett Werthmann, Robi Robichaud, Deepak Krishnan, Hong Miao, Robin 
King, Xiangyi Li, Su Song, Hui Jiang, and Vishant Kothari. We would also like to 
thank our external reviewers, Rongxin Yin, Jian Liu, Jianhua Chen, Anders Hove, 
and Ying Wang for their helpful comments and suggestions. 
Thank you also to Gregory Taff, Li Fang, Emilia Suarez, Romain Warnault, Lauri 
Scherer, and Emily Matthews for editing, design, administrative, and advisory 
support. 
ABOUT THE AUTHORS 
Lulu Xue is the China Urban Mobility Manager at World Resources Institute.
Contact: lxue@wri.org
Junrong Xia is the Senior Specialist at China Electric Power Research 
Institute.

40  |  
Copyright 2020 World Resources Institute. This work is licensed under the Creative Commons Attribution 4.0 International License.
To view a copy of the license, visit http://creativecommons.org/licenses/by/4.0/
10 G STREET, NE  |  WASHINGTON, DC 20002  |  www.WRI.org
ABOUT WRI 
World Resources Institute is a global research organization that turns big ideas 
into action at the nexus of environment, economic opportunity, and human 
well-being.
Our Challenge
Natural resources are at the foundation of economic opportunity and human 
well-being. But today, we are depleting Earth’s resources at rates that are not 
sustainable, endangering economies and people’s lives. People depend on 
clean water, fertile land, healthy forests, and a stable climate. Livable cities 
and clean energy are essential for a sustainable planet. We must address these 
urgent, global challenges this decade.
Our Vision
We envision an equitable and prosperous planet driven by the wise 
management of natural resources. We aspire to create a world where the 
actions of government, business, and communities combine to eliminate 
poverty and sustain the natural environment for all people.
Our Approach
COUNT IT
We start with data. We conduct independent research and draw on the latest 
technology to develop new insights and recommendations. Our rigorous 
analysis identifies risks, unveils opportunities, and informs smart strategies. 
We focus our efforts on influential and emerging economies where the future 
of sustainability will be determined.
CHANGE IT
We use our research to influence government policies, business strategies, 
and civil society action. We test projects with communities, companies, 
and government agencies to build a strong evidence base. Then, we work 
with partners to deliver change on the ground that alleviates poverty and 
strengthens society. We hold ourselves accountable to ensure our outcomes 
will be bold and enduring.
SCALE IT
We don’t think small. Once tested, we work with partners to adopt and 
expand our efforts regionally and globally. We engage with decision-makers 
to carry out our ideas and elevate our impact. We measure success through 
government and business actions that improve people’s lives and sustain a 
healthy environment.
