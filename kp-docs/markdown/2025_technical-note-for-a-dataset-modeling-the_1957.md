---
doc_id: 2025_technical-note-for-a-dataset-modeling-the_1957
source_pdf: kp-docs/askwri-kps/2025_technical-note-for-a-dataset-modeling-the_1957.pdf
extraction_method: cache-plaintext
char_count: 84554
title: Technical Note for a Dataset Modeling the Societal Health and Climate Benefits Associated With Transitioning the US School Bus Fleet From Diesel to Electric
authors: Oztaner, Burak; Soltanzadeh, Marjan; Todd, Amy; Zepka, Brian; Hakami, Amir
date_published: 8/27/2025
article_type: Technical Note
sub_tag: Transport decarbonization
wri_primary_office: WRI US
wri_programs: Cities
language: English
url: "https://www.wri.org/research/technical-note-dataset-modeling-societal-health-and-climate-benefits-electric-school-buses"
doi: "https://doi.org/10.46830/writn.24.00024"
summary: Approximately 90 percent of the half million school buses operating in the United States run on diesel, a fossil fuel known to emit harmful pollutants such as particulate matter, nitrogen oxides, and volatile organic compounds. These emissions, particularly from older buses, pose significant health risks to children and drivers, including of respiratory and cognitive impairment. Diesel exhaust has been classified as a carcinogen by the World Health Organization. Research shows that older diesel buses emit substantially more pollution than newer models, exacerbating public health burdens.
---

# Technical Note for a Dataset Modeling the Societal Health and Climate Benefits Associated With Transitioning the US School Bus Fleet From Diesel to Electric

TECHNICAL NOTE  |  Version 1.0  |  August 2025  |  1
TECHNICAL NOTE
Modeling the societal health and climate 
benefits associated with transitioning the  
US school bus fleet from diesel to electric
Y. Burak Oztaner, Marjan Soltanzadeh, Amy Todd, Brian Zepka, and Amir Hakami
CONTENTS
Abstract. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1
Introduction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1
Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .4
Findings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .9
Discussion ................................. 17
Limitations  ................................ 18
Conclusion ................................. 19
Appendix A. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .20
Appendix B. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .24
Appendix C ................................ 27
Appendix D ................................ 30
Appendix E ................................. 33
Glossary ................................... 36
References  ................................ 37
Acknowledgments ......................... 39
Technical notes document the research or analytical 
methodology underpinning a publication, interactive 
application, or tool.
Suggested Citation: Oztaner, Y.B., M. Soltanzadeh, 
A. Todd, B. Zepka, and A. Hakami. 2025. “Modeling 
the societal health and climate benefits associated 
with transitioning the US school bus fleet from 
diesel to electric.” Technical Note. Washington, DC: 
World Resources Institute. Available online at doi.
org/10.46830/writn.24.00024.
Abstract
Approximately 90 percent of the half-million school buses operating in the 
United States run on diesel, a fossil fuel known to emit harmful pollutants 
such as particulate matter, nitrogen oxides, and volatile organic compounds. 
These emissions, particularly from older buses, pose significant health risks to 
children and drivers, including respiratory and cognitive impairment. Diesel 
exhaust has been classified as a carcinogen by the World Health Organiza-
tion. Research shows that older diesel buses emit substantially more pollution 
than newer models, exacerbating public health burdens. In contrast, electric 
school buses produce zero tailpipe emissions and have the lowest greenhouse 
gas emissions of any school bus type, even when accounting for electricity 
generation. As a result, there is growing momentum toward electrifying school 
bus fleets, supported by increased public funding and policy interest.
This study is one of the first to model and quantify the health and climate 
impacts of replacing aging diesel school buses with either new diesel or new 
electric buses, incorporating both upstream and tailpipe emissions at the US 
county level. Using reverse source influence modeling, the research estimates 
the societal benefits of various fleet renewal scenarios. Key questions include 
which regions would benefit most from electrification and what the national 
emissions would be under different replacement strategies. The findings are 
intended to inform policymakers, school districts, manufacturers, and utilities 
by providing monetized estimates of health and climate impacts, enabling 
data-driven decisions about school bus fleet modernization.
Introduction
With about half a million school buses nationwide driving a total of 3.16 
billion miles per year, school buses are among the most ubiquitous and visible 
vehicles in the United States. In the 2022–23 school year, more than 21 million 
students rode the bus to school each day (School Bus Fleet Magazine 2024).

2  |  
  
An estimated 90 percent of the half-million US school buses 
are powered by fossil fuels, primarily diesel (Lazer et al. 2022). 
Diesel exhaust—classified as a carcinogen by the World Health 
Organization—contains particulate matter, cancer-causing air 
toxins, nitrogen oxides, and volatile organic compounds  (WHO 
2012; US EPA 2015). The pollution levels of school buses are 
closely tied to the age of the bus fleet. Past research has found 
that a 30-year-old diesel bus produces two to three times more 
onboard pollution than a three-year-old bus across similar time 
frames (Austin et al. 2019). Similarly, an old bus can impose 
significantly higher public health burdens on society than a 
new bus (Hakami et al. 2024a). Specifically, buses manufactured 
before 2010 produce significantly more exhaust, which infiltrates 
the bus cabin and exposes children and drivers to diesel exhaust 
pollution that negatively impacts their health and cognition. 
The World Health Organization estimates that outdoor air 
pollution caused an estimated 4.2 million premature deaths 
worldwide in 2019 (WHO 2024). A study by Anenberg et al. 
(2019) found that transportation emissions contributed to 11.4 
percent of deaths related to particulate matter and ozone. Diesel 
vehicles contributed to the majority of these mortalities and 
health impacts. 
In addition to cancer, exposure to diesel exhaust can lead to 
increased asthma symptoms and a host of other respiratory 
illnesses and health impacts such as reduced lung function, more 
frequent asthma attacks, and impaired cognitive development 
(US EPA 2025a). Children are especially susceptible to these 
risks due to their ongoing respiratory development, smaller 
average lung size, and increased activity levels (Beatty and Shim-
shack 2011). Further, diesel exhaust can directly impact student 
academic performance, since it can lead to shortened attention 
spans and respiratory illnesses that result in absenteeism. Reduc-
ing students’ exposure to air pollution from school buses while 
riding, near bus stops, and along bus routes, in contrast, has had 
positive and significant effects on student English and math test 
scores (Austin et al. 2019).
Conversely, electric school buses have zero tailpipe emissions, 
so students and the public aren’t exposed to toxic diesel exhaust 
pollution that contributes to the adverse health outcomes 
described above. Electric school buses also have the lowest 
greenhouse gas (GHG) emissions of any school bus type, even 
when accounting for emissions from the generation of electric 
power (WRI 2025). Due in part to their associated health 
and climate benefits, there has been a growing demand for the 
electrification of school bus fleets (Lazer and Freehafer 2024) as 
well as a large increase in public funding for electric school buses 
in the United States (Levinson and Achury 2024). Compared 
to diesel, electric school buses are attractive to school districts 
and communities for reasons including decreased operating 
costs, quieter rides, and opportunities to support grid resiliency. 
Specifically, about 14,000 electric school buses were on the road 
or on the way in the United States as of January 2025. At the 
beginning of 2021, there were just over 1,400 electric school 
buses on the road or on the way in the United States—meaning 
we have seen a 10-fold increase in electric school bus commit-
ments in four years (Lazer and Freehafer 2024).
The harms of aging diesel school buses that electric school buses 
often replace are well documented. However, many of the health 
and climate impacts of new electric buses compared to new diesel 
buses are not clear. This technical note is currently one of only 
two known published studies to model and quantify such cli-
mate and health impacts for new electric and new diesel school 
buses from both upstream and tailpipe emissions, specifically at 
the US county level. A recent study by Choma et al. (2024) fol-
lows a similar approach in monetizing climate and public health 
impacts of diesel school buses and the benefits associated with 
electrifying school bus fleets, but it uses different models and 
methodologies, leading to somewhat different results. We com-
pare these results and discuss the differences later in this note. 
In this technical note, we define climate impact as the atmo-
spheric release of GHGs and their warming potential, while the 
health impact is the change in excess mortality due to exposure 
to fine particulate matter. In estimating these impacts, we 
account for the atmospheric release of pollutants during school 
bus operations and, wherever possible, for the emissions associ-
ated with upstream generation of the school bus fuel, diesel 
or electricity. We use a state-of-the-art technique for reverse 
influence modeling, termed adjoint modeling, to quantify the 
location-specific impact of operational and upstream school 
bus emissions (Errico 1997). Depending on the type of school 
bus—diesel or electric—the overall estimated impact consists 
of various climate or public health components. For example, 
the health impact from diesel school buses consists of emissions 
from the bus’s tailpipe and upstream emissions, while the health 
impact from electric school buses only consists of emissions 
from upstream electricity generation, since there are zero tailpipe 
emissions from electric buses. 
Estimating the climate footprint of school buses is a straightfor-
ward process, as the impact is not dependent on the location of 
the release of GHGs. GHGs last in the atmosphere for decades, 
and their impact on the climate is therefore evenly spread across 
the globe. Consequently, estimating the climate impact of a 
school bus, diesel or electric, is reduced to estimating GHG 
emissions associated with its operation.

