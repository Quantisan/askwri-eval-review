---
doc_id: 2023_financial-analysis-of-charging-station-fact_2082
source_pdf: kp-docs/askwri-kps/2023_financial-analysis-of-charging-station-fact_2082.pdf
extraction_method: cache-plaintext
char_count: 113588
title: Financial Analysis of Charging station (FACt)
authors: Mulukutla, Pawan; Das, Shyamasis; Bansal, Priya
date_published: 3/27/2023
article_type: Technical Note
sub_tag: Transport decarbonization
wri_primary_office: WRI India
wri_programs: Cities
language: English
url: "https://wri-india.org/research/financial-analysis-charging-station-fact"
doi: "https://doi.org/10.46830/writn.22.00085"
summary: FACt is an innovative Excel-based tool designed to facilitate the financial evaluation of public charging infrastructure for electric vehicles in India. By providing a comprehensive analysis of project costs, internal rates of return, and sensitivity to variable changes, it empowers stakeholders such as financial institutions and policymakers to assess the viability of charging stations. The tool addresses the existing knowledge gap regarding the business case for public charging stations, enabling cities to identify financial barriers and develop targeted policies. Its user-friendly design and adaptability to various contexts make it a unique resource for enhancing EV infrastructure deployment in India.
---

# Financial Analysis of Charging station (FACt)

TECHNICAL NOTE   |  Version 1.0  |   March 2023  |  1
CONTENTS
Abstract. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  1
Introduction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  1
How to use FACt. . . . . . . . . . . . . . . . . . . . . . . . . . . .4
Behind the curtain: how the tool works .... 16
Caveats for users. . . . . . . . . . . . . . . . . . . . . . . . . . .19
Disclaimer ................................ 20
Appendix A ................................. 21
Endnotes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
References ................................ 29
Acknowledgments ........................ 30
About the authors. . . . . . . . . . . . . . . . . . . . . . . . . 32
Technical notes document the research or analytical 
methodology underpinning a publication, interactive 
application, or tool.
Suggested Citation: Das, S., P . Bansal, and P . 
Mulukutla. 2023. "Financial Analysis of Charging 
station (FACt)." Technical Note. Mumbai: WRI 
India. Available online at https://doi.org/10.46830/
writn.22.00085
ABSTRACT
The aim of Financial Analysis of Charging station (FACt) (the “Tool”) is to help 
build an understanding of the business case for rolling out public charging 
infrastructure for electric vehicles (EVs) in India in different contexts. The 
MS-Excel-based tool is a flexible, transparent, and user-friendly solution to 
the problem of conducting a quick preliminary assessment of the financial 
justification for setting up a public charging station (PCS). The wide-ranging 
outputs from the Tool provide a well-rounded view of the financials of a 
public charging infrastructure project, including the project cost composition 
and the possible impact of various factors on the return. Currently, there 
is no publicly available open access application-based solution, made for 
the Indian market, that achieves the stated goals of FACt. The model is 
particularly useful for entities that are interested in gaining a foundational 
understanding of PCS finances in India, such as financial institutions, 
policymakers/regulators, real estate companies, urban local bodies, and 
implementing agencies. It is designed to allow several implementation 
situations and charging use cases spanning the gamut of technological, 
operational, financial, and regulatory aspects to be accounted for in the 
financial calculation. Cities in India can benefit from FACt as it can help them 
identify the financial barriers to private sector deployment of PCSs, enabling 
stakeholders to design policies to overcome them.
INTRODUCTION
Motivation
The availability of adequate public charging infrastructure is widely  
considered a prerequisite for EV adoption (IEA 2022a). To this end, the 
central government and subnational governments in India have emphasized 
rolling out public charging points. Financial incentives have been offered to 
encourage the setting up of public chargers for EVs. The government has 
advocated setting up at least one charging point in every 3 km by 3 km grid in 
a city to allay range anxiety (Ministry of Power–GoI
TECHNICAL NOTE
Financial Analysis of Charging  
station (FACt)
Shyamasis Das, Priya Bansal, and Pawan Mulukutla
A tool for easy financial evaluation of public charging infrastructure deployment in India

2  |  
  
 2022). Despite the policy push, on-ground implementation of 
public charging infrastructure has not seen much traction. 
One of the major causes of this slow progress is the high-risk 
perception of the investment. There is a perceived uncertainty 
around the business case for establishing and running a PCS.1 
This is often attributed to factors such as the high up-front 
investment in charging equipment and the ancillary electrical 
setup, expensive space rental in cities, uncompetitive electricity 
tariffs for EV charging, the additional cost of operators to staff 
the facility, and suboptimal asset utilization due to the lack of 
charging demand (The World Bank 2021; Sandalkhan et al. 
2021; IEA 2022b; Singh 2021; Das and Banerjee 2022; Pathak 
and Patel 2021). 
The nascency of the electric mobility sector, its fast-evolving 
technological and business landscapes, and the different  
charging use cases2 make it difficult to templatize the 
implementation mechanisms. It is evident that no silver bullet 
can make investment in public charging infrastructure attractive. 
A range of policy or regulatory interventions along with a fresh 
take on the tender clauses may be necessary. These efforts will 
need to strike a balance between the interests of the parties 
involved in the implementation of PCSs, especially the charge 
point operator (CPO),3 the electricity distribution utility, and 
the land-owning entity. 
To this end, it is critical to build an understanding of the business 
case for setting up a PCS in applicable contexts and different 
charging use cases. The present understanding of the financials of 
a public charging infrastructure project for many stakeholders 
in the sector, other than the established charging service 
providers, is largely superficial and liable to be influenced by 
market commentary and the gray literature.4 The need thus 
arises to empower these actors with a freely available, open 
access resource that can help decode the financial performance 
of an investment in PCS deployment and also yield insights 
into the associated financial aspects. A simple, user-friendly tool 
can help build the capacity of the stakeholders, who may not 
have the expertise to appreciate and deal with the problem. No 
open access tool for this purpose that is suitable for India’s EV 
sector is available in the public domain. The current solutions 
are primarily developed for advanced economies.5 Importantly, 
the dynamics of electric mobility markets vary considerably 
from one major economy to another. The variation can be 
seen in aspects such as the profiles of EV stock and charging 
patterns, types of charging units deployed and the entailed 
costs, electricity pricing and supply regulations, provision for 
land, personnel cost, charging fees, applicable rates for taxes and 
interest on loans, and inflation. Hence, it is critical to capture
the state of play unique to a country. A bespoke analytical 
solution thus needs to be developed for the Indian market.
Objectives of FACt
FACt, the Excel-based tool presented here, is a flexible,  
transparent, and user-friendly solution to the problem of  
conducting a quick preliminary assessment of the financial  
justification for setting up a PCS in India. The wide-ranging 
outputs from FACt provide a well-rounded view of the  
financials of a public charging infrastructure project, including 
the project cost composition and the possible impact of  
various factors on the return. This Tool is primarily meant to 
help develop a foundational understanding of PCS finances. For 
in-depth financial analysis of an investment, the use of more 
extensive calculations using a suite of financial indicators is 
recommended. This application should not be considered a  
one-stop solution for investment decision-making.
FACt serves the aforementioned objectives by enabling the user 
to achieve the following:
 ▪ Understand the composition of the entailed cost of setting 
up and running a PCS.
 ▪ Estimate the possible project internal rate of return (project 
IRR) for a CPO (see Box 1). 
 ▪ Gauge the contributions of the key input variables to the 
project’s net cash inflow. 
 ▪ Undertake sensitivity (what-if ) analysis to assess impacts of 
changes in specific input variables on the project IRR.
 ▪ Understand the changes in the values of input parameters 
needed to achieve the hurdle rate (see Box 2).
 ▪ Forecast over the project contract period the potential 
incomes of the stakeholders and the break-even year for the 
investment (see Box 3).
Box 1. What is the internal rate of return?
The internal rate of return (IRR) is the annual rate of growth that 
an investment is expected to generate. The higher the IRR, the 
more desirable the investment. However, before making an 
investment decision, one should also evaluate other financial 
metrics such as the net present value and debt-service 
coverage ratio.

TECHNICAL NOTE   |  March 2023  |  3
Financial Analysis of Charging station (FACt)
 ▪ It is a transparent application that helps the user perform 
analyses and gain insights into the different aspects of the 
charging business and its viability; all the assumptions and 
methods are clearly explained.
Although the user can use this tool to assess several  
implementation situations and charging use cases accurately, 
cases could occur in which certain aspects, especially those 
concerning new regulations and business models, might not be 
fully captured.
Potential use cases of FACt 
The model is expected to benefit entities interested in  
achieving a foundational understanding of PCS finances in 
India, such as financial institutions, policymakers/regulators, 
real estate companies, urban local bodies, and implementing 
agencies. Cities in India can benefit from FACt as it will help 
them identify financial barriers to private sector deployment 
of PCS, thus enabling stakeholders to design policies that 
may overcome them. The following are some of the specific 
use cases of FACt:
 ▪ An analyst in an early-stage start-up that is planning to 
venture into or is already in the business of providing EV 
charging services to customers can use this tool to quickly 
conduct a preliminary viability assessment of setting up a 
PCS in a certain context.
 ▪ An officer in a real estate company that is planning to 
rent out unused space to CPOs at its properties can apply 
FACt to identify a suitable rental mechanism and fix 
the rental rates.
 ▪ A loan officer of a retail bank can use FACt to get a 
sense of the financial outcome from a proposed charging 
infrastructure project for which a company has submitted an 
application for a loan.
 ▪ An officer of a nodal public agency, department, or ministry 
can use FACt to gauge the possible financial attractiveness to 
CPOs of deploying public charging infrastructure in a given 
policy and regulatory environment.
 ▪ An official of a city authority entrusted to design project 
tenders for installing and managing a PCS can use FACt to 
assess the viability of the projects and understand the impact 
of various tender clauses and site characteristics on the 
project financials. 
Uniqueness of the tool
FACt is one of its kind—currently, there is no publicly available 
open access application-based solution made for the Indian 
market that offers the functions of the Tool. Some of the key 
features of the Tool are the following: 
 ▪ It accounts for several implementation contexts covering 
technological, operational, financial, and regulatory aspects in 
the financial calculation.
 ▪ It is curated for the Indian context as it takes into account 
the mainstream EV chargers, electricity tariff framework and 
regulations, land arrangement, and other factors.
 ▪ The user has to provide a limited number of mandatory 
inputs. The default values (preloaded in the Tool) are 
customizable. Further, all data required to be entered are 
commonly available with the stakeholders.
 ▪ It offers flexibility, in that the user can consider various PCS 
configurations, CPO income mechanisms, types of electricity 
connections, tariff designs, and land rentals to account for 
different public charging use cases.
 ▪ It allows the user to benchmark the resulting project IRR 
and get a sense of the conditions required to achieve the 
targeted rate of return.
Box 2. What is the hurdle rate?
The hurdle rate is the minimum rate of return on an investment 
that will offset its costs. The hurdle rate is generally equal to the 
company’s cost of capital.
Box 3. What is breakeven?
Realizing breakeven in this case means that the aggregate  
revenue from the PCS (including the charging fee revenue, 
income from parking charges, and secondary net revenue) 
along with any financial support from the government to the 
project is able to match at a given point in time the cumulative 
cash outflow from the investment, which includes both the 
up-front capital expenditure (primarily on charging and 
ancillary infrastructure) and recurrent expenses (i.e., the cost of 
electricity, land rental, operator cost, and other operational and 
maintenance expenses) up to that time. The breakeven year is the 
year when breakeven is achieved.

4  |  
  
Approach to the development of FACt
FACt was developed using a three-pronged approach: need 
assessment, tool conceptualization, and user feedback.
Need assessment
A series of interactions with stakeholders and an in-depth 
literature review were used to understand the major challenges 
in scaling up charging infrastructure rollout. A major gap  
was found in understanding the business viability of setting  
up a PCS. This gap has been slowing down on-ground  
implementation, as highlighted in the section titled “Motivation” 
(The World Bank 2021; Das and Banerjee 2022). The team 
also reached out to select players to understand how this  
possible knowledge gap could be bridged, and it was during 
the ensuing interactions that the idea of formulating an Excel-
based financial tool germinated.6 Subsequently, WRI India 
organized an EV Masterclass to socialize the concept of an 
Excel-based tool, which was well received by the participants 
and potential funders.7 These need assessment activities led 
to the formalization of the research initiative to develop 
FACt. Also, the target stakeholders (users of the Tool) were 
identified and invited to submit detailed feedback on FACt’s 
design and function.
Conceptualization of FACt
As ideated during the stakeholder consultation, Excel was 
found to be the best-suited platform for the application because 
of its popularity across a cross section of potential users, easy 
accessibility, sufficient flexibility, user-friendliness, and its 
comprehensive suite of functions. The need assessment helped 
identify the possible project financial indicators or target  
outputs. It was found that answers to the following key  
questions would help potential stakeholders:
 ▪ What would be the cumulative and operating costs 
