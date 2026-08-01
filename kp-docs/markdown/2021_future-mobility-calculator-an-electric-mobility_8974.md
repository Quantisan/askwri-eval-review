---
doc_id: 2021_future-mobility-calculator-an-electric-mobility_8974
source_pdf: kp-docs/askwri-kps/2021_future-mobility-calculator-an-electric-mobility_8974.pdf
extraction_method: cache-plaintext
char_count: 106772
title: "Future Mobility Calculator: An electric mobility infrastructure tool"
authors: Kothari, Vishant; Sclar, Ryan; Jackson, Eleanor; Werthmann, Emmett; Orbea, Jone
date_published: 3/30/2021
article_type: Technical Note
sub_tag: Transport decarbonization
wri_primary_office: WRI Global
wri_programs: Cities
language: English
url: "https://urbantransitions.global/en/publication/future-mobility-calculator-an-electric-mobility-infrastructure-tool/"
doi: No DOI listed
summary: The Future Mobility Calculator (FMC) is an Excel-based tool designed to assess the infrastructure needs and costs associated with electric vehicle (EV) adoption in urban settings. By inputting city-specific data and projected electrification scenarios for 2035 and 2050, users can estimate the quantity of charging stations required, electricity demand, and potential emissions reductions. The tool emphasizes the importance of tailored planning for EV infrastructure to enhance resource management and political support for electrification initiatives. Ultimately, the FMC aids city planners and policymakers in making informed decisions regarding sustainable urban mobility and energy systems.
---

# Future Mobility Calculator: An electric mobility infrastructure tool

1 
 
Future Mobility Calculator: 
An electric mobility infrastructure assessment  
tool technical note 
 
 
Vishant Kothari, Ryan Sclar, Eleanor Jackson, Emmett Werthmann and Jone 
Orbea

2 
 
 
Contents 
1 Introduction................................................................................................................................................................... 5 
1.1 Background ........................................................................................................................................................... 5 
1.2 Tool Overview ...................................................................................................................................................... 5 
1.3 Tool Structure ...................................................................................................................................................... 6 
2 Tool Methodology & Configuration .................................................................................................................. 12 
2.1 Tool Configuration .......................................................................................................................................... 12 
2.2 Data Input and Calculation Sheets ........................................................................................................... 14 
2.2 Results .................................................................................................................................................................. 49 
3 Conclusion ................................................................................................................................................................... 52 
Annex................................................................................................................................................................................. 53 
Annex 1 ........................................................................................................................................................................ 53 
Annex 2 ........................................................................................................................................................................ 56 
Bibliography ................................................................................................................................................................... 59 
Acknowledgements ..................................................................................................................................................... 63 
About the authors ........................................................................................................................................................ 63 
 
Figures and tables 
Figure 1. General view of the FMC structure and informational flow ..................................................... 7 
Figure 2. Screenshot of the Initial Data Entry tab, where users input basic city information and 
define a city typology. ................................................................................................................................................... 8 
Figure 3. Visual breakdown of the inputs included in the Data Input tabs ........................................ 10 
Figure 4. Visual breakdown of the results included in the FMC .............................................................. 10 
Figure 5. Screenshot of the City Data tab, where users input general city information ............... 14 
Figure 6. Screenshot of the Mobility Data tab, where users input general city information. ..... 16 
Figure 7. Mobility calculations use information from the City Input and Mobility Input tabs .. 20 
Figure 8. Screenshot of the Charging Infrastructure Data tab, where users input general city 
information. .................................................................................................................................................................... 25 
Figure 9. Electric Infrastructure Calculations use input data from City Input and Electric 
Infrastructure Input sheets and outputs from the Mobility Calculations sheet. .............................. 28 
Figure 10. Screenshot of the Cost Data tab, where users input cost information for the city.... 31

3 
 
Figure 11. Cost Calculations use input data from Mobility Input, Electric Infrastructure Input, 
and Cost Input. .............................................................................................................................................................. 34 
Figure 12. Emissions Calculations use input data from City Input and Mobility Input. ............... 42 
Figure 13: Benefit Data sheet, showing the emission social cost factors used in the tool. .......... 46 
Figure 14. Benefits Calculations use input data from City Input, Mobility Input and Benefits 
Input sheets. ................................................................................................................................................................... 47 
Figure 15. Screenshot of the Infrastructure & Emissions Results tab, showing demonstration 
results. Source: WRI .................................................................................................................................................... 50 
Table 1. A breakdown of all tabs included in the FMC.................................................................................... 8 
Table 2. The percentage of low or zero carbon electricity generation associated with each 
electricity mix type included in the FMC. .......................................................................................................... 16 
 
Table 3 – Battery size ranges allow users to input costs that vary by battery size and vehicle 
modes. ............................................................................................................................................................................... 32 
Table A1.-Intervals of the main city type variables. Source: Elaborated by WRI with data from 
UN Habitat and World bank Data. ........................................................................................................................ 53 
Table A2.- Urban population density and GDP per capita of selected cities Source: World Bank 
national accounts data, and OECD National Accounts data files. ............................................................ 55 
Table A3. Vehicle pollutant emission Source: Victoria Transport Policy Institute (2018) ......... 56

4 
 
Abstract 
Mass e lectrification within the transport sector presents a n opportunity  to simultaneously 
reduce tailpipe emissions  by switching propulsion technolo gies and to improve the electrical 
grid. Fully realizing the potential that electric vehicles (EV) offer requires a robust roadmap for 
infrastructure development and investment to ensure deployment  is cost effective and 
resource efficient. To help quantify the infrastructure and investment needed for EV adoption 
for urban passenger mobility and its associated benefits , this paper introduces the  Future 
Mobility Calculator (FMC). Developed by WRI and Siemens in collaboration with the Coalition 
for Urban Transitions, t he FMC is an Excel -based tool that —for a given ra nge of city -specific 
inputs and a projected rate of  transport electrification—identifies the quantity and cost of 
infrastructure required for EV adoption through 2050. The tool also estimates the potential 
social benefits associated with a reduction in emi ssions that would result from electrification 
and modal shifts.  The FMC does not  provide a comparative cost -benefit analysis  between 
scenarios but is rather designed to estimate impacts of a designated EV uptake scenario 
developed by the user given a set of inputs and assumptions. The FMC is intended to be used by 
modelers to support  city planners, transit agencies , city policy makers , utilities, and charge 
point operators. The FMC aims to help cities make informed decisions and plan accordingly for 
the future of their mobility and energy systems.  This technical note details the structure, 
methodology and assumptions (listed separately under each section) of the FMC. 
Abbreviations and Acronyms 
 EV = Battery electric vehicle 
 PHEV = Plug-in hybrid electric vehicle 
 ICE = Internal combustion engine 
 VKT = Vehicle kilometers traveled  
 LDV = Light duty vehicle 
 HDV = Heavy duty vehicle

5 
 
1 Introduction 
1.1 Background  
As urban centers continue to grow, so will the share of global emissions they produce linked to 
an expanding transport sector and increased electricity consumption. In 2019, transportation 
accounted for 24 percent of global CO2 emissions (IEA 2020)  and is the fastest growing 
emissions sector (Wang and Ge 2019), with road vehicles accounting for nearly three-quarters 
of all transport CO2 emissions. Electrification within the transport sector presents a solution to 
help mitigate potential emissions associated with the  growth of cities by reducing tailpipe 
emissions and improving grid functionality and sustainability through smart charging.  
While the promise of EVs for emissions reductions and reduced operational costs are attractive, 
uptake of the technology at scale will require the development of a robust  vehicle adoption 
pathway and charging infrastructure network. To help facilitate planning, this paper introduces 
the Future Mobility Calculator (FMC). Developed by WRI and Siemens in collaboration with the 
Coalition for Urban Transitions, the FMC  focuses on the urban infrastructure needed for 
successful EV and charging station rollout and the costs and social benefits associated with that 
investment. Understanding the appropriate quantity and type of charging stations to install, the 
increased ele ctricity demand from EVs, and the cost (and social benefits)  of vehicle and 
infrastructure deployment are crucial for effective resource management, decision making, and 
building political support for electrification . The FMC aims to help cities make infor med 
decisions and plan accordingly for the future of their mobility and energy systems. 
The term "EVs" can refer to few different vehicle technologies including battery EVs (fully 
electric), plug-in hybrid EVs (battery and petrol), and fuel cell vehicles ( hydrogen fuel). While 
plug-in hybrid and fuel cell vehicles are an important part of the shift to sustainable transport, 
the FMC considers the adoption of battery EVs only, any reference to "EV" or "EVs" in this paper 
refers exclusively to fully electric battery EVs. 
1.2 Tool Overview  
The FMC is an Excel-based tool that, for a given range of city-specific inputs (general city data, 
mobility data, charging infrastructure data, and cost data) and a projected electric transport 
uptake scenario for 2035 and 2050, identifies the quantity and cost of infrastructure required. 
It also quantifies some of emissions benefits that would result  from an investment in electric 
transport infrastructure, based on input data and listed assumptions . The FMC is not intended 
to provide a direct comparative cost -benefit analysis against other propulsion technologies 
such as diesel, hydrogen or CNG. These types of comparisons are addressed in other literature 
and tools (UChicago Argonne, LLC 2019; Cooper et al. 2019a). Instead, the main purpose of the 
tool is to estimate the costs, requirements, and  some of the  key benefits of defined 
electrification scenarios, which are needed to effectively plan for future EV use.  
The FMC is designed to provide a city -specific analysis, informed by the city-specific inputs  
entered by the user. When user inputs are not available, the tool provides def aults. These 
defaults vary based on the typology of the city, but they represent broad and generic 
estimations. The less default inputs that are needed, the more the calculator outputs will reflect 
the reality of the city.  Likewise, the user should take ca re to match the geographic scope of all

6 
 
data. Users are encouraged to manually enter as many city-specific inputs as they are able and 
to avoid mixing with regional data to the extent possible. 
The FMC is designed to accommodate inputs for four modes of mo torized transit: private car, 
private two-wheeler, public bus, and shared fleet vehicle.  This tool is designed for fully battery 
electric vehicles and not for plug -in hybrid electric vehicles (PHEVs) or hydrogen fuel cell 
vehicles. Users may include PHEVs  in their total EV count, but the vehicle specifications 
included in the tool are tailored to the attributes of battery electric vehicles.  Since the tool is 
designed specifically to plan for electric vehicles (and not to p rovide guidance on other topics 
related to general mobility planning), the tool does not analyze non-motorized transportation. 
The user designates a desired future transport electrification scenario for the years 2035 and 
2050. 
The FMC incorporates a transparent interface allowing the user to view inputs and calculations 
as well as integrate their own data , allowing complete customization for the city in question.  
The tool is open-sourced, and users can change any desired default assumptions, in addition to 
the suggested city -specific inputs . For example, the user can change  the default emission 
factors, default assumption for battery efficiency loss in hot or cold climates,  or any other 
default assumption in the tool.  
When city -specific data is not available , the tool is programmed with over 500 default data 
points, which help fill gaps in the user’s data. These default inputs are sourced from work done 
by a range of institutions including the IPCC, World Bank, C40, IEA, IRENA, US EPA, UNEP, and 
ICCT among ot hers. Inputs are based on p resent day and projected values as well as 
assumptions inferred based on trends.  Based on the city’s population density and economy, 
these default inputs are sourced from four pre-loaded city typologies: (1) emerging economy – 
high density, (2) developed economy – low density, (3) developed economy – high density, and 
(4) emerging economy – low density. While no planning tool can provide complete scenarios 
with absolute certainty, the FMC uses these different city typologies to source specific default 
inputs which are intended to be most applicable to the city in question.  
The FMC is specifically designed to conduct city-level analysis, but the geographic extent of the 
city’s analysis can be modified depending on how the user defines a city’s limits in the inputs. 
Using the city-specific inputs entered by the user in conjunction wi th default inputs, the tool 
estimates the emission reductions, number of necessary EV purchases, electricity consumption, 
and required number and type of EV charging stations.  
1.3 Tool Structure  
The FMC is an excel-based tool developed around three primary operational sections: 
 Data input tabs: Initial Data Input, city, mobility, charging, and cost.  
 Calculation tabs: Mobility, charging, cost, emissions, and benefits. 
 Results tabs: Results and Yearly Selected Costs-Benefits 
The general informational flow within the tab is broken down visually in Figure 1. Building on 
basic city information  from Initial Data Input , user inputs  in the remaining data  input tabs 
combined with default data are used in Calculation tabs to produce outcomes in the Results. A 
complete list of the tabs included in the FMC is shown in Table 1.

7 
 
Figure 1. General view of the FMC structure and informational flow 
 
Note: Figure 1 d epicts each of the different tool sections: Data Input, Calculation and Results. Starting with basic city 
information collected in Initial Data Entry, user inputs from Data Input tabs combined with Default Data  feed into 
Calculation tabs. The calculated outcomes are disp layed in Results tabs. This figure does not depict every tab included 
in the FMC, please see Table 1 for a complete list. Source: WRI 
Tab Type Tab Name 
Information 
tabs 
Start 
Overview 
Glossary 
Sources 
Tool 
configuration 
tabs  
Initial Data Entry 
User Typology Selection 
 Tool Section 
City Mobility Charging Cost Emissions Benefits 
Data input tabs City 
Data 
Mobility 
Data 
Charging 
Data Cost Data   
Default input 
tabs 
City 
Default 
Mobility 
Default 
Charging 
Default Cost Default  Benefits Default 
Calculation 
tabs  
Mobility 
Calc 
Charging 
Calc 
Cost Calc 
Cost Calc 1 -Vehicle 
Uptake 
Cost Calc 2 -Vehicle 
Investment 
Cost Calc 3 -Vehcile 
Maintenance 
Emissions 
Calc 
Benefits Calc 
Benefits Calc 1 -
Emissions

8 
 
Table 1. A breakdown of all tabs included in the FMC 
 
Note: Tabs are divided by Tab Type  and Tab Name. Data input, Default input, and Calculation 
tabs are further separated by the Tool Section they are associated with. Note that some sections 
of the tool such as Emissions, only have a Calculation tab , where inputs  for those calculations 
are sourced from other sections of the tool.  Similarly, the City  section does not have a 
calculation tab, where City inputs feed into other calculation sheets , but the City section does 
not have a calculation tab of its own. Source: WRI 
1.3.1 Main Configuration 
 Figure 2. Screenshot of the Initial Data Entry tab, where users input basic city information and define a city typology.   
 
 
Source: WRI     
The Initial Data Entry tab gathers basic city attributes and establishes the City Typology  
associated with the city under analysis. For information on how these typologies were chosen, 
see Annex 1. The selected City Typology will inform the Default Inputs used throughout the tool. 
Inputs for Initial Data Entry can be seen in Figure 2. Current and future electricity generation is 
designated as moderate, low-carbon, or dirty, depending on the mix of  electricity generation 
sources input by the user. The ranges for these three categories are defined in Table 2. This tab 
also includes an option to indicate if your city experiences temperature extremes , which can 
impact battery performance.   
1.3.2 Data Input and Calculation 
Data Input tabs are where the user enters the bulk of the city’s data used in the tool. Associated 
with e ach Data Input tab is a Default Data tab, which houses the City Typo logy default 
information. The inputs for each of the Data Input tabs are listed visually in Figure 3. Given that 
the FMC is a long-term planning tool, the inputs for the default data tab should reference overall 
Cost Calc 4 -Charger 
Uptake 
Cost Calc 5 -Charger 
Monetization 
Cost Calc 6-Electricity 
Results tabs Results 
Yearly Selected Costs and Benefits

