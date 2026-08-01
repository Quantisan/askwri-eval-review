---
doc_id: 2025_financial-impact-assessment-for-zero-emission_8156
source_pdf: kp-docs/askwri-kps/2025_financial-impact-assessment-for-zero-emission_8156.pdf
extraction_method: cache-plaintext
char_count: 66277
title: Financial Impact Assessment for Zero-Emission Trucks (Fi-ZET)
authors: Patki, Sharvari; Polisetty, Manojna; Ramaprasad, Vishal; Mir, Waseem; Mulukutla, Pawan
date_published: 8/14/2025
article_type: Technical Note
sub_tag: Transport decarbonization
wri_primary_office: WRI India
wri_programs: Cities
language: English
url: "https://wri-india.org/research/financial-impact-assessment-zero-emission-trucks-fi-zet"
doi: No DOI listed
summary: The MS Excel-based tool ‘Financial Impact Assessment for Zero-Emission Trucks (Fi-ZET) has been developed to assess the financial viability of replacing a diesel-powered internal combustion engine (ICE) truck with a zero-emission electric truck (ZET). The tool is a flexible, transparent, and user-friendly solution for conducting a preliminary financial comparison between an electric truck and a diesel truck.
---

# Financial Impact Assessment for Zero-Emission Trucks (Fi-ZET)

TECHNICAL NOTE   |  July 2025  |  1
WR I IN DI AWR I IN DI A
WR I IN DI AWR I IN DI A
TECHNICAL NOTE
Financial Impact Assessment for  
Zero-Emission Trucks (Fi-ZET)
A tool for comparative feasibility analysis of a single zero-emission 
truck (ZET) and an internal combustion engine (ICE) truck
Sharvari Patki, Manojna Polisetty, Vishal Ramaprasad, Waseem Mir, and Pawan Mulukutla
CONTENTS
Introduction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1
How to use the Fi-ZET tool  .............. 5
Behind the curtain: how the tool works 9
Future enhancements  ................... 11
Caveats .................................. 12
Disclaimer ............................... 12
Appendix. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .13
Endnotes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
References ............................... 21
Acknowledgments ....................... 21
About the authors. . . . . . . . . . . . . . . . . . . . . . . 24
Technical notes document the research or analytical 
methodology underpinning a publication, interactive 
application, or tool.
Suggested Citation: Patki, S., M. Polisetty, V. 
Ramaprasad, W. Mir, and P . Mulukutla. 2025. 
“Financial Impact Assessment for Zero-Emission 
Trucks (Fi-ZET).” Technical Note. New Delhi: 
WRI India. Available online at doi.org/10.46830/
writn.24.00053.
Abstract
The Financial Impact Assessment for Zero-Emission Trucks (Fi-ZET) tool is 
designed to offer a comparative feasibility assessment to truck owners and 
fleet operators considering a transition from internal combustion engine 
(ICE) trucks to zero-emission electric trucks (ZET). Based on Microsoft 
Excel, the tool evaluates critical financial outputs, such as payback period 
and total cost of ownership, and compares the unit economics of running a 
ZET (e-truck) with that of an ICE truck (diesel truck). A route-level analysis 
offers a granular understanding of the operational and financial viability. 
As the Fi-ZET tool ensures adaptability to evolving market conditions 
while aligning with the sustainability goals of shippers and fleet owners, it 
alleviates uncertainty among potential buyers and builds confidence.
The Fi-ZET tool empowers stakeholders with actionable insights, facilitating 
data-driven decisions that can accelerate the confident adoption of ZETs in 
India’s freight sector. Policymakers may use Fi-ZET to test different scenarios, 
assess policy incentives, and make informed decisions based on data.
Introduction
Motivation
India’s logistics sector relies on road freight for over 71 percent of its goods 
movement (NITI Aayog 2021). While trucks represent a mere 3 percent 
(NITI Aayog 2022) of the total vehicle fleet,  they are responsible for a 
staggering 73.5 percent of India’s diesel consumption (Mattoo and Saxena 
2023) and 53 percent of particulate matter (PM) emissions (Figure 1) (NITI 
Aayog 2022). The logistics sector’s reliance on trucks translates to significant 
pollution-related challenges, especially considering that the road freight 
sector is projected to grow fourfold by 2050 (NITI Aayog 2022).

2  |  WR I IN DI AWR I IN DI A
  
However, air pollution is not the only challenge that the 
logistics sector is facing; dependence on oil imports and 
operational costs are significant challenges, too, and adopting 
zero-emission trucks (ZETs) serves as a key enabler in 
tackling these challenges.
Curb air pollution: The widespread adoption of ZETs could 
result in the reduction of emissions of cumulative truck-
related PM and nitrogen oxides (NOx) by nearly 40 percent 
by 2050 (NITI Aayog, RMI, and RMI India, 2022). The 
resulting improvement in air quality would benefit the health 
of millions of Indian citizens.
Reduce dependence on oil imports: Switching to ZETs 
could lead to cumulative savings of 838 billion liters of diesel 
by 2050, translating to a saving of a staggering ₹116 lakh crore 
(~ $1.5 trillion) on oil expenditure (NITI Aayog, RMI, and 
RMI India 2022). Transitioning to ZETs could dramatically 
decrease India’s reliance on imported diesel fuel and, thus, 
strengthen India’s energy security.
Lower operational costs for fleet owners: Upfront 
costs might be higher for e-trucks, but they require less 
maintenance than ICE trucks and consume less energy. Over 
time, the cost saving translates to a substantial long-term 
economic advantage for fleet owners and operators.
The case for transitioning to e-trucks is both environmental 
and economic, particularly as regulations tighten and the 
logistics sector faces growing pressure to reduce emissions. 
However, challenges specific to e-trucks—such as high 
upfront costs, rapidly evolving technology, and uncertainties in 
financial feasibility—pose significant barriers to adoption.
To help navigate these barriers, Fi-ZET was developed 
primarily to provide fleet owners,2  shippers,3  and other truck 
operators with essential insights into the financial viability 
of transitioning from an ICE truck to an e-truck. It enables 
detailed evaluation of financial and operational aspects.
Fi-ZET equips users with a granular understanding of key 
financial metrics, including payback period, total cost of 
ownership (TCO), earnings, and cash flow analysis. It further 
models critical elements such as electric vehicle (EV) charging 
costs, debt structures, and potential revenue variations, 
helping users make informed decisions that balance financial 
performance with environmental goals.
Additionally, Fi-ZET serves as a valuable tool for 
policymakers by simulating the impact of different policy 
scenarios on e-truck adoption. This enables data-backed 
decision-making for designing incentives and regulations 
that encourage widespread e-truck adoption and help drive a 
sustainable, low-carbon road freight sector.
Objectives of Fi-ZET
Fi-ZET aims to generate a comparative feasibility assessment 
for the electrification of trucks in India’s road freight sector. 
Its overarching objective is to evaluate the financial viability of 
running an e-truck in place of a diesel truck by undertaking a 
route-level analysis and comparing the unit economics.
The tool integrates financial levers (like financing options and 
tax implications) while adapting to market dynamics (such 
as energy prices and battery costs) and offers a responsive 
framework for shippers and fleet operators to adapt to 
evolving market conditions. The analysis culminates in key 
output metrics: payback period, TCO, net earnings, and 
discounted cash flows (DCF).4 
Payback period is the time it will take for an investment 
to break even (recover all the money invested). This crucial 
metric helps gauge and compare profitability between a diesel 
truck and an e-truck while offering stakeholders insights into 
key factors affecting profitability.5 
TCO, expressed in INR per km, facilitates a comprehensive 
financial view of a truck’s lifecycle costs by encompassing 
capital, and operational, expenses. By quantifying cost 
per kilometer, the tool provides a comparative TCO 
analysis and helps assess the financial differences between 
diesel and e-trucks.
Figure 1  |   Emissions from trucks are disproportionate 
to their share of the vehicle fleet in India’s 
road freight sector  
Source: NITI Aayog (2022).
Trucks
Others
Truck Share in 
India’s Vehicle Fleet
PM emissions  
of trucks
3%
53%