of the project?
 ▪ How attractive would the project be under the 
given conditions?
 ▪ What major factors could impact the project’s 
business viability?
 ▪ What could be the possible financial impact of changes in 
the input (independent) variables or factors?
 ▪ What did the revenue trends for investors, distribution 
utilities, and land-owning entities (the three main actors 
associated in a project’s implementation) look like?
 ▪ What would it take to make the project financially viable?
Accordingly, the Tool provides the following major outputs:
 ▪ Cost dissection: This shows estimates of the total 
project cost, including the operating cost and the major 
cost components and sub-components over the 10-year 
project period.8
 ▪ Project IRR: This is a commonly applied indicator for 
evaluating the profitability of a potential investment, which 
is the core function of the Tool.
 ▪ Contributions of the key input parameters or variables: 
This output shows the contribution of key variables, such as 
the capital investment, charging fees, cost of electricity, land 
rental, cost of operator/crew, and average daily active  
use of charging units, to the project’s net cash inflow.
 ▪ Sensitivity (what-if ) analysis: This is used to predict 
possible changes in the project IRR value with ±10 and ±20 
percent variations in the values of the key input parameters 
compared to their original or baseline values.
 ▪ Revenue profiles: These show the projections of the possible 
yearly revenue trends for the CPO, the distribution utility, 
and the land-owning entity over the entire project duration.
 ▪ Solver analysis: This indicates how the key input parameters 
must be changed to achieve the benchmark or target 
rate of return.
User feedback on FACt
Extensive feedback from the identified potential users 
was central to the development of FACt, which was 
carried out in multiple stages. To seek specific feedback, 
detailed demonstrations of the draft Tool were given to the 
stakeholders,9 and several changes were made in the design and 
function of the draft Tool based on their inputs, which were 
documented for future reference. Moreover, the stakeholders 
were made part of a robust peer review exercise while advancing 
FACt from its beta version. FACt is thus the product of effective 
collaboration with its potential users. 
HOW TO USE FACt
The landing page of FACt titled “User Guide” provides 
instructions on how to use the Tool (Figure 1).
The Tool comprises a number of input pages and output  
or results worksheets. The input pages are used to feed the 
model with the required input data, and the output pages  
display the corresponding results. More details are given in 
the following sections.

TECHNICAL NOTE   |  March 2023  |  5
Financial Analysis of Charging station (FACt)
Figure 1  |   “User Guide” page of FACt 
Note: The purpose of the above figure is to help in referring to the particular page of the Excel tool.
Source: Financial Analysis of Charging station (FACt) tool developed by WRI India.
Input pages
FACt mainly uses four categories of data: technological, 
operational, financial, and regulatory. These four sets of data are 
captured in two ways:
 ▪ User inputs: These are very context or case specific and 
hence must be provided by the user. FACt requires a 
limited number of such inputs, which makes the Tool quick 
and easy to use.
 ▪ Pre-set inputs: These are default values that are already 
preloaded in the Tool, but the user can change them 
depending on the context. The user does not have to collect 
and provide these input data unless the default values must 
be replaced with new inputs.
A short description of each of the input pages follows. Table 
A-1 in Appendix A gives the details (including the units of the  
concerned inputs, sources of input data collection, the purpose 
of the inputs, and specific guidance for users) of the input 
parameters. These details are also given in FACt. 
Financial Analysis of Charging station (FACt)
A Tool For Easy Financial Evaluation Of Public Charging Infrastructure Deployment In India
About the Tool:
The aim of FACt is to help the user conduct a quick preliminary assessment of the financial justification for setting up an electric vehicle (EV) public charging station (PCS) in India. The wide-rangingoutputs from the tool provide a well-rounded view of the
financials of a public charging infrastructure project, including the possible impact of different factors. This tool is primarily intended to help develop a foundational understanding of PCS finances. 
Why Use This Tool:
FACt enables the user to achieve the following:
1. Understand the composition of the entailed cost of setting up and running a PCS (see the "Cost Dissection" page). 
2. Estimate the possible project internal rate of return (project IRR+), which is the primary financial yardstick for evaluating the financial attractiveness of investing in a public charging infrastructure project (see the "Project IRR & Sensitivity" worksheet).
3. Gauge the contributions of the key input variables to the project’s net cash inflow (see the "Project IRR & Sensitivity" page).  
4. Undertake sensitivity (what-if) analysis in the ±10% and ±20% ranges, to show how changes in the given range in the values of individual independent variables affect the project IRR (the dependent variable; see the "Project IRR & Sensitivity" worksheet).    
 
5. Use the tool feature "Solver" to understand the changes in the values of the key input parameters needed to achieve the benchmark rate of return,also known as the hurdle rate (if the project IRR in the base case falls short of the target; see the    
    "Solver" page).    
6. Forecast over the 10-year project period the potential incomes of the stakeholders (i.e., the charge point operator [CPO], the power distribution utility, and the land-owning entity) that are directly involved in implementing a PCS (see the     "Revenue Profile" worksheet).
*As defined by the guidelines issued by the Ministry of Power or any other competent authority.
The internal rate of return (IRR) is the annual rate of growth that an investment is expected to generate. The higher an IRR, the more desirable the investment
Key Features:
1. The tool is designed in such a way that several implementation contexts covering technological, operational, financial, and regulatory aspects can be taken into account in the financial calculation.
2. It requires a limited number of mandatory inputs from the user, and all data to be entered are commonly available with the stakeholders.
3. It offers flexibility, in that the user can consider various PCS configurations, income mechanisms for a CPO, types of electricity connections, tariff designs, and land rentals to take into account different public charging use cases.
 
4. FACt is curated for the Indian context as it takes into account the mainstream EV chargers, electricity tariff framework and regulations, land arrangement, and other factors.
Steps To Use the Tool Effectively:
1. Access: Download the MS Excel file from WRI India's Electric Mobility practice area page (https://www.wricitiesindia.org/content/electric-mobility), and check the background details and tutorial video on the website.  
2. Familiarize: After opening the Excel file and enabling the Editing and Macros options (see the commands at the top of the file), visit the current page ("User Guide") for a description of FACt and instructions on how to use it. When the Excel file is first opened,
a security alert from Microsoft is triggered as the file contains VBA code. To unblock the file, follow the steps mentioned in the Technical Note. For information on the required inputs and produced outputs, see the "Input Data Table" and "Output Data Table"
pages, respectively.
   
3.
 
Start: Click on the
 
Start button on the current worksheet to open the "User Inputs" worksheet along with the "Pre-set Inputs" page.
  
4.
 
Provide:
 
Enter the requested inputs on the "User Inputs" worksheet in accordance with the given guidance, and if required, click the Clear All Inputs
 
button at the bottom of the worksheet to key in a fresh set of input values. 
   
5.
 
Validate:
 
Click the Check Pre-set Inputs
 
button to visit the "Pre-set Inputs" worksheet and ascertain whether the default input values are appropriate for the required analysis; if not, change the input values accordingly. To restore the default values, click the
    Restore Default Inputs
 
button at the bottom of the worksheet.
6.
 
Generate: Press the
 
Check Results button on the “Pre-set Inputs” page to produce the results and open the first of the four output-related pages.
  
7.
 
Visit: Explore the "Cost Dissection" worksheet to understand the project cost composition and annual operating cost over the 10-year
 
operation of the PCS.
8.
 
See:
 
Go to the "Project IRR & Sensitivity" page for results on the project IRR, the impact of key input variables, and sensitivity analysis.
9.
 
Explore:
 
Visit the "Revenue Profile" worksheet to check the 10-year projection of the potential incomes of the CPO, the power distribution utility, and the land-owning entity.
 10. Apply:
 
Click the Solve  button at the bottom of the "Solver" page to understand the scenario in which the benchmark project IRR is achieved (if it is not reached in the base case); to refresh the page, click the Restore button.  
11. Understand: Check "Input Data Table" and "Output Data Table" pages for more details about the different types of required inputs and the produced outputs.
12. Learn:
 
For more information about FACt, download and read the associated Technical Note, which is available on the website. 
Caveats:
1. Macros should be enabled in the Trust Settings after opening the Excel file; otherwise, some functions of the Tool will not
 
work.
2. It is strongly suggested to run FACt in a device with an active Microsoft Office license. Office 2016 or any later version of MS Office is recommended.
3. Some features of FACt such as Solver may not work properly under macOS. However, the tool will be able to generate reliable
 
results for the project IRR.
 4. It is recommended that the user acquire a fundamental understanding of a PCS and its operation before applying the tool.
The purpose of FACt is to help develop a foundational understanding of PCS finances. This application should not be considered a one-stop-solution for assessment of and/or decision-making
regarding an exisiting or proposed project or investment. The functions of FACt and the produced results are the sole responsibility of the users of this tool. Neither WRI India nor the creators of FACt
can be held, directly or indirectly, responsible or accountable for the use of this tool and/or the results. The tool uses some third-party information, the source of which should be independently verified
by users.
Disclaimer:
User Guide Pre-set Inputs Cost Dissection Project IRR & Sensitivity Revenue Profile Input Data Table Output Data TableSolverUser Inputs
Start

6  |  
  
User inputs 
Figure 2 shows a sample “User Inputs” page. Users can input 
data into this worksheet. For specific guidance on each input 
parameter, a user can hover the cursor on the concerned cell in 
the worksheet or refer to the “Input Data Table” page of the 
Tool or Table A-1 in Appendix A of this document. 
The following categories of data are covered by this 
input worksheet.
PCS CONFIGURATION, UTILIZATIONS, AND FEE RATES
 ▪ The user is required to input the number of charging units, the 
average daily active use of the charging unit in terms of hours, 
and the charging/swapping fees for the corresponding types of 
charging units. 
 ▪ The charging unit type signifies the type of charging 
solution deployed at the PCS (slow charger, moderately fast 
charger, fast charger, or a stack battery charging system for 
swappable batteries). 
 ▪ The eight EV charging solutions recognized in the guidelines 
issued by the Ministry of Power, GoI, on January 14, 2022, 
and commonly deployed at PCSs have been listed on this 
page. For details about these charging units, see the notified 
guidelines and their amendments.
 ▪ For the types of charging units that are not on the list, the 
user should provide the required inputs under the category 
“Other Charger Type” on both the input pages (i.e., “User 
Inputs” and “Pre-set Inputs”). 
 ▪ Importantly, FACt considers that the charging units are used 
at their rated output power levels. In reality, the effective 
power level during a charging session can fall below the rated 
power depending on the recommended C-rate of the EV’s 
battery (if a DC charging unit is used) and/or the power 
rating of the vehicle’s on-board charger (if an AC charging 
unit is used). 
PAYMENTS TO BE MADE TO THE DISTRIBUTION UTILITY
 ▪ The user is first required to input the energy charge and the 
demand charge, elements of the two-part tariff structure.
The energy charge is the variable component of the tariff 
and is linked to the recorded electricity consumption (kWh), 
energy charge is the variable component of the tariff and 
is linked to the recorded electricity consumption (kWh), 
whereas the demand charge is the fixed component of the 
tariff, its value depending on the sanctioned load or contract 
demand (kVA10) of the given electricity connection. For the 
energy charge, it is recommended to consider the landed 
cost or all-in rate of electricity (i.e., inclusive of taxes and 
other state-levied charges). Information on these charges11 
can be obtained from the state tariff orders for their serving 
distribution utilities, which are usually available on the 
websites of State Electricity Regulatory Commissions or the 
distribution utilities. 
 ▪ The user is then required to specify whether a new dedicated 
electricity connection is necessary to energize the PCS. A 
new dedicated electricity connection is typically required 
to take advantage of the preferential tariff (also known as 
the EV tariff ), if this benefit is offered by the electricity 
distribution utility. An existing connection can be used if the 
PCS is established on the premises of a host facility such as a 
workplace or shopping complex.
PAYMENTS TO BE MADE TO THE LAND-OWNING ENTITY
 ▪ The user is required to provide inputs under this category 
only if land rental is applicable. For instance, land rental 
may not be applicable for a shared workplace or residential 
charging use case as the concerned organization or the 
housing society is likely to own the land and offer space to 
the CPO free of charge to make cost of installation, and 
consequently the cost of service, economical. 
 ▪ In scenarios where a land rental is applicable, the user has 
to select whether the land rental is fixed on a monthly 
basis or is variable (that is, linked to the actual electricity 
consumption at the facility). The latter land rental 
arrangement is often referred to as the revenue sharing 
model. According to the revised consolidated Guidelines & 
Standards for Charging Infrastructure for Electric Vehicles 
(EV) released by the Union Ministry of Power on January 
14, 2022, land available with the government/public entities 
shall be provided for installation of a PCS to a government 
/public entity on a revenue sharing basis at a fixed rate of 
₹1/kWh (used for charging), to be paid to the land-owning 
agency from the PCS business on a quarterly basis. A 
Model Revenue Sharing agreement has also been included 
in the guidelines. Such a revenue sharing agreement may be 
initially entered into by the parties for a period of 10 years. 
The revenue sharing model may also be used by a public 
land-owning agency to provide land to a private entity 
for installation of a PCS on a bidding basis with a floor 
price of ₹1/kWh.
 ▪ To give the user a sense of the possible total land 