9 
 
trends over the long-term. Short- and medium-term influences, such as the impact of COVID-19 
or other topical issues, are not intended to be reflected by this tool. 
Calculation tabs utilize the values from Data Input tabs to draw out relationships in the data 
and produce tool outputs.  Outputs from one Calculation tab are often utilized in another 
Calculation tab to help produce results.

10 
 
Figure 3. Visual breakdown of the inputs included in the Data Input tabs 
 
 
Note: Input definitions and their utility within the tool are detailed in the Methodology. Source: 
WRI 
 
1.3.3 Results Tabs 
Results tabs display the outputs produced with in the Calculation tabs. The outputs for each of 
the Results tabs are listed visually in Figure 4. 
Figure 4. Visual breakdown of the results included in the FMC 
 
Note: Results and associated calculations are described in the Methodology section. Source: WRI

11 
 
1.3.4 Limitations 
Although the FMC provides a robust calculation framework, it faces some limitations: 
 
• Accuracy of the outputs will significantly depend on the degree and accuracy of city-
specific inputs from the user . Default data is provided to help fill out potential gaps in 
the user’s data input and is based on comparative assumptions from existing literature.  
• Some data inputs have more weight than others. The FMC analysis is built around 
several key inputs including, population growth rate, 2020 vehicle population, modal 
split, average vehicle occupancy rate, trip length, charger power, and monetary input 
values included in the Cost Data. Users should pay particular attention to the accuracy 
of these key central inputs. 
• The term “ EVs” can refer to few different vehicle technologies including battery EVs 
(fully electric), plug-in hybrid EVs (battery and petrol), and fuel cell vehicles (hydrogen 
fuel). While plug-in hybrid and fuel cell vehicles are an important part of the shift to 
sustainable transport, t he FMC considers the adoption of battery EVs only, any 
reference to “EV” or “EVs” in this paper refers exclusively to fully electric battery EVs. 
• The FMC uses 2020 as a baseline year for analysis. Short- and medium-term influences, 
such as the impact of COVID-19 or other topical issues, are not intended to be reflected 
by this tool. 
• The FMC produces estimates of the quantity and cost of infrastructure associated with 
EV uptake scenarios built by the user. These estimates can be used to compare different 
EV uptake scenarios. The outcomes produced in different scenarios are not intended to 
show which outcomes are more or less likely to occur.  
• In all annual ridership calculations, the authors assume the  default number of days as 
365.  
• The tool is not intended to help cities decide which propulsion systems would be best 
for their fleets. These types of comparisons are addressed in other literature and tools, 
including recent work produced by WRI  (Cooper et al. 2019a) . Rather, this tool 
is designed to provide estimates of the energy and infrastructure needs for a given 
electrification scenario and an analysis of the associated costs and some social benefits.  
• The emission factors estimations in this tool are related only to tailpipe and e lectricity 
generation, as the ones coming from suspended material due to vehicle operation, such 
as vehicle braking and tire friction, are not considered in this version of the FMC. 
• In its analysis the FMC focuses on  a limited number of transport modes including 
private cars, private two-wheelers, shared fleets (cars), and public buses and rail. 
• In terms of electricity generation, when users define their future electricity generation 
mix, the FMC does not account for the infrastructure requirements and costs associated 
with increasing the share of renewable generation on the grid. When calculating the 
daily electricity load the grid will experience from EV adoption, the tool  it is assumed 
the charging load will be distributed equally over the course of the day (24 hours). The 
location and duration of EV charging occurring during the day is a major determinant 
of the upgrades which will be required (or could be offset) to power distribution and 
generation infrastructure. The tool also does not consider smart charging or any 
vehicle-to-grid integration, which will likely impact the use of charging ports.

12 
 
• The social benefits included in the tool do not measure or account for the value of time 
of residents in the city. 
• While the costs associated with health impacts are incorporated into the social cost 
values linked to pollutants in the tool, t here are several health and social impacts 
associated with air pollution (such as organ damage and lower reproductive rates) that 
the tool does not currently capture. 
• This tool does not include scenarios for electrifying trucks  and urban goods 
transportation.  
• The tool also does not consider how new technologies such as autonomous vehicles 
would impact the electrification process. 
• When the authors refer to ‘modal split’, they refer only the split between motorised 
options only.   
2 Tool Methodology & Configuration  
2.1 Tool Configuration  
Tool configuration and establishing the City Type occur within the Initial Data Entry tab. This 
section will describe the different city typologies and other parameters that calibrate the FMC 
to determine which default inputs will be used to fill in unknown data. For information on how 
these typologies were chosen, see Annex 1. For more reliable results, it is highly recommended 
that users input city-specific information (cells in yellow) about the city being analyzed instead 
of relying on default data.  
2.1.1 City Configuration (Input sheet—Initial Data Entry tab) 
This is the main configuration tab where users define and determine key attributes of the city 
under analysis. User inputs and selections in this tab will impact assumptions and calculations 
throughout the tool, to best reflect the city under analysis. There are four key selections that 
are impacted by this:  
 City Typology Selection  – Based on inputs for population density  and income per 
capita, the tool will determine the most appropriate City Type and associated default 
inputs for the city (see Annex 1 for definition of City Types) . The City Type can also be 
manually selected by the user. 
 Projected electricity generation mix – This informs the user whether the electricity 
generation in their city will be considered dirty, moderate, or low-carbon based on user 
assumptions made for the city’s projected low-carbon electricity generation. Please 
refer to City Section (below)  for benchmarking default data assumptions. For reliable 
results, it is preferred to have city-specific inputs from the user based on the city being 
analyzed. This information will likely be made available by local utility companies or at 
the system operator level (regional or national, especially for future projections). 
 Island State – This determines whether the city is on an isolated island or not. We have 
defined an isolated island as one which needs to import most of its electricity. This 
impacts electricity infrastructure and transmission costs. 
 Environmental Factor  – Determines if a city’s climate will have an impact on EV 
performance. Users may select if their city is considered hot (summer monthly average 
above 35C during the hottest month of the summer) and/or cold (monthly average

13 
 
below -6C during the coldest month of the winter) (Motoaki, Yi, and Salisbury 2018; 
Hawkins 2019) . If these attributes are present in a city, the too l will account for its 
impacts on additional battery use for climate control within the vehicle and impacts on 
battery performance.

14 
 
2.2 Data Input and Calculation Sheets 
2.2.1 City 
This section  comprises of the variables that depend on the physical, social and economic 
characteristics of the city. While the City Data tab does not correspond to “City Calculations,” as 
is the case with other tabs, these inputs are used throughout all of the calculations and are key 
inputs for the emissions and benefits calculations . It is dedicated to a range of  city attributes 
and variables related to population and land use, electricity consumption mix,  health 
information, electricity generation, and mobili ty emissions factors. While default inputs are 
present in the tool (based on assumptions listed below), a s shown in Figure 5, city-specific 
inputs entered in the yellow cells for each attribute are preferred.  
Figure 5. Screenshot of the City Data tab, where users input general city information 
 
Note: The data sheet includes cells for both city-specific user input (preferred) and pre-loaded 
default inputs based on the previously designated city typology. Source: WRI

15 
 
Input (Data input sheet - ‘City Data’) 
 
 Population (number of people): This contains the population of the city in 2020.  
 Average annual population growth rate, today-2050 (percentage): The average rate 
at which the population grows every year. This percentage is sensitive , and the user 
input will have a significant impact on results.  
 Population Density (residents/km2): The density is based on the number of residents 
within the defined municipal area of the city . This is an input from the “Initial Data 
Input.” 
 Emissions per capita  (MTCO2/year): The annual regional median per capita  
emissions, BASIC, GHG emissions from stationary electricity, transportation and waste 
(“C40 : Greenhouse Gas Protocol for Cities Interactive Dashboard” n.d.) 
 Electricity mix (percentage of electric ity generated in M Wh from each source) : The 
electricity mix of the grid currently available in the selected city and expected or desired 
mix in the future . The final results will vary d epending on whether the user inputs 
expected or desired mix.  
 Electricity generation emission s (kg/MWh per each generation source) : List of 
emission factors for electricity generation pollutants - CO2, PM 10, and NO x emissions 
based on fuel type. 
 ICE vehicles emission factors; (kg/km): List of emission factors for ICE combustion 
engine pollutants - CO2 PM10, and NOx emissions based on vehicle mode. 
City General Default Input Assumptions (Default input – ‘City Default’) 
 
 Population: The default average annual population growth rate from 2020 -2050 is 
2.3% for emerging economies and 0.5% for developed economie s based on (United 
Nations, Department of Economic and Social Affairs, and Population Division 2019) 
 Average annual population growth rate, today-2050 (percentage): The average rate 
at which the population grows every year. These rates are based on the World 
Urbanization Prospects 2018 projections that incorporate data from 1950 and project 
out to 2050 (United Nations 2019). 
 Population Density (residents/km2): The density is based on the number of residents 
within the defined municipal area of the city. This is an input from the “Initial Data 
Input.” 
 Climate information: By default, “Hot” is considered above 35C (95F) while “Cold” is 
considered below -6C (20F).  
 Emission per capita: Based on the city location, the default regional median per capita 
emissions per year is sourced from (“C40 : Greenhouse Gas Protocol for Cities 
Interactive Dashboard” n.d.) 
 Electricity mix : The city is  categorized as Dirty, Moderate , or Low-Carbon based on 
current and projected electricity mix data input from the user. It is assumed that the 
electricity on the grid will get cleaner with time. The tool provides analysis of different 
potential future scenarios, not business as usual projections.

16 
 
Table 2. The percentage of low or zero carbon electricity generation associated with each electricity mix type included 
in the FMC. 
 
 
 
Source: Authors assumption, estimated based on (Kennedy, Stewart, and Westphal 2019)  
 Electricity generation emissions : The default Emission factors for coal, natural gas , 
and oil are sourced from IPCC 2006 Emission Fact ors, (Mawdsley et al., n.d.)  and 
(Comission for Environmental Cooperation 2015) . These are global averages. By 
default, the electricity generation emission factors only consider in-site generation and 
not life-cycle value. It is assumed that the following electricity generation types have 
zero pollutant emission factors: Solar, Wind, Hydro and Nuclear. 
 ICE vehicles emission factors : The default emission factors by pollutant and vehicle 
type are sourced from (Yang and Bandivadekar, n.d.) , (UNEP 2018) , (Song 2017) , 
(Victoria Transport Policy Institute 2018) , and (Cooper et al. 2019b) . All shared fleet 
vehicles are assumed to have the same emission factors as private cars.   
2.2.2 Mobility 
In this section the user is provided with the ability to explore different future scenarios  by 
defining future modal split and EV up take into 2035 and 2050.  For the year 2020 , tool users 
input the total number of vehicles (ICE and EV) operating in the city; these inputs used to define 
the city’s average daily VKT and the projected vehicle populations in the city for 2035 and 2050.  
Within the tool there are five vehicle modes considered:  
 Private cars: owned and used by private residents or households. 
 Private two -wheelers: privately owned and operated motorized two -wheeled 
vehicles, does not include human-powered bicycles. 
 Shared fleets: owned by businesses or cities (public)  and used for taxi services, on -
demand rides, ridesharing, or car rentals. In the FMC, shared fleets are classified as cars. 
Generally, they are the same size as private cars, but with higher utilization rates. 
 Public buses: part of the city public transit system  
 Rail: includes subway, light rail, tram, cable-car, regional train, etc. 
Figure 6. Screenshot of the Mobility Data tab, where users input general city information.  
The data sheet includes cells for both city-specific user input (preferred) and pre-loaded default 
inputs based on the previously designated city typology. Source: WRI 
Electricity Mix 2020 2035 2050 
Dirty 12% 29% 55% 
Moderate 25% 55% 85% 
Low-Carbon 65% 95% 100%

17 
 
 
Mobility Input (Data input sheet - ‘Mobility Data’; Default information – ‘Mobility Default’)  
 
 Modal split , 2035 and 2050  (% motorized vehicle utilization  by mode ): The 
breakdown of travel between different modes including private cars, public buses, 
shared fleets, and rail. While modal split can be measured in a variety of ways (such as 
vehicle distance traveled, passenger distance traveled, or number of trips for the years 
2035 and 2050), in this tool we calculate  modal split by the percentage breakdown of 
commuters’ predominant (i.e., longest distance)  mode. For 2020 , the modal split is 
calculated based on the total number of vehicles input by the user, and by the ridership 
information provided by the user for public transportation . User input  can have a 
significant impact on the vehicle numbers in the future. Users should keep  modal split 
measurements the same across all sources.  
 Total ICE vehicles 2020  (no. of  vehicles): For each mode, the total number of 
registered ICE vehicles operating within a city for 2020. If possible, this input should be 
sourced from vehicle registrations. This is NOT the total number of vehicles in a city. If 
using a value that is the total number of vehicles in a city, please subtract  out the  
number of EVs  in the city.  Additionally, ple ase ensure shared vehicles, taxis and 
transportation network company (TNC) vehicles, are counted separately from the total 
number of total private vehicles. As with EVs, TNCs will likely need to be subtracted 
from the total number of registered vehicles gi ven that they are not registered 
separately. Despite the fact that many TNC drivers operate on multiple platforms, all 
TNC vehicle numbers should be counted as individual drivers  because it is not public 
knowledge which drivers have dual -registrations. Almost all calculations are based off 
registered vehicle numbers in some way, so users should be careful when inputting 
these numbers. For private vehicles, if available, user can input only the number of ICE 
vehicles which are used on a daily basis  (not all of the registered vehicles), if they (1) 
also input this information for EVs, and (2)  use an average occupancy per vehicle (see 
below) which only includes vehicles used daily.

18 
 
 Total EVs 2020  (no. of vehicles): For each mode,  the total number of registered EVs 
(fully battery electric vehicles) operating in a city for 2020. This input should be sourced 
from vehicle registrations. This tool is designed for fully battery electric ve hicles and 
not for plug-in hybrid electric vehicles (PHEVs).  For private vehicles, i f available, user 
can input only the number of  EVs which are used on a daily basis (not all of the 
registered vehicles), if they (1) also input this information for ICE vehicles, and (2) use 
an average occupancy per vehicle (see below) which only includes vehicles used daily. 
 Uptake of EVs , 2035 and 2050  (% EVs): For each mode, the p ercentage of total 
vehicles targeted to be electric in a city  for the years 2035 and 2050 . These numbers 
are based on the goals put forward by the city. For 2020, this value is already calculated 
from the values input for “Total ICE vehicles 2020” and “Total EVs 2020.” 
 Average trip length (km/trip): For all modes excluding public bus and rail, the average 
distance traveled per trip taken by a vehicle. For buses, this is average trip length. The 
average trip length will have a significant impact on the charging infrastructure outputs.  
 Average number of trips  per day per vehicle (trips/day): For all modes excluding 
public bus and rail, the average quantity of trips taken per day  per vehicle. These data 
are commonly collected in household travel surveys. 
 Average occupancy per registered vehicle  (passengers/vehicle): For all modes 