TECHNICAL NOTE  |  August 2025  |  3
Modeling the societal health and climate benefits associated with transitioning the US school bus fleet from diesel to electric
By contrast, air pollutants such as fine particulate matter (i.e., 
particulate matter with an aerodynamic diameter smaller than 
2.5 mm, or PM2.5) have much shorter atmospheric lifetimes, and 
as a result their impact is heavily dependent on where they are 
released. The public health impact of these short-lived air pollut-
ants can vary by orders of magnitude depending on proximity to 
populations, weather patterns, and various atmospheric transport 
and transformation processes that they can undergo. To cover 
such complexities, estimating the public health impact of diesel 
or electric school buses is best carried out by using photochemi-
cal air quality models (AQMs) that can account for various 
atmospheric processes and provide spatial distribution of air pol-
lutants (US EPA 2025b). 
There are various approaches to using AQMs in air pollution 
health impact assessments. The most common approach is to 
use AQMs to simulate atmospheric concentrations of pollutants 
with and without certain sources, or under various intervention 
scenarios, to elicit the air quality impacts from pollution sources 
of concern, such as school buses. The results from this approach, 
schematically depicted in Figure 1, are then used in epidemio-
logical modeling and/or a benefit assessment tool to estimate 
the resulting population health outcomes, such as asthma exac-
erbations, emergency room visits, premature mortality, and so 
on. These health outcomes can be expressed as incident counts, 
or as valuated or monetized estimates to facilitate benefit-cost 
analyses. This approach is straightforward and has the advantage 
that it provides a distribution of health outcomes in the popula-
tion. However, in this approach (Figure 1, top panel) it is not 
easy to distinguish between specific polluters, such as school 
buses in different districts, or school buses of different types or 
age (vintage) in the same district. 
We use a different and more recent technique—reverse source 
influence modeling—to estimate the impact of emissions associ-
ated with school buses in various counties in the contiguous 
United States. Reverse influence modeling uses an augmented 
version of a photochemical model, known as an adjoint model, 
as it traces the overall health impact on the entire population 
back to individual polluting sources at all locations. In that 
sense, reverse influence modeling using an adjoint model starts 
from the overall population health impact as characterized 
by the combination of a regular AQM and an epidemiologi-
cal model (Figure 1, bottom panel). The adjoint model then 
attributes these impacts to emissions from each school bus at 
each location (i.e., each US county). Contrary to the traditional 
approach, an adjoint model provides location-specific health 
impact estimates for school buses.
The primary objective of this research was to model the mone-
tized health and climate impacts associated with replacing aging 
diesel school buses with new diesel buses or new electric buses 
in each county in the United States to better understand the 
impacts from a range of school bus fleet renewal scenarios. These 
findings would then help us further understand where electrifi-
cation of school buses entails largest public health benefits. We 
posed two research questions:
 ▪ What estimated monetized health impacts would be 
associated with replacing old diesel school buses with either 
new electric or new diesel school buses in each US county?
 ▪ What estimated monetized climate impacts would be 
associated with replacing old diesel school buses with either 
new electric or new diesel school buses in each US county?
Figure 1  |   Traditional health impact assessment using air quality models (top) versus reverse influence modeling using 
an adjoint model (bottom)
Traditional modeling
Air quality  
model
Epidemiological 
model
Reverse influence modeling
Adjoint 
model
Note: The traditional approach provides more information about the locations where health impacts occur, while the adjoint model provides far more detail about the impacts of various 
sources on the overall population. 
Source: WRI authors.

4  |  
  
This research is targeted toward policymakers, advocates, 
researchers, school districts, school bus operators, school bus 
manufacturers, and utilities who are interested in the health 
and climate impacts of school bus fleet renewals in the United 
States. These audiences will be able to use the national or 
county-level data to compare the total monetized health and 
climate impacts of replacing older diesel school buses with new 
diesel buses or electric buses, incorporating both upstream and 
tailpipe emissions in their respective county or region. This 
will help users appreciate the health and economic burden of 
continuing to use aging diesel buses across different counties 
and states and how new buses may impact health and climate 
outcomes. Local users can incorporate these data into funding 
applications and educational materials, as well as use the find-
ings to inform their fleet renewal strategies. While this study 
uses a novel approach to address some of the questions involv-
ing the overall societal impacts of old and new school buses, it 
should be taken as a first attempt at such quantification since 
it only addresses certain aspects of the problem; future work 
exploring other aspects (e.g., other pollutants such as ozone, 
impact on vulnerable and marginalized groups, higher-resolu-
tion estimates, etc.) is needed and may be guided by the findings 
shown in this technical note.
Methods 
Our aim in this methodology is to evaluate the societal impacts 
of the release of pollutants associated with school bus powering 
and operations. In so doing, we consider climate impacts due 
to the release of GHGs, as well as the public health impact due 
to excess mortality from long-term exposure to fine particulate 
matter. In estimating these impacts, we account for the atmo-
spheric release of pollutants during school bus operation, as well 
as for the emissions associated with upstream production of 
diesel fuel or electricity (Figure 2). 
Population health impacts
We use a novel approach for reverse-source influence model-
ing to estimate the impact of emissions associated with school 
buses county by county across the contiguous United States. We 
do so by employing an augmented version of the Community 
Multiscale Air Quality (CMAQ) model developed by the US 
Environmental Protection Agency (EPA) (Byun and Schere 
2006), referred to as the adjoint model, or CMAQ-ADJ (Zhao 
et al, 2020). Traditional methods for health impact assessment 
follow emissions from various sources to the location where 
the population health impact takes place, or at various recep-
tor locations (Figure 1). Adjoint models provide the opposite 
perspective for source impact quantification. Adjoint simulations 
Figure 2  |  Components of the societal impacts (i.e., climate or public health impacts) of school bus operations, and type
CO2 from operation
Climate impact
Upstream CO2 from  
diesel production
Diesel
Tailpipe emissions
Health impact
Societal impact
Diesel production 
emissions
Climate impact CO2 from electricity 
generation
Electric
Health impact Stack emissions from 
electricity generation
Note: CO2 = carbon dioxide.
Source: WRI authors.

TECHNICAL NOTE  |  August 2025  |  5
Modeling the societal health and climate benefits associated with transitioning the US school bus fleet from diesel to electric
start with the impact on a receptor, or on a group of receptors. 
These impacts are then traced back to preceding times, all the 
way to the initial time and location of the release of the pollut-
ant from any and all sources. Contrary to traditional methods, 
an adjoint model provides location-specific source impact 
estimates, and therefore can help distinguish between the health 
impacts of school buses at various locations across the country. 
Reverse influence modeling is an effective approach for answer-
ing policy questions when the following two conditions are met:
 ▪ The policy question can be condensed into a single number 
(e.g., the number of premature deaths across the country).
 ▪ That single number has a known dependence on ambient 
concentrations.
These two conditions are met for certain types of air pollution 
health impact assessment studies. In the case of school bus 
health impacts, the health outcome (i.e., premature mortality) is 
cumulative across various locations and adds up to nationwide 
health burdens from PM2.5 exposure; in addition, the relation-
ship between pollutant concentrations and health outcomes is 
known from established epidemiological studies, which yield 
concentration-response functions (CRF). Overall, this approach 
takes location-specific emissions over time and outputs total 
health and economic impacts within the population residing in 
the entire domain of the model simulation. While these impacts 
are generally larger among populations closer to the emission 
locations, CMAQ-ADJ produces total impacts on the whole 
population, those near and far from the emission sources.
Adjoint modeling using CMAQ-ADJ relies on a range of 
upstream models (e.g., meteorological and emission models) and 
a variety of data sources (Figure 3). Adjoint simulations in our 
study are based on Hakami et al. (2024a) and Zhao et al. (2024) 
and have undergone an extensive quality-assurance process (the 
dashed area in Figure 3). While Hakami et al. (2024a) inves-
tigated various types of on-road vehicles and off-road engines, 
their study did not focus on school buses. Here, the raw results 
from that study are processed with more detailed data specific to 
school buses in the United States. While further details about 
the adjoint simulations and the underlying data can be found 
in Hakami et al. (2024a), here we apply their findings to the 
specific case of school bus impacts. 
Figure 3  |   Data flow for calculation of health impacts from the replacement of older diesel school buses with new 
diesel or electric school buses
Population and health data Epidemiological model
NCEP-NARR WRF MCIP
CMAQ-ADJ eGRID
NEI SMOKE (all emissions) CMAQ
Raw BPTs Power plant co-benefit 
calculations (2.1.2)
NEI SMOKE (school buses) Diesel bus BPTs
Electric bus health 
impactsMOVES Diesel bus co-benefit 
calculations (2.1.2)
This study
Hakami et al., 2024a
Models
Results
Diesel bus health 
impacts
Notes: BPT = benefit per ton; CMAQ = Community Multiscale Air Quality model; CMAQ-ADJ = Community Multiscale Air Quality, Adjoint model; eGRID = emissions and Generation 
Resource Integrated Database; MCIP = Meteorology-Chemistry Interface Processor; MOVES = Motor Vehicle Emission Simulator; NCEP-NARR = National Centers for Environmental 
Prediction North American Regional Reanalysis; NEI = National Emission Inventory; SMOKE = Sparse Matrix Operator Kernel Emissions; WRF = Weather Forecasting and Research. 
Terms in parentheses refer to the section in this technical note in which the item is discussed or introduced. 
Source: WRI authors.

6  |  
  