requirement to set up a PCS with the given configuration 
and thus arrive at the monthly total fixed land rental, 
FACt autonomously estimates and displays the total 
land requirement on the “User Inputs” page. However, this

TECHNICAL NOTE   |  March 2023  |  7
Financial Analysis of Charging station (FACt)
Source: Financial Analysis of Charging station (FACt) tool developed by WRI India.
Note:  The purpose of the above figure is to help in referring to the particular page of the Excel tool.
Figure 2  |   A sample “User Inputs” page
Attention: Hover the cursor on the input parameters for specific guidance. Brackets in the input parameters indicate the units of the values. If a parameter, for example, a type of charging unit, 
is not applicable, leave the concrtned input cell blank. 
Remark: The EV charging solutions recognized in the guidelines issued by the Ministry of Power, GoI, on January 14, 2022, and commonly deployed at PCSs have been listed above. 
Enter inputs for at least one charging unit, and leave blank the input cells corresponding to the types of charging units that are not applicable. 
For the types of charging units that are not on the list but are applicable, provide the required inputs under "Other Charger Type" on this page as well as in the "Pre-set Inputs" worksheet.
PCS Configuration, Utilization, and Fee Rates
Type of Charging Units Number of 
Charging Units
 Average Daily Active Use of 
Charging Unit in Year 1 of 
Operation (hours per day)
LEV AC
AC Type-2
Bharat AC 001
Bharat DC 001
CCS-2 DC Wallbox Charger
CCS-2
CHAdeMO
Stack Battery Charging System for Swappable
Batteries
Other Charger Type 1
Other Charger Type 2
Other Charger Type 3
Payment to Electricity Distribution Utility
Has a New Dedicated Electricity Connection
been Applied for to Energize the PCS?
Payment to Land-owner
Is Monthly Land Rental Fixed?
Estimated Land Requirement (sq. m )0 .00
Operation Cost
Is the PCS manned for the entir daily
operational time?
Mandatory Inputs to be Provided by Users
Page description: Mandatory User Inputs
Information on the energy charge and other state-levied charges and taxes can be obtained from state tariff orders, 
which are usually available on the websites of the State Electricity Regulatory Commissions or DISCOMs.
Ascertain whether a demand or fixed charge is applicable to the PCS. Information on the demand charge can be 
obtained from the state tariff orders, which are usually available on the websites of the State Electricity Regulatory 
Commissions or DISCOMs.
Remark: Depending on the selected answer to the above question, enter a numerical value for one of 
the following input parameters. If land rental is not applicable, ignore the following input parameters.
 
Subsidies
1
1
1
11.008
5.00 14
3.00 17
6.50
300
YES
NO
2.00
YES 30000
User Guide Pre-set Inputs Cost Dissection Project IRR & Sensitivity Revenue Profile Input Data Table Output Data TableSolverUser Inputs
Check Pre-set inputs Clear all inputs

8  |  
  
 ▪ is not a direct input to the other results of the Tool. This 
FACt autonomously estimates and displays the total land 
requirement on the “User Inputs” page. However, this is not a 
direct input to the other results of the Tool. This value is for 
the user’s reference only; the user has to provide the inputs 
related to land rental on this page. 
OPERATION COST AND SUBSIDIES
 ▪ The user must specify whether the PCS will be staffed for 
the entire daily operational time or not. 
 ▪ The operational hours may differ depending on the operation 
of the host facility. For instance, the operational hours for a 
charging station at a workplace may be 16 hours as against 
24 hours for a stand-alone charging station.
 ▪ The user is also required to input the eligible total capital 
subsidy amount (non refundable) available under central 
and state schemes. The information on the applicable 
capital subsidy will be available in the EV policies or 
scheme documents. 
After keying in the required input values on this page, the 
user should click the Check Pre-set Inputs button to validate 
the default input values. To input a fresh set of values, the 
user should click the Clear All Inputs button at the bottom 
of the worksheet.
Pre-set inputs
Figure 3 shows a sample “Pre-set Inputs” page. Here, the Tool 
is preloaded with default values for a set of parameters that are 
less case specific or more difficult to specify for a user who does 
not have much experience in the sector. However, the values 
may change depending on the implementation context, and 
hence the user is allowed to modify the given values. For specific 
guidance, the user can hover the cursor on each of the different 
input parameter cells on the worksheet or refer to the “Input 
Data Table” page of the Tool or Table A-1 in Appendix A of 
this Technical Note. 
The following categories of data are covered in this 
input worksheet.
CHARGING UNIT CONFIGURATIONS AND COSTS
 ▪ This section feeds default or pre-set values for the power 
ratings and the unit costs of the eight types of charging 
units recognized in the applicable guidelines issued by 
the Ministry of Power, GoI, on January 14, 2022, and are 
commonly deployed at PCSs. For certain types of charging 
units, such as AC Type-2 and CCS-2,  various products or
models are available in the market with different power ratings 
and, consequently, different price tags. The Tool is preloaded 
with default values for charger power ratings and the costs of 
models that are commonly deployed in public charging infra-
structure in India currently. The user can consider a different set 
of values for charger power ratings and costs to accurately reflect 
the applicable PCS configuration. For example, instead of 7 kW, 
one can input 22 kW as the power rating for AC Type-2. The 
value of the cost per charging unit should be revised accordingly. 
Similarly, a PCS may house a stack battery charging system with 
more or less than 12 battery charging units and with different 
power ratings for each unit. The user can modify the required 
input values accordingly.
 ▪ For charging units other than the eight listed on the page, 
the user can provide the required inputs under the charging 
unit category “Other Charger Type.” 
OTHER COSTS FOR CHARGERS/STACK BATTERY 
CHARGING SYSTEM
 ▪ The worksheet includes pre-set values for the cost of 
civil works and installation and commissioning costs as a 
percentage of the total cost of the charging system. These 
costs are used to estimate the cost of charging equipment as 
part of the overall capital investment, as also reflected later 
on the “Cost Dissection” page of the Tool.
ANCILLARY ELECTRICAL INFRASTRUCTURE
 ▪  This section of the Tool feeds pre-set values for the 
power factor of the electricity connection, the cost of the 
distribution transformer (DT) and associated equipment 
per 50 kVA rated capacity, meter costs, and the ancillary 
electrical infrastructure installation cost (including labor). 
 ▪ The power factor is a measure of how effectively the 
incoming power is used in the electrical system. A high 
power factor indicates that the power supplied to the 
electrical system is effectively used. A system with a low 
power factor consumes the incoming electricity supply 
inefficiently, resulting in losses. Information on the power 
factor can be obtained from the serving distribution utility.
 ▪ The cost of the DT and associated equipment per 50 
kVA rated capacity, along with the ancillary electrical 
infrastructure installation cost (including labor), are set 
using the utility-provided values, and the meter costs are set 
using the India Smart Grid Forum’s values. The India Smart 
Grid Forum is a public-private partnership initiative of the 
Ministry of Power, GoI.

TECHNICAL NOTE   |  March 2023  |  9
Financial Analysis of Charging station (FACt)
Figure 3  |   A sample of “Pre-set Inputs” page
Source: Financial Analysis of Charging station (FACt) tool developed by WRI India.
Note: The purpose of the above figure is to help in referring to the particular page of the Excel tool.
Attention: Hover the cursor on the input parameters for specific guidance. Brackets in the input parameters indicate the units of the values.
If a type of charging unit is not applicable, users need not delete the given input values. The Tool filters out invalid pre-set input values based on the user response on the "User Inputs" page.
The charging system refers to the charging units to be installed at a PCS,  
including the stack battery charging system, if any.
The information can be obtained from the serving DISCOM.
Pre-set Inputs That Users Can Change
Page description: This input worksheet is preloaded with default values for the given parameters. However, the values may change depending on the situation, and hence, users have been 
given the flexibility to input their own data.
Charging Unit Configurations and Costs
Other Costs for Chargers/ Stack Battery Charging System
Ancillary Electrical Infrastructure 
Type of Charging Unit Power Rating of the
Charging Unit (kW)
LEV AC 3.3 3500
AC Type-2 7 38000
Bharat AC 001 10 40000
Bharat DC 001 15 200000
CCS-2 DC Wallbox Charger 25 700000
CCS-25 0 1100000
CHAdeMO 50 1050000
Stack Battery Charging System for Swappable Batteries 12 2080000
Other Charger Type 1 00
Other Charger Type 2 00
Other Charger Type 3 00
Cost of Civil Works as a Percentage of the Total Cost
of the Charging System (%) 5
Installation and Commissioning Costs as a Percentage
of the Total Cost of the Charging System (%) 20
Power Factor of the Electricity Connection0 .85
150000
3500
250000
Remark: Enter the above inputs if the charger types are not in the given list. By 
default, no other charger type is considered. For certain types of charging units 
such as AC Type-2 and CCS-2, various products or models are available in the 
market with different power ratings and, consequently, different price tags. The 
Tool is preloaded with default values for charger power ratings and costs of 
models that are commonly deployed in public charging infrastructure in India 
currently. The user can consider a different set of values for charger power 
ratings and costs to accurately reflect the applicable PCS configuration. For 
example, instead of 7 kW, one can input 22 kW as the power rating for AC 
Type-2. The value of the cost per charging unit should be revised accordingly. 
Similarly, a PCS may house a stack battery charging system with more or less 
than 12 battery charging units and with different power ratings for each unit. 
The user can modify the required input values accordingly.
User Guide Pre-set Inputs Cost Dissection Project IRR & Sensitivity Revenue Profile Input Data Table Output Data TableSolverUser Inputs
 ▪ These costs are used to infer the cost of ancillary equipment 
as part of the overall capital investment, as also reflected later 
on the “Cost Dissection” page of the Tool.
OTHER POSSIBLE INCOMES FOR CPOS
 ▪ Users are required to input the parking charges (if applicable) 
for each of the selected charging unit types. By default, the 
Tool considers parking charges to be zero. These charges are 
typically applicable only to certain use cases employing 
slow/moderately fast chargers such as destination charging 
 
(such as malls) and charging at public-authority-owned 
parking. For shops and rest stops, customers usually park for 
15–30 minutes, making a fast-charging solution ideal; hence, 
parking charges may not typically be applicable here.
 ▪ As a CPO may explore secondary income sources at the 
facility through advertisements, public conveniences, 
refreshment kiosks, and so on, to complement its core 
revenue from the charging business, the “Pre-set Inputs” 
page can capture the secondary net revenue for the CPO. By 
default, the Tool does not consider any non core income.

10  |  
  
OPERATIONAL DETAILS
The worksheet includes pre-set values for the daily operational 
hours and annual operational days of the PCS. The default 
values are 24 and 365, respectively.
OTHER TECHNICAL DETAILS
 ▪ The worksheet includes values for the power demand 
threshold for an exclusive DT , charger efficiency, 
time for planned annual maintenance, and auxiliary 
electricity consumption. 
 ▪ The power demand threshold (kVA) for an exclusive DT 
is a critical parameter that can potentially impact the 
up-front investment of the CPO. If the sanctioned load for 
the electricity connection of the PCS equals or exceeds the 
given threshold, the CPO would be required to install an 
exclusive DT for the PCS. The Tool by default considers the 
threshold value applicable to the National Capital Territory 
of Delhi. However, the value varies from state to state and 
can be obtained from the applicable State Electricity Supply 
Code Regulations. One may also check with the concerned 
electricity distribution utility.
 ▪ Charger efficiency can be defined as the percentage of power 
drawn from the energy source that is actually fed to the 
vehicle battery. The default efficiency is 98 percent.
 ▪ The Tool considers 5 percent of operational hours as the time 
set aside for planned annual maintenance of the PCS. EV 
charging units require periodic checks for wear and tear, as 
well as to keep the overall system clean.
 ▪ Auxiliary electricity consumption is related to other electrical 
end uses at the PCS, such as illumination at the site. 
OTHER OPERATIONAL AND MAINTENANCE  
COSTS (ANNUAL)
 ▪ This section of the Tool feeds values for annual maintenance 
costs as a percentage of the cost of the core hardware, 
the insurance cost as a percentage of the total cost of the 
charging system, the electric vehicle supply equipment 
(EVSE) management software cost per unit of dispensed 
electricity, the hourly operator cost if the PCS is staffed, 
and the minimum alternate annual operator cost for a 
crewless facility.
 ▪ The hourly operator cost becomes applicable (and the 
corresponding value is triggered in the “Pre-set Inputs” 
page) if the user chooses “Yes” to answer the question of 
whether the PCS needs to be staffed. In that case, the hourly 
operator cost is fed into the calculation. The hourly rate is the 
minimum wage limit for semi-skilled labor notified by the 
Ministry of Labour & Employment, GoI.
 ▪ An operator may be required for periodic checks and 
