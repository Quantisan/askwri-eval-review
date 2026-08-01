---
doc_id: 2019_costs-and-emissions-appraisal-tool-for-transit_4706
source_pdf: kp-docs/askwri-kps/2019_costs-and-emissions-appraisal-tool-for-transit_4706.pdf
extraction_method: cache-plaintext
char_count: 56177
title: Costs and Emissions Appraisal Tool for Transit Buses (Technical Note)
authors: Cooper, Erin; Kenney, Erin; Velásquez, Juan Miguel; Li, Xiangyi; Tun, Thet Hein
date_published: 3/25/2019
article_type: Technical Note
sub_tag: Transport decarbonization
wri_primary_office: WRI Global
wri_programs: Cities
language: English
url: "https://www.wri.org/research/costs-and-emissions-appraisal-tool-transit-buses"
doi: No DOI listed
summary: The Costs and Emissions Appraisal Tool for Transit Buses enables transit agencies to evaluate the financial viability and emissions impact of different bus fleet configurations. By allowing users to compare costs and emissions of up to six bus types based on customizable inputs or default data from Brazil and the U.S., the Tool aids in identifying the most sustainable options for transitioning to cleaner fleets. Its flexibility and comparative analysis capabilities make it particularly beneficial for agencies in developing countries, facilitating informed decision-making during project scoping. Future updates aim to expand default data to better serve a wider range of locations.
---

# Costs and Emissions Appraisal Tool for Transit Buses (Technical Note)

TECHNICAL NOTE   | March 2019  |  1
TECHNICAL NOTE
COSTS AND EMISSIONS APPRAISAL TOOL  
FOR TRANSIT BUSES
ERIN COOPER, ERIN KENNEY, JUAN MIGUEL VELASQUEZ, XIANGYI LI, AND THET HEIN TUN
CONTRIBUTORS: DARIO HIDALGO, ANQI ZHAO, AND MAGDALA ARIOLI
EXECUTIVE SUMMARY 
The Costs and Emissions Appraisal Tool for Transit Buses 
(“the Tool”) is intended to help bus operators and transit 
agencies make informed decisions about alternative bus 
types during the preliminary analysis phase and to help 
them determine whether the transition to a “clean fleet” 
is financially viable and worthwhile based on expected 
emissions reductions. The Excel-based Tool allows users 
to compare the cost and emissions reductions of two bus 
fleets, each composed of up to three bus types. Bus types 
can differ in terms of fuel type, the technology used to 
achieve different emissions standards, and length. Users 
can input fuel and vehicle unit cost data for a city or 
country. If they lack these data, they can use the default 
data for Brazil and the United States included in the Tool. 
Based on either the inputted or default data, the Tool 
calculates the costs and emissions of each bus type and 
the total costs and emissions of each fleet. 
Application of the version of the Tool presented here 
should identify gaps in user needs, which the authors 
hope to address in subsequent versions. Updates will also 
expand the default cost data to include other locations in 
the developing world. 
1.  MOTIVATION 
Significant work has been conducted on vehicle emissions, 
including the development of tools that compare the costs 
and emissions of fleets in the United States (examples 
include Argonne National Laboratory’s GREET Model 
and Duke University’s Best Bus Model). However, 
CONTENTS
Executive Summary  .............................................1
1. Motivation .......................................................1
2. How to Use the Tool .......................................... 2
3. Behind the Curtain: How the Tool Works ................... 8
4. Limitations of the Tool  ...................................... 17
Appendix A ...................................................... 18
Endnotes ........................................................ 21
References ...................................................... 21
Acknowledgments..............................................22
Technical notes document the research or analytical 
methodology underpinning a publication, interactive 
application, or tool.
Suggested Citation: Cooper, E., E. Kenney, J. M. Velasquez, 
X. Li, and T. H. Tun. 2019. “Costs and Emissions Appraisal 
Tool for Transit Buses.” Technical Note. Washington, DC: 
World Resources Institute. Available online at: www.wri.org/
publication/transit-buses-tool.

2  |  
transit agencies around the world have different levels 
of knowledge of clean fleets, as well as data on their own 
fleets. International bus agencies in the Global South often 
turn to the World Resources Institute (WRI) to help them 
understand the big picture of financial feasibility and the 
tradeoffs associated with acquiring bus fleets with specific 
fuel types and engine technologies in order to achieve 
emissions reduction targets. 
The Excel-based Tool presented here provides a flexible, 
transparent platform that can quickly calculate the annual 
financial costs and emissions incurred by two different bus 
fleets. The model is particularly useful for agencies and 
operators in developing countries during the initial project 
scoping phase. It can help them shortlist alternatives and 
determine which of them deserves detailed analysis.
Three characteristics make the Tool particularly useful in 
developing countries:
 ▪ It is flexible. Users can create their own fleets, 
including and excluding different bus types to reveal 
how individual buses affect fleet costs and emissions. 
 ▪ It is comparative. Users can use the Tool to see which 
fleet performs best (or reduces costs and emissions more). 
 ▪ It can be used by agencies that lack data. Users can 
use local data (the preferred approach) or draw on  
the default cost and emissions tables (a good option 
for users that lack local data).
2.  HOW TO USE THE TOOL 
The Tool allows users to compare two bus fleets made 
up of a maximum of three bus types each. Each bus type 
is defined in terms of fuel type, engine technology, and 
bus length and has different characteristics (such as fuel 
economy) and procurement costs. For each bus type, users 
can input the number of buses, and the annual distance 
traveled by each bus type. Users may also input the down 
payment, the loan maturity period, the interest rate, and 
the discount rate, in order to better estimate costs. Users 
who lack local data can use the Tool’s default data from 
Brazil or the United States. Based on these inputs, the 
Tool estimates the annual financial costs and the volume 
of emissions for the two bus fleets as well as for the 
individual bus types.
Table 2.1 describes the Tool’s Excel sheets. (To be able to 
follow this section, readers are encouraged to download 
the Tool here.)
Figure 2.1  |   Inputs and outputs of the Tool
Fleet 1
Costs
Emissions
Fleet 2
Fuel type 
engine 
length
Fuel 
economy 
cost, etc.
INPUTS
Create up to six bus types (each bus type has 
its own operational characteristics)
Select up to three bus 
types to create each 
bus fleet (number of 
buses may vary)
Generate outputs 
for comparison, based on 
different financing 
options and operational 
conditions
OUTPUTS
Bus type 1
Bus type 2
Bus type 3
Bus type 4
Bus type 5
Bus type 6

TECHNICAL NOTE   | March 2019  |  3
Costs and Emissions Appraisal Tool for Transit Buses
Input Pages
Fuel selection page
Figure 2.2 shows a sample fuel selection page. Users can 
use the default values or input their own data. To use the 
default values, they must first select either the United 
States or Brazil (1).
Users then create up to six bus types by selecting the fuel, 
technology, and bus length (2). Green cells are cells that 
require user selections. Grey cells use data pulled from 
the default data page. 
Checking a box fills in the rows with default emissions 
and cost data based on the selected combination of fuel, 
technology, and bus length (3). These numbers can also 
be filled in manually, edited, or deleted, depending on 
analysis requirements.
Pressing the Refresh All button (4) will reset all columns 
to the defaults (or blank cells if a box is not checked).
TYPE SPREADSHEETS COMMENT
Informational sheets  
for users
 ▪ Introduction
 ▪ How to use
 ▪ Fuel selection
 ▪ Fleet inputs
 ▪ Summary table
 ▪ Summary graphs–fleet
 ▪ Summary graphs–bus type
 ▪ List of terms
