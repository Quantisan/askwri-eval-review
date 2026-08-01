---
doc_id: 2022_technical-note-for-a-dataset-of-us-school-bus_8896
source_pdf: kp-docs/askwri-kps/2022_technical-note-for-a-dataset-of-us-school-bus_8896.pdf
extraction_method: cache-plaintext
char_count: 60640
title: Technical Note for a Dataset of U.S. School Bus Fleets
authors: Lazer, Leah; Freehafer, Lydia; Wang, Jessica
date_published: 12/23/2022
article_type: Technical Note
sub_tag: Transport decarbonization
wri_primary_office: WRI US
wri_programs: Cities
language: English
url: "https://www.wri.org/research/technical-note-dataset-us-school-bus-fleets"
doi: "https://doi.org/10.46830/writn.22.00076"
summary: The dataset provides comprehensive information on over 475,000 school buses across 46 states and the District of Columbia, detailing characteristics such as model year, fuel type, and school district affiliation. Compiled through public records requests from state governments, the dataset aims to address significant gaps in knowledge regarding school bus fleets, which can inform environmental and equity analyses. Key applications include assessing the impact of transitioning to electric buses on greenhouse gas emissions and public health, as well as identifying districts with outdated diesel buses. Limitations include missing data from four states and inconsistencies in data collection methods across states. The dataset serves as a crucial resource for policymakers, researchers, and advocates focused on improving school transportation systems.
---

# Technical Note for a Dataset of U.S. School Bus Fleets

WO RL DWO RL D
RE SO UR CE SRE SO UR CE S
IN STIT UT EIN STIT UT E
TECHNICAL NOTE   |  Version 2.0  |  May 2024  |  1
CONTENTS
Abstract. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1
1. Introduction. . . . . . . . . . . . . . . . . . . . . . . . . . . . .1
2. Motivation .............................. 4
3. Methods ................................ 5
4. Limitations and Conclusion. . . . . . . . . . . .18
References ............................... 19
Endnotes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .19
Acknowledgments ...................... 22
About the authors. . . . . . . . . . . . . . . . . . . . . . . 22
About WRI  .............................. 22
Technical notes document the research or analytical 
methodology underpinning a publication, interactive 
application, or tool.
Suggested Citation: Lazer, L., L. Freehafer, and J. 
Wang. 2024. “Dataset of U.S. School Bus Fleets.” 
Technical Note. Washington, DC:  
World Resources Institutes. Available online at 
https://doi.org/10.46830/writn.22.00076.v2.
TECHNICAL NOTE
Dataset of U.S. School Bus Fleets
Leah Lazer, Lydia Freehafer, and Jessica Wang
ABSTRACT
This dataset contains detailed information on the composition of school bus 
fleets in the United States. The available data vary by state. For most states 
bus-level information, such as the school district that the school bus serves, 
its model year, and fuel type are included; for many others the manufacturer 
and seating capacity are also available. The dataset contains data from the 
46 states and the District of Columbia where this information was available. 
Prompted by requests from a range of stakeholders, WRI researchers compiled 
the dataset by submitting records requests to state governments between 
March and November 2022; they then harmonized and combined those state-
level datasets to enable multistate analysis. This dataset can serve a range 
of environmental and equity use cases, including estimating reductions in 
greenhouse gas emissions or benefits to public health resulting from the elec-
trification of all U.S. school buses, planning for electricity grid upgrades related 
to electric transportation, and identifying school districts with the oldest and 
probably most polluting school buses. There are two major limitations of this 
dataset. The first is missing data from four states (Colorado, Hawaii, Louisiana, 
and New Hampshire) and all the U.S. territories (Guam, Puerto Rico, U.S. Virgin 
Islands, Northern Mariana Islands, and American Samoa). The second limita-
tion results from methodological and structural differences between states’ 
original datasets.
1. INTRODUCTION
This dataset contains detailed information on the composition of school bus 
fleets in the United States. WRI researchers compiled this dataset by submit-
ting records requests to state governments between March and November 
2022; they then harmonized and combined these state-level datasets to enable 
multistate analysis. This dataset includes data from 46 states and the District 
of Columbia. Table 1 lists every state and U.S. territory alphabetically and 
notes whether school bus-fleet data were available for inclusion in this data-
set, the data source, and the date that the source collected or most recently 
updated the data.

2  |  
  
Table 1  |  Data Availability, Source, and Collection Date for Every U.S. State and Territory (alphabetical)
STATE OR TERRITORY DATA 
AVAILABLE? DATA COLLECTION METHOD SOURCE
DATE THAT THE SOURCE 
COLLECTED OR MOST 
RECENTLY UPDATED THE DATA
Alabama Yes Public records request Alabama State Department of Education 18 October 2021
Alaska Yes Public records request Alaska Department of Education and Early Development 30 June 2022
American Samoa No  X  X  
Arizona Yes Public records request Arizona Department of Education September 2021 – May 2022 
(varies by district)
Arkansas Yes Public records request Arkansas Department of Education February 2022
California Yes Public records request California Highway Patrol February 2022
Colorado No  X  X  
Connecticut Yes Public records request Connecticut Department of Motor Vehicles July 2022
Delaware Yes Public records request Delaware Department of Education 2019–2020
District of Columbia Yes Public records request District of Columbia Office of the State 
Superintendent of Education  31 May 2022
Florida Yes Downloaded published data Florida Department of Education 2021
Georgia Yes Public records request Georgia Department of Education March 2022
Guam No  X X  
Hawaii No  X X  
Idaho Yes Public records request Idaho State Department of Education March 2022
Illinois Yes Public records request Illinois Secretary of State 2 June 2022
Indiana Yes Public records request Indiana State Police July 2022
Iowa Yes Public records request Iowa Department of Education 17 March 2022
Kansas Yes Public records request Kansas State Department of Education 6 April 2022
Kentucky Yes Downloaded published data Kentucky Department of Education 2020–2021
Louisiana No  X  X  
Maine Yes Public records request Maine Department of Education 2021–2022
Maryland Yes Downloaded published data, 
public records request
Maryland State Department of Education, Maryland Motor 
Vehicle Administration 21 January 2022
Massachusetts Yes Public records request Massachusetts Department of Transportation May 2022 
Michigan Yes Downloaded published data Michigan State Police 31 August 2022
Minnesota Yes Downloaded published data Minnesota Department of Education 2021
Mississippi Yes Public records request Mississippi Department of Education 2021
Missouri Yes Public records request Driver and Vehicle Safety Division, Missouri 
State Highway Patrol 2021
Montana Yes Public records request Montana Office of Public Instruction 30 June 2022
Nebraska Yes Public records request Nebraska Department of Motor Vehicles  
Nevada Yes Public records request Nevada Department of Education May 2022 
New Hampshire No  X  X  
New Jersey Yes Public records request New Jersey Department of Environmental Protection December 2021
New Mexico Yes Public records request New Mexico Public Education Department 23 March 2022
New York Yes Public records request New York Department of Transportation, New York City 
Department of Education 2022, 2023