excluding public bus and rail , the average number of users in a vehicle. This number 
includes the average across all registered vehicles, including those which are not used 
daily. This number is a standard metric of shared mobility vehicles. For private cars and 
two-wheelers, this number can be estimated by taking the average occupancy for a 
vehicle on the road (a metric commonly kept by cities) and reducing it by the percentage 
of vehicles which are not used for everyday travel (this can be estimated based on the 
percentage of households with 3 or more vehicles, which is a common metric recorded 
in household travel surveys). Alternatively, users can also input the average occupancy 
per vehicle on the road, if they input the number of vehicles used daily above (as 
opposed to inputting the total number of registered vehicles above). This number is 
highly sensitive. Changing occupancy from 1 pa ssenger to 2 passengers can cut the 
number of total vehicles in half.   
 Average l ifespan of ICE vehicles  (years): For all modes excluding rail , the average 
vehicle lifespan of an ICE vehicle.  
 Average l ifespan of e -vehicles (years): For all modes excluding rail , the average 
vehicle lifespan of an EV. 
 Public bus a nnual vehicle revenue kilometers , 2020  (km): For public buses only. 
This information is typically provided in annual reports from the local transit agency. If 
a region has several agencies,  use information from an aggregated source (preferred, 
such as from a regional planning entity) or from  the largest agency in the region  (if 
necessary). Ideally, this information would represent just revenue miles traveled, but 
total VKT will suffice. This information may be given on a per -bus basis; if so, use that 
information to calculate the total annual VKT for all buses together. 
 Public bus and rail annual ridership, 2020 (no. of riders): For both public buses and 
rail, the annual ridership numbers on that transit system. This information is typically 
provided in annual reports from the local transit agency. If a region has several agencies, 
use information from an aggregated source (preferred, such as from a regional planning

19 
 
entity) or from the largest agency in the region (if necessary).  Ideally this information 
will include linked trips as one rider, but unlinked trip data will suffice as well. 
 Average annual population growth rate, today-2050 (%): From City Input. 
Mobility Default Input Assumptions 
 Modal split, 2035 and 2050 : The default modal split for 2035 and 2050 is 
automatically filled in with the same modal split that is calculated in 2020 based on the 
vehicle numbers. If users want to change their modal split, they will need to  manually 
input their own projections. If mode split is manually entered, it should be broken down 
by the predominant mode (i.e., the mode used for the longest distance) for each user of 
multimodal trips. 
 Uptake of EVs, 2035 and 2050: The default uptake of EVs is based on U.S. market share 
indications from the Edison Electric Institute’s EV Sales 2019 report and mode share 
projections from the IEA’s 2018 Global EV Outlook report (Edison Electric Institute 
2019; IEA 2018) 
 Average trip length : By default , EVs and ICE vehicles have the same unit distance 
traveled, and they are the only two types of engines (for simplification purposes). While 
EV drivers have been found to travel less miles than ICE drivers, it assumed that ICE 
vehicles and EVs have the same average trip length and number of trips per day and the 
same VKT for each mode (Boston and Werthman 2016). For shared fleets, the default 
trip length only accounts for distance traveled with a passenger in the vehicle. 
Deadheading, drivers traveling without passengers, is not taken into account.  
 Average number of trips per day per vehicle: The average number of trips per day is 
calculated based on the CURB database from (The World Bank 2016). Private cars and 
private two-wheelers are assumed to have the same number of trips per day. Literature 
reveals that the number of trips taken by an individual correlates with economic activity 
(Blumenberg et al. 2012; Litman 2020) . Therefore, the number of trips is assumed 
higher in developed economies than in emergin g economies.  Determining t he 
difference between high-income and low-income trips per day is an imperfect science, 
and a simple binary variable is used between these two income levels, based on author’s 
assumptions. Literature is inconsistent on whether future trends will dictate more or 
less trips per person. Therefore, t he average number of trips are expected to remain 
constant between the different years. 
 Average occupancy per registered vehicle : In general, shared fleets ha ve higher 
occupancy rates than private vehicles (UNEP 2018; Schaller 2018) . Private cars are 
assumed to have lower occupancy  than other modes  (UNEP 2018; Schaller 2018) . 
Private vehicle occupancy is based on national data in the US, which is then reduced by 
24% to account for all registered vehicles (not just occupancy of vehicles on the road. 
The 24% reduction is based on the 24% of US households that have three or more 
vehicles (Center for Sustainable Systems 2019) . The default inputs do not change 
overtime.  
 Average lifespan of ICE vehicles: The default average lifespan for all modes does not 
change over time  or by economy type. The average lifespans come from the following 
reports: IAEE Report 2014, Nationwide Insurance 2017, US DoT.

20 
 
 Average lifespan of e -vehicles: The default average lifespan for all modes does not 
change over time. The average lifespans come from the following reports: (US DOE n.d.), 
BYD Warranty, UNEP 2018. 
 Public bus annual vehicle revenue kilometers, 2020: No default alternative listed in the 
tool. 
 Public bus and rail annual ridership, 2020: No default alternative listed in the tool. 
Figure 7. Mobility calculations use information from the City Input and Mobility Input tabs 
 
Note: Outputs produced in the Mobility Calculations sheet are used in all other FMC calculation 
sheets.

21 
 
Mobility Calculations (Calculation sheet - ‘Mobility Calc’) 
 
1. Number of vehicles per mode (V) 
Number of vehicles per mode will be a required input for each mode for 2020, but the tool will 
calculate these figures for 2035 and 2050 . Also, not all private cars and private two-wheelers 
are expected to be used every day , so a utilization factor will be applied to these modes to 
calculate their use in 2020. 
a. Number of vehicles per mode in 2020 
a. For all modes: These data are required inputs. 
b.  Number of vehicles per mode in 2035 and 2050 
a. For private cars, private two-wheelers, and shared fleets: 
𝑈𝑠𝑒𝑟𝑠𝑚
𝐴𝑣𝑒𝑟𝑎𝑔𝑒 𝑂𝑐𝑐𝑢𝑝𝑎𝑛𝑐𝑦 𝑝𝑒𝑟 𝑅𝑒𝑔𝑖𝑠𝑡𝑒𝑟𝑒𝑑 𝑉𝑒ℎ𝑖𝑐𝑙𝑒𝑚
=  𝑽𝒎   
b. For public bus and rail: 
𝑈𝑠𝑒𝑟𝑠𝑚
𝑈𝑇𝑉𝑚
=  𝑽𝒎   
Variables: 
o m = vehicle mode (private car, private two -wheeler, shared fleet, public bus, 
rail) 
o Users = people traveling daily per mode (calculations provided below) 
o UTV = Users per transit vehicle (calculations provided below) 
 
2. Number of EVs and Number of ICE vehicles (EVm, ICEm) 
•  
a. For 2020: These values are input by the user. 
b. For 2035 and 2050: 
c. Number EVs: 
𝑉𝑚  % 𝑢𝑝𝑡𝑎𝑘𝑒 𝑜𝑓 𝐸𝑉𝑠𝑚 =  𝑬𝑽𝑚 
d. Number ICE vehicles: 
𝑉𝑚 −  𝐸𝑉𝑚 = 𝑰𝑪𝑬𝒎 
Variables 
o m = vehicle mode (private car, private two -wheeler, shared fleet, public bus, 
rail) 
o V = Number of vehicles per mode 
 
3. Number of users per mode (Users) 
Users for each transportation mode is used to  calculate and/or incorporate mode-split 
information.

22 
 
a. Numbers of users per mode for 2020: 
a. Total: 
∑ 𝑈𝑠𝑒𝑟𝑠
𝑚
=  𝑼𝒔𝒆𝒓𝒔𝒕𝒐𝒕𝒂𝒍 
b. For private cars, private two-wheelers, and shared fleets: 
𝑉𝑚 ⦁  𝐴𝑣𝑒𝑟𝑎𝑔𝑒 𝑂𝑐𝑐𝑢𝑝𝑎𝑛𝑐𝑦 𝑝𝑒𝑟 𝑅𝑒𝑔𝑖𝑠𝑡𝑒𝑟𝑒𝑑 𝑉𝑒ℎ𝑖𝑐𝑙𝑒 𝑚 =  𝑼𝒔𝒆𝒓𝒔𝒎 
c. For public bus and rail: 
𝐴𝑛𝑛𝑢𝑎𝑙 𝑅𝑖𝑑𝑒𝑟𝑠ℎ𝑖𝑝𝑚
365 𝑑𝑎𝑦𝑠 ⦁ 2 𝑟𝑖𝑑𝑒𝑠 𝑝𝑒𝑟 𝑢𝑠𝑒𝑟 𝑝𝑒𝑟 𝑑𝑎𝑦 =  𝑼𝒔𝒆𝒓𝒔𝒎   
 
d. Number of riders per mode for 2035 and 2050: 
i. Total: 
𝑈𝑠𝑒𝑟𝑠𝑡𝑜𝑡𝑎𝑙,2020 ⦁  (1 +  𝐴𝑛𝑛𝑢𝑎𝑙 𝑃𝑜𝑝𝑢𝑙𝑎𝑡𝑖𝑜𝑛 𝐺𝑟𝑜𝑤𝑡ℎ 𝑅𝑎𝑡𝑒)^ 𝑛𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑦𝑒𝑎𝑟𝑠 =  𝑼𝒔𝒆𝒓𝒔𝒕𝒐𝒕𝒂𝒍 
ii. For each mode:  
 
𝑈𝑠𝑒𝑟𝑠𝑡𝑜𝑡𝑎𝑙 ⦁  𝑀𝑜𝑑𝑒 𝑆𝑝𝑙𝑖𝑡𝑚 =  𝑼𝒔𝒆𝒓𝒔𝒎   
Variables: 
o m = vehicle mode (private car, private two -wheeler, shared fleet, public bus, 
rail) 
o V = Number of active vehicles per mode 
 
4. Number of users per transit vehicle (UTV) 
The number of riders per transit vehicle is used to calculate the number of transit vehicles in in 
2035 and 2050. These numbers are calculated based on 2020 input data. 
a. Numbers of users per transit vehicle (applies only for bus and rail): 
• 
𝐴𝑛𝑛𝑢𝑎𝑙 𝑅𝑖𝑑𝑒𝑟𝑠ℎ𝑖𝑝𝑚
𝑉𝑚 ⦁  365 ⦁  2 𝑟𝑖𝑑𝑒𝑠 𝑝𝑒𝑟 𝑢𝑠𝑒𝑟 =  𝑼𝑻𝑽𝒎   
Variables: 
o m = vehicle mode (only applies here to bus, rail) 
o V = Number of active vehicles per mode 
 
5. Vehicle Kilometers Traveled per Day (VKT) 
•  
a. Total:

23 
 
∑ 𝑉𝐾𝑇
𝑚
=  𝑽𝑲𝑻𝒕𝒐𝒕𝒂𝒍 
b. For private cars, private two-wheelers, and shared fleets: 
𝑉𝑚 ⦁  𝐴𝑣𝑒𝑟𝑎𝑔𝑒 𝑁𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑇𝑟𝑖𝑝𝑠𝑚 ⦁ 𝐴𝑣𝑒𝑟𝑎𝑔𝑒 𝑇𝑟𝑖𝑝 𝐿𝑒𝑛𝑔𝑡ℎ𝑚 =  𝑽𝑲𝑻𝒎 
c. For public bus (VKT for rail is not calculated): 
𝑉𝑚 ⦁ 𝐾𝑃𝑉𝑚   =  𝑽𝑲𝑻𝒎 
 𝐴𝑛𝑛𝑢𝑎𝑙 𝑅𝑒𝑣𝑒𝑛𝑢𝑒 𝐾𝑖𝑙𝑜𝑚𝑒𝑡𝑒𝑟𝑠 𝑝𝑒𝑟 𝑇𝑟𝑎𝑛𝑠𝑖𝑡 𝑆𝑦𝑠𝑡𝑒𝑚𝑚
365 ⦁ 𝑉𝑚,2020 =  𝑲𝑷𝑽𝒎 
Variables: 
o m = vehicle mode (private car, private two -wheeler, shared fleet, public bus, 
rail) 
o V = Number of vehicles per mode 
o KPV = Kilometers per bus per day 
o VKT = Daily Vehicle Kilometers Traveled 
Mobility Outputs 
 
 Total ICE vehicles per mode 2035 and 2050.  
 Total EVs per mode 2035 and 2050.  
 Total distance travelled by ICE and EVs per vehicle mode all years.  
 Growth rate required of vehicle electrification per mode to achieve the designated EV 
uptake percentage.

24 
 
2.2.3 Charging Infrastructure 
Electricity consumption calculation and estimation are an important component for calculating 
a city’s  charging infrastructure requirements and the emissions associated with vehicle 
electricity use. For electricity usage , two main variables  are considered : 1) VKT and 2)  an 
environmental factor which adjusts that estimate by considering average temperature s of the 
city, which can impact battery efficiency.  
The FMC assumes that EV operators can charge at four different location types:  
 Home: residential charging setting 
 Work: charging located at a place of employment 
 Public: charging locations accessible for public use 
 Depot: charging locations for fleets, most commonly not accessible to the public 
The FMC assumes that there are six different charger types that EVs can use to charge.  This is 
broken down between LDVs and HDVs, each vehicle class is associated with three charger types. 
Charger power values (kW) listed below should be used as reference values, the terminology 
used to describe different kW  ranges can vary  by geography  (International Energy Agency 
2019). 
LDV Charging 
 Level 1: Most commonly found in home charging settings and facilitated by a wall outlet, 
either 120V or 240V depending on geography. Charging power is less than 3.7 kW.  
 Level 2: Most commonly found in public, private, and work charging settings. Charging 
power can range between 3.7 kW and 22 kW. 
 Level 3: Almost exclusively found in public or depot charging settings. Charging power 
is above 50 kW, but no greater than 400 kW. 
HDV Charging 
 Slow chargers: Most commonly found in depot settings. Charging power capabilities can 
range between 22 kW and 60 kW 
 Fast chargers:  Most commonly found in depot settings.  Charging power capabilities 
range between 125 kW and 400 kW.

25 
 
Figure 8. Screenshot of the Charging Infrastructure Data tab, where users input general city information. 
 
Note: The data sheet includes cells for both city-specific user input (preferred) and pre-loaded 
default inputs based on the previously designated city typology. Source: WRI 
Charging Infrastructure Input (Data input sheet - ‘Charging Data’) 
 Battery capacity (kWh): Average battery capacity available in the city for each vehicle 
mode in the years 2020, 2035, and 2050. 
 Battery range (km): Maximum distance each vehicle mode can travel with the battery 
size defined in the battery capacity input.  
 Charger power (kW): The average power flow (kW) each EV charger type can supply 
to a vehicle in your city under normal circumstances. This input is sensitive and has an 
impact on charger numbers.  
 Charging infrastructure li fespan (years): Number of years each charger type will 
continue to function properly assuming regular maintenance and usage habits.  
 Charger user behavior  (by mode, % charging location ): Percentage of time during a 