Health outcomes
Air pollution health impacts span a range of health outcomes 
from exposure to various pollutants such as PM2.5 and ozone. 
While we recognize this wide range, this study focuses only 
on excess mortality due to long-term exposure to PM2.5. It is 
important to note that our study evaluates the overall popula-
tion health impact due to PM2.5 excess mortality, and not the 
impact due to other factors or the impact on schoolchildren 
specifically. Mortality due to air pollution is by far the largest 
valuated health outcome, and PM2.5 is the single most signifi-
cant contributor to pollution-related premature mortality in the 
United States (Wolfe et al. 2019; Zhang et al. 2018). As a result, 
this study’s focus covers the largest portion of the valuated air 
pollution health impact in the United States; however, since it 
does not cover all pollutants and health impacts, the derived 
estimates should be considered underestimations. 
A number of epidemiological studies provide epidemiologi-
cal relationships between PM2.5 exposure and the excess risk 
of mortality. Our study uses the Global Exposure Mortality 
Model (GEMM) to characterize PM2.5 mortality in the United 
States (Burnett et al. 2018). Reasons for choosing GEMM are 
described in Hakami et al., where the uncertainties associated 
with the choice of GEMM as the epidemiological model are 
also evaluated (Hakami et al. 2024a). GEMM is an epidemio-
logical model from a pooled cohort of cohorts from across the 
globe, and as such covers a wider range of exposed concentra-
tions than national cohorts. GEMM employs a sublinear 
concentration response function (CRF) that conforms with 
the growing evidence of larger relative risk reductions at lower 
concentrations (Pope et al. 2015; Weichenthal et al. 2022). 
GEMM is a nonlinear CRF for the associations between pre-
mature mortality from noncommunicable diseases (NCDs) and 
lower respiratory infections (LRIs) in populations 25 years and 
older. The population data for exposure assessment were taken 
from the 2015 US census at the census block level. Baseline 
mortality rates for NCDs and LRIs were taken from the appro-
priate disease classification codes from the Centers for Disease 
Control databases. These data were mapped (gridded and/or 
aggregated) into CMAQ’s 12-kilometer (km) computational 
domain from county-level data and county shapefiles. 
School bus co-benefits
School bus impacts are quantified as benefits per ton (BPTs) 
and co-benefits for each county in the United States. The BPTs 
of a certain pollutant are the population health benefit of 
reducing school bus emissions or upstream emissions of that 
pollutant in a given county by one metric ton. Similarly, co-
benefits are estimated from BPTs and are the cumulative 
population health benefits from reduction of all pollutants, but 
normalized to, and expressed per metric ton of, carbon dioxide 
(CO2) emitted from the school bus. CMAQ-ADJ simulations 
provide estimates of BPTs for primary PM2.5 emissions and 
nitrogen oxides (NOx), sulfur dioxide (SO2), ammonia (NH3), 
and volatile organic compounds (VOCs) emitted from school 
buses that contribute to PM2.5 exposure, such as primary PM2.5, 
or NOx emissions. Co-benefits refer to the ancillary benefits of 
reducing GHG emissions that are not directly related to the 
impacts of climate change, and therefore, are not accounted for 
in climate costs of GHGs. As an example in the case of school 
buses, electrification results in reduced tailpipe emissions of CO2 
from the replaced diesel bus, as well as the associated reduction 
in the emissions of CO2’s co-emitted pollutants, such as NOx, 
SO2, and PM2.5 and VOCs. Like BPTs, co-benefits are defined 
as the monetized societal benefits associated with a reduction of 
one metric ton of emissions, but for CO2 emissions rather than 
the emissions of its co-emitted pollutants. Co-benefits form the 
basis of our health impact estimations from school bus opera-
tions. Co-benefits are calculated from BPTs via the 
following equation,
where spc is each of the co-emitted pollutants (PM2.5, NOx, SO2, 
NH3, and VOCs). Estimation of co-benefits requires informa-
tion about emissions of CO2 and co-emitted pollutants (i.e., 
intensity ratios on the right-hand side of the above equation). 
BPTs and co-benefits are estimated burdens of existing emis-
sions from a source (e.g., a diesel bus), but similarly they can be 
construed as benefits of removing that source and its emissions. 
Emissions modeling 
Air quality simulations by CMAQ or CMAQ-ADJ and the 
processing of school bus health impacts require informa-
tion about the release of pollutants into the atmosphere from 
different sources. Modeling of emissions for CMAQ and 
CMAQ-ADJ is conducted through the US EPA’s Sparse Matrix 
Operator Kernel Emissions (SMOKE) modeling systems 
(Houyoux and Vukovich 1999). SMOKE allocates available 
inventories into temporal, gridded, and speciated CMAQ-ready 
emission files. SMOKE requires emission inventory informa-
tion, and various data for spatial and temporal allocation of 
emissions, as well as for speciation to proper chemical species. 
These data are obtained from the National Emission Inventory

TECHNICAL NOTE  |  August 2025  |  7
Modeling the societal health and climate benefits associated with transitioning the US school bus fleet from diesel to electric
(NEI) 2016 platform (US EPA 2019). SMOKE is run for emis-
sions from all sectors to produce BPTs as reported in Hakami 
et al. (2024a). 
While BPT estimates are based on the 2016 NEI, school bus 
emissions are taken from the US EPA’s 2020 NEI platform (US 
EPA 2023) for all counties in the contiguous United States, to 
reflect a later year. SMOKE is run separately for school buses 
only to allocate emissions to various locations in each county. 
Processing school bus emissions separately also ensures that the 
temporal allocation of emissions (time of the day, day of the 
week, and month of the year) matches the unique characteristics 
of school bus operations. However, NEI inventories do not 
provide fleet breakdowns across school bus vintages. To estimate 
impacts from school buses from different vintages, we conduct 
simulations with the US EPA’s Motor Vehicle Emission Simula-
tor, Version 3 (MOVES3). The breakdown between different 
years is based on MOVES’s default databases. Operating pro-
cedures and technical documentation for MOVES are available 
from the US EPA (2019). MOVES is the EPA’s state-of-the-art 
emissions modeling platform that provides default inventories 
and county-specific emission factors for on-road vehicles and 
off-road engines, including school buses. We use MOVES to 
produce emission factors for various model years of school buses 
(but running MOVES3 is the default mode for all US coun-
ties for school buses alone) and to provide fleet breakdown of 
school bus impacts. Emission factors from MOVES are used for 
estimation of intensity ratios (i.e., ratio of criteria contaminants 
to CO2 emissions), as well as for burden estimates for various 
school bus vintages. 
The use of MOVES in this study entails certain limitations. 
The version of MOVES used in the study does not include 
electric school buses, as the data for the vehicle type are not 
yet mature. While electric school buses have no tailpipe emis-
sions, we assume that tire-wear and brake-wear emissions 
from these buses are similar to those from diesel school buses, 
and therefore those types of emissions are not included in 
the comparison between electric and diesel school buses. This 
assumption is made to isolate the impact from emissions that 
are linked to CO2 and combustion (i.e., affected by electrifica-
tion), and also because MOVES3 was considered inadequate to 
characterize differences between tire- and brake-wear emis-
sions from diesel and electric buses. The MOVES database 
does not distinguish between different types of school buses 
(e.g., type C or D), and, as a result, our impact assessment does 
not differentiate between school bus types either. Finally, in 
our analysis, we run MOVES for all model years up to 2020. 
As our analysis of school bus models does not extend beyond 
2020, we consider a 2020 model year diesel or electric school 
bus to be “new.” Note that our underlying BPT estimates are 
for the year 2016, as available from Hakami et al. (2024a), while 
we calculate school bus impacts for 2020 emissions to provide 
more recent information. In other words, for our calculations, 
we assume that BPTs do not change significantly between 2016 
and 2020, which has been found to be a reasonable assumption 
(Hakami et al. 2024b).
To evaluate the impact from electric school buses (i.e., upstream 
impact due to electricity generation), we use emission data 
for thermal electricity generating units in the United States. 
Emissions from all power plants are taken (on a facility basis) 
from the US EPA’s emissions and the Generation Resource 
Integrated Database (eGRID). eGRID is a compilation of 
emissions of NOx, SO2, PM2.5, ammonia, and CO2 for most 
power plants in the United States. These emissions are used in 
combination with each power plant’s location-specific BPTs 
to produce co-benefits for various coal and natural gas facili-
ties in the United States. We use CO2 inventory and electricity 
generation information from each of the 22 eGRID regions 
within the contiguous United States, in combination with 
facility-specific co-benefits from adjoint simulations, to estimate 
the upstream public health impact of the electricity use by 
electric school buses. 
Atmospheric modeling
CMAQ (Byun and Schere 2006) is a community-based air 
quality model that is widely used across the globe. Most CMAQ 
applications use the same modeling platform configuration 
used for this study. CMAQ is a multiscale and multiphase 
model that accounts for various atmospheric processes. CMAQ 
produces spatial and temporal distributions of pollutants over a 
computational domain that consists of uniform grid cells. For 
this national study, the spatial resolution of the CMAQ grid 
was 12 × 12 km. Simulations for this study are conducted for 
the year 2016 and are taken to be representative of the recent 
atmospheric composition in North America. CMAQ and 
CMAQ-ADJ are used to estimate BPTs, and subsequently, 
co-benefits across the United States at the 12-km grid, which 
are then converted to county-level estimates of co-benefits for 
various school bus models.
CMAQ requires meteorological fields produced by a meteo-
rological model. We use the National Center for Atmospheric 
Research’s Weather Forecasting and Research (WRF) model 
(Skamarock et al. 2008), driven by the National Centers for 
Environmental Prediction North American Regional Reanalysis 
datasets to create initial and boundary values for our WRF 
simulations. The Meteorology-Chemistry Interface Processor 
(MCIP) is a crucial component of the CMAQ modeling system, 
used for air quality forecasting and research. MCIP processes

8  |  
  
meteorological data from the WRF and prepares them for use in 
the CMAQ modeling system.
The CMAQ-ADJ model was developed based on CMAQ v5.0 
and includes all the atmospheric transport and transformation 
processes of that version. It has undergone extensive evalua-
tion and is publicly available (Zhao et al. 2020). The evaluation 
process for CMAQ-ADJ used various comparative methods to 
verify that CMAQ-ADJ results are consistent with the under-
lying CMAQ model. CMAQ-ADJ has been used in various 
applications for health impact assessment across different 
domains (Hakami et al. 2024a, 2024b; Zhao et al. 2024). Further 
details about the use of adjoint modeling in air quality models 
can be found elsewhere (Hakami et al. 2007; Henze et al. 2007; 
Sandu et al. 2005).
School bus health impact calculations
County-level results are processed for existing and new diesel 
and new electric school buses. These results provide societal 
impacts (health, climate, or both health and climate) for each 
type of school bus of any vintage. The benefits of school bus 
replacements can then be calculated as the difference between 
the impacts of replaced and replacing buses. The CMAQ-ADJ 
model operates on a computational grid structure, and, as a 
result, co-benefit estimates and emissions are produced and 
stored in two dimensional gridded (2D, surface) files. Using 
SMOKE allocations, school bus emissions are also estimated 
at the grid level but are then mapped onto county values using 
a geographical information system based on area overlaps 
between grids and counties. These calculations are done for 
3,108 counties in the contiguous United States, as well as 41 
independent cities.
School bus health co-benefits ($/ton-CO2) are calculated 
directly from combining adjoint BPTs and NEI emissions, 
as described above, for each county in the contiguous United 
States. Values are estimated for model years up to 2020. Addi-
tionally, co-benefits and impacts are also estimated for school 
buses in the subfleet groups and across the entire fleet. We 
consider the following model year groupings: extremely old 
(XXOLD, before 2000), very old (XOLD, 2000–2006), old 
(OLD, 2007–10), existing or current (CUR, 2011–20), and the 
entire fleet (ALL, all model years). We consider this subfleet 
grouping to somewhat (but not fully) match the gradual trend 
of more stringent standards for diesel engines. In particular, 
beginning with the 2007 model year, PM emission standards 
were tightened significantly, while more strict NOx emission 
standards were phased in between the years 2007 and 2010 (US 
EPA 2004). As noted above, we consider new school buses to be 
of the 2020 model year and onward. We produce the following 
summary results for the impact of school buses: 
 ▪ Fleet (and subfleet) impact ($/year): Fleet-level impacts (i.e., 
health burdens) associated with diesel school buses for each 
county in the contiguous United States are provided. Values 
are reported for model years 2000–2020 and for subfleet 
groupings. Total burden is calculated from co-benefit values 
(all values are at the county level).
 ▪ Unit impact ($/bus-year or $/distance): The societal burden 