TECHNICAL NOTE   |  May 2024  |  3
Dataset of U.S. School Bus Fleets
STATE OR TERRITORY DATA 
AVAILABLE? DATA COLLECTION METHOD SOURCE
DATE THAT THE SOURCE 
COLLECTED OR MOST 
RECENTLY UPDATED THE DATA
North Carolina Yes Downloaded published data North Carolina Department of Public Instruction 2018–2019
North Dakota Yes Public records request North Dakota Department of Public Instruction 2020–2021
Northern Mariana Islands No  X  X  
Ohio Yes Public records request Ohio Department of Education 21 March 2022
Oklahoma Yes Public records request Oklahoma Tax Commission 4 November 2022
Oregon Yes Public records request Oregon Department of Education 2021
Pennsylvania Yes Public records request Pennsylvania Department of Transportation June 2022
Puerto Rico No  X  X  
Rhode Island Yes Requested records 
from contractor First Student, Inc. 26 June 2022
South Carolina Yes Public records request South Carolina Department of Education 2022
South Dakota Yes Public records request South Dakota Department of Revenue September 2022
Tennessee Yes Downloaded published data Tennessee Department of Educsation 2019–2020
Texas Yes Public records request Texas Education Agency 2021
U.S. Virgin Islands No X  X  
Utah Yes Public records request Utah State Board of Education 2021
Vermont Yes Public records request Vermont Department of Motor Vehicles 31 December 2021
Virginia Yes Public records request Virginia Department of Education 2022
Washington Yes Downloaded published data Washington State Office of Superintendent of 
Public Instruction 2022
West Virginia Yes Public records request West Virginia Department of Education 31 May 2021
Wisconsin Yes Public records request Division of State Patrol, Office of the Superintendent, 
Wisconsin Department of Transportation 2021
Wyoming Yes Public records request Wyoming Department of Education 29 March 2022
Note: X indicates data that were not received.
Sources:  Table was compiled by WRI authors. Full citations of data sources are included in the References, pp. 19–21.
a range of others, especially NCES’s datasets on school dis-
trict demographics, educational outcomes, and administrative 
characteristics. 
This dataset includes approximately 30 variables that describe 
the buses based on characteristics including the bus owner 
or user, model year, fuel type, the school district that the bus 
serves, the manufacturer, and seating capacity. The specific data 
available vary by state. Cover Sheet – Data Maps in the dataset 
shows which variables are present for each state in the dataset. 
Most (41) original datasets were structured at the bus level, but 
some (7) were structured at the school district level and could 
not be disaggregated to the bus level.
The dataset includes over 475,000 buses and over 11,000 entities 
that use these buses. An “entity” is a school district or other 
primary user of the school bus, such as Head Start Programs, 
day-care facilities, private schools, and churches. Nearly 9,700 
of these entities are public school districts. There are around 
115,000 buses in the dataset for which the entity using the 
bus is unknown. Most school districts were able to be matched 
with their Local Education Agency Identification Number 
(LEAID, sometimes called NCES ID), a unique identifica-
tion number assigned by the National Center for Education 
Statistics (NCES) to each school district in the country. The 
LEAID makes it possible to cross-reference this dataset with 
Table 1  |  Data Availability, Source, and Collection Date for Every U.S. State and Territory (Alphabetical) (Continued)

4  |  
  
There are two major limitations of this dataset: missing data 
and methodological and structural differences between the 
original datasets. 
Data were not available from every state, and this is therefore 
not a complete dataset of all school bus fleets in the U.S. Data 
were unavailable from the four states of Colorado, Hawaii, 
Louisiana, New Hampshire and from all the U.S. territories—
American Samoa, Guam, U.S. Virgin Islands, Northern Mariana 
Islands, and Puerto Rico. Table 2 provides more detail on our 
attempts to gather data from these states and territories.
Some states (like Wyoming) included only school buses owned 
by school districts, and others (like New York and Maryland) 
included buses owned by both school districts and contractors 
(often referred to as “private fleet operators”). In states that did 
not include buses owned by contractors, the total number of 
buses for each school district and the state overall is likely an 
undercount. In some states, it was unclear whether the number 
of school buses per district included buses owned by a contractor 
in addition to those owned by the district. Cover Sheet – Data 
Maps in the dataset shows which variables are present whether a 
given state’s data include buses owned by a contractor.
Each state’s dataset contained different fields and different sets 
of allowed values within multiple-choice fields; therefore, some 
of the data are not directly comparable between states. The 
authors standardized multiple-choice options whenever pos-
sible. Table 3 and Table 4 detail how data were standardized. In 
addition, each state collected their data at a different time; this 
dataset includes the most recently available data from each state. 
The original datasets are available for download in a .zip file on 
the dataset download page. See Section 4 for a more detailed 
discussion of limitations and how they were mitigated.
2. MOTIVATION
WRI’s Electric School Bus Initiative created this dataset to 
help fill a major knowledge gap related to school bus fleets. No 
nationwide, district-level dataset of school bus fleets in the U.S. 
is publicly available. State-level and school district-level data are 
rarely made public, and key stakeholders, like policymakers and 
advocates, probably lack the capacity to undertake the time-
intensive data collection process that was required to compile 
this dataset. WRI’s Electric School Bus Initiative created this 
dataset in direct response to frequent queries from stakeholders, 
including utilities, environmental justice advocates, government 
agencies, media, and researchers from non-profit organizations. 
Given the high level of demand for these data and the intensity 
of effort required to compile them, we hope that moving for-
ward a federal agency will create and maintain a public dataset 
of U.S. school buses. 
Landscape of current datasets on 
school bus fleets
The existing nationwide datasets on school bus fleets have 
significant limitations. Data from School Bus Fleet Magazine 
(School Bus Fleet Magazine 2021) and the Federal Highway 
Administration (U.S. Department of Transportation 2020) only 
estimate the total number of school buses in each state and pro-
vide no district-level information or detail on fleet composition. 
Data from many states are missing, and there are often meth-
odological problems with what data are available. For example, 
survey data that does not include accompanying documentation 
prevents users from evaluating the data quality and mitigating 
any issues that are identified. 
More detailed datasets on school bus fleets are available for 
purchase. IHS Markit purports to have a similar proprietary 
dataset, but it is costly (over US$60,000 for a one-time purchase 
of zip code-level data); buyers are prohibited from publishing 
any portion of it; and it is intended primarily for commercial use 
(e.g., to inform a company’s sales or marketing strategy) rather 
than for policy, advocacy, or research uses.1 Atlas Public Policy’s 
EV Hub (Atlas Public Policy 2019) offers a dataset of medium- 
and heavy-duty vehicles (including school buses) based on those 
IHS Markit data. At a much more affordable price (half of users 
pay nothing, and the other half pay rates ranging from $300 
to $500 per user per year), Atlas EV Hub is targeted to public 
agencies and non-profits. However, the smallest spatial disag-
gregation is the state, and it takes time to set up the institutional 
account or purchase agreement to access the dataset. Neither 
dataset enables users to disaggregate or match data to the school 
district level, even though school districts are a primary unit of 
analysis for school transportation policy and research. 
Use cases
This dataset can serve a range of environmental and equity 
use cases. For example, it could be used to identify the school 
districts with the oldest diesel-powered buses, which create the 
most pollution and health problems (Beatty and Shimshack 
2011). In turn, this information could help direct national- or 
state-level funding to those areas where the health burden from 
pollution from current diesel buses is highest; or it could help 
communities and advocates focus their campaigns on areas 
where they would have the greatest impact. This dataset could 
also be used to more accurately estimate the total number, bus