TECHNICAL NOTE   |  July 2025  |  3
Financial Impact Assessment for Zero-Emission Trucks (Fi-ZET)
Net earnings provides an estimate of a vehicle’s total income 
over its lifetime. It considers key factors such as loan interest, 
depreciation, and taxes. This helps stakeholders understand 
how different inputs affect the financial differences between 
diesel and e-trucks.
Discounted cash flow (DCF): Cash flows represent the 
projected future inflows and outflows of cash associated with 
an investment. The DCF reflects the present value of each 
year’s future cash flows discounted at a specific rate. The 
present value of cash flows (PVCF) is the sum of all DCFs 
over the entire period. The metrics help stakeholders assess the 
long-term financial performance of the investment.4
Uniqueness of the tool 
The Fi-ZET tool, customized for India and customizable for 
both ICE trucks and e-trucks, offers a comprehensive financial 
analysis, sensitivity analysis, and range of financial levers.
Comprehensive financial analysis: The tool assesses a broad 
spectrum of metrics—including payback periods, TCO, 
annual cash flows, and net earnings—over the holding period, 
providing a nuanced understanding of financial performance. 
Its unique features include customizable financial assumptions 
such as debt and equity structures, integration of policy levers, 
real-time output updates, and advanced depreciation methods. 
Additionally, it enables users to model diverse scenarios, 
reflecting specific operational conditions like changes in 
energy costs, battery expenses, or tire replacements, making it 
a robust and adaptable feasibility modeling tool.
Sensitivity analysis: The tool enables users to conduct a 
detailed sensitivity analysis6 on key parameters such as interest 
rates, toll expenses, year-on-year operational cost increases, 
and capital structure. Additionally, it incorporates the ability 
to factor in various policy and technological developments, 
allowing users to create different scenarios and perform 
robust evaluations across diverse conditions. These include 
policy conditions such as subsidies and tax incentives, as well 
as technological advancements like improvements in battery 
efficiency, reductions in energy costs, and innovations in 
charging infrastructure.
Truck customization: Designed for both ICE and e-trucks, 
the tool incorporates relevant features for every truck 
category.7 These include battery replacement schedules, battery 
size, and charging infrastructure costs for e-trucks, and general 
parameters like gross vehicle weight (GVW) and number 
of tires applicable to both. This ensures accurate financial 
modeling for all truck types.
Policy levers: Fi-ZET includes a range of policy options, 
allowing users to simulate the impacts of capital incentives,8  
operational subsidies,9  and other government support 
measures on financial viability.10 
Local context consideration: Specifically designed for the 
Indian market, the tool allows users to input and adjust local 
variables that often vary across states, such as road taxes, 
electricity power factors, and so on, ensuring subnational-level 
contextualization (see the Sources section of the tool for data 
source information).
User-friendly with transparent assumptions: The tool is 
designed to be accessible and easy to use, with preloaded 
default values that can be customized. All assumptions and 
methodologies are clearly explained for full transparency.
The tool provides an optional module for editing detailed 
inputs. It offers customizable analysis periods, user-defined 
truck specifications, and detailed input parameters. The tool’s 
flexible approach ensures transparency in assumptions and 
enables users to tailor factors such as taxes, resale values, 
crew costs, and financing. Additionally, Fi-ZET includes a 
dedicated policy levers module to model incentives, subsidies, 
and taxes—enabling deeper, more decision-relevant financial 
assessment for e-truck adoption.
The Fi-ZET tool enables fleet managers, policymakers, and 
other stakeholders in the Indian trucking ecosystem to make 
well-informed, data-driven assessments of the viability of 
transitioning to e-trucks under diverse market conditions.
Potential use cases for Fi-ZET
The Fi-ZET tool is designed to assist a range of 
stakeholders—logistics service providers (LSPs), 11 fleet 
managers, shippers, policymakers, and academic researchers. 
By utilizing Fi-ZET , these entities can identify associated 
financial challenges and opportunities, ultimately 
facilitating data-driven, informed decision-making and 
policy formulation.
This includes, but is not limited to, the following use cases:
 ▪ Financial feasibility analysis for fleet electrification: Fleet 
managers and LSPs can leverage Fi ZET to conduct 
detailed financial comparisons of e-trucks against 
their equivalent diesel counterparts, enabling strategic 
operational planning and informed decision-making 
regarding the viability of adopting e-trucks.
 ▪ Sustainability assessment for shippers: The tool enables 
shippers that own and operate their own fleets to assess 
the economic viability and environmental benefits of 
integrating e-trucks into their supply chains and the 
potential green premium for reducing Scope 1 emissions.12 
 ▪ Evidence-based policy formulation: Policymakers can 
employ the tool to create data-driven scenarios that 
analyze the impact of various policy levers on the TCO 
for e-trucks and support the development of effective 
regulations and incentive mechanisms.

4  |  WR I IN DI AWR I IN DI A
  
 ▪ Academic research and analysis: Researchers focused on 
freight decarbonization and sustainable logistics can utilize 
the tool for comprehensive analysis and contribute to the 
academic discourse on the financial aspects of e-truck 
adoption and its implications for the logistics industry.
Development approach
As the market for e-trucks is still nascent, truck owners 
face uncertainty over the costs and benefits of transitioning, 
especially given their specific operational requirements, 
which slows down decision-making. Pilot conversations 
and discussions with fleet operators and truck owners under 
the Electric Freight Accelerator for Sustainable Transport 
(e-FAST) initiative revealed a significant gap in their 
understanding of the financial viability of diesel trucks versus 
e-trucks and the need for tailored financial analysis to address 
their unique operational needs. To address this gap, the 
concept of developing a comparative feasibility assessment 
tool that provides a tailored approach to analyzing the 
financial implications of e-truck ownership emerged.
With road freight decarbonization gaining momentum, a 
few TCO tools for e-trucks—C40’s TCO Tool for Electric 
Freight, World Resources Institute’s TCO Evaluator Tool, 
CoEZET’s TCO Estimator Tool—have emerged. However, 
the trucking sector is highly dependent on commercial 
viability, and TCO alone is not sufficient. By incorporating 
not only TCO but also critical financial metrics like 
payback period, earnings, and full financial statements, 
Fi-ZET stands apart. 
Most market tools focus primarily on TCO, often ignoring 
other financials like payback periods and cash flows. A 
comprehensive tool is particularly important to assess how 
quickly high upfront costs can be recovered through business 
operations. Additionally, many tools do not integrate detailed 
parameters like daily trip frequency, payload utilization, and 
financing structures—gaps that Fi-ZET addresses by offering 
a comprehensive analysis for e-trucks.
Conceptualization of Fi-ZET
Primary stakeholders and objectives: Fi-ZET is tailored 
for the use of truck owners and fleet operators, the primary 
decision-makers in adopting e-trucks. The tool focuses on the 
unit economics of a single truck and enables stakeholders to 
delve into the financial and operational specifics of individual 
vehicles. The tool has the ability to input truck configurations 
based on GVW and offers detailed, truck-level analysis to 
support informed financial decisions. Fi-ZET addresses a few 
critical questions:
 ▪ When will the investment in an e-truck start to break even 
compared to a diesel truck?
 ▪ How will switching to an e-truck impact an individual 
truck’s profitability over the next few years?
 ▪ What financial advantages or disadvantages will arise 
considering upfront costs and long-term savings?
 ▪ How do specific operational patterns affect the financial 
performance of an e-truck versus a diesel truck?
 ▪ How will incentives influence the financial 