associated with one diesel school bus for each county in the 
contiguous United States is reported for model years 
2000–2020 and for subfleet groupings. For a diesel school 
bus, this value can be used as the societal benefit of removing 
an existing diesel school bus from the fleet. Per-bus impacts 
are estimated from total burden estimates for each county:
Per–vehicle mile traveled (VMT) impacts are estimated in 
similar fashion:
 ▪ Electrification benefits: The difference between the societal 
health burden associated with a diesel school bus from a 
certain vintage or subfleet with that of a new electric school 
bus. Electrification benefits are provided on a per-bus basis, 
per 1,000 miles traveled, and for the subfleet groupings. 
 ▪ Electric school bus impacts are assumed to be limited to the 
upstream impact from the electricity generation, which 
produces NOx and PM2.5 emissions, for the county’s eGRID 
region. For example, per-bus upstream impacts for an electric 
bus are estimated as

TECHNICAL NOTE  |  August 2025  |  9
Modeling the societal health and climate benefits associated with transitioning the US school bus fleet from diesel to electric
Where the per-kilowatt-hour (kWh) co-benefit is calculated 
using adjoint-based co-benefits for individual power plants 
and eGRID emission and generation data. 
Diesel upstream impacts are estimated using adjoint-based 
co-benefit estimates for the oil and gas industry in the 
United States to be $35/ton-CO2, assuming that all diesel 
fuel used in the United States is produced domestically.
Similarly, upstream impacts for electric school buses are 
calculated as:
Upstream CO2 emission rates for diesel school buses (i.e., 
CO2 emissions due to production and distribution) are taken 
from the Alternative Fuel Life-Cycle Environmental and 
Economic Transportation (AFLEET) emission model 
(Burnham 2021):
Climate impacts
To value climate impacts (i.e., excluding health impacts) of 
school buses, we assign estimates of the social cost of carbon 
(SCC) to CO2 emissions. The SCC is an all-encompassing 
measure of the societal damage of GHG emissions and includes 
various endpoints such as health, extreme heat, sea level rise, 
food security, and the like. Similar to co-benefits, the SCC is 
expressed per metric ton of CO2 (or CO2-equivalent) emissions. 
Accounting of the climate footprint of school buses is a straight-
forward process, as the impact does not depend on where the 
GHGs are released. As a result, climate impact estimation will 
only require estimation of CO2 emissions. Climate impacts are 
calculated from operational (diesel) and upstream CO2 emission 
estimates (diesel and electric) by applying the SCC for moneti-
zation. Climate impacts are calculated using the latest estimate 
of the SCC: the 2022 value of $190/ton-CO2 (US EPA 2022). 
Operational CO2 emissions for diesel school buses are taken 
from MOVES for each county, while their upstream emis-
sions (diesel production and distribution) are the national-level 
value of 331 grams/mile from Argonne National Laboratory’s 
AFLEET tool (Burnham 2021). Upstream CO2 emissions for 
electric buses are based on an assumed national-level average 
electricity usage of 1.85 kWh/mile for electric buses (Levinson 
et al. 2023) and transition and charging losses of 15 percent 
(Choma et al. 2024), combined with generation and CO2 emis-
sion data for each eGRID region. Climate impacts are reported 
in the same fashion as health impacts (i.e., fleet-level, per-bus, 
and per-VMT for diesel school buses) and as electrification 
benefits (i.e., diesel impact − electric impact). 
Findings
Overview
We present a range of results that quantify the impacts of school 
bus operations in each county in the contiguous United States. 
Various forms of results are discussed in this technical note and 
its appendices. For all categories of results described below, they 
are provided for each model year and each subfleet grouping 
(XXOLD, XOLD, OLD, CUR, ALL). The datasets produced 
include the following: 
1. Diesel school bus impacts: Diesel school bus impacts are 
calculated as unit impacts and total impacts. 
i. Unit impacts for each county are provided in three 
forms: per ton-CO2 emitted (i.e., co-benefits, in units of 
$/ton-CO2), per school bus ($/bus-year), or per VMT 
($/1,000 VMT). 
ii. Total impacts for each county are impacts from all 
buses in a model year or subfleet category in that county 
and are expressed in units of $/year. Total impacts are 
broken down to health, climate, or overall (health + 
climate) impacts.  
2. Electrification benefits: Societal benefits of replacing diesel 
school buses with electric school buses are calculated as 
the difference between their respective societal impacts. 
Electrification benefits are made up of both climate and 
health benefits of school bus replacement. Similar to the 
diesel school bus results, these benefits are provided for all 
US counties, and as unit impacts (per bus or per VMT) and 
total impacts ($/year) for model year or subfleet categories.

10  |  
  
Health impacts of diesel school buses 
Diesel school bus health impacts, expressed per bus, per VMT , 
or as co-benefits, vary significantly across counties and by bus 
vintage (Figure 4). Per VMT impacts range from less than 
$10/1,000 miles to nearly $4,000/1,000 miles across all counties 
and model years. As one would expect, larger impacts are from 
emissions in more populous counties, as school bus emissions in 
these counties affect a larger population, and older diesel school 
buses have greater impacts as they emit greater amounts of pol-
lutants. Among the counties with the largest impacts are Kings 
County, Queens, and the Bronx (NY), Orange County and 
Sacramento (CA), Philadelphia (PA), and Washington (DC). 
There is a gradual reduction in health impacts in newer model 
years due to more stringent tailpipe emission control standards. 
This reduction is most significant starting in the 2007 model 
year, when new PM emissions standards for heavy-duty diesel 
vehicles took effect, while more stringent NOx standards were 
phased in between 2007 and 2010. 
The disparity in the health burden of school bus emissions 
(Figure 4) reveals the value of the adjoint model in providing 
location-specific source impact estimates. The extent of school 
bus health impact variability across counties and model years 
can also be seen in Figure 5, which depicts the share of health 
impacts borne by various fractions of school buses or their 
VMTs. Each point on the plot (also known as the Lorenz curve) 
corresponds to the share of the diesel school bus impact (y-axis 
value) that can be attributed to the share of the most damaging 
emissions by number of buses or their VMTs (x-axis value). If 
emissions from school buses were all equally impactful, then 
Figure 5 would reduce to the one-on-one (black) line. In other 
words, the significant curvature of the curves in Figure 5 indi-
cate differences in school bus emission impacts across counties 
and vintages. For instance, the top 10 percent and 20 percent of 
the school buses with the highest impacts account for 49 percent 
and 65 percent of the health burden of the total diesel school 
bus fleet in the United States, respectively. Similarly, the top 10 
percent and 20 percent of the most damaging miles traveled by 
school buses are responsible for 54 percent and 70 percent of the 
health burden of the fleet. School buses with the largest impacts 
are likely the result of two contributing factors: more pollut-
ing (i.e., older) buses and operation in more populous counties 
where a larger population is exposed to the emissions of the 
school bus. Note that impacts shown in Figure 5 only include 
health impacts of school bus operations, and not the climate 
Figure 4  |   Per VMT impacts of diesel school buses for the all fleet average (left) and older (2000–2006, right)
Notes: VMT = vehicle miles traveled.
Source: WRI authors.
Impact per 1,000 miles: Health (Diesel, all model years) Impact per 1,000 miles: Health (Diesel, 2000–2006 model years)
$/1,000 miles-year
51 03 05 01 00 1502 00 250 300 4005 00 600 800 1,0001 ,500 2,000 2,5003 ,000

TECHNICAL NOTE  |  August 2025  |  11
Modeling the societal health and climate benefits associated with transitioning the US school bus fleet from diesel to electric
Figure 5  |   The share of the health burden imposed by fractions of the most polluting school buses (orange),  
or school bus VMTs (blue)
Notes: VMTs = vehicle miles traveled. For example, nearly 50 percent of the health burden of all school buses is attributed to only 10 percent of the most polluting buses. 
Source: WRI authors.
0.0
0.2
0.4
0.6
0.8
1.0
0.0 0.20 .4 0.6 0.8 1.0
Fraction of Health Burden 
Fraction of School Buses or School Bus VMT 
School bus VMT
School bus number
impacts. There is significantly less variability of climate impacts 
of tailpipe CO2 emissions from school buses across counties and 
model years. This is due to two facts: climate impacts are not 
location-dependent, and changes in fuel efficiency (and there-
fore CO2 emissions) across different vintages are significantly 
less pronounced than the change in emissions of air pollutants.
Figure 6 shows the overall impact (climate and health) of school 
buses in all US counties for OLD (2000–2006) and newer (i.e., 
CUR, 2011–20) fleet segments, and for 2022 SCC values. As 
mentioned before, in 2007 new PM standards were enacted 
for heavy-duty diesel vehicles, resulting in significantly lower 
health impacts. However, these standards did not affect fuel 
efficiency as significantly, and therefore the climate impacts of 
these newer vehicles decreased only marginally. Higher VMTs 
for newer school buses result in comparable overall (i.e., climate 
and health) impacts for newer buses, despite their lower tailpipe 
emissions of criteria pollutants. The relative contribution of 
the health impact to the overall impact can be seen in Figure 
7. Given the increase in the value of SCC in 2022, the overall 
impact is dominated by climate impacts under this higher value 
of SCC, where the contribution of health impacts is only com-
parable to that of climate impacts in some major urban areas.

12  |  
  