troubleshooting at a PCS even if it is crewless. In this case, 
a dedicated operator may not be required. A lump-sum cost 
has been considered for this purpose as a minimum alternate 
annual operator cost.
FINANCING
 ▪ The worksheet includes pre-set values for debt as a 
percentage of the capital investment, the construction period 
(which is notional, for the purpose of accounting), the loan 
repayment period, and the rate of interest on the loan. 
 ▪ The default loan repayment period is taken to be six years 
based on the commonly used lending practice. 
 ▪ Default values based on the State Bank of India’s benchmark 
prime lending rate (BPLR) have been provided for the 
interest rate on loans.
OTHER COSTS INCURRED BY CPO
 ▪ The pre-set values in the Tool account for cost items 
such as service-line-cum-development charges 
(SLDC) and tax rates.
 ▪ SLDC is a one-time charge that a consumer has to pay to 
the serving electricity distribution utility when applying 
for a new electricity connection. The amount is usually 
linked to the sanctioned load (kVA) for the connection. 
SLDC becomes applicable (and the corresponding value is 
triggered on the “Pre-set Inputs” page) if the user states on 
the “User Inputs” worksheet that a new dedicated electricity 
connection is needed. By default, SLDC charges are based 
on the rates prevailing in the National Capital Territory of 
Delhi. Information on the charges for a new connection can 
be obtained from the concerned serving distribution utility.
 ▪ Default values based on the current landscape have been 
provided for the corporate tax and minimum alternate 
tax (MAT) rates.
BENCHMARKING
 ▪ To assess the business attractiveness of an investment in a 
PCS, benchmarking the estimated project IRR against a 
hurdle rate is an industry-wide practice. For this purpose, the 
Tool bases the benchmark rate of return on the State Bank 
of India’s BPLR. 
YEAR-ON-YEAR (Y-O-Y) ESCALATIONS
 ▪ The “Pre-set Inputs” worksheet has default values for the 
Y-o-Y escalations of the cost or operational parameters, 
which tend to vary with time. These include the electricity 
rate, land rental, other operational and maintenance (O&M)

TECHNICAL NOTE   |  March 2023  |  11
Financial Analysis of Charging station (FACt)
  
costs, charging fees, hourly parking charges, secondary 
revenue, and average daily active use of charging units. 
 ▪ The default Y-o-Y escalation rates are based on stakeholder 
consultations or past trends. The user can change these rates 
depending on the market outlook.
After changing the input values on this worksheet, a one-click 
option, Restore Default Inputs, can be used to restore the defaults 
if required. The Check Results button will take the user to the first 
of the four output-related pages.
Output pages
The Tool offers six different outputs: project cost composition, 
calculation of the project IRR, estimation of the contributions 
of the key input parameters to the project’s net cash inflow, 
sensitivities of major input variables, revenue trends for the 
associated actors, and Solver analysis (which helps identify the  
changes in the values of the key input parameters needed to 
achieve the benchmark rate of return). These six sets of outputs 
are captured by the Tool on the following four output pages. The 
Print button on each output worksheet can be used to print the 
entire active worksheet in formats such as PDF.  
The following section gives a short description of the output 
pages. Table A-2 in Appendix A shows the details (such as the 
outputs, the section in which the output is displayed in the Tool, 
the unit of the output, and guidance specific to the output for 
users) of each output.
Cost dissection
This output page produces the following two sets of results
(see Figure 4).
BREAKUP OF THE TOTAL PROJECT COST OVER THE 
PROJECT PERIOD 
The breakup shows the estimates for the major components 
and their sub-components over the 10-year project period. The 
components include the following:
 ▪ Capital investment
 ▪ Cost of charging equipment
 ▪ Cost of ancillary equipment
 ▪ Cost of electricity
 ▪ Energy charges
 ▪ Demand charges
 ▪ Land rental
 ▪ Other O&M costs
 ▪ Operator cost
 ▪ EVSE management software cost
 ▪ Maintenance costs and miscellaneous expenses
 ▪ Interest on term loan
The 10-year costs for the given components are also expressed 
per unit of dispensed electricity,12 which can be considered 
the buildup for the cost of the charging service over the entire 
project period. This can be a useful yardstick for setting the 
charging fee. The project period is considered 10 years, in line 
with the procurement practices for setting up and operating 
a PCS in India.13 In the majority of cases, the concessionaire 
agreements are found to be effective for about 10 years. Hence, 
market players are interested in understanding the financial 
viability of a project for the span of the concessionaire period. 
Policymakers and implementing agencies, therefore, should 
also frame the tender clauses or the concessionaire agreement 
such that an investor would be able to realize modest returns 
during the project period; that is, 10 years. Hence, to support in 
the financial evaluation and make the results meaningful and 
relevant, the Tool too adopts a similar project timespan for the 
associated calculations. All duration-sensitive outputs from the 
Tool are based on a 10-year project period. If required, from the 
results, one can easily deduce the possible outcome for a little 
shorter or longer project timeline.
TOTAL ANNUAL OPERATING COST OF RUNNING A PCS
The analysis of the annual operating cost includes estimates 
for the cost of electricity, land rental, and other O&M costs 
over the 10-year operation of the PCS. The breakup is also 
presented graphically.
Project IRR and sensitivity
Figure 5 shows a sample “Project IRR & Sensitivity” page. The 
underlying core methodology of the Tool is the one widely used 
in the industry for calculating the project IRR, a commonly 
applied indicator for evaluating the profitability of a potential 
investment.  The Tool auto-generates the IRR based on the 
user-provided inputs on the input pages.
Once the IRR for a project is determined, it is typically 
compared with the investor’s hurdle rate or cost of capital. If 
the IRR equals or exceeds the cost of capital, the project is 
considered investment worthy. A hurdle rate, which is also 
known as the benchmark, or minimum acceptable rate of return, 
is the minimum rate of return or target rate that the investor 
expects to realize on an investment. The rate is generally

12  |  
  
Figure 4  |   A sample “Cost Dissection” page  
Source: Financial Analysis of Charging station (FACt) tool developed by WRI India.
Note: The purpose of the above figure is to help in referring to the particular page of the Excel tool.
User Guide Pre-set Input s Cost Dissection Project IRR & Sensitivity Revenue Profile Input Data Ta ble Output Data T ableSolverUser Inputs
Project Cost Breakup Annual Operating Cost
Major Cost Components Cost Sub-components Cash Outflows                     Year
Cumulative over
a 10-year period Ye a r 1 Ye a r 2 Ye a r 3 Ye a r 4 Ye a r 5 Ye a r 6 Ye a r 7 Ye a r 8 Ye a r 9 Ye a r 10
Capital Investment 19260001 .16
Cost of Electricity 169744751 0.21 Total Operating Cost 30756033 2099335 2166718 2361627 2578275 2819345 3087865 3387252 3721365 4094562 4439689
Land Rental 40586082 .44
Other Operational & Maintenance
Costs 97229505 .85
Interest on Term Loan 5416880 .33
Cost of Electricity 16974475 1142041 1132471 1249121 1380266 1527804 1693883 1880937 2091723 2329362 254686 8
Land Rental 4058608 217985 246978 279826 317042 359209 406984 461113 522441 591925 65510 6
Other Operational & Maintenance
Costs 9722950 739309 787269 832680 880967 932332 986998 1045202 1107202 1173276 123771 5
Aggregate Cost of the Project 332237212 0
Cost of Charging Equipment 167250 01 .0 1
Cost of Ancillary Equipment 25350 00 .1 5
Energy Charges 13190476 7. 93
Demand Charges 367059 92 .2 1
Operator Cost 680375 94 .0 9
EVSE Management Software Cost 174114 51 .0 5
Maintenance Costs and
Miscellaneous Expenses
 117804 50 .7 1
Remark: Minor cost elements have not been listed and are not part of the aggregate project cost shown in the above table.
0
500000
100000 0
150000 0
200000 0
250000 0
300000 0
350000 0
400000 0
450000 0
500000 0
Year 1 Year 2 Year 3 Year 4 Year 5 Year 6 Year 7 Year 8 Year 9 Year 10
Annual Operating Costs
Cost of El ectricity Land Renta lO ther O perational & Maintenance Cost s
Cost Dissection
Cost of Electricity
Aggragat e
Project Cost
Demand Charges
Operator Cos
t
Land Rental
Capital Investment
Coast of Charging
Equipment
Other O&M Cost
s
EVS E Ma n a ge me n t
S o ftw a re  C o s t
En e r gy  C ha rg e s
Siz e of the inner donut □
is not for comparison □
with the outer one.
Cost Dissection
Page description: This output worksheet shows the results for the project IRR, the contribution of the given input parameters t o the projectÕs net cash inflow, and the □
sensitivity analysis (whose purpose is to find out how the target or dependent variable, in this case the project IRR, is affec ted by changes in the input variables). Print

TECHNICAL NOTE   |  March 2023  |  13
Financial Analysis of Charging station (FACt)
Figure 5  |   A sample “Project IRR & Sensitivity” page  
Source: Financial Analysis of Charging station (FACt) tool developed by WRI India.
determined by assessing the cost of capital, which in turn is 
commonly equated with the BPLR of the largest retail public 
sector bank in the country. The Tool by default considers the 
average BPLR for the current year of the State Bank of India, 
which is a public sector bank and also the largest retail bank in  
India. However, the Tool allows the user to set a different hurdle 
rate for benchmarking the project IRR. 
The value of the project IRR can be positive, negative, or null, as 
described in the following:
Note: The purpose of the above figure is to help in referring to the particular page of the Excel tool.
User Guide Pre-set Input s Cost Dissection Project IRR & Sensitivity Revenue Profile Input Data T able Output Data T ableSolverUser Inputs
Project IRR & Sensitivity Analysi s
Project Internal Rate of Return -4 .35%
Key Influencing Factors for the Input Parameters Key Input Parameters Contribution to Net
Cash Inflows (% )
Cost of Charging Units and Ancillary Equipment Capital Investment -2 56%
-256%
Charging Rate + Average Daily Active Use of Charging Units Ch ar ging Fees 3629 %
3629%
Hourly Parking Charge Parking Charges 273%
273%
Secondary Net Revenue 366%
4%366%
Increase Decrease
Capital Subsidy 4%
Energy Charges + Demand Charges Cost of Electricity -2260 %
-2260 %
Rental Rate Land Rental
-540%
-72%
-540%
Annual Maintenance Costs + EVSE Management Software Cost
+ Insurance Cost + Operator Cost Other Operational & Maintenance Cost s- 1294 %
Rate of Interest on Debt Interest on Term Loan -7 2%
Contribution of the Input Parameters
Cont ri buti on  of Different Input Parameter s
-1294%
Page description: This output worksheet shows the results for the project IRR, the contribution of the given input parameters t o the projectÕs net cash inflow, and the □
sensitivity analysis (whose purpose is to find out how the target or dependent variable, in this case the project IRR, is affec ted by changes in the input variables). Print
 ▪ A “positive” IRR indicates that the project or investment is 
expected to offer a positive return to the investor. 
 ▪ A “negative” IRR occurs when the aggregate net cash 
inflow from the project is less than the initial or up-front 
investment, which means the investor will realize a negative 
return on the investment. 
 ▪ A “null” IRR indicates that either the net cash inflow does 
not have at least one negative and one positive value (which 
is a likely reason) or the Excel calculation fails to converge