given day (out of 24 hours) that each mode will utilize each location to charge the 
vehicle battery. For each vehicle mode, the user behavior at each associated charging 
setting should add to 100%.  Current, expected, or desired charging behavior of EV 
owners when charging their vehicles can be applied to this variable by the user. 
 Charger utilization rate  (% charging location ): Percentage in a given day (out of 24 
hours) that a charger will be operating and plugged into a vehicle per charging location 
(home, work, public, depot charging).  
 Distribution of charging type (by location, % charger type ): The distribution of 
charging speeds type that exists  within a defined  charging location type . For each 
charging setting, the percent of each charging speed present should collectively add to

26 
 
100 percent. Current, expected or desired available charging infrastructure type/level 
by location in your city.  
 Environmental factor (percent): Percentage of operation al loss and impact to vehicle 
battery efficiencies due to presence of extreme temperatures. This is determined by the 
selection made within the tool’s “Initial Data Entry” tab. 
Charging Infrastructure Default Input Assumptions (Default information – ‘Charging Default’)  
 Battery range (km): By default,  the battery range is projected to increase over time 
based on current trends (IEA 2020). Battery range and battery capacity are assumed to 
increase at similar rates in the default settings.  
 Charger power (kW): This default input data considers various levels of charging for 
both light duty vehicles (Level1; Level 2; Level 3) and heavy -duty vehicles (Slow 
charging; Fast charging) (Nicholas, Lutsey, and Hall 2019; Proterra 2019) . Future 
projections are based on the rationale that  charging capacity is projected to increase 
over time. Therefore, it is assumed that there is a desire to access to faster chargers, so 
charging power increases over time. 
 Charging infrastructure lifespan  (years): The default  input data considers multiple 
charger settings and for relevant charging levels available within each setting (Smith 
and Castellano 2015; Chang et al. 2012).   
 Charger user behavior (by mode, % charging location): The default input data is based 
on IRENA smart charging projections and trends observed by the US DOE and ICCT (Hall 
and Lutsey 2020; US DOE n.d.; IRENA 2019) . It assumes that  vehicles are charged to 
100% each ti me they are plugged in for charging. It also assumes that, t hrough time, 
home charging for private vehicles will decrease, while work and public charging 
increase. For shared fleets, home charging is assumed to decrease through time as depot 
charging incre ases. For public buses, charging is assumed to  always take place in a 
depot given that opportunity charging is a nascent technology. 
 Charger utilization rate  (% charging location) : Based on research done on public 
charging trends and the speed of chargers, utilization rate is assumed to start at 30% of 
the day in places that serve private vehicles (home and work) . 30% is roughly 8 hours 
which corresponds to an average workday or an average night  (IRENA 2019) . The 
author assumes this percentage will decrease slightly through time (20% by 2050) for 
home charging based on (1) an increase in charger speed and (2) a n increase in public 
and depot charging, especially for shared fleets (Wolbertus, Van den Hoed, and Maase 
2016; Wolbertus et al . 2018). Electricity consumption is also assumed to  continue to 
increase with time (IEA 2019). 
 Distribution of charging type (by location, % charger type): The default percentages 
are based on the percentages of each level of charger currently a vailable globally (IEA 
2020). Future trends are based on the following: 
o Home charging for both level 1 and 2 chargers are assumed to grow in the model 
at the same rate as private vehicles (electric cars and two -wheelers) initially, 
however home charging is expected to decrease as the utilization of charging 
infrastructure in the workplace and public spaces increases (Engel et al. 2018). 
We are not assuming that buying an EV means you purchased a home charger, 
so the number of level 1 chargers will likely be lower than the number of private 
vehicles.

27 
 
o In the case of workplace chargers, level 2 chargers are expected to grow more 
rapidly at the beginning due to government incentive programs and then grow 
steadily. In parallel, level 3 chargers will grow steadily as it is primarily 
deployed in the public space due to higher installation and operational cost but 
faster cha rging speed. As volumes and infrastructure increase, the costs will 
reduce and make level 3 viable for workplace charging as well.  
o Public charging may vary depending on the city type. In cities associated with 
developed economies, as public investment inc reases, level 2 chargers will be 
replaced with level 3 chargers. In emerging economies, we can expect both 
chargers to be in place simultaneously.   
 Environmental factor (percent): By default, this factor is assumed to be 1%, meaning 
that in “hot” or “cold ” climates batteries consume 1% more energy  (Motoaki, Yi, and 
Salisbury 2018; Hawkins 2019).

28 
 
Figure 9. Electric Infrastructure Calculations use input data from City Input and Electric Infrastructure Input sheets and 
outputs from the Mobility Calculations sheet.

29 
 
Charging Infrastructure Calculations (Calculation sheet - ‘Charging Calc’) 
1. Total daily electricity demand per transit mode.  
a. Electricity used per km by vehicle mode (m): each mode’s kWh of fuel used per km. 
𝑉𝑒ℎ𝑖𝑐𝑙𝑒 𝑏𝑎𝑡𝑡𝑒𝑟𝑦 𝑐𝑎𝑝𝑎𝑐𝑡𝑖𝑡𝑦𝑚  
𝐵𝑎𝑡𝑡𝑒𝑟𝑦 𝑟𝑎𝑛𝑔𝑒𝑚
= 𝑬𝒍𝒆𝒄𝒕𝒓𝒊𝒄𝒊𝒕𝒚 𝒖𝒔𝒆𝒅 𝒑𝒆𝒓 𝒌𝒎𝒎 (𝒌𝑾𝒉/𝒌𝒎)   
b. Adjusted e lectricity used per km by vehicle mode (m), accounting for  the 
Environmental factor. 
 𝐸𝑙𝑒𝑐𝑡𝑟𝑖𝑐𝑖𝑡𝑦 𝑢𝑠𝑒𝑑 𝑝𝑒𝑟 𝑘𝑚𝑚 + (𝐸𝑙𝑒𝑐𝑡𝑟𝑖𝑐𝑖𝑡𝑦 𝑢𝑠𝑒𝑑 𝑝𝑒𝑟 𝑘𝑚 ⦁ 𝐸𝑛𝑣𝑖𝑟𝑜𝑛𝑚𝑒𝑛𝑡𝑎𝑙 𝑓𝑎𝑐𝑡𝑜𝑟𝑚)
= 𝑨𝒅𝒋𝒖𝒔𝒕𝒆𝒅 𝒆𝒍𝒆𝒄𝒕𝒓𝒊𝒄𝒊𝒕𝒚 𝒖𝒔𝒆𝒅 𝒑𝒆𝒓 𝒌𝒎𝒎 (𝒌𝑾𝒉/𝒌𝒎)   
c. Daily electricity demand, per transit mode (m).  
Total kWh needed for each mode to drive the defined daily km (Mobility Calculation) based on 
the calculated electricity used per km (Charging Infrastructure Calculation). 
𝐴𝑑𝑗𝑢𝑠𝑡𝑒𝑑 𝑒𝑙𝑒𝑐𝑡𝑟𝑖𝑐𝑖𝑡𝑦 𝑢𝑠𝑒𝑑 𝑝𝑒𝑟 𝑘𝑚𝑚 ⦁  𝑒𝑉𝐾𝑇𝑚 = 𝑬𝒍𝒆𝒄𝒕𝒓𝒊𝒄𝒊𝒕𝒚 𝒅𝒆𝒎𝒂𝒏𝒅𝒎 (𝒌𝑾𝒉/𝒅𝒂𝒚) 
Variables: 
o m = vehicle mode (private car, private two-wheeler, shared fleet, public bus) 
o eVKT = VKT of electric vehicles (Average Daily VKT from Mobility calculations) 
 
2. Chargers needed in the city.  
The quantity of  chargers by type (k) needed to support each transit mode’s calculated daily 
electricity consumption (Charging Infrastructure Calculation). The following calculation is run 
for each transit mode (m).  
a. Daily electricity demand (kWh) per transit mode (m) by charging location (j) 
  𝐸𝑙𝑒𝑐𝑡𝑟𝑖𝑐𝑖𝑡𝑦 𝑑𝑒𝑚𝑎𝑛𝑑𝑚  ⦁ 𝐶ℎ𝑎𝑟𝑔𝑒𝑟 𝑢𝑠𝑒𝑟 𝑏𝑒ℎ𝑎𝑣𝑖𝑜𝑟𝑚 (%𝑗)
= 𝑬𝒍𝒆𝒄𝒕𝒓𝒊𝒄𝒊𝒕𝒚 𝒓𝒆𝒒𝒖𝒊𝒓𝒆𝒅𝒎/𝒋 (𝒌𝑾𝒉/𝒅𝒂𝒚)  
 
b. Electricity required (kWh) per charging setting (j). 
  ∑ 𝐸𝑙𝑒𝑐𝑡𝑟𝑖𝑐𝑖𝑡𝑦 𝑟𝑒𝑞𝑢𝑖𝑟𝑒𝑑𝑗 (𝑘𝑊ℎ/𝑑𝑎𝑦)𝑚 = 𝑬𝒍𝒆𝒄𝒕𝒓𝒊𝒄𝒊𝒕𝒚 𝒓𝒆𝒒𝒖𝒊𝒓𝒆𝒅𝒋 
c. Quantity of chargers needed by type (k), per charging location (j).  
This equation assumes that for each charger type at each charging location, those sochargers 
will be used uniformly throughout the day. The number of chargers needed is a function of the 
electricity required at charging location (j) and the total power flow (kW) each charger type (k) 
present at that location can facilitate given its associated charger utilization rate , which is a 
percentage of 24 hours.

30 
 
𝐸𝑙𝑒𝑐𝑡𝑟𝑖𝑐𝑖𝑡𝑦 𝑟𝑒𝑞𝑢𝑖𝑟𝑒𝑑𝑗  ⦁ 𝐷𝑖𝑠𝑡𝑟𝑖𝑏𝑢𝑡𝑖𝑜𝑛 𝑜𝑓 𝑐ℎ𝑎𝑟𝑔𝑒𝑟 𝑡𝑦𝑝𝑒𝑗  (%𝑘)
𝐶ℎ𝑎𝑟𝑔𝑒𝑟 𝑝𝑜𝑤𝑒𝑟𝑘  ⦁ 24 ℎ𝑜𝑢𝑟𝑠 ⦁ 𝐶ℎ𝑎𝑟𝑔𝑒𝑟 𝑢𝑡𝑖𝑙𝑖𝑧𝑎𝑡𝑖𝑜𝑛 𝑟𝑎𝑡𝑒 (%𝑗) =  𝑪𝒉𝒂𝒓𝒈𝒆𝒓𝒔 𝒏𝒆𝒆𝒅𝒆𝒅𝒌 𝒋⁄  
Variables: 
o m = vehicle mode (private car, private two-wheeler, shared fleet, public bus) 
o j = location (home, work, public, depot) 
o k = charger type (LDV [Level 1, Level 2, Level 3], HDV [Slow, Fast, Overhead]) 
Charging Infrastructure Output 
 
1. Total electricity demand for all vehicle modes (m) 
∑ 𝐷𝑎𝑖𝑙𝑦 𝑒𝑙𝑒𝑐𝑡𝑟𝑖𝑐𝑖𝑡𝑦 𝑐𝑜𝑛𝑠𝑢𝑚𝑝𝑡𝑖𝑜𝑛𝑚
𝑚
 
2. Number of chargers per charger type (k) 
∑ 𝑐ℎ𝑎𝑟𝑔𝑒𝑟𝑠 𝑛𝑒𝑒𝑑𝑒𝑑𝑘
𝑗

31 
 
2.2.3 Cost 
This section is focused on estimating cost information  of vehicles and chargers, the public 
investment required for vehicle adoption and infrastructure, the cost of electricity transmission 
to the charging station and consumption. It does not include potential grid reinforcement or 
upgrade costs.  
Figure 10. Screenshot of the Cost Data tab, where users input cost information for the city. 
 
Note: The data sheet includes cells for both city-specific user input (preferred) and pre-loaded 
default inputs based on the previously designated city typology. Source: WRI  
Cost Input (Data input sheet - ‘Cost Data’)  
All cost numbers should be entered without tax. 
 Average E-Vehicle investment cost by battery size (thousand USD 2020) : Average 
cost of vehicle split by vehicle mode and battery size with ranges to customize inp ut 
from the selected city.

32 
 
Table 3 – Battery size ranges allow users to input costs that vary by battery size and vehicle modes.   
Vehicle mode Battery size range (kWh) 
Min Max 
E-Light Duty Vehicle Car 1 40 
41 75 
76 100 
101 600 
Two-wheelers 1 2.5 
2.6 7 
7.1 11 
12 20 
E-Heavy Duty Vehicle Public b uses - 
depot 
1 275 
276 400 
401 600 
601 1,000 
 
 Average cost of vehicle investment for ICE vehicles (thousand USD 2020): Average cost 
of vehicle, by vehicle mode.   
 Average E-Vehicle maintenance cost per vehicle mode per battery size (USD 2020 Cost 
per km): The average maintenance cost of each vehicle mode per battery size (same as 
Table 3).  
 Average cost of vehicle maintenance for ICE vehicles (USD 2020, Cost per km): Average 
maintenance cost of vehicle, by vehicle mode.   
 Public investment by investment asset (percentage) : Public sector investment in 
the purchase of different vehicles and infrastructure as a percentage of the total cost to 
consumers. This number has a significant impact on cost results.  
o LDV – Car 
o LDV – Shared vehicle 
o LDV – Two-wheelers 
o HDV – Public bus depot 
o Charging infrastructure 
o Electricity consumption cost 
o Electricity transmission cost 
 Electricity transmission (USD 2020 per charger) : Average total cost of electricity  
transmitted to the charging infrastructure. 
o Greenfield (thousand USD 2020 per charger) 
o Greenfield (island state) (thousand USD 2020 per charger) 
o Operation and maintenance (USD 2020 per charger) 
 Charging infrastructure cost (thousand USD 2020) : Cost of each charger type 
including installation costs.  
 Electricity consumption cost (USD 2020 per kWh) : Cost of electricity consumption. 
This number has a significant impact on the fi nal cost of electricity per vehicle class. 
Doubling the consumption will roughly double the final electricity cost for all vehicles.  
Cost Default Input Assumptions (Default information – ‘Cost Default’)

33 
 
All cost default values are in USD 2020 (based on rates in February 2020). 
 Average E-Vehicle investment cost by battery size (thousand USD 2020):  
o Default input data for cars is calculated based on estimates from EIA (2017) and 
IDB (2016). 
o Default input data for two wheelers is calculated based on estimates from Shu 
(2019); Hinton (2018); Zero Motorcycles; and Muoio (2017).  
o Default input data for buses is calculated based on estimates from  Bloomberg 
New Energy Finance (2018) and Reuters (2017). 
o In real terms, the default input values assume vehicle costs fall at 10% over a 
15-year period due to improvements in technology and increase in sales 
volume. 
o For ease of calculation, the cost of a shared fleet vehicle is assumed to be the 
same as the cost of a private car.  
 Average cost of vehicle investment for ICE vehicles (thousand USD 2020):  