assessment of an e-truck?
User feedback on Fi-ZET: The primary stakeholders 
consulted during the development process were original 
equipment manufacturers (OEMs),13  shippers, and LSPs. We 
conducted detailed demonstrations of the draft tool, and at 
multiple stages, to enable the stakeholders to review the tool’s 
analysis results and provide feedback.
Leveraging their industry expertise, the stakeholders refined 
a variety of parameters to enhance the tool’s functionality, 
usability, accuracy, and practical relevance. Based on their 
extensive inputs and feedback, we made several adjustments 
to the tool’s design and functions; for example, while annual 
TCO was initially emphasized due to its importance in 
understanding the long-term decreasing cost of ownership, 
some stakeholders preferred the average TCO for simplicity, 
and we incorporated both options to accommodate the 
diversity of needs.
The feedback from identified potential users was central 
to the development of Fi-ZET , and it ensured that the 
tool is relevant and usable. Since Fi-ZET is developed in 
collaboration with stakeholders, the tool is well-positioned to 
meet the practical needs of its users.
Platform selection: Excel was found to be the best-suited 
platform for the application because of its popularity across 
a cross-section of potential users, easy accessibility, sufficient 
flexibility, user-friendliness, transparency of assumptions, and 
comprehensive suite of functions.
Deployment and user engagement: To maximize the 
tool’s reach and impact, intermediaries such as consultants, 
associations, and NGOs can play a vital role in facilitating 
its usage. They can assist truck owners by using the tool to 
analyze financial scenarios and present results, given the 
particularly complex and competing interests between diesel 
dealers and e-truck dealers. The insights provided by the 
tool can be integrated into awareness campaigns aimed at 
motivating stakeholders, particularly truck owners and fleet 
operators, to adopt e-trucks.

TECHNICAL NOTE   |  July 2025  |  5
Financial Impact Assessment for Zero-Emission Trucks (Fi-ZET)
How to use the Fi-ZET tool
Download the Excel file of Fi-ZET from WRI India’s 
Electric Mobility practice area page.
Run the tool on a Windows device with an active Microsoft 
Office license (Office 2016 or later recommended). The tool is 
not fully compatible with macOS.
The Excel file may open in ‘Read Only’ mode — click the 
Edit button to enable full interaction.
Some tool features rely on macros — click “Enable Content” 
to allow macros in “Trust Settings” after opening the file.
If the text is difficult to read, use the Zoom function in Excel 
to adjust your view.
Begin with reading the User Guide for tool description and 
usage instructions, then click Start to access the User Inputs 
and Output Dashboard.
The User Inputs and Output Dashboard has user inputs 
zone on its left and output graphs zone on its right. Upon 
opening, the sheet shows with a built-in reference case using 
preset values for all parameters to showcase a representative 
realistic scenario.
Upon reviewing the existing inputs, the user can
 ▪ edit specific parameters as required;
 ▪ click to clear Preset V alues to remove all parameters, set 
inputs to a blank state, and enter preferred values; or
 ▪ click to restore Preset V alues.
Refer to the output zone in the User Inputs and Output 
Dashboard for results on key metrics, including payback 
period, TCO, earnings, and cash flow.
Choose the Secondary Inputs button for additional inputs 
or the Policy Levers button for policy analysis based on the 
desired deep dive.
Use the Print Output button to save the outputs.
Download and read the Fi-ZET Technical Note for more 
information, including the applied methodology.
Inputs
The User Inputs and Output Dashboard (Figure 2) is the main 
interface of the tool. The input values are color-coded for 
clarity: green cells are editable inputs, blue cells are optional 
pre-filled inputs, and gray cells are fixed and non-editable.This 
step-by-step approach allows users to progress from general 
inputs to more detailed configurations.
 ▪ User Inputs and Output Dashboard: The page opens with 
pre-filled Preset Values to demonstrate a reference case and 
help users understand its functionality. Users can modify 
the preset inputs to suit their requirements. Based on the 
changes, the output metrics update dynamically. 
     The Click to clear Preset V alues button at the top of the      
     page clears all values, leaves the fields blank, and lets the  
     user start afresh. The Click to reset Preset V alues button,  
     also at the top and to its right, restores the original inputs.
     Buttons link to two additional input sheets— Secondary  
     Inputs and Policy Levers—for interested users.
Secondary Inputs: An optional input sheet (Figure 3) 
contains assumptions that adjust dynamically based on the 
user’s inputs into the User Input and Output Dashboard. Users 
can review and, if needed, override these to enter case-
specific inputs.
Policy levers: In this section, tailored to specific research 
objectives, users can modify incentive-related variables 
to assess their impact on the financial metrics of 
ZETs (Figure 4).
Users should be mindful that several input parameters are 
interdependent factors and can significantly influence each 
other. In e-trucks, for example, battery size, GVW, and 
payload are closely linked—changing one may impact the 
others. Similarly, in diesel trucks, adjustments to GVW affect 
payload capacity. Additionally, the tool assumes a single 
ownership cycle and allows a maximum holding period of up 
to 15 years; it does not model multiple life cycles.
The data entry structure of the input sheets is streamlined 
and standardized. Each category’s inputs are subcategorized. 
All Fi-ZET input sheets use two categories of data input: 
Capital Parameters and Operating Parameters (Table 1; see all 
input parameters in comprehensive detail in Table A-1 to A-3 
in the Appendix).

6  |  WR I IN DI AWR I IN DI A
  
Figure 2  |   Landing page of Fi-ZET — “User Guide”  
Note: The purpose of this figure is to help in referring to the landing page of the Excel tool.
Source: Financial Impact Assessment for Zero Emission Trucks (Fi-ZET) tool developed by WRI India.

TECHNICAL NOTE   |  July 2025  |  7
Financial Impact Assessment for Zero-Emission Trucks (Fi-ZET)
Figure 3  |   A sample “User Input and Output Dashboard” page  
Note: The purpose of this figure is to help in referring to the landing page of the Excel tool.
Source: Financial Impact Assessment for Zero Emission Trucks (Fi-ZET) tool developed by WRI India.
Table 1  |  Input sheets and their data categorization  
SHEET BROAD CATEGORIES SUB CATEGORIES
GENERAL INFORMATION
User inputs and output 
dashboard
Capital parameters Vehicle upfront cost, battery and charging inputs, capital structure
Operating parameters Operating characteristics, operating expenses, revenue details
Secondary input sheet Capital parameters Vehicle upfront cost, battery and charging inputs, capital structure, other capital inputs
Operating parameters Operating characteristics, operating expenses, revenue details
Policy levers Capital subsidies Road tax waiver, demand incentive, charging infrastructure waiver
Operating subsidies Toll waiver, subsidized electricity tariff, interest subvention
Source: Financial Impact Assessment for Zero Emission Trucks (Fi-ZET) tool developed by WRI India.

8  |  WR I IN DI AWR I IN DI A
  
Figure 4  |   Snapshots of optional input sheets - “Secondary Input Sheet” and “Policy Levers”  
Secondary Inputs Policy LeversSecondary Inputs Policy Levers
Note: The above figure is a collation of snapshots of a few pages of the Excel Tool.
Source: Financial Impact Assessment for Zero Emission Trucks (Fi-ZET) tool developed by WRI India.

TECHNICAL NOTE   |  July 2025  |  9
Financial Impact Assessment for Zero-Emission Trucks (Fi-ZET)
Outputs
The User Inputs and Output Dashboard has an output zone 
on the right that displays real-time graphs of two key output 
metrics (payback period and TCO) and two supporting 
output metrics (net earnings and DCF).
 ▪ Payback period: The output zone begins with the 
comparative bar graph of payback periods for e-truck and 
diesel truck in months.
 ▪ TCO: The line graph illustrates the annual TCO in INR 
per kilometer for both e-trucks and diesel trucks. The 
graph also highlights the crossover year when the TCO for 
e-truck becomes cheaper than for a diesel truck. Adjacent 
to the line graph, the average TCO graph displays TCO 
for the entire lifespan of both e-trucks and diesel trucks.
Below the TCO chart are side-by-side graphs of two sup-
porting output metrics: earnings and cash flow at the net 
present value (NPV).
 ▪ Net earnings: A bar chart compares the annual earnings 