14  |  
  
 ▪ to a result after 20 iterations (set by default in 
Excel [CFI 2022]).
As part of the impact analysis, the Tool analyzes the dataset to 
gauge the contributions of the key input parameters or variables 
(such as the capital investment, charging fees, parking charges, 
capital subsidy, cost of electricity, land rental, average daily 
active use of charging units, and other O&M costs) to the 
project’s net cash inflow. Based on the data input by the users 
on the input pages, the table and the corresponding graph of 
the contributions of the key input parameters or variables are 
automatically updated in the Tool and reflected in the displayed 
results. The key factors influencing the input parameters are 
listed alongside the input parameters in the table. The Tool also 
predicts possible changes in the project IRR value with ±10 and 
±20 percent variation in the values of the key input parameters 
compared to their original, or base-case, values using the 
sensitivity (what-if ) analysis. The given variation range is 
considered reasonable for studying the uncertainty in the 
project IRR associated with changes in the key input variables. 
For investment in public charging infrastructure, the key input 
variables are the capital investment, charging fees, capital 
subsidy, cost of electricity, land rental, other O&M costs, and the 
average daily active use of the charging units. The Tool is able to 
auto-generate the results without user intervention.
The sensitivity analysis is helpful for the stakeholders of the 
charging infrastructure ecosystem because the values of the 
input parameters constantly evolve depending on market 
developments, consumer preferences, and government 
regulations. This feature of the Tool will enable stakeholders to 
easily forecast the likely fluctuations in the project IRR. 
Revenue profile 
Figure 6 shows a sample “Revenue Profile” page. Based on the 
data input by users on the input pages, the table and the
Figure 6  |   A sample “Revenue Profile” page 
Source: Financial Analysis of Charging station (FACt) tool developed by WRI India.
Note: The purpose of the above figure is to help in referring to the particular page of the Excel tool.
User Guide Pre-set Inputs Cost Dissection Project IRR & Sensitivity Revenue Profile Input Data Table Output Data TableSolverUser Inputs
Revenue Profiles
Page description: This output sheet shows the projection of the possible incomes for the CPO, the power distribution utility, and the land-owning entity over the project duration 
of 10 years. Moreover, the specific years in the project period that are envisaged to register a positive net cash inflow for the CPO will automatically appear in green, indicating 
that the breakeven for the project has been achieved at the given point in time.
Print
Cashflows                                     Year 
Gross Revenue for the CPO
Net Cash Inflow for the CPO
Revenue for Electricity Distribution Utility
Revenue for Land Owner
Cumulative over
10-year period Year 0 Year 1 Year 2 Year 3 Year 4 Year 5 Year 6 Year 7 Year 8 Year 9 Year 10
032097005 1842858 2029248 2273677 2549850 2861968 3214787 3613696 4064801 4575017 5071103
-751245- 1926000- 256477- 137470- 87950- 28425 42623 126922 199938 287682 390446 637465
169744750 1142041 1132471 1249121 15278041380266 1693883 1880937 2091723 2329362 2546868
40586080 217985 246978 279826 317042 359209 406984 461113 522441 591925 655106
-3000000
-2000000
-1000000
0
1000000
2000000
3000000
4000000
5000000
6000000
Year 0 Year 1 Year 2 Year 3 Year 4 Year 5 Year 6 Year 7 Year 8 Year 9 Year 10
Revenue Trend
Gross Revenue for the CPO Revenue for Electricity Distribution Utility Revenue for Land Owner Net Cash Inflow for the CPO

TECHNICAL NOTE   |  March 2023  |  15
Financial Analysis of Charging station (FACt)
corresponding graph representing the revenue trends for 
the entire project duration are automatically updated in the 
displayed results. 
The Tool projects the gross revenue and net cash inflow for the 
CPO, the revenue for the distribution utility, and the revenue 
for the land-owning entity over the project duration. This is to 
give a sense of the possible revenues for the actors involved in 
the implementation of a PCS. It is considered an important 
insight for implementing agencies, regulators, city authorities, 
and policymakers.
Moreover, the specific years in the project period that are 
envisaged to register a positive net cash inflow for the CPO will 
automatically appear in green, indicating that the breakeven for 
the project has been achieved. This visual representation would 
help users easily identify the break-even year if it is within the 
project duration of 10 years. 
Solver 
Figure 7 shows a sample “Solver” page. Solver shows the 
required changes in the values of the different input variables 
that in combination will help achieve the benchmark project 
IRR or the hurdle rate (if the project IRR in the base case 
falls short of the target). With the click of a button, the Tool 
produces the required results. While carrying out the iterations, 
Solver takes into account the individual contributions of the 
input variables to the project IRR as reflected in the earlier 
section (the “Project IRR & Sensitivity” page) of the Tool. 
Boundary conditions have also been imposed on the Solver 
function to ensure that the results from the permutations and 
combinations of the input variables are realistic. 
In addition, on this page, the user can conduct sensitivity 
analyses by varying the input parameters over any range. 
Figure 7  |   A sample “Solver” page
Source: Financial Analysis of Charging station (FACt) tool developed by WRI India.
Note: The purpose of the above figure is to help in referring to the particular page of the Excel tool.
User Guide Pre-set Input s Cost Dissection Project IRR & Sensitivity Revenue Profile Input Data T able Output Data T ableSolverUser Inputs
Scenario Analysis to Find the Scenario in Which the Benchmark Project IRR is Achieve d
Page description: This output sheet shows the percentage changes in the values of the input variables required to achieve the b enchmark project IRR or the hurdle rate □
(if the project IRR in the base case falls short of the target). Print
Current Project Internal Rate of Retur n -4 .35%
Benchmark Rate of Return/Hurdle Rat e 13.00%
Input Variables Required Changes
in Input Variables Resulting Project IRR (% )
So lv er
0.00%Capital Investment
-4.35%
Charging Fees 0.00%
Parking Charge s0 .00%
Capital Subsid y0 .00%
Cost of Electricity 0.00%
Land Rental 0.00%
Average Daily Active Use of Charging Units 0.00%
Other Operational & Maintenance Cost s0 .00%
Solve Restore

16  |  
  
 ▪ Explore: Visit the “Revenue Profile” page to check the 
10-year projection of the potential incomes of the CPO, the 
power distribution utility, and the land-owning entity. The 
years registering a positive net cash inflow for the CPO will 
automatically appear in green, indicating the breakeven for 
the project. The break-even point of the investment can also 
be found from the auto-generated chart, at the point where 
the line plot of the net cash inflow of the CPO crosses the 
X-axis;14 that is, the “0” mark on the Y-axis.15
 ▪ Apply: Click the Solve button on the “Solver” page if the 
resulting project IRR falls below the hurdle rate. A command 
box will pop up with the following text: “Solver has found 
a solution. All constraints and optimality conditions are 
satisfied.” Two options are available: (i) “Keep the Solver 
Solution” or (ii) “Restore Original V alues,” where the default 
selection is Option (i). Click the Ok button to display the 
results. If the project IRR is “null,” input values under the 
column “Required Change” against the input parameters 
such that the resulting project IRR changes to a non-null 
value. Even a negative project IRR value will suffice. Then 
click the Solve button, and repeat the above steps. To refresh 
the page, click the Restore button.
 ▪ Understand: Check the “Input Data Table” and “Output 
Data Table” pages for more details about the different types 
of required inputs and the produced outputs.
 ▪ Learn: Download and read the Technical Note available on 
the website for more information about FACt, including the 
applied methodology.
BEHIND THE CURTAIN: HOW 
THE TOOL WORKS
Figure 8 shows how the broad logic of the Tool works at the 
back end of the given input and output pages, linking the 
different input and output parameters.
Formulas for calculating  
different parameters
Dissecting the cost
The Tool disaggregates the project cost into major components 
and their sub-components, both up-front and recurring, and 
estimates them for the 10-year project period. Moreover, the 
estimated costs are expressed per unit of dispensed 
electricity; that is, as
Steps to use the tool effectively
The user should follow these steps in the following sequence 
and consult the specific guidance given on the relevant 
worksheets or pages:
 ▪ Access: Download the Excel file of FACt from WRI 
India's Electric Mobility practice area page (https://www.
wricitiesindia.org/content/electric-mobility) and check the 
background details and tutorial video on the website.
 ▪ Familiarize: After opening the Excel file and enabling the 
Editing and Macros options (see the commands at the top 
of the file), visit the “User Guide” page for a description of 
the Tool and instructions on how to use it. For information 
on the required inputs and available outputs, visit the “Input 
Data Table” and “Output Data Table” pages, respectively. 
When the Excel file is first opened, a security alert from 
Microsoft is triggered as the file contains VBA code. To 
unblock the file, go to the folder where the file is saved. 
After right-clicking the file, choose Properties from the 
context menu. Select the Unblock checkbox at the bottom of 
the General tab and click OK. This permission needs to be 
given only once.
 ▪ Start: Click the Start button on the “User Guide” worksheet 
to open the “User Inputs” page along with the “Pre-set 
Inputs” worksheet.
 ▪ Provide: Follow the instructions to enter the requested 
inputs on the “User Inputs” page and, if required, click the 
Clear All Inputs button at the bottom of the worksheet to key 
in a fresh set of input values.
 ▪ Validate: Click the Check Pre-set Inputs button to visit the 
“Pre-set Inputs” worksheet and ascertain whether the default 
input values are appropriate for the required analysis; if not, 
change the input values accordingly. If required, the default 
values can be restored by clicking the Restore Default Inputs 
button at the bottom of the page.
 ▪ Generate: Press the Check Results button on the  
“Pre-set Inputs” page to produce the results and open the 
first of the four output-related pages.
 ▪ Visit: Explore the “Cost Dissection” worksheet to understand 
the project cost composition and annual operating cost over 
the 10-year operation of the PCS.
 ▪ See: Go to the “Project IRR & Sensitivity” page for results 
on the project IRR, the impact of the key input variables, 
and sensitivity analysis. While considering the results from 
the sensitivity analysis, ensure that the "Solver" is not used 
simultaneously (i.e., the values under “Required Change” 
against individual input parameters should remain 0 percent). 
Otherwise, the standard sensitivity results will change.
∑N cinn=0
∑N Enn=0

TECHNICAL NOTE   |  March 2023  |  17
Financial Analysis of Charging station (FACt)
Figure 8  |   Overview of the functioning of the Tool
Composition of entailed cost to set 
up and run a PCS
Project IRR, contribution of input 
parameters to project’s net cash 
inflow, and sensitivity analysis
Projection of possible incomes for 
CPO, the distribution utility and 
land-owning entity
Necessary changes in 
input variables to achieve 
benchmark rate of return
Cost Dissection Project IRR & 
Sensitivity Revenue Profile
Outputs
Total Revenues
Capital Costs
Total Costs
Other Costs
O&M Costs
Solver
Income & Support
 ▪ Charging/Swapping Fees 
 ▪ Parking Charges
 ▪ Non-Core Businesses 
 ▪ Capital Subsidy
Charging Equipment 
Data
 ▪ Number of Charging  
Units by Type 
 ▪ Average Daily Active Use 
of Charging Unit
 ▪ Charger Power Ratings
 ▪ Charger Efficiency
 ▪ Cost of Charging 
/Swapping Unit
 ▪ Cost of Civil Work
 ▪ Installation & 
Commissioning Cost
 ▪ EVSE Management 
Software Cost
Ancillary Equipment 
Data
 ▪ Power Demand
 ▪ Power Demand Threshold
 ▪ Cost of DT
 ▪ Meter Cost
 ▪ Installation Cost
Electricity Distribution 
Utility Data
 ▪ SLDC
 ▪ Electricity Consumption
 ▪ Energy Charge
 ▪ Demand Charge
 ▪ Power Factor
Land Owning Entity Data
 ▪ Total Land Requirement
 ▪ Land Rental
Other O&M Data
 ▪ Daily Operational Time
 ▪ Annual Operational Days
 ▪ Time for Planned 
Maintenance
 ▪ Annual Maintenance Cost
 ▪ Insurance Cost
 ▪ Operator Cost
Taxes
 ▪ Corporate Tax
 ▪ MAT
Financing
 ▪ Debt
 ▪ Interest on Term Loan
 ▪ Loan Repayment Period
Depreciation
INPUT
Source: WRI India authors.

18  |  
  
where:
CF0 = The capital investment or outlay in the project; that is, the 
up-front investment expected to be incurred to set up a PCS
The capital investment cost usually covers the capital needed to 
build the charging station:
Capital investment = Cost of Charger/Battery Swapping System 
+ Cost of Ancillary Electrical Infrastructure
(Note: These costs are used to calculate the investment and are 
exclusive of Goods & Services Tax (GST).) 
CF1, CF2, CF3 … CFn = Cash flows; that is, all the possible 
incomes or cash inflows (including the capital subsidy) and 
one-time as well as recurrent expenditures for setting up and 
operating a PCS
n = Each period; that is, one year in this case
N = The project period; that is, the contract period to operate the 
PCS, which is considered 10 years
The given IRR formula can be applied in Excel using 
the IRR function. 
The IRR for a project is typically compared with the investor’s 
hurdle rate or cost of capital, and the project is considered 
investment-worthy if the IRR equals or exceeds the cost of 
capital. The hurdle rate, as explained previously, is the minimum 
required rate of return or target rate that the investor expects 
to realize on an investment. The Tool allows the user the 
flexibility of setting a different hurdle rate for benchmarking 
the project IRR. 
The cash inflows include the following:
 ▪ Income from EV charging fees
 ▪ Charging Fee Revenue = (Number of Charging Units × 
Charger Power Rating × (Average Daily Active Use of 
Charging Unit ÷ Number of Daily Operational Hours × 
100) × (Number of Daily Operational Hours × Number 
of Annual Operational Days) × (1 − Time for Planned 
Annual Maintenance)) × Charging or Swapping Fee Rate
(Note: This formula must be separately applied to each 
of the different charging unit types to arrive at the 
cumulative charging fee revenue)
 ▪ Income from parking charges (if applicable)
 ▪ Income from Parking Charges = (Number of Charging 
Units × (Average Daily Active Use of Charging Unit 
÷ Number of Daily Operational Hours × 100) × (Number 
of Daily Operational Hours × Number of Annual 
Operational Days) × (1 − Time for Planned Annual 
Maintenance)) × Hourly Parking Charges
 ▪ Net income from secondary sources or non core 