TECHNICAL NOTE   |  May 2024  |  5
Dataset of U.S. School Bus Fleets
type, and fuel type of U.S. school buses, which would result in 
better estimates of the effect of electrifying all U.S. school buses 
on greenhouse gas emissions or public health. A better estimate 
of the total number and type of buses in a region would also 
be useful for cities, regional governments, and utilities that are 
planning for the increased electricity demand and grid upgrades 
associated with the electrification of transportation. Finally, a 
district-level count of school buses, when combined with WRI’s 
Dataset of Electric School Bus Adoption in the United States 
(Lazer and Freehafer 2024), makes it possible to estimate the 
percentage of school districts’ buses that are electric, painting a 
more nuanced picture of local progress and leadership in school 
bus electrification.
3. METHODS
Data collection
WRI researchers collected these data from state-level govern-
mental departments between March and November 2022. Eight 
states had published data available for download. For the rest, 
researchers sent public records requests (often called Freedom 
of Information Act (FOIA) requests) to state departments and 
agencies that were likely to keep records on school bus fleets. In 
most states, each department or agency had a separate process 
for submitting records requests (as opposed to a state-wide 
FOIA request process). The processes included at least some of 
the following steps: submitting a PDF form via email; submit-
ting an online form; creating an account in a FOIA portal in 
which users submit, track, and receive responses to requests; 
and emailing the department’s designated FOIA contact. The 
time between submitting a request to the correct state depart-
ment and receiving data ranged from less than a week to 
several months.
Records about school buses are held by different departments 
in each state. The most challenging part of data collection was 
identifying which department (if any) had the data and deter-
mining the department’s process for obtaining them. The process 
was complicated by the fact that state departments that did not 
have the requested data often incorrectly informed us that no 
other state department had them either. We typically contacted 
two to three departments per state before identifying the one 
that held the records; but in some cases, we contacted eight or 
more. See Table 1 for a full list of data sources.
The most common data sources were departments of education 
(or the state’s equivalent, such as North Dakota’s Department 
of Public Instruction), and second most common was the state 
police, highway patrol, or equivalent department. However, in 
some states, records were held by other departments—for exam-
ple, by the Secretary of State in Illinois. Different departments 
had different reasons for collecting the data, which informed 
what information they collected. For example, state police 
concerned with documenting bus safety inspections focused on 
identifying the most recent inspection dates of individual buses. 
Data collected by departments of education often described the 
state’s school transportation program and therefore included 
more contextualizing information, including school district 
served; the ownership model of the buses; and operational data, 
like mileage. Table 1 provides a full list of data sources.
For a number of reasons, Departments of Motor Vehicles 
(DMVs) were often not the best source of school bus-
registration data. In most states, DMVs could only share the 
county where a bus was registered. Since counties and school 
districts often have different boundaries, it would be difficult or 
impossible to determine which school district the bus served, 
especially if it was registered to a contractor with buses operat-
ing in multiple districts. Citing privacy concerns, DMVs often 
refused to disclose who owned a given bus (i.e., the school dis-
trict or a contractor). Moreover, whereas data from departments 
that deal specifically with school transportation often included 
fields relevant to the use cases of this dataset, such as the bus’s 
district or bus type (A, B, C, or D), the data from DMVs were 
often less pertinent. Finally, DMVs consistently charged—typi-
cally around $100 to $500—for access to these public records. 
However, since their databases are updated on an ongoing basis, 
DMVs often have very recent data, while departments of educa-
tion tend to compile school bus-fleet data once per year. 
As noted above, the dataset is missing data from four states 
(Colorado, Hawaii, Louisiana, and New Hampshire) and all U.S. 
territories (Guam, Puerto Rico, U.S. Virgin Islands, Northern 
Mariana Islands, and American Samoa). See Table 2 for more 
detail on our attempts to collect data from these states and 
territories. The scope of our data collection efforts, however, was 
limited to state-wide datasets. Individual school districts main-
tain records of their own school bus fleets, and users interested 
in fleets in states or school districts where data were unavailable 
should consider directly contacting those districts, which are 
also subject to FOIA laws. Many state departments of educa-
tion publish lists of superintendents or other school district 
contact-points.

6  |  
  
Data compilation, harmonization,  
and analysis
The data on each state’s school bus fleets were shared in differ-
ent formats and contained different fields. The authors had to 
compile and harmonize the data received from states to create 
a consistent dataset of all states. Most states shared their data 
as a spreadsheet, but some shared them as PDF files, including 
Maryland, Massachusetts, New Jersey, New Mexico, and Ohio. 
Data received as PDFs were converted to spreadsheets using the 
free tool Tabula.2 
First, a “data map” noting which fields were present in each 
state’s dataset was created (see “Cover Sheet – Data Maps” in 
the dataset). This allowed us to determine which fields were 
present in multiple states’ datasets and could be combined into 
one field in the final, harmonized dataset. This included deter-
mining fields that contained functionally equivalent data, which 
could therefore be combined. For example, “Shell Capacity,” 
“Rated Capacity,” and “Design Capacity” were determined to 
be functionally equivalent and were combined, as were “District 
ID” and “System ID,” both of which refer to state-level school 
district identification numbers. 
Based on the equivalencies determined in the data map (see 
“Cover Sheet – Data Maps” in the dataset), the authors then 
combined the state-level datasets into a multistate dataset of 
school bus fleets. Most of the data contained a separate row of 
data for each individual bus, so we compiled a sheet of that bus-
level data. However, some of the data organized at the district 
or fleet level were impossible to disaggregate to the bus level, so 
Table 2  |  Departments Contacted in States Where Data Were Determined to Be Unavailable
STATE, TERRITORY, OR AGENCY POSSIBLE DATA SOURCES THAT WERE CONTACTED NOTES
U.S. Department of Education U.S. Department of Education (DOE)  
Bureau of Indian Education Bureau of Indian Education (U.S. Department of the Interior)
The Bureau of Indian Education was not in possession 
of any compiled data on school buses owned by tribal 
nations. Some states included data on school buses 
owned by tribal nations located within their borders.
Colorado
Colorado Department of Education, Colorado Department of Public Health 
and Environment, Colorado Department of Transportation, Colorado 
Department of Motor Vehicles, Regional Air Quality Council, Colorado 
State Pupil Transportation Association
 
Guam Guam Department of Education  
Hawaii Hawaii State Department of Education, Hawaii Open Data
Hawaii is a single school district that contracts 100% 
of student transportation services out to private 
contractors. While Hawaii DOE has access to their 
fleet information, they were unable to share it with 
outside sources because the contractors are privately 
owned entities.
Louisiana Louisiana Department of Education, Louisiana Department of 
Transportation, Louisiana State Police  
New Hampshire
New Hampshire Department of Education, New Hampshire Department of 
Transportation, New Hampshire State Police, New Hampshire Department 
of Environmental Services, New Hampshire Department of Energy, New 
Hampshire Department of Motor Vehicles, New Hampshire Department of 
Health and Human Services
 
Puerto Rico Puerto Rico Department of Education  
U.S. Virgin Islands Virgin Islands State Department of Education  
Source: WRI authors.