o Default input data for all modes are ca lculated based on estimates from  UNEP 
(2018). 
o In real terms, the default input values assume vehicle costs fall at 10% over a 
15-year period due to improvements in technology and increase in sales 
volume. 
o For ease of calculation, the cost of a shared fleet vehicle is assumed to be the 
same as the cost of a private car.  
 Average E-Vehicle maintenance cost per vehicle mode per battery size (USD 2020 Cost 
per km):  
o Default input data for cars is calculated based on estimates from Berman (2018) 
and Edmunds (2020). 
o Default input data for two wheelers is calculat ed based on estimates from  
(UNEP 2018). 
o Default input data for buses is calculated based on estimates from Mickle, Siegel, 
and Sutton  and FTA (2018). 
o The maintenance cost per EV mode is the same, independent of the battery size.   
o Assumed decrease of 50% in EV maintenance cost in developing economies due 
to cheaper labor compared to developed economies. This is assuming the major 
portion of the maintenance cost comes from labor based on Antich (2018). 
 Average cost of vehicle maintenance for ICE vehicles (USD 2020, Cost per km):  
o Default input data  for cars and two wheelers  is calculated based on estim ates 
from Lutsey and Nicholas (2018). 
o Default input data for buses is calculated based on estimates from FTA (2018). 
 Public investment by investment asset (percentage):  
o The default values assume a 5% public investment per year for a private car in 
2020 based on information from this US Energy Information Administration 
report (EIA 2017) . The public investment in shared fleet vehicles and two -
wheelers are based on car numbers. For buses, public investment is assumed to 
be 100%.  
o Public investment for charging infrastructure includes total cost for public  
chargers and existing policy incentives for private ones (Slowik et al. 2019).

34 
 
o Public investment decreases in vehicles by 1% over a 15 -year period in 
developed economies and by 3% over a 15 -year perio d in developing 
economies as vehicles become cheaper with increased adoption and lower 
battery prices. The assumptions are based on insights in IEA (2020). 
o Public investment increases in charging infrastructure by 30% over a 30 -year 
period as charging infrastructure increases drastically to overcome barriers to 
EV adoption, especially as more expensive DC fast charging infrastructure 
increases in the public and at the workplace (through incentives and subsidies) 
(Slowik et al. 2019). 
o The public investment in shared fleets is assumed to be double of cars as it 
includes private and publicly owned fleets. Public investment in shared fleets is 
the percentage of total cost paid by public institutions to subsidize fleet 
purchase. Shared fleets are cars owned either publicly (city-owned) or privately 
(Uber, Lyft, etc.).  
 Electricity transmission (USD 2020 per charger):  
o Electricity transmission costs cover the cost of transmission and distribution 
and are a fixed cost, based on retail electricity bills.  Future cost scenarios for 
2035 and 2050  are calculated based on impacts from GDP rate increase 
(Cambridge Econometrics 2018). 
o The electricity transmission cost for islands is assumed to be 10% higher cost 
due to the isolated nature of island states and added infrastruct ure to transmit 
electricity. 
o The tool uses values estimated from Cambridge Econometrics (2018). 
o Electricity transmission costs do not consider Level 1 chargers as they are 
connected to the existing residential grid infrastructure. 
 Charging infrastructure cost (thousand USD 2020):  
o Charging station infrastructure cost decrease by 20% over a 15-year period as 
volume of infrastructure deployment increases causing manufacturing and 
installation costs to reduce. It includes cost of each charger type including 
installation costs (labor, materials, permits) (Agenbroad 2014; Bloomberg New 
Energy Finance 2018). 
 Electricity consumption cost (USD 2020 per kWh):  
o Electricity consumption prices increase at a 10% rate over a 15 -year period 
based on information EuroStat electricity prices for household consumers  
(Eurostat 2020).  
Figure 11. Cost Calculations use input data from Mobility Input, Electric Infrastructure Input, and Cost Input.

35 
 
 
Note: Information is also pulled from Mobility Calculations and Electric Infrastructure  
Calculation sheet outputs.

36 
 
Cost Calculations (Calculation sheet - ‘Cost Calc’ compiles inputs calculation sheets below) 
1. Vehicle uptake estimation (Calculation sheet - ‘Cost Calc 1 – Vehicle Uptake’) 
The desired vehicle numbers for selected years 2020, 2035 and 2050 and vehicle lifespan from 
the Mobility section are used as input to calculate number of new vehicles to be purchased per 
year per vehicle mode assuming growing technological adoption  and r etirement based on 
lifespan (for EVs only) . The calculations are split between 2020-2035 and 203 5-2050 to 
account for different adoption rates. 
Annual change of vehicles (Ai) without retirement:   
Between 2020-2035: 
𝐴𝑖𝐸𝑉𝑚 = 𝑛 ∗ (𝑡𝑜𝑡𝑎𝑙 𝐸𝑉2035,𝑚 −  𝑡𝑜𝑡𝑎𝑙 𝐸𝑉2020,𝑚
∑ 𝑛16
1
) 
𝐴𝑖𝐼𝐶𝐸𝑉𝑚 = 𝑛 ∗ (𝑡𝑜𝑡𝑎𝑙 𝐼𝐶𝐸2035,𝑚 −  𝑡𝑜𝑡𝑎𝑙 𝐼𝐶𝐸2020,𝑚
∑ 𝑛16
1
) 
 
Between 2036-2050: 
𝐴𝑖𝐸𝑉𝑚 = 𝑛 ∗ (𝑡𝑜𝑡𝑎𝑙 𝐸𝑉2050,𝑚 −  𝑡𝑜𝑡𝑎𝑙 𝐸𝑉2035,𝑚
∑ 𝑛31
17
) 
𝐴𝑖𝐼𝐶𝐸𝑉𝑚 = 𝑛 ∗ (𝑡𝑜𝑡𝑎𝑙 𝐼𝐶𝐸2035,𝑚 −  𝑡𝑜𝑡𝑎𝑙 𝐼𝐶𝐸2020,𝑚
∑ 𝑛31
17
) 
 
Retirement for Pre-2020 EV purchases 
a. Year of expiration for EVs (nex2020) 
 𝑛𝑒𝑥2020𝑚 =  2020 + 𝑣𝑒ℎ𝑖𝑐𝑙𝑒 𝑙𝑖𝑓𝑒𝑠𝑝𝑎𝑛  
b. Percentage of EVs retired each year 
   % 𝑜𝑓 𝐸𝑉 𝑟𝑒𝑡𝑖𝑟𝑒𝑑𝑚 =  1
𝐸𝑉 𝐿𝑖𝑓𝑒𝑠𝑝𝑎𝑛𝑚
 
c. Number of EVs retired  
𝑁𝑢𝑚𝑏𝑒𝑟 𝐸𝑉 𝑅𝑒𝑡𝑖𝑟𝑒𝑑𝑚 =  ∫ {𝑡𝑜𝑡𝑎𝑙 𝐸𝑉2020,𝑚 ∗ % 𝐸𝑉 𝑟𝑒𝑡𝑖𝑟𝑒𝑑𝑚}
𝑛𝑒𝑥2020
1
 
 
For EV purchase between 2020-2035 
a. Year of expiration for EVs (nex2035m) = nex2020m + vehicle lifespan 
b. Number of EVs retired = Corresponding AiEVm

37 
 
For EV purchase between 2035-2050 
a. Year of expiration for EVs (nex2050m) = nex2035m + vehicle lifespan 
b. Number of EVs retired = Corresponding AiEVm  
Total Necessary New EV purchases 
a. Necessary New EV Purchases (NEVn) = AiEVm + retired vehiclespre-2020 + retired 
vehicles2020-2035+ retired vehicles2035-2050 
Variables:  
o m = vehicle mode (private car, private two-wheeler, shared fleet, public bus) 
o n = selected year number (assuming for 2020, n=1) 
o l = vehicle lifespan 
o nex = year of expiration of EV 
o NEV = necessary new EV purchases  
o Ai = annual change of vehicles without retirement 
 
2. Growth Rate (Calculation sheet - ‘Cost Calc 1 – Vehicle Uptake’) 
 
a. 
𝑇𝑜𝑡𝑎𝑙 𝐸𝑉𝑠−𝑃𝑟𝑒𝑣𝑖𝑜𝑢𝑠 𝐸𝑉𝑠
𝑃𝑟𝑒𝑣𝑖𝑜𝑢𝑠 𝐸𝑉𝑠  𝑥 100 = 𝐺𝑟𝑜𝑤𝑡ℎ 𝑅𝑎𝑡𝑒𝑛,𝑚 
 
3. Vehicle Investment Cost (Calculation sheet - ‘Cost Calc 2 – Vehicle Investment’) 
 
a. Cost of new vehicles per year per vehicle mode (per battery size for EVs).  
The vehicle investment cost is estimated based on vehicle mode and the battery size, since the 
battery is the most important element determining the cost of a n e-vehicle. If different battery 
sizes have been enter ed in the Charging Infrastructure section, the battery size for 20 20 is 
stated only for 2020, the battery size for 2035 is applied to all the years from 2021 to 2035, and 
the battery size for 2050 is applied to all the years from 2036 to 2050.  
𝑇𝑜𝑡𝑎𝑙 𝑖𝑛𝑣𝑒𝑠𝑡𝑚𝑒𝑛𝑡 𝑐𝑜𝑠𝑡 𝑝𝑒𝑟 𝑦𝑒𝑎𝑟 (𝑇𝑁𝐸𝑉𝑖𝑛𝑣𝑒𝑠𝑡𝑛)=  ∑ 𝑁𝐸𝑉𝑛 ∗ 𝐶𝐸𝑉𝑠,𝑛
𝑚
 
𝑇𝑜𝑡𝑎𝑙 𝑖𝑛𝑣𝑒𝑠𝑡𝑚𝑒𝑛𝑡 𝑐𝑜𝑠𝑡 𝑝𝑒𝑟 𝑦𝑒𝑎𝑟 (𝑇𝐼𝐶𝐸𝑉𝑖𝑛𝑣𝑒𝑠𝑡𝑛)=  ∑ 𝑇𝐼𝐶𝐸𝑉𝑛 ∗ 𝐶𝐼𝐶𝐸𝑉𝑛
𝑚
 
b. Total public investment per year.

38 
 
It includes the total cost for public fleets (buses, city fleets) and subsidy for private vehicles 
(cars, two wheelers, shared fleets ). For default input assumptions are stated earlier in the 
section 2.2.4.  
𝑇𝑜𝑡𝑎𝑙 𝑝𝑢𝑏𝑙𝑖𝑐 𝑖𝑛𝑣𝑒𝑠𝑡𝑚𝑒𝑛𝑡 𝑝𝑒𝑟 𝑦𝑒𝑎𝑟 =  𝑇 𝑁𝐸𝑉𝑛,𝑚 ∗ 𝑃𝑢𝑏𝑖𝑛𝑣𝑒𝑠𝑡𝑚,𝑛 
Variables:  
o CEV = Cost of an EV based on battery size  
o CICEV = Cost of an ICE vehicle 
o m = vehicle mode (private car, private two-wheeler, shared fleet, public bus) 
o n = selected years 
o s = battery size (kWh) 
o Pubinvest = public investment percentage for EVs 
 
4. Vehicle Maintenance Cost (Calculation sheet - ‘Cost Calc 3 – Vehicle Maintenance’) 
•  
a. Total km traveled per year per vehicle mode and engine. Number of km traveled for 
each vehicle mode and engine from the Mobility Data section. The maintenance cost 
is estimated based on vehicle mode and the battery size, since the battery is the most 
important element determining the cost of an e-vehicle. It is suggested for the cities, 
to enter an average maintenance cost of their fleet, given that different cities may 
have different fleet compositions for each vehicle mode.  
𝐸𝑉 𝑚𝑎𝑖𝑛𝑡𝑒𝑛𝑎𝑛𝑐𝑒 𝑐𝑜𝑠𝑡 = ∑ ∑ 𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒 𝑡𝑟𝑎𝑣𝑒𝑙𝑒𝑑∗
𝑛𝑚
𝑚𝑎𝑖𝑛𝑡𝑒𝑛𝑎𝑛𝑐𝑒 𝑐𝑜𝑠𝑡𝑠 
 
𝐼𝐶𝐸 𝑚𝑎𝑖𝑛𝑡𝑒𝑛𝑎𝑛𝑐𝑒 𝑐𝑜𝑠𝑡 = ∑ ∑ 𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒 𝑡𝑟𝑎𝑣𝑒𝑙𝑒𝑑∗
𝑛𝑚
𝑚𝑎𝑖𝑛𝑡𝑒𝑛𝑎𝑛𝑐𝑒 𝑐𝑜𝑠𝑡  
Variables:  
o m = vehicle mode (private car, private two-wheeler, shared fleet, public bus) 
o n = selected years 
o s = battery size (kWh) 
 
5. Total number of charging stations (Calculation sheet - ‘Cost Calc 4 – Charger Uptake’) 
From the Charging Infrastructure section, we retrieve the total number of chargers needed per 
location per type for 2020, 2035 and 2050 , and calculate the number of chargers that need to 
be purchased per year  assuming the number of vehicles increases at a constant rate . The 
calculations are split between 2020 -2035 and 2035 -2050 to account for different adoption 
rates. 
New chargers per year (Nc) without retirement:

39 
 
Between 2020-2035: 
𝑁𝑐𝑘 = 𝑛 ∗ (𝑡𝑜𝑡𝑎𝑙 𝑐ℎ𝑎𝑟𝑔𝑒𝑟𝑠2035,𝑘 −  𝑡𝑜𝑡𝑎𝑙 𝑐ℎ𝑎𝑟𝑔𝑒𝑟𝑠2020,𝑘
∑ 𝑛16
1
) 
Between 2036-2050: 
𝑁𝑐𝑘 = 𝑛 ∗ (𝑡𝑜𝑡𝑎𝑙 𝑐ℎ𝑎𝑟𝑔𝑒𝑟𝑠2050,𝑘 −  𝑡𝑜𝑡𝑎𝑙 𝑐ℎ𝑎𝑟𝑔𝑒𝑟𝑠2035,𝑘
∑ 𝑛31
17
) 
For Pre-2020 charger purchases 
a. Year of expiration for chargers (nex2020) 
 𝑛𝑒𝑥2020𝑘 =  2020 + 𝑐ℎ𝑎𝑟𝑔𝑒𝑟 𝑙𝑖𝑓𝑒𝑠𝑝𝑎𝑛  
b. Percentage of chargers retired each year 
   % 𝑜𝑓 𝐸𝑉 𝑟𝑒𝑡𝑖𝑟𝑒𝑑𝑘 =  1
𝐶ℎ𝑎𝑟𝑔𝑒𝑟 𝐿𝑖𝑓𝑒𝑠𝑝𝑎𝑛𝑘
 
c. Number of chargers retired  
𝑁𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝐶ℎ𝑎𝑟𝑔𝑒𝑟𝑠 𝑅𝑒𝑡𝑖𝑟𝑒𝑑𝑘 =  ∫ {𝑡𝑜𝑡𝑎𝑙 𝐶ℎ𝑎𝑟𝑔𝑒𝑟𝑠2020,𝑘 ∗ % 𝐶ℎ𝑎𝑟𝑔𝑒𝑟𝑠 𝑟𝑒𝑡𝑖𝑟𝑒𝑑𝑘}
𝑛𝑒𝑥2020
1
 
For charger purchase between 2020-2035 
a. Year of expiration for chargers (nex2035k) = nex2020k + charger lifespan 
b. Number of chargers retired = Corresponding Nck  
 
For charger purchase between 2035-2050 
a. Year of expiration for chargers (nex2050k) = nex2035k + charger lifespan 
b. Number of chargers retired = Corresponding Nck  
 