Figure 7  |  Ratio of health impacts to overall impacts (climate and health) for the 2022 SCC
Note: SCC = social cost of carbon.
Source: WRI authors.
Fraction of health total benefits (2022 SCC)
Fraction
0.05 0.10 .150 .2 0.25 0.30 .350 .4 0.45 0.50 .550 .6 0.65 0.70 .8 0.9
Figure 6  |  Per-bus impact of older (2000–2006, left) and newer (2011–20, right) school buses across the United States
Note: SCC = social cost of carbon. 
Source: WRI authors.
Impact per bus: Climate + health (Diesel, 2022 SCC, 2000–2006 model years) Impact per bus: Climate + health (Diesel, 2022 SCC, 2011–2020 model years)
$/bus-year
400
600
800
1,000
1,500
2,000
2,250
2,500
2,750
3,000
3,250
3,500
3,750
4,000
4,500
5,000
5,500
6,000
7,000
8,000
10,000
12,500
15,000
20,000
30,000
40,000
50,000

TECHNICAL NOTE  |  August 2025  |  13
Modeling the societal health and climate benefits associated with transitioning the US school bus fleet from diesel to electric
Figure 8  |   The total impact of diesel school bus fleets for very old (2000–2006) and newer (2011–20) fleet segments,  
and for the entire fleet of diesel school buses (bottom) in all counties in the United States
Note: SCC = social cost of carbon. 
Source: WRI authors.
Impact, fleet: Climate + health (Diesel, 2022 SCC, 2000–2006 model years) Impact, fleet: Climate + health (Diesel, 2022 SCC, 2011–2020 model years)
$1,000/year
51 01 52 02 55 07 51 00 1502 00 250 300 5007 00 1,0001 ,500 2,000 3,000 4,0005 ,000 10,000
Impact, fleet: Climate + health (Diesel, 2022 SCC, all model years)

14  |  
  
Table 1  |   Summary of nationwide (contiguous United States) diesel school bus statistics and impacts presented in  
this report
FLEET COUNT (1,000) VMTS (M) HEALTH IMPACT ($M) CLIMATE IMPACT ($M) TOTAL IMPACT ($M)
< 2000 40 300 150 90 240
2000–2006 100 1,000 290 300 600
2007–10 80 900 60 290 350
2011–20 300 4,400 170 1450 1,620
All fleet 520 6,600 670 2,140 2,810
Notes: M = million; VMTs = vehicle miles traveled. The table also includes the total count and VMTs of each school bus subfleet grouping.
Source: WRI authors.
The results shown in Figure 6 are per-bus impacts. The total 
impact for the full fleet population of school buses (i.e., the 
impact of all school buses in each county) or subfleet population 
(e.g., the impact of all buses from 2000–2006 model years in 
every county) can be calculated by accounting for the number of 
buses in each county (Figure 8). Newer diesel school buses are 
more numerous and have more VMTs, and therefore they pose 
greater societal impacts, particularly climate ones. The impact is 
noticeably larger for major urban areas, where both the health 
impacts and the number of buses operating are larger. Figure 8 
also shows the impact of the entire fleet of diesel school buses 
for each county in the United States. Table 1 summarizes the 
nationwide impacts of diesel school buses for various sub-
fleet groupings. 
Benefits of school bus electrification
The benefits of school bus electrification are calculated as the 
difference between climate and health impacts of diesel and 
electric school buses. For electric school buses, those impacts 
would depend on the electricity market where the bus oper-
ates and is charged. We use eGRID reported emission levels 
for CO2 and air pollutants, together with electricity produc-
tion data, to account for climate and health impacts. All 
electric buses are assumed to be 2020 model year, and they are 
compared on a bus-to-bus basis with individual diesel school 
buses in any county. The resulting total benefits are compiled 
by aggregating benefits across individual buses for each fleet 
grouping and county.
The electrification of school buses generally results in benefits 
(Figure 9), with the largest benefits in larger cities, particularly 
along the coasts. However, there are occasional regions where 
electrification entails disbenefits (i.e., negative benefits); for 
example, in some Midwest US counties in Illinois, Missouri, 
Kentucky, Wisconsin, and so on. Electricity in these areas is 
serviced by two eGRID regions (Midwest Reliability Organiza-
tion East and SRC Midwest) that relied most heavily on coal 
(in 2020) and have the highest CO2 emissions rates. As a result, 
the health and climate impact of electricity generation through 
coal is larger than that of diesel school bus operations. In these 
areas, while electrification of older school buses is beneficial, 
electrification of newer (2011–20 model years) school buses 
entails small disbenefits due to the reliance of the electricity mix 
on coal. These disbenefits are the results of the current grid’s reli-
ance on coal; as the electricity grid becomes cleaner and/or less 
reliant on coal, they are likely to turn to benefits. We also note 
that the magnitude of occasional disbenefits are considerably 
smaller than the benefits provided in much of the United States.
Electrification of school buses is particularly beneficial in large 
urban areas, where the health benefits of electrification are more 
pronounced (Figure 10). This is primarily due to the proximity 
of the bus operation to population. In all major cities, the ben-
efits of electrification are significantly larger than the benefits 
of fleet renewal with new diesel school buses. Nationwide, we 
estimate benefits of $1.6 billion/year for electrification of the 
entire US school bus fleet under the 2022 SCC values.

TECHNICAL NOTE  |  August 2025  |  15
Modeling the societal health and climate benefits associated with transitioning the US school bus fleet from diesel to electric
Figure 9  |   Benefits: Benefits of electrification of school buses for older (2000–2006, left) and newer (2011–20, right) buses
Notes: SCC = social cost of carbon. Benefits are shown per 1,000 vehicle miles traveled (top) and as total fleet benefits (bottom). The color map is not symmetrical for positive and 
negative values.
Source: WRI authors.
$/1,000 miles (diesel-electric)
-175 -150 -100 -50 -30 -10 -5 -1 0 5 10 30 50 100 200 300 500 700 1,000 1,250 1,750
Electrification benefits: Per 1,000 miles (2022 SCC, 2000–2006 model years) Electrification benefits: Per 1,000 miles (2022 SCC, 2011–2020 model years)
$1,000/year (diesel-electric)
Electrification benefits: Fleet (2022 SCC, 2000–2006 model years) Electrification benefits: Fleet (2022 SCC, 2011–2020 model years)
1,500
-30
-20
-1
-0.1
0
0.15
10 20
25
30 50
75
100
1507 50
1,000
1,500
2,000
3,000
4,000-10
-5
1
15 45
200
250
500

16  |  
  
Figure 10  |   Comparison of the yearly societal impacts of existing and new diesel and electric school buses in major 
urban areas in the United States  
Notes: SCC = social cost of carbon.
Source: WRI authors.
05 00 1,0001 ,500 2,0002 ,500 3,0003 ,500 4,000
Denver, CO
Los Angeles, CA
Dallas, TX
Philadelphia, PA
Multnomah, OR
Johnson, KS
Suﬀolk, MA
Cook, IL
Fulton, GA
Richmond, NY
Bronx, NY
Kings, NY
Queens, NY
New York, NY
Albany, NY
Monroe, NY
Erie, NY
$US per 1,000 miles
New electric: 2020 model year
New diesel: 2020 model year
Diesel: 2000–2006 model years
Diesel: All model years (1990–2020)

TECHNICAL NOTE  |  August 2025  |  17
Modeling the societal health and climate benefits associated with transitioning the US school bus fleet from diesel to electric
Discussion
We note that the most recent results presented here are 
estimates of the school bus impacts and the benefits of their 
electrification as of 2020, given available data from MOVES. 
Any school bus model year after 2020, diesel or electric, will 
have life cycle impacts that are not accounted for in this study. 
Also, the operational impacts of school buses are bound to 
change in time. The age of the fleet, and consequently its 
emissions characteristics, will change as old units are decom-
missioned and more stringent new vehicle standards take effect 
for new school buses. The electricity mix in the United States 
is likely to become cleaner and less reliant on fossil fuels, which 
would in turn help increase benefits of electrification. Changes 
in atmospheric composition will impact BPT and co-benefit 
estimates because of the changing chemical regimes, although 
these changes are likely to be small within the lifetime of the 
existing fleet. 
While several studies have investigated the impact of diesel 
school buses on students, studies of the impact of school buses 
on general population health and climate are rather limited. The 
recent study by Choma et al. (2024) similarly investigates the 
benefits of electrifying school buses in the United States, but 
Choma et al. (2024) estimate substantially larger nationwide 
health impacts for diesel school buses (in 2017) and lower 
health impacts for electric school buses than this study, though 
the climate benefit estimates are generally comparable. Several 
factors contribute to these discrepancies. Choma et al. (2024) 
include asthma in their health outcomes (an increase of about 
10 percent in their valuation) and use higher valuations (2023 
US$ vs. 2016 US$) for the value of statistical life and the SCC 
(an increase of about 15 percent). Choma et al. (2024) estimate 
lifetime electrification benefits by projecting a nationwide aver-
age for future electricity generation impacts. Further, they use a 
simplified modeling platform that may not fully and adequately 
capture the response of the atmosphere to emissions, and that 
has a tendency to overestimate the health burden from trans-
portation (Choma et al. 2021; Davidson et al. 2020; Fann et al. 
2013). However, their modeling platform does employ higher 
spatial resolution in urban areas that better represents popula-
tion distributions. Table 2 summarizes the differences between 
the two studies. Nonetheless, as climate benefits constitute a 
large portion of the total electrification benefits, the overall 
benefit estimates from both studies are generally comparable. 
Table 2  |  Comparison of methods and results of this study with Choma et al. (2024)
ITEM CHOMA ET AL. (2024) THIS STUDY
Inputs, 
assumptions, 
and methods
Health outcomes Mortality and asthma from PM 2.5 Mortality from PM 2.5
Epidemiological model (mortality) GEMM GEMM
VSL $12.4M $10.2M
SCC $228/ton-CO 2 $190
VMT 6.8B miles 6.6B miles
Number of buses ~500,000 520,000
Emitted pollutants considered PM2.5 , SO2, NOx, NH3, VOCs PM2.5 , SO2, NOx, NH3, VOCs
Air quality model Reduced complexity (InMAP) Full complexity (CMAQ)
Model resolution Variable, down to 1 km in cities 12 km
Temporal variability (seasonality) Not considered Considered
Electricity generation burden Nationwide, projected Grid-dependent, 2020
Electricity losses 15% 15%
Energy use by electric buses 1.54 kWh/mi 1.85 kWh/mi