TECHNICAL NOTE   |  May 2024  |  7
Dataset of U.S. School Bus Fleets
these data were added to the dataset in a separate district-level 
tab. Original data received from states are available for download 
on the dataset landing page.
Matching school district names and LEAIDs
We then added the school district’s federal Local Education 
Agency Identification Number (LEAID, sometimes called 
NCES ID), a unique number assigned to each school district 
in the country, whenever only the state-level district ID or the 
school district name was included in the original data. (Below, 
we explain how we identified entities without LEAIDs). Their 
inclusion was a priority because LEAIDs enable cross-referenc-
ing with a range of other datasets, such as the Electric School 
Bus Initiative’s Dataset of Electric School Bus Adoption (Lazer 
and Freehafer 2022) and the NCES’s various datasets, which 
include information on school district demographics, educa-
tional outcomes, and administrative characteristics. 
Two methods were used for matching. First, if a state-level 
district identification number was included, we referred to 
the NCES’s Common Core of Data (NCES n.d.) to identify 
corresponding LEAIDs. This was done with the XLOOKUP 
function in Excel.
Second, if only school district names were included, we ran 
a customized machine routine to attempt to determine the 
LEAID for that school district. We used this method for about 
5,700 school districts, bus owners, or primary bus users (entities) 
from Illinois, New York, Oregon, Tennessee, Vermont, Wash-
ington, and Wisconsin, which were identified only by a name 
and not by any ID number. The customized machine routine, 
which was developed by former Electric School Bus Initiative 
intern Naveen Raman, compares the entity name from the 
state dataset to a full list of school district names and LEAIDs 
from NCES’s Common Core of Data (NCES n.d.). It uses the 
Jellyfish Python library for approximate and phonetic matching 
of strings (Turk 2022) and the string distance algorithm ( Jaro 
1989) to create an index of the frequency of direct matches and 
possible transpositions (re-arrangements of pairs of letters) that 
describe how similar two strings (school district names) are. The 
routine exhaustively tries every possible match and then chooses 
the match with the best score (0-100), producing a single best 
guess of which LEAID matches a given school district’s name.
We then conducted an informal visual inspection to see which 
match scores seemed correlated with a relatively high share of 
correct matches. We generated three categories:
 ▪ Low match, 0–74.9: Matches with a score below 75 seemed 
to have a very low share of correct matches. This category 
included 2,489 matches, which we initially discarded because 
manually inspecting them seemed too time-consuming. 
As capacity allowed later on, we did inspect some of these 
matches manually and confirmed another 39 correct matches 
from among those with scores between 62 and 75. 
 ▪ Moderate match, 75–86: A majority of matches with scores 
between 75 and 86 appeared to be correct, so we manually 
inspected them by comparing the school district name from 
the state dataset to the school district name of the guessed 
NCES LEAID. Of 1,385 matches, 956 were confirmed.
 ▪ High match, 87–100: We automatically accepted all 1,917 
matches with match scores 87 and higher, because a visual 
inspection of a sample of several dozen of those matches 
showed all correct matches. Of these, 281 had scores of 
100 percent match.
Some examples of guessed matches that we confirmed based 
on visual inspection include “HELIX SCHOOL DIST 1” 
and “helix sd 1” and “WEYAUWEGA FREMONT” and 
“weyauwega-fremont school district.” Examples of incorrect 
guessed matches include “SWCAP HEAD START” and 
“aupaca school district” and “NORTHLAND LUTHERAN 
HIGH SCHOOL ASSOCIATION INC” and “northland 
pines school district.”
Approximately 3,000 matches were confirmed (of about 5,700), 
and the resulting LEAIDs were incorporated into the dataset. 
Figure 1 shows the frequency of match scores by state. States 
with data from departments of education tended to have higher 
matches because the naming conventions are more likely to 
adhere to those included in the NCES Common Core of 
Data (such as Tennessee and Oregon). Conversely, states with 
data from agencies like the DMV tended to have lower match 
scores (such as Vermont). Aside from these correspondences, 
we are not aware of any characteristics shared by school districts 
that were not matched with an LEAID. As far as we know, 
unmatched districts are distributed randomly across states, 
locales, and so on.

8  |  
  
Figure 1  |  Histogram of Match Scores by State
Source: WRI authors.
45
590
839
377 331 275 257
426
0
200
400
600
800
1000
0.60 .7 0.80 .9 1
Frequency
Score
Illinois
2 5
62
323 327
149
60 61
229
68
0
100
200
300
400
0.60 .7 0.80 .9 1
Frequency
Score
New York
15
40
31
14
83 78
4
19
0
20
40
60
80
100
0.60 .7 0.80 .9 1
Frequency
Score
Oregon
12
39
53
43
22
11 10 6
0
10
20
30
40
50
60
0.60 .7 0.80 .9 1
Frequency
Score
Vermont
5
24 39
71
35
57
194
40
50
100
150
200
0.60 .7 0.80 .9 1
Frequency
Score
Wisconsin
1 3 9
83
3
24
0
20
40
60
80
100
0.60 .7 0.80 .9 1
Frequency
Score
Tennessee
11 2 1 3
294
0
50
100
150
200
250
300
0.60 .7 0.80 .9 1
Frequency
Score
Washington
0.5
0.5
0.5
0.5
0.5
0.5
0.5

TECHNICAL NOTE   |  May 2024  |  9
Dataset of U.S. School Bus Fleets
Identifying entities without LEAIDS
After the machine routine, we were left with about 1,800 
entities whose LEAID could not be determined. This is not 
necessarily a matching issue; entities that are not school dis-
tricts, such as certain types of private schools or Head Start 
programs, are not assigned an LEAID by NCES. To enable 
better data management and aggregation in the “District Sum-
mary” tab, we therefore created a new identification number, 
called a “WRI Entity ID.” We assigned a WRI Entity ID to 
every primary user, including those that have LEAIDs, those 
that inherently do not have an LEAID, and those that we were 
not able to match with LEAIDs through one of the processes 
described above. 
A primary user, or entity, uses the bus on a day-to-day basis; 
they may or may not own the bus. Examples of primary users 
include a school district that owns and uses a school bus, a 
school district that uses buses leased from a contractor, and a 
day care that uses a school bus, the identity of whose owner is 
unknown to us. In cases in which we know the owner of the 
bus and the owner is different from the primary user, only the 
primary user was assigned a WRI Entity ID. For example, if a 
Bank of America leasing corporation owns a school bus, and 
a private school called Springfield School leases that bus from 
Bank of America and uses it on a day-to-day basis, Springfield 
School is the primary user. Only Springfield School would 
have a WRI Entity ID; Bank of America would not. Third 
parties - such as contractors, individual owners, or leasing 
agencies - without a known primary user did not receive a WRI 
Entity ID either.
WRI Entity IDs are in the format of a five-digit numerical 
sequence and were assigned to entities sorted alphabetically 
by state and then by “Name of school district or primary user.” 
The “District Summary” tab includes one row for every unique 
primary user, including school districts and other entities. The 
variable “Public school district or other?” allows users to filter for 
primary users that are school districts.
Standardizing allowed values for each variable
For the variables that are most important to the use cases of this 
data, “Fuel Type,” “Bus Type,” and “Year,” the authors standard-
ized the data so that each variable contained a limited set of 
allowed values. For example, original bus type values included 
both “Type A” and “A” when referring to the same type of bus, 
so we standardized all values to “A” to enable aggregation and 
analysis. Similarly, values referring to diesel buses included “D” 
“1 – Diesel” and “Diesel,” so we standardized them all to “Die-
sel.” In many instances, this process required us to contact the 
original data source to obtain the key for the abbreviations they 
used. Keys were often not provided with the original dataset 
and were sometimes not obvious. For example, West Virginia 
used “Type A” and “Type B” to refer to buses widely identified 
as “Type C” (Conventional). In Vermont, fuel type “B” stands 
for “Both gas and electric,” which is more commonly referred to 
as “Hybrid.” One surprising finding was the range of fuel types 
used in school buses; the authors were not previously aware 
that there were eight or more possible fuel types. The original 
datasets included a variety of variables indicating the year or age 
of the bus, such as “Model Year,” “Date Delivered,” “Age” and 
more. For the summary statistics, we combined all the variables 
that were functionally equivalent to “Model Year” into one 
new variable. See Table 3 and Table 4 for the raw and cleaned 
allowed values for bus type and fuel type. 
For the approximately 6,700 buses for which we had the VIN 
but no model year, we used the VIN to look up the model 
year. This was possible because the model year is encoded in a 
specific location within the VIN. A given year is represented by 
a specific character, such as D representing 2013 for medium-
duty vehicles. We used a key extracted from Atlas EV Hub’s 
VIN Decoder (Atlas Public Policy n.d.) to create an Excel-
based decoder for the model year from school bus VINs. We 
also used the National Highway Traffic Safety Administration’s 
VIN Decoder (National Highway Traffic Safety Administration 
2022) for some spot-checks and additional lookups.