Necessary New Charger Purchases (NCn) = Nck + retired chargerspre-2020 + retired             
chargers2020-2035+ retired chargers2035-2050 
 
Variables:  
o n = selected year number (assuming for 2020, n=1) 
o k = charger type (LDV [Level 1, Level 2, Level 3], HDV [Slow, Fast, Overhead]) 
o l = charger lifespan 
o nex = year of expiration for chargers  
o NC = necessary new charger purchase 
o Nc = new chargers per year without retirement

40 
 
 
6. Charger investment cost (Calculation sheet - ‘Cost Calc 5 – Charger Investment’) 
•  
a. Total cost for chargers per year 
𝑡𝑜𝑡𝑎𝑙 𝑖𝑛𝑣𝑒𝑠𝑡𝑚𝑒𝑛𝑡 𝑝𝑒𝑟 𝑦𝑒𝑎𝑟 (𝑇𝐶ℎ𝑖𝑛𝑣𝑒𝑠𝑡𝑛) =  ∑ 𝑇 𝑁𝐶ℎ𝑛 ∗ 𝐶𝑐ℎ𝑛
𝑘
 
b. Total public investment in chargers per year. This incorporates the charger’s public 
investment percentage (Pubinvest) input in this section. It includes the total cost of 
public chargers and potential subsidies offered for private ones. For additional 
details please refer to Cost Assumptions section above.   
𝑇𝑜𝑡𝑎𝑙 𝑝𝑢𝑏𝑙𝑖𝑐 𝑖𝑛𝑣𝑒𝑠𝑡𝑚𝑒𝑛𝑡 𝑝𝑒𝑟 𝑦𝑒𝑎𝑟 =  𝑇 𝑁𝐶ℎ𝑛,𝑘 ∗ 𝑃𝑢𝑏𝑖𝑛𝑣𝑒𝑠𝑡𝑘,𝑛 
Variables:  
o m = vehicle mode (private car, private two-wheeler, shared fleet, public bus) 
o n = selected years 
o k = charger type (LDV [Level 1, Level 2, Level 3], HDV [Slow, Fast, Overhead]) 
o Pubinvest = percentage of public investment for charging stations 
 
7. Electricity transmission and consumption cost (Calculation sheet - ‘Cost Calc 6 – 
Electricity’) 
•  
a. Total electricity transmission cost of the charging stat ion types  informed in this 
section, depending on if it is an island or non-island state  
𝑇 𝐶𝐸𝑙𝑒𝑐𝑡𝑟𝑎𝑛𝑠=  ∑ 𝑇 𝑁𝐶ℎ𝑚,𝑠
𝑛
∗ 𝐶𝐸𝑙𝑒𝑐𝑡𝑟𝑎𝑛𝑠 
b. Total public investment in charger’s deployment cost per year. This incorporates 
the investment percentage (Pubinvest) input in this section  
𝑇𝑜𝑡𝑎𝑙 𝑝𝑢𝑏𝑙𝑖𝑐 𝑖𝑛𝑣𝑒𝑠𝑡𝑚𝑒𝑛𝑡 𝑝𝑒𝑟 𝑦𝑒𝑎𝑟 =  𝑇 𝐶𝐸𝑙𝑒𝑡𝑟𝑎𝑛𝑠𝑛 ∗ 𝑃𝑢𝑏𝑖𝑛𝑣𝑒𝑠𝑡𝑛 
c. Total Electricity consumption per vehicle mode per year . Using the kWh/day 
variable from the Charging infrastructure section and the total EVs per vehicle mode 
from the Mobility section, we calculate the yearly electricity consumption per 
vehicle. 
𝑇𝑜𝑡𝑎𝑙 𝑒𝑛𝑒𝑟𝑔𝑦 𝑐𝑜𝑛𝑠𝑢𝑚𝑝𝑡𝑖𝑜𝑛𝑚,𝑛 =  ( 𝑡𝑜𝑡𝑎𝑙 𝑘𝑤ℎ/𝑑𝑎𝑦𝑚
𝑒𝑙𝑒𝑐𝑡𝑟𝑖𝑐 𝑣𝑒ℎ𝑖𝑐𝑙𝑒𝑚
)∗ 365 
d. Total cost of electricity consumption per year.  
𝑇𝑜𝑡𝑎𝑙 𝑒𝑛𝑒𝑟𝑔𝑦 𝑐𝑜𝑛𝑠𝑢𝑚𝑝𝑡𝑖𝑜𝑛 𝑐𝑜𝑠𝑡 =  ∑ 𝑇𝑜𝑡𝑎𝑙 𝑒𝑛𝑒𝑟𝑔𝑦 𝑐𝑜𝑛𝑠𝑢𝑚𝑝𝑡𝑖𝑜𝑛𝑚
𝑛
∗ 𝑒𝑙𝑒𝑐𝑡𝑟𝑖𝑐𝑖𝑡𝑦 𝑐𝑜𝑠𝑡

41 
 
Variables:  
o m = vehicle mode (private car, private two-wheeler, shared fleet, public bus) 
o n = selected years 
o k = charger type (LDV [Level 1, Level 2, Level 3], HDV [Slow, Fast, Overhead]) 
o s = battery size (kWh) 
Cost Output 
 Total investment in EVs (million USD 2020) per vehicle mode per year 
 Total public investment in EVs (million USD 2020) per vehicle mode per year 
 Total maintenance cost for EVs (million USD 2020) per vehicle mode per year 
 Total investment in chargers (million USD 2020) per charger type per year 
 Total public investment in chargers (million USD 2020) per charger type per year 
 Total electricity transmission cost (million USD 2020) per charger type per year 
 Total public investment in electricity  transmission cost (million USD 20 20) per 
charger type per year 
 Total electricity consumption cost (million USD 2020) per vehicle mode per year 
 Total public investment in electricity consumption cost (million USD 2020) per vehicle 
mode per year

42 
 
2.2.5 Emissions 
For the Emissions Calculations, the tailpipe emission of e-vehicles is 0. The emissions generated 
by the electricity production for charging are included. The emission factors estimations in this 
tool are related only to tailpipe and electricity generation . We do not consider emissions from 
braking and tire friction  in this version of the FMC . Additionally, the tool does not account for 
carbon produced during manufacturing.  
 
Figure 12. Emissions Calculations use input data from City Input and Mobility Input.  
Outputs produced in the Mobility Calculations and Electric Infrastructure Calculation sheets are 
also used. 
 
Emissions Inputs (Data input sheet - ‘City Data’) 
 Average vehicle trips per day: from Mobility Input 
 Average trip length: from Mobility Input 
 ICE emissions factor: from City Input 
 Total km per vehicle mode: from Mobility Calculations 2. 
 Pollutant emission for electricity generation by source: from City Input 
 EV distance travelled by vehicle mode: from Mobility Calculations 2. 
Emissions Assumptions (Default information – ‘City Default’) 
 I ICE vehicle emission factors are taken primarily from US EPA (2008) and Song 
(2017).  Because fuel economy standards (EURO I-V) do not exist in every country, they 
are not considered in this version of the FMC. The tool assumes that emission factors 
are constant over time. Users are encouraged to update the data with more 
geographically or temporally relevant data when inputting their data.  
 All low-carbon electricity sources (the tool includes wind, solar, hydro, nuclear) are 
assumed to have zero emissions for electricity generation. 
 We assume shared fleets to have the same emissions factors as private cars.

43 
 
Emissions Calculations (Calculation sheet - ‘Emissions Calc’, ‘Benefit Calc 1-Emissions’) 
1. Number of projected ICEs in a situation where the electrification rate stays at the 2020 
electrification rate.  
If all vehicles were Internal Combustion Engine (ICE) 
𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒 𝑒𝑚𝑖𝑠𝑠𝑖𝑜𝑛𝑠
= ((𝐼𝐶𝐸 𝑉𝐾𝑇𝑚,𝑛 + 𝐸𝑉 𝑉𝐾𝑇𝑚,𝑛)− ((𝐼𝐶𝐸 𝑉𝐾𝑇𝑚,𝑛
+ 𝐸𝑉 𝑉𝐾𝑇𝑚,𝑛) ×  2020 % 𝐸𝑙𝑒𝑐𝑡𝑟𝑖𝑓𝑖𝑐𝑎𝑡𝑖𝑜𝑛)))× 𝐼𝐶𝐸 𝐸𝑚𝑖𝑠𝑠𝑖𝑜𝑛 𝐹𝑎𝑐𝑡𝑜𝑟𝑝,𝑛,𝑚  
Variables:  
o m = vehicle mode (private car, private two-wheeler, shared fleet, public bus) 
o n = selected years 
o p = pollutant (CO2, PM10, NOx)  
 
2. ICE emission in the scenario  
𝑆𝑐 𝐼𝐶𝐸 =  𝑆𝑐 𝐼𝐶𝐸 𝑉𝐾𝑇 ∗  𝐼𝐶𝐸𝑝,𝑚 
Variables:  
o m = vehicle mode (private car, private two-wheeler, shared fleet, public bus) 
o p = pollutant (CO2, PM10, NOx) 
o Sc ICE VKT = The number of ICE vehicles remaining after accounting for EV uptake 
calculated based on Mobility Inputs.  
o ICEp = ICE Vehicle Emissions factor 
 
3. EV emission factor per VKT 
𝐸𝑉 𝐸𝑚𝑖𝑠𝑠𝑖𝑜𝑛 𝑓𝑎𝑐𝑡𝑜𝑟𝑓,𝑚
= ∑ 𝑒𝑙𝑒𝑐𝑡𝑟𝑖𝑐𝑖𝑡𝑦 𝑚𝑖𝑥∗ 𝑓𝑢𝑒𝑙 𝑒𝑚𝑖𝑠𝑠𝑖𝑜𝑛 𝑓𝑎𝑐𝑡𝑜𝑟𝑓,𝑚 ∗ 𝐸𝑉 𝑒𝑓𝑓𝑖𝑐𝑖𝑒𝑛𝑐𝑦𝑚,𝑛  
𝑝,𝑚
 
Variables:  
o m = vehicle mode (private car, private two-wheeler, shared fleet, public bus) 
o n = selected years 
o f = fuel source 
o p= pollutant (CO2, PM10, PM2.5, NOx) 
 
4. EVs emission in the selected scenario 
𝑆𝑐 𝐸𝑉 =  𝑆𝑐 𝐸𝑉 𝑉𝐾𝑇 𝑚,𝑛 ∗  𝐸𝑉 𝑒𝑚𝑖𝑠𝑠𝑖𝑜𝑛 𝑓𝑎𝑐𝑡𝑜𝑟 𝑓,𝑚 
Variables:

44 
 
o m = vehicle mode (private car, private two-wheeler, shared fleet, public bus) 
o n = selected years 
o Sc EV VKT = Vehicle kilometers trav elled in selected scenario of EV uptake 
calculated based on Mobility Calculations 2 
 
5. Emission change 
•  
a. 𝐴𝑛𝑛𝑢𝑎𝑙 𝑝𝑜𝑙𝑙𝑢𝑡𝑎𝑛𝑡 𝑒𝑚𝑖𝑠𝑠𝑖𝑜𝑛 𝑐ℎ𝑎𝑛𝑔𝑒𝑝 = 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒 𝑒𝑚𝑖𝑠𝑠𝑖𝑜𝑛𝑠− (𝑆𝑐 𝐼𝐶𝐸 +
𝑆𝑐 𝐸𝑉) 
b. 𝐴𝑐𝑐𝑢𝑚𝑢𝑙𝑎𝑡𝑒𝑑 𝑝𝑜𝑙𝑙𝑢𝑡𝑎𝑛𝑡 𝑒𝑚𝑖𝑠𝑠𝑖𝑜𝑛 𝑐ℎ𝑎𝑛𝑔𝑒𝑝 =
 ∑ 𝑎𝑛𝑛𝑢𝑎𝑙 𝑝𝑜𝑙𝑙𝑢𝑡𝑎𝑛𝑡 𝑒𝑚𝑖𝑠𝑠𝑖𝑜𝑛 𝑐ℎ𝑎𝑛𝑔𝑒  𝑛,𝑚  
Variables:  
o p = pollutant (CO2, PM10, PM2.5, NOx)  
o m = vehicle mode (private car, private two-wheeler, shared fleet, public bus) 
o n = selected years 
 
6. Percentage of emission change, selected years 
𝑃𝑒𝑟𝑐𝑒𝑛𝑡𝑎𝑔𝑒 𝑜𝑓 𝑎𝑛𝑛𝑢𝑎𝑙 𝑒𝑚𝑖𝑠𝑠𝑖𝑜𝑛 𝑟𝑒𝑑𝑢𝑐𝑡𝑖𝑜𝑛
= (𝑃𝑜𝑙𝑙𝑢𝑡𝑎𝑛𝑡 𝑒𝑚𝑖𝑠𝑠𝑖𝑜𝑛 𝑐ℎ𝑎𝑛𝑔𝑒
𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒 ⁄ ) ∗ 100 
7. Percentage of city CO2 emissions reduced by electrification  
𝑃𝑒𝑟𝑐𝑒𝑛𝑡𝑎𝑔𝑒 𝑜𝑓 𝑎𝑛𝑛𝑢𝑎𝑙 𝑟𝑒𝑑𝑢𝑐𝑡𝑖𝑜𝑛=
          (𝐶𝑂2 𝑒𝑚𝑖𝑠𝑠𝑖𝑜𝑛 𝑐ℎ𝑎𝑛𝑔𝑒
(𝑃𝑜𝑝𝑢𝑙𝑎𝑡𝑖𝑜𝑛 𝑛 × 𝐸𝑚𝑖𝑠𝑠𝑖𝑜𝑛𝑠 𝑝𝑒𝑟 𝑐𝑎𝑝𝑖𝑡𝑎)⁄ ) ∗ 100  
•  
o n = selected years 
 
Emissions Output 
 Total emission reduction kg/year per pollutant 
 Percentage of annual emission reduction in transportation per pollutant  
 Percentage of city CO2 emissions reduced by electrification (kg/year) 
 
 
2.2.6 Benefits 
The benefits calculations put the emissions reductions in context by quantifying the social 
costs avoided by switching to EVs. In this section, the user cannot input information directly

45 
 
and will be using the default input data to assess benefit impacts. This is done to simplify 
calculations and align data sources.  
The factors determining the “value of social cost” are complex and vary by emission type and 
source. The sources and estimations for social cost used in this tool is available in Annex 2. 
These values are subjective in nature and are only intended to provide a general estimate for 
initial planning purposes. 
 
Benefit Input (Default information – ‘Benefits Default’) 
 Emissions social cost factors (SCFs) (USD 2020/kg): the social cost of key pollutants 
(CO2, PM10, PM2.5. NOx) per kilogram emitted based on the Social Cost Factor (SCF).  
 ICE emissions factors  (kg/km): the amount of key pollutants emitted per km of 
different ICE vehicle classes.  
 EV emissions factors  (kg/km): the amount of key pollutants emitted per km of 
different EV classes. 
 Total emission reduction per pollutant  (kg/year): the total reduction of poll utants 
caused by electrifying vehicles as calculated by Emissions section.  
 Total ICE vehicles: the total number of ICE vehicles existing in a city  sourced from 
