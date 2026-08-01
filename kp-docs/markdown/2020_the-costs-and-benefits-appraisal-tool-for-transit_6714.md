---
doc_id: 2020_the-costs-and-benefits-appraisal-tool-for-transit_6714
source_pdf: kp-docs/askwri-kps/2020_the-costs-and-benefits-appraisal-tool-for-transit_6714.pdf
extraction_method: cache-plaintext
char_count: 123832
title: The Costs and Benefits Appraisal Tool for Transit Buses (Working Paper)
authors: Li, Xiangyi; Gao, Jun; Song, Su
date_published: 10/11/2020
article_type: Technical Note
sub_tag: Transport decarbonization
wri_primary_office: WRI Global
wri_programs: Cities
language: English
url: "https://www.wri.org/research/costs-and-benefits-appraisal-tool-transit-buses"
doi: "https://doi.org/10.46830/writn.19.00147"
summary: The Costs and Benefits Appraisal Tool for Transit Buses (“the Tool”) is an updated version of the Costs and Emissions Appraisal Tool for Transit Buses. It aims to inform bus operators and city officials of the costs, emissions, and social benefits associated with bus fleets using different fuel types. The Tool’s outputs can help bus operators make the most cost-efficient decisions when making a clean bus upgrade, allow transit agencies to validate information provided by bus operators, and inform city officials of the social benefits of a low-carbon transit fleet.
---

# The Costs and Benefits Appraisal Tool for Transit Buses (Working Paper)

TECHNICAL NOTE  |  October 2020  |  1
TECHNICAL NOTE
Technical notes document the research or analytical 
methodology underpinning a publication, interactive 
application, or tool.
Suggested Citation: Xiangyi Li, Jun Gao, Su Song. 
2020. “The Costs and Benefits Appraisal Tool for 
Transit Buses.” Technical Note. Washington, DC: World 
Resources Institute. Available online at: https://www.
wri.org/publication/costs-benefits-appraisal-tool-buses.
XIANGYI LI, JUN GAO, AND SU SONG
THE COSTS AND BENEFITS APPRAISAL TOOL 
FOR TRANSIT BUSES
EXECUTIVE SUMMARY
The Costs and Benefits Appraisal Tool for Transit 
Buses (“the Tool”) is an updated version of the Costs 
and Emissions Appraisal Tool for Transit Buses. It 
aims to inform bus operators and city officials of the 
costs, emissions, and social benefits associated with 
bus fleets using different fuel types. The Tool’s outputs 
can help bus operators make the most cost-efficient 
decisions when making a clean bus upgrade, allow 
transit agencies to validate information provided by 
bus operators, and inform city officials of the social 
benefits of a low-carbon transit fleet. Compared with 
the previous version, this tool includes more default 
data on electric bus costs and operational information 
with wider geographic coverage and more bus types; 
provides social cost and benefit calculations; and 
includes simplified cost functions. Users are encouraged 
to input their own data to reflect their local situations. 
The Tool is published as a webtool ( https:// www.
wri.org/resources/data-visualizations/costs-and-
benefits-appraisal-tool-transit-buses) to increase 
user friendliness, and allows users to compare basic 
procurement and business model scenarios. 
CONTENTS
Executive Summary ....................................................... 1
1. Introduction ............................................................... 2
2. Tool Functionality and Layout .................................... 5
3. Data ........................................................................... 13
4. Calculations ............................................................... 22
5. Limitations and Future Development of the Tool ........ 24
Appendix 1. Explanations of Inputs ............................... 27
Appendix 2. Default Data ............................................... 31
Endnotes .......................................................................  36
References ..................................................................... 36
Acknowledgments .......................................................... 41

2  |  
1. INTRODUCTION
1.1 Background
As the need to mitigate air pollution and reduce 
carbon emissions from the urban transport sector has 
risen, more cities have begun to adopt low-carbon 
technologies such as electric buses (e-buses) in their 
public transit systems. The electric bus stock rose 
by about 17 percent from 2018 to 2019, and reached 
513,000 worldwide in 2019 (IEA 2020). In Western 
Europe alone, the number of registered e-buses tripled 
in 2019 (Sustainable Bus 2020). Many European cities 
have announced bans on using fossil-fueled vehicles 
in future years (Wappelhorst 2020). Cities in Latin 
America have accelerated the electrification process 
following advances in China, Europe, and the United 
States, with Santiago de Chile running the second-
largest electric bus fleet in the world after China ( TST 
2018), followed by Colombia. India also increased its 
transport electrification ambition through its Faster 
Adoption and Manufacturing of Hybrid and Electric 
Vehicles in India (FAME India) Scheme Phase II 
(DHI 2019). However, city bus operators, especially 
those from developing economies, need more cost and 
operational information about the new technologies 
in order to make more informed decisions during fleet 
electrification.
General tools exist that provide cost implications 
for electric vehicles and conventional internal 
combustion engine (ICE) vehicles, but they usually 
do not have good coverage of public transit, or of the 
social or environmental costs in the global South. For 
example, the Vehicle Cost Calculator developed by the 
Alternative Fuels Data Center at the U.S. Department 
of Energy (Hove and Sandalow 2019) and the EV 
Savings Calculator by the Pacific Gas and Electric 
Company (PG&E 2020) provide detailed information 
on vehicle costs, especially those for electric vehicles, 
but do not contain related information on public 
transit. The Volpe Center of the U.S. Department of 
Transportation has developed the Bus Lifecycle Cost 
Model to provide federal agencies with cost-related 
knowledge, providing information regarding direct 
procurement, operation, and maintenance costs 
(USDOT 2020), but does not focus on the social and 
environmental side. The AFLEET tool developed by 
Argonne National Laboratory so far contains the most 
detailed information for buses, including total cost of 
ownership calculations and environmental costs and 
benefits. However, it contains only U.S. data (ANL 
2020), which is useful but not ideal for other countries 
due to differences in technology, routes, operational 
conditions, and other local circumstances. 
World Resources Institute’s (WRI’s) earlier Costs and 
Emissions Appraisal Tool for Transit Buses provided 
suggestions on vehicle upgrade options for transit 
agencies and bus operators toward a clean energy 
transition (Cooper et al. 2019). However, during the 
tool’s development, electric buses remained a nascent 
technology and only a few data points were included. 
Also, even though emissions generated by the fleets 
could be quantified, social implications such as the 
social cost of emissions were not clear yet.
To increase the applicability and user-friendliness 
of the previous tool, this updated Costs and Benefits 
Appraisal Tool for Transit Buses (“the Tool”) is 
published as a webtool with several new features: 
More electric bus information with wider 
geographic coverage.  The energy consumption 
and operational efficiency of buses differ across 
vehicle models. To better capture the variation, 
different features, including fuel type, bus length, and 
emission standards, are included in the Tool. Given 
the heterogeneity of electricity mixes, fuel contents, 
and price levels across countries, the Tool also adds 
more country profiles for reference. Currently, the 
Tool covers information for China, where 99 percent 
of the world’s electric buses were located as of 2018; 
the European Union (EU), where the second-highest 
number of e-buses are registered (IEA 2019); and other 
emerging markets for electric buses such as the United 
States, Brazil, India, and Mexico. Electric buses in this 
tool refer mainly to battery electric buses. To a lesser 
degree, plug-in electric buses as well as the major ICE 
buses, such as diesel buses and compressed natural gas 
(CNG) and liquefied natural gas (LNG) buses, are also 
included in the Tool. Hydrogen fuel-cell buses are not 
included due to limited real-world applications and 
data availability.
Social cost and benefit calculations are 
included.  Electric buses can significantly reduce 
local air pollution and generate social, health, and 
environmental benefits for city residents. 1 The potential 
reduction of greenhouse gas (GHG) emissions can also 
help reduce future climate impacts. The new feature in

The Costs and Benefits Appraisal Tool for Transit Buses
TECHNICAL NOTE  |  October 2020  |  3
the Tool includes a monetization of emissions reduced, 
based on data from van Essen et al. (2019), EPA (n.d.), 
and Ricke et al. (2018), to reflect the potential social 
benefits that a cleaner fleet can bring to a city (see 
Section 3). In addition, the Tool assumes that not all 
of the external costs have been internalized by policy 
interference.
Simplified functions with user interaction 
options.  Many of the calculation functions in the Tool 
have been simplified, mainly to reduce the amount 
of data required and improve the user experience. 
Accuracy is not compromised to a great extent as the 
major cost components are accounted for. A few user 
interactions—technology comparisons, financing 
options, and charging infrastructure options—are 
included to reflect the real-life options that users may 
face during a fleet upgrade. 
The Tool aims to inform bus operators and transit 
agencies of the total cost of ownership, emissions 
reductions, and social benefits associated with bus fleet 
renewals and upgrades. This can help bus operators 
make the most cost-efficient decisions to reduce air 
pollution and emissions, and help transit agencies 
verify information provided by bus operators. The Tool 
can also help city decision-makers quantify the benefits 
of emissions reductions from a cleaner urban transit 
system, and develop reasonable incentives and policies 
to encourage their adoption.
1.2 Definition
The costs and benefits to bus operators of a clean bus 
technology upgrade can be categorized as direct and 
indirect. Costs in the Tool refer mainly to direct costs, 
which include bus procurement and scrappage costs 
(including capital and finance costs), labor costs of 
bus operation, fuel costs, maintenance costs, and other 
costs related to bus operation and maintenance but 
not included in the previous categories. Direct costs 
generally differ by bus technology. Indirect costs, 
including administrative costs, depot and land rental 
costs, and other compliance costs, normally do not vary 
much with different bus technologies (Ang-Olson and 
Mahendra 2011), and are thus set as optional in the 
Tool. However, due to the mandatory charging needs of 
electric buses, infrastructure-related costs need to be 
considered for electric buses, but not necessarily other 
technologies. Therefore, infrastructure-related costs 
are included as a stand-alone section in the Tool.
Benefits in this tool refer to direct benefits, which 
flow from the emissions reduction potential of cleaner 
bus technologies (e.g., electric buses, ICE buses with 
higher emissions standards) compared with that of 
other buses. Thus, benefits are presented as emissions 
reduced. Indirect benefits include potential reductions 
in operational and maintenance costs by changing 
technology and other savings due to changes in use 
patterns, which are considered cost savings when 
applicable. Thus, indirect benefits are not included in 
the benefit outputs of the Tool, but rather reflected in 
the cost section. 
Social costs avoided by emissions reductions are 
also treated as direct social benefits. Social costs 
represent the sum of the private (internal) and external 
costs (Korzhenevych et al. 2014; S. Song 2017). 
This technical note defines social cost as the cost of 
externalities. The social cost of traditional bus fleets 
can include local impacts such as air pollution, noise, 
congestion, and accidents (Ozbay et al. 2007), and 
global or regional impacts such as climate change and 
habitat damage (van Essen et al. 2019). Air pollution 
and climate impacts are the only two categories 
calculated in this technical note. Note that in the 
Tool, we calculate the social cost of air pollutants at 
the local level (tailpipe, or tank-to-wheel, emissions), 
and the social cost of carbon emissions at both the 
local (tailpipe) and global (upstream, or well-to-
wheel, emissions) levels. The reason is that the major 
impact from air pollutants—the impact on local public 
health—is on the tailpipe side (tank-to-wheel), while 
local carbon emissions have a global impact, making 
it meaningful to use the well-to-wheel approach. The 
general components of costs and benefits are indicated 
in the structure of the Tool (Figure 1).

4  |  
Figure 1  |  General Components and Layout of the Tool
Notes:  Variables in red require users’ selection or manual input. The Tool provides default values for other variables based on users’ selections of country, bus size, and fuel type. Beyond basic 
analysis, “Advanced Features” (in grey) indicate the costs and emissions variations by operational condition and maturity of technology. Abbreviations: CO: carbon monoxide; THC: total 
hydrocarbons; NOx: nitrogen oxides; PM2.5/PM10: particulate matter of 2.5 and 10 micrometers or less in diameter, respectively; CO2: carbon dioxide; GHGs: greenhouse gases.
Source: Authors.
INPUTS
OUTPUTS
General 
Information
• Country
•  Discount rate
•  Social 
discount rate
• City
Infrastructure
•  Number of 
chargers
•  Charger 
construction 
costs
•  Procurement 
cost
•  Operation 
costs
•  Maintenance 
costs
Social Cost 
Factors
•  CO
•  THC
•  NOx
•  PM2.5/
PM10
•  CO2
Emission 
Factors
Tailpipe
•  CO
•  THC
•  NOx
•  PM2.5/PM10
•  CO2
•  GHGs
Upstream
•  CO2
•  GHGs 
Advanced 
Features
Operational 
factors
•  Average 
speed
•  Air 
conditioning
•  Load
Advanced 
Features
•  Replacement 
ratio
Bus Fleet 
Information
•  Number of 
buses
•  Bus size
•  Fuel type
•  Emission 
standard
•  Annual distance 
traveled
•  Operational 
years
•  Average speed
•  Load 
•  Fuel efficiency
Economic Costs
Procurement
•  Procurement subsidy
•  Down payment
•  Purchase price
•  Residual value
•  Loan interest
•  Loan time
Operation (annual)
•  Total labor
•  Fuel price
•  Fuel cost projection
•  Additional fuel price
•  Additional operational costs
•  Insurance 
Maintenance (annual)
•  General maintenance costs
•  Maintenance labor 
•  Additional maintenance costs
•  Overhaul 
Additional
•  Administration
•  Other taxes and fees
Capital and Financing Costs Operational Costs Total Emissions
Total Cost of Ownership Social Costs
Detailed Numeric Output
(annualized, by fleet and fuel type)
Graphic Summary
(annualized, by fleet and fuel type)

The Costs and Benefits Appraisal Tool for Transit Buses
TECHNICAL NOTE  |  October 2020  |  5
Source: “Costs and Benefits Appraisal Tool for Transit Buses.” Webtool. Washington, DC: World Resources Institute.
2. TOOL FUNCTIONALITY AND LAYOUT
2.1 How to Use the Tool
In general, users can explore the Tool in two ways: 
 ▪ Users select or fill in basic variables → Default data 
are pulled from the database → Users choose different 
user interaction options → Results are calculated and 
compared based on default data
 ▪ Users select or fill in basic variables → Default data are 
pulled from the database → Users update variables with 
their own data to reflect certain conditions → Users 
choose different user interaction options, using default 
data or their own data → Results are calculated and 
compared based on user input
The basic variables that require user input include the 
following: 
 ▪ Country: Drop-down menu with limited options
 ▪ City: Drop-down menu with limited options; users can 
select one of the available cities and use city data from 
the default database or fill in their own data, or select 
“general” and use country averages from the default 
database or fill in their own data
 ▪ Bus size: Drop-down menu with limited options; users 
can select the “general” category to input a bus size 
not listed
 ▪ Fuel type: Drop-down menu with limited options 
based on default data available, such as diesel and 
electric
 ▪ Emission standard: Drop-down menu with limited 
options based on default data available
 ▪ Number of buses: Requires manual input
Additional variables require user input but are optional 
to generate results:
 ▪ Procurement subsidy
 ▪ Down payment
 ▪ Number of chargers
The following variables are mandatory for calculations, 
but because default data are available for them, users 
are not required to fill in their own information. 
However, we encourage users to customize the data.
 ▪ Operational years
 ▪ Annual distance traveled
 ▪ Fuel efficiency
For the rest of the mandatory variables in the “General 
Information” and “Cost Factors” categories, the 
Tool provides default data that users may use for 
convenience, but we encourage users to customize the 
inputs to fit their situations. 
Variables in the “Emission Factors” and “Social Cost 
Factors” categories are automatically filled in based on 
basic variables selected by users, though these can also 
be manually edited. We recommend that users use the 
default data unless local data are available.
2.2 Input Pages
Inputs  of the Tool include the following:
 ▪ General information  (see Figure 2): The 