10  |  
  
Table 3  |  Clean and Raw Set of Allowed Values – Bus Type
RAW CLEAN NOTE
1 1  
2 2  
Type A Bus A  
Type A Bus with Lift A  
A A  
A1 A  
A2 A  
A-Mini Bus A  
A-I A  
A-1 A  
A-II A  
A-11 A  
A-2 A  
BUS TYPE A - 23 PAX (NO LIFT) A  
TYPE A A  
A II 24 A  
A I 28 A  
AI 24 A  
AI 30 A  
A II 28 A  
A I 24 A  
Type B Bus B  
Type B Bus with Lift B  
B B  
TYPE B B  
A - West Virginia C Conventional Regular 
B - West Virginia C Conventional Special Ed 
BUS TYPE C - 29 PAX (LIFT) C  
BUS TYPE C - 33 PAX (LIFT) C  
BUS TYPE C - 62 PAX C  
BUS TYPE C - 65 PAX C  
BUS TYPE C - 66 PAX C  
BUS TYPE C - 72 PAX C  
BUS TYPE C - 75 PAX C  
BUS TYPE C - 77 PAX C  
C C  
C 42 C  
C 54 C  
C 60 C  
CLEAN SET 
OF ALLOWED VALUES
1
2
A
B
C
D
Othera
[Blank if unknown]b

TECHNICAL NOTE   |  May 2024  |  11
Dataset of U.S. School Bus Fleets
Table 3  |  Clean and Raw Set of Allowed Values – Bus Type (Continued)
RAW CLEAN NOTE
C 66 C  
C 66 wb pr C  
C 72 C  
C 72 wb C  
C-Conventional Bus C  
TYPE C C  
Type C Bus C  
Type C Bus with Lift C  
F D Transit Spare
Type D Bus D  
Type D Bus with Lift D  
D D  
D-Flat Nose Bus D  
BUS TYPE D - 66 PAX D  
BUS TYPE D - 78 PAX D  
D D  
TYPE D D
H D  
D RE 78 D  
D FE 81 D  
D RE 75 D  
D RE 66 D  
D FE 66 D  
D RE 48 D  
E - West Virginia D Transit Special Ed
V Other Van
O Stands for “Other.” Bus type unknown. Left blank.
MPV Other
Note from data source: "‘Multipurpose Passenger Vehicle’ (MPV) means every motor vehicle with less than ten passenger 
positions (including the driver) and that cannot be certified as a bus or school bus by federal standards. (In determining 
passenger capacity, wheelchair positions are counted as 4 passenger positions.) Although a school entity may use such 
a vehicle as a station wagon, full-sized sedan, suburban, etc., to transport pupils to and from school or related events, the 
vehicle shall not be identified as a school bus (including color) and shall not stop or control traffic on the traveled portion 
of the roadway to load or unload passengers. Drivers of such vehicles shall utilize the same precautions to safeguard 
the safety of their passengers as they would if they were driving a privately owned passenger vehicle. See Section 9, 
Multipurpose Passenger Vehicle, for additional requirements. https://wyoleg.gov/ARULES/2011/AR11-054PTSB.pdf." c
Y   Bus type unknown. Left blank.
N - Idaho   "Non-reimbursable" or "non-confirmed." d Bus type unknown. Left blank.
Other Activity Bus   Bus type unknown. Left blank.
3   Bus type unknown. Left blank.
OTHER Bus type unknown. Left blank.
X – West Virginia   Contracted Vehicle Bus type unknown. Left blank.

12  |  
  
RAW CLEAN NOTE
E - Indiana  
"The Type E is a special purpose bus, basically a bus of several size types that are not school bus yellow and are used for 
various type of student transportation (generally they are MFSAB activity buses, but some could be full size buses). Many 
times district will report those buses by their size type instead of the Type E designation. It was a way to track non-school 
buses in the state." e Bus type unknown. Left blank.
T D Stands for "transit style." f
Notes: 
a “Other” indicates a vehicle type known to be something other than a Type A, B, C, or D school bus, such as a van. 
b [Blank] indicates an unknown bus type; the vehicle type could not be determined based on the available information. The bus type was left blank. 
c See Wyoming Department of Education 2022.
d See Idaho State Department of Education 2022.
e See Indiana State Police 2022.
f See California Highway Patrol 2022.
Source: WRI authors.
Table 4  |  Clean and Raw Set of Allowed Values – Fuel Type
RAW CLEAN NOTE
Alternative Fuel Alternative fuel
A common definition of “alternative fuel” is any fuel type other than diesel 
and gasoline. Buses in this category use one of the other fuel types in this 
column, but it is unknown which fuel type they use, because it is not possible 
to disaggregate this general label into specific fuel types. Only Arizona, 
Idaho, and Minnesota use this category, which might refer to different fuel 
types in each case.
Alternative Alternative fuel
4-CNG CNG  
CNG CNG  
Compressed Nat Gas CNG  
Compressed Natural Gas CNG  
D84CNG CNG  
C CNG  
Alternate Fuel BIO Diesel Based on the VINs of school buses with this fuel type, it seems to be biodiesel.
Clean Diesel Diesel  
Bio-diesel Diesel  
2-Diesel Diesel  
A22D Diesel  
A22DL Diesel  
A34D Diesel  
A34DL Diesel  
B34D Diesel  
B34DL Diesel  
C48D Diesel  
C48DL Diesel  
CLEAN SET  
OF ALLOWED VALUES
Alternative Fuel  
(not otherwise specified)
CNG
Diesel
Electric
Flexible fuel
Gasoline
Hybrid (diesel)
Hybrid (gasoline)
Hybrid  
(not otherwise specified)
LNG
Natural gas
Propane
[Blank if unknown]
Table 3  |  Clean and Raw Set of Allowed Values – Bus Type (Continued)