Mobility Calculations. 
 Total EVs: the total number existing in a city as calculated by Mobility Calculations. 
 Vehicle Kilometers travelled: (km/day): the number of kilometers each vehicle mode 
travels each day in a city calculated by Mobility Calculations. 
Benefits Default Input Assumptions 
 
 Emissions social cost factors (SCFs) (USD 2020/kg):  
o All SCFs come from (Victoria Transport Policy Institute 2018) and the Transport 
Emissions & Social Cost Assessment Tool  (Su 2017). (details are available in 
Annex 2)

46 
 
 Figure 13: Benefit Data sheet, showing the emission social cost factors used in the tool.  
 
  
 
Source: WRI     
 
Benefits Calculations (Calculation sheet – indicated below) 
 
 m = vehicle mode (private car, private two-wheeler, shared fleet, public bus) 
 p = pollutant (CO2, PM10, PM2.5, NOx)  
 n = selected years 
 All ICE VKT = Vehicle kilometers travelled assuming all vehicle growth is with ICE 
vehicle mode, calculated in Mobility section 
 Sc EV VKT = Vehicle kilometers travelled by EVs, calculated in Mobility section 
 Sc ICE VKT= Remaining number of ICE vehicles after EV uptake , calculated in Mobility 
section 
 ICEe = ICE Vehicle emissions factor 
 EVe = EV emissions factor  
 SCF = Emission Social Cost Factor (details available in Annex 2)

47 
 
Figure 14. Benefits Calculations use input data from City Input, Mobility Input and Benefits Input sheets.  
Outputs produced in the Mobility Calculations and Emissions Calculation sheets are also used. 
 
1. Social cost avoided (selected years) (Calculation sheet - ‘Benefits Calc 1 – Emissions’) 
The social cost avoided is calculated for each pollutant from each vehicle in 2020, 2035, and 
2050. Social costs are calculated for CO2, PM2.5, PM10, NOx. 
a. Annual emissions reductions by vehicle mode (m) and pollutant (p) 
𝐸𝑚𝑖𝑠𝑠𝑖𝑜𝑛𝑠 𝑟𝑒𝑑𝑢𝑐𝑡𝑖𝑜𝑛𝑠𝑛,𝑚,𝑝 = (𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒 𝐼𝐶𝐸 𝑉𝐾𝑇 ∗ 𝐼𝐶𝐸𝑝)− [(𝑆𝑐 𝐸𝑉 𝑉𝐾𝑇 ∗ 𝐸𝑉𝑝)+
(𝑆𝑐 𝐼𝐶𝐸 𝑉𝐾𝑇 ∗ 𝐼𝐶𝐸𝑝)] 
𝐴𝑛𝑛𝑢𝑎𝑙 𝐸𝑚𝑖𝑠𝑠𝑖𝑜𝑛𝑠 𝑟𝑒𝑑𝑢𝑐𝑡𝑖𝑜𝑛𝑠𝑛,𝑚,𝑝 = 𝐸𝑚𝑖𝑠𝑠𝑖𝑜𝑛𝑠 𝑟𝑒𝑑𝑢𝑐𝑡𝑖𝑜𝑛𝑠𝑛,𝑚,𝑝 ∗ 365  
b. Social cost avoided (selected years)  
𝑇𝑜𝑡𝑎𝑙 𝑠𝑜𝑐𝑖𝑎𝑙 𝑐𝑜𝑠𝑡 𝑎𝑣𝑜𝑖𝑑𝑒𝑑𝑝,𝑛,𝑚 = 𝐴𝑛𝑛𝑢𝑎𝑙 𝐸𝑚𝑖𝑠𝑠𝑖𝑜𝑛𝑠 𝑟𝑒𝑑𝑢𝑐𝑡𝑖𝑜𝑛𝑠𝑝,𝑚,𝑛  ∗ 𝑆𝐶𝐹𝑝 
Variables:  
o m = vehicle mode (private car, private two-wheeler, shared fleet, public bus) 
o n = selected years 
o p = pollutant (CO2, PM10, PM2.5, NOx)  
o SCFp = Emission Social Cost Factor (USD/ton of pollutant) 
o All ICE VKT= Vehicle kilometers travelled assuming all vehicle growth is with 
ICE vehicle mode, calculated based on Mobility section 
o Sc EV VKT = Vehicle kilometers travelled by EVs, calculated based on Mobility 
section 
o Sc ICE VKT= Remaining number of ICE vehicles after EV uptake, calculated 
based on Mobility section 
 
2. Social cost avoided (cumulative) (Calculation sheet - ‘Benefits Calc 1 – Emissions’)  
𝑇𝑜𝑡𝑎𝑙 𝑠𝑜𝑐𝑖𝑎𝑙 𝑐𝑜𝑠𝑡 𝑎𝑣𝑜𝑖𝑑𝑒𝑑𝑝,𝑛,𝑚 = ∑ 𝐴𝑛𝑛𝑢𝑎𝑙 𝐸𝑚𝑖𝑠𝑠𝑖𝑜𝑛𝑠 𝑟𝑒𝑑𝑢𝑐𝑡𝑖𝑜𝑛𝑠𝑝,𝑚,𝑛
𝑝
∗ 𝑆𝐶𝐹𝑝 
Variables:

48 
 
o m = vehicle mode (private car, private two-wheeler, shared fleet, public bus) 
o n = selected years 
o p = pollutant (CO2, PM10, PM2.5, NOx)  
o SCFp = Emission Social Cost Factor (USD/ton of pollutant) 
Benefits Output 
 
 Social cost avoided (USD 2020) from CO2, PM10, PM2.5, and NOx selected.  
 Social cost avoided (USD 2020) from CO2, PM10, PM2.5, and NOx accumulated.

49 
 
2.2 Results  
The results from the tool are all displayed on one results tab. Below is a list of every result 
produced by the tool.  
Costs Results:  
The cost estimation is based on the total vehicles needed to fulfill population demand in the 
given years. In terms of vehicles, it adds both internal combustion engine and EVs’ cost.  
 Total investment in EVs  (million USD 2020) per vehicle mode per year (See Cost 
Calculation 2) 
 Total public investment in EVs  (million USD 2020) per vehicle mode per year (See 
Cost Calculation 2) 
 Total maintenance cost for EVs  (million USD 2020) per vehicle  mode per year (See 
Cost Calculation 3) 
 Total chargers’ investment cost (million USD 2020) per charger type per year (See 
Cost Calculation 5) 
 Total public investment in chargers  (million USD 2020) per charger type per year 
(See Cost Calculation 5) 
 Total electricity transmission cost (million USD 2020) (See Cost Calculation 6) 
 Total public investment in electricity transmission cost (million USD 2020) (See Cost 
Calculation 6) 
 Total electricity consumption cost (million USD 2020) per vehicle mode per year (See 
Cost Calculation 6) 
 Total public investment electricity consumption cost  (million USD 2020) per 