countries and cities included in the Tool are 
limited based on the availability of default 
Figure 2  |  Input Page for General Country and City Information

6  |  
Notes: Abbreviations: L/100 km: liters per 100 kilometers; VKT: vehicle kilometers traveled. 
Source: “Costs and Benefits Appraisal Tool for Transit Buses.” Webtool. Washington, DC: World Resources Institute.
Source: “Costs and Benefits Appraisal Tool for Transit Buses.” Webtool. Washington, DC: World Resources Institute.
Figure 3  |  Input Page for Bus Fleet Information
Figure 4  |  Input Page for Cost-Related Factors

The Costs and Benefits Appraisal Tool for Transit Buses
TECHNICAL NOTE  |  October 2020  |  7
data. Users can refer to regions with similar 
characteristics if their country or city of interest 
is not included. Under the drop-down menu for 
“City,” there is an option of “General” that, when 
selected, populates the remaining fields with the 
averages of the data collected for the selected 
country. Users may also enter their own data 
when selecting “General.” Discount rate refers to 
nominal discount rate, which considers inflation 
factors. Social discount rate is the discount rate 
used for social projects and is used in the Tool for 
social cost and benefit calculations.
 ▪ Bus fleet information  (see Figure 3): The fuel 
efficiency factor can be identified based on users’ 
selections of basic variables, such as bus length, fuel 
type, and emission standard. Default fuel efficiency 
data based on these variables are included in the Tool 
when available. When such data are not available, 
the average fuel efficiency factors given by the Tool’s 
underlying sources are used. 
 ▪ Costs are categorized as procurement, operation, 
and maintenance costs (Figure 4). Although the 
Tool focuses mainly on the bus itself, charging 
infrastructure also generates costs in these 
categories. These may not be included in bus-related 
costs, so they are addressed in a separate category.
 ▪ Emission factors include tailpipe emissions (tank-
to-wheel) and upstream emissions (well-to-tank). 
The default data are collected by bus length, fuel type, 
and emission standard, when such data are available 
for tailpipe emissions. Upstream emission factors 
(EFs) are collected for different fuels, including 
the emission factors for fossil fuel production 
processes, and grid emission factors, which account 
for emissions generated by electricity used when 
operating electric buses. Unlike a conventional 
well-to-wheel analysis, this tool considers upstream 
emissions only for greenhouse gases, and does not 
include upstream emissions for other air pollutants 
due to different social benefits implications (refer 
to Section 3.2.3 for more information). Geographic 
differences are considered by incorporating 
information from different cities and countries. The 
pollutants considered include carbon monoxide (CO), 
total hydrocarbons (THC), nitrogen oxides (NOx), 
particulate matter (PM2.5 and PM102), and carbon 
dioxide (CO2) or carbon dioxide equivalent (CO2e),3 
whichever is available or recorded in the sources. 
Figure 5 shows the specific EFs and their units.
Notes:  Abbreviations: g/km: grams per kilometer; PM2.5/PM10: particulate matter of 2.5 and 10 micrometers or less in diameter, respectively; g/L: grams per liter; CO2e: carbon dioxide 
equivalent; g/kWh: grams per kilowatt-hour.
Source: “Costs and Benefits Appraisal Tool for Transit Buses.” Webtool. Washington, DC: World Resources Institute.
Figure 5  |  Input Page for Emission Factors

8  |  
 ▪ Social cost factors  are collected for each type 
of air pollutant (Figure 6). They measure the 
total social cost per unit mass of each pollutant 
(in US$/tonne) at the national level. Localized 
social cost factors as default values are included 
in the Tool. The localization procedure requires 
national-level income data, such as purchasing 
power parity (PPP)–adjusted gross domestic 
product (GDP) per capita.
 ▪ Advanced features  reflect variables that impact 
fuel efficiency, emission factors (e.g., speed, 
load), or a bus’s total cost of ownership (e.g., 
replacement ratio). Correction factors for these 
variables are not included in this tool due to 
limited data and research available to generate a 
robust number for different countries. Therefore, 
the variables are included as advanced features 
for reference only for users who are interested 
in exploring how they can impact fuel efficiency, 
emissions, and costs. Users may choose different 
combinations of operational factors. When default 
data are available for these variables for a certain 
city, related fuel efficiency and emission factors 
are used. When such data are not available, users 
cannot get condition-specific data. Some reference 
numbers are included as notes for each variable, 
which users can refer to for more information. 
Users are encouraged to explore different numbers 
reflecting different operational conditions. The 
Notes: Abbreviations: PM2.5/PM10: particulate matter of 2.5 and 10 micrometers or less in diameter, respectively. 
Source: “Costs and Benefits Appraisal Tool for Transit Buses.” Webtool. Washington, DC: World Resources Institute.
Figure 6  |  Input Page for Social Cost Factors
intention behind the advanced features is to give 
users an idea of other factors that impact fuel 
efficiency and emission factors.
    The replacement ratio refers to the number of 
electric buses—or buses with more advanced 
technology—it takes to achieve the same level of 
service as one traditional ICE bus. Ideally, the 
ratio is 1:1, which means one electric bus can 
fully replace one ICE bus. However, in reality, 
especially when the technology is still in its 
nascent stage or still has operational issues, the 
ratio can be 1.5–2:1 (Jin 2020). Therefore, we 
recommend users use 1:1 and 2:1 in different 
scenarios.
    Operational factors—speed, load factor, and air 
conditioning—are discussed in more detail in 
Section 3.3. The Tool provides some reference 
values, representing the general impact these 
factors have on fuel efficiency and emission factors. 
However, as the numbers are extracted from 
academic papers, they serve only as a reference, 
and do not necessarily reflect the operational 
conditions in the city of interest.
2.3 User Interactions
Three user interaction options are also included in the 
Tool, covering the issues most often faced by bus operators 
when procuring clean technology buses:

The Costs and Benefits Appraisal Tool for Transit Buses
TECHNICAL NOTE  |  October 2020  |  9
Source: “Costs and Benefits Appraisal Tool for Transit Buses.” Webtool. Washington, DC: World Resources Institute.
Figure 7  |  Compare Fleets
 ▪ Add Fleet: Bus upgrade options, which compare the 
costs and emissions implications of a fleet upgrade 
(similar to the previous tool).
 ▪ Add Cost Factor : Financing and subsidy options, 
which allow for a direct subsidy per bus, and other 
subsidy options given through better financing 
conditions, which users can simulate by inputting 
different combinations of factors such as interest 
rate, loan year, and down payment. Battery leasing 
is one way to reduce the cost of an electric bus; while 
this financing option is not explicitly mentioned 
in the Tool, users can fill in the related cost in 
the “Additional Operational Costs” box if such a 
financing option is used or desired.
 ▪ Add Infrastructure : Charging infrastructure costs 
are included to reflect the potential business models 
of charging infrastructure. 
After users create a first, baseline-scenario fleet, they can 
create additional fleets by changing the inputs, and then 
compare the cost and emission implications of different 
bus upgrade, financing, and infrastructure business models 
(Figure 7).
2.3.1 Bus Upgrade Options
As illustrated in Figure 8, users can change the basic 
features related to a fleet upgrade and compare 
the cost and emission implications when switching 
Notes: Abbreviations: VKT: vehicle kilometers traveled; km: kilometers; m: meters.
Source: “Costs and Benefits Appraisal Tool for Transit Buses.” Webtool. Washington, DC: World Resources Institute.
Figure 8  |  Input Page for Bus Features

10  |  
bus technologies. By changing these features, 
procurement cost, fuel efficiency, and emission 
factor will change accordingly when default data 
are available. If default data are not available or 
not applicable to the user’s situation, the user is 
encouraged to input their own data. 
Other variables such as number of buses, vehicle 
kilometers traveled (VKT), and operational years 
(lifespan) determine the quality of service of the bus 
fleet. These numbers change according to the choice 
of technology. For example, electric buses may have 
a shorter VKT due to battery range and, therefore, 
more buses and higher operational frequency may be 
necessary to keep the same level of bus service. Users 
must input the number of buses needed, VKT, and 
operational years; the Tool does not automatically 
calculate them. 
2.3.2 Financing and Subsidy Options
Bus procurement business models vary widely across 
regions (Moon-Miklaucic et al. 2019). Some involve 
public funding via financial subsidies, whereas others 
involve different financing options. This tool offers a 
simplified way to reflect the core differences between 
business models and financing options: down payment, 
procurement subsidy, interest rate, loan time, residual 
value during bus scrappage, and potential other 
operational costs due to different financing mechanisms 
(such as battery leasing cost, which can be considered 
in “Additional operational costs to include”) (see Figure 
9). Most innovative ways to finance buses result from 
adjusting these variables. While this tool does not 
provide users with the detailed design of a potentially 
relevant business model, users can still change these 
numbers and compare the cost differences of various 
financing options.
 
2.3.3 Charging Infrastructure Needed/Costs
The costs related to charging infrastructure are 
complicated (Nelder and Rogers 2019), and the cost 
implications for bus operators differ by business model. 
For example, operators may have the opportunity to 
construct and manage their own chargers, purchase 
charging services from charger operators, or get a 
preferential electricity price based on certain incentive 
policies. To simplify the calculations, the Tool includes 
only some basic components related to chargers (see 
Figure 10). 
In Figure 10, procurement costs refer to the unit 
charger costs, if chargers need to be purchased. 
Construction costs for charging infrastructure in this 
tool may include labor, materials, utility upgrades, and 
other costs incurred during the installation process, 
and should be considered early in the planning process 
of upgrading to an electric bus fleet (Nelder and 
Rogers 2019). Operational and maintenance costs are 
Source: “Costs and Benefits Appraisal Tool for Transit Buses.” Webtool. Washington, DC: World Resources Institute.
Figure 9  |  Input Page for Bus Financing Factors

The Costs and Benefits Appraisal Tool for Transit Buses
TECHNICAL NOTE  |  October 2020  |  11
Source: “Costs and Benefits Appraisal Tool for Transit Buses.” Webtool. Washington, DC: World Resources Institute.
Figure 10  |  Input Page for Charging Infrastructure 
annual costs incurred by bus operators. Users can 
adjust the related costs to reflect specific business 
models. For example, if the bus operator owns the 
charging infrastructure, users can put all direct costs 
into this infrastructure section; if charging services are 
purchased under contract, users can use operational 
and maintenance costs in this section to roughly reflect 
that; if electricity prices or charging service fees are 
changed under this business model, users can adjust 
“fuel price” and “additional fuel price” in the cost 
section.
As is discussed in Section 6, this tool does not intend 
to tell users how many chargers to construct or where 
to install them. Such information can be explored 
using WRI’s other tools, 4 such as the Future Mobility 
Calculator, which takes a city-level macro approach, and 
a tool that analyzes the impact of charging behaviors on 
the distribution grid. In this tool, users need to create 
their own scenarios to conduct an analysis.
2.4 Outputs and Sample Graphics
Outputs of the Tool can be downloaded into Microsoft 
Excel and tailored to fit the comparison needs of the user. 
Some direct output comparisons are also available in 
sample graphics (Figure 11) after users input information 
for multiple bus fleets and compare results. It is worth 
noting that the Tool provides only a few general graphics. 
Users are encouraged to generate their own graphics.
Some of the Tool’s outputs include the following:
 ▪ The present value (PV) of the total cost of 
ownership of a bus fleet in its operational lifespan, 
annualized cost and unit cost (single bus per 
kilometer, or km). 
 ▪ The total emissions of different air pollutants and 
greenhouse gases in a fleet’s operational lifespan, 
annualized, by unit (single bus per km). 
 ▪ The PV of lifetime social costs or avoided social 
costs (social benefits).

12  |  
Figure 11  |  Sample Output Graphics
Notes:  Abbreviations: Labor cost pv: the present value of labor costs; Fuel cost pv: the present value of fuel costs; Others operational cost pv: the present value of operational costs other than for 
labor and fuel; Maintenance cost pv: the present value of maintenance costs; Overhaul cost pv: the present value of the cost to overhaul a fleet of buses;  Capital cost pv: the present value 
of capital costs; Financial cost pv: the present value of financial costs; Infrastructure cost pv: the present value of infrastructure costs; CO: carbon monoxide (tailpipe emissions); THC: 
total hydrocarbons (tailpipe emissions); NOx: nitrogen oxides (tailpipe emissions); PM2.5: particulate matter of 2.5 micrometers or less in diameter (tailpipe emissions); PM10: particulate 
matter of 10 micrometers or less in diameter (tailpipe emissions); CO2: carbon dioxide (tailpipe emissions); CO2e: carbon dioxide equivalent (tailpipe emissions); CO2 upstream: carbon 
dioxide (upstream emissions);  CO2e upstream: carbon dioxide equivalent (upstream emissions).
Source: “Costs and Benefits Appraisal Tool for Transit Buses.” Webtool. Washington, DC: World Resources Institute.
Emissions Output
CO PM2.5THC PM10NOx
Fleet 1
0
1
2
3
4
5
Total emissions (tonne)
Fleet 1
CO2 CO2e upstreamCO2e CO2 upstream
0
100
200
300
400
Total emissions (tonne)
Social Cost Output
CO CO2PM2.5THC PM10NOx
0
10,000
20,000
30,000
40,000
Social cost (UD$/tonne)
Total cost (US$) 
Fleet 1
Cost Output
Fleet 1
Fuel cost pv Others operational cost pv
Maintenance cost pv Capital cost pv
Labor cost pv
Financial cost pv Infrastructure cost pv
Overhaul cost pv
0
8,000,000
6,000,000
4,000,000
2,000,000

The Costs and Benefits Appraisal Tool for Transit Buses
TECHNICAL NOTE  |  October 2020  |  13
Table 1  |  Summary of Data Categories, Availability, and Geographic Distribution
Notes:  Abbreviations: E-bus: electric bus; ICE: internal combustion engine; EF: emission factor.
Source: Authors. 
3. DATA
3.1 Data Overview
Default data related to costs and emissions calculations 
were collected mainly by literature review. The 
authors explored, using keywords, local transport 
agency websites (e.g., that of the U.S. Department 
of Transportation), databases of academic journals, 
and publication archives of transport-related or 
environment-related research institutions (e.g., 
International Council on Clean Transportation). A 
more detailed description of this compiled dataset 
can be found in the next section. We also conducted 
a few interviews with transit agencies to gain a better 
understanding of cost structure, which helps to justify 
the calculation methodology. The geographic coverage 
of the dataset of this tool includes China, India, some 
Latin American countries (Brazil, Colombia, and Chile), 
the United States, the United Kingdom, some members 
of the EU (Austria, France, Germany, Norway, Sweden), 
and Switzerland (Table 1). In general, data identified 
through this literature review mostly came from the 
United States, followed by China and the EU. 5 In terms 
of fuel types, diesel buses, hybrid-electric buses, and 
battery electric buses have a heavier focus in this tool, 
compared with buses powered by natural gas (LNG or 
CNG), liquified petroleum gas (LPG), and biodiesel. 
Hydrogen fuel cell buses are not included in this tool.
Fuel Efficiency
ICE Bus EF Grid EF Financial 
Cost Social Cost
E-bus ICE bus
United 
States GA GA GA GA   
European 
Union  GA GA GA   
Switzerland  
United 
Kingdom  GA GA GA   
China   GA GA   
India    GA   
Chile       
Colombia       
Brazil    GA   
Mexico       
GA
Datasets by 
government 
agencies
 Over 10 