18  |  
  
Limitations 
The estimates provided in this study are subject to several 
limitations stemming from incomplete inputs, model errors and 
imperfections, and study assumptions. Like all modeling studies, 
our results are also subject to a range of uncertainties. Sources of 
these uncertainties include, but are not limited to, uncertainty in 
emissions, including those of school buses; uncertainty in epi-
demiological models; lack of detailed county-level information 
about school bus fleets and operations; and a lack of knowledge 
of the operational parameters of electric school buses. Our 
results are also subject to the following limitations due to mod-
eling constraints or study design:
 ▪ Our health impact estimation only included mortality as the 
health endpoint due to chronic PM2.5 exposure. Diesel school 
buses have significant NOx emissions that can lead to ozone-
induced health outcomes, including asthma and mortality. 
NOx emissions also lead to increased NO2 exposure, with 
its associated impacts on mortality or morbidity (Faustini et 
al. 2014; Khreis et al. 2017; Turner et al. 2016). Due to the 
magnitude of NOx emissions from heavy-duty diesel engines, 
exclusion of ozone from the analysis is likely to result in 
a sizeable underestimation of the impact of diesel school 
buses or the benefits of their electrification. As a result, the 
inclusion of NOx also has the potential to delineate a sharper 
contrast between population health impacts of new electric 
and diesel school buses. The adjoint model used here can also 
be employed in future studies to extend the estimates in this 
study to include ozone-related health outcomes.
ITEM CHOMA ET AL. (2024) THIS STUDY
Results Diesel school bus health burden * $1.8B $670M
Diesel school bus health burden ($/mi) * 0.27 $/mi 0.1 $/mi
Electrification benefits ** $1.9B $1.6B
Electrification benefits ($/mi) ** 0.28 $/mi 0.24 $/mi
Disparity (burden of worst 10% miles) 30% 54%
Notes: B = billion; CMAQ = Community Multiscale Air Quality model; CO 2 = carbon dioxide; GEMM = Global Exposure Mortality Model; InMAP =  Intervention Model for Air Pollution; 
kWh = kilowatt-hours; km = kilometers; M = million; mi = miles; NH 3 = ammonia; NO x = nitrogen oxides; PM = particulate matter; SCC = social cost of carbon; SO 2 = sulfur dioxide; VMT 
= vehicle miles traveled; VOC = volatile organic compound; VSL = value of statistical life; * Mortality only, i.e., asthma excluded; ** Climate and health benefits.
Source: WRI authors. 
Table 2  |  Comparison of methods and results of this study with Choma et al. (2024) (cont).
 ▪ While the approach used in this study can be extended 
to estimate county-specific environmental justice 
benefits of school bus electrification, our study focused 
on the health and climate impacts of school buses. Like 
other transportation sources, school bus emissions are 
likely contributors to air pollution exposure disparities. 
Environmental justice and equity benefits are important 
considerations in the analysis of school bus electrification 
that are absent from the current study. An analysis of 
environmental justice benefits (e.g., with regards to race, 
ethnicity, gender, or income) is likely to result in its own 
differential delineation of impacts across different counties, 
adding another layer of differentiation between school bus 
electrification benefits in different counties.
 ▪ Our results at a 12-km resolution in major cities show 
school bus health impacts that are 20–40 times larger than 
the national average. While 12-km resolution is found 
to be generally sufficient for health impact assessment 
studies, in certain cities higher resolution simulations can 
lead to significantly higher estimates (Hakami et al. 2024b; 
Valencia et al. 2023). 
 ▪ In our analysis we did not consider brake- and tire-wear 
emissions, assuming that they are similar for diesel and 
electric school buses. Due to operational differences between 
electric and diesel engines and weight differences between 
the vehicles, this assumption may not be justifiable, and as 
more data on emissions from electric heavy-duty vehicles 
become available, it should be revisited.

TECHNICAL NOTE  |  August 2025  |  19
Modeling the societal health and climate benefits associated with transitioning the US school bus fleet from diesel to electric
To address these limitations, we recommend that future studies 
using this methodology include the following:
 ▪ Estimation of cumulative health benefits (mortality and 
morbidity due to exposure to PM2.5, ozone, and NO2).
 ▪ Incorporation of environmental justice benefits of school bus 
electrification with population health and climate benefits.
 ▪ Conducting of higher-resolution simulations in select cities, 
particularly densely populated areas on the West Coast, as 
such areas are likely to be more sensitive to model resolution 
(Hakami et al. 2024b). 
Conclusion
This study contributes important data to help policymakers, 
districts, advocates, and others understand the societal impacts 
of school bus fleets, particularly when deciding to purchase a 
new diesel or electric school bus. The data help fill a gap in the 
literature about the actual effects of school bus electrification in 
the United States. We recommend that future work use these 
county-level results to analyze the equity implications of the 
current societal impacts of school bus fleets nationwide, as well 
as the potential effects of electrification. These calculations can 
be done using county-level census data. Policymakers can also 
use the data and findings to promote public investments in 
school bus electrification. 
Further work can also address the limitations listed above and 
build on this important foundational work. As interest and 
policy support grow for school bus electrification, it is important 
to maintain and expand the evidence base for the effects of 
diesel versus electric school buses. Federal, state, and local policy 
changes, as well as technological improvements in bus design, 
electricity procurement, and the energy grid, have the potential 
to shift outcomes over time. This reinforces the need for contin-
ued updates to these findings and associated modeling efforts.

20  |  
  
Appendix A: Health and climate impacts 
($/1,000 miles-year) of school buses 
(diesel and electric)
Figure A-1  |  Health and climate impact per 1,000 miles VMT of diesel school buses for model years
Impact per 1,000 miles: Climate + health (Diesel, 2022 SCC)
$/1,000 miles-year
10 50 1001 50 2002 50 300 4005 00 6007 00 800 900 1,0001 ,500 2,000 2,5003 ,000
200820072006
200520042003
2000 2001 2002

TECHNICAL NOTE  |  August 2025  |  21
Modeling the societal health and climate benefits associated with transitioning the US school bus fleet from diesel to electric
Figure A-1  |  Health and climate impact per 1,000 miles VMT of diesel school buses for model years (cont.)
Note: VMT = vehicle miles traveled.
Source: Authors.
Impact per 1,000 miles: Climate + health (Diesel, 2022 SCC)
$/1,000 miles-year
10 50 1001 50 2002 50 300 4005 00 6007 00 800 900 1,0001 ,500 2,000 2,5003 ,000
20102009
202020192018
201720162015
201420132012
2011

22  |  
  
Figure A-2  |  Health and climate impact per 1,000 miles VMT of diesel school buses for fleet segments
Note: VMT = vehicle miles traveled.
Source: Authors.
 Impact per 1,000 miles: Climate + health (Diesel, 2022 SCC)
Pre-2000 2000–2006 2007–2010
2011–2020 All model years
$/1,000 miles-year
10 50 1001 50 2002 50 300 4005 00 6007 00 800 900 1,0001 ,500 2,000 2,5003 ,000

TECHNICAL NOTE  |  August 2025  |  23
Modeling the societal health and climate benefits associated with transitioning the US school bus fleet from diesel to electric
Figure A-3  |  Health and climate impact per 1,000 miles VMT for new electric school buses (2020 model year)
Note: VMT = vehicle miles traveled.
Source: Authors.
Impact per 1,000 miles (electric): Climate + health (2022 SCC, all model years)
$/1,000 miles-year
50 60 80 100 125 150 175 200 225 250 300 350

24  |  
  
Appendix B: Health and climate burden 
($/year) of school buses (diesel)
Figure B-1  |  Health and climate burden ($/year) of diesel school buses for model years
Impact, fleet: Climate + health (Diesel, 2022 SCC)
200820072006
200520042003
2000 2001 2002
$1,000/year
0.5 1 3 5 7 10 13 15 20 25 30 40 45 50 60 75 100 1,000150 200 250 300 500 700

TECHNICAL NOTE  |  August 2025  |  25
Modeling the societal health and climate benefits associated with transitioning the US school bus fleet from diesel to electric
Figure B-1  |  Health and climate burden ($/year) of diesel school buses for model years (cont.)
Source: Authors.
Impact, fleet: Climate + health (Diesel, 2022 SCC)
20102009
202020192018
201720162015
201420132012
2011
$1,000/year
0.5 1 3 5 7 10 13 15 20 25 30 40 45 50 60 75 100 1,000150 200 250 300 500 700

26  |  
  
Figure B-2  |  Health and climate burden ($1,000/year) of diesel school buses for fleet segments
Source: Authors.
Impact, fleet: Climate + health (Diesel, 2022 SCC)
Pre-2000 2000–2006 2007–2010
2011–2020 All model years
$1,000/year
5 10 15 20 25 50 75 100 150 200 250 300 500 700 1,000 10,0001,500 2,000 3,000 4,000 5,000

TECHNICAL NOTE  |  August 2025  |  27
Modeling the societal health and climate benefits associated with transitioning the US school bus fleet from diesel to electric
Appendix C: Health and climate benefits 
of electrification ($/1,000 miles-year) of 
diesel school buses
Figure C-1  |  Health and climate benefits of electrification ($/1,000 miles-year) of diesel school buses for model years
Electrification benefits: Per 1,000 miles (2022 SCC)
200820072006
200520042003
2000 2001 2002
$/1,000 miles (diesel-electric)
-175 -150 -100 -50 -30 -10 -5 -1 0 5 10 30 50 100 200 300 500 1,750700 1,000 1,250 1,500

28  |  
  
Figure C-1  |  Health and climate benefits of electrification ($/1,000 miles-year) of diesel school buses for model years (cont.)
Source: Authors.
Electrification benefits: Per 1,000 miles (2022 SCC)
20102009
202020192018
201720162015
201420132012
2011
$/1,000 miles (diesel-electric)
-175 -150 -100 -50 -30 -10 -5 -1 0 5 10 30 50 100 200 300 500 1,750700 1,000 1,250 1,500