of a diesel truck and an e-truck during the holding period. 
An info-panel shows the total earnings over the holding 
period and the percentage difference in net earnings 
between an e-truck and a diesel truck.
 ▪ Discounted cash flows (DCF): The tool displays the 
DCF as a bar chart that compares the annual discounted 
cash flow over the holding period for both an ICE 
truck and an e-truck. Below the bar chart an info-panel 
shows the PVCF as a consolidated figure and also a 
percentage difference in cash flow between an e-truck and 
a diesel truck.
Click to view Financial Statements beneath both charts for a 
deep dive into the financial statement.
Behind the curtain: how the tool 
works
Figure 5 details the work flow of the Fi-ZET tool. 
Fi-ZET is designed to assess the financial feasibility of 
transitioning an individual truck to an e-truck, providing 
detailed, truck-specific financial analysis. It focuses on single-
vehicle scenarios rather than fleet-wide transitions.
Financing model assumptions
The current version of the tool processes inputs to generate 
financial outputs in detail based on two assumptions. The 
owner procures trucks only through debt financing and 
finances battery replacements through debt.
Captive charging infrastructure is used; opportunity 
charging is excluded. 
Methods for calculating output metrics
The key output metrics are annual earnings, DCF, payback 
period, and TCO. 
Annual earnings
Objective: To reflect the asset’s net income after accounting 
for all expenses, interest, and taxes within the holding 
period of the truck.
Process: To calculate earnings, a profit and loss (P&L) 
statement is constructed that summarizes the financial 
performance over a given period.
 ▪ Revenue: Begin by recognizing income from the asset’s 
operations; that is transport services.
 ▪ Operational expenses: Subtract direct costs like electricity, 
maintenance, and so on, to calculate gross profit, also 
referred to as earnings before interest, tax, depreciation, 
and amortization (EBITDA).14 
 ▪ Earnings before interest and taxes (EBIT): Further 
reduce gross profit by the depreciation of the truck. This 
metric provides operational profitability before interest and 
taxes are deducted.
 ▪ Profit before taxes (PBT): Deduct equated monthly 
installments (EMI) on loans to arrive at PBT .
 ▪ Net earnings: Deduct applicable taxes from PBT to 
determine net earnings. The metric is used in further 
financial analysis, such as calculating payback.
DCF
Objective: To assess future cash inflows and outflows 
and evaluate financial liquidity by factoring in the time 
value of money.
Process: Calculated by tracking all cash inflows and outflows 
to determine the net change in cash and the closing cash 
balance over the holding period.
 ▪ Operating cash flow: Add back depreciation to 
net earnings to reflect the actual cash generated 
from operations.
 ▪ Investing cash flow: Account for cash inflows and 
outflows related to investing activities; for example, 
acquisition of the truck and battery for battery 
replacements and resale proceeds.
 ▪ Financing cash flow: Include cash inflows from 
borrowings and cash outflows for debt repayments.

10  |  WR I IN DI AWR I IN DI A
  
Vehicle Upfront Cost Inputs
Battery & Charging Inputs
 
Financing Structure
Operational Characteristics
 ■ Onward Revenue distance
 ■ Return Revenue distance
 ■ Dead km per trip
 ■ Onward payload utilization
 ■ Return payload utilization
 ■ How often does the vehicle return 
without load?
 ■ No. of trips per day (manual entry)
 ■ Mileage with payload
 ■ Mileage without payload
 ■ Degradation of mileage
Operational Expenses
 ■ Toll charges per trip
 ■ Cost of Energy
 ■ Annual cost of maintenance
 ■ Number of Tyres
Revenue Details
 ■ Revenue as per contract
 ■ Revenue rate for onward load
 ■ Revenue rate for return load
 ■ Annual escalation in revenue
Operational Characteristics
 ■ Time taken to cover onward distance
 ■ Time taken to cover return distance
 ■ Charging and rest time
 ■ Gate-to-Gate time 
 ■ Working days a month
 ■ Operational months in a year
Operational Expenses
 ■ Annual insurance premium
 ■ 5-year periods 
 ■ Annual cost of AMC
 ■ Annual maintenance cost (if no AMC)
 ■ Maintainace cost in addition to AMC
 ■ Crew cost 
 ■ Admin cost 
 ■ Cost of one tire
 ■ Life of tire
 ■ Retreading required after
 ■ Second life after retreading
 ■ Cost of retreading tires
 ■ Ad Blue Consumption per trip
 ■ Ad Blue Cost per liter
YoY Increase 
 ■ Crew Cost 
 ■ Admin Cost
 ■ Fuel Cost
 ■ Direct Tax
Secondary Input Sheet 
Vehicle Upfront Cost Inputs
Battery Cost per kWh
Financing Structure
 
 
Other Financial Inputs 
Policy Levers 
Capital Subsidies
Operational Subsidies
Figure 5  |   Overview of the functioning of the tool  
Source: WRI India authors.
General
Info.
Capital
Parameters
Operational 
Parameters
User Input and 
Output Dashboard
Derived 
Financial Statements TCO Master
Statewise Road Tax, Electricity
Interest ComponentAnnual Calculations
Payback Master
User Input and Output Dashboard
 ■ Vehicle Cost
 ■ Battery Cost (for e-truck)
 ■ Trailer Cost (if Tractor Trailer)
 ■ Registration Fees
 ■ Other Costs at Registration
 ■ Road Tax (Manual Input)
 ■ Road Tax Waiver
 ■ Demand Incentive
 ■ Battery Capacity Based Subsidy 
 ■ Vehicle Cost Based Cap
 ■ Fixed Subsidy Cap
 ■ Charging Infrastructure Waiver
 ■ ZET Toll Waiver
 ■ Amount of subsidy
 ■ Time period of subsidy
 ■ Subsidized Electricity Tariff
 ■ Subsidized on Energy Cost for e-truck
 ■ Waiver on increase in cost of 
electricity provided
 ■ Time period of subsidy
 ■ Interest Subvention
 ■ Battery Life in km
 ■ Battery Resale Proportion
 ■ Charger Cost
 ■ No. of Chargers
 ■ Upstream electricity cost
 ■ Total Fleet Size
 ■ No. of installments per year
 ■ Moratorium period 
 ■ Upfront received by shipper
 ■ Recovery period of upfront
 ■ Cost of Equity (Opportunity Cost)
 ■ Vehicle resale proportion
 ■ Depreciation Model
 ■ Value of X in case of Accelerated 
Depreciation Model
 ■ Battery Capacity
 ■ Downpayment
 ■ Loan Interest rate
 ■ Loan Tenure
 ■ Vehicle’s Holding Period
 ■ State of Purchase Gross Vehicle Weight 
(GVW) Vehicle Payload Capacity

TECHNICAL NOTE   |  July 2025  |  11
Financial Impact Assessment for Zero-Emission Trucks (Fi-ZET)
 ▪ Net cash flow: Determine net cash flow by summing 
operating cash flow, investing activities, and 
financing activities.
 ▪ Discounted cash flow (DCF): Calculate DCF by 
discounting the net cash flow for each year using 
a discount rate.
Payback period
Objective: Measure the time required for the investment in a 
truck to recoup its initial cost through monthly cash flows.
Process: Monthly cash flows are analyzed and the cumulative 
cash flow tracked until it matches or exceeds the initial 
investment. The payback period is then calculated as the 
number of months needed for the total cash flow to break 
even with the original investment.
 ▪ Average monthly DCF is calculated by dividing the 
NPV of annual net cash flows by 12 to derive the average 
monthly cash flow. The cumulative cash flow is then 
tracked by adding the average monthly cashflows to the 
previous cumulative total, at year 0, which reflects the 
outflow from initial investment.
TCO
Objective: Calculate overall cost of owning and operating a 
vehicle over its lifetime, expressed in INR per kilometer.
Annual TCO: This method annualizes capital and operating 
costs and expresses them per kilometer for an average 
operational year.
Process: First, capital expenditure (CAPEX)15  is adjusted 
by subtracting the expected resale value and factoring in the 
present value. This adjusted CAPEX is then annualized using 
the capital recovery factor (CRF).16  The result is added to 
the annual operating expense. Finally, the annual operating 
expense is divided by the annual travel distance to determine 
the cost per kilometer.
 ▪ The CAPEX component is the sum of all the upfront 