sources 
  5-10 
sources 
  Fewer than 
5 sources

14  |  
3.2 General Costs
3.2.1 General Costs 
 ▪ Procurement costs 
Financial information about existing projects was 
gleaned mainly from bidding documents in the case 
of China, and journal articles for other regions. The 
purchase price of individual buses varies greatly 
depending on the specifications—such as engine type, 
chassis make and model, emission control technology, 
manufacturer, whether production and materials are 
domestic or imported, time and location of purchase, 
and the procurement model—which makes it hard to 
give a precise price for each bus technology. Further 
analyses are encouraged to assess how these factors 
impact the actual purchase cost. In this version of the 
Tool, however, default costs are empirical estimates 
that reflect the average values of models used in bus 
fleets around the world. 
Figure 12 shows the majority of bus procurement 
information in the Tool’s dataset in different regions. 
Users are encouraged to use the default data as a 
reference, and update costs to fit their situations 
when needed. In this dataset, bus prices in developing 
countries are generally lower than those in developed 
countries, especially for electric buses, which can cost 
three to four times more in the EU and the United States 
than in China and Latin American countries. However, 
it is worth noting that due to data availability, the figure 
does not aim to provide a comprehensive picture of the 
world’s bus market. Other cases and trends may exist 
but were not captured by the authors by the time the 
Tool was released. As indicated above, several factors 
may impact the actual procurement cost, which may not 
be captured in the graphic. The tool does not analyze 
how these factors have impacted the procurement cost, 
but rather provides a general picture using empirical 
data. Users should use the multi-country information 
only as a reference.
Figure 12  |  Purchase Prices of Diesel and Electric Buses 
Notes:  The lower and upper hinges correspond to the 25th and 75th percentiles. The upper whisker extends from the hinge to the largest value no further than 1.5 * IQR from the hinge (where 
IQR is the inter-quartile range). The lower whisker extends from the hinge to the smallest value, at most 1.5 * IQR of the hinge. Data beyond the end of the whiskers are “outliers” and are 
plotted individually.  
Sources:  Eudy et al. 2014; Eudy and Jeffers 2018; Goswami and Chandra Tripathi 2019; ZEBRA 2019; Dallmann 2019; Potkány et al. 2018; BNEF 2018; USDOT 2016; ChinaBuses 2020; MFC 
2020; Lajunen and Lipman 2016; ANL 2020.

The Costs and Benefits Appraisal Tool for Transit Buses
TECHNICAL NOTE  |  October 2020  |  15
 ▪ Subsidy and financing options
Due to the higher procurement costs of electric buses (Figure 
12), public entities and financing institutions around the 
world use various incentives to encourage their use (Moon-
Miklaucic et al. 2019). Two common options are included 
in this tool: procurement subsidies, which can reduce the 
upfront costs immediately, and normally depend on the 
operational range and battery size of the vehicles; and loans, 
which are a common financing option for bus operators. 
Different interest rates can reflect innovative financing 
options and specific costs vary widely. A comprehensive 
dataset may be informative but cannot help cities when 
making context-specific electric bus procurement decisions. 
Therefore, this tool includes only some default information 
to provide users with a general idea of the potential options; 
we encourage users to explore their own scenarios.
 ▪ Operation and maintenance costs
The operation and maintenance (O&M) costs for buses 
vary greatly by location, operational pattern, and business 
model. For example, labor costs, and how labor costs are 
accounted for, are different across cities. Fuel costs depend 
on local fuel prices, charging times (if electric), fuel efficien-
cy, and operational mileage. Maintenance can be contracted 
out as a service package or be kept in-house with specialists. 
Also, the cost of battery replacement, or engine overhaul, 
depends largely on the operator’s contract with the manu-
facturer, and the operator’s decision of whether to replace 
the whole vehicle at once or just key parts. 
Given such cost variations, the Tool captures only 
the key calculations for O&M but does not include an 
extensive set of related data. Some default values are 
included, but only as a reference. Users are encouraged 
to fill in the information that best represents their 
situation to get the most applicable results. 
3.2.2 Fuel Efficiency
We collected fuel efficiency and emission factors mostly 
from studies conducting field or road tests, except for data 
from European countries, which came mainly from lab test 
results. During road tests, buses are usually operated under 
controlled conditions, such as at a certain operational speed 
with a certain passenger load and following a fixed route 
reflecting local traffic conditions. In this dataset, we classify 
speed into seven categories, in increments of five kilometers 
per hour (km/h): (0–5 km/h, 5–10 km/h … 25–30 
km/h, and over 30 km/h). Three levels of load factors are 
applied—low (<40 percent), medium (40–60 percent), and 
high (>60 percent)—which indicate the ratio of actual load 
to the maximum passenger load.
As illustrated in Table 2, the United States has the 
largest number of fuel efficiency records for all types of 
buses in the Tool. Data are relatively limited for other 
Table 2a  |  Number of Records of Fuel Efficiency Data by Fuel and Country
Country Diesel Electric Hybrid Gasoline NG LPG Total
Brazil 33 0 25 0 0 0 58
Chile 2 0 1 0 0 0 3
Colombia 1 0 2 0 0 0 3
Mexico 30 0 0 0 0 0 30
China 49 65 15 0 8 0 137
India 8 2 1 0 2 0 13
European Union 16 14 0 0 16 0 46
Switzerland 3 2 0 0 3 0 8
United Kingdom 15 0 0 0 0 0 15
United States 558 58 19 539 22 32 1,228
Total 715 141 63 539 51 32 1,541

16  |  
locations in the default dataset. This does not necessarily 
mean that data are less available in these regions, or that 
the results are less accurate for these regions. The Tool 
is not intended to include a comprehensive dataset. The 
data collection process and the size of the dataset were 
affected by time and resources available.  
The default fuel efficiency of buses by fuel and by 
country (see Table 3) is calculated as a sample average. 
When local data are not available, users can refer to 
geographic regions with similar characteristics.
There are some discrepancies in the Tool’s default 
dataset worth mentioning. First is the discrepancy 
between lab test results and real-world operational 
fuel efficiency, the latter of which is usually higher due 
to diverse operational conditions (Tietge et al. 2017). 
Variances are large and depend on various impacting 
factors (see Sections 3.3.1 and 5.1 for more information). 
In addition, different driving cycles applied during the 
tests represent different operational conditions, which 
Table 2b  |  Number of Records of Fuel Efficiency Data by Fuel and Bus Length
Bus length Diesel Electric Hybrid Gasoline NG LPG
6 m 0 0 2 0 0 0
8 m 6 13 0 0 0 0
9 m 0 3 0 0 0 0
10 m 3 25 0 0 1 0
12 m 688 94 53 539 50 32
14 m 0 3 0 0 0 0
15 m 3 0 0 0 0 0
18 m 4 3 8 0 0 0
23 m 2 0 0 0 0 0
25 m 7 0 0 0 0 0
27 m 2 0 0 0 0 0
Total 715 141 63 539 51 32
Notes:  Abbreviations: NG: natural gas; LPG: liquified petroleum gas; m: meters. 
Sources:  Roychowdhury 2010; APTA 2018; Borén 2019; Chen et al. 2017; Guo et al. 2015; Boulter et al. 2009; Giraldo and Huertas 2019; Gota et al. 2014; He et al. 2018; MJB&A 2013; Barnitt 
and Chandler 2006; Barnitt et al. 2008; GGGI and CSTEP 2016; Lammert 2008; S. Zhang et al. 2014b; Göhlich et al. 2014; Dreier et al. 2018; Barnitt 2008; Huo et al. 2012; ISSRC 2013; 
X. Wu et al. 2013; Q. Song et al. 2018; HBEFA 2019; EEA 2019b; Zhou et al. 2016; Prohaska et al. 2016; AC Transit 2018; Dallmann 2019; Goswami and Chandra Tripathi 2019. 
may lead to discrepant test results. For example, in 
Table 3, the fuel efficiency for diesel buses listed for 
India is quite high because the average speed from 
Indian data sources was 40–67 kilometers per hour 
(km/h) (Gota et al. 2014), while the average speed in 
many other places was less than 30 km/h. Therefore, 
the Tool does not try to compare countries but rather 
provides country-specific data for reference. 
Also, although emission standards are not directly 
correlated with fuel efficiency, as it is a standard 
used to control emissions, in reality it may affect fuel 
efficiency. To be compliant with the standard, emissions 
reduction technologies may be applied to the bus, which 
increase the weight or impact the combustion process 
of the vehicle. Therefore, buses with different emission 
standards may have different fuel efficiencies. In the 
Tool, default data were collected by emission standard 
when available. But the Tool does not provide an 
analysis on how emissions reduction technology affects 
the actual operational efficiency of buses.

The Costs and Benefits Appraisal Tool for Transit Buses
TECHNICAL NOTE  |  October 2020  |  17
Table 3  |  Fuel Consumption Data by Country and Fuel for 12-Meter Buses (mean and range)
Region Diesel 
(L/100km)
Electric 
(kWh/100km)
Hybrid 
(L/100km)
Gasoline 
(L/100km)
NG 
(MJ/100km)
LPG 
(MJ/100km)
Brazil
46.7 17.6
(33.5-55.0) (4.9-58.8)
Chile
37.5 25.2
(36.0-38.9) (25.2-25.2)
Colombia
37.7 31.8
(37.7-37.7) (29.9-33.6)
Mexico
34.4
(21.4-57.2)
China
45 150.3 37.7 1,433.9
(27.9-88.4) (90.7-260.6) (22.9-81.9) (1,333.3-1,610.0)
India
26.6 158.3 30.7 2,079
(17.9-50.0) (150.0-166.7) (30.7-30.7) (1,848.0-2,310.0)
European Union
37.3 173.1 1,827.7
(30.9-46.8) (118.0-360.0) (1,471.9-2,664)
Switzerland
44.5 188.7 2,039.1
(43.4-45.7) (188.2-189.3) (1,978.4-2,099.1)
United Kingdom
45.4
(22.9-101.1)
United States
46.1 154.1 46.7 32.1 2,171.8 1,812.8
(11.3-101) (15.9-311.1) (29.3-75) (10.2-95.6) (1,142.9-4,955) (105.3-2,897.5)
Notes:  Abbreviations: NG: natural gas; LPG: liquified petroleum gas; L/100 km: liters per 100 kilometers; kWh/100 km: kilowatt-hours per 100 kilometers; MJ/100 km: Megajoules per 100 
kilometers.
Sources:  Chen et al. 2017; Roychowdhury 2010; Guo et al. 2015; Boulter et al. 2009; Giraldo and Huertas 2019; Gota et al. 2014; He et al. 2018; MJB&A 2013; Barnitt and Chandler 2006; Dreier 
et al. 2018; X. Wu et al. 2013; Q. Song et al. 2018; EEA 2019b; Zhou et al. 2016; Borén 2019; APTA 2018; Dallmann 2019; Goswami and Chandra Tripathi 2019; Barnitt et al. 2008; 
GGGI and CSTEP 2016; Lammert 2008; Göhlich et al. 2014; Barnitt 2008; Huo et al. 2012; ISSRC 2013; HBEFA 2019; Prohaska et al. 2016; AC Transit 2018; S. Zhang et al. 2014b.
3.2.3 Emission Factors 
In this tool, a tank-to-wheel (TTW) approach is used to 
calculate local air pollutants and a well-to-wheel (WTW) 
approach (including well-to-tank and tank-to-wheel 
components) is used to calculate carbon emissions. We 
used two approaches because the major impact from 
air pollutants—that on local public health—occurs on 
the tailpipe side (TTW approach), while local carbon 
emissions have a global impact (WTW approach). For 
the same reason, at the social cost appraisal stage, only 
local impacts from air pollutants are monetized, while 
the global impacts of carbon emissions are monetized.
 ▪ Tailpipe emissions
As was the case for fuel efficiency, emission factors 
were collected mainly from studies conducting field or

18  |  
road tests. Results of lab tests that simulated real-world 
driving cycles in different cities were used when field 
test data were not available. It was assumed that battery 
electric buses have zero tailpipe emissions since they 
use only electricity. A sample sheet of EF data for China 
(Table 4) shows the wide variation in emission factors 
by fuel type and emission standard, and even for buses 
using the same standard.
It should be noted that the Tool uses only European 
emission standards due to data availability and to 
reduce the complexity of the Tool. China has been 
implementing European standards for heavy-duty 
vehicles since 2000. Although the China VI standard 
is more stringent than Euro VI, at the time of this 
tool’s development, operational data for China VI were 
limited. Therefore, using European emission standards 
to represent China’s standards is feasible. For US cases, 
since it has been over 10 years since the Environmental 
Protection Agency last released an exhaust emission 
standard for urban buses (2007), the Tool does not 
distinguish between standards for US cases, but shows 
an average of values found in the data sources. The Tool 
also uses averages rather than specific standards for 
India and South American countries, due to limited data 
and sources being unclear about emission standards. 6 
 ▪ Upstream emission factors
Upstream emissions for buses of different technologies 
were calculated based on emission factors of fuel. 
Emission factors of electricity depend largely on the 
local grid mix. Countries like China and India rely 
heavily on coal, which contributes to higher carbon 
intensities, while Brazil has abundant hydropower and 
Table 4  |  Air Pollutant Emission Factors in China by Emission Standard (mean and range)
Pollutant 
(g/km)
Diesel Hybrid
Pre Euro Euro I Euro II Euro III Euro IV Euro V Euro III Euro IV Euro V
THC
25.9 24.2 21.2 16.4 7.5 3.8 1.0 3.2
(9.2-64) (8.6-60) (7.6-52.8) (0.8-41) (2.1-17.8) (1.4-8.9) (0.8-1.2) (3.0-3.5)
HC
4.9 1.1 0.6 0.5 0.2 0.1 0.2 0.1
(2.7-8.2) (0.6-1.8) (0.4-1.8) (0.2-1.3) (0.1-0.7) (0.1-0.3) (0.2-0.2) (0-0.2)
NOx
16.8 15.1 13.3 13.3 13.8 12.1 10.3 5.7
(9.7-30.6) (8.7-27.5) (7.7-24.3) (4-24.3) (2-27) (6.7-22.6) (7.6-13) (2.2-12.3)
PM2.5
1.7 1.3 1.2 0.5 0.4 0.2 0.2
(0.9-3.4) (0.7-2.6) (0.5-2.3) (0.3-1.0) (0.1-0.7) (0.1-0.4) (0.1-0.3)
CO2
807.6 844.2 1,161.9 787.3 754.4 646.0
(807.6-
807.6)
(844.2-
844.2)
(737.3-
2,150.8)
(787.3-
787.3)
(389.1-
1,440.5) (646-646)
Notes:  Pre Euro was the emission standard implemented before Euro I. In China, the Euro I standard was implemented for heavy-duty vehicles in 2000 (Y. Wu et al. 2012). EEV stands for 
“enhanced environmentally friendly vehicles,” which is somewhere between Euro 5 and Euro 6. Abbreviations: NG: natural gas; g/km: grams per kilometer; CO: carbon monoxide; NOx: 
nitrogen oxides; PM2.5: particulate matter of 2.5 micrometers or less in diameter; CO2: carbon dioxide; THC: total hydrocarbons.
Sources: He et al. 2018; S. Zhang et al. 2014; X. Wu et al. 2015; Yue et al. 2016; MEE 2014; Hu et al. 2009; Chen et al. 2017; Q. Song et al. 2018; Y. Wu et al. 2012; Yang et al. 2016.