businesses such as advertisements (if applicable)
 ▪ Capital subsidy from the government (if applicable)
On the other hand, cash outflows cover the following:
 ▪ Cost of electricity 
Cost of electricity = (Energy Charge per kWh × Annual 
Electricity Consumption) + (Demand Charge per kVA 
Month × Power Demand of the Charging Station  
× Number of Months)
 ▪ Land rental 
The land rental, when fixed on a monthly basis, can be 
calculated as follows: 
Land Rental = Total Monthly Land Rental  
× Number of Months 
When linked to electricity consumption, land rental can 
be calculated as follows:
Land Rental = Annual Electricity Consumption × Rate of 
Land Rental per Unit of Electricity Consumption
 ▪ Other O&M costs 
Other O&M Costs = Annual Maintenance Costs  
+ EVSE Management Software Cost + Insurance Cost 
+ Operator Cost 
Here, annual maintenance costs are calculated as a 
percentage of the cost of chargers and of the DT . The cost
where: 
Cin = Cost due to item i in the nth year of the project
En = Total dispensed electricity in the nth year of the project
N is the total project period; that is, 10 years.
Estimating the project IRR
The formula for calculating the project IRR is as follows:
0 = CF0 + (1 + IRR)
CF1
(1 + IRR)2
CF2
(1 + IRR)3
CF3 ...+ + + (1 + IRR)n
CFn+
That is, ∑
N
n=0
= 0(1 + IRR)n
CFn

TECHNICAL NOTE   |  March 2023  |  19
Financial Analysis of Charging station (FACt)
 ▪ of the EVSE management software is pegged at ₹1 
per unit of dispensed electricity. The insurance cost is 
calculated as a percentage of the cost of the chargers. The 
operator cost comprises the costs of staffing the PCS. If 
the facility is crewless, there is a fixed cost for periodic 
checking and troubleshooting.
 ▪ Taxes (set in accordance with the applicable tax regime) 
    Corporate tax 
    MAT16 
(Note: GST is not considered as it is directly passed on 
to EV customers.)
 ▪ Interest on the term loan and depreciation are also duly 
accounted for in accordance with standard practice.
Gauging the contribution of key 
input parameters
To evaluate the contribution of a key input parameter or variable 
to the net cash inflow, the Tool calculates its cumulative share 
(in the form of a cash inflow or outflow) in the aggregate net 
cash inflow or income for the project over the entire project 
period; that is, as
where: 
CFi = Cash inflow or outflow due to item i
CF = Absolute value of all cash flows
Undertaking sensitivity (what-if) analysis
Based on the given key input variables and the sensitivity range, 
the analysis is carried out using the Data Table function of 
“What-If Analysis” in the Data tab of Excel.
Projecting potential revenue for  
concerned stakeholders
The Tool utilizes the parameters considered in the project IRR 
calculation to forecast the possible incomes of the CPO, the 
power distribution utility, and the land-owning entity over the 
project contract period of 10 years. Accounting for the gross 
and net revenues from the PCS is straightforward for the 
CPO because these are already included in the project IRR 
calculation. To estimate the revenue for the power distribution 
utility from the PCS, the Tool considers the value of the “Cost 
of Electricity,” which is a cash outflow item in the project IRR 
computation. Similarly, the revenue for the land-owning entity 
from the PCS is equal to the “Land Rental,” which is accounted 
as a cash outflow item in the project IRR calculation.
Executing Solver
The Tool employs the Solver function (under the Data tab), an 
Excel add-in, but simplifies the execution by applying Excel 
macros to give users a hassle-free experience.
CAVEATS FOR THE USER
Despite the well-thought-out approach to formulating 
and designing the Tool, rigorous user testing, and prompt 
troubleshooting, the following limitations (or risks) of the Tool 
have been identified. 
Limited quality risk
FACt requires the user to provide a limited number of 
mandatory inputs and validate or change a set of default input 
values. Detailed guidance is available if the user needs it. Also, 
the data validation function of Excel has been applied on the 
input worksheets to flag and prevent inappropriate data inputs. 
The analytical framework employed in the Tool is an industry 
standard. However, there could still be an element of risk if the 
user provides data inputs that do not appropriately reflect the 
context, in spite of the given guidance. This situation is beyond 
the control of the Tool. 
Avoidable usage glitches
On the “User Guide” page of the Tool, specific caveats have been 
given. The user should be aware of the following:
 ▪ Macros should be enabled in the Trust Settings after 
opening the Excel file; otherwise, some functions of the 
Tool will not work.
 ▪ The Tool should be run in a device with an active Microsoft 
Office license. Office 2016 or any later version of MS Office 
is recommended.
 ▪ The Mac operating system (macOS) should be avoided 
as some features of the Tool such as Solver may not 
function properly.
 ▪ When the Excel file of the Tool is opened for the first time, 
a security alert from Microsoft could be triggered, as the 
file contains VBA code. Permission to open the file has to 
be granted using the process laid down by Microsoft. The 
required guidance has been provided in this Technical Note.
 ▪ In case of difficulty in viewing the texts on the pages 
of the Tool, the worksheet sizes should be adjusted by 
zooming in or out.
∑N CFinn=0
∑N CFnn=0

20  |  
  
Need for understanding EV  
charging infrastructure
To use FACt effectively, it is recommended that the user have a 
fundamental understanding of PCS operations before applying 
it. Going through the literature on public charging infrastructure 
may be useful in this regard.
After taking these few precautions and with suitable 
preparation, the user can use the Tool effectively without 
any difficulty.
DISCLAIMER
The purpose of this tool is to help develop a foundational 
understanding of PCS finances. This application should not 
be considered a one-stop-solution for assessment of and/or 
decision-making regarding an existing or proposed project or 
investment. The functions of the Tool and the produced results 
are the sole responsibility of the users of this tool. Neither 
WRI India nor the creators of the Tool can be held, directly or 
indirectly, responsible or accountable for the use of this tool  
and/or the results. The Tool uses some third-party information, 
the source of which should be independently verified by users.

TECHNICAL NOTE   |  March 2023  |  21
Financial Analysis of Charging station (FACt)
APPENDIX A
Table A-1  |  Input data table 
INPUTS UNITS OF THE INPUTS SOURCES OF INPUT 
DATA COLLECTION PURPOSE GUIDANCE FOR USERS
User Inputs worksheet
Number of  
charging units
- To consider the public charging station 
(PCS) configuration that will impact 
capital expenditures (CAPEX) and 
operating expenses (OPEX)
The user has to enter positive integral 
values for each type of charging unit.
Average daily active 
use of charging unit in 
year 1 of operation
Hours per day - To calculate the income and operational 
cost of the charge point operator (CPO) 
and revenues of the distribution utility 
and land-owning entity
The user has to enter a numerical value 
for each type of charging unit. Note 
that the daily active use of a charging 
unit refers to the daily number of hours 
for which the unit is being used, or is 
expected to be used, for EV charging. 
The number of hours of active use of 
a charging unit is different from (and 
less than) the daily operational hours of 
the charging facility. The active use of 
a charging unit, which depends on the 
demand for EV charging at the facility, 
helps estimate its capacity utilization. 
For example, if a charging unit is in active 
use for 4 hours a day on average out of 
the daily operational hours (16 hours), its 
capacity utilization would be 25%  
(4/16 × 100).
Charging 
/swapping fees
₹/kWh - To calculate the CPO’s income The user has to enter a value for each 
type of charging unit used in Year 1. 
These fees are exclusive of GST. The 
following are some suggested values for 
charging/swapping fees per kWh:
- ₹7 to ₹11 for slow and moderately fast 
(AC) chargers
- ₹12 to ₹18 for fast (DC) chargers
- ₹30 to ₹40 for battery swapping.
Energy charge ₹/kWh - To calculate the CPO’s operational cost 
and the distribution utility’s revenues 
The user has to enter the value 
applicable for Year 1. It is recommended 
to consider the landed cost or all-in rate 
of electricity (i.e., inclusive of taxes and 
other state-levied charges). The energy 
charge and other charges vary from 
state to state. Information on the energy 
charge and other state-levied charges 
and taxes can be obtained from the state 
tariff orders, which are usually available 
on the websites of State Electricity 
Regulatory Commissions or distribution 
companies (DISCOMs).

22  |  
  
INPUTS UNITS OF THE INPUTS SOURCES OF INPUT 
DATA COLLECTION PURPOSE GUIDANCE FOR USERS
Demand charge ₹/kVA month - To calculate the CPO’s operational cost 
and the distribution utility’s revenues
The user has to enter the value 
applicable for Year 1. The user must also 
ascertain whether a demand or fixed 
charge is applicable to the PCS. This 
depends on state regulations and hence 
varies from state to state. Information on 
the demand charge can be obtained  
from the state tariff orders, which are 
usually available on the websites of the 
State Electricity Regulatory Commissions 
or DISCOMs.
To convert kW to kVA, divide kW by the 
power factor.
Monthly fixed  
land rental
₹ - To calculate the CPO’s operational cost 
and the land-owning entity’s revenues 
The user has to enter the value 
applicable for Year 1 only if the land rental 
is based on the area requirement.
Land rental rate 
per electricity 
consumption
₹/kWh - To calculate the CPO’s operational cost 
and the land-owning entity’s revenues 
The user has to enter the value 
applicable for Year 1 only if the land rental 
is set per unit of electricity consumption.
Available total  
capital subsidy
₹ - To calculate the project internal rate of 
return (IRR)
The user has to enter this input if a 
capital subsidy is applicable. The 
total amount of direct capital subsidy 
applicable to the PCS under central  
 and state/city schemes must be 
considered. This amount is not 
refundable. Information on capital 
subsidy is available in EV policies or 
scheme documents.
Pre-set Inputs  worksheet
Power rating of the 
charging unit 
kW  ■ Charging 
infrastructure 
guidelines issued 
by the Ministry of 
Power, Government 
of India 
 ■ Portal on charger 
products that are 
commonly available 
in the market
To calculate the electricity consumption 
and power demand at a PCS
The user has to enter values for other 
types of charging units.
Caveat: The Tool assumes that the 
charging units are used at their rated 
output power levels. In reality, the 
effective power level during a charging 
session could drop below the rated 
power, depending on the recommended 
C-rate of the EV’s battery (if a DC 
charging unit is used) and the power 
rating of the vehicle’s on-board charger 
(if an AC charging unit is used).
Cost per charging 
/swapping unit 
₹ Stakeholder 
consultation
To calculate the CPO’s capital costs The user has to enter values for other 
types of charging units.
Cost of civil works as a 
percentage of the total 
cost of the charging 
system (%)
Assumption based 
on stakeholder 
consultation
To estimate the CPO’s capital costs The user has to enter a numerical value 
without the % symbol. The charging 
system refers to the charging units to be 
installed at the PCS, including a stack 
battery charging system, if any.

TECHNICAL NOTE   |  March 2023  |  23
Financial Analysis of Charging station (FACt)
INPUTS UNITS OF THE INPUTS SOURCES OF INPUT 
DATA COLLECTION PURPOSE GUIDANCE FOR USERS
Installation and 
commissioning costs 
as a percentage of 
the total cost of the 
charging system (%)
Assumption based 
on stakeholder 
consultation
To estimate the CPO’s capital costs The user has to enter a numerical 
value without the % sign. The charging 
system refers to the charging units to be 
installed at the PCS, including a stack 
battery charging system, if any.
Power factor of the 
electricity connection
Based on industry 
practice; the 
information can be 
obtained from the 
serving DISCOM.
To convert values expressed in kW to 
kVA and vice versa
The power factor is a measure of how 
effectively the incoming power is used 
in an electrical system. A high power 
factor indicates that the power supplied 
to the electrical system is effectively 
used. A system with a low power factor 
consumes the incoming electricity 
supply inefficiently, resulting in losses. 
Cost of the distribution 
transformer (DT) and 
associated equipment 
per 50 kVA rated 
capacity
₹ Cost Data Sheet of 
BESCOMa
To estimate the up-front installation cost 
of the PCS
Apart from the DT’s cost, this includes the 
cost of earthing, the high tension  
/low tension (HT/LT) panel, cabling 
and trenching, and local distribution 
panels. These costs are incurred if a HT 
connection is necessary.
Meter cost ₹ ISGF White Paperb To estimate the up-front installation cost 
of the PCS
The cost does not include the  
installation cost.
Ancillary electrical 
infrastructure 
installation cost 
(including labor)
₹ Cost Data Sheet of 
BESCOMa
To estimate the up-front installation cost 
of the PCS
Daily operational hours Considered 24 hours 
by default
To calculate the CPO’s income and 
operational cost, and the distribution 
utility and land-owning entity’s revenues 
The value could be less than 24 hours  
if the PCS is set up inside a host  
 facility, depending on the facility’s 