TECHNICAL NOTE   |  May 2024  |  13
Dataset of U.S. School Bus Fleets
RAW CLEAN NOTE
C60D Diesel  
C60DL Diesel  
C77D Diesel  
C77DL Diesel  
D Diesel  
D1 Diesel  
D48D Diesel  
D48DL Diesel  
D60D Diesel  
D60DL Diesel  
D84D Diesel  
D84DL Diesel  
D90D Diesel  
D90DL Diesel  
DIE Diesel  
Diesel Diesel  
H84D Diesel  
DSL Diesel  
5-Electric Electric  
A34E Electric  
C77E Electric  
C77EC Electric  
D84E Electric  
E                         Electric  
ELE Electric  
Electric Electric  
EV Electric  
Plug In Electric Electric
F                         Flexible fuel  
FLEX FUEL Flexible fuel  
Flexible Flexible fuel  
Gasoline Flex Flexible fuel
Flexible Fuel Flexible fuel  
1-Gasoline Gasoline  
A22G Gasoline  
A22GL Gasoline  
A34G Gasoline  
A34GL Gasoline  
Table 4  |  Clean and Raw Set of Allowed Values – Fuel Type (Continued)

14  |  
  
RAW CLEAN NOTE
B34G Gasoline  
C60G Gasoline  
C60GL Gasoline  
C77G Gasoline  
C77GL Gasoline  
G Gasoline  
G` Gasoline  
Gas Gasoline  
Gasoline Gasoline  
DIESEL HYBRID Hybrid (diesel)  
GASOLINE HYBRID Hybrid (gasoline)  
B (Vermont)                    Hybrid (not 
otherwise specified) Includes both gasoline-electric hybrids and diesel-electric hybrids.
LNG Natural gas  
natural gas Natural gas  
NG Natural gas  
N Natural gas “Stands for ‘Natural’ – any type of natural gas”a
L Propane Used VIN decoder to determine that “L” stands for LPG, not LNG.
3-Propane Propane  
A34P Propane  
A34PL Propane  
C60P Propane  
C60PL Propane  
C77P Propane  
C77PL Propane  
Liquified Petroleum Gas Propane  
LPG Propane  
P                         Propane  
PRO Propane  
Propane Propane  
LPG, PROPANE Propane  
Other   Unknown for the purposes of this dataset.
O   Unknown for the purposes of this dataset.
26   Typo—same as seating capacity. Fuel type unknown. Left blank.
35   Typo—same as seating capacity. Fuel type unknown. Left blank.
62   Typo—same as seating capacity. Fuel type unknown. Left blank.
82   Typo—same as seating capacity. Fuel type unknown. Left blank.
N/A   Fuel type unknown. Left blank.
Table 4  |  Clean and Raw Set of Allowed Values – Fuel Type (Continued)

TECHNICAL NOTE   |  May 2024  |  15
Dataset of U.S. School Bus Fleets
RAW CLEAN NOTE
Not Identified   Fuel type unknown. Left blank.
S   Only one CA bus; seems to be a typo. Fuel type unknown. Left blank.
Note: 
a See Vermont Department of Motor Vehicles 2021. 
Source: WRI authors.
Aggregating data in summary sheets
We then aggregated the data in a “District Summary” sheet and 
a “State Summary” sheet. Summary statistics included the num-
ber of buses, the number of buses of each fuel type, the number 
of each bus type (A, C, D, etc.), and so on. Not all data were 
summarized, only the variables that the authors determined 
would be most useful to the target audience and for which there 
were data from a significant share of states. The summary sheets 
contain the following fields:
DISTRICT SUMMARY SHEET:
 ▪ Source Sheet
 ▪ State 
 ▪ WRI Entity ID
 ▪ LEAID
 ▪ Name of School District or Primary User (primary users 
include day care centers, churches, scout groups, and other 
entities that make regular use of school buses)
 ▪ Public School District (with LEAID) or Other? 
 ▪ Total Number of Buses
 ▪ Fuel Type 
 ▪ Diesel
 ▪ Percent diesel 
 ▪ Gasoline
 ▪ Percent gasoline 
 ▪ Propane
 ▪ Percent propane 
 ▪ Electric
 ▪ Percent electric
 ▪ Natural gas
 ▪ Percent natural gas
 ▪ Hybrid (all types)
 ▪ Percent hybrid (all types)
 ▪ Alternative fuel
 ▪ Percent alternative fuel
 ▪ CNG
 ▪ Percent CNG
 ▪ Flexible fuel
 ▪ Percent flexible fuel
 ▪ Unknown
 ▪ Percent unknown
 ▪ Bus Age
 ▪ Number of buses 2020-newer
 ▪ Percent of buses 2020-newer
 ▪ Number of buses 2010-2019
 ▪ Percent of buses 2010-2019
 ▪ Number of buses 2000-2009
 ▪ Percent of buses 2000-2009
 ▪ Number of buses 1999 and older
 ▪ Percent of buses 1999 and older
 ▪ Number of buses with age unknown
 ▪ Percent of buses with age unknown
 ▪ Bus Type
 ▪ Type A 
 ▪ Type B 
 ▪ Type C 
 ▪ Type D 
Table 4  |  Clean and Raw Set of Allowed Values – Fuel Type (Continued)

16  |  
  
 ▪ 1 (California only) 
 ▪ 2 (California only)  
 ▪ Other 
 ▪ Unknown
STATE SUMMARY SHEET:
 ▪ Source Sheet
 ▪ State
 ▪ Total Number of Buses 
 ▪ Number of Buses Owned by School Districts 
or Primary Users
 ▪ Percent of Buses Owned by School Districts 
or Primary Users
 ▪ Number of Buses Owned by Third Party
 ▪ Percent of Buses Owned by Third Party
 ▪ Number of Buses with Unknown Ownership
 ▪ Percent of Buses with unknown ownership
 ▪ Fuel Type
 ▪ Diesel
 ▪ Percent diesel 
 ▪ Gasoline
 ▪ Percent gasoline 
 ▪ Propane
 ▪ Percent propane 
 ▪ Electric
 ▪ Percent electric
 ▪ Natural gas
 ▪ Percent natural gas
 ▪ Hybrid (all types)
 ▪ Percent hybrid (all types)
 ▪ Alternative fuel
 ▪ Percent alternative fuel
 ▪ CNG
 ▪ Percent CNG
 ▪ Flexible fuel
 ▪ Percent flexible fuel
 ▪ Unknown
 ▪ Percent unknown
 ▪ Bus Type
 ▪ A
 ▪ B
 ▪ C
 ▪ D
 ▪ 1
 ▪ 2
 ▪ Other
 ▪ Bus Age
 ▪ Number of buses 2020-newer
 ▪ Percent of buses 2020-newer
 ▪ Number of buses 2010-2019
 ▪ Percent of buses 2010-2019
 ▪ Number of buses 2000-2009
 ▪ Percent of buses 2000-2009
 ▪ Number of buses 1999 and older
 ▪ Percent of buses 1999 and older
 ▪ Number of buses with age unknown
 ▪ Percent of buses with age unknown
COMPILED BUS-LEVEL DATA SHEET:
 ▪ Identity, Location, and Ownership 
 ▪ State
 ▪ WRI Bus ID Number
 ▪ State District ID
 ▪ WRI Entity ID
 ▪ LEAID
 ▪ Name of school district or primary user
 ▪ Public school district (with LEAID) or other? 
 ▪ Does the school district or primary user own the bus? 
 ▪ Third party involved
 ▪ County 
 ▪ County 2
 ▪ ZIP code
 ▪ Type, Size, and Fuel 
 ▪ Bus type

TECHNICAL NOTE   |  May 2024  |  17
Dataset of U.S. School Bus Fleets
 ▪ Shell capacity
 ▪ Seating capacity
 ▪ Fuel type 
 ▪ Date and Age 
 ▪ Y ear for summary sheet
 ▪ Model year
 ▪ Chassis year
 ▪ Build date
 ▪ Date into operation
 ▪ Purchase date
 ▪ Delivery date
 ▪ Bus age
 ▪ Bus ID and Manufacturer  
 ▪ VIN
 ▪ Body manufacturer
 ▪ Chassis manufacturer
 ▪ Manufacturer (not otherwise specified)
 ▪ Model
 ▪ Date updated or last inspected
COMPILED DISTRICT-LEVEL DATA SHEET:
 ▪ Identity, Location, and Ownership 
 ▪ State
 ▪ WRI Entity ID
 ▪ State District ID
 ▪ LEAID
 ▪ Public school district (with LEAID) or other?
 ▪ Name of school district or primary user
 ▪ Who owns the buses?
 ▪ Is a contractor used for some or all of the buses?
 ▪ Contractor name
 ▪ Number, Fuel, and Type
 ▪ T otal number of buses
 ▪ Diesel
 ▪ Gasoline
 ▪ Propane
 ▪ CNG
 ▪ Unknown fuel type
 ▪ Public owned A
 ▪ Public owned B
 ▪ Public owned C
 ▪ Public owned D
 ▪ Public owned Total
 ▪ Contract owned A
 ▪ Contract owned B
 ▪ Contract owned C
 ▪ Contract owned D
 ▪ Contact owned T otal
 ▪ T otal type A
 ▪ T otal type B
 ▪ T otal type C
 ▪ T otal type D
 ▪ T otal type A/B
 ▪ T otal type C/D
 ▪ Date and Age
 ▪ Has some age data?
 ▪ 1977 and earlier
 ▪ 1989–99
 ▪ 2000–04
 ▪ 2005–09
 ▪ 2010–14
 ▪ 2015–20
 ▪ 5 years and newer
 ▪ 6–10 years
 ▪ More than 10 years
 ▪ More than 15 years
 ▪ Unknown age
 ▪ Date Updated or Last Inspected

18  |  
  
4. LIMITATIONS AND 
CONCLUSION
Data were not available from every state; this is therefore not a 
complete dataset of all school bus fleets in the U.S. Data were 
unavailable from the following states and territories: Colorado, 
Hawaii, Louisiana, New Hampshire, American Samoa, Guam, 
U.S. Virgin Islands, Northern Mariana Islands, and Puerto Rico. 
Some states (like Wyoming) included only school buses owned 
by school districts, and others (like New York and Maryland) 
included buses owned by both school districts and private 
contractors. In states that did not include buses owned by 
private contractors, the total number of buses for each school 
district and the state overall is likely an undercount. In some 
states, it was unclear whether the number of school buses per 
district included buses owned by a contractor or not. The data 
map includes a field indicating whether the state’s data include 
buses owned by a contractor (see “Cover Sheet – Data Maps” 
in the dataset).
Each state’s dataset contained different fields and different 
sets of allowed values within multiple-choice fields, making it 
impossible to aggregate some of the data. For example, some 
states included separate designations for all known fuel types, 
while others combined several fuel types (like CNG or pro-
pane) together under “Alternative Fuels.” When it was possible 
to do so with certainty, the authors standardized multiple-
choice options like “Gas” and “Gasoline.” In another example, 
states used different dates to indicate age, such as “Purchase 
Date” (Iowa), “Build Date” (Florida), or “Date Into Opera-
tion” (Georgia). (See Tables 6 and 7 for details on how data 
were standardized.)
Each state collected their data at a different time. While this 
dataset includes the most recently available data, the reality on 
the ground may have changed since the data were collected—for 
example, a school bus might have been added mid-year. There 
are no current plans to publish an update to this dataset, but 
WRI may decide to do so in the future if, for example, data from 
more states are found.
The data are also subject to data entry errors imported from the 
raw datasets. The authors were able to identify obvious typos and 
some duplicates. We also checked against other data sources to 
confirm that the number of buses reported in each state did not 
differ significantly from other estimates. However, beyond these 
limited corrections and crosschecks, we were not able to validate 
the data or check for other errors. We were unable to develop a 
quantitative estimate of data quality issues.

TECHNICAL NOTE   |  May 2024  |  19
Dataset of U.S. School Bus Fleets
REFERENCES
Alabama State Department of Education. 18 October 2021. "Re -
cords Request—School Bus Data.” Released to the World Re -
sources Institute.
Alaska Department of Education and Early Development. 30 June 
2022. "Records Request—School Bus Data.” Released to the World 
Resources Institute.
Arizona Department of Education. September 2021–May 2022 (varies 
by district). "Records Request—School Bus Data.” Released to the 
World Resources Institute.
Arkansas Department of Education. February 2022. "Records Re -
quest—School Bus Data.” Released to the World Resources Institute.
Atlas Public Policy. 2019. “Atlas EV Hub, Medium and Heavy Duty 
Vehicle Dashboard.” Washington, DC: Atlas Public Policy. https://
www.atlasevhub.com/materials/medium-and-heavy-duty-vehicle-
registrations-dashboard/ 
Beatty, T.K.M., and J.P. Shimshack. 2011. “School Buses, Diesel Emis -
sions, and Respiratory Health.” Journal of Health Economics 30 (5): 
987–99. doi:10.1016/j.jhealeco.2011.05.017.
California Highway Patrol. February 2022. "Records Request—School 
Bus Data.” Released to the World Resources Institute.
Connecticut Department of Motor Vehicles. July 2022. "Records Re -
quest—School Bus Data.” Released to the World Resources Institute.
Delaware Department of Education. 2019–2020. "Records Request—
School Bus Data.” Released to the World Resources Institute.
District of Columbia Office of the State Superintendent of Education. 
31 May 2022. "Records Request—School Bus Data.” Released to the 
World Resources Institute.
Division of State Patrol, Office of the Superintendent, Wisconsin 
Department of Transportation. 2021. "Records Request—School Bus 
Data.” Released to the World Resources Institute.
Division of State Patrol, Office of the Superintendent, Wisconsin 
Department of Transportation. 2021. "Records Request—School Bus 
Data.” Released to the World Resources Institute.
Driver and Vehicle Safety Division, Missouri State Highway Patrol. 
2021. "Records Request—School Bus Data.” Released to the World 
Resources Institute.
First Student, Inc. 26 June 2022. "Records Request—School Bus Data.” 
Released to the World Resources Institute.
ENDNOTES
1. Since this landscape analysis was conducted, IHS Markit was 
acquired by S&P Global: https://ihsmarkit.com/index.html.
2. Tabula is available online here: https://tabula.technology/.

20  |  
  
Florida Department of Education. 2022. “Florida School District 2020–
21 Transportation Profiles.” https://www.fldoe.org/core/fileparse.
php/7585/urlt/schtrandist2021.pdf.
Jaro, M.A. 1989. “Advances in Record-Linkage Methodology as Ap -
plied to Matching the 1985 Census of Tampa, Florida.” Journal of the 
American Statistical Association 84 (406): 414–20. doi:10.1080/016214
59.1989.10478785.
Georgia Department of Education. March 2022. "Records Request—
School Bus Data.” Released to the World Resources Institute.
Idaho State Department of Education. March 2022. "Records Re -
quest—School Bus Data.” Released to the World Resources Institute.
Illinois Secretary of State. 2 June 2022. "Records Request—School Bus 
Data.” Released to the World Resources Institute.
Indiana State Police. July 2022. "Records Request—School Bus Data.” 
Released to the World Resources Institute.
Iowa Department of Education. 17 March 2022. "Records Request—
School Bus Data.” Released to the World Resources Institute.
Kansas State Department of Education. 6 April 2022. "Records Re -
quest—School Bus Data.” Released to the World Resources Institute.
Kentucky Department of Education. 26 October 2022. “Pupil 
Transportation: Buses.” https://education.ky.gov/districts/trans/
Pages/Buses.aspx.
Lazer, L., and L. Freehafer. May 2022. “A Dataset of Electric School 
Bus Adoption in the United States.” Washington, DC: World Re -
sources Institute. https://datasets.wri.org/dataset/electric_school_
bus_adoption.  
Maine Department of Education. 2021–2022. "Records Request—
School Bus Data.” Released to the World Resources Institute.
Maryland State Department of Education, Maryland Motor Vehicle 
Administration. 21 January 2022. "Records Request—School Bus 
Data.” Released to the World Resources Institute.
Massachusetts Department of Transportation. May 2022. "Re -
cords Request—School Bus Data.” Released to the World Re -
sources Institute.
Michigan State Police. 2021. “School Bus Inspection Report for School 
Year 2020/2021.” https://www.michigan.gov/-/media/Project/Web -
sites/msp/cved/bus/school_bus_inspection_results_2021.pdf?rev=cf
cc5dd69e7246c0bc2782a6dc13122a.
Minnesota Department of Education. n.d. “Data Reports 
and Analytics.”
Mississippi Department of Education. 2021. "Records Request—
School Bus Data.” Released to the World Resources Institute.
Montana Office of Public Instruction. 30 June 2022. "Records Re -
quest—School Bus Data.” Released to the World Resources Institute.
National Highway Traffic Safety Administration. 2022. “VIN Decoder.” 
Washington, DC: U.S. Department of Transportation.  https://vpic.
nhtsa.dot.gov/decoder/.
NCES (National Center for Education Statistics). n.d. “Common Core 
of Data (CCD).” https://nces.ed.gov/ccd/files.asp. Accessed Oc -
tober 20, 2021. 
North Carolina Department of Public Instruction. 2018. “North 
Carolina School Bus Safety Web.” http://www.ncbussafety.org/
resources.html.
Nebraska Department of Motor Vehicles. 28 November 2022. 
"Records Request—School Bus Data.” Released to the World Re -
sources Institute.
Nevada Department of Education. May 2022. "Records Request—
School Bus Data.” Released to the World Resources Institute.
New Jersey Department of Environmental Protection. December 
2021. "Records Request—School Bus Data.” Released to the World 
Resources Institute.
New Mexico Public Education Department. 23 March 2022. "Re -
cords Request—School Bus Data.” Released to the World Re -
sources Institute.
New York City Department of Education. 1 August 2023. “NYC School 
Bus Fleets Data.” Released to World Resources Institute.
New York Department of Transportation. 2022. "Records Request—
School Bus Data.” Released to the World Resources Institute.
North Dakota Department of Public Instruction. 2020–2021. "Re -
cords Request—School Bus Data.” Released to the World Re -
sources Institute.
Ohio Department of Education. 21 March 2022. "Records Request—
School Bus Data.” Released to the World Resources Institute.
Oklahoma Tax Commission. 4 November 2022. "Records Request—
School Bus Data.” Released to the World Resources Institute.

TECHNICAL NOTE   |  May 2024  |  21
Dataset of U.S. School Bus Fleets
Oregon Department of Education. 2021. "Records Request—School 
Bus Data.” Released to the World Resources Institute.
Pennsylvania Department of Transportation. June 2022. "Records Re -
quest—School Bus Data.” Released to the World Resources Institute.
School Bus Fleet Magazine. 2021. “School Bus Fleet 2021 Factbook.” 
Torrance, CA: School Bus Fleet Magazine. https://www.schoolbus -
fleet.com/download?id=10131920&dl=1.
South Carolina Department of Education. 2022. "Records Request—
School Bus Data.” Released to the World Resources Institute.
South Dakota Department of Revenue. September 2022. "Records Re -
quest—School Bus Data.” Released to the World Resources Institute.
Tennessee Department of Education. 2020. “State of Tennessee 
Annual Statistical Report of the Department of Education for the 
Scholastic Year Ending June 30, 2020.” Tennessee Department of 
Education. https://eric.ed.gov/?id=ED612382.
Texas Education Agency. 2021. "Records Request—School Bus Data.” 
Released to the World Resources Institute.
Turk, J. 2022. “Jellyfish.” Python. https://github.com/jamesturk/jellyfish.
U.S. Department of Transportation, Federal Highway Administration. 
2021. “Bus Registrations: 2020.” Highway Statistics Series. Washing -
ton, DC: Federal Highway Administration. https://www.fhwa.dot.gov/
policyinformation/statistics/2020/mv10.cfm.
Utah State Board of Education. 2021. "Records Request—School Bus 
Data.” Released to the World Resources Institute.
Vermont Department of Motor Vehicles. 31 December 2021. "Re -
cords Request—School Bus Data.” Released to the World Re -
sources Institute.
Virginia Department of Education. 2022. "Records Request—School 
Bus Data.” Released to the World Resources Institute.
Washington State Office of Superintendent of Public Instruction. 
n.d. “School Bus Inventory Report.” https://eds.ospi.k12.wa.us/
BusDepreciation/default.aspx?pageName=busSearch. Accessed 
November 15, 2022.
West Virginia Department of Education. 31 May 2021. "Records Re -
quest—School Bus Data.” Released to the World Resources Institute.
Wyoming Department of Education. 29 March 2022. "Records Re -
quest—School Bus Data.” Released to the World Resources Institute.

Copyright 2024 World Resources Institute. This work is licensed under the Creative Commons Attribution 4.0 International License.  
To view a copy of the license, visit http://creativecommons.org/licenses/by/4.0/
  
10 G Street, NE  |  Washington, DC 20002  |  WRI.ORG
ABOUT WRI 
World Resources Institute is a global research organization that 
turns big ideas into action at the nexus of environment, economic 
opportunity, and human well-being. 
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
ACKNOWLEDGMENTS
Thank you to Naveen Raman for supporting the collection and 
compilation of this dataset and for developing the machine routine 
for matching school district names with LEAIDs. Thank you to Logan 
Byers from the WRI Data Lab for technical assistance with table 
extraction and LEAID matching and to Artemis Brod for editing the 
technical note. Thank you to the data source agencies for responding 
to requests for clarification about their datasets and to the Electric 
School Bus Initiative team for their support in identifying data sources 
and connecting with state-level contacts.
ABOUT THE AUTHORS
Leah Lazer  is a Research Associate focused on sustainable, 
equitable transportation with the Ross Center for Sustainable Cities 
program and the New Urban Mobility Alliance at WRI.
Lydia Freehafer  is a Research Analyst focused on sustainable, 
equitable transportation with the Ross Center for Sustainable Cities 
program and the New Urban Mobility Alliance at WRI.  
Jessica Wang is a Research Associate focused on school district 
technical assistance with the Electric School Bus Initiative at WRI.