The Costs and Benefits Appraisal Tool for Transit Buses
TECHNICAL NOTE  |  October 2020  |  19
the local grid emission factor is relatively low. Country-
specific grid emission factors are shown in Table 5.
Grid emission factors also vary by electricity market 
and time of use, even within the same country (Holland 
et al. 2016). For example, in markets run by different 
independent system operators (ISOs) in the United 
States, the electricity mixes and emission factors vary. 
Also, when the generation capacity of renewables is 
higher (e.g., solar generation is high on sunny days), 
the electricity is cleaner than when the grid draws more 
on fossil fuel generation. Users are encouraged to use 
the most applicable emission factors from their target 
regions. However, as such detailed and local specific 
data are available only for a few places, and hard to 
Table 5  |  Carbon Dioxide Emission Factors by Country and Fuel
Country Diesel (g/L) Electricity (g/kWh) NG (g/MJ)
China 490.60 610.21
India 731.20
Mexico 449.00
Brazil 428.18 110.21
Austria 108.98
France 48.48
Germany 402.14
Norway 11.18
Sweden 12.60
Switzerland 11.82
European Union 326.90
United Kingdom 244.71
United States 567.92 427.03 10.32
Notes:  Abbreviations: NG: natural gas; g/L: grams per liter; g/kWh: grams per kilowatt-hour; g/MJ: grams per Megajoule.
Sources:  Dreier et al. 2018b; He et al. 2018; Zhou et al. 2016a; MJB&A 2013; Tao et al. 2016; Climate Transparency 2019; IMP 2017; EEA 2017; Rangaraju et al. 2015; 
Li and Yang 2020; EPA 2020. 
collect in detail from all regions and countries, the 
default inputs of this tool are country averages. 
3.2.4 Social Cost Factors 
Social cost factors (SCFs), expressed in US$ per 
tonne of each pollutant, are the least available data 
type. Most countries do not have localized SCF data 
at either the national or city level. Results of existing 
studies still have high uncertainty. In this tool, we 
primarily used data on the social cost of carbon (SCC) 
from Ricke et al. (2018) as well as transport-specific 
SCFs of other air pollutants from Europe (van Essen 
et al. 2019), which covers all major impacts including 
health effects, crop loss, biodiversity loss, and material

20  |  
damage. Then we localized the SCFs to other countries 
by using the income data of GDP (PPP) per capita 
from each country; we assumed income elasticity, e, 
to be 1.2 for low- and middle-income countries and 
0.8 for high-income countries (World Bank and IHME 
2016). See Table 6 for the SCFs used in the Tool and 
Section 4.4 for more information about the localization 
method.
3.3  Other Factors Affecting Efficiency and 
Emissions 
Bus operational efficiency and emissions are affected 
by multiple other factors. In the default dataset 
under “Advanced Features,” the Tool captures three 
key variables: operational speed, load factor, and 
air conditioning (AC). These factors are commonly 
discussed in papers and analyzed during road tests. 
Temperature and slope are environmental factors that 
affect the operational efficiency and emission factors of 
Table 6  |  Social Cost Factors for Transport Emissions (US$/tonne)
Country CO2 CH4 N2O PM10 PM2.5 NOX CO HC
Brazil 24.20 7,528.59 41,525.41 7,190.99 405.13 
China 24.10 812.00 7,461.00 8,745.73 48,238.80 8,353.55 1,146.00 470.62 
European Union 0.00 24,753.00 136,530.00 23,643.00 1,332.00 
India 85.40 3,138.25 17,309.64 2,997.52 168.87 
Mexico 11.90 9,679.07 53,386.78 9,245.03 520.85 
United States 42.00 1,200.00 15,000.00 33,264.74 183,478.15 31,773.05 1,790.03 
Global 417.00 10,236.80 56,463.06 9,777.75 550.86 
Notes:  European social cost factors (SCFs), and therefore the localized SCFs for other countries’ air pollutants, cover all impacts including health effects, crop loss, biodiversity loss, and material 
damage. Abbreviations: CO2: carbon dioxide; CH4: methane; N2O: nitrous oxide; PM10/PM2.5: particulate matter of 10 or 2.5 or less micrometers in diameter, respectively; NOx: nitrogen 
oxides; CO: carbon monoxide; THC: total hydrocarbons.
Sources:  SCFs for greenhouse gasses (CO2, CH4, N2O): EPA n.d.; World Bank 2017; Ricke et al. 2018; World Bank and IHME 2016. SCFs for air pollutants were calculated through a value transfer 
approach based on data from the European Union (van Essen et al. 2019). We used a unit value transfer approach with income adjustments based on the recommendation of (van Essen et 
al. 2019; World Bank and IHME 2016).
buses and are often of concern to operators during the 
initial phases of electric bus adoption. However, due 
to data availability, it is difficult to estimate the exact 
impact of these factors, which is discussed later as a 
limitation of this tool.
Ideally, correction factors for these variables can help 
adjust the variances. However, the data in the default 
dataset cannot generate a valid or robust correction 
factor. In addition, the information varies a great deal 
under different conditions, geographies, and even 
operational behaviors, so it would not be possible 
to use just one number to represent bus operational 
efficiency and emissions. Therefore, in this tool, default 
fuel efficiencies and emission factors are collected by 
different speeds and load factors and whether AC is 
running, when such information is available. Users 
may choose different combinations of these variables 
to get the specific fuel efficiency and emission factor 
information they are looking for.

The Costs and Benefits Appraisal Tool for Transit Buses
TECHNICAL NOTE  |  October 2020  |  21
Some additional explanations and analyses are 
provided in the next section, which try to capture the 
general impact these factors have on fuel efficiency and 
emissions with some ballpark numbers. Users can refer 
to the information when using the Tool. 
3.3.1 Speed, Load Factor, and Air Conditioning
Studies generally agree that emission factors (in grams 
per liter or grams per kilowatt-hour) decrease as the 
vehicle speeds up and increase as the load increases 
(Huang et al. 2013; Yao et al. 2015; S. Zhang et al. 
2014; He et al. 2018; X. Wu et al. 2015). However, the 
variations depend on specific operational conditions and 
local circumstances, which make it hard to modify EFs 
by a single correction factor. For instance, in a study in 
China (He et al. 2018), fuel consumption at the speed of 
5–10 km/h is 2.00–2.65 times that at a speed over 30 
km/h for a 10-meter electric bus; for a 12-meter electric 
bus, a 12-meter hybrid bus, and a 12-meter diesel bus, 
the numbers are 2.01–2.16, 2.77, and 2.61, respectively. 
In a study done in Brazil (Dreier et al. 2018b), when the 
speed decreases from 25–30 km/h to 15–20 km/h, the 
fuel consumption increases by 36 percent to 142 percent. 
Things are more complicated for air pollutants. He et 
al. (2018) show that for diesel buses, the correction 
factors in terms of speed (5–10 km/h versus over 30 
km/h) of THC, NO x, and PM2.5 are 3.16, 3.10, and 
3.02, respectively. Calculated using the European 
Environmental Agency’s (EEA’s) 2019 air pollutant 
emission inventory guidebook, the emission factors at 
the speeds of 30 km/h versus 50 km/h of CO, THC, NO x, 
and PM2.5 are 1.52, 1.54, 1.24, and 1.33, respectively 
(EEA 2019b).
In terms of passenger load, the EEA (2019a) indicates 
that emission factors for CO, THC, NO x, and PM2.5 at 
full load compared with an empty load are 1.33, 0.99, 
1.32, and 1.30, respectively. From empty load to half 
load, He et al. (2018) find an increase in the emission 
factors of pollutants varying from 1.13 to 1.33.
The fuel efficiency of ICE buses generally decreases on 
extreme hot and cold days due to the use of AC or a 
heating system (Kwon et al. 2017; S. Zhang et al. 2014a; 
S. Zhang et al. 2014c; He et al. 2018). Studies in China 
show that operating with air conditioning increases the 
fuel consumption of hybrid buses by 32–55 percent but 
only by 3–26 percent for diesel buses (S. Zhang et al. 
2014b). Though most pollutant emissions increase as AC 
operates, emissions sometimes decrease; for example, by 
40 percent for NO x and 21 percent for THC emitted by 
hybrid buses (S. Zhang et al. 2014b) and by 9 percent for 
THC emitted by LPG buses (Hu et al. 2009).
3.3.2 Temperature
The impact of extreme temperature may be still larger 
for battery-powered electric buses. On cold days, there 
is no excess engine heat to be used for cabin heating 
(Rastani et al. 2019). And both excessively hot and cold 
temperatures lead to battery degradation or a reduction 
in battery range (Neubauer and Wood 2014; Yuksel and 
Michalek 2015). 
3.3.3 Slope
Studies of light-duty and heavy-duty vehicles consistently 
show that on-road tailpipe emission factors increase with 
road grade or slope, due to larger driving resistance and 
more frequent high engine load points (Gallus et al. 2017; 
L. Zhang et al. 2019; Prakash and Bodisco 2019). The 
emissions characteristics for mountainous and lowland 
areas are therefore different. The effect is similar for ICE 
vehicles and electric vehicles. However, research focused 
on electric buses is still limited and it is hard to provide 
an accurate factor.
In addition, although not included in this tool due to a 
lack of data and variances, vehicle age, driving behavior, 
and fuel quality also impact efficiency and emissions. In 
general, older vehicles and aggressive driving behavior 
increase energy consumption. Higher octane fuels with 
less complete combustion may reduce fuel efficiency 
and increase emissions. Other factors are not included 
in the Tool because of inconsistent findings or difficulty 
quantifying the impacts. These include after-treatment 
devices like selective catalytic reduction (SCR) systems 
and particulate filters, which can significantly reduce 
NOx and PM emissions, respectively (Weiss et al. 2012; 
Mccaffery et al. 2020). However, SCR may not function 
well when exhaust temperature is low (Liu et al. 2011; S. 
Zhang et al. 2014a). Evidence also shows that aggressive 
driving could contribute to high NOx emissions (Huang et 
al. 2013; Prakash and Bodisco 2019), but driving styles are 
hard to define and quantify.

22  |  
4. CALCULATIONS
The general output calculation methodology is the same 
as that in the first version of this tool, the Bus Costs 
and Emissions Appraisal Tool (Cooper et al. 2019). 
Financing cost, annualized cost, unit cost, and 
emissions calculation methodologies are the 
same as those used in the previous version.  For 
local air pollutants, the categories have been narrowed 
down to PM2.5, PM10, NO x, THC, and CO, given 
applicability. Simplification and adjustments were made 
in a few categories below, based on data availability, 
user friendliness, and electric bus–related features. 
The Tool also applies two general methods for cost-
related calculations:
 ▪ A present value (PV)  calculation is used to 
address lifespan differences between buses. All 
direct and indirect costs of buses over their lifetimes 
are discounted to present values so that costs are 
comparable. Avoided social costs, or social benefits, 
are also translated into present values. However, a 
net present value approach is not used here since 
the costs and social benefits are not calculated in a 
comparable way—all bus costs are private costs to 
the internal account of bus operators, while social 
benefits represent the external benefits that are in 
the category of the public account—and they cannot 
simply be added together.
 ▪ Total cost of ownership (TCO)  is used for the 
bus cost calculation because of the different cost 
profiles of different bus technologies over different 
bus lifespans. Electric buses can have higher 
upfront procurement costs, but can save costs 
during operation and have longer operational lives. 
Although the higher upfront costs may not be ideal 
for bus operators, the total costs may be lower over 
the lifetime of a bus. TCO methodology can thus 
be a more accurate way to make cost comparisons 
between diesel and electric buses. In this tool, TCO is 
translated into present value for final comparison. 
4.1 Capital Costs
The capital cost, or upfront procurement cost, 
calculation has been adjusted slightly from the previous 
version of the Tool (Equation 1). A subsidy is included 
in the function to capture the public grant option. A 
subsidy need not be considered if the procurement 
cost or down payment is not the original price and 
already includes a subsidy (e.g., in China’s case, the 
procurement cost reflects the original procurement 
price minus the government procurement subsidy). 
Infrastructure cost includes procurement and 
construction costs. Users have the flexibility not to 
include subsidy- and infrastructure-related costs, and to 
adjust the number of chargers and the electricity price 
based on their business models. 
Equation 1.
 PV of Lifetime Capital Cost
          = DP - RV - Subsidy + n × (IFP+IFC) + ∑     Pi
where DP = down payment; RV = PV of bus’s 
residual value; n = number of infrastructures; 
IFP = infrastructure procurement cost and IFC = 
infrastructure construction cost, both of which happen 
in year 0; Pi = principal in year i; r = discount rate; L = 
bus useful life; i = year i. 
4.2 Operation and Maintenance Costs
The operation and maintenance costs are simplified 
in this tool and incorporate cost categories listed and 
defined as follows: Labor cost is the operating labor 
cost; fuel cost includes the cost of electricity if the bus 
uses electricity; other operating costs include insurance 
and any additional operating costs; maintenance 
costs include a fixed annual maintenance cost and 
maintenance labor cost (depending on business model); 
the overhaul cost is a one-time engine overhaul or 
battery replacement cost occurring during the bus’s 
lifespan (Equation 2).
Equation 2. 
 Total O&M Cost
          = Labor Cost + Fuel Cost + Other Operating Costs
              +  Maintenance Costs + Onetime Overhaul        
Cost + Infrastructure O&M Costs
4.3 Infrastructure O&M Costs
In the previous version of the Tool, the variable 
“(additional) depot/infrastructure cost” was considered 
a one-time upfront cost for infrastructure in the 
initial year (year 0). It was calculated based on the 
infrastructure construction cost, the retrofit cost, 
and the cost of other special tools. In this version, 
infrastructure cost represents only procurement and 
i=1
L
(1+r)i

The Costs and Benefits Appraisal Tool for Transit Buses
TECHNICAL NOTE  |  October 2020  |  23
construction costs. Other costs related to operating 
and maintaining the infrastructure in some business 
models are captured in this new category. To simplify 
the calculation and given data availability, the costs 
are calculated based on the annual operation and 
maintenance costs of the overall infrastructure (e.g., all 
chargers operated by the bus operator), rather than on 
the basis of a single infrastructure. 
The PV of total infrastructure-related costs is 
also included in the outputs, combining the PV of 
infrastructure-related capital costs and the PV of 
infrastructure O&M costs (Equation 3). The costs are 
split into two categories in the Tool.
Equation 3. 
PV of Lifetime Infrastructure O&M Cost= ∑ (IFO+IFM) i 
where IFO = annual infrastructure operation 
cost shared by all infrastructures; IFM = annual 
infrastructure maintenance cost shared by all 
infrastructures; r = discount rate; L = bus useful life,  
i = year i.
Maintenance and Overhaul Costs
Maintenance costs (Equation 4) and overhaul costs 
(Equation 5) are simplified in the Tool, due to data 
availability, differences in maintenance models, and 
the reduced need for overhaul due to technology 
enhancement. However, a one-time overhaul cost is still 
included in the Tool to capture the potential need for 
engine overhaul and battery replacement. 
Equation 4.
    PV of Lifetime Maintenance Cost
              = N × ∑ (FAM+AM+ML) i 