vehicle mode per year (See Cost Calculation 6) 
Infrastructure Results:  
 Total number of EVs per vehicle mode and year (see Mobility Calculation 3) 
 Total number of internal combustion vehicles per vehicle mode and year (see Mobility 
Calculation 3) 
 Percentage of EV over the total fleet per vehicle mode and year (see Mobility Calculation 
3) 
 Growth rate of EVs over the fifteen-year period (see Cost Calculation  
 Total number of new chargers needed per charger type and year  (see Charging 
Infrastructure Calculation 2) 
 Electricity Demand in kWh per day per vehicle mode and in selected year (see Charging 
Infrastructure Calculation 1) 
 Total electricity consumption in MWh per vehicle mode and year (See Cost Calculation 
3) 
Benefits Results:  
 Social cost avoided selected (USD 2020) from CO2, PM10, PM2.5, and NOx (See Benefit 
Calculation 1) 
 Social cost avoided accumulated  (USD 2020) from CO2, PM10,  PM2.5, and NO x 
accumulated (See Benefit Calculation 2)

50 
 
 Total accumulated emission reduction kg/year per pollutant (See Emissions Calculation 
5) 
 Percentage of annual emission reduction in transportation per pollutant and year  (see 
Emissions Calculation 6) 
 Percentage of City CO2 emissions reduced by electrification, selected years  (See 
Emissions Calculation 7) 
Figure 15. Screenshot of the Infrastructure & Emissions Results tab, showing demonstration results. Source: WRI   
 
2.3.4 Yearly Selected Costs and Benefits (Results sheet—Yearly Selected Costs & 
Benefits) 
In addition to the results page, some costs and benefits are annualized on the Yearly Selecte d 
Costs and Benefits sheet.  
 Social cost avoided (million USD 2020) calculated by Benefit Calculation.  
 Vehicle cost (million USD 2020) calculated by Cost Calculation. 
 Vehicle maintenance cost (million USD 2020) calculated by Cost Calculation. 
 Charging infrastructure cost (million USD 2020) calculated by Cost Calculation. 
 Electricity consumption cost (million USD 2020) calculated by Cost Calculation. 
 Electricity transmission cost (million USD 2020) calculated by Cost Calculation.

51 
 
 Public investment in vehicles (million USD 2020) calculated by Cost Calculation. 
 Public investment in charging infrastructure (million USD 2020)  calculated by Cost 
Calculation. 
 Public investment in electricity consumption (million USD 2020)  calculated by Cost 
Calculation. 
 Public investment in electricity transmission (million USD 2020) calculated by Cost 
Calculation.

52 
 
3 Conclusion 
The FMC is designed to help cities analyze the impact of their future electrification plans. Cities 
around the world have  set ambitious goals for electrifying their vehicle fleets, but few cities 
have prudently analyzed the impacts (both positive and negative) and requirements that these 
EVs will bring.  These electrification objectives depend on evidence-based planning. Planning, 
in turn, requires solid estimates of the expected costs and benefits, such as those provided 
through the FMC.  Through the FMC, cities around the world will have a new tool to help them 
intelligently navigate their own planning processes. 
The FMC is a tool that, for a given range of city -specific inputs, estimates the costs, 
requirements, and benefits of different electrification scenarios. While these data points are 
critical for planning and gaining political support for electrification, the tool does have some 
limitations. For example, the FMC is not intended for (nor does it provide) a comparative cost-
benefit analysis against other propulsion technologies such as diesel or CNG. The tool is also 
not designed to provide guidance on what percentage of vehicle fleets should be electrified in 
future plans; rather the tool provides analysis on the costs and benefits of scenarios which are 
predefined by the user. Furthermore, like any model, the FMC is only as good as its underlying 
inputs. If users are unable to provide robust city-specific inputs, the results may not be directly 
applicable to their city. If users understand intended use of FMC, they can leverage this tool to 
quantitatively enhance EV planning in their city. 
Early iterations of this tool were tested with scenarios from Beijing, Bogota, and Delhi, and the 
authors found results to be reasonable.  
Future iterations of this tool may consider adding spatial analysis  to identify appropriate 
locations for chargers, impacts of electrifying urban freight vehicles and inclusion of non -
exhaust emissions to capture the overall emissions impact if the share of energy mix  
(renewable energy source v/s fossil-fuel based source) in the city changes.  
While the FMC is not a panacea for EV planning and analysis, it does allow cities to understand 
the real -world implications of enacting EV policies.  EV a doption is critical to help combat 
climate change and clear urban air of local pollution; however, it represents a new and daunting 
challenge. The FMC can help cities navigate these obstacles as they sail off into the uncharted 
waters of vehicle electrification.

53 
 
Annex 
Annex 1     
Integrated into the FMC are four city typologies. Each city type is linked to a set of default inputs. 
These default inputs are broad generic estimations intended to fill informational gaps in a user’s 
city-specific input data. Two primary variables were used to develop the four typologies:  
 Population density 
 GDP per capita 
Each city typology is defined by a range of values associated with these variables. The city types 
developed from this are  
(1) emerging economy – high density  
(2) developed economy – low density,  
(3) developed economy – high density, and  
(4) emerging economy – low density.  
City density is informed by population densities. GDP per capita informs whether the city is an 
emerging or developed economy. The attributes of each City Type are defined in Table A1. 
Table A1.-Intervals of the main city type variables. Source: Elaborated by WRI with data from UN Habitat and World 
bank Data.  
Criteria 
Emerging 
economy, high 
density 
Emerging 
economy, low 
density 
Developed 
economy, high 
density 
Developed 
economy, low 
density 
GDP per capita 
(USD 2020)1 693.3 - 13,221.2 13,221.2 - 24,462.3 
Population density Above 13,500 Below 13,500 Above 13,500 Below 13,500 
 
1 National GDP per capita, PPP (current international $). GDP per capita based on purchasing 
power parity (PPP). PPP GDP is gross domestic product converted to international dollars using 
purchasing power parity rate s. An international dollar has the same purchasing power over 
GDP as the U.S. dollar has in the United States. GDP at purchaser's prices is the sum of gross 
value added by all resident producers in the economy plus any product taxes and minus any 
subsidies not included in the value of the products. It is calculated without making deductions 
for depreciation of fabricated assets or for depletion and degradation of natural resources. Data 
are in current international dollars based on the 2011 ICP round.  Source: World Bank Data. 
Based on 50% percentile values. High income OECD Countries: Australia, Austria, Belgium, 
Canada, Chile, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, 
Iceland, Ireland, Israel, Italy, Japan, Korea, Latvia, Lithuania, Luxembourg, Mexico, Netherlands, 
New Zealand, Norway, Poland, Portugal, Slovak Republic, Slovenia, Spain, Sweden, Switzerland, 
Turkey, United Kingdom and United States.

54 
 
(population/km2)2 
 
  
 
2 Urban agglomeration population density (population/km²). Source: UN HABITAT http://data.unhabitat.org. Based 
on S percentile values.

55 
 
Table A2.- Urban population density and GDP per capita of selected cities Source: World Bank national accounts data, 
and OECD National Accounts data files. 
Country name City name 
Urban agglomeration 
population density 
(population/km²) 
GDP per capita, PPP 
(current international $) 
USA Phoenix 1,200 $ 59,531.66 
USA York 1,800 $ 59,531.66 
USA Georgetown 1,900 $ 8,162.60 
Finland Helsinki 2,400 $ 44,865.84 
New Zealand Auckland 2,400 $ 41,109.01 
USA Los Angeles 2,400 $ 59,531.66 
Netherlands Amsterdam 2,500 $ 52,503.27 
Belgium Brussels 2,600 $ 47,840.20 
Denmark Copenhagen 2,700 $ 51,364.14 
Malaysia Kuala Lumpur 3,400 $ 29,431.47 
Brazil Brasilia 3,600 $ 15,483.54 
Russia Moscow 3,600 $ 25,533.00 
France Paris 3,800 $ 42,850.39 
Armenia Yerevan 4,000 $ 9,647.49 
Russia St. Petersburg 4,100 $ 25,533.00 
Ghana Accra 4,200 $ 4,641.32 
Spain Barcelona 4,300 $ 37,997.85 
Japan Yokohama 4,400 $ 43,278.99 
China Beijing 5,200 $ 16,806.74 
India Chandigarh 5,300 $ 7,055.55 
UK London 5,900 $ 43,268.78 
Greece Athens 6,000 $ 27,601.90 
Thailand Bangkok 6,200 $ 17,870.52 
Burkina Faso Ouagadougou 6,300 $ 1,869.76 
Brazil Sao Paulo 6,500 $ 15,483.54 
Mexico Guadalajara 6,500 $ 18,258.10 
Tanzania Dar es Salaam 6,500 $ 2,945.88 
Central African 
Republic Bangui 7,100 $ 725.95 
Kenya Nairobi 8,000 $ 3,285.91 
Ethiopia Addis Ababa 8,300 $ 1,899.21 
Egypt Cairo 9,100 $ 11,582.59 
Rwanda Kigali 9,300 $ 2,035.65 
Indonesia Jakarta 9,600 $ 12,283.62 
Singapore Singapore 10,200 $ 93,905.42 
Nigeria Abuja 10,500 $ 5,860.85 
India Kota 12,100 $ 7,055.55

56 
 
Nigeria Lagos 13,300 $ 5,860.85 
Morocco Casablanca 14,200 $ 8,217.46 
Philippines Manila 14,800 $ 8,342.80 
Colombia Medellin 19,700 $ 14,552.01 
India Mumbai 31,700 $ 7,055.55 
Bangladesh Dhaka 44,500 $ 3,868.82 
Annex 2  
Social cost assessment 
The social cost of pollutants is the measure, in a certain currency, of the long-term damage done 
by a ton of each pollutant emissions each year. Each pollutant derived from motor vehicles 
produce different harm to the environment and human health. While some are local or regional 
impacts, in other cases the location is less important.  
Table A3. Vehicle pollutant emission Source: Victoria Transport Policy Institute (2018) 
Emission Description Sources Harmful effects Scale 
Carbon dioxide 
(CO2) 
A product of 
combustion 
Fuel production 
and tailpipe 
Climate change Global  
Fine 
particulates 
(PM10) 
Inhalable particles Tailpipe, brake 
lining, road dust, 
etc. 
Human health, 
aesthetics 
Local or 
regional 
Nitrogen oxides 
(NOx)   
Various compounds, 
some are toxics, all 
contribute to ozone 
Tailpipes Human health, 
ozone 
precursor, 
ecological 
damage 
Local or 
regional  
 
The monetary assessment of the selected pollutant does not account for the impact on health 
as this impact is separa tely evaluated in the previous section. We have selected  values from 
Victoria Transport Policy Institute 2018 (VTPI). VTPI converted original values from different 
publications to 2007 USD, adjusted based on the CPI, and the authors inflated them further to 
2020. 
Emissions 
Social Cost 
Factors  
CO2 Per 
kg 
The value of social cost for CO2eq is originally sourced by UK 
Department for Environment, Food and Rural Affairs - AEA 
Technology Environment (2005) and included in table 5.10.4 -
14 in Victoria Transport Policy Institute (2018). This number 
represents the upper bound estimate of the abovementioned 
sources, since this figure was on par with other estimates in 
other major sources (such as Downing et al. [2005] who 
indicate this figure is well within one standard deviation of the 
average estimates).  This number was converted from dollars

57 
 
 
Emission Value used in this tool $(2020) per kg 
CO2 $ 0.39 
PM10 $ 575.98 
PM2.5 $ 345.59 
NOX $ 12.83 
 
Calculations: 
Emission $ (2007) /ton   
(from sources)  
kg/to
n 
$(2007) 
/kg inflation $ (2020) /kg 
CO2 310 0.001  $ 0.31  24.6%  $ 0.39  
PM10 462265 0.001  $ 462.27  24.6%  $ 575.98  
PM2.5 277359 0.001  $ 277.36  24.6%  $ 345.59  
NOX 10293 0.001  $ 10.29  24.6%  $ 12.83  
 
per ton to dollars per kilogram and then adjusted for inflation 
to 2020 USD.  
PM10 Per 
kg 
The value of social cost for PM10 is originally sourced by 
Rowan Williams Davies and Irwin Inc (RWDI) (2006) and 
included in table 5.10.4-1 in Victoria Transport Policy Institute 
(2018). Since it is difficult to find reliable and robust sources 
for information on the value of the social cost associated with 
PM10, this figure represents a number provided for PM2.5, 
which was converted to PM10 by dividing by a conversion 
factor of 0.6, based on WHO (2014). This number was 
converted from dollars per ton to dollars per kilogram and then 
adjusted for inflation to 2020 USD.  
PM2.5 Per 
kg 
The value of social cost for PM2.5 is originally sourced by 
Rowan Williams Davies and Irwin Inc (RWDI) (2006) and 
included in table 5.10.4-1 in Victoria Transport Policy Institute 
(2018). This number was converted from dollars per ton to 
dollars per kilogr am and then adjusted for inflation to 2020 
USD.  
NOX Per 
kg 
The value of social cost for NOx is originally sourced by AEA 
Technology Environment (2005) and included in table 5.10.4-1 
in Victoria Transport Policy Institute (2018). This number was 
converted from dollars per ton to dollars per kilogram and then 
adjusted for inflation to 2020 USD.

58 
 
Assumption for Inflation 24.6% (13-year period) 
https://www.usinflationcalculator.com/ 
Another good source for users of this tool to find the input to social costs of carbon specific to 
their country is Ricke et al. 2018 . The supplementary information from their research, which 
includes data for all countries is available here: https://country-level-scc.github.io/ .

59 
 
Bibliography 
Blumenberg, Evelyn, Brian D. Taylor, Michael Smart, Kelcie Ralph, Madeline Wander, and 
Stephen Brumbagh. 2012. “What’s Youth Got to Do with It? Exploring the Travel Behavior of 
Teens and Young Adults,” September. https://escholarship.org/uc/item/9c14p6d5. 
Boston, Daniel, and Alyssa Werthman. 2016. “Plug -in Vehicle Behaviors: An Analysis of 
Charging and Driving Behavior of Ford Plug -in Electric Vehicles in the Real World.” World 
Electric Vehicle Journal 8 (4): 926–35. https://doi.org/10.3390/wevj8040926. 
“C40 : Greenhouse Gas Protocol for Cities Interactive Dashboard.” n.d. Accessed September 1, 
2020. https://www.c40.org/other/gpc-dashboard. 
Cambridge Econometrics. 2018. “Low-Carbon Cars in Spain: A Socioeconomic Assessment.” 
Center for Sustainable Systems. 2019. “Personal Transportation.” University of Michigan. 
http://css.umich.edu/sites/default/files/Personal%20Transportation_CSS01-07_e2019.pdf. 
Chang, Daniel, Daniel Erstad, Ellen Lin, Alicia Falken Rice, Chia Tzun Goh, and Tsao Angel. 2012. 
“Financial Viability Of Non -Residential Electric Vehicle Charging Stations.” UCLA Anderson. 
https://innovation.luskin.ucla.edu/wp-
content/uploads/2019/03/Financial_Viability_of_Non-Residential_EV_Charging_Stations.pdf. 
Comission for En vironmental Cooperation. 2015. “North American Black Carbon Emissions 
Estimation Guidelines.” http://www3.cec.org/islandora/en/item/11629 -north-american-
black-carbon-emissions-recommended-methods-estimating-black-en.pdf. 
Cooper, Erin, Erin Kenney, Juan Miguel Velásquez, Xiangyi Li, and Thet Hein Tun. 2019a. “Costs 
and Emissions Appraisal Tool for Transit Buses.” World Resources Institute. March 2019. 
https://www.wri.org/publication/transit-buses-tool. 
———. 2019b. “Costs and Emissions Appraisal Tool for Tran sit Buses,” March. 
https://www.wri.org/publication/transit-buses-tool. 
Edison Electric Institute. 2019. “Electric Vehicle Sales: Facts & Figures.” 
EIA. 2017. “Analysis of the Effect of Zero -Emission Vehicle Policies: State-Level Incentives and 
the California Zero -Emission Vehicle Regulations.” United States Energy Information 
Administration, September, 56. 
Engel, Hauke, Russell Hensley, Stefan Knupfer, and Shivika Sahdev. 2018. “The Basics of 
Electric-Vehicle Charging Infrastructure | McKinsey.” 201 8. 
https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/charging-
ahead-electric-vehicle-infrastructure-demand. 
Environment, U. N. 2018. “The EMob Calculator.” UNEP - UN Environment Programme. 
November 14, 2018. http://www.unenvironment. org/resources/toolkits-manuals-and-
guides/emob-calculator. 
Hall, Dale, and Nic Lutsey. 2020. “Electric Vehicle Charging Guide for Cities,” 24.

60 
 
Hawkins, Andrew J. 2019. “Extreme Weather Is Sucking the Life from Your Electric Car.” The 
Verge. February 10, 2019. https://www.theverge.com/2019/2/10/18217041/electric-car-ev-
extreme-weather-polar-vortex. 
Hinton, TJ. 2018. “2019 Vespa Elettrica.” TopSpeed. November 30, 2018. 
https://www.topspeed.com/motorcycles/motorcycle-reviews/vespa/2019-vespa-elettrica-
ar183554.html. 
IDB. 2016. “The Incorporation of Electric Cars in Latin America | Publications.” Inter-American 
Development Bank. 2016. https://publications.iadb.org/publications/english/document/The-
Incorporation-of-Electric-Cars-in-Latin-America.pdf. 
IEA. 2018. “Global EV Outlook 2018,” 139. 
———. 2019. “Electricity – World Energy Outlook 2019 – Analysis.” IEA. 2019. 
https://www.iea.org/reports/world-energy-outlook-2019/electricity. 
———. 2020. “Global EV Outlook 2020 – Analysis - IEA.” 2020. 
https://www.iea.org/reports/global-ev-outlook-2020. 
International Energy Agency. 2019. Global EV Outlook 2019: Scaling -up the Transition to 
Electric Mobility. IEA. https://doi.org/10.1787/35fb60bd-en. 
IRENA. 2019. “Innovation Outlook: Smart Charging for Electric Vehicles.” 
/Publications/2019/May/Innovation-Outlook-Smart-Charging. 2019. 
/publications/2019/May/Innovation-Outlook-Smart-Charging. 
Kennedy, Christopher, Iain D Stewart, and Michael I Westphal. 2019. “Shifting Currents: 
Oppportunities for Low-Carbon Electric Cities in the Global South.” WRI, 36. 
Litman, Todd. 2020. “Evaluating Transportation Affordability.” Victoria Transport Policy 
Institute, June. https://www.vtpi.org/affordability.pdf. 
Mawdsley, Ingrid, Tomas Wisell, Håkan Stripple, and Carina Ortiz. n.d. “SMED 2016,” 66. 
Motoaki, Yutaka, Wenqi Yi, and Shawn Salisbury. 2018. “Empirical Analysis of Electric Vehicle 
Fast Charging under Cold Temperatures.” Energy Policy 122 (November): 162 –68. 
https://doi.org/10.1016/j.enpol.2018.07.036. 
Nicholas, Michael, Nic Lutsey, and Dale Hall. 2019. “Quantifying the Electric Vehicle Charging 
Infrastructure Gap across U.S. Markets,” 39. 
Proterra. 2019. “Charging Infrastructure.” Proterra. April 9, 2019. 
https://www.proterra.com/energy-services/charging-infrastructure/. 
Schaller. 2018. “The New Automobility: Lyft, Uber and the Future of American Cities.” Schaller 
Consulting. 
Shu, Catherine. 2019. “Gogoro Launches Its Newest Electric Vehicle, a Lightweight Scooter 
Called Viva | TechCrunch.” Tech Crunch. 26 2019. 
https://techcrunch.com/2019/09/25/gogoro-launches-its-newest-electric-vehicle-a-
lightweight-scooter-called-viva/.

61 
 
Smith, Margaret, and Jonathan Castellano. 2015. “Costs Associated With Non -Residential 
Electric Vehicle Supply Equipment.” AFDC, 43. 
Song, Su. 2017. Transport Emissions  & Social Cost Assessment: Methodology Guide. 
https://www.wri.org/publication/transport-emissions-social-cost-assessment-methodology-
guide. 
Su, Song. 2017. “Transport Emissions & Social Cost Assessment: Methodology Guide.” WRI. 
2017. https://www.wri.org/pu blication/transport-emissions-social-cost-assessment-
methodology-guide. 
The World Bank. 2016. “The CURB Tool: Climate Action for Urban Sustainability.” World Bank. 
2016. https://www.worldbank.org/en/topic/urbandevelopment/brief/the -curb-tool-
climate-action-for-urban-sustainability. 
UChicago Argonne, LLC. 2019. “Argonne GREET Model.” 2019. https://greet.es.anl.gov/. 
UNEP. 2018. “The EMob Calculator.” https://www.unenvironment.org/resources/toolkits -
manuals-and-guides/emob-calculator. 
United Nations. 2019. Wo rld Urbanization Prospects: 2018  : Highlights. 
https://population.un.org/wup/Publications/Files/WUP2018-Highlights.pdf. 
United Nations, Department of Economic and Social Affairs, and Population Division. 2019. UN 
WUP 2018. 
US DOE. n.d. “Charging at Home.” Energy.Gov. Accessed August 20, 2020a. 
https://www.energy.gov/eere/electricvehicles/charging-home. 
———. n.d. “Electric Car Safety, Maintenance, and Battery Life.” Energy.Gov. Accessed July 10, 
2020b. https://www.energy.gov/eere/electricvehicles/elec tric-car-safety-maintenance-and-
battery-life. 
Victoria Transport Policy Institute. 2018. “Transportation Cost and Benefit Analysis II – Air 
Pollution Costs.” Victoria Transport Policy Institute. https://www.vtpi.org/tca/tca0510.pdf. 
Victorian Transport Pol icy Institute. 2018.  “Transportation Cost and Benefit Analysis II - Air 
Pollution Costs."  http://www.vtpi.org/tca/tca0510.pdf. 
Wang, Shiying, and Mengpin Ge. 2019. “Everything You Need to Know About the Fastest -
Growing Source of Global Emissions: Transport.” World Resources Institute. October 16, 2019. 
https://www.wri.org/blog/2019/10/everything-you-need-know-about-fastest-growing-
source-global-emissions-transport. 
Wolbertus, Rick, Maarten Kroesen, Robert van den Hoed, and Caspar Chorus. 2018. “Fully 
Charged: An Empirical Study into the Factors That Influence Connection Times at EV -Charging 
Stations.” Energy Policy 123 (December): 1–7. https://doi.org/10.1016/j.enpol.2018.08.030. 
Wolbertus, Rick, Robert Van den Hoed, and S. Maase. 2016. “Benchmarking Chargi ng 
Infrastructure Utilization.” World Electric Vehicle Journal 8 (4): 754–771. 
Yang, Zifei, and Anup Bandivadekar. n.d. “ICCT 2017,” 36.

62

63 
 
Acknowledgements 
The authors would like to thank all individuals and organisations who provided information 
and insights in preparing this tool. We would like to thank our donors, reviewers, editors, and 
the design team.  
About the authors 
1. Vishant Kothari, Manager, Electric vehicle-grid integration, Electric Mobility, WRI  
2. Ryan Sclar, Research Associate, Electric Mobility, WRI  
3. Emmett Werthmann, Research Analyst, Electric Mobility, WRI  
4. Eleanor Jackson, Research and Communications Assistant, Electric Mobility, WRI  
5. Jone Orbea, past Urban Efficiency and Climate Manager, WRI and curr ent 
Electromobility Leader, UNEP