Of the eight tabs, only fuel selection and fleet inputs require user input. 
Summary tables, summary graphs–fleet, and summary graphs–bus type 
present the calculation results. 
Data storage sheets  ▪ Default cost data
 ▪ Default emissions data
These sheets are protected to restrict editing.
Costs and emissions 
calculation sheets
 ▪ Capital-financial calc
 ▪ Total operating cost calc
These sheets are protected to restrict editing. They are organized by both 
fleet and bus type. All emissions calculations and some easy-to-compute 
cost calculations are presented in the summary tables.
Table 2.1  |   Description of Tool spreadsheets
Figure 2.2  |    Example of fuel selection page
(1)
(2)
(3)
(4)

4  |  
limited to, whether to include both weekday and  
weekend travel (or a weighted average of the two), 
revenue and nonrevenue hours of service, and the 
number of days in the year.
For emissions and cost data for each bus type (4), users 
simply check the boxes, which pulls the data from the 
fuel selection page. Alternatively, users can input these 
data manually, edit them, or delete them, depending 
on analysis requirements. (If the information from the 
fuel selection page is changed, users must uncheck and 
recheck the box to update the information on the fleet 
inputs page.)
Pressing the Refresh All button (5) resets all columns 
to either the defaults or blank cells (if the boxes for 
emissions and cost data are not checked).
Figure 2.3  |    Example of fleet inputs page
Fleet inputs page
To construct two bus fleets, users first select the bus types 
(1). They then enter a discount rate (2), which converts 
future costs to present values. This number varies widely 
across countries, depending on a country’s socioeconomic 
conditions. The public discount rate is 3–7 percent in 
high-income countries and 8–15 percent in the Global 
South (Zhuang et al. 2007). Private discount rates also 
range widely. Users should input their own discount 
rates, based on local conditions. They are encouraged to 
perform sensitivity analysis using different discount rates.
Users next input the number of buses and annual bus 
distance traveled for each bus type (also known as an 
average annual vehicle kilomter travelled [VKT] per bus, 
measured in km/year/bus) (3). If VKT is not available 
and needs to be estimated, users are advised to consider 
various factors that might affect it, including, but not 
(2)
(5)
(1)
(3)
(4)

TECHNICAL NOTE   | March 2019  |  5
Costs and Emissions Appraisal Tool for Transit Buses
Output Pages
Summary graphs—fleet page
On the summary graphs—fleet page, the annual cost for 
the two bus fleets is broken down into seven components: 
financing, capital (or upfront procurement), depot/
infrastructure, overhaul, maintenance, fuel, and operating 
costs. The seven components can be characterized based 
on the specific context. For example, a transit agency 
could include infrastructure costs as part of the capital  
(or upfront procurement) cost, as in Figure 2.4, which sets 
the depot/infrastructure costs at zero. Alternatively, if 
these costs constitute a significant portion of the overall 
budget, they could be calculated separately. 
In the example shown in Figure 2.4, the annual operations 
cost is zero, because the relevant inputs (specifically, the 
driver and on-board labor data) are missing. It is critical 
that users understand the limitations of default data and 
their inputs.
Figure 2.4  |    Comparison of annual costs of two fleets

6  |  
The annual cost for each bus fleet is the sum of the 
equivalent annual cost of each bus type in the fleet over 
its lifetime, calculated by dividing the present value of 
lifetime costs of each bus type by an annuity factor. 1  
Because each bus type is likely to have a different 
lifespan, the annual fleet cost provides more useful 
information for transit agencies interested in acquiring  
a new bus fleet than calculating lifecycle costs.
The summary graphs–fleet page also plots the emissions  
of each fleet against the annual unit cost ($/kilometer/bus). 
Figure 2.5 does so for CO2 emissions. The Tool also plots 
total hydrocarbon (THC) and methane (CH4) emissions. 
Summary graphs—bus type page
The summary graphs—bus type page presents the annual 
unit costs for each bus type, in order to show how costs 
vary based on different combinations of fuel types, engine 
technology, and bus lengths. In Figure 2.6, for example, 
bus type 3 has higher fuel costs per bus than bus type 5, 
and the total cost of acquiring one bus is higher for bus 
type 3 than for bus type 5. 
Figure 2.5  |    Tradeoff between CO 2 emssions and unit costs of two bus fleets

TECHNICAL NOTE   | March 2019  |  7
Costs and Emissions Appraisal Tool for Transit Buses
To help users weigh the costs of a fleet against its 
emissions, the page also plots the annual unit cost against 
the emissions produced by each bus for each kilometer 
traveled (Figure 2.7). Buses can be expensive but  
achieve low emissions, economical but pollute more,  
or somewhere in between. Bus types in the lower left-
hand corner are the most cost-effective in reducing 
emissions. Users can use these graphs to select their bus 
types based on their budget and emissions targets. 
Figure 2.6  |    Annual cost per bus by bus type
Figure 2.7  |    Tradeoff between CO 2 emissions and unit costs of six bus types

8  |  
Summary tables page
The summary tables page has two main sections, cost 
output and emission output. Cost output includes three 
tables. The first two show the total and per bus annual 
cost breakdown for each bus type and fleet by operations, 
fuel, maintenance, overhaul, depot/infrastructure, and 
capital (or upfront procurement) costs. The third table 
shows capital and financing, operating, annual total, 
lifetime total, and annual total unit costs. The formulae 
used for these calculations are shown in section 3.
Emissions output includes two tables. They show the 
annual and lifetime emissions outputs for each bus type 
and fleet for various pollutants.
3.  BEHIND THE CURTAIN: HOW THE  
TOOL WORKS
Figure 3.1 shows how the Tool works. Users provide the 
inputs, shown in the six boxes at the top of the figure, 
using their own data or the default data built into the 
program. Based on these inputs, the Tool calculates 
capital and financing costs, operational costs, and 
emissions. The Tool also produces detailed output (such as 
annual cost by fleet and bus type, unit cost and emission 
comparison for different bus types, lifetime emissions of 
different buses) and a graphical summary of the results. 
Default Data
One of the key characteristics of the Tool is its flexibility, 
which allows users to input their own operational, cost, 
Figure 3.1  |    Visual overview of the Tool
Graphical Summary
(By fleet and by bus type)
Detailed Output
Cost Output
INPUTS
General 
Economic Data
• Country
• Discount rate (%)
Fleet-Specific Data
• Fuel type, technology
• Number of buses
• Annual (individual) bus 
  distance traveled (km/year/bus)
• Bus life (years)
• Bus length (m)
• Final purchase price for a 
  single bus ($/bus)
• Residual value (% of final 
  purchase price)
• Down payment (% of total cost)
• Loan interest rate (%)
• Loan lifetime (years)
Overhaul Data
• Engine overhaul ($/bus);
  frequency (years)
• Transmission overhaul ($/bus);
   frequency (years)
• CNG fuel system overhaul
  ($/bus); frequency (years)
• Hybrid system overhaul ($/bus);
   frequency (years)
• Battery replacement ($/bus);
   frequency (years)
• Vehicle retrofits ($/bus); 
  frequency (years)
Infrastructure Data
• Depot/fuel station
  construction ($); bus
  quantity
• Depot/fuel station
  retrofit($); bus quantity
• Special tools ($); 
  bus quantity