where N = number of buses within a bus type;  
FAM = fixed annual maintenance cost; AM = additional 
maintenance cost; ML = maintenance labor;  
r = discount rate; L = bus useful life, i = year i.
Equation 5. 
PV of Lifetime Overhaul Cost = N ×   OOn 
where N = number of buses within a bus type; OO = 
One-time engine overhaul cost or battery replacement 
i=1
L
(1+r)i
cost; r = discount rate; L = bus useful life, n = the year 
when the overhaul happens ( n = L/2+1 if L is even and 
n = (L+1)/2 if L is odd).
4.4 Social Cost
We employed a commonly used, top-down approach 
to calculate social cost due to its simplicity and fewer 
data requirements. This practice entails reviewing the 
existing studies, obtaining initial social cost factors 
(usually in $/tonne) from different countries, and 
localizing the SCFs through a “value transfer” method 
(NEEDS 2009). SCFs measure the total social cost 
per unit mass pollutant within specified geographical 
boundaries. The social cost, therefore, can be estimated 
by multiplying SCF (in US$/tonne) by the amount of 
each air pollutant (in tonnes) within a specific region. 
Although it has a high level of uncertainty, it is the most 
appropriate way to evaluate social costs for a tool like 
this that covers multiple geographic regions. The total 
social costs (Equation 6) are represented separately as 
the sum of the costs of CO 2 (as the climate forcer) and 
the sum of all air pollutants (as the local public health 
threats; i.e., PM2.5, PM10, NO x, THC, and CO).
Equation 6. 
 PV of Social Cost j = N × ∑ Emission ij × SCFj
where Emission  = annual emissions of a certain air 
pollutant; SCF = social cost factor of a certain air 
pollutant; r = discount rate; j = type of atmospheric 
emissions, i = year i.
The value transfer method is applied to localize SCFs 
in the Tool. The value transfer procedure converts 
the estimated values from the “study site” to “another 
site” by adjusting for income. It can fill in gaps where 
country or regional values are not available from 
primary sources (van Essen et al. 2019). PPP-adjusted 
GDP per capita is used for value transfer calculations to 
address income differences across countries. This is an 
intermediate step and not an outcome calculation. The 
function is shown in Equation 7:
Equation 7. 
 SCFos = SCFss × ( GDP (PPP) per capita os
 )
e
where, PPP-adjusted GDP per capita  is in US$/capita; 
SCF is in US$/tonne; OS is the “other site,” or the other 
i=1
L
(1+r)i
(1+r)n
i=1
L
(1+r)i
GDP (PPP) per capita ss

24  |  
city or country for which we’d like to calculate SCFs; SS 
is the study site that already has the local SCF data; e 
is income elasticity of SCF, where income is the PPP-
adjusted GDP per capita. We assume e = 1.2 for middle-
income countries and 0.8 for high-income countries 
(World Bank and IHME 2016).
5.  LIMITATIONS AND FUTURE 
DEVELOPMENT OF THE TOOL
5.1  Limitations
Given the universal nature of the Tool and 
its global target audience, the Tool includes 
only general data and simplified functions to 
increase its applicability. 
The use of general data points from a literature 
review may not reflect real-world performance 
results. In addition, since the Tool has many variables 
and requires user input, the outputs also involve 
uncertainty. As briefly mentioned in Section 3.2, the 
data included in the Tool differ greatly across countries. 
Besides the factors that impact fuel efficiency and 
emissions discussed in Section 3.3, bus procurement, 
operation, and maintenance costs also depend on 
local context. Thus, if users use only the default cost 
information provided by the Tool, or default data 
combined with some local information, the results 
can provide only a general picture of the potential 
costs, rather than an estimate of the actual costs. 
Therefore, we recommended using the Tool as a first 
step in understanding the costs and social benefits 
of using different bus technologies. Other planning 
tools7 can be applied together with this one to provide 
a comprehensive picture of the situation and help bus 
operators and city officials plan for a bus fleet upgrade. 
The adoption of simplified functions—such as in the 
financing options section—is another limitation of the 
Tool. Table 7 shows some examples of procurement 
models and payment options observed in 22 cities 
operating electric buses (Moon-Miklaucic et al. 2019). It 
is hard to capture these nuances in one tool. However, 
the key differences in procurement costs and loan 
options have been included. In addition, cost categories, 
accounting rules, and other economic variables like 
discounting factors impact the results but are highly 
variable locally. Related information in this tool is only 
a reference point. 
The social cost calculation methodology adopted 
in this tool also has limitations. 
SCF values for certain air pollutants (e.g., PM2.5) 
can vary by more than three orders of magnitude (S. 
Song 2017). The reason could be that citizens assign 
very different willingness-to-pay values to pollution 
and health, or that the literature is very limited, with 
most existing studies still in their early stages and 
showing significantly different results (S. Song 2018; 
van Essen et al. 2019). The uncertainties in social cost 
evaluations will remain for a long time and sometimes 
be unavoidable, especially for developing countries (van 
Essen et al. 2019).
The current value transfer approach (using income 
adjustment) might underestimate SCFs in some 
countries or cities with high population densities. There 
is a positive correlation between SCFs and the density 
of the exposed population (S. Song 2017), so ignoring 
the influence of density might cause inaccurate SCF 
estimates. Future studies should further adjust the 
SCFs based on this and other factors, if necessary. For 
example, we will further develop the methodologies 
of SCF localization techniques to consider population 
density and many other characteristics in the countries 
for which we have data to better predict values in 
other places (e.g., benefit function transfer technique, 
meta-analysis if there are more available data). 
Decision-makers should also keep in mind that some 
uncertainties will always be there. And given current 
data limitations, the estimates could not include all 
negative externalities such as social inequity. Decision-
makers should always pay attention to the range of 
uncertainty and provide a detailed interpretation about 
why it exists.
5.2 Potential Future Development of the Tool
The Tool in its current form may not address all 
the concerns and needs of the intended audience. 
Additional related functions may be added to the Tool 
following user feedback. The topics below are regularly 
raised in discussions about electric buses. They are 
worth discussing by policy-makers and bus operators 
but are not the current focus of the Tool.   
Impact on the job market.  The growth of electric 
vehicles is transforming the entire vehicle industry. New 
players, such as stakeholders along the battery supply 
chain and charging infrastructure manufacturers, are

The Costs and Benefits Appraisal Tool for Transit Buses
TECHNICAL NOTE  |  October 2020  |  25
Table 7  |  Examples of Different Payment and Acquisition Methods for Electric Buses
Sources:  Moon-Miklaucic et al. 2019.
Type of 
Acquisition Source Features
Cash purchases
Grants often cover upfront costs but are time-limited and irregular
Preferential pricing sets prices at rates lower than otherwise available in the market
In-kind incentives provide support in the form of goods, services, training, and transactions that do 
not involve money
Operating 
budgets and 
budget transfer
Often used to cover operational or capital expenses
Includes farebox revenue and revenue from other operations such as property leasing and advertising 
or taxes 
Debt financing
Concessional 
loan
Provided by financier at flexible lending conditions 
Can encourage higher lending rates among local banks for environmentally beneficial investments 
Green bond
Created to fund projects that have positive environmental or climate benefits 
Backed by issuer’s entire balance sheet
Leasing
Lease-to-buy
Between operator and bus manufacturer
Operator pays rent over the course of the agreed-upon lease period and then purchases the bus at a 
designated price at the end of the contract
Allows operators to purchase buses without tying up their cash 
Purchase-
leaseback
Seller of asset leases the same asset from the buyer they sold it to 
Especially used in cities where third party leasing companies are not allowed to purchase vehicles directly
Details of arrangement are made immediately after sale of the asset
Battery lease Manufacturers own battery during lease term, and replace batteries when needed 
Operating lease
No residual value risks 
Predictable cash flow and cash flow benefits due to fixed monthly cost
Monthly payment paid out of operating income and offset against taxable profits
Financial lease
Only pay interest on the outstanding value
Potential tax and VAT benefits
Trade-in value: potential to profit from careful maintenance and use
Vehicle appears as an asset on the balance sheet

26  |  
entering the market, whereas vehicle maintenance 
workers and those in the conventional vehicle 
manufacturing industry may experience job losses 
(Todd et al. 2013). The Tool has a labor input regarding 
bus operators and maintenance workers but does not 
address the dynamics of the labor market. 
Operation decisions and implications.  Ideally, 
electric buses can replace ICE buses at a 1:1 ratio. 
However, due to various factors impacting the actual 
bus fleet operation—such as bus route selection, 
operation schedule, technology maturity, and location 
of charging infrastructure—the number of electric buses 
needed may be more than the number of original ICE 
buses (Xue et al. 2019). The Tool allows users to assume 
a certain replacement ratio in the advanced features, 
but does not help users estimate what the ratio is. 
Maintenance decisions and implications.  Electric 
buses generate lower maintenance costs because they 
are less complicated mechanically than diesel buses 
(Borén 2019), though battery replacement can be a 
burden to operators. In China, manufacturers usually 
provide guarantees for battery maintenance and/
or replacement, with details differing by contract. 
Maintenance schemes also differ, with some operators 
employing labor on-site, and others contracting out for 
a service package. Such variations are hard to capture 
in this tool and need to be analyzed on a case-by-case 
basis. 
Charging infrastructure planning and business 
models. The Tool mainly focuses on the bus fleet. 
Charging infrastructure is considered in a general 
manner, but is not correlated with the features of 
buses. Charging infrastructure location planning itself 
is an important topic for electric vehicle adoption and 
requires detailed modeling work, which is not within 
the scope of this tool. Business models for charging 
infrastructure vary by location and company (Hove 
and Sandalow 2019) and bus operators are encouraged 
to work with local service providers to determine the 
models that are most applicable. 
Financial planning and risk assessment. The 
Tool can compare the costs of different financial 
mechanisms used when purchasing buses, including 
financial products like subsidies and loans or other 
options such as preferential electricity rates and 
battery leasing to reduce cost factors. Users can apply 
the results to analyze the potential financial risks 
of different financing options to the bus operators, 
considering the operators’ existing financial situations, 
such as revenue profiles and other expenses. However, 
due to the existing scope, the Tool cannot provide a 
comprehensive risk assessment for users, other than 
making cost comparisons among different scenarios. 
In addition, the Tool does not allow users to directly 
explore and develop potential financing options. 
Measures such as battery leasing and financial leasing 
are innovative financing options that help lower the 
risks and costs associated with electric bus procurement 
(Moon-Miklaucic et al. 2019). Whether operators 
should adopt any new mechanisms should be analyzed 
on a case-by-case basis. Users can compare the cost 
implications associated with different financing options 
by adjusting the inputs in the Tool, but the current 
version of the Tool does not make recommendations 
to users about which financial mechanism might be 
optimal for them.
This tool provides an entry point for users to compare 
cost, operational, and emission data for different types 
of buses and understand the cost, emission, and social 
benefit implications of converting from diesel to electric 
bus fleets. City governments and bus operating agencies 
should conduct detailed analyses based on local 
information and business models before making any 
decisions regarding their bus fleets.

The Costs and Benefits Appraisal Tool for Transit Buses
TECHNICAL NOTE  |  October 2020  |  27
APPENDIX 1. EXPLANATIONS OF INPUTS
Variable Unit Description
Country* Investment 
incentive
Countries with default data. For the current version, users cannot customize country name, but can 
select the available country that best reflects the conditions in their location.
City
Cities with default data. For the current version, users cannot customize city name, but can select 
either the available city that best reflects the conditions in their location or “general” to see country 
averages for the remaining variables. Users can input their own data in both cases.
Discount rate*  % A discount rate is the rate of return used to discount future cash flows back to their present value.
Social discount 
rate*  %
The social discount rate (SDR) is the discount rate used in computing the value of funds spent on 
social projects. It is an estimate of how society values consumption at different points in time. This 
gives a social time preference (STP) approach that is appropriate for discounting costs and benefits 
measured in consumption units. The SDR reflects a society’s relative valuation of today’s well-
being versus well-being in the future. The appropriate selection of an SDR is crucial for cost-benefit 
analysis and has important implications for resource allocations. 
SDR is normally lower than corporate discount rates. There is wide diversity in SDRs, with developed 
nations typically applying a lower rate (3–7%) than developing nations (8–15%). The selection of 
the SDR is highly controversial and there is no consensus among economists. It is good practice to 
not use a single SDR, but to apply a stochastic approach whereby the SDR varies with the expected 
outcomes. It is also widely accepted that SDRs should decline over time, giving increasingly more 
weight to future generations.
It is worth noting that the SDR used in the Tool incorporates social projects that address other issues 
in addition to climate change. Thus, it is larger than the near-zero SRD (0–3%) used for climate-
related projects; e.g., the SDR for the United States is set at 7% in the Tool, and that for the UK at 3.5%.
Bus Fleet Information 
Bus size*  m
The Tool includes a variety of bus lengths. The most common is 12 meters (m), which is the major 
city bus length in many countries. The available bus sizes in the drop-down list within the Tool 
depend on the available default data in the city or country selected.
Fuel type*  L, kWh, MJ
The Tool includes common fuel types, including diesel, hybrid, electric, natural gas (compressed 
natural gas and liquified natural gas), gasoline, and liquified petroleum gas (LPG). The units vary 
based on the fuel type for emission factors and fuel efficiency. Normally, for diesel, hybrid, and 
gasoline buses, liters (L) are used; for electric buses, kilowatt-hours (kWh) are used; and for natural 
gas and LPG buses, Megajoules (MJ) are used. 
Emission 
standard*  
The Tool specifies only European emission standards based on data availability and to reduce the 
complexity of the Tool. Some countries may have their own emission standards but these are not 
reflected in the Tool. Users can refer to Section 3.2.3 for more information. 
Number of buses*  The number of buses in a fleet.

28  |  
Annual distance 
traveled (VKT)*  km The (average) annual distance a bus of a certain type travels.
Operational 
years*  years The typical useful life of a bus of a certain type. This should reflect the length of time after which 
buses must be retired or sold for reuse.
Fuel efficiency*
L/100 km
kWh/100 km
MJ/100 km
Fuel consumption by distance traveled.
Cost Factors
Procurement
Purchase price* $/bus The cost to buy one bus of a certain type, including all taxes and deductions that may be applied 
toward the base price.
Procurement 
subsidy $/bus The subsidies that can be applied to this bus, if not included in the purchase price.
Residual value* % The expected residual value of a single bus of a certain type.
Down payment* % The percentage required as a down payment for a loan to finance a bus of a certain type.
Loan interest 
rate* % The yearly interest rate that a certain bus type’s loan will have.
Loan time* years The expected term of the loan.
Operation
Annual labor cost 
(operation) $/bus/year The total cost to hire drivers for a certain bus type. Any factors taken into account for one bus type 
and fleet should also be included in subsequent bus types and fleets to remain consistent.
Fuel price*
$/L
$/kWh
$/MJ
The current fuel price for a certain bus type.
Fuel cost 
projection % The projected annual increase or decrease in fuel price for a certain bus type.
Additional fuel 
price* $/bus/year The cost for any fuel additive, charging service fee, or other fee.

The Costs and Benefits Appraisal Tool for Transit Buses
TECHNICAL NOTE  |  October 2020  |  29
Additional 
operational costs $/bus/year
Any other operational costs that weren’t covered in the previous categories. Any factors taken into 
account for one bus type and fleet should also be included in subsequent bus types and fleets to 
remain consistent.
Battery leasing costs can be included in this category. 
Insurance $/bus/year The cost of any insurance used.
Maintenance
Annual general 
maintenance 
cost*
$/bus/year The average maintenance cost for one bus of a certain type. If the maintenance is not done in-house, 
but contracted out, then the contract costs should be included here.
Annual labor cost 
(maintenance) $/bus/year
The total cost to hire maintenance workers for a certain bus type. Any factors taken into account 
for one bus type or fleet should also be included in subsequent bus types and fleets to remain 
consistent.
Additional 
maintenance 
costs
$/bus/year
Any other maintenance costs that weren’t covered in the previous categories. Any factors taken into 
account for one bus type or fleet should also be included in subsequent bus types and fleets to 
remain consistent. 
One-time overhaul 
cost $/bus
The Tool assumes only one overhaul during the total lifespan of a bus, if one is needed. It largely 
depends on the operator’s contract with the manufacturer, and whether the operator decides to replace 
the entire vehicle at once or just key parts.
The cost of a battery replacement or engine overhaul can be included here for electric buses and ICE 
buses. 
Infrastructure
Infrastructure related to charging (for electric vehicles) or fuel filling (for ICE vehicles). Depots are 
not considered a default infrastructure-related cost. However, if users want to include depot-related 
costs, they should fill in related information as annual operational costs, maintenance costs, or other 
one-time costs, based on local business models for depots. Users can refer to Section 2.3 for more 
information. 
Additional
Administration $/year Any overarching indirect costs that weren’t covered in the previous categories, but that are important 
to include for the correct cost calculation of a certain fleet. 
Other taxes and 
fees $/year Any additional taxes and fees that weren’t covered in the previous categories, but that are important to 
include for the correct cost calculation of a certain fleet.