capital costs of the truck, including initial truck costs, 
registration, road tax, charging infrastructure, total interest 
on debt, and battery replacement costs.
 ▪ The annual present value factor (PVF)17  is 
calculated to discount the expected resale value to its 
present-day equivalent. 
 
 
where i represents the periodic interest rate and n the year 
of calculation. This ensures future values are adjusted to 
present-day financial terms.
 ▪ The annual capital recovery factor (CRF) is calculated 
to convert the adjusted CAPEX into equivalent 
annual payments and ensure that the allocation for 
capital recovery is consistent throughout the truck’s 
operational life. 
 
 
 
where i represents the periodic interest rate and n denotes 
the year of calculation.
 ▪ The annual operating expenditure (OpEx)18 is calculated 
through the rolling average of annual fixed and variable 
OpEx costs to factor in all past operational costs and 
reduce volatility. For each year, add the OpEx of all 
previous years and the current year and divide by the 
number of years included in the calculation to calculate the 
cumulative average of OpEx costs.
Average TCO: This method evaluates the total lifetime cost 
of owning and operating the truck to account for the time 
value of money throughout the holding period.
Process:
 ▪ Calculate the total operating costs expected over the 
vehicle’s life and discount them to their present value.
 ▪ Similarly, discount the projected resale value 
to present value.
 ▪ Sum the initial capital cost and the discounted OpEx, then 
subtract the discounted resale value.
 ▪ Divide this net total by the expected total kilometers the 
truck will travel over its lifetime to determine the average 
cost per kilometer.
Future enhancements
To keep the Fi-ZET tool relevant and useful in the 
future, enhancements and additional analyses will be 
required, such as: 
 ▪ Collaboration with OEMs, trucks owners, shippers, and 
LSPs will help to update and refine the tool continually to 
meet the evolving needs of the market.
 ▪ Incorporation of support for assessing the financial and 
operational feasibility of upcoming technologies such 
as fuel cells; for example, by including hydrogen-based

12  |  WR I IN DI AWR I IN DI A
  
solutions alongside battery-electric technologies, the 
tool can cater to future developments in sustainable 
transportation and provide insight into their 
long-term viability.
 ▪ Integration of mechanisms to account for advancements 
in battery technologies, such as declining battery costs and 
increased energy densities, to allow users to anticipate how 
technological progress and innovative operational methods 
could impact the TCO and profitability of e-trucks.
 ▪ Adaptation of the tool for use in other regions 
by incorporating region-specific data and 
regulatory frameworks.
 ▪ Expansion of the tool’s capabilities beyond individual 
truck assessments to fleet-wide analysis to offer a 
broader perspective.
Caveats
The approach to formulating and designing the Fi-ZET 
tool is well-considered, user testing is thorough, and 
troubleshooting timely. However, the tool has a few 
limitations (or risks).
Sensitivity to financial assumptions: Fi-ZET incorporates 
user-defined financial inputs, such as interest rates, inflation 
rates, and fuel cost escalations, which are crucial for accurate 
financial projections. While the tool includes illustrative 
default values for these inputs, users should regularly update 
them to reflect actual market conditions and ensure reliable 
long-term analyses.
Limited geographic adaptability: Designed for the Indian 
market, Fi-ZET factors in local costs and regulatory 
frameworks. Using the tool in other regions would require 
context-based customization in user inputs to adapt to 
different regulatory environments, market conditions, and 
operational practices.
Data quality risk: Fi-ZET relies on users to provide a small 
set of mandatory inputs and review or adjust the default input 
values. While detailed guidance is available for users who need 
assistance, the tool cannot control for inaccuracies stemming 
from incorrect data types or invalid input values. This risk 
arises if users input incorrect or incomplete data.
Availability of charging infrastructure: Fi-ZET’s financial 
modeling is based on captive charging solutions by default. 
This reflects the current reality, where high-capacity public 
charging infrastructure—especially for long-haul freight 
operations—is largely absent.
Adoption challenges in the unorganized freight sector: 
Fi-ZET presents strong potential as a decision-support 
tool, but its uptake in India’s freight ecosystem may face 
early challenges. Limited digital literacy and fragmented 
institutional setups in the unorganized freight sector could 
slow adoption. To maximize its impact, the tool will need 
to be supported by targeted outreach, user training, and 
integration into broader policy and industry efforts.
Disclaimer
The purpose of this tool is to enable a comparative financial 
assessment of ICE trucks and e-trucks. This application 
should not be considered a one-stop solution for assessment 
of and/or decision-making regarding an existing or proposed 
project or investment. The functions of the tool and the 
produced results are the sole responsibility of the users of 
this tool. Neither WRI India nor the creators of the tool can 
be held responsible or accountable, directly or indirectly, for 
the use of this tool and/or the results. The tool uses some 
third-party information, the source of which should be 
independently verified by users.

TECHNICAL NOTE   |  July 2025  |  13
Financial Impact Assessment for Zero-Emission Trucks (Fi-ZET)
Appendix
Table A1  |  User Inputs & Output Dashboard  
INPUTS INPUT UNIT INPUT DATA SOURCE GUIDANCE FOR USERS
GENERAL INFORMATION
State of purchase Considered for illustration Use the dropdown cell to choose the state of operation. 
Gross vehicle 
weight (GVW)
Ton IPLT Rhino 55T Specs Enter the truck GVW. The “EV models” reference sheet lists the specifications of 
existing e-trucks in the market.
Vehicle payload Ton IPLT Rhino 55T Specs Enter the effective payload. a The “EV models” reference sheet lists the specifications of 
e-trucks in the market.
CAPEX INPUTS
Vehicle upfront cost
Vehicle cost INR Primary interviews with OEMs Enter the purchase cost of the truck. The “EV models” reference sheet lists the 
specifications of e-trucks in the market.
Battery cost (if 
not included in 
the vehicle cost)
INR - Enter the purchase cost of the battery. If the vehicle cost includes the battery cost, 
enter zero.
Trailer cost (if 
tractor trailer)
INR Primary interviews with OEMs Enter the purchase cost of the tractor trailer. In a case where the vehicle is a rigid body 
trailer, enter zero.
Battery inputs
Battery capacity kWh IPLT Rhino 55T Specs Enter the battery capacity (in kWh). The “EV models” reference sheet lists the 
specifications of e-trucks on the market.
Financial structure
Down payment % Primary interviews with fleet operators Enter a percentage value to input the proportion of equity for the truck.
Loan interest rate % Primary interviews with fleet operators
e-Amrit Financing Options
BankBazaar Commercial Vehicle Loan
Enter the loan interest rate.
Loan tenure Years BankBazaar Commercial Vehicle Loan Enter the loan tenure.
Vehicle’s holding 
period
Years Primary interviews with OEMs and fleet 
operators
Enter the intended duration of ownership or use.
OpEx inputs
Operational characteristics 
Onward revenue 
distance
km Primary interviews with fleet operators Enter the onward distance of a trip (in km) over which revenue will be generated.
Return revenue 
distance
km Primary interviews with fleet operators Enter the return distance of a trip (in km) over which revenue will be generated. 
Dead km per trip km Primary interviews with fleet operators Enter the distance traveled (in km) during each trip without generating revenue.
Onward payload 
utilization
% Primary interviews with fleet operators Enter payload capacity (%) used during the onward journey to generate revenue.
Return payload 
utilization
% Primary interviews with fleet operators Enter payload capacity (%) used during the return journey to generate revenue.

14  |  WR I IN DI AWR I IN DI A
  
Do you want to 
enter the number 
of trips per day 
manually? 
Boolean 
input
Assumed to be Yes Boolean input; in the dropdown menu choose Yes or No to turn on manual entry.
Number of trips 
per day
Number Primary interviews with fleet operators Enter the number of trips made by a truck in a day.
Mileage with 
payload
km/kWh | 
km/liter
 Enter the vehicle’s fuel efficiency (in km per liter or km/kWh) while carrying its full 