Emissions Data
• CO exhaust (g/km)
• THC exhaust (g/km)
• NOx exhaust (g/km)
• PM exhaust (g/km)
• CO2 exhaust (g/km)
• GHG/ CO2e exhaust (g/km)
• Upstream CO2 (g/km)
• Upstream PM (g/km)
Operations/Maintenance Data
• Total cost of driver labor ($/year/bus)
• Fuel economy (L/100 km)
• Fuel cost ($/L)
• Fuel cost projection (%/year)
• Fuel station operation costs ($/y)
• Insurance ($/year/bus)
• Additional operational costs to
  include ($/year/bus)
• Fixed annual maintenance costs
  ($/year/bus)
• Total cost of maintenance labor
  ($/year/bus)
• Brake reline ($/bus); frequency (years)
• Tires ($/bus); frequency (years)
• Battery conditioning ($/bus);
  frequency (years)
• DPF cleaning ($/bus); frequency (years)
• Fuel station maintenance ($/bus);
  frequency (years)
• Additional maintenance costs to
  include ($/year/bus)
Emissions Output
Operational
 Costs
Capital and  
Financing 
Costs

TECHNICAL NOTE   | March 2019  |  9
Costs and Emissions Appraisal Tool for Transit Buses
and emissions data to customize the analysis. For users 
who lack good local data, the Tool also includes default 
data from Brazil and the United States.2 (Based on 
feedback from users, the next version of the Tool will 
incorporate data from locations that find strategic value 
in the Tool, as well as from countries in which WRI has 
worked with transit operators for many years.) For both 
Brazil and the United States, the default inflation and 
discount rates (or lending interest rates) are the 2014 rates 
published by the World Bank. The data are average values 
from a wide range of sources (Cooper et al. 2012). 
Table 3.1 presents various combinations of fuel, 
technologies, and bus lengths.
COUNTRY FUEL TYPE TECHNOLOGY BUS LENGTH (METERS)
United States
Biodiesel 100 percent Euro V-VI 
Exhaust gas recirculation 12
Biodiesel 20 percent Euro V-VI 
Exhaust gas recirculation
Selective catalyst reduction
12
Diesel (more than 150 parts per million [ppm]) Euro II
Euro III 
Oxidation catalyst
12
Diesel-electric hybrid (15 ppm) Selective catalyst reduction 12
Low-sulfur diesel (50 ppm) Euro II
Euro III 12
Natural gas Euro V-VI 
Oxidation catalyst
Three-way catalyst
12
Ultra-low-sulfur diesel (15 ppm) Diesel particulate filter
EPA 2007
EPA 2010
Euro III
Euro IV
Euro V-VI
Exhaust gas recirculation
Oxidation catalyst
12
Brazil
Diesel-electric hybrid (10 ppm) Euro V 12
Electric Electric 12
Ultra-low-sulfur diesel (10 ppm) Euro III
12
Euro V
Euro V 18
Table 3.1  |   Combinations of fuel, technology, and bus length available in the Tool 
Note: EPA: Environmental Protection Agency.  Specific technology required to meet related emissions standards. 
Source: Cooper et al. 2012.