30  |  
Emission factors Emission factors include tailpipe emissions (tank-to-wheel) and upstream emissions (well-to-tank). 
Tailpipe g/L, g/MJ
The default data are collected by bus length, fuel type, and emission standard, when such data are 
available for tailpipe emissions. Tailpipe emission factors cover air pollutant emissions and carbon 
emissions for all types of buses. Electric buses have zero tailpipe emissions in this tool.
Upstream g/kWh
Upstream emission factors are collected for different fuels, including emission factors of fossil 
fuel production processes, and grid emission factors, which account for emissions generated by 
electricity used when operating electric buses. Upstream emission factors cover carbon emissions for 
all types of buses.
Social cost factors
The Tool defines social cost as the cost of externalities. Social cost factors measure the total social 
cost per unit mass of each pollutant (in US$/tonne) at the national level. Social cost represents the 
sum of the private (internal) and external costs (Korzhenevych et al. 2014; S. Song 2017). 
Advanced features Please refer to Sections 2.2 and 3.3 for more information.
Replacement ratio
The replacement ratio refers to the number of electric buses—or buses with more advanced 
technology—it takes to achieve the same level of service as one traditional ICE bus. Ideally, the ratio 
is 1:1. We recommend users use 1:1 and 2:1 to represent different scenarios and levels of technology 
readiness.
Notes:  Variables with an asterisk represent mandatory variables. When data are either not available or not applicable, a 0 must be filled in for the Tool to function. Abbreviations: ICE: internal 
combustion engine; km: kilometer; L/100 km: liters per 100 kilometers; kWh/100 km: kilowatt-hours per 100 kilometers; MJ/100 km: Megajoules per 100 kilometers; g/L: grams per liter; 
g/MJ: grams per Megajoule; g/kWh: grams per kilowatt-hour.
Source: Authors.

The Costs and Benefits Appraisal Tool for Transit Buses
TECHNICAL NOTE  |  October 2020  |  31
APPENDIX 2. DEFAULT DATA
a. 
c. 
b. 
China
Diesel Hybrid Gasoline NG
Pre 
Euro
Euro 
I
Euro 
II
Euro 
III
Euro 
IV
Euro 
V
Euro 
III
Euro 
IV
Euro 
V
Pre 
Euro
Euro 
I
Euro 
II
Euro 
III
Euro 
IV
Euro  
V
Euro 
II
Euro 
IV
Euro 
V EEV
CO 31.1 29.1 25.3 19.2 8.5 4.3 1.0 3.2 522.2 316.8 79.2 42.8 21.0 21.0 17.9 7.0 1.2 9.8
CO2 807.6 844.2 996.7 787.3 736.0 646.0 667.7 1,056.1 836.5
HC 5.9 1.3 0.8 0.6 0.2 0.1 0.2 0.1 17.0 16.4 6.2 2.9 1.5 1.5 6.5 1.4 1.5
NOx 19.5 17.5 15.3 15.2 16.1 14.3 10.3 5.9 7.5 3.9 3.9 2.3 1.2 0.9 19.8 6.9 4.4 5.8
PM2.5 1.9 1.5 1.3 0.6 0.4 0.2 0.2 0.5 0.2 0.1 0.1 0.1 0.1
Austria France Germany Norway Sweden Switzerland
Diesel NG Diesel NG Diesel NG Diesel NG Diesel NG Diesel NG
CO 1.2 0.7 1.9 0.7 0.7 1.2 0.8 0.8 1.6 0.8 0.7 0.8
CO2 831.5 827.0 952.1 1006.9 1223.9 1291.8 831.2 987.5 1032.5 1019.9 1143.6 1114.8
THC 0.1 0.2 0.1 0.2 0.1 0.4 0.0 0.3 0.0 0.3 0.0 0.3
NOx 2.0 0.9 3.7 1.5 3.4 2.5 1.8 1.2 2.5 1.3 3.5 1.6
PM2.5 0.0 0.0 0.1 0.0 0.0 0.0 0.0 0.0 0.1 0.0 0.0 0.0
India
Diesel NG
Euro II Euro II
CO 1.2 3.2
CO2 782.1 729.7
THC 0.2 1.5
NOx 8.6 5.4
Table A2.1 a–g  |  Tailpipe/Exhaust Emission Factors for 12-Meter Buses by Country/Region

32  |  
d. 
e. 
Mexico Chile Colombia Brazil
Diesel Diesel Hybrid Diesel Hybrid
Diesel Hybrid
Average Euro V Average Euro V
CO 26.7 7.6 0.4 6.4 3.3 7.1 2.6
CO2 750.0 993.8 667.4 1,011.0 843.7 1,257.8 1,341.2 1,232.1 595.4
THC 0.1 0.0 0.5 0.0 0.2 0.1
NOx 5.7 14.1 2.6 12.2 3.9 11.8 8.1
US Diesel Hybrid NG
CO 5.1 0.1 3.4
THC 0.0 0.0 3.6
NOx 7.4 0.5 4.1
PM2.5 0.3 0.0
CO2 922.4 1,008.8 897.3
f. 
g. 
UK
Diesel
Pre Euro Euro I Euro II Euro III Euro IV Euro V Euro VI
CO 5.7 3.1 2.6 2.5 0.3 0.26 0.3
THC 2.1 1.0 0.6 0.5 0.0 0.03 0.0
NOx 16.9 10.9 11.5 10.4 6.0 3.76 0.8
CO2 1,249.5 1,045.7 1,006.5 1,056.8 998.6 1,020.92 1,020.9
EU
Diesel NG
Pre Euro Euro I Euro II Euro III Euro IV Euro V EEV Euro VI Euro I Euro II Euro III EEV
CO 5.6 2.5 2.2 2.3 1.1 1.5 0.15 0.2 8.4 2.7 1.0 0.6
THC 1.7 0.6 0.4 0.4 0.1 0.1 0.01 0.0 7 4.7 1.3 1.2
NOx 17.1 11.1 11.4 9.6 6.4 4.3 6.35 0.6 16.5 15.0 10.0 3.8
PM2.5 0.8 0.4 0.2 0.2 0.0 0.0 0.0 0.02 0.0 0.0 0.0
Notes:  Units are in grams per kilometer. Emission standards are provided if they were given in the source. Abbreviations: NG: natural gas; CO: carbon monoxide; CO2: carbon dioxide; THC: total 
hydrocarbons; NOx: nitrogen oxides; PM2.5: particulate matter of 2.5 micrometers or less in diameter.
Source:  CARB 2019; Chen et al. 2017; Dreier et al. 2018; Ntziachristos and Galassi 2014; EEA 2019a; Guo et al. 2015; Goswami and Chandra Tripathi 2019; Giraldo and Huertas 2019; Matzer 
et al. 2019; He et al. 2018; Hu et al. 2009; MEE 2015; Merkisz et al. 2016; MJB&A 2013; ISSRC 2013; Roychowdhury 2010; Q. Song et al. 2018; X. Wu et al. 2015; Y. Wu et al. 2012; S. 
Zhang et al. 2014b; S. Zhang et al. 2014c; Zhou et al. 2016.

The Costs and Benefits Appraisal Tool for Transit Buses
TECHNICAL NOTE  |  October 2020  |  33
Country Emission Standard Diesel 
(L/100km)
Electric 
(kWh/100km)
Hybrid 
(L/100km)
NG 
(MJ/100km)
China
Average 40.9 149.9 33.1 1,437.3
EEV 1,410.0
Euro II
Euro III 30.7
Euro IV 31.8
Euro V 37.1 28.2
India
Average 29.0 24.3
Euro I 24.5
Euro II 26.0
Euro III 23.4
Euro IV 22.6
Austria Average 30.9 136.7 1,471.9
France 36.0 133.3 1,627.1
Germany Average 46.6 262.0 1,967.4
Norway 31.4 1,595.7
Sweden Average 39.3 157.6 1,648.0
Switzerland 43.4 188.2 1,978.4
United Kingdom
Pre Euro 55.2
Euro I 44.4
Euro II 42.3
Euro III 45.8
Euro IV 42.4
Euro V 44.0
Euro VI 44.0
Mexico Average 34.4
Chile Average 37.5 25.2
Colombia Average 37.7 31.8
Brazil Average 49.1 43.7
Euro V 44.6 10.1
European Union
Pre-Euro 43.6
Euro I 35.8 2,664.0
Euro II 35.8 2,472.0
Euro III 35.8 2,184.0
Euro IV 35.8
Euro V 35.8
EEV 2,184.0
Euro VI 35.8
Table A2.2  |  Fuel Efficiency of 12-Meter Buses by Country/Region

34  |  
United States Diesel 
(L/100km)
Electric 
(kWh/100km)
Hybrid 
(L/100km)
NG 
(MJ/100km)
Gasoline 
(L/100km)
LPG 
(MJ/100km)
Biodiesel 
(L/100km)
Average 46.1 154.1 46.7 2,171.8 32.1 1,812.8 66.8
Country Discount Rate Discount Rate 
Year
Social 
Discount Rate
Social 
Discount Rate 
Year
Inflation Rate Bank Lending 
Rate
Bank Lending 
Rate Year
United States 0.25% 2020 3.50% 2018 0.60% 3.25% 2020
United Kingdom 0.10% 2020 3.50% 2018 1.20% 0.35% 2020
European Union 0.25% 2017 3.00% 2018 1.20% 0.25% 2018
Austria 0.00% 2020 3.00% 2018 0.40% 1.33% 2020
Poland 0.10% 2020 3.00% 2018 3.20% 2.41% 2020
France 0.25% 2017 3.00% 2018 0.30% 1.20% 2020
Germany 0.25% 2017 3.00% 2018 0.30% 1.93% 2020
Sweden 0.00% 2020 3.00% 2018 0.50% 0.10% 2020
Switzerland -0.75% 2020 3.00% 2018 -0.40% 2.63% 2020
Brazil 8.73% 2020 5.10% 2008 3.60% 40.73% 2020
China 2.90% 2020 8.70% 2019 3.00% 4.35% 2020
India 4.25% 2020 9.90% 2019 3.30% 13.50% 2020
Chile 3.35% 2015 4.60% 2008 3.40% 4.82% 2020
Colombia 6.25% 2019 4.20% 2008 3.50% 9.96% 2020
Mexico 7.25% 2017 3.30% 2008 2.70% 6.30% 2020
Notes:  Abbreviations: NG: natural gas; LPG: liquified petroleum gas; L/100 km: liters per 100 kilometers; kWh/100 km: kilowatt-hours per 100 kilometers; MJ/100 km: Megajoules per 100 
kilometers. 
Sources:  Chen et al. 2017; Roychowdhury 2010; Guo et al. 2015; Boulter et al. 2009; Giraldo and Huertas 2019; Gota et al. 2014; He et al. 2018; MJB&A 2013; Barnitt and Chandler 2006; Dreier 
et al. 2018; X. Wu et al. 2013; Q. Song et al. 2018; EEA 2019a; Zhou et al. 2016; Borén 2019; APTA 2018; Dallmann 2019; Goswami and Chandra Tripathi 2019; Barnitt et al. 2008; 
GGGI and CSTEP 2016; Lammert 2008; Göhlich et al. 2014; Barnitt 2008; Huo et al. 2012; ISSRC 2013; HBEFA 2019; Prohaska et al. 2016; AC Transit 2018; S. Zhang et al. 2014b.
Sources:  CEIC 2020a; CEIC 2020b; Trading Economics 2020a; Trading Economics 2020b; Moore and Vining 2018; Freeman et al. 2018; Lopez 2008; Global Petrol Prices 2020.
Table A2.3  |  General Profiles of Countries in the Tool

The Costs and Benefits Appraisal Tool for Transit Buses
TECHNICAL NOTE  |  October 2020  |  35
Country
VKT  
(km/year 
/bus)
Operational 
Years
Average 
Speed  
(km/h)
Bus Length 
(m)
Residual 
Value (%)
Charger 
Construction 
Costs ($)
Charger 
Procurement 
Cost ($)
Charger 
Operation 
Costs  
($/year)
Charger 
Maintenance 
Costs  
($/year)
United 
States 40,250 12 >30 12 0 28,312 75,000
United 
Kingdom 60,000 12 20-25 12 0 28,312 75,000
European 
Union 60,000 12 20-25 12 0 28,312 75,000
Austria 60,000 12 20-25 12 0 28,312 75,000
Poland 60,000 12 20-25 12 0 28,312 75,000
France 60,000 12 15-20 12 0 28,312 75,000
Germany 60,000 12 20-25 12 0 28,312 75,000
Sweden 60,000 12 20-25 12 0 28,312 75,000
Switzerland 60,000 12 15-20 12 0 28,312 75,000
Brazil 88,000 10 20-25 12 0 5,784 20,128.32 867.60 86.76
China 57,962 13 15-20 12 0 5,784 20,128.32 867.60 86.76
India 39,600 15 15-20 12 0 5,784 20,128.32 867.60 86.76
Chile 111,120 12 20-25 12 0 5,784 20,128.32 867.60 86.76
Colombia 60,000 12 20-25 12 0 5,784 20,128.32 867.60 86.76
Mexico 60,000 12 20-25 12 0 5,784 20,128.32 867.60 86.76
Notes:  Abbreviations: VKT: vehicle kilometers traveled; km: kilometers; m: meters.
Sources: Nicholas 2019; Shengang Securities 2020; Urban Bus Toolkit 2006; Q. Song et al. 2018; ACEA 2020; MEE 2012; Dimensions.com n.d.
Table A2.4  |  Fleet Assumptions