operational time.
Annual operational 
days
Considered 365 days 
by default
To calculate the CPO’s income and 
operational cost, and the distribution 
utility and land-owning entity’s revenues 
Planned maintenance time is by default 
taken into account in the calculation, and 
hence, the operational days need not be 
adjusted for maintenance requirements.
Parking charges ₹/hour Considered not 
applicable by default
To calculate the CPO’s income The user has to enter the values 
applicable for Year 1 for each type of 
charging unit. Parking charges are 
commonly applicable to slow/moderately 
fast chargers.
Secondary net revenue 
for the CPO from non 
-core business
₹/month Considered not 
applicable by default
To calculate the CPO’s income If applicable, the user has to enter the 
net revenue for Year 1 from secondary 
income sources such as advertisements, 
public convenience facilities, and 
refreshment kiosks. The net revenue 
should not take into account the costs 
attributed to the operation of the PCS.

24  |  
  
INPUTS UNITS OF THE INPUTS SOURCES OF INPUT 
DATA COLLECTION PURPOSE GUIDANCE FOR USERS
Power demand 
threshold for an 
exclusive DT
kVA The default value of 118 
kVA (100 kW) is taken 
from the 
Delhi Supply Code 
Regulationc
To determine the requirement for a 
dedicated DT at a PCS 
This input value depends on state 
regulations and hence varies from state 
to state. The information can be obtained 
from the applicable State Electricity 
Supply Code Regulations.
Charger efficiency (%) Stakeholder 
consultation
To calculate the electricity consumption 
at a PCS
The user has to enter a numerical value 
without the % symbol.
Time for planned 
annual maintenance 
(%)
Assumption based 
on stakeholder 
consultation
To estimate the effective operational 
time of the PCS, which impacts the CPO’s 
operational cost and income, and the 
distribution utility’s revenues
The user has to enter a numerical value 
without the % symbol.
Auxiliary electricity 
consumption (%)
Assumption based 
on stakeholder 
consultation
To calculate the electricity consumption 
at a PCS
The user has to enter a numerical 
value without the % symbol. Auxiliary 
electricity consumption is related to 
other electrical end uses at the PCS, such 
as for illumination at the site.
Annual maintenance 
costs as a percentage 
of the cost of the core 
hardware (%)
Based on industry 
practice
To calculate the CPO’s other operational 
and maintenance (O&M) costs
The user has to enter a numerical value 
without the % symbol.
Cost rate for electric 
vehicle supply 
equipment (EVSE) 
management software
₹/kWh Assumption based 
on stakeholder 
consultation
To calculate the CPO’s other O&M costs
Insurance cost as a 
percentage of the total 
cost of the charging 
system (%)
Assumption based 
on stakeholder 
consultation
To calculate the CPO’s other O&M costs The user has to enter a numerical value 
without the % symbol.
Hourly total operator 
cost if the PCS is 
staffed
₹/hour The default value 
is ₹65 per hour 
according to the 
minimum wage 
limit notified by the 
Ministry of Labour 
& Employment, 
Government of India. 
However, the value 
varies from city to city 
and from state 
 to state.d
To calculate the CPO’s other O&M costs The user has to enter the value 
applicable for Year 1. The total operator 
cost (which depends on the number of 
operators deployed) per hour must be 
considered if the PCS is staffed.
Minimum alternate 
annual operator cost if 
the facility is crewless 
₹ Assumption based 
on stakeholder 
consultation
To calculate the CPO’s other O&M costs Note that an operator may be required  
for troubleshooting at a PCS even  
if it is crewless. A lump-sum cost has 
been considered.
Debt as a percentage 
of the capital 
investment (%)
Based on the standard 
accounting method
To estimate the yearly interest on the 
term loan to be paid out as part of debt 
financing for the EV charging business
The user has to enter a numerical value 
without the % symbol.

TECHNICAL NOTE   |  March 2023  |  25
Financial Analysis of Charging station (FACt)
INPUTS UNITS OF THE INPUTS SOURCES OF INPUT 
DATA COLLECTION PURPOSE GUIDANCE FOR USERS
Construction period Months For accounting 
purposes, it is 
considered 12 months; 
i.e., one full year
To estimate the yearly interest on the 
term loan to be paid out as part of debt 
financing for the EV charging business
Loan repayment 
period
Years Based on the 
commonly used 
lending practice
To estimate the interest on the term loan 
to be paid out as part of debt financing 
for the EV charging business
Rate of interest on 
loan (%)
The default value is 
15%, in accordance 
with the State Bank 
of India’s benchmark 
prime lending 
rate. However, the 
value may change 
depending on the 
marginal cost of funds 
based lending rate 
(MCLR) of the bank and 
the credit score of the 
borrower.
To estimate the yearly interest on the 
term loan to be paid out as part of debt 
financing for the EV charging business
The user has to enter a numerical value 
without the % symbol. If there is no debt, 
0 must be entered. If multiple lenders are 
involved, the weighted average lending 
rate must be considered.
Service-line-cum  
-development charge 
paid for a new 
electricity connection 
application 
₹/kW The default charge is 
₹1,500/kW. However, 
this value depends 
on state regulations 
and hence varies from 
state to state. The 
required information 
can be obtained from 
the serving DISCOM e
To estimate the up-front PCS installation 
cost and the distribution utility’s revenue 
This is the one-time charge that a 
consumer has to pay to the serving 
electricity distribution utility when 
applying for a new electricity connection; 
this charge varies from state to state. 
The amount is usually linked to the 
sanctioned load (kW) for the connection.
Corporate tax rate (%) The default rate is 
25%. However, the 
Ministry of Finance 
and Corporate Affairs, 
Government of India, 
can change this valuef
To estimate the net income/profit from 
the PCS operation
The user has to enter a numerical value, 
if applicable, without the % symbol.
Minimum alternate tax 
(MAT) rate (%)
Cleartax f To estimate the net income/profit from 
the PCS operation 
GST on service is not considered as it is 
directly passed on to the EV customers.
Hurdle rate or 
benchmark rate of 
return (%)
By default, the State 
Bank of India’s 
benchmark prime 
lending rate (BPLR) at 
a given point of time 
is taken into account, 
which is currently 
about 13%. The value 
changes with time. g
To check whether the project IRR crosses 
the benchmark rate and thus determine 
whether the charging business is 
profitable or not; to understand the 
changes in the values of the key input 
parameters to achieve the benchmark 
rate, using the tool feature Solver (if the 
project IRR in the base case falls short of 
the target)
This is to enable comparison with 
the resulting project IRR to assess 
the business attractiveness of the 
investment in the PCS. The user has to 
enter a numerical value, if applicable, 
without the % symbol.
Escalation of the 
electricity rate (%)
Assumption based 
on stakeholder 
consultation
To calculate the CPO’s operational cost 
and the distribution utility’s revenues 
over a 10-year period
The user has to enter a numerical value 
without the % symbol.

26  |  
  
INPUTS UNITS OF THE INPUTS SOURCES OF INPUT 
DATA COLLECTION PURPOSE GUIDANCE FOR USERS
Land rental 
 escalation (%)
Assumption based 
on stakeholder 
consultation
To calculate the CPO’s operational cost 
and the land-owning entity’s revenues 
over a 10-year period
The user has to enter a numerical value, 
if applicable, without the % symbol.
Escalation of other 
O&M costs (%)
Assumption based 
on stakeholder 
consultation
To calculate the CPO’s other O&M costs 
over a 10-year period
The user has to enter a numerical value 
without the % symbol.
Escalation of the 
charging fees (%)
Assumption based 
on stakeholder 
consultation
To calculate the CPO’s income over a 
10-year period
The user has to enter a numerical value 
without the % symbol.
Escalation of the 
hourly parking  
charges (%)
Assumption based 
on stakeholder 
consultation
To calculate the CPO’s income over a 
10-year period
The user has to enter a numerical value 
without the % symbol.
Increase in secondary 
revenue (%)
Assumption based 
on stakeholder 
consultation
To calculate the CPO’s income over a 
10-year period
The user has to enter a numerical value 
without the % symbol.
Increase in the 
average daily active 
use of charging 
units (%)
Assumption based 
on stakeholder 
consultation
To calculate the CPO’s income and 
operational cost, and the distribution 
utility and land-owning entity’s revenues 
over a 10-year period
The user has to enter a numerical value 
without the % symbol.
Note:   
a BESCOM n.d.
b ISGF 2016
c DERC 2017
d Office of the Chief Labour Commissioner 2022
e PTI 2019
f Cleartax 2022
g SBI 2022

TECHNICAL NOTE   |  March 2023  |  27
Financial Analysis of Charging station (FACt)
Table A-2  |  Output data table
OUTPUTS TOOL PAGES ON WHICH THE 
OUTPUTS ARE DISPLAYED UNITS OF THE OUTPUTS GUIDANCE FOR USERS
Project cost breakup Cost Dissection ₹ The breakup of the total project cost over the project period 
shows the estimates for the major components and their 
sub components over the 10-year project period. The 
components include the following:
 ■ Capital investment
• Cost of charging equipment
• Cost of ancillary equipment
 ■ Cost of electricity
• Energy charges
• Demand charges
 ■ Land rental
 ■ Other operational and maintenance (O&M) costs
• Operator cost
• Electric vehicle supply equipment (EVSE) management 
software cost
• Miscellaneous expenses
 ■ Interest on term loan
Cost per unit of  
electricity dispensed
Cost Dissection ₹/kWh The 10-year costs for the given components are expressed 
per unit of dispensed electricity, which can be considered the 
buildup for the cost of the charging service over the entire 
project period.
Total annual operating cost 
of running a public charging 
station (PCS)
Cost Dissection ₹ Analysis of the annual operating cost shows estimates for the 
cost of electricity, land rental, and other O&M costs over the 
10-year operation of the PCS.
Project internal rate of return 
(IRR) (%)
Project IRR & Sensitivity The project IRR is a commonly employed indicator for  
evaluating the profitability of a potential investment. The 
Tool estimates the possible project IRR for a charge point 
operator (CPO) from the investment in setting up a PCS of 
a certain configuration in a given context. The underlying 
core methodology applied in the Tool for calculating it is the 
one widely used in the industry. Once the IRR for a project is 
determined, it is typically compared with the investor’s hurdle 
rate or cost of capital. If the IRR equals or exceeds the hurdle 
rate, the project is considered investment worthy.

28  |  
  
OUTPUTS TOOL PAGES ON WHICH THE 
OUTPUTS ARE DISPLAYED UNITS OF THE OUTPUTS GUIDANCE FOR USERS
Contribution of the key input 
parameters to the net cash 
inflow (%)
Project IRR & Sensitivity As part of the impact analysis, the Tool analyzes the dataset  
to gauge the contributions of the key input parameters or 
variables (such as capital investment, charging fees, parking 
charges, capital subsidy, cost of electricity, land rental, average 
daily active use of charging units, and other O&M costs) to  
the project’s net cash inflow. Based on the data input by users 
on the input pages, the table and the corresponding graph  
on the contributions of the key input parameters or variables  
are automatically updated in the Tool and reflected in the 
displayed results.
Sensitivity to the key input 
parameters (%)
Project IRR & Sensitivity The Tool predicts possible changes in the project IRR  
value with ±10% and ±20% variations in the values of the  
key input parameters compared to their original or  
base-case values using the sensitivity (what-if) analysis. 
The given range is considered reasonable for studying the 
uncertainty in the project IRR associated with changes in the 
key input variables. As far as investment in public charging 
infrastructure is concerned, the key input variables are the 
capital investment, charging fees, capital subsidy, cost of 
electricity, land rental, other O&M costs, and the average daily 
active use of charging units. The Tool is able to auto-generate 
the results without user intervention.
CPO’s gross revenue Revenue Profile ₹ The Tool analyzes the dataset to project the revenue trends 
(which include the CPO’s gross revenue and net cash inflow, 
the distribution utility’s revenue, and the land-owning entity’s 
revenue) over the entire project duration. This is to give a 
sense of the possible revenues for the actors involved in the 
implementation of a PCS. On the basis of the data input by the 
users on the input pages, the table and the corresponding graph 
representing the revenue trends for the entire project duration 
are automatically updated to show the results. 
CPO’s net cash inflow Revenue Profile ₹
Electricity distribution utility’s 
revenue 
Revenue Profile ₹
Land owner’s revenue Revenue Profile ₹
Required changes in input 
variables to achieve the 
benchmark rate of return 
/hurdle rate (%)
Solver Solver shows the required changes in the values of the different 
input variables that in combination will help achieve the 
benchmark project IRR or the hurdle rate (if the project IRR in 
the base case falls short of the target). While carrying out the 
iterations, Solver  takes into account the individual contributions 
of the input variables to the project IRR. Certain boundary 
conditions have also been imposed on the Solver  function to 
ensure that the results from the permutations and combinations 
of the input variables are realistic. With the click of a button, 
the Tool produces the required results. In addition, on this page, 
the user can conduct sensitivity analyses by varying the input 
parameters over any range.