10  |  
Data on the United States
US cost default data come from studies of expenditures 
on US transit buses (e.g., the 2013 American Public 
Transportation Association [APTA] database cited in 
Neff and Dickens (2013), as shown in Table 3.2. The cost 
categories may differ from the cost categories of the user. 
The defaults should therefore be used only as a guide, not 
to make specific cost calculations.
Costs were taken from data for 2002–11 and converted to 
2014 US dollars using the inflation calculator of the US 
Bureau of Labor Statistics. The costs of specific technolo-
gies could have changed significantly over this period.  
The defaults used in the model are a combination of aver-
age cost data and expert analysis that focuses on the last 
five years of the data.
The fuel cost projections are nominal (without inflation). 
They were reported in 2013 dollars and converted to 2014 
values. These data come from the US Energy Information 
Administration’s Annual Energy Outlook 2015. 
Emissions default data were averaged over different fuel 
and technology types (Table 3.3). The dataset covers 
1994–2010 and is based on reports from field and lab 
emissions tests (see Cooper et al. 2012). 
Fuel Biodiesel 100% Biodiesel  
20%
Diesel  
(150 ppm +)
Diesel-Electric 
Hybrid (15 ppm)
Low Sulfur 
Diesel (50 ppm) Natural Gas Ultra Low Sulfur 
Diesel (15 ppm) Electric
Bus Length 12m 12m 12m 12m 12m 12m 12m 12m
Fleet-Specific Data
Useful life of bus (years) 13 13 13 13 13 13 13 20
Final purchase price for a single bus ($/bus)  $ 189,466  $ 189,466  $ 349,830  $ 540,000  $ 349,830  $ 153,000  $ 349,830  $ 800,000 
Residual value (percent of final purchase price) 10% 10% 10% 10% 10% 10% 10% 10%
Down payment (percent of total cost) 30% 30% 30% 30% 30% 30% 30% 30%
Loan interest rate (percent) 12% 12% 12% 12% 12% 12% 12% 12%
Loan life (years) 13 13 13 13 13 13 13 13
Annual Operations Data
Total cost of driver and on-board labor ($/year/bus)  $ 61,778  $ 61,778  $ 45,567  $ 45,567  $ 45,567  $ 79,829  $ 45,567  $ 45,567
Fuel economy (Liter/100km) 50 50 50 50 50 50 50 0
Fuel cost ($/liter) $ 1.04 $ 1.04 $ 0.79 $ 0.79 $ 0.79 $ 0.46 $ 0.79 –
Fuel projection (Percent/year) 0.0% 0.0% 0.8% 0.8% 0.8% 0.4% 0.8%
Fuel station operation costs ($/year/bus) $ 6,800 $ 6,800 $ 6,800 $ 6,800 $ 6,800 $ 8,500 $ 6,800
Maintenance Data
Fixed annual maintenance cost ($/year/bus) $ 35,621 $ 35,621 $ 30,970 $ 28,725 $ 30,970 $ 36,017 $ 30,970 $ 30,970
Total cost of maintenance labor ($/year/bus) $ 39,022 $ 36,194 $ 39,022 $ 54,000 $ 39,022 $ 39,022
Brake reline ($/bus) $ 2,000 $ 2,700 $ 2,000 $ 3,800 $ 2,000
Frequency (years) 1 1 1 1 1
Tires ($/bus) $ 11,410 $ 11,410 $ 9,939 $ 9,939 $ 6,752 $ 9,939
Frequency (years)
Fuel station maintenance ($/bus) $ 6,567 $ 6,567 $ 6,012 $ 2,097 $ 6,012 $ 5,306 $ 6,012
Frequency (years) 1 1 1 1 1 1 1
Additional maintenance costs to include ($/year/bus) $ 11,409 $ 11,409 $ 11,847 $ 24,811 $ 11,847 $ 7 ,109 $ 11,847
Overhaul or Retrofitting  (Optional)
Engine overhaul ($/bus) $ 23,000 $ 23,000 $ 23,000 $ 17 ,000 $ 23,000 $ 23,000 $ 23,000
Frequency (years) 6 6 6 6 6 6 6
Transmission overhaul ($/bus) $ 13,400 $ 13,400 $ 13,400 $ 39,000 $ 13,400 $ 13,400 $ 13,400
Frequency (years) 6 6 6 6 6 6 6
Hybrid system overhaul ($/bus) $ 13,200
Frequency (years) 2
Battery replacement ($/bus) $ 31,400
Frequency (years) 6
Additional Infrastructure (Optional)
Depot/fuel station construction ($) $ 14,617 $ 14,617 $ 24,091 $ 53,000 $ 24,091 $ 10,275 $ 24,091 $ 1,000,000 
INCLUDES: Battery charging 
and conditioning 
equipment 
Refueling  
station 
Depot/fuel station retrofit ($) $ 870 $ 870 $ 85,000 $ 33,000
INCLUDES: Update depot Update depot Battery 
conditioning 
station 
Refueling  
station 
Special tools ($) $ 11,400 $ 7 ,300
Special tools quantity 100 1
INCLUDES: Diagnostic 
equipment 
Diesel Particulate 
Filter (DPF) 
Table 3.2  |  Default fleet-specific and annual operations cost data for the United States

TECHNICAL NOTE   | March 2019  |  11
Costs and Emissions Appraisal Tool for Transit Buses
Data on Brazil
Data on Brazil (Tables 3.4 and 3.5) were collected by 
WRI Brasil from interviews with Brazilian transit 
agencies such as SPTrans and Transport Agency of São 
Paulo (Preferitura de São Paulo 2015), as well as from 
a literature review that included reports by Agência 
Nacional do Petróleo, Gás Natural e Biocombustíveis 
(2017), Instituto Brasileiro de Geografia e Estatística 
(2014), and Ministério do Meio Ambiente Secretaria de 
Mudanças Climáticas e Qualidade Ambiental (2011). 
Monetary figures are presented in US dollars (at an 
exchange rate of US$0.43 per Brazilian real). Users can 
modify this value in the default cost data tab. In the same 
tab, they can adjust the inflation rate to forecast fuel costs.
Collecting data in developing countries is difficult. Capital 
costs and financing costs are relatively accessible, but 
operations and maintenance costs, which transit agencies 
are most interested in, are still very difficult to capture. 
For this reason, the default data should be used for 
general guidance for initial project scoping, not to make 
specific cost calculations.
Fuel Biodiesel 
100% Biodiesel 20% Diesel (150 ppm +)
Diesel-
Electric 
Hybrid 
(15 ppm)
Low Sulfur 
Diesel (50 
ppm)
Natural Gas Ultra Low Sulfur Diesel (15 ppm)
Technology
Exhaust 
Gas 
Recir-
culation 
(EGR)
Euro 
V-VI
Exhaust 
Gas 
Recir-
culation 
(EGR)
Selective 
Catalyst 
Reduc-
tion 
(SCR)
Euro 
V-VI
Oxidation 
Catalyst 
(OC)
Euro 
II
Euro 
III
Selective 
Catalyst 
Reduc-
tion 
(SCR)
Euro 
II
Euro 
III
Oxidation 
Catalyst 
(OC)
Three-
Way 
Catalyst 
(3WC)
Euro 
V-VI
Oxidation 
Catalyst 
(OC)
Diesel 
Par-
ticulate 
Filter 
(DPF)
Exhaust 
Gas 
Recir-
culation 
(EGR)
EPA 
2007
EPA 
2010
Euro 
III
Euro 
IV
Euro 
V-VI
Bus Length 12m 12m 12m 12m 12m 12m 12m 12m 12m 12m 12m 12m 12m 12m 12m 12m 12m 12m 12m 12m 12m 12m
Carbon 
dioxide  
(CO2), g/L
2,432 2,432 2,714 2,414 2,564 2,266 2,320 1886 2,586 2,400 2,918 2,418 2,380 2,958 2,802 2,668 3,780 3,260 2,418 2,238 2,352
Total  
hydrocarbons 
(THC), g/km
0.2 0.0 0.0 0.0 0.0 0.2 0.8 1.0 0.1 0.1 16.2 1.2 0.4 0.5 0.0 0.0 0.1 0.0 0.2 0.0 0.0
Non-methane  
hydrocarbons 
(NMHC), g/km
2.0
Methane  
(CH4), g/km 3.0
Nitrogen oxide 
(NOx), g/km 8.3 8.1 10.4 10.1 10.2 10.1 12.4 9.8 12.5 11.0 12.3 3.2 1.9 5.3 16.3 9.0 3.6 1.0 9.0 8.5 8.0
Nitrous oxide 
(N2O), g/km 4.0
Nitric oxide 
(NO), g/km 5.0
Particulate 
matter (PM), 
g/km
0.05 0.03 0.04 0.03 0.04 0.05 0.11 1.12 0.17 0.11 0.11 0.03 0.03 0.03 0.11 0.11 0.11 0.11 0.11 0.11 0.11 0.11
Carbon 
monoxide 
(CO), g/km
0.2 0.8 0.1 5.0 2.5 2.5 2.3 1.6 2.2 5.7 0.4 1.5 1.6 1.0 0.7 0.3 0.1 0.1 2.8 4.5 1.8
Table 3.3  |  Default emissions data for the United States

12  |  
FUEL DIESEL-ELECTRIC 
HYBRID (10 PPM) ELECTRIC ULTRA-LOW SULFUR DIESEL (10 PPM)
BUS LENGTH 12M 12M 12M 18M
Fleet-specific data
Useful life of bus (years) 12 15 10 12
Final purchase price for a single bus ($/bus) 322,500 537,500 215,000 344,000
Residual value (percent of final purchase price) 10 5 10 10 
Down payment (percent of total cost) 20 20 30 30 
Loan interest rate (percent) 9.9 9.4 9.9 9.9 
Loan life (years) 9 14 9 9
Annual operations data
Energy use (kwh/km) 1.3
Energy cost ($/kwh) 0.215
Fuel consumption (L/100km) 41.5 45.0 73.0
Fuel cost ($/L) 1.43 1.43 1.43
Maintenance data
Fixed annual maintenance cost ($/year/bus) 19,350 7,310 12,900 30,100
Table 3.4  |   Default cost data for Brazil 
FUEL ULTRA-LOW SULFUR DIESEL (10PPM) DIESEL-ELECTRIC 
HYBRID (10 PPM) ELECTRIC
TECHNOLOGY EURO V EURO III EURO V EURO V ELECTRIC
BUS LENGTH 12M 12M 18M 12M 12M
Carbon dioxide (CO 2), g/L 2,603 2,603 2,603 2,352
Non-methane hydrocarbons (NMHC), g/km 0.033 0.326 0.033 0.46
Methane (CH4), g/km 0.06 0.06 0.06 0.06
Nitrogen oxide (NO x), g/km 2.103 8.515 2.103 1.70
Nitrous oxide (N 2O), g/km 0.03 0.03 0.03 0.03
Particulate matter (PM), g/km 0.02 0.154 0.02 0.02
Carbon monoxide (CO), g/km 0.44 1.487 0.44 1.55
Upstream GHG/CO 2e, g/km 179
Total GHG, g/km 179
Table 3.5  |   Default emissions data for Brazil

TECHNICAL NOTE   | March 2019  |  13
Costs and Emissions Appraisal Tool for Transit Buses
Calculation of Costs and Emissions 
Calculation of costs
This part examines two assumptions made in calculating 
costs. Section 4 discusses additional issues. 
First, to avoid comparing buses with different lifespans, 
the Tool uses the equivalent annual cost concept to 
distribute the capital (or upfront procurement) cost 
across the actual operating years. Second, in the default 
calculation, operation and maintenance costs are assumed 
to be constant over time. Fuel cost can be adjusted to 
change over time. 
The back-end lifetime cost calculations for each bus type 
are found on the capital financing calc and total operating 
cost calc pages. The capital financing calc page includes 
three lifetime costs: capital, financing, and depot/
infrastructure costs. (Note that infrastructure costs 
can be defined as part of or separate from capital cost, 
depending on user need.) The total operating cost calc 
page calculates four costs: operations, fuel, maintenance, 
and overhaul/retrofits. Table 3.6 describes the formulae 
used to calculate lifetime costs.
Costs are annualized by using the equivalent annual cost 
formula from the summary tables page. Other costs, such 
as annual unit costs per bus/kilometer and per bus, are 
calculated in the summary tables. Table 3.7 shows the 
formulae for the unit costs at both the bus type and bus 
fleet levels.
COST FORMULA
Capital (or upfront 
procurement) cost
For each bus type, the present value ( PV) of the capital cost includes any down payment, residual value, infrastructure, 
and principal over the course of the loan’s lifetime (if there is a loan). Infrastructure costs can be included either as 
part of the overall capital cost or separately, under depot/infrastructure cost. Total capital costs are calculated over the 
course of the bus’s useful life, as follows:
                                     PV of Lifetime Capital Cost =  DP – BR + IF + ∑
L 
i=1
 
where DP = down payment; BR = PV of bus’s residual value ( BRV) =               
IF = infrastructure cost; Pi = principal in year i; r = discount rate; and L = bus useful life.
Financing cost For each bus type, the financing cost is based on the interest on the loan financing the bus purchase:
                                                   PV of Lifetime Financing = ∑
L 
i=1
where Ii = interest in year i; r = discount rate; and L = bus useful life.
Additional depot/
infrastructure cost 
For each bus type, the (additional) depot/infrastructure cost is considered a one-time cost in the initial year (year 0). It 
is calculated based on the depot/fuel station construction cost, the depot/fuel station retrofit cost, and the cost of other 
special tools:
                                             Additional Depot/Infrastructure Cost = N  ×  (        +        +         )
where N = number of buses within a bus type; C = depot/infrastructure construction cost; NC = number of buses 
that share the depot/infrastructure; R = depot/infrastructure retrofit; NR = number of buses that share the depot/
infrastructure retrofit; SP = special tools cost; and NSP = number of buses that share the special tools.
Table 3.6  |   Formulae for calculating lifetime costs
Pi
(1+ r)i
Ii
(1+ r)i
BRV
(1+ r)i
C
NC
R
NR
SP
NSP

14  |  
COST FORMULA
Total operating cost For each bus type, the total operating cost is broken down into operating cost (driver labor, fuel station operation cost, 
insurance cost, etc.); fuel cost; maintenance cost; and overhaul cost (not all of these costs are required for the 
calculation). The formula does not subtract out any national or local subsidies (e.g., for electric buses), although they  
could strongly affect the costs for fleet operators. 
PV of Lifetime Total Operating Cost = 
PV of Lifetime Operating Cost + PV of Lifetime Fuel Cost + PV of Lifetime Maintenance 
Cost + PV of Lifetime Overhaul Cost 
  PV of Lifetime Operating Cost = 
                                              N  = ∑
L 
i=1 
(FSO + DL + IN + AO)
where N = number of buses within a bus type; FSO = lump-sum number for operating costs related to fuel stations; 
DL = driver labor; IN = insurance; AO = additional operating costs; r = discount rate; and L = bus useful life.
PV of Lifetime Fuel Cost =
                                          N  = ∑
L 
i=1 
d x 0.01 x FE x (FA + FC) x
where N = number of buses within a bus type; d = annual bus distance travelled; FE  = fuel consumption (fuel 
economy, in liters per 100 kilometers); FA  = fuel additive ($ per liter); FC  = fuel cost ($ per liter); p = fuel cost 
projection; r = discount rate; and L= bus useful life.
PV of Lif etime Maintenance Cost = 
                   ∑
 
(FAM + A M + ML + αBR + βTI + γBC + ⅾDC + φFSM + μLU) i
                   α, β, γ, ⅾ, φ, and μ are 1, for ┌ bf, tf, bcf, df, fs, and lf, respectively  ┐= integera; otherwise 0
where N = number of buses within a bus type; FAM = fixed annual maintenance cost; AM = additional maintenance 
cost; ML = maintenance labor; BR = brake reline cost; bf = brake reline frequency; TI = tires cost; tf = tire frequency; 
BC = battery conditioning cost; bcf = battery conditioning frequency;  DC = diesel particulate filter (DPF) cleaning cost; 
df = DPF cleaning frequency; FSM = fuel station maintenance; cost; fs = fuel station maintenance frequency;  
LU = lubricant cost; lf = lubricant frequency; r = discount rate; and L = bus useful life.
PV of Lifet ime Overhaul Cost =
                                       ∑ 
(σEO + τTO + xCF + ωHS + ρBA + ξVR) i
               σ, τ, x, ω, ρ, and ξ are 1, for ┌ eof, tof, cof, hos, brf, and vf, respectively  ┐= integer; otherwise 0
where N = number of buses within a bus type; EO = engine overhaul cost; eof = engine overhaul frequency;  
TO = transmission overhaul cost; tof = transmission overhaul frequency; CF = CNG system overhaul cost; cof = CNG 
system overhaul frequency; HS = hybrid system overhaul cost; hos = hybrid system overhaul frequency;  
BA = battery replacement cost; brf = battery replacement frequency; VR = vehicle retrofits; vf = vehicle  
retrofits frequency; r = discount rate; and L = bus useful life.
Table 3.6  |   Formulae for calculating lifetime costs
Note: a. ┌x┐ = ceiling of x = smallest integer greater than or equal to x.
(1+ p) i
(1+ r) i
I
(1+ r) i
N   
i=1
L
N   
i=1
L
(1+ r) i
i
i
(1+ r) i

TECHNICAL NOTE   | March 2019  |  15
Costs and Emissions Appraisal Tool for Transit Buses
Calculation of emissions 
Ideally, emissions factors should be based on average 
speeds, taking road congestion and other conditions  
into account. Because of lack of data on all types of 
vehicles under different conditions, the emissions 
estimates provided in the Tool are instead based on 
general emissions factors from lab testing reports in  
the database. 
For pollutants other than CO2, tailpipe technology plays a 
bigger role than fuel economy and road conditions. Road 
conditions, such as congestion, and operational behaviors 
can be adjusted on a case-by-case basis if users have local 
operational data or factors to adjust the results. 
The Tool assumes that fuel economy for each bus and fuel 
type is constant over the life of the bus.
Emissions calculations appear on the summary tables 
page. Exhausts are grouped into three categories, based 
on their emissions factors, which are measures in terms 
of grams per liter for CO2 and grams per kilogram for all 
other exhaust pollutants (Table 3.8). For each bus type, 
annual emissions are then multiplied by the useful bus 
lifespan to obtain lifetime exhaust emissions.
COST FORMULA
Annual cost of each  
bus type 
where PV = net present value for each cost type (from table 3.6); r = discount rate; and L = bus useful life.  
(Note: A built-in Excel function, –PMT( ), is used to calculate this equivalent annual cost.) 
Annual unit cost of each  
bus type 
where A = annual cost for all buses within a bus type and N = number of buses within a bus type.
Annual unit cost of each 
bus type traveling for one 
kilometer 
where A = annual cost for all buses within a bus type; N = number of buses within a bus type; and d = annual bus 
distance traveled.
Annual unit cost of each 
bus fleet traveled for one 
kilometer 
where AF = annual cost for all buses within a bus fleet; n = number of bus types within a bus fleet; di = annual 
bus distance traveled for bus type i; and Ni = number of buses within bus type i.
Table 3.7  |   Formulae for calculating unit costs
PV * r
1-(1+ r)-L
 A
N
 A
d * N
AF * n
∑ n
i = 1(di *Ni)

16  |  
EXHAUST FORMULA
CO2  For each bus type, CO 2 emissions are calculated based on fuel economy (liters per 100 km) and the CO 2 emissions 
factor (g/L) for the total distance traveled by all buses.
Annual CO2 Emissions = N × d × FE × eCO2
where N = number of buses within a bus type; d = annual bus distance traveled; FE = fuel consumption  
(fuel economy in liter per 100 km); and eCO2  = emissions factor for CO 2.
THC, NMHC, CH 4, NOx, N2O,  
NO, PM, CO  
For each bus type, total emissions are calculated based on emissions factors (grams per kilogram), which rely 
primarily on different technology types (e.g., Euro III). Not all emissions factors apply to all bus technology types.
Annual Pollutant Emissions = N × d × EFP
where N = number of buses within a bus type; d = annual bus distance traveled; and EFP = emissions factor for 
THC, NMHC, CH 4, NOx, N2O, NO, PM, and CO.
Greenhouse gases (GHG) Different greenhouse gases are translated into CO 2 equivalent based on their impacts on global warming (US EPA 
2017; Myhre et al. 2013). Three GHG-related emissions can be calculated: 
 ▪ GHG or CO2 equivalent (tank-to-wheel emissions) 
 ▪ Upstream (well-to-tank) GHG or CO 2 equivalent 
 ▪ Total GHG or CO2 equivalent.
For each bus type,
Annual GHG Emissions = N × d × EFGHG
Annual Upstream GHG Emissions = N × d × EFUp
Annual Total GHG Emissions = N × d × EFTotal  = 
Annual GHG Emissions + Annual Upstream GHG Emissions
where N = number of buses within a bus type; d = annual bus distance traveled; EFGHG = emissions factor  
for GHG/CO2 equivalent for a certain type of fueled bus; EFUp = emissions factor for upstream GHG/CO 2 equivalent 
(based on bus fuel technologies); and EFTotal = emissions factor for total GHG/CO 2 equivalent (based on bus  
fuel technologies).
Table 3.8  |   Formulae for calculating exhaust emissions
Note: All estimates are in grams or tonnes. CO 2: Carbon dioxide; THC: Total hydrocarbons; NMHC: Non-methane hydrocarbons; CH 4: Methane; NO x: Nitrogen oxides; N 2O, Nitrous oxide;  
NO, Nitric oxide; PM: Particulate matter; CO: Carbon monoxide; GHG/CO 2e: Greenhouse gases/carbon dioxide equivalent; Upstream GHG/CO 2e: Upstream greenhouse gases/carbon dioxide 
equivalent; Total GHG/CO 2e: Total greenhouse gases/carbon dioxide equivalent.

TECHNICAL NOTE   | March 2019  |  17
Costs and Emissions Appraisal Tool for Transit Buses
4.  LIMITATIONS OF THE TOOL
This easy-to-use Excel-based Tool allows users to examine 
costs and emissions as part of an initial screening of 
potential bus fleets. More comprehensive analysis is 
needed for final decision making. Some of the Tool’s 
advantages and limitations are identified below. 
 
1. The Tool distributes capital costs across 
years, to improve decision making.  The high 
upfront cost of purchasing a bus may cause decision 
makers to make a suboptimal decision, forgoing a 
bus with a longer lifespan, higher fuel efficiency, 
and lower tailpipe emissions, for example, because 
its purchase price is too high. To prevent this kind 
of decision making, this Tool distributes the capital 
(or upfront procurement) cost across the operating 
years by using the equivalent annual cost concept. 
It allows operators to compare the annual total cost 
of ownership of different technologies to determine 
which is cheapest. The Tool calculates annual costs 
based on each bus type, which are then summed 
to obtain the total cost for the bus fleet. The simple 
calculation of present value does not account for 
the various contracting and bus leasing options that 
might take place when a transit agency acquires the 
buses or account for inflation.
Transit agencies around the world often use different 
terminologies in their financial decision-making 
processes. Most agencies distinguish between Capital 
Expenses (CapEx), which include costs such as bus 
procurement, and Operating Expenses (OpEx), which 
include fuel and maintenance. But agencies group 
specific costs under the two umbrella categories in 
different ways. For this reason, the Tool does not use 
the two categories. Users are encouraged to customize 
the output results to fit their needs. 
 
2. The Tool does not capture full life cycle 
emissions. Because of lack of data, the only scenario 
in which the Tool incorporates upstream emissions 
is the one for electric buses in the Brazil country 
selection. Even in this case, users cannot perform 
a comprehensive life cycle analysis, because the 
exercise would entail considering emissions from other 
processes (such as upstream fuel production, vehicle 
production, nonexhaust emissions, and bus scrappage).  
3. The Tool does not automatically optimize 
options. The Tool can analyze various costs and 
emissions scenarios. But users have to create these 
cases manually, by selecting different combinations 
of fuel type, engine technology and useful life, and 
so forth. The Tool does not automatically perform 
optimization based on multiple variables. 
4. The Tool assumes constant (rather than 
declining) fuel economy over the life of the 
vehicle. Fuel consumption depends on a range of 
factors, such as bus age, operating speed, average 
occupancy rate, fuel quality, road conditions, and 
congestion. Emissions also depend on the sources of 
fuel, the production and transmission process, and the 
emissions reduction technology used on the bus. The 
Tool translates complex fuel consumption patterns into 
simplified fuel economy and emissions factors. The 
quality of the results on operation costs and exhaust 
emissions depends on how well the data reflect local 
conditions. To simplify the real operational conditions, 
fuel economy in this Tool is assumed to be a constant 
value, instead of either declining as the vehicle ages or 
changing at different speeds.
5. The Tool’s default data may not reflect local 
conditions. The default data used in the Tool are 
based mainly on US and European bus lab and road 
test data. US and European bus emissions and costs 
data are not suitable for local decision making in most 
developing countries, because cities in the Global 
South have different emissions and vehicle standards 
as well as different cost levels to achieve them. Even 
when buses are from the same manufacturer, tailpipe 
emissions can still vary widely because of different 
road conditions and operating styles. 
The Tool also includes default data from Brazil. These 
data may be more comparable to local conditions 
in developing countries. For electricity-related data 
(which are very difficult to obtain, as electric buses are 
still relatively new), the default grid emissions factors 
from Brazil may not be applicable in other places, 
however, given Brazil’s heavy use of hydropower (and 
therefore low electricity prices).

18  |  
INPUT DESCRIPTION
Annual operations data Records all operating costs incurred in a year, including the total cost of driver and on-board labor, electricity use 
and cost, fuel economy and cost, fuel cost projections, fuel additive cost, fuel station operating costs, insurance, 
and additional operating costs. Options do not include inputs for national or local subsidies. Users can populate the 
values automatically, using the default values. 
Emissions factors Asks user to input values for exhaust and upstream emissions or select default data. Exhaust emissions refer to the 
emissions caused directly by the bus, including carbon monoxide (CO), total hydrocarbons (THC), nitrogen oxides 
(NOx), particulate matter (PM), carbon dioxide equivalent (CO 2e), and greenhouse gas/carbon dioxide equivalent 
(GHG/CO2e). Upstream emissions refer to the emissions caused during fuel production, including GHG/CO 2e and PM. 
Fleet-specific data Provides information about the bus and how it will be financed, including the useful life of the bus; the final pur -
chase price per bus; the residual value; and the down payment, loan interest rate, and loan tenure. (The interest rate 
and tenure are input as zero if the operator does not plan to finance the bus purchase.)
Infrastructure Takes into account any capital-related, one-time updates or construction. Parameters include depot/fuel station 
construction cost and the number of buses it refers to, depot/fuel station retrofit cost and the number of buses it 
refers to, and special tools and the number of buses it refers to. Users can populate the values with local data if this 
is relevant.
Maintenance data Records all maintenance data. Users can report maintenance as a fixed annual cost per bus or as itemized costs 
with prescribed frequencies. Itemized costs include annual maintenance labor; the cost and frequency of brake 
reline, tires, battery conditioning, diesel particulate filter (DPF) cleaning, fuel station maintenance, and lubricant; and 
any additional annual maintenance costs. Users can populate the values with default option or local data.
Overhaul or retrofitting Considers all vehicle retrofits or overhauls that might take place over the vehicle’s useful life. Parameters include the 
cost and frequency of engine overhaul, transmission overhaul, compressed natural gas (CNG) fuel system overhaul, 
hybrid system overhaul, battery replacement, and vehicle retrofit. Users can populate the values with local data.
Table A.1  |   Description of input data 
APPENDIX A

TECHNICAL NOTE   | March 2019  |  19
Costs and Emissions Appraisal Tool for Transit Buses
TERM UNIT DESCRIPTION
Additional maintenance costs $/year/bus Maintenance costs not covered in previous categories. Costs included should also be 
included in subsequent bus types and fleets, to remain consistent.
Additional operational costs $/year/bus Operations costs not covered in previous categories. Costs included should also be 
included in subsequent bus types and fleets, to remain consistent.
Annual (individual) bus 
distance traveled
Km/year/bus  Average annual distance each bus travels for each bus type
Battery conditioning $/bus; years Cost and frequency of battery conditioning
Battery replacement $/bus; years Cost and frequency of battery replacement
Brake reline $/bus; years Cost and frequency of brake relining
Bus length Meters Bus length (12 meters [standard] or 18 meters [articulated])
Compressed natural gas 
(CNG) fuel system overhaul
$/bus; years Cost and frequency of transmission overhaul (applies only if bus type includes CNG)
Country Brazil or United States
Depot/fuel station 
construction
$/bus quantity Cost of and capacity for constructing a station for each bus type
Depot/fuel station retrofit $/bus quantity Cost of and capacity for fuel station retrofitting for each bus type
Discount rate  Percent Figures vary widely around the world. The public discount rate is 3–7 percent for high-
income countries and 8–15 percent for the Global South, depending on the country’s 
socioeconomic conditions (Zhuang et al. 2007). For private companies, the value also 
differs greatly; users should input their own data, based on local conditions. Users are 
encouraged to perform sensitivity analysis using different discount rates.
Down payment Percent Percentage required as down payment for loan to finance bus type
Diesel particulate filter (DPF) 
cleaning
$/bus; years Cost and frequency of DPF cleaning
Engine overhaul $/bus; years Cost and frequency of engine overhaul
Final purchase price for a 
single bus
$/bus Cost to buy one bus, after relevant deductions
Fuel additive $/liter Cost of fuel additive
Fuel cost $/liter Current fuel cost
Fuel economy Liter/100 km Expected fuel economy for an individual bus
Table A.2  |   Glossary of cost-related inputs

20  |  
TERM UNIT DESCRIPTION
Fuel projection Percent/year Projected annual change in fuel cost
Fuel station maintenance $/bus; years Cost and frequency of fuel station maintenance
Fuel station operation costs $/year/bus Fuel station operation costs
Fuel type Types include biodiesel 100 percent, biodiesel 20 percent, diesel (more than 150 ppm); 
diesel-electric hybrid (10 ppm), diesel-electric hybrid (15 ppm), and diesel-electric 
hybrid (50 ppm); electric; ethanol; natural gas; and low-sulfur diesel (50 ppm), ultra-
low-sulfur diesel (10 ppm), and ultra-low-sulfur diesel (15 ppm). The fuel type can differ 
for each bus type.
Hybrid system overhaul $/bus; years Cost and frequency of hybrid system overhaul (applies only if bus type includes hybrid)
Insurance $/year/bus Insurance
Loan interest rate Percent/year Annual interest rate on loan for bus 
Loan lifetime Years Term of loan
Lubricant $/bus; years Cost and frequency of lubricants
Number of buses Number Number of buses for each bus type. (Note: This item is not the total number of buses in 
the fleet; it is the number of buses of this type.)
Residual value Percent Expected residual value of a single bus
Special tools $/bus quantity Cost of special tools that each bus type warrants and number of buses it applies to.
Technology type Types include diesel particulate filter (DPF), exhaust gas recirculation (EGR), oxidation 
catalyst (OC), and three-way catalyst (3WC), electric, and the technology required to 
meet emissions standards such as EPA 2007, Euro II, Euro III, Euro V, Euro V-VI standards. 
The list of technologies will be updated based on the fuel type selected.
Tires $/bus; years Cost and frequency of tire changes
Total cost of driver labor $/year/bus Total cost of drivers. Factors taken into account in this response should also be included 
in subsequent bus types and fleets, to remain consistent.
Total cost of maintenance 
labor
$/year/bus Total cost to hire maintenance workers. Factors included in this response should also 
be included in subsequent bus types and fleets, to remain consistent. 
Transmission overhaul $/bus; years Cost and frequency of transmission overhaul
Useful life Years Typical useful life of buses in each bus type. Value should reflect length of time after 
which buses must be retired or sold for reuse.
Vehicle retrofits $/bus; years Cost and frequency of vehicle retrofitting for each bus type. 
Table A.2  |   Glossary of cost-related inputs (Cont.)

TECHNICAL NOTE   | March 2019  |  21
Costs and Emissions Appraisal Tool for Transit Buses
ENDNOTES
1. The annuity factor is calculated as A( t, r) = (1 – [1 /(1 + r)]t) /r, where t 
is the number of years of operation of a bus (its lifespan) and r is the 
discount rate.
2. The mobile combustion emissions factors used by the Intergovern -
mental Panel on Climate Change (IPCC) (https://www.epa.gov/sites/
production/files/2015-07/documents/emission-factors_2014.pdf) can 
also be used as references when local emissions data are unavailable. 
Users are encouraged to use local emissions factors for bus operation 
whenever possible. 
REFERENCES
Agência Nacional do Petróleo, Gás Natural e Biocombustíveis. 2017. Sistema 
de levantamento de preços. https://www.anp.gov.br/preco/index.asp.
Argonne National Laboratory. 2017. A fresh design for GREET life cycle 
analysis tool. https://greet.es.anl.gov/index.php?content=greetdotnet.
COPPE/UFRJ, & FETRANSPOR. 2012. Alternativas tecnológicas para ônibus no 
Rio de Janeiro. http://www.fetranspordocs.com.br/downloads/37Alternativas
tecnologicas.pdf.
Cooper, Erin, Magdala Arioli, Aileen Carrigan, and Umang Jain. 2012. “Exhaust 
Emissions of Transit Buses: Sustainable Urban Transportation Fuels and 
Vehicles.” Working Paper. Washington, DC: EMBARQ. https://wrirosscities.
org/research/publication/exhaust-emissions-transit-buses. 
Instituto Brasileiro de Geografia e Estatística. 2014. Índices de Preços ao 
Consumidor - IPCA e INPC [Broad National Consumer Price Index].  
https://ww2.ibge.gov.br/home/estatistica/indicadores/precos/inpc_ipca/
ipca-inpc_201802_1.shtm.
Ministério do Meio Ambiente Secretaria de Mudanças Climáticas e 
Qualidade Ambiental. 2011. Inventário nacional de emissões atmosféricas por 
veículos automotores rodoviários: Relatório final. http://www.mma.gov.br/
estruturas/163/_publicacao/163_publicacao27072011055200.pdf.
M.J. Bradley and Associates. 2006. Life Cycle Cost and Emissions 
Model: Alternative Bus Technologies . Durham, NC: Nicholas Institute for 
Environmental Policy Solutions, Duke University. https://nicholasinstitute.
duke.edu/sites/default/files/publications/best-bus-model-november-2006-
paper.pdf.
Myhre, G., D. Shindell, F.‐M. Bréon, W. Collins, J. Fuglestvedt, J. Huang, D. Koch, 
J.‐F. Lamarque, D. Lee, B. Mendoza, T. Nakajima, A. Robock, G. Stephens, 
T. Takemura, and H. Zhang. 2013. “Anthropogenic and Natural Radiative 
Forcing.” In Climate Change 2013: The Physical Science Basis. Contribution 
of Working Group I to the Fifth Assessment Report of the Intergovernmental 
Panel on Climate Change . Cambridge: Cambridge University Press.
Neff, J., and M. Dickens. 2013. 2013 Public Transportation Fact Book , 64th 
ed. American Public Transportation Association. http://www.apta.com/
resources/statistics/Documents/FactBook/2013-APTA-Fact-Book.pdf.
Preferitura de São Paulo. 2015. São Paulo Transporte. http://www.prefeitura.
sp.gov.br/cidade/secretarias/upload/transportes/SPTrans/acesso_a_
informacao/2015/detalhamento-planilha-tarifaria-reajustejan-16.xlsx.
Sistema Especial de Liquidação e de Custódia [Special Settlement and 
Custody System]. n.d. Taxa de Juros Selic [Interest Rate from SELIC]. 
http://idg.receita.fazenda.gov.br/orientacao/tributaria/pagamentos-e-
parcelamentos/taxa-de-juros-selic. Accessed on May 4, 2018.
US Bureau of Labor Statistics. n.d. CPI Inflation Calculator.  
https://www.bls.gov/data/inflation_calculator.htm. Accessed on May 4, 2018.
US Energy Information Administration. 2015. Annual Energy Outlook 2015 : 
Appendix A. https://www.eia.gov/outlooks/aeo/pdf/tbla3.pdf.
US Environmental Protection Agency. 2017. Understanding Global Warming 
Potentials. https://www.epa.gov/ghgemissions/understanding-global-
warming-potentials.
World Bank. 2014. Inflation, GDP deflator (annual percent).  
https://data.worldbank.org/indicator/NY.GDP .DEFL.KD.ZG.
Zhuang, J., Z. Liang, T. Lin, and F.D. Guzman. 2007. “Theory and Practice in 
the Choice of Social Discount Rate for Cost-Benefit Analysis: A Survey.” 
Asian Development Bank, Manilla. https://www.adb.org/sites/default/files/
publication/28360/wp094.pdf.

ABOUT WRI 
World Resources Institute is a global research organization that turns big ideas 
into action at the nexus of environment, economic opportunity, and human 
well-being. 
Our Challenge
Natural resources are at the foundation of economic opportunity and human 
well-being. But today, we are depleting Earth’s resources at rates that are not 
sustainable, endangering economies and people’s lives. People depend on clean 
water, fertile land, healthy forests, and a stable climate. Livable cities and clean 
energy are essential for a sustainable planet. We must address these urgent, 
global challenges this decade.
Our Vision
We envision an equitable and prosperous planet driven by the wise management 
of natural resources. We aspire to create a world where the actions of 
government, business, and communities combine to eliminate poverty and 
sustain the natural environment for all people.
Our Approach
COUNT IT
We start with data. We conduct independent research and draw on the latest 
technology to develop new insights and recommendations. Our rigorous 
analysis identifies risks, unveils opportunities, and informs smart strategies. 
We focus our efforts on influential and emerging economies where the future of 
sustainability will be determined.
CHANGE IT
We use our research to influence government policies, business strategies, 
and civil society action. We test projects with communities, companies, 
and government agencies to build a strong evidence base. Then, we work 
with partners to deliver change on the ground that alleviates poverty and 
strengthens society. We hold ourselves accountable to ensure our outcomes  
will be bold and enduring.
SCALE IT
We don’t think small. Once tested, we work with partners to adopt and expand 
our efforts regionally and globally. We engage with decision-makers to carry out 
our ideas and elevate our impact. We measure success through government and 
business actions that improve people’s lives and sustain a healthy environment.
Maps are for illustrative purposes and do not imply the expression of any opinion on the 
part of WRI, concerning the legal status of any country or territory or concerning the 
delimitation of frontiers or boundaries.
Copyright 2019 World Resources Institute. This work is licensed under the Creative Commons Attribution 4.0 International License.  
To view a copy of the license, visit http://creativecommons.org/licenses/by/4.0/
10 G Street, NE  |  Washington, DC 20002  |  www.WRI.org
ACKNOWLEDGMENTS
This Tool and research were supported by the FedEx-WRI Mobility and 
Accessibility Program. The authors thank Cristina Albuquerque, Matheus Jotz, 
Fabricio Pietrobelli, and Eduardo Siqueira for help in obtaining local data  
on Brazil and improving the calculations and methodology of the Tool to fit  
local needs. 
The authors are grateful to peer reviewers Suarez Jorge Augusto, Sebastian 
Castellano, Subrata Chakrabarty, Tim Dallmann, Helen Ding, Marine Gorner, 
Alejandro Guerrero, Robin King, Anjali Mahendra, Felix Jacob Santiago Sanchez, 
and Su Song, who provided insightful suggestions to improve the Tool and 
the technical note. They also thank Maria Hart, Romain Warnault, Barbara 
Karni, Caroline Taylor, and Lauri Scherer for their valuable assistance with the 
publication and editorial process and Jenna Park for her support with graphics, 
design, and layout.
ABOUT THE AUTHORS
Erin Cooper is a former associate working on transportation and climate at the 
WRI Ross Center for Sustainable Cities program.
Erin Kenney is a former research intern with the WRI Ross Center for Sustainable 
Cities program.
Juan Miguel Velásquez  is a former senior associate transport planner with  
the WRI Ross Center for Sustainable Cities program.
Xiangyi Li  is a research analyst with the WRI China and Ross Center for 
Sustainable Cities program.
Thet Hein Tun  is a transport research analyst with the WRI Ross Center for 
Sustainable Cities program.
Contact: thet.tun@wri.org