36  |  
REFERENCES 
AC Transit. 2018. “Progress Report on the District’s Study on ZEB Expansion 
and Facilities Assessment.” http://www.actransit.org/wp-content/uploads/
board_memos/18-134 ZEB Assessment.pdf.
ACEA (European Automobile Manufacturers Association). 2020. “Average 
Vehicle Age.”
Ang-Olson, J., and A. Mahendra. 2011. “Cost/Benefit Analysis of Converting 
a Lane for Bus Rapid Transit — Phase II Evaluation and Methodology.” 
Transportation Research Board, April.
APTA (American Public Transportation Association). 2018. “National Transit 
Database 2018.” https://www.apta.com/research-technical-resources/transit-
statistics/ntd-data-tables/.
ANL (Argonne National Laboratory). 2020. “Alternative Fuel Life-cycle 
Environmental and Economic Transportation (AFLEET) Tool.” Last updated 
March 2, 2020. https://greet.es.anl.gov/afleet_tool.
Barnitt, R.A. 2008. In-Use Performance Comparison of Hybrid Electric, CNG, 
and Diesel Buses at New York City Transit. SAE Technical Papers. Warrendale, 
PA: SAE International. https://doi.org/10.4271/2008-01-1556.
Barnitt, R., and K. Chandler. 2006. New York City Transit (NYCT) Hybrid 
(125 Order) and CNG Transit Buses. Golden, CO: National Renewable Energy 
Laboratory.
Barnitt, R., R.L. McCormick, and M. Lammert. 2008. St. Louis Metro Biodiesel 
(B20) Transit Bus Evaluation: 12-Month Final Report. Golden, CO: National 
Renewable Energy Laboratory. http://www.nrel.gov/docs/fy08osti/43486.pdf 
https://trid.trb.org/view/908189.
BNEF (Bloomberg New Energy Finance). 2018. “Electric Buses in Cities 
Driving towards Cleaner Air and Lower CO2.” Blog. https://about.bnef.com/
blog/electric-buses-cities-driving-towards-cleaner-air-lower-co2/.
Borén, S. 2019. “Electric Buses’ Sustainability Effects, Noise, Energy Use, and 
Costs.” International Journal of Sustainable Transportation, September: 1–16. 
https://doi.org/10.1080/15568318.2019.1666324.
Boulter, P.G., T.J. Barlow, and I.S. Mccrae. 2009. “Emissions Factors 2009: 
Report 3—Exhaust Emission Factors for Road Vehicles in the United 
Kingdom.” Prepared for the Department of Transport, United Kingdom. TRL 
Limited.
CARB (California Air Resources Board). 2019. “Methods to Find the Cost-
Effectiveness of Funding Air Quality Projects: Emission Factor Tables.”
CEIC. 2020a. “Chile CL: Discount Rate: End of Period.” 
CEIC. 2020b. “Colombia CO: Discount Rate: End of Period.” 
ChinaBuses. 2020. “Passenger Vehicle Bids.” (In Chinese.) https://www.
chinabuses.com/tender/.
Chen, X., X. Shan, J. Ye, F. Yi, and Y. Wang. 2017. “Evaluating the Effects of 
Traffic Congestion and Passenger Load on Feeder Bus Fuel and Emissions 
Compared with Passenger Car.” Transportation Research Procedia 25: 
616–26.
ENDNOTES
1. It is worth noting that emissions at power plants will increase as the 
plants generate electricity to power the vehicles, redistributing the pol -
lution that previously came from vehicle tailpipes in densely populated 
areas to power plant locations, which tend to be less populated.   
2. PM10 and PM2.5 refer to particulate matter with diameters of 10 and 2.5 
micrometers or less, respectively.  
3. In the Tool’s database, most studies include carbon dioxide, methane, 
and nitrous oxide using the 100-year global warming potentials sug -
gested by the Fifth Assessment Report of the United Nations Intergov -
ernmental Panel on Climate Change: 1,34, and 298, respectively; one 
US study included black carbon (with a global warming potential of 900) 
instead of nitrous oxide.  
4. Work in progress. 
5. This does not necessarily mean that data are more available in these re -
gions, or that the results are more accurate for these regions. The dataset 
is not intended to be comprehensive. The collection process and the size 
of the dataset were limited by time and resources available.  
6. Emission standards other than European standards exist; for example, 
the U.S. Environmental Protection Agency standards are used in Central 
American countries and those that have signed on to the North American 
Free Trade Agreement. However, these standards are not included in 
this version of the tool. Future development may cover more emission 
standards.  
7. Work in progress.

The Costs and Benefits Appraisal Tool for Transit Buses
TECHNICAL NOTE  |  October 2020  |  37
Cooper, E., E. Kenney, J.M. Velasques, X. Li, and T. Hein Tun. 2019. 
“Costs and Emissions Appraisal Tool for Transit Buses.” Washington, 
DC: World Resources Institute. https://wriorg.s3.amazonaws.com/
s3fs-public/costs-emissions-appraisal-tool-transit-buses.pdf?_
ga=2.153840504.1989315013.1554690110-29079707.1530758621.
Dallmann, T. 2019. “Climate and Air Pollutant Emissions Benefits of Bus 
Technology Options in São Paulo.” Washington, DC: International Council on 
Clean Transportation. https://www.theicct.org/sites/default/files/publications/
Emissions_benefits_bus_sao paulo_201902014.pdf%0Ahttps://trid.trb.org/
view/1584764.
DHI (Department of Heavy Industry). 2019. “About FAME II.” https://fame2.
heavyindustry.gov.in/content/english/13_1_brief.aspx.
Dimensions.com. n.d. “City: Transit Buses.” Accessed October 12, 2020.  
https://www.dimensions.com/element/city-transit-buses.
Donat, L., H. Schindler, J. Burck, et al. 2019. Brown to Green: The 
G20 Transition towards a Net-Zero Emissions Economy 2019. Climate 
Transparency.
Dreier, D., S. Silveira, D. Khatiwada, K.V.O. Fonseca, R. Nieweglowski, 
and R. Schepanski. 2018. “Well-to-Wheel Analysis of Fossil Energy Use 
and Greenhouse Gas Emissions for Conventional, Hybrid-Electric and 
Plug-in Hybrid-Electric City Buses in the BRT System in Curitiba, Brazil.” 
Transportation Research Part D: Transport and Environment 58 (January): 
122–38. https://doi.org/10.1016/j.trd.2017.10.015.
EEA (European Environment Agency). 2017. “CO2 Emission Intensity.” https://
www.eea.europa.eu/data-and-maps/daviz/co2-emission-intensity-5.
EEA. 2019a. “1.A.3.b.i-Iv Road Transport Appendix 4 Emission Factors 
2019.” https://www.eea.europa.eu/publications/emep-eea-guidebook-2019/
part-b-sectoral-guidance-chapters/1-energy/1-a-combustion/road-transport-
appendix-4-emission/view.
EEA. 2019b. “EMEP/EEA Air Pollutant Emission Inventory Guidebook 2019.”
EPA (U.S. Environmental Protection Agency). n.d. “The Social Cost of Carbon: 
Estimating the Benefits of Reducing Greenhouse Gas Emissions.” Accessed 
June 4, 2020. https://19january2017snapshot.epa.gov/climatechange/social-
cost-carbon_.html.
EPA. 2020. “Emissions & Generation Resource Integrated Database (EGRID) 
EGRID2018.” Washington, DC: EPA. https://www.epa.gov/energy/emissions-
generation-resource-integrated-database-egrid.
Eudy, L., and M. Jeffers. 2018. “Zero-Emission Bus Evaluation Results: 
County Metro Battery Electric Buses.” Golden, CO: National Renewable 
Energy Laboratory.
Eudy, L., R. Prohaska, K. Kelly, and M. Post. 2014. “Foothill Transit Battery 
Electric Bus Demonstration Results.” Golden, CO: National Renewable Energy 
Laboratory. https://www.nrel.gov/docs/fy16osti/65274.pdf.
Freeman, M., B. Groom, and M. Spackman. 2018. “Social Discount Rates 
for Cost-Benefit Analysis: A Report for HM Treasury.” London School of 
Economics, Department of Geography and Environment; University of York; 
Centre for Climate Change Economics and Policy; Grantham Research 
Institute on Climate Change and the Environment. 
Gallus, J., U. Kirchner, R. Vogt, and T. Benter. 2017. “Impact of Driving 
Style and Road Grade on Gaseous Exhaust Emissions of Passenger 
Vehicles Measured by a Portable Emission Measurement System (PEMS).” 
Transportation Research Part D: Transport and Environment 52 (2): 215–26.
GGGI and CSTEP (Global Green Growth Institute and Center for Study of 
Science, Technology & Policy). 2016. Electric Buses in India: Technology, 
Policy and Benefits. Seoul, Republic of Korea: GGGI, August: 82. https://
gggi.org/site/assets/uploads/2016/10/2016-08-Electric-Buses-in-India-
Technology-Policy-and-Benefits.pdf.
Giraldo, M., and J.I. Huertas. 2019. “Real Emissions, Driving Patterns and 
Fuel Consumption of In-Use Diesel Buses Operating at High Altitude.” 
Transportation Research Part D: Transport and Environment 77 (December): 
21–36. https://doi.org/10.1016/j.trd.2019.10.004.
Global Petrol Prices. 2020. “Retail Energy Price Data.” 
Göhlich, D., A. Kunith, and T. Ly. 2014. “Technology Assessment of an Electric 
Urban Bus System for Berlin.” WIT Transactions on the Built Environment 138: 
137–49. https://doi.org/10.2495/UT140121.
Goswami, R., and G. Chandra Tripathi. 2019. “Economic, Environmental and 
Congestion Impact on the Life-Cycle Cost of Ownership: A Case Study in 
the Delhi Transit Bus System.” International Journal of Electric and Hybrid 
Vehicles 11 (1): 59–72. https://doi.org/10.1504/IJEHV.2019.098719.
Gota, S., P. Bosu, and S. Kumar Anthapur. 2014. “Improving Fuel Efficiency 
and Reducing Carbon Emissions from Buses in India.” Journal of Public 
Transportation 17 (3).
Guo, J., Y. Ge, L. Hao, J. Tan, Z. Peng, and C. Zhang. 2015. “Comparison 
of Real-World Fuel Economy and Emissions from Parallel Hybrid and 
Conventional Diesel Buses Fitted with Selective Catalytic Reduction Systems.” 
Applied Energy 159 (December): 433–41. https://doi.org/10.1016/j.
apenergy.2015.09.007.
HBEFA (Handbook Emission Factors for Road Transport). 2019. “Handbook 
Emission Factors for Road Transport.” https://www.hbefa.net/Tools/EN/
MainSite.asp.
He, X., S. Zhang, W. Ke, Y. Zheng, B. Zhou, X. Liang, and Y. Wu. 2018. 
“Energy Consumption and Well-to-Wheels Air Pollutant Emissions of Battery 
Electric Buses under Complex Operating Conditions and Implications on Fleet 
Electrification.” Journal of Cleaner Production 171 (January): 714–22. https://
doi.org/10.1016/j.jclepro.2017.10.017.
Holland, S.P., E.T. Mansur, N.Z. Muller, and A.J. Yates. 2016. “Are There 
Environmental Benefits from Driving Electric Vehicles? The Importance of 
Local Factors.” American Economic Review 106 (12): 3700–29. https://doi.
org/10.1257/aer.20150897.

38  |  
Hove, A., and D. Sandalow. 2019. Electric Vehicle Charging in China and 
the United States. New York: Columbia University, School of International 
and Public Affairs. Center on Global Energy Policy.  https://energypolicy.
columbia.edu/research/report/electric-vehicle-charging-china-and-united-
states%0Ahttps://energypolicy.columbia.edu/sites/default/files/file-uploads/
EV_ChargingChina-CGEP_Report_Final.pdf.
 
Hu, H., Z. Zou, and H. Yang. 2009. On-Board Measurements of City Buses 
with Hybrid Electric Powertrain, Conventional Diesel and LPG Engines. SAE 
International. https://doi.org/10.4271/2009-01-2719.
Huang, C., D. Lou, Z. Hu, Q. Feng, Y. Chen, C. Chen, P. Tan, et al. 2013. “A 
PEMS Study of the Emissions of Gaseous Pollutants and Ultrafine Particles 
from Gasoline- and Diesel-Fueled Vehicles.” Atmospheric Environment 77: 
703–10. https://doi.org/10.1016/j.atmosenv.2013.05.059.
Huo, H., Q. Zhang, K. He, Z. Yao, and M. Wang. 2012. “Vehicle-Use Intensity 
in China: Current Status and Future Trend.” Energy Policy 43: 6–16. https://
doi.org/10.1016/j.enpol.2011.09.019.
IEA (International Energy Agency). 2019. “Global EV Outlook 2019.” https://
www.iea.org/reports/global-ev-outlook-2019.
IEA. 2020. “Electric Vehicles.” https://www.iea.org/reports/electric-vehicles.
IMP (India Ministry of Power). 2017. “Daily Reports.” http://www.cea.nic.in/.
ISSRC (International Sustainable Systems Research Center). 2013. Hybrid – 
Electric Bus Test Program in Latin America Final Report. La Habra, CA: ISSRC.
Jin, L. 2020. “Preparing to Succeed: Fleet-Wide Planning Is Key in the 
Transition to Electric Buses.” Washington, DC: International Council on Clean 
Transportation. https://theicct.org/blog/staff/fleet-wide-planning-key-to-ebus-
transition-jul2020.
Korzhenevych, A., N. Dehnen, J. Bröcker, M. Holtkamp, H. Meier, G. Gibson, 
A. Varna, et al. 2014. Update of the Handbook on External Costs of Transport. 
Final Report for the European Commission DG MOVE. Ricardo-AEA. https://
doi.org/Ref: ED 57769 - Issue Number 1.
Kwon, S., Y. Park, J. Park, J. Kim, K. Choi, and J. Cha. 2017. “Characteristics 
of On-Road NOx Emissions from Euro 6 Light-Duty Diesel Vehicles Using a 
Portable Emissions Measurement System.” Science of the Total Environment 
576: 70–77.
Lajunen, A., and T. Lipman. 2016. “Lifecycle Cost Assessment and Carbon 
Dioxide Emissions of Diesel, Natural Gas, Hybrid Electric, Fuel Cell Hybrid 
and Electric Transit Buses.” Energy 106: 329–42.
Lammert, M. 2008. Long Beach Transit: Two-Year Evaluation of Gasoline-
Electric Hybrid Transit Buses. Golden, CO: National Renewable Energy 
Laboratory.
Li, J., and B. Yang. 2020. “Quantifying the Effects of Vehicle Technical 
Performance and Electricity Carbon Intensity on Greenhouse Gas Emissions 
from Electric Light Truck: A Case Study of China.” Atmospheric Pollution 
Research 11 (8): 1290–1302. https://doi.org/10.1016/j.apr.2020.05.001.
Liu, Z., Y. Ge, K.C. Johnson, A. Naeem, J. Tan, C. Wang, and L. Yu. 2011. 
“Real-World Operation Conditions and On-Road Emissions of Beijing Diesel 
Buses Measured by Using Portable Emission Measurement System and 
Electric Low-Pressure Impactor.” Science of the Total Environment 409 (8): 
1476–80. https://doi.org/10.1016/j.scitotenv.2010.12.042.
Lopez, H. 2008. “The Social Discount Rate: Estimates for Nine Latin American 
Countries.” World Bank.
Matzer, C., K. Weller, M. Dippold, S. Lipp, M. Röck, M. Rexeis, and S. 
Hausberger. 2019. Update of Emission Factors for HBEFA Version 4.1. Graz, 
Austria: Graz University of Technology (TU Graz).
Mccaffery, C., H. Zhu, C. Li, T.D. Durbin, K.C. Johnson, H. Jung, R. Brezny, 
et al. 2020. “On-Road Gaseous and Particulate Emissions from GDI Vehicles 
with and without Gasoline Particulate Fi lters (GPFs) Using Portable 
Emissions Measurement Systems (PEMS).” Science of the Total Environment 
710: 136366.
Merkisz, J., P. Fuc, P. Lijewski, and J. Pielecha. 2016. “Actual Emissions from 
Urban Buses Powered with Diesel and Gas Engines.” Transportation Research 
Procedia 14: 3070–78.
MEE (Ministry of Ecology and Environment, China). 2012. “Regulation on 
Compulsory Disposal Standards of Vehicles.” (In Chinese.)
MEE. 2015. “Technical Guidelines for Establishment of Air Pollutant Emission 
Inventory of Road Motor Vehicles (Trial).” (In Chinese.) https://www.mee.gov.
cn/gkml/hbb/bgg/201501/W020150107594587831090.pdf.
MFC (Ministry of Finance of China). 2020. “Service Purchase Information 
Platform of the Government of China.” (In Chinese.) Ministry of 
Finance of the People’s Republic of China. http://search.ccgp.gov.cn/
bxsearch?searchtype=1&page_index=16&bidSort=0&buyerName=&proj
ectId=&pinMu=0&bidType=0&dbselect=bidx&kw=公交车采购&start_
time=2019%3A01%3A01&end_time=2019%3A12%3A08&timeType=6&displ
ayZone=&zoneId=&pppStatus=0&agentName=.
MJB&A (M.J. Bradley & Associates). 2013. Comparison of Modern CNG, 
Diesel and Diesel Hybrid-Electric Transit Buses. https://mjbradley.com/sites/
default/files/CNG%20Diesel%20Hybrid%20Comparison%20FINAL%20
05nov13.pdf.
Moon-Miklaucic, C., A. Maassen, X. Li, and S. Castellanos. 2019. “Financing 
Electric and Hybrid-Electric Buses: 10 Questions City Decision-Makers 
Should Ask.” Washington, DC: World Resources Institute. https://files.wri.org/
s3fs-public/financing-electric-hybrid-electric-buses_0.pdf.
Moore, M., and A. Vining. 2018. “The Social Rate of Time Preference and the 
Social Discount Rate.” Arlington, Virginia: Mercatus Center, George Mason 
University.
NEEDS (New Energy Externalities Developments for Sustainability). 2009. 
Value Transfer Techniques and Expected Uncertainties. http://www.needs-
project.org/.
Nelder, C., and E. Rogers. 2019. Reducing EV Charging Infrastructure Costs. 
Rocky Mountain Institute. https://rmi.org/ev-charging-costs.