TECHNICAL NOTE   |  March 2023  |  29
Financial Analysis of Charging station (FACt)
REFERENCES
Atlas Public Policy. 2019. “EV Charging Financial Analysis Tool.” April. 
https://atlaspolicy.com/ev-charging-financial- analysis-tool/.
BESCOM. n.d. “Cost Data Sheet.” https://bescom.karnataka.gov.in/
storage/pdf-files/Common%20SR%2016-17/CSR-16-17-CDS-1-23.pdf. 
Accessed January 9, 2023.
CFI (Corporate Finance Institute). 2022. “IRR Function.” Corporate 
Finance Institute. December 4. https://corporatefinanceinstitute.com/
resources/excel /irr-function/.
Cleartax. 2022. “Corporate Taxes.” February 1. https://cleartax.
in/s/corporate-tax.
Das, Shouvik, and Avishek Banerjee. 2022. “High Costs, Low Use May 
Derail Development of EV Charging Infra.” Mint, January 11. https://
www.livemint.com/industry/infrastructure/high-costs-low-use-may-
derail-development-of-ev-charging-infra-11641 878749850.html.
Deployment of Alternative Vehicle and Fuel Technologies Initiative. 
n.d. “EV Charging Financial Analysis Tool.” https://altfueltoolkit.
org/resource/ev-charging-financial-analysis-tool/. Accessed 
January 06, 2023.
DERC (Delhi Electricity Regulatory Commission). 2017. “DERC 
(Supply Code and Performance Standards) Regulations, 2017.” 
http://derc.gov.in/sites/default/files/Regulations-07.07.2017.
pdf#:~:text=%281%29%20These%20Regulations%20may%20be%20
called%20%E2%80%9CDelhi%20Electricity,consumers%20in%20
the%20National%20Capital%20Territory%20of%20Delhi.
IEA (International Energy Agency). 2022a.  Global EV Outlook 
2022. Paris: IEA.
IEA. 2022b. Policy Brief on Public Charging Infrastructure.  Paris: IEA.
ISGF (India Smart Grid Forum). 2016. AMI Rollout Strategy and Cost-  
Benefit Analysis for India . New Delhi: ISGF. https://indiasmartgrid.org  
/reports/AMI%20Roll-Out%20Strategy%20and%20Cost-Benefit%20
Analysis%20for%20India%20FINAL(1).pdf.
Ministry of Power–GoI (Government of India). 2022. Charging 
Infrastructure for Electric Vehicles (EV) – The Revised Consolidated 
Guidelines & Standards. New Delhi: Ministry of Power–GoI.
NREL (National Renewable Energy Laboratory). n.d. “EVI-FAST: 
Electric Vehicle Infrastructure – Financial Analysis Scenario Tool.” 
https://www.nrel.gov/transportation/evi-fast.html.  Accessed 
January 6, 2023.
ENDNOTES
1. The definition of a PCS depends on the guidelines issued by the 
Ministry of Power or any competent authority from time to time.
2.  Charging use cases may include charging at public parking 
areas, charging at destinations (e.g., shopping malls), on  
-the-go charging, community charging at shared residential and 
workplace facilities, and so on.
3.  It is responsible for setting up and running a PCS.
4.  Some blogs describe business opportunities in charging 
infrastructure without carrying out the required calculations. 
5.  These include EVI-FAST: Electric Vehicle Infrastructure  
 – Financial Analysis Scenario Tool (NREL, n.d.); EV Charging 
Financial Analysis Tool – Atlas Public Policy (Atlas Public Policy, 
2019); and EV Charging Financial Analysis Tool – Alternative Fuel 
Toolkit  (Deployment of Alternative Vehicle and Fuel Technologies 
Initiative, n.d.).
6.  One-on-one interactions with stakeholders such as charge point 
operators, distribution utilities, and real estate agencies occurred 
in April 2021. 
7.  The Masterclass was part of the Electric Mobility Forum, a 
platform for stakeholder engagement that was organized from 
September 13 to September 17, 2021. One of the sessions was 
“Charging Infrastructure Development.” 
8.  The project period is considered 10 years, in line with the 
procurement practices for setting up and operating PCSs in India. 
A detailed explanation is given in the “Cost Dissection” section 
of this document.
9.  The operation of the draft tool was demonstrated to players such 
as CPOs, real estate companies, and public sector undertakings.
10.  To convert kW to kVA, divide kW by the power factor. The default 
value of the power factor is given in Table A-1 in Appendix A.
11.  Along with other state-levied charges and taxes.
12. Dispensed electricity is the energy fed to charge EVs and is 
different from the electricity consumption at a PCS. It primarily 
depends on the power ratings (kW) and the average daily active 
use of the charging units (hours) and the yearly escalation rate 
of the latter. 
13.  Design, Build, Finance, Operate, Maintain, and Transfer of land 
(DBFOMT) is the fundamental implementation model for a PCS.
14.  The horizontal axis of the graph.
15.  The vertical axis of the graph.
16.  This special tax is to ensure that a commercial entity pays 
a minimum amount of tax even after enjoying the benefits of 
various deductions, exemptions, depreciation, and so on, on the 
income generated.

30  |  
  
ACKNOWLEDGMENTS
The authors would like to thank NITI Aayog, especially Sudhendu J. 
Sinha, Adviser (Infrastructure Connectivity – Transport and Electric 
Mobility) and Diewakarr Anupam Mittal, Young Professional (Electric 
Vehicles) for their support while this research was conducted. 
The authors also thank Dr. Indradip Mitra, Team Leader – E-mobility 
at Deutsche Gesellschaft für Internationale Zusammenarbeit (GIZ) 
GmbH (India), and Madhav Pai, Executive Director of WRI India Ross 
Center, for their encouragement.
The authors express gratitude to the following external reviewers 
(ordered by surname): Sanjana Chhabra (Manager – Policy, Advocacy 
and Government Relations, Statiq), Pushpendra Vishal Kaushal 
(former Business Operations Lead, Statiq), Sahana L (Energy Adviser, 
GIZ India), Chrishant Macwan (Senior Business Developer, System 
Level Solutions, and Senior Business Analyst, VerdeMobility), Anant 
Mehra (Product Head, Bolt), and N. Mohan (former Deputy General 
Manager, Head – EV Charging Infrastructure, Convergence Energy 
Services Limited).
The authors are also grateful to the following internal reviewers 
(ordered by surname): Garima Agrawal, Brittany Barrett, Logan Byers, 
Shahana Chattaraj, Sudeshna Chatterjee, Chaitanya Kanuri, Michelle 
Levinson, Sharvari Patki, Ashim Roy, and Ramesh S. 
In addition, the authors also thank Emilia Suarez (Publications 
Coordinator, Research, Data and Innovation, WRI) for her support 
on the publication, Avinash Dubedi for his guidance on formulating 
certain macros for the Tool, and Nikita Gupta, Garima Jain, Santhosh 
Matthew Paul, Visual Best, and Rama Thoopal, who supported 
the copyediting, design, and production of the Tool and the 
technical note.
This publication is part of NDC Transport Initiative for Asia (NDC-TIA). 
NDC-TIA is ably supported by International Climate Initiative (IKI). IKI 
operates under the leadership of the Federal Ministry for Economic 
Affairs and Climate Action, in close cooperation with its founder, the 
Federal Ministry of Environment and the Federal Foreign Office. For 
more details, visit: www.ndctransportinitiativeforasia.org.
Office of the Chief Labour Commissioner. 2022. “Revised VDA 
(Minimum Wages) wef 01 April 2022.” Government order. March 31. 
https://clc.gov.in/clc/node/690.
Pathak, Minal, and Shaurya Patel. 2021. “India Electric Vehicle: 
The Speed Bumps in India’s Electric Vehicle Drive That No One’s 
Talking About.” Economic Times, December 8, 2021.  https://
economictimes.indiatimes.com/industry/renewables/the-speed-
bumps-in-indias-electric-vehicle-ride-that-no-one-is-talking-about/
articleshow/8814462 5.cms?from=mdr.
PTI (Press Trust of India). 2019. “Service Line Development Charges in 
Non-electrified Areas Reduced: Delhi Govt.” Times of India, December 
31. https://.timesofindia.indiatimes.com/city/delhi/service-line  
-development-charges-in-non-electrified-areas-reduced-delhi-govt  
/articleshow/73050562.cms.
Sandalkhan, Bakatjan, Jennifer Carrasco, Aykan Gökbulut, and Yusuf 
Tash. 2021. “How Governments Can Solve the EV Charging Dilemma.” 
Boston Consulting Group. October 4. https://www.bcg.com/
publications/2021/electric-vehicle-charging-station -infrastructure  
-plan-for-governments.
SBI (State Bank of India). 2022. “Benchmark Prime Lending  
Rate – Historical Data – Interest Rates.” September 15. https://sbi.co.in  
/web/interest-rates/interest-rates/benchmark-prime-lending-rate-
historical-data.
Singh, Preetesh. 2021. “EV Charging Infrastructure in India – Current 
Status, Challenges and Way Forward.”  EVreporter (blog). September 
27, 2021. https://evreporter.com/ev-charging-infra structure-india  
-status-challenges/.
The World Bank. 2021. Electric Mobility in India: Accelerating 
Implementation. Washington, D.C The World Bank.

TECHNICAL NOTE   |  March 2023  |  31
Financial Analysis of Charging station (FACt)
This page is intentionally left blank.

Copyright 2023 World Resources Institute. This work is licensed under the Creative Commons Attribution 4.0 International License.  
To view a copy of the license, visit http://creativecommons.org/licenses/by/4.0/
  
1st Floor, Godrej & Boyce Premises, Gasworks Lane, Lalbaug, Parel  |  Mumbai 400012, India  |  wri-india.org
ABOUT THE AUTHORS
Shyamasis Das is a consultant with WRI India. For over 14 years, 
he has been dealing with core and cross-cutting energy and 
climate change issues and has supported several clean energy 
and electric mobility initiatives. He has an illustrious track record 
of supporting ministries, departments, and public agencies at the 
national and subnational levels, regulators, power distribution utilities, 
industries, multilateral and bilateral development organizations, 
international think tanks, and donor agencies. He has authored over 
15 publications and given talks at several national and international 
forums. Recently, he was invited by the International Energy 
Agency to present and participate in a panel discussion as part 
of the GEF Global E-Mobility Program. His hands-on experience 
is complemented by advanced academic pursuits. He has an 
international master's degree in Energy Management from a top-tier 
institute in France.
Contact: shyamasis.das@wri.org
Priya Bansal is Program Associate (Electric Mobility, Sustainable 
Cities and Transport) at WRI India. She conducts research and 
analysis relating to the impacts of the e-mobility transition on the 
automotive workforce. Her research also involves understanding the 
economics of charging infrastructure deployment and conducting 
financial analysis to understand the business case for setting up 
public charging infrastructure along with the different implementation 
models that can help overcome the associated challenges. Before 
joining WRI, she gained experience in market research and 
quantitative as well as qualitative data analysis while working at 
Kantar as a research manager for the technology consulting division. 
Priya holds a master’s degree in Economics from the National 
University of Singapore (NUS) and a bachelor’s degree in Economics 
from Sri Venkateswara College, University of Delhi. 
Contact: priya.bansal@wri.org
Pawan Mulukutla  is Director (Integrated Transport, Electric Mobility, 
and Hydrogen) at WRI India. Pawan leads the overall strategy, 
implementation, and partnerships to accelerate electric mobility 
and clean tech adoption by supporting the government at both the 
national and state levels in India. He also guides technical and policy 
research on electric mobility and green hydrogen. He holds a degree 
in Advanced Management Program from IIM-Bengaluru and an MS in 
Transport Engineering and Planning from Clemson University, South 
Carolina, United States.
Contact: pawan.mulukutla@wri.org
ABOUT WRI INDIA
WRI India is a research organization that turns big ideas into
action at the nexus of environment, economic opportunity, and 
human well-being.
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
Our rigorous analysis identifies risks, unveils opportunities, and 
informs smart strategies. We focus our efforts on influential 
and emerging economies where the future of sustainability 
will be determined.
CHANGE IT
We use our research to influence government policies, business 
strategies, and civil society action. We test projects with communities, 
companies, and government agencies to build a strong evidence 
base. Then, we work with partners to deliver change on the ground 
that alleviates poverty and strengthens society. We hold ourselves 
accountable to ensure our outcomes will be bold and enduring.
SCALE IT
We don’t think small. Once tested, we work with partners to adopt 
and expand our efforts regionally and globally. We engage with 
decision-makers to carry out our ideas and elevate our impact. We 
measure success through government and business actions that 
improve people’s lives and sustain a healthy environment.