payload capacity. 
Mileage without 
payload
km/kWh | 
km/liter
 Enter the vehicle’s fuel efficiency (in km per liter or km/kWh) when not carrying any 
payload.
Degradation of 
mileage
km Primary interviews with fleet operators Enter the YoY decrease in fuel/energy efficiency (%).
Operational Expenses 
Toll charges per 
trip
INR/trip  Mumbai Pune Expressway Toll Enter toll charges. 
Energy cost INR/kWh | 
INR/L
Diesel: April, 2025
CEA Electricity Tariffs EV Charging HT 
Enter the energy cost for e-trucks (in INR per kWh) and for diesel trucks (INR per liter).
Do you have an 
annual tonnage 
commitment from 
the shipper?
Boolean 
Input
 Assumed to be No Boolean input; in the dropdown menu choose Yes or No.
Annual 
commitment by 
shipper
Metric tons - Enter the tonnage (in metric tons) that the shipper is committed to providing annually.
Annual cost of 
maintenance
INR/year Primary interviews with fleet operators Enter the total annual maintenance expenses (in INR). For more granular input options, 
refer to the secondary input sheet.
Tires Number  Number of axles in the truck model Enter the number of tires to calculate tire maintenance cost; to enter more details, go 
to the secondary input sheet.
Revenue details
Revenue rate for 
onward load
INR Primary interviews with fleet operators  Enter revenue rate for onward load.
Revenue rate for 
return load
INR Primary interviews with fleet operators Enter revenue rate for return load.
Annual escalation 
in revenue
% Primary interviews with fleet operators Enter the percentage increase expected in annual revenue.
Table A1  |  User Inputs & Output Dashboard (cont.)
INPUTS INPUT UNIT INPUT DATA SOURCE GUIDANCE FOR USERS
Note: a. The cargo-carrying capacity of a truck is its payload. In an e-truck, the weight of its battery pack reduces its payload, especially when compared to that of a conventional 
diesel truck; the reduction in payload is the e-truck’s payload penalty. The payload after accounting for the payload penalty is the effective payload.
Source: Financial Impact Assessment for Zero Emission Trucks (Fi-ZET) tool developed by WRI India.

TECHNICAL NOTE   |  July 2025  |  15
Financial Impact Assessment for Zero-Emission Trucks (Fi-ZET)
Table A2  |  Secondary Input Sheet  
INPUTS INPUT UNIT INPUT DATA SOURCE GUIDANCE FOR USERS
CAPEX INPUTS
Vehicle upfront cost
Registration fees INR Parivaahan Registration Fees
Assumed value is automated based on 
GVW
Enter registration fees in INR.
Other costs at 
registration
INR Primary interviews with fleet operators
Assumed value is automated based on 
GVW
Enter expenses (apart from fees and taxes) on vehicle purchase.
Do you want to 
input road tax 
manually? 
Boolean 
Input
Assumed to be No Boolean input; in the dropdown menu choose Yes or No.
Road tax (manual 
input)
%  - If you chose Yes in the previous input, manually enter road tax here. 
Battery inputs
Battery cost per 
kWh
INR/kWh Bloomberg Battery Price 2025
Considered value of dollar as INR 85.73 
on 15 April 2025
Enter battery replacement cost (in INR per kWh).
Battery life km EVReporter
Assumed value is automated based on 
battery size
Enter battery life (in km).
Battery resale 
value
% valleyindustrialtrucks.com Enter the battery resale value as a percentage of the battery cost; the resale value is 
considered in calculating the cost of replacing the battery.
Charger cost INR Bengaluru Electric Bus Market Study - Pg 
72
Assumed value is automated based on 
battery size
Enter the cost of the charger (in INR) best suited for the e-truck considered.
Number of 
chargers
Ordinal cell 
type
Assumed to be two In the dropdown menu choose the number of chargers to consider origin and 
destination charging depending on the range of the e-truck and trip length.
Upstream 
electricity cost
INR/kVa Primary interviews with shippers 
and electric vehicle charging station 
operators (EVCS)
Assumed value is automated based on 
battery size
Enter the cost of setting up the charging unit (transformers, cables, etc.) in INR per 
kVa.
Total fleet size 
(considered 
only for cost 
of charging 
infrastructure)
Number Primary interviews s with OEMs Enter the total fleet size to calculate the cost of the charging infrastructure.
Financial structure
Number of 
installments per 
year
Number Considered 12 based on industry 
practice
Enter the number of debt repayment installments.
Moratorium Months SBI Commercial Vehicle Loan Enter the moratorium (in months).

16  |  WR I IN DI AWR I IN DI A
  
Payment 
received by 
shipper upfront
INR  - If the shipper pays the LSP an upfront for procuring electric freight, enter the payment 
(in INR) 
Recovery period 
of upfront 
payment
Years  - If the shipper has funded the initial procurement capital, enter the number of years the 
carrier will take to repay the debt.
Cost of equity 
(opportunity 
cost)
% Assumed to be equal to debt cost The opportunity cost of equity financing is the cost of equity as proportion of the 
vehicle cost; enter it (%).
Other financial inputs
Vehicle resale 
proportion
% Primary interviews with fleet operators Enter the vehicle's expected price at resale or at the end of its useful life as a 
percentage of its purchase cost.
Depreciation 
model
Ordinal cell 
type
Income Tax India Depreciation Rates The dropdown menu lists three depreciation models:
1. straight line, where the asset (vehicle) is depreciated uniformly over its useful life;
2. income tax model, where the asset (vehicle) is depreciated at 30% of the previous 
year’s value throughout the useful life of the vehicle; and
3. accelerated, where a large portion of the asset is depreciated in the first year, 
following which the asset is depreciated using the income tax model. This acts as 
an incentive to reduce tax liabilities in the first year to offset the CAPEX incurred on 
procuring the vehicle.
Choose one.
Value of X in case 
of accelerated 
depreciation 
model
 %  - Enter the depreciation in the first year as the value of x
Other financial inputs
Operational characteristics
Definition of a trip in the tool:
The back-and-forth movement of the vehicle from its point of origin to its destination and back.
Time taken to 
cover onward 
distance
Hours The average speed has been assumed 
to be 30 kmph based on stakeholder 
discussions and supporting sources
Average Speed of Road Cargo in India TOI
Using this information and total distance 
traveled, the time taken is calculated
Enter the time (in hours) the onward distance of the trip takes.
Time taken to 
cover return 
distance
Hours The average speed has been assumed 
to be 30 kmph, based on stakeholder 
discussions and supporting sources
Average Speed of Road Cargo in India TOI
Using this information and total distance 
traveled, the time taken is calculated
Enter the time (in hours) a truck takes to travel the onward distance.
Charging and rest 
time
Hours Based on stakeholder consultations, we 
have assumed that, on average, 80% 
of the battery capacity will be utilized 
for charging; to account for energy loss 
during the charging process, we consider 
charging efficiency is 90%, and we factor 
in an additional hour for rest time
Enter the time (in hours) a truck spends charging and resting.
Gate-to-gate time Hours - (Only for port-led freight movement) enter the time (in hours) a truck takes from arrival 
to departure from the gate. 
Table A2  |  Secondary Input Sheet (cont.)  
INPUTS INPUT UNIT INPUT DATA SOURCE GUIDANCE FOR USERS