The Costs and Benefits Appraisal Tool for Transit Buses
TECHNICAL NOTE  |  October 2020  |  39
Neubauer, J., and E. Wood. 2014. “Thru-Life Impacts of Driver Aggression, 
Climate, Cabin Thermal Management, and Battery Thermal Management 
on Battery Electric Vehicle Utility.” Journal of Power Sources 259: 262–75. 
https://doi.org/https://doi.org/10.1016/j.jpowsour.2014.02.083.
Nicholas, M. 2019. “Estimating Electric Vehicle Charging Infrastructure Costs 
across Major U.S. Metropolitan Areas.” Working paper. Washington, DC: The 
International Council on Clean Transportation.
Ntziachristos, L., and M.C. Galassi. 2014. “Emission Factor for New and 
Upcoming Technologies in Road Transport.” Luxembourg: Publications Office 
of the European Union.
Ozbay, K., B. Bartin, O. Yanmaz-Tuzel, and J. Berechman. 2007. “Alternative 
Methods for Estimating Full Marginal Costs of Highway Transportation.” 
Transportation Research Part A: Policy and Practice 41 (8): 768–86. https://
doi.org/10.1016/j.tra.2006.12.004.
PG&E (Pacific Gas and Electric Company). 2020. “EV Savings Calculator.” 
https://ev.pge.com/.
Potkány, M., M. Hlatká, M. Debnár, and J. Hanzl. 2018. “Comparison of 
the Lifecycle Cost Structure of Electric and Diesel Buses.” Nase More 65 (4 
Special issue): 270–75. https://doi.org/10.17818/NM/2018/4SI.20.
Prakash, S., and T.A. Bodisco. 2019. “An Investigation into the Effect of Road 
Gradient and Driving Style on NOx Emissions from a Diesel Vehicle Driven on 
Urban Roads.” Transportation Research Part D: Transport and Environment 
72: 220–31.
Prohaska, R., K. Kelly, and L. Eudy. 2016. “In-Use Fleet Evaluation of Fast-
Charge Battery Electric Transit Buses.” Golden, CO: National Renewable 
Energy Laboratory. 
Rangaraju, S., L. De Vroey, M. Messagie, J. Mertens, and J. Van Mierlo. 
2015. “Impacts of Electricity Mix, Charging Profile, and Driving Behavior 
on the Emissions Performance of Battery Electric Vehicles: A Belgian Case 
Study.” Applied Energy 148 (June): 496–505. https://doi.org/10.1016/j.
apenergy.2015.01.121.
Rastani, S., T. Yüksel, and B. Çatay. 2019. “Effects of Ambient Temperature 
on the Route Planning of Electric Freight Vehicles.” Transportation Research 
Part D: Transport and Environment 74: 124–41. https://doi.org/https://doi.
org/10.1016/j.trd.2019.07.025.
Ricke, K., L. Drouet, K. Caldeira, and M. Tavoni. 2018. “Country-Level 
Social Cost of Carbon.” Nature Climate Change 8 (10): 895–900. https://doi.
org/10.1038/s41558-018-0282-y.
Roychowdhury, A. 2010. “CNG Programme in India: The Future Challenges.” 
Fact Sheet Series. New Delhi: Centre for Science and Environment. 
Song, Q., Z. Wang, Y. Wu, J. Li, D. Yu, H. Duan, and W. Yuan. 2018. “Could 
Urban Electric Public Bus Really Reduce the GHG Emissions: A Case Study in 
Macau?” Journal of Cleaner Production 172 (January): 2133–42. https://doi.
org/10.1016/j.jclepro.2017.11.206.
Song, S. 2017. Transport Emissions & Social Cost Assessment: Methodology 
Guide. Washignton, DC: World Resources Institute. https://www.wri.org/
publication/transport-emissions-social-cost-assessment-methodology-guide.
Song, S. 2018. “Assessment of Transport Emissions Impact and the 
Associated Social Cost for Chengdu, China.” International Journal of 
Sustainable Transportation 12 (2): 128–39. https://doi.org/10.1080/1556831
8.2017.1337833.
Sustainable Bus. 2020. “Electric Bus, Main Fleets and Projects around the 
World.” https://www.sustainable-bus.com/electric-bus/electric-bus-public-
transport-main-fleets-projects-around-world/.
Tao, X., P. Wang, and B. Zhu. 2016. “Measuring the Interprovincial CO2 
Emissions Considering Electric Power Dispatching in China: From Production 
and Consumption Perspectives.” Sustainability (Switzerland) 8 (6). https://doi.
org/10.3390/su8060506.
Tietge, U., S. Dias, Z. Yang, and P. Mock. 2017. From Laboratory to Road 
International: A Comparison of Official and Real-World Fuel Consumption and 
CO2 Values for Passenger Cars in Europe, the United States, China, and Japan. 
White Paper. Washington, DC: International Council on Clean Transportation. 
https://theicct.org/publications/laboratory-road-intl.
Todd, J., J. Chen, and F. Clogston. 2013. “Creating the Clean Energy 
Economy: Analysis of the Electric Vehicle Industry.” Washington, DC: 
International Economic Development Council.
Trading Economics. 2020a. “Bank Lending Rate.” 2020.
Trading Economics. 2020b. “Interest Rate.” 2020.
TST (The Santiago Times). 2018. “Chile Drives into the Future with Largest 
Electric Bus Fleet in Latin America,” December 13. https://santiagotimes.
cl/2018/12/13/chile-drives-into-future-with-largest-electric-bus-fleet-in-latin-
america/.
Urban Bus Toolkit. 2006. “Kilometers per Vehicle per Day (KPVPD).” 
The World Bank Group and PPIAF. https://ppiaf.org/sites/ppiaf.org/files/
documents/toolkits/UrbanBusToolkit/assets/1/1c/1c11.html.
USDOT (U.S. Department of Transportation). 2016. “Department of the Interior 
— Bus and Ferry Lifecycle Cost Modeling.” 2016. https://www.volpe.dot.
gov/transportation-planning/public-lands/department-interior-bus-and-ferry-
lifecycle-cost-modeling.
USDOT. 2020. “Bus Lifecycle Cost Model.” https://www.volpe.dot.gov/
transportation-planning/public-lands/bus-lifecycle-cost-model.
van Essen, H., L. van Wijngaarden, A. Schroten, D. Sutter, C. Bieler, S. Maffii, 
M. Brambilla, et al. 2019. “Handbook on the External Costs of Transport: 
Version 2019.” Delft, Netherlands: European Commission. https://doi.
org/10.2832/27212.
Wappelhorst, S. 2020. “The End of the Road? An Overview of Combustion-
Engine Car Phase-Out Announcements across Europe.” Briefing. Washington, 
DC: International Council on Clean Transportation. https://theicct.org/
sites/default/files/publications/Combustion-engine-phase-out-briefing-
may11.2020.pdf.

40  |  
Weiss, M., P. Bonnel, J. Kühlwein, A. Provenza, U. Lambrecht, S. Alessandrini, 
M. Carriero, et al. 2012. “Will Euro 6 Reduce the NOx Emissions of New Diesel 
Cars? Insights from On-Road Tests with Portable Emissions Measurement 
Systems (PEMS).” Atmospheric Environment 62 (2): 657–65.
World Bank. 2017. “GDP per Capita, PPP (Current International $).” Data. 
https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.CD?year_high_
desc=true.
World Bank and IHME (Institute for Health Metrics and Evaluation). 2016. 
The Cost of Air Pollution: Strengthening the Economic Case for Action. 
Washington, DC: World Bank. https://doi.org/10.1080/000368497326688.
Wu, X., J. Du, and C. Hu. 2013. “Energy Efficiency and Fuel Economy Analysis 
of a Series Hybrid Electric Bus in Different Chinese City Driving Cycles.” 
International Journal of Smart Home 7 (5): 353–68. https://doi.org/10.14257/
ijsh.2013.7.5.34.
Wu, X., S. Zhang, Y. Wu, Z. Li, Y. Zhou, L. Fu, and J. Hao. 2015. “Real-World 
Emissions and Fuel Consumption of Diesel Buses and Trucks in Macao: From 
On-Road Measurement to Policy Implications.” Atmospheric Environment 120 
(November): 393–403. https://doi.org/10.1016/j.atmosenv.2015.09.015.
Wu, Y., S.J. Zhang, M.L. Li, Y.S. Ge, J.W. Shu, Y. Zhou, Y.Y. Xu, et al. 2012. 
“The Challenge to NOx Emission Control for Heavy-Duty Diesel Vehicles in 
China.” Atmospheric Chemistry and Physics 12 (19): 9365–79. https://doi.
org/10.5194/acp-12-9365-2012.
Xue, L., W. Wei, L. Peng, and L. Daizong. 2019. “Overcoming the Operational 
Challenges of Electric Buses: Lessons Learnt from China,” 1–40. Beijing: 
World Resources Institute China. (In Chinese.) http://www.wri.org.cn/
Overcoming_the_operational_challenges_of_electric_buses%3A lessons_
learnt_from_China_CN.
Yang, L., S. Zhang, Y. Wu, Q. Chen, T. Niu, X. Huang, S. Zhang, L. Zhang, Y. 
Zhou, and J. Hao. 2016. “Evaluating Real-World CO2 and NOx Emissions for 
Public Transit Buses Using a Remote Wireless On-Board Diagnostic (OBD) 
Approach.” Environmental Pollution 218 (November): 453–62. https://doi.
org/10.1016/j.envpol.2016.07.025.
Yao, Z., X. Shen, Y. Ye, X. Cao, and X. Jiang. 2015. “On-Road Emission 
Characteristics of VOCs from Light-Duty Gasoline Vehicles in Beijing, 
China.” Atmospheric Environment 103: 87–93. https://doi.org/10.1016/j.
atmosenv.2015.06.019.
Yue, T., F. Chai, J. Hu, M. Jia, X. Bao, Z. Li, L. He, et al. 2016. “Gaseous 
Emissions from Compressed Natural Gas Buses in Urban Road and Highway 
Tests in China.” Journal of Environmental Sciences (China) 48 (October): 
193–99. https://doi.org/10.1016/j.jes.2016.01.028.
Yuksel, T., and J.J. Michalek. 2015. “Effects of Regional Temperature on 
Electric Vehicle Efficiency, Range, and Emissions in the United States.” 
Environmental Science & Technology 49 (6): 3974–80. https://doi.
org/10.1021/es505621s.
ZEBRA (Zero Emission Bus Resource Alliance). 2019. “Technology and 
Financing Options to Deploy Zero-Emission Fleets in the Public Transport 
Bus System (TPC) in Medellín.” Medellín Business Roundtable Summary. 
Presentation. 
Zhang, L., X. Hu, R. Qiu, and J. Lin. 2019. “Comparison of Real-World 
Emissions of LDGVs of Different Vehicle Emission Standards on Both 
Mountainous and Level Roads in China.” Transportation Research Part D: 
Transport and Environment 69 (January): 24–39.
Zhang, S., Y. Wu, J. Hu, R. Huang, Y. Zhou, X. Bao, L. Fu, et al. 2014a. 
“Can Euro V Heavy-Duty Diesel Engines, Diesel Hybrid and Alternative Fuel 
Technologies Mitigate NOx Emissions? New Evidence from On-Road Tests 
of Buses in China.” Applied Energy 132 (November): 118–26. https://doi.
org/10.1016/j.apenergy.2014.07.008.
Zhang, S., Y. Wu, H. Liu, R. Huang, L. Yang, Z. Li, Lixin Fu, et al. 2014b. 
“Real-World Fuel Consumption and CO2 Emissions of Urban Public Buses 
in Beijing.” Applied Energy 113: 1645–55. https://doi.org/10.1016/j.
apenergy.2013.09.017.
Zhang, S., Y. Wu, X. Wu, M. Li, Y. Ge, B. Liang, Y. Xu, et al. 2014c. “Historic 
and Future Trends of Vehicle Emissions in Beijing, 1998–2020: A Policy 
Assessment for the Most Stringent Vehicle Emission Control Program 
in China.” Atmospheric Environment 89 (June): 216–29. https://doi.
org/10.1016/j.atmosenv.2013.12.002.
Zhou, B., Y. Wu, B. Zhou, R. Wang, W. Ke, S. Zhang, and J. Hao. 2016. “Real-
World Performance of Battery Electric Buses and Their Life-Cycle Benefits 
with Respect to Energy Consumption and Carbon Dioxide Emissions.” Energy 
96: 603–13. https://doi.org/10.1016/j.energy.2015.12.041.

The Costs and Benefits Appraisal Tool for Transit Buses
TECHNICAL NOTE  |  October 2020  |  41
ACKNOWLEDGMENTS 
This tool and research were supported by the FedEx-WRI Mobility and 
Accessibility Program. We are pleased to acknowledge our institutional strategic 
partners, who provide core funding to WRI: Netherlands Ministry of Foreign 
Affairs, Royal Danish Ministry of Foreign Affairs, and Swedish International 
Development Cooperation. 
The authors are grateful to peer reviewers Carlos Muñoz Piña (WRI), Ayushi 
Trivedi (WRI), Eduardo Henrique Siqueira (WRI), Lulu Xue (WRI), Mengpin 
Ge (WRI), Muhamad Rizki (WRI), Sergio Avelleda (WRI), Elizabeth Connelly 
(International Energy Agency), Lanzhi Qin (Innovation Center for Energy 
and Transportation), Nikola Medimorec (The Partnership on Sustainable, 
Low Carbon Transport), and Tim Dallmann (International Council on Clean 
Transportation), who provided insightful suggestions to improve the data inputs, 
tool layouts, and technical note. The authors thank Benjamin Welle and Adam 
Davidson for their administrative support of the project. They also thank Emily 
Matthews, Emilia Suarez, Romain Warnault, and Sarah DeLucia for their valuable 
assistance with the publication and editorial process and Ye Zhang for support 
with graphics, design, and layout.
ABOUT THE AUTHORS 
Xiangyi Li is a research associate in the Ross Center for Sustainable Cities 
program at WRI China. Contact: xiangyi.li@wri.org
Jun Gao is a research consultant with WRI China and a graduate student at 
Oxford University. 
Su Song is a research associate at WRI China.

42  |  
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