TECHNICAL NOTE  |  August 2025  |  29
Modeling the societal health and climate benefits associated with transitioning the US school bus fleet from diesel to electric
Figure C-2  |  Health and climate benefits of electrification ($/1,000 miles-year) of diesel school buses for fleet segments
Source: Authors.
Electrification benefits: Per 1,000 miles (2022 SCC)
Pre-2000 2000–2006 2007–2010
2011–2020 All model years
$/1,000 miles (diesel-electric)
-175 -150 -100 -50 -30 -10 -5 -1 0 5 10 30 50 100 200 300 500 1,750700 1,000 1,250 1,500

30  |  
  
Appendix D: Health and climate benefits 
of electrification ($/bus-year) of diesel 
school buses
Figure D-1  |  Health and climate benefits of electrification ($/bus-year) of diesel school buses for model years
Electrification benefits: Per bus (2022 SCC)
200820072006
200520042003
2000 2001 2002
$/bus-year (diesel-electric)
-1,200
-500
-400
-300
-200
-100
-50
-5
0
5
50
150
250
500
750
1,000
1,250
1,500
2,000
2,500
3,000
3,500
4,000
5,000
7,000
10,000
15,000
-1,000
-700

TECHNICAL NOTE  |  August 2025  |  31
Modeling the societal health and climate benefits associated with transitioning the US school bus fleet from diesel to electric
Figure D-1  |  Health and climate benefits of electrification ($/bus-year) of diesel school buses for model years (cont.)
Source: Authors.
Electrification benefits: Per bus (2022 SCC)
20102009
202020192018
201720162015
201420132012
2011
$/bus-year (diesel-electric)
-1,200
-500
-400
-300
-200
-100
-50
-5
0
5
50
150
250
500
750
1,000
1,250
1,500
2,000
2,500
3,000
3,500
4,000
5,000
7,000
10,000
15,000
-1,000
-700

32  |  
  
Figure D-2  |  Health and climate benefits of electrification ($/bus-year) of diesel school buses for fleet segments
Source: Authors.
Electrification benefits: Per bus (2022 SCC)
Pre-2000 2000–2006 2007–2010
2011–2020 All model years
$/bus-year (diesel-electric)
-1,200
-500
-400
-300
-200
-100
-50
-5
0
5
50
150
250
500
750
1,000
1,250
1,500
2,000
2,500
3,000
3,500
4,000
5,000
7,000
10,000
15,000
-1,000
-700

TECHNICAL NOTE  |  August 2025  |  33
Modeling the societal health and climate benefits associated with transitioning the US school bus fleet from diesel to electric
Appendix E: Health and climate  
benefits of electrification ($/year)  
of diesel school buses
Figure E-1  |  Health and climate benefits of electrification ($1,000/year) of diesel school buses for model years
Electrification benefits: Fleet (2022 SCC)
200820072006
200520042003
2000 2001 2002
$1,000/year (diesel-electric)
-30 -20 -10 -5 -1 -0.1 0 0.1 1 3 5 7 10 250 300 500 700 1,00015 20 25 30 45 50 75 100 150 200

34  |  
  
Figure E-1  |  Health and climate benefits of electrification ($1,000/year) of diesel school buses for model years (cont.)
Source: Authors.
Electrification benefits: Fleet (2022 SCC)
20102009
202020192018
201720162015
201420132012
2011
$1,000/year (diesel-electric)
-30 -20 -10 -5 -1 -0.1 0 0.1 1 3 5 7 10 250 300 500 700 1,00015 20 25 30 45 50 75 100 150 200

TECHNICAL NOTE  |  August 2025  |  35
Modeling the societal health and climate benefits associated with transitioning the US school bus fleet from diesel to electric
Figure E-2  |  Health and climate benefits of electrification ($1,000/year) of diesel school buses for fleet segments
Source: Authors.
Electrification benefits: Fleet (2022 SCC)
Pre-2000 2000–2006 2007–2010
2011–2020 All model years
$1,000/year (diesel-electric)
-20- 5 -0.10 .1 52 51 ,500 3,00045 75 1502 50 75015
-30 -10- 10 11 02 01 ,000 2,00030 50 1002 00 500 4,000

36  |  
  
Glossary
Air contaminants:  Co-emitted pollutants with CO 2, other than 
greenhouse gases.
Benefits per ton (BPTs): Monetized societal benefits of a metric 
ton reduction in emissions of a pollutant (e.g., primary particles, or 
precursors such as nitrogen oxides, volatile organic compounds, or 
ammonia). Expressed in units of $/ton-pollutant.
Co-benefits:  In this technical note, the monetized societal health 
benefits of a metric ton reduction in CO 2 emissions. Co-benefits in 
this note refer to health benefits from reduced emissions of co-
emitted criteria pollutants, regardless of the impact of a changing 
climate. Similar to BPTs, co-benefits refer to health benefits but are 
expressed per units of emitted CO 2 ($/ton-CO2).
Concentration response function:  Epidemiological relationship 
between increased risk of mortality and exposure.
Intensity ratios:  Mass ratios of criteria air contaminants to CO 2 
emissions from an emissions source.
Social cost of carbon (SCC): Aggregated monetized impact of 
climate change attributed to a metric ton of CO 2 emissions. SCC only 
accounts for impacts due to climate change and does not include air 
pollution health co-benefits from reduced emissions of co-emitted 
pollutants, as defined above. Expressed in units of $/ton-CO 2.
Valuation (valuated benefits):  Monetizing intangible burdens and 
external costs.
Value of statistical life (VSL):  A widely used willingness-to-pay 
measure for monetization of a statistical life in governmental cost-
benefit analysis.

TECHNICAL NOTE  |  August 2025  |  37
Modeling the societal health and climate benefits associated with transitioning the US school bus fleet from diesel to electric
References 
Anenberg, S.C., J. Miller, D.K. Henze, R. Minjares, and P. Achakulwisut. 
2019. “The Global Burden of Transportation Tailpipe Emissions on Air 
Pollution–Related Mortality in 2010 and 2015.” Environmental Research 
Letters 14 (9): 094012. https://doi.org/10.1088/1748-9326/ab35fc.
Austin, W., G. Heutel, and D. Kreisman. 2019. “School Bus Emissions, 
Student Health and Academic Performance.” Economics of Education 
Review 70: 109–26. https://doi.org/10.1016/j.econedurev.2019.03.002.
Beatty, T.K.M., and J.P. Shimshack. 2011. “School Buses, Diesel Emis -
sions, and Respiratory Health.” Journal of Health Economics 30 (5): 
987–99. https://doi.org/10.1016/j.jhealeco.2011.05.017.
Burnett, R., H. Chen, M. Szyszkowicz, N. Fann, B. Hubbell, C.A. Pope, 
et al. 2018. “Global Estimates of Mortality Associated with Long-Term 
Exposure to Outdoor Fine Particulate Matter.” Proceedings of the Na -
tional Academy of Sciences 115: 9592–97. doi:10.1073/pnas.1803222115.
Burnham, A. 2021. User Guide for AFLEET Tool 2020 . file:///C:/Users/
User/Downloads/User%20Guide%20for%20AFLEET%20Tool%20
2020.pdf.
Byun, D., and K.L. Schere. 2006. “Review of the Governing Equations, 
Computational Algorithms, and Other Components of the Models-3 
Community Multiscale Air Quality (CMAQ) Modeling System.” Applied 
Mechanics Reviews 59: 51–77. doi:10.1115/1.2128636.
Choma, E.F., J.S. Evans, J.A. Gómez-Ibáñez, Q. Di, J.D. Schwartz, J.K. 
Hammitt, et al. 2021. “Health Benefits of Decreases in On-Road Trans -
portation Emissions in the United States from 2008 to 2017.” Proceed -
ings of the National Academy of Sciences 118: e2107402118. doi:10.1073/
pnas.2107402118.
Choma, E.F., L.A. Robinson, and K.C. Nadeau. 2024. “Adopting Electric 
School Buses in the United States: Health and Climate Benefits.” 
Proceedings of the National Academy of Sciences 121: e2320338121. 
doi:10.1073/pnas.2320338121.
Davidson, K., N. Fann, M. Zawacki, C. Fulcher, and K.R. Baker. 2020. 
“The Recent and Future Health Burden of the U.S. Mobile Sector 
Apportioned by Source.” Environmental Research Letters  15: 075009. 
doi:10.1088/1748-9326/ab83a8.
Errico, R.M. 1997. “What Is an Adjoint Model?” Bulletin of the American 
Meteorological Society  78 (11): 2577–92.
Fann, N., C.M. Fulcher, and K. Baker. 2013. “The Recent and Fu -
ture Health Burden of Air Pollution Apportioned across U.S. 
Sectors.” Environmental Science and Technology 47: 3580–89. 
doi:10.1021/es304831q.
Faustini, A., R. Rapp, and F. Forastiere. 2014. “Nitrogen Dioxide and 
Mortality: Review and Meta-analysis of Long-Term Studies.” European 
Respiratory Journal  44: 744–53. doi:10.1183/09031936.00114713.
Hakami, A., D.K. Henze, J.H. Seinfeld, K. Singh, A. Sandu, S. Kim, et al. 
2007. “The Adjoint of CMAQ.” Environmental Science and Technology 
41: 7807–17. doi:10.1021/es070944p.
Hakami, A., S. Zhao, M. Soltanzadeh, P. Vasilakos, A. Alhusban, B. Oz -
taner, et al. 2024a. “Estimating Model-Based Marginal Societal Health 
Benefits of Air Pollution Emission Reductions in the United States and 
Canada.” Research Reports: Health Effects Institute , 218.
Hakami, A., S. Zhao, P. Vasilakos, A. Alhusban, Y.B. Oztaner, A. 
Krupnick, et al. 2024b. “Spatiotemporally Detailed Quantification of Air 
Quality Benefits of Emissions—Part II: Sensitivity to Study Parameters 
and Assumptions.” ACS EST Air 1 (10). doi:10.1021/acsestair.4c00128.
Henze, D.K., A. Hakami, and J.H. Seinfeld. 2007. “Development of 
the Adjoint of GEOS-Chem.” Atmospheric Chemistry and Physics 7: 
2413–33. doi:10.5194/acp-7-2413-2007.
Houyoux, M., and J. Vukovich. 1999. “Updates to the Sparse Matrix Op -
erator Kernel Emissions (SMOKE) Modeling System and Integration 
with Models-3.” Paper presented at The Emission Inventory: Regional 
Strategies for the Future, Air and Waste Management Association, 
October 26–28, Raleigh, NC.
Khreis, H., C. Kelly, J. Tate, R. Parslow, K. Lucas, and M. Nieuwenhui -
jsen. 2017. “Exposure to Traffic-Related Air Pollution and Risk of Devel -
opment of Childhood Asthma: A Systematic Review and Meta-analy -
sis.” Environment International 100: 1–31. doi:10.1016/j.envint.2016.11.012.
Lazer, L., and L. Freehafer. 2024. “A Dataset of Electric School Bus 
Adoption in the United States.” World Resources Institute, August 19. 
https://www.wri.org/research/technicalnote-dataset-electric-school-
bus-adoption-united-states.
Lazer, L., L. Freehafer, and J. Wang. 2022. “Dataset of U.S. School Bus 
Fleets.” World Resources Institute, December. https://datasets.wri.
org/dataset/school_bus_fleets.
Levinson, M., and A. Achury. 2024. “Clearinghouse: Electric School 
Bus Funding and Financing Opportunities.” World Resources 
Institute, Electric School Bus Initiative. https://electricschoolbusini -
tiative.org/clearinghouse-electric-school-bus-funding-and-financ -
ing-opportunities.
Levinson, M., P. Burgoyne-Allen, A. Huntington, and N. Hutchinson. 
2023. “Recommended Total Cost of Ownership Parameters for Elec -
tric School Buses: Summary of Methods and Data.” World Resources 
Institute, Electric School Bus Initiative. https://www.wri.org/research/
recommended-total-cost-ownership-parameters-electric-school-
buses-methods-data.
Pope, C.A., M. Cropper, J. Coggins, and A. Cohen. 2015. “Health 
Benefits of Air Pollution Abatement Policy: Role of the Shape of the 
Concentration-Response Function.” Journal of Air and Waste Manage -
ment Association 65: 516–22. doi:10.1080/10962247.2014.993004.
Sandu, A., D.N. Daescu, G.R. Carmichael, and T. Chai. 2005. “Adjoint 
Sensitivity Analysis of Regional Air Quality Models.” Journal of Compu -
tational Physics 204: 222–52. doi:10.1016/j.jcp.2004.10.011.
School Bus Fleet Magazine . 2024. “By the Numbers: School Transpor-
tation, 2022–2023.” https://schoolbusfleet.mydigitalpublication.com/
publication/?m=65919&i=810506&p=14&ver=html5.