TECHNICAL NOTE   |  July 2025  |  17
Financial Impact Assessment for Zero-Emission Trucks (Fi-ZET)
Number of 
working days a 
month
Number Primary interviews with fleet operators Enter the number of days.
Number of 
operational 
months in a year
Number Primary interviews with fleet operators Enter the number of operational months in a year.
Operational expenditure
Annual insurance 
premium
INR Primary interviews s with LSPs Enter the annual insurance premium. 
Do you have 
an annual 
maintenance 
contract (AMC) 
for the vehicle? 
(year 0 to year 5)
Boolean 
input
Assumed to be No Boolean input; in the dropdown menu choose Yes or No.
AMC cost (year 0 
to year 5)
INR  - If Yes, enter the AMC cost (INR) for the first 5 years of the vehicle’s life.
If no AMC, annual 
maintenance 
cost (year 0 to 
year 5)
INR  - If No, enter the annual maintenance cost (INR) for the first 5 years of the vehicle’s life.
Do you have 
an AMC for the 
vehicle? (year 5 
to year 10)
Boolean 
input
 - If No, enter the annual maintenance cost (INR) for the first 5 years of the vehicle’s life.
AMC cost (year 5 
to year 10)
INR  - If Yes, enter the AMC cost (INR) for the next 5 years of the vehicle’s life.
If no AMC, annual 
maintenance 
cost (year 5 to 
year 10)
INR  - If No, enter the annual maintenance cost (INR) for the next 5 years of the vehicle’s life.
Do you have 
an AMC for the 
vehicle (year 10 
to year 15)?
Boolean 
input
 Assumed to be No Boolean input; in the dropdown menu choose Yes or No.
AMC cost (year 10 
to year 15)
INR  - If Yes, enter the AMC cost (INR) for the last 5 years of the vehicle’s life.
If no AMC, annual 
maintenance 
cost (year 10 to 
year 15)
INR  - If No, enter the annual maintenance cost (INR) for the last 5 years of the vehicle’s life.
Maintenance cost 
in addition to the 
AMC
INR Primary interviews s with fleet operators Enter maintenance cost (INR) in addition to the AMC.
Number of 
crew members 
required
Number   
Crew cost per 
month per 
vehicle
INR/month Primary interviews s with fleet operators
Assumed value is automated based on 
trip distance
Enter maintenance cost (INR) in addition to the AMC.
Table A2  |  Secondary Input Sheet (cont.)  
INPUTS INPUT UNIT INPUT DATA SOURCE GUIDANCE FOR USERS

18  |  WR I IN DI AWR I IN DI A
  
Administration 
cost per year 
per vehicle as 
percentage of 
revenue
% Primary interviews s with fleet operators Enter the annual administration cost of a vehicle as a percentage of the revenue 
generated.
AdBlue 
consumption per 
trip (% of diesel)
% Primary interviews s with fleet operators Enter for each trip the consumption of AdBlue as a percentage of diesel consumption.
AdBlue cost per 
liter
INR AdBlue Indiamart If the shipper pays the LSP an upfront for procuring electric freight, enter the payment 
(in INR) 
Port entry fee 
per trip
INR - Enter the port entry fee (INR) per trip.
Cost of one tire INR Commercial Vehicle Tires 
Assumed value is automated based on 
GVW
Enter the purchase cost (INR) of a tire.
Tire life km Primary interviews with fleet operators Enter the distance (km) a tire can travel before it needs retreading.
Kilometers run 
before retreading
km Primary interviews with fleet operators Enter a number value in km to input expected distance a tire can travel before needing 
to retread.
Second life of tire 
after retreading
km Primary interviews with fleet operators Enter a number value in km to input expected distance a tire can travel before 
replacement.
Cost of retreading 
tires
INR Primary interviews with fleet operators Enter the cost (INR) of retreading tires.
Annual increase 
in fuel cost
% Historical increase electricity (considered 
10 years)
Enter the percentage increase in fuel cost expected every year.
Annual increase 
in administration 
cost per vehicle 
(YoY)
% Inflation Focus Economics Enter the annual percentage increase in crew cost.
Annual increase 
in administration 
cost per vehicle 
(YoY)
% Inflation Focus Economics Enter the annual percentage increase in administration cost.
Direct tax (based 
on income or 
profit and paid 
directly to the 
government)
% Income Tax India Direct Tax Enter the distance (km) a tire can travel before it needs retreading.
Do you have an 
annual tonnage 
commitment from 
the shipper?
Boolean 
input
Assumed to be No Boolean input; in the dropdown menu choose Yes or No.
Annual 
commitment by 
shipper
Metric tons - Enter the tonnage (metric tons) that the shipper is committed to providing annually.
Table A2  |  Secondary Input Sheet (cont.)  
INPUTS INPUT UNIT INPUT DATA SOURCE GUIDANCE FOR USERS
Source: Financial Impact Assessment for Zero Emission Trucks (Fi-ZET) tool developed by WRI India.

TECHNICAL NOTE   |  July 2025  |  19
Financial Impact Assessment for Zero-Emission Trucks (Fi-ZET)
Table A3  |  Policy levers 
INPUTS INPUT UNIT INPUT DATA SOURCE GUIDANCE FOR USERS
Does road tax 
waiver apply?
Boolean 
Input
Assumed to be No Boolean input; in the dropdown menu choose Yes or No.
Do you want to 
include capital 
subsidy? 
Boolean 
Input
Assumed to be No Boolean input; in the dropdown menu choose “Yes” or “No” to apply the capital 
subsidy.
The capital subsidy structure follows the PM e-DRIVE scheme for e-buses, as a 
structure for e-trucks is yet to be finalized. The subsidy is determined as the lowest of 
three specified criteria.
Subsidy based on 
battery capacity 
INR per kWh Inputs are based on the PM-eDrive 
Operational Guidelines for e-Trucks 
(2025).
The subsidy cap is inherently linked 
to the Gross Vehicle Weight (GVW) as 
outlined in the guidelines
The calculation adopts the minimum 
of the three specified conditions for 
determining the subsidy, as per the 
official notification
PM-eDrive Operational Guidelines
Enter the subsidy amount in INR per kWh.
Cap based on 
vehicle cost
% of e-truck 
cost
Enter the maximum subsidy as a percentage of the e-truck’s total cost.
fixed subsidy cap INR Enter number value in INR to input absolute subsidy for the e-truck.
Is the charging 
infrastructure 
provided by the 
shipper or the 
government?
Boolean 
input
Assumed to be No Boolean input; in the dropdown menu choose Yes or No to apply toll waiver.
Apply toll charges 
incentive
Boolean 
input
Assumed to be No Boolean input; in the dropdown menu choose Yes or No to apply toll waiver.
Amount of 
subsidy
% Enter percentage value to input discount on existing toll charges.
Time period of 
subsidy
Years Enter the number of years that EVs will attract toll incentives.
Apply incentives 
on cost of 
electricity?
Boolean 
input
Assumed to be No Boolean input; in the dropdown menu choose Yes or No to apply incentives on 
electricity cost.
Waiver on 
increase in cost 
of electricity 
provided
Boolean 
Input
Assumed to be No Boolean input; in the dropdown menu choose Yes or No to apply waiver on increase in 
cost of electricity provided.
Subsidized cost 
of electricity per 
unit
INR - Enter unit cost of electricity.
Time period of 
subsidy
Years - Enter the number of years that electricity will be subsidized for EVs.
Discount on 
interest rate 
% - Enter the discount on the market interest rate.
Source: Financial Impact Assessment for Zero Emission Trucks (Fi-ZET) tool developed by WRI India.

20  |  WR I IN DI AWR I IN DI A
  