38  |  
  
Skamarock, W.C., J.B. Klemp, J. Dudhia, D.O. Gill, D.M. Barker, 
M.G. Duda, et al. 2008. “A Description of the Advanced Research 
WRF Version 3.” National Center for Atmospheric Research, June. 
doi:10.5065/D68S4MVH.
Turner, M.C., M. Jerrett, C.A. Pope, D. Krewski, S.M. Gapstur, W.R. Diver, 
et al. 2016. “Long-Term Ozone Exposure and Mortality in a Large 
Prospective Study.” American Journal of Respiratory and Critical Care 
Medicine 193: 1134–42. doi:10.1164/rccm.201508-1633OC.
US EPA (Environmental Protection Agency). 2004. “40 CFR Part 
86 Subpart A: General Provisions for Heavy-Duty Engines and 
Heavy-Duty Vehicles.” https://www.ecfr.gov/current/title-40/
part-86/subpart-A.
US EPA. 2015. “Learn about Impacts of Diesel Exhaust and the Diesel 
Emissions Reduction Act (DERA).” Overviews and Factsheets. https://
www.epa.gov/dera/learn-about-impacts-diesel-exhaust-and-diesel-
emissions-reduction-act-dera.
US EPA. 2019. “Preparation of Emissions Inventories for the Version 
7.2, 2016 North American Emissions Modeling Platform.”
US EPA. 2022. “Supplementary Material for the Regulatory Impact 
Analysis for the Supplemental Proposed Rulemaking, ‘Standards of 
Performance for New, Reconstructed, and Modified Sources and 
Emissions Guidelines for Existing Sources: Oil and Natural Gas Sector 
Climate Review.’”
US EPA. 2023. “2020 National Emissions Inventory Technical Support 
Document: Introduction.”
US EPA. 2025a. “Air Pollution: Current and Future Challenges.” https://
www.epa.gov/clean-air-act-overview/air-pollution-current-and-fu -
turhttps://www.epa.gov/clean-air-act-overview/air-pollution-current-
and-future-challengese-challenges.
US EPA. 2025b. “Photochemical Air Quality Modeling.” https://www.
epa.gov/scram/photochemical-air-quality-modeling. 
Valencia, A., M. Serre, and S. Arunachalam. 2023. “A Hyperlocal Hy -
brid Data Fusion Near-Road PM 2.5 and NO2 Annual Risk and Environ -
mental Justice Assessment across the United States.” PLoS ONE  18: 
e0286406. doi:10.1371/journal.pone.0286406.
Weichenthal, S., L. Pinault, T. Christidis, R.T. Burnett, J.R. Brook, and Y. 
Chu, et al. 2022. “How Low Can You Go? Air Pollution Affects Mortal -
ity at Very Low Levels.” Science Advances  8: eabo3381. doi:10.1126/
sciadv.abo3381.
WHO (World Health Organization). 2012. “IARC: Diesel Engine Exhaust 
Carcinogenic.” https://www.iarc.who.int/news-events/iarc-diesel-
engine-exhaust-carcinogenic/.
WHO. 2024. “Ambient (Outdoor) Air Pollution.” https://www.
who.int/news-room/fact-sheets/detail/ambient-(outdoor)-air-
quality-and-health.
Wolfe, P., K. Davidson, C. Fulcher, N. Fann, M. Zawacki, and K.R. Baker. 
2019. “Monetized Health Benefits Attributable to Mobile Source Emis -
sion Reductions across the United States in 2025.” Science of the 
Total Environment 650: 2490–98. doi:10.1016/j.scitotenv.2018.09.273.
WRI (World Resources Institute). 2025. “How Electric School Buses 
Benefit Kids’ Health, School Budgets, Jobs and More.” https://elec -
tricschoolbusinitiative.org/how-electric-school-buses-benefit-kids-
health-school-budgets-jobs-and-more.
Zhang, Y., J.J. West, R. Mathur, J. Xing, C. Hogrefe, S.J. Roselle, et 
al. 2018. “Long-Term Trends in the Ambient PM2.5 - and O3-Related 
Mortality Burdens in the United States under Emission Reductions 
from 1990 to 2010.” Atmospheric Chemistry and Physics 18: 15003–16. 
doi:10.5194/acp-18-15003-2018.
Zhao, S., M.G. Russell, A. Hakami, S.L. Capps, M.D. Turner, D.K. Henze, 
et al. 2020. “A Multiphase CMAQ Version 5.0 Adjoint.” Geoscientific 
Model Development 13: 2925–44. doi:10.5194/gmd-13-2925-2020.
Zhao, S., P. Vasilakos, A. Alhusban, Y.B. Oztaner, A. Krupnick, H. 
Chang, et al. 2024. “Spatiotemporally Detailed Quantification of Air 
Quality Benefits of Emissions Reductions–Part I: Benefit-per-Ton 
Estimates for Canada and the U.S.” ACS EST Air 1: 1215–26. doi:10.1021/
acsestair.4c00127.

TECHNICAL NOTE  |  August 2025  |  39
Modeling the societal health and climate benefits associated with transitioning the US school bus fleet from diesel to electric
Acknowledgments
We are pleased to acknowledge our institutional strategic partners 
that provide core funding to WRI: the Netherlands Ministry of 
Foreign Affairs, Royal Danish Ministry of Foreign Affairs, and Swedish 
International Development Cooperation Agency. 
This research was conducted in collaboration between WRI’s Electric 
School Bus Initiative and Carleton University, with generous support 
from the Bezos Earth Fund, which funds WRI’s Electric School Bus 
Initiative. The authors extend their gratitude to the many individuals 
who contributed their time and expertise to review and provide 
feedback on this technical note. In particular, we thank the following 
reviewers for their invaluable insights: Simone Athayde, Sarav 
Arunachalam, Beatriz Cardenas, Ken Davidson, Amanda Gian, Sue 
Gander, Arya Harsono, Heather Holmes, Rohit Jaikumar, Joel Jaeger, 
Adriana Kocornik-Mina, Tirthankar Mandal, Anne Maassen, Fernando 
Menendez, Mehri Mohebbi, Meredith Pedde, Elizabeth Wesley, 
and Sophie Young.
About the authors
Amir Hakami is a Professor in Environmental Engineering at 
Carleton University.
Burak Oztaner  is a Postdoctoral Fellow at Carleton University.
Marjan Soltanzadeh  is a PhD graduate from Carleton University.
Amy Todd is the Monitoring, Evaluation, Learning, and Research 
Lead for WRI’s Electric School Bus Initiative.
Brian Zepka is a Research Manager for WRI’s Electric School Bus 
Initiative.

Copyright 2025 World Resources Institute. This work is licensed under the Creative Commons Attribution 4.0 International License.  
To view a copy of the license, visit http://creativecommons.org/licenses/by/4.0/
  
10 G Street, NE  |  Washington, DC 20002  |  WRI.ORG
About WRI 
World Resources Institute works to improve people’s lives, protect 
and restore nature, and stabilize the climate. As an independent 
research organization, we leverage our data, expertise, and global 
reach to influence policy and catalyze change across systems like 
food, land and water; energy; and cities. Our 2,000+ staff work on the 
ground in more than a dozen focus countries and with partners in 
over 50 nations.
About WRI’s Electric School Bus Initiative 
In collaboration with partners and communities, the Electric School 
Bus Initiative aims to build unstoppable momentum toward an 
equitable transition of the US school bus fleet to electric, bringing 
health, climate, and economic benefits to children and families 
across the country and normalizing electric mobility for an entire 
generation. The Electric School Bus Initiative was founded in 
partnership with the Bezos Earth Fund in late 2020. We work with 
key stakeholders at all levels and across areas, including school 
districts, private fleet operators, electric utilities, public and private 
lenders, manufacturers, policymakers, equity and environmental 
advocacy groups, program administrators, community members, and 
communitybased organizations.