Endnotes
1. Trucks carry most of India’s goods, accounting for 70 percent 
of current domestic freight demand. Heavy and medium-duty 
trucks are primarily responsible for freight transportation (NITI 
Aayog, RMI, and RMI India 2022).
2. A fleet owner is an individual or organization that owns, 
operates, and manages a group of trucks used for freight 
transportation.
3. A shipper is a business or individual that requires their goods to 
be transported from one location to another.
4. Discounted cash flow (DCF) represents the present value of 
future cash flows adjusted for time value while net present cash 
flow (NPCF) accounts for cumulative discounted cash flows 
over the entire holding period
5. The payback period is calculated by dividing the investment 
amount by the annual cash flow. Discounted cash flow 
has been used to factor in the time value of money in the 
payback period.
6. Sensitivity analysis helps to understand how independent 
variables affect the output highlight key drivers of impact. 
7. Truck categories refer to the classification of trucks based on 
their gross vehicle weight (GVW), which includes the total 
allowable weight of the vehicle, cargo, passengers, and fuel.
8. The government provides capital incentives in the form of 
financial support (subsidies and tax exemptions, for example) to 
reduce the upfront purchase cost. 
9. Operational subsidies that lower running costs (toll waivers and 
reduced energy tariffs, for example) constitute ongoing support. 
10. In the context of our tool, a policy lever refers to a variable or 
incentive that the user can adjust to assess its impact on the 
output metrics.
11. A logistics service provider (LSP) is a company that manages 
and executes logistics services such as freight transportation, 
warehousing, and distribution for businesses.
12. Scope 1 emissions refer to direct greenhouse gas (GHG) 
emissions from sources that are owned or controlled by 
an organization, such as company-owned vehicles, on-site 
fuel combustion (in boilers and furnaces, for example), and 
manufacturing processes.
13. An OEM manufactures e-trucks, diesel trucks, or components 
such as batteries or drivetrains.
14. Amortization typically refers to the process of writing down 
the value of either a loan or an intangible asset. Intangibles 
are amortized (expensed) over time to tie the cost of the asset 
to the revenues it generates, in accordance with the matching 
principle of generally accepted accounting principles (GAAP).
15. Capital expenditure (CAPEX) refers to the initial costs 
associated with purchasing an truck, including the vehicle’s 
price and any associated infrastructure investments.
16. The capital recovery factor (CRF) is a financial formula used 
to determine the amount of money that needs to be earned 
annually to recover an initial investment over a specified period 
given a fixed interest rate. The CRF is the ratio of a constant 
annuity to the present value of receiving that annuity for a given 
length of time.
17. The present value factor (PVF) is used within the calculation 
of the net present value (NPV) to discount future cash flows to 
their present value. Essentially, PVF helps in determining the 
current worth of future cash flows by accounting for the time 
value of money.
18. Operational expenditure (OpEx) refers to the ongoing costs 
of operating and maintaining a truck—such as energy costs, 
maintenance, and insurance—which are crucial for evaluating 
the tool’s TCO analysis.

TECHNICAL NOTE   |  July 2025  |  21
Financial Impact Assessment for Zero-Emission Trucks (Fi-ZET)
References
Mattoo, R., & Saxena, P. 2023. Fuel Efficiency Improvement and 
Emission Standards in Road Transport.  New Delhi, India: The 
Energy and Resources Institute. Retrieved from https://www.teriin.
org/sites/default/files/2023-08/1692266908Policy%20Brief%20
Fuel%20%20. Efficiency%20Improvement%20Emission%20
Standards.pdf.
NITI Aayog. 2021. Fast Tracking Freight in India. Retrieved from 
https://www.niti.gov.in/sites/default/files/2021-06/FreightReport -
NationalLevel.pdf.
NITI Aayog. 2022. Transforming Trucking in India. Retrieved from 
https://www.niti.gov.in/documents/reports/.
Acknowledgments
The authors would like to thank Harshvardhan Jakher for their key 
contributions toward the conceptualization of the project and for 
helping to get it started.
The authors also extend their heartfelt gratitude to Rohan Rao 
for his invaluable guidance, which ensured that the tool met the 
rigorous standards of other WRI tools. His extensive experience 
with similar WRI products was instrumental in enhancing the detail 
and utility of these sections.
The authors express gratitude to the consulted stakeholders, 
including fleet operators, shippers, OEMs, and academic experts, 
for their valuable input. Their contributions were instrumental 
in developing the framework and finetuning the tool. Consulted 
stakeholders have opted to remain anonymous under the Electric 
Freight Accelerator for Sustainable Transport (e-FAST) platform, 
India’s first national platform dedicated to accelerating freight 
electrification. Their insight into vehicle costs, annual insurance 
premiums, and other key parameters have been essential in 
ensuring that the tool accurately reflects real-world conditions.
The authors are also grateful to the following internal reviewers 
(ordered by surname): Cristina Albuquerque, Sudeshna Chatterjee, 
Arun Krishnan, Aloke Mukherjee, Anuraag Nallapaneni, Shamindra 
Nath Roy, and Priyadarshi Singh for their valuable feedback and 
insights that greatly improved the quality of this work.
Special thanks to the following external reviewers (ordered by 
surname): Mahua Acharya (INTENT Platform), Manish Pandey 
(INTENT Platform), and Aditya Ramji (UC Davis) for their time and 
constructive feedback during the review process.
In addition, the authors gratefully acknowledge the assistance 
provided by The Rewriting Company for copy editing,  Zebra Kross 
for design, Romain Warnault and Karthikeyan Shanmugam for his 
support during the publication of the tool and this technical note.
About the authors
Sharvari Patki  is Program Head, Electric Mobility with the 
Sustainable Cities and Transport program at WRI India
Manojna Polisetty  is Sr. Program Associate with the Sustainable 
Cities and Transport program at WRI India
Vishal Ramprasad  is a Sr. Program Manager with the Integrated 
Transport vertical in the Sustainable Cities and Transport program 
at WRI India
Waseem Mir is a Jr. Program Associate with the Sustainable Cities 
and Transport program at WRI India 
Pawan Mulukutla  is the Executive Program Director—Integrated 
Transport, Clean Air and Hydrogen at WRI India

22  |  WR I IN DI AWR I IN DI A
  
THIS PAGE LEFT BLANK INTENTIONALLY

TECHNICAL NOTE   |  July 2025  |  23
Financial Impact Assessment for Zero-Emission Trucks (Fi-ZET)
THIS PAGE LEFT BLANK INTENTIONALLY

LGF, AADI  |  2 Balbir Saxena Marg  |  Hauz Khas  |  New Delhi 110016, India  |  WRI-INDIA.ORG WR I IN DI AWR I IN DI A
Copyright 2025 WRI India. This work is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License. To view a 
copy of this license, visit https://creativecommons.org/licenses/by-nc-nd/4.0/
About WRI India
WRI India, an independent charity legally registered as the India 
Resources Trust, provides objective information and practical 
proposals to foster environmentally sound and socially equitable 
development. Our work focuses on building sustainable and 
liveable cities and working towards a low carbon economy. 
Through research, analysis, and recommendations, WRI India puts 
ideas into action to build transformative solutions to protect the 
earth, promote livelihoods, and enhance human well-being. We are 
inspired by and associated with World Resources Institute (WRI), a 
global research organization. Know more: www.wri-india.org 
Our challenge  
Natural resources are at the foundation of economic opportunity and 
human well-being. But today, we are depleting Earth’s resources at 
rates that are not sustainable, endangering economies and people’s 
lives. People depend on clean water, fertile land, healthy forests, 
and a stable climate. Livable cities and clean energy are essential 
for a sustainable planet. We must address these urgent, global 
challenges this decade.
Our vision  
We envision an equitable and prosperous planet driven by the wise 
management of natural resources. We aspire to create a world where 
the actions of government, business, and communities combine to 
eliminate poverty and sustain the natural environment for all people. 
Our approach  
COUNT IT  
We start with data. We conduct independent research and draw on 
the latest technology to develop new insights and recommendations. 
Our rigorous analysis identifies risks, unveils opportunities, and informs 
smart strategies. We focus our efforts on influential and emerging 
economies where the future of sustainability will be determined. 
CHANGE IT  
We use our research to inform government policies, business 
strategies, and civil society action. We test projects with communities, 
companies, and government agencies to build a strong evidence 
base. Then, we work with partners to deliver change on the ground 
that alleviates poverty and strengthens society. We hold ourselves 
accountable to ensure our outcomes will be bold and enduring.
SCALE IT  
We don’t think small. Once tested, we work with partners to adopt and 
expand our efforts regionally and globally. We engage with decision-
makers to carry out our ideas and elevate our impact. We measure 
success through government and business actions that improve 
people’s lives and sustain a healthy environment.
