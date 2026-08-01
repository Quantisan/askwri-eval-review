---
doc_id: 2022_impactar-tool-valuing-air-quality-health-impacts_4741
source_pdf: kp-docs/askwri-kps/2022_impactar-tool-valuing-air-quality-health-impacts_4741.pdf
extraction_method: cache-plaintext
char_count: 147930
title: "ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil (2022)"
authors: Betti, Luana; Garcia, Marina Caregnato; Siqueira, Eduardo; Evers, Henrique
date_published: 2/23/2022
article_type: Technical Note
sub_tag: Transport decarbonization
wri_primary_office: WRI Brasil
wri_programs: Cities
language: English
url: "https://www.wri.org/research/impactar-tool-air-quality-health-impacts-urban-bus-fleet-brazil-2022"
doi: "https://doi.org/10.46830/writn.21.00044"
summary: In Brazil, where the transport sector is one of the biggest contributors to air pollution in cities, replacing conventional buses with electric vehicles can save lives and positively impact the economy. This is what ImpactAr tool, a technical note and a valuation model, demonstrates.
---

# ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil (2022)

TECHNICAL NOTE   | November 2021  |  1
TECHNICAL NOTE
IMPACTAR TOOL: VALUING AIR QUALITY HEALTH IMPACTS  
OF URBAN BUS FLEET CHANGES IN BRAZIL
LUANA PRISCILA BETTI, MARINA CAREGNATO GARCIA, EDUARDO SIQUEIRA, AND HENRIQUE EVERS 
CONTENTS
Summary ....................................................................................................................1
1. Introduction ........................................................................................................2
2. Methodology .....................................................................................................3
3. ImpactAr Tool Structure ........................................................................14
4. Data Sources ..................................................................................................17
5. Limitations and Uncertainties ..........................................................18
6. Pilot Test Analysis .....................................................................................20
7. Final Remarks and Conclusion .......................................................28
Appendix A ...........................................................................................................29
Appendix B...........................................................................................................40
Abbreviations.......................................................................................................41
Endnotes .................................................................................................................41
References ...........................................................................................................43
WRI Technical Notes document the research or 
analytical methodology underpinning research 
publications, interactive applications, and other tools.
This is the third version of this publication. It updates the technical parameters of the environmental stage of the methodology. 
The second version adjusted an error in the values of the PM fixed conversion measures (PM FCM) for Belo Horizonte (MG) 
and Rio de Janeiro (RJ).
SUMMARY
Air pollution is recognized as one of the greatest 
challenges of our time. Besides being an important 
contributor to climate change, several epidemiological 
studies indicate the association between air pollution 
and mortality (fatal diseases) and morbidity (nonfatal 
diseases). These impacts have implicit (unobservable) 
costs, such as hospitalization expenditures and 
productivity losses. The assessment and valuation of air 
pollution impacts is essential to make observable the 
implicit costs (or savings) of certain choices of economic 
agents (population, companies, and governments) that 
can increase or reduce air pollution levels. In Brazil, 
the transport sector accounts for the largest share of 
outdoor air pollution emissions, impacting the number 
of hospitalizations, deaths, and public and private 
expenditures, among other impacts. 
Within the Brazilian transport sector, public urban 
bus fleets, dominated by diesel-powered technologies, 
contribute significantly to high levels of air pollution, 
especially particulate matter (PM). Transitioning urban 
bus fleets from less efficient in terms of pollutant emissions 
to cleaner technologies, however, can present higher 
investment costs because the up-front purchase price of 
more developed technologies is often higher compared to 
less efficient ones. This can discourage the improvement 
of a city’s bus fleet. In order to promote a more accurate 
benefit-cost analysis of fleet renewal projects, it is crucial 
to measure the direct and indirect costs of premature 
mortalities, morbidities, workforce loss, and the associated 
monetary loss due to fatal and nonfatal diseases associated 
with variations on air pollution levels.
Suggested Citation: Betti, L. B., M. C. Garcia, E. Siqueira, 
and H. Evers. 2020. “ImpactAr Tool: Valuing Air Quality 
Health Impacts of Urban Bus Fleet Changes in Brazil.” 
Technical Note. Porto Alegre, Brazil: WRI Brasil. Available 
online at: https://doi.org/10.46830/writn.21.00044

2  |  
This technical note presents the Valuation Tool for 
Health Impacts of Air Pollution (ImpactAr), a tool 
that aims to assess the impacts of urban air pollution 
on health and economy. It evaluates these health 
impacts and the associated monetary costs of changes 
in emissions levels linked to modifications in urban 
bus fleets in four Brazilian cities: São Paulo, Rio de 
Janeiro, Belo Horizonte, and Niterói. Focused on public 
managers—but also available for politicians, private 
sector operators, academics and researchers—it works 
as a support tool for the decision-making process, 
demonstrating the potential costs and returns of air 
pollution externality connected with investments in 
different transport technologies. This tool is the first step 
in measuring the implicit costs and benefits of changes 
in urban transport fleets in terms of different effects 
on PM10 and PM2.5 emissions and concentration levels 
and their impacts on fatal and nonfatal diseases. The 
ImpactAr tool was developed with the financial support 
of the Children’s Investment Fund Foundation (CIFF). 
1. INTRODUCTION
Atmospheric air pollution is the contamination of the 
external or internal environment by any chemical, 
physical, or biological agent that modifies the natural 
characteristics of the atmosphere (air quality). Outdoor 
air pollution originates from natural and anthropogenic 
sources.1 The most prominent polluting anthropogenic 
sources include fuel combustion for transport, power 
generation, heating, and industry (WHO 2018).
Among the main pollutants, particulate matter (PM) is 
commonly used as an indicator for air pollution because 
it affects more people than any other pollutant (WHO 
2018). PM is a mixture of solid and liquid particles 
of organic and inorganic substances suspended in 
the air, including sulfate, nitrates, ammonia, sodium 
chloride, black carbon, mineral dust, and water. PM 
vary in size, composition, and origin. Whereas particles 
with a diameter of 10 micrometers or less (≤ PM10) 
can penetrate and lodge deep inside the lungs, the 
even more health-damaging particles are those with a 
diameter of 2.5 micrometers or less (≤ PM2.5) (WHO 
2018). According to epidemiologists, air pollution 
represents a risk factor; this means it is not the direct 
cause of individual deaths (Roy and Braathen 2017), 
diseases, or injuries, but it significantly increases the 
likelihood of an individual dying or developing disease 
(WHO 2016).
In most of Brazil’s urban areas, which compose about 84 
percent of the national population (IBGE 2010), vehicles 
are the main source of pollutants emitted into the 
atmosphere (Miranda et al. 2012). Within the country’s 
transport sector, the major contributor to PM emissions 
are heavy vehicles moved by diesel—mainly trucks and 
buses (MMA 2014).2
According to national studies,3 in terms of health 
impacts, outdoor air pollution in the main metropolitan 
regions and state capitals of the country is linked to 
about 20,500 annual deaths caused by cardiovascular 
and respiratory diseases (Miraglia and Gouveia 2014) 
and is responsible for 5.2 percent of hospital admissions 
for respiratory causes among children and 8.3 percent 
among elderly, totaling 4,581 respiratory admissions 
per year (Marcilio and Gouveia 2007). Other studies 
strongly suggest an association between the country’s 
air pollution and fatal and nonfatal cases of cancer, 
restrictions on fetal development, and changes in the 
human male-to-female ratio, among others (Hettfleisch 
et al. 2017; Miraglia et al. 2013; Yanagi, Assunção, 
and Barrozo 2012). From a financial point of view, air 
pollution in the country leads to about 130,000 cases 
of work absences and a cost of US$6,472,686 in terms 
of hospitalization expenditures and absences at work 
every year (Rodrigues-Silva et al. 2012). All of these 
impacts heavily affect the population’s quality of life and 
pressure the local public budgets.
Given this scenario, urban bus fleets in most Brazilian 
cities continue to be outdated and less efficient in terms 
of PM emissions when compared to cleaner technologies 
available throughout the world. Low-emissions buses 
account for only 0.003 percent of the national urban bus 
fleet (NTU 2020). This can be partially explained by the 
fact that fleet transitions to cleaner technologies, such 
as electric buses, may present high investment costs 
because the initial purchase price of these technologies 
is often higher than less efficient ones (Sclar et al. 2019). 
Additionally, the policies, regulations, and incentives 
to improve a fleet are determined at the federal 
government level, but the health costs of air pollution 
particularly impact municipal budgets, reducing the 
incentives to a faster fleet upgrading.

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  3
How can managers overcome these obstacles and 
provide municipalities with cleaner bus technologies 
in terms of air pollution emissions, resulting in less 
fatal and nonfatal diseases, lower associated costs, and 
increased quality of life for all Brazilians? The first step 
is to include the measurement of emissions variations 
and their implicit health costs into investment 
evaluation—which are not often considered—allowing 
managers to perform a more accurate benefit-cost 
analysis of projects aimed at achieving cleaner urban 
bus fleets.
With this goal, WRI Brasil has developed the Valuation 
Tool for Health Impacts of Air Pollution (ImpactAr). 
The interactive spreadsheet tool using Microsoft 
Excel measures the health impacts and the associated 
monetary costs of changes in emissions levels linked 
to modifications in urban bus fleet technologies in the 
cities of São Paulo, Rio de Janeiro, Belo Horizonte, and 
Niterói. The measurement and analysis of the impacts 
of such pollutants are made for a 1-year period (short-
run analysis) and a 30-year period (long-run analysis), 
aiming to inform users of the short-run and the long-
run cumulative effects of air pollution. 
The ImpactAr tool covers the impacts of PM2.5, one of 
the most harmful pollutants to human health, as well as 
PM10. The tool also provides, among other financial and 
economic results, the measurement of hospitalization 
costs in both the public and private health care systems. 
These monetary outcomes, interpreted as savings or 
costs, are compared to municipal macroeconomic 
variables, such as the annual municipal gross domestic 
product (GDPm) and annual public health budget, 
providing a reference of cost magnitude for users.4
Ultimately, ImpactAr serves as a support tool for 
decision-makers, indicating the implicit costs 
and returns of public investments related to air 
pollution in four Brazilian cities. It provides relevant 
information about air pollution health impacts and 
their consequences for the economy, which are useful 
information to complement the project’s benefit-cost 
analysis and other complementary studies. 
This technical note is divided into seven sections: (i) an 
introduction; (ii) the methodology, with clarifications 
on the model embedded in the ImpactAr tool; (iii) the 
ImpactAr tool structure; (iv) the data sources used to 
build the tool; (v) the limitations and uncertainties; (vi) 
the pilot test analysis; and (vii) concluding remarks. 
2. METHODOLOGY
In this section, we explain the key concepts used in this 
technical note and describe the framework for analyzing 
the ImpactAr tool, the methodological choices, and the 
data applied in the development of the tool.5
2.1 Key Concepts
Bottom-up approach: In the case of air pollution 
assessment, a methodology that measures air pollution 
emissions and atmospheric concentrations by analyzing 
the specific sources of emissions. It is the opposite 
of the top-down approach, according to which the 
concentration levels of pollutants are first analyzed, and 
the sources of the emissions are estimated later on.
Concentration-response coefficients (C-Rs):  
Coefficients that indicate the magnitude of response of 
morbidity and mortality cases related to a variation in 
air pollution concentration levels (Marcilio and Gouveia 
2007). They are derived from epidemiological studies. 
Economic costs:  Economic costs measure changes 
in people’s welfare as a consequence of air pollution. 
They are not related to tangible services and products 
(such as the cost of medical appointments), but they 
are based on individual perceptions and valuations, 
which cannot be considered financial measures. Such 
costs represent the assessments on the amount of value 
that, for individuals, is lost due to air pollution. This 
can be the cost of suffering caused by diseases linked to 
air pollution. 
Emissions and concentration levels of 
pollutants: Emissions are a measure of mass (tons) 
of pollutants emitted by one or more sources. In the 
ImpactAr tool, they represent the mass of PM2.5 and 
PM10 produced by the urban bus fleets in each city. 
Concentration levels express the volume of pollutants 
in a specific area (microgram per cubic meter, µg/m3). 
It can differ according to temperature, humidity, wind, 
and other factors. Consequently, although cities can 
present the same emissions levels, concentration levels 
can vary greatly according to local conditions.

4  | 
Emissions factor: According to the U.S. 
Environmental Protection Agency (EPA), “An emissions 
factors is a representative value that attempt to relate 
the quantity of a pollutant released to the atmosphere 
with an activity associated with the release of that 
pollutant” (industry, motorized vehicle, etc.) (EPA, n.d.). 
In the case of the ImpactAr tool, it consists of a mass 
of pollutant emitted by buses when consuming fuel to 
travel for a determined distance (measuring unit: grams 
of pollutant per liter of diesel, g/L). 
Epidemiology: The fi  eld of study that deals with the 
causes and distribution of diseases and other related 
phenomena. Examples of epidemiological studies 
include issues such as the relation between smoking 
and lung cancer, obesity and stroke, and the causes of 
psychiatric disorders, among others.
Externality:  This term refers to the impacts coming 
from the activities of one entity that change the welfare 
of another entity (Rosen and Gayer 2008), without 
the latter’s consent. Externalities can be positive (e.g., 
vaccinations) or negative (e.g., passive smoking). For 
this technical note, air pollution and all of its impacts 
on health and economy are considered a negative 
externality coming from the transport sector—more 
specifi  cally, coming from the public urban bus fl  eet. 
Financial costs:  The state-of-the-art literature on 
the monetization of air pollution impacts presents two 
typologies of costs: fi  nancial costs and economic costs. 
Financial costs are related to monetized, market-based 
costs. In relation to air pollution, these can be the costs 
of hospitalization and medical expenses caused by 
diseases attributable to pollutants.
Health endpoint: The type of fatal and nonfatal 
diseases caused by air pollution. In the case of the 
ImpactAr tool, health endpoints include fatal and 
nonfatal cardiovascular and respiratory diseases 
according to Chapters I and J, respectively, of the 10th 
revision of the International Statistical Classifi  cation of 
Diseases and Related Health Problems (ICD-10).
PM fixed conversion measure (FCM): This is 
the estimated factor used to convert a variation of PM 
emissions levels into variations of PM concentration 
levels for each city. FCMs were obtained through two 
numerical experiments with the Brazilian Developments 
on the Regional Atmospheric Modeling System 
(BRAMS 5.2),6 which identifi  ed the existence of a 
fi  xed pattern in the conversion between emissions 
variations and concentrations variations for each 
city (for further discussion, please see Section 2.3, 
Methodology Description; and Section 5, Limitations 
and Uncertainties, of this technical note). 
Value of statistical life (VSL): The monetization 
of the welfare/economic cost caused by mortality. It 
represents the aggregate of the individual willingness 
to pay (WTP) for a marginal reduction in the risk of 
dying from air pollution. It should be noted that this is a 
judgment or an evaluation of the measure of one’s life; it 
measures the amount that individuals would be willing 
to pay, considering not only impacts on their income but 
also on their well-being, to marginally reduce their risk 
of dying due to air pollution. 
2.2 Framework for Analysis 
The impact of air pollution on health and economy is 
not direct. Before aff  ecting a population’s health and 
creating related costs, pollutants go through a chain of 
environmental, epidemiological, fi  nancial, and economic 
stages (Figure 1). A motorized vehicle, through its fuel 
combustion, brakes, tires, and road surface wear emits 
pollutants, among them PM. PM emissions react with 
atmospheric conditions (meteorological conditions, 
physical obstacles, etc.), resulting in a concentration 
level of PM in a determined region. A set of the 
Figure 1  |  The Pollutant Chain of Impacts
Source: WRI authors.

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  5
population is exposed to this concentration of pollutants 
in the determined region and so, by increasing the 
likelihood of individuals suff  ering illnesses and deaths, 
cases of morbidity and mortality linked to PM are 
verifi  ed among the population. Finally, the premature 
deaths and illnesses result in monetary costs.
Measuring the health and related fi  nancial and economic 
impacts of air pollution requires the reproduction of 
this chain process. The ImpactAr tool systematizes the 
stages presented in Figure 1 based on the impact pathway 
approach (IPA) formulated by the ExternE Project.7
This approach consists of a bottom-up approach that 
proposes the measurement of environmental benefi  ts and 
costs caused by changes in air pollution levels through a 
pathway from source emissions to monetary expressions 
of benefi  ts and costs (ExternE, n.d.). The calculation 
involves two sets of components:
▪ Data points: Data estimates that inform the 
results of the impacts in each stage of the IPA. 
For example, total annual variation in PM10
concentration levels and total annual number of 
avoided deaths due to cardiovascular diseases. They 
are represented by the boxes in Figure 2. 
▪ Linking functions: Algebraic functions that connect 
and convert the diff  erent stages of the IPA, allowing 
the assessment between distinctive types of data. They 
are represented by the yellow arrows in Figure 2.
In the ImpactAr tool, the set of data points and linking 
functions that are encompassed in the pathway are 
organized in a sequence of three stages, which starts 
with the technical solution for the urban bus fl  eet’s 
renewal (for instance, the number of buses replaced for 
each technology): 
1. Environmental Stage: This provides the annual 
variations in emissions and concentration levels of 
PM2.5 and PM10 as a result of the diff  erences between 
the current fl  eet (scenario 0) and the projected fl  eet 
(scenario 1) features. 
2. Epidemiological Stage:  By assessing the number 
of people and general epidemiological cases of 
cardiovascular and respiratory diseases in one 
city, this stage isolates the impacts of the annual 
concentration variations of PM2.5 and PM10 levels on 
the number of hospitalizations and deaths caused by 
cardiovascular and respiratory diseases. 
3. Financial and Economic Stage: This 
stage monetizes nonfatal and fatal respiratory 
and cardiovascular diseases isolated in the 
epidemiological stage through the cost of illness 
(COI) methodology, which measures the fi  nancial 
costs of nonfatal cases, and through the VSL, which 
measures the economic costs of fatal cases. 
Figure 2 illustrates the steps of the methodology 
embedded in the tool. We can list fi  ve data points—
represented by the boxes in Figure 2—and four linking 
functions applied to each data point to obtain new 
outcome units—represented by the yellow arrows.
Figure 2  |  Methodology Steps Used in the ImpactAr Tool
Source: WRI authors.

6  |  
2.3 Methodology Description
The methodologies and data applied to build the 
ImpactAr tool were based on the most recent 
Brazilian empirical literature on the measurement of 
air pollution impacts on health and economy in the 
country. Before the development of the tool, a three-
stage literature review was carried out by the World 
Resources Institute (WRI) staff, starting from research 
on the main academic search platforms, followed by 
research of publications from leading researchers and 
institutions, and closing with a workshop with the main 
Brazilian specialists and institutions for validation 
of the literature review. This process resulted in 67 
studies from which the impacts to be analyzed and 
methodologies applied were chosen.8
The ImpactAr tool comprises environmental, 
epidemiological, and financial methodologies and 
data presented in the Brazilian empirical literature, 
arranged according to the IPA chain process. Among 
others, it includes the analysis of deaths and illnesses 
caused by cardiovascular and respiratory diseases in 
the Epidemiological Stage, and it uses the COI and VSL 
methodologies in the Financial and Economic Stage. 
The ImpactAr tool focuses on the pollutants PM10 and 
PM2.5 for the following reasons:
 ▪ PM imposes the most serious threat to human 
health compared to other pollutants (WHO 2018).
 ▪ Brazilian epidemiological literature, using a 
consolidated measurement methodology, identifies 
PM as responsible for a high number of health and 
economic impacts.
 ▪ PM10 and PM2.5 present different sources of 
emissions from the road transport activities9 
(Hooftman et al. 2016) and distinct health 
incidence on the development of respiratory and 
cardiovascular cases10 (Abe and Miraglia 2016; Silva 
et al. 2017).
 ▪ The transport sector is a major contributor of 
outdoor air pollution and the largest emitter of PM 
in Brazil (MMA 2014). 
This version of the tool only fits four Brazilian cities: 
São Paulo, Rio de Janeiro, Belo Horizonte, and Niterói. 
The first three cities were chosen because they are the 
most important cities with which WRI Brasil has plans 
for implementing electric buses in their fleets. Also, they 
represent three of the largest vehicle fleets in the country, 
representing 8 percent, 3 percent, and 2 percent of the 
national share, respectively.11 Although Niterói has a 
relatively less expressive fleet in relation to the other 
cities—about 0.3 percent of the national fleet—the city 
was added due to its previous partnership with WRI 
Brasil in the field of electric bus impact measurement.
Unfortunately, as we expect to include more cities in 
the tool in the future, it will not be possible to include 
all Brazilian municipalities due to the size of the input 
data and the time required to do so. In this sense, we 
recommend potential users and people interested in 
assessing air pollution impacts due to bus fleet change 
projects in their cities use this technical note and the tool 
itself as a blueprint or a guide to build their own tool. 
We strongly encourage people to contact the authors in 
such cases, so we can help with any possible doubts and 
questions that may not be covered by this technical note. 
A more detailed look at data points, linking functions 
(both presented in Figure 2), and the methodology 
selected to measure air pollution changes and impacts is 
provided below. 
2.3.1 Project
Data point 1, technical solution: A public project 
aiming to renew a city’s current public bus fleet. Data 
required is entered twice: first for the baseline or current 
fleet (scenario 0), and then for the projected fleet 
(scenario 1). The ImpactAr tool requires the following 
input data: (i) the number of buses per technology,12 (ii) 
the bus technology, and (iii) the average annual travel 
distance per bus in kilometers (km). Optional input data 
include emissions factors (g/L) and average fuel efficiency 
per technology in liters or kilowatt-hours per 100 km 
(L or kWh/100 km). If the user does not possess such 
information, the model will provide data by default.13
2.3.2 Environmental Stage
Linking function 1, from technical solution to 
variation on annual emissions levels: Both scenario 
0 fleet and scenario 1 fleet annual emissions levels (tons 
per year) are measured according to the formula
Annual PM emissions = N x d x CC x ex (1)
where N is the number of buses per technology, d is the 
average annual traveled distance per bus (km), CC is the 
annual fuel efficiency per technology (L or kWh/100 km) 
and ex is the emissions factor of PM per technology (g/L).
This formula is applied to each technology reported. 
It only provides annual PM emissions, without 
distinctions between the PM diameters, due to the 
methodology used to measure the PM FCMs (for further

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  7
information, please see Linking function 2 below). 
In this sense, a ratio, obtained from the Handbook 
Emission Factors for Road Transport, model version 
3.3, is adopted to assess PM emissions of less than 10µg 
(PM10) and PM emissions smaller than 2.5 µg (PM2.5).14 
The ratio applied is PM2.5/PM10 = 0.7. This ratio was 
equally applied for all four cities as, during numerical 
experiments to determine concentration levels, we used 
a regional round covering the four cities.15
It is worth noting that PM2.5 and PM10 emissions and 
concentration variations, as well as impacts, cannot 
be summed because PM10 particulates include PM2.5 
particulates. In this sense, all the results are showed 
separately, once for PM10 and once for PM2.5. 
Data point 2, variation on annual emissions 
levels: This is the difference between annual PM2.5 
and PM10 emissions of the current/scenario 0 fleet and 
annual PM2.5 and PM10 emissions of the projected/
scenario 1 fleet. This represents the total annual 
emissions variations that the technical solution would 
bring, if implemented. These can be represented as
ΔE PM2.5 = annual PM2.5 emissions of scenario 1 – annual PM2.5 
emissions of scenario 0 (2)
ΔE PM10  = annual PM10 emissions of scenario 1 – annual PM10 
emissions of scenario 0 (3)
where ΔEPM2.5 represents the total annual variation on 
PM2.5 emissions levels due to the technical solution, and 
ΔEPM10 represents the total annual variation on PM10 
emissions levels due to the technical solution. 
Linking function 2, from annual variations 
on emissions levels to annual variations on 
concentration levels: Concentration levels can vary 
greatly according to temperature, humidity, and wind, 
among other factors. Consequently, concentration levels 
vary significantly in different geographic regions. To 
obtain the annual variations in concentration levels 
for each city, the WRI team carried out numerical 
experiments with the BRAMS 5.2, using the Coupled 
Chemistry Aerosol-Tracer Transport model (CCATT), 
analyzing the dispersion of the pollutants from 
the emissions data available from public transport 
scenarios. This modeling system (CCATT-BRAMS) 
performs predictions of weather and atmospheric 
composition in real-time and simultaneously 
(meteorology integrated with dispersion/chemistry). 
The CCAT-BRAMS model was applied to evaluate 
the variations in the annual concentration levels. The 
simulations were configured to evaluate the regional 
dispersion of pollutants PM2.5 and PM10, associated only 
with the activity of the bus fleet. For this, meteorological 
initial and boundary conditions were used from the global 
model combining data from the Center for Weather 
Forecast and Climatic Studies (Centro de Previsão do 
Tempo e Estudos Climáticos, CPTEC), National Institute 
for Space Research (Instituto Nacional de Pesquisas 
Espaciais, INPE), and Global Forecast System.
Two alternative simulations were used to obtain 
such results. The first, developed in 2018 and named 
Linking function 2.1, was broader and encompassed 
four Brazilian cities: São Paulo, Rio de Janeiro, Belo 
Horizonte, and Niterói. Later, in 2020, a second version 
was developed to obtain more robust results for two 
cities in which WRI Brasil has continuously deepened 
its work on electromobility: Belo Horizonte and São 
Paulo. Due to project scope limitations and constraints 
(including time and budget), it was possible to update 
the Linking function only for these two cities.
Thus, this tool uses the PM FCMs of Niterói and Rio de 
Janeiro, obtained by Linking function 2.1, and FCMs 
of Belo Horizonte and São Paulo, by Linking function 
2.2 (a PM FCM for each city). The technical parameters 
used in the two simulations are described below.
LINKING FUNCTION 2.1: 
This broader simulation was performed including in 
the same spatial resolution the cities of Rio de Janeiro 
and Niterói. For that, a control experiment (baseline) 
and three scenarios modified by different technology 
configurations were simulated for the urban bus fleets 
among cities.
The emissions scenarios were simulated in grid points 
with 25 km of spatial resolution and 80 meters (m) of 
thickness in the first vertical layer over the urban area 
of the cities, using a methodology proposed by Alonso 
et al. (2010). The weather conditions that calibrated the 
model were obtained from observed data in June 2018 
in the Southeast region of Brazil.
From such simulations, a linear pattern in the conversion 
between the emissions variations and concentrations 
was identified, providing a conversion factor for each 
city.16 The PM FCM for Rio de Janeiro is 0.00195 and 
for Niterói, 0.0001407. Current fleet (scenario 0) annual 
variations on emissions of PM10 and PM2.5 and projected 
fleet (scenario 1) annual variations on emissions of PM10 
and PM2.5 are multiplied by this factor. Hence,
ΔE PM2.5 × FCM = ΔC PM2.5 (4)
ΔE PM10 × FCM = ΔC PM10 (5)

8  |  
where ΔEPM2.5 represents the total annual variation on 
PM2.5 emissions levels due to the technical solution, ΔEPM10 
represents the total annual variation on PM10 emissions 
levels due to the technical solution, FCM is the PM FCM 
for each city, ΔCPM2.5 represents the total annual variation 
on PM2.5 concentration levels due to the technical solution, 
and ∆CPM10 represents the total annual variation on PM10 
concentration levels due to the technical solution. 
LINKING FUNCTION 2.2:
This approach was developed to obtain more accurate 
results and reduce the aggregate errors of the 
environmental stage inherent to Linking function 2.1. 
The same basis was maintained (Alonso et al. 2010) 
incorporating a few adjustments to the model’s technical 
parameters, described below.
This more refined simulation was performed 
considering three urban transport emissions scenarios 
for the cities of São Paulo and Belo Horizonte. For 
weather conditions, the model simulated conditions 
of August 2019 with observed data from the city level 
and no longer from the regional level. The month of 
August is an ideal weather period, as the meteorological 
conditions present an adequate behavior for the purpose 
of this simulation, with average annual temperatures 
and humidity levels.
Regarding the technical parameters of the simulation, 
three grids of the spatial resolution were considered: 25, 
5, and 2 kilometers (km). The same 80 meters (m) of 
thickness was maintained in the first vertical layer. 
The spatial distribution of emissions was performed 
using information data in a General Transit Feed 
Specification (GTFS) format, available by the transport 
agencies of São Paulo and Belo Horizonte. GTFS is a 
data specification that divides information into a static 
component that contains schedule, fare, and geographic 
transit information; and a real-time component that 
contains arrival predictions, vehicle positions, and 
service advisories (Fortin et al. 2016). GTFS was used to 
identify in which regions of the city there are more bus 
stops, and hence, are more impacted by PM emissions 
due to public transport—assuming the number of bus 
stops has a direct linear relationship with bus arrival and 
departure frequencies. The data were compiled using the 
Geographic Information System (GIS) software ArcGIS. 
After that, the data format was converted and exported 
at a resolution of 1 km. With that, it was possible to 
extract relative weights of bus stops in each pixel and the 
spatial coordinates in text format and distribute the PM 
emissions. Despite being a more realistic distribution, 
not all cities in the Global South already have these GTFS 
data in accessible formats.
As in Linking function 2.1, it maintained the same 
linear patterns verified (Equations 4 and 5), but new 
conversion factors were obtained. The PM FCM is 
0,0011 for São Paulo and 0,0015 for Belo Horizonte. 
COMPARISON BETWEEN SIMULATIONS
The simulations performed using the CCAT- BRAMS 
model show some methodological differences. Table 
1 compares the main differences between Linking 
functions 2.1 and 2.2.
PARAMETERS LINKING FUNCTION 2.1 LINKING FUNCTION 2.2
Period June 2018 August 2019
Spatial resolution Regional-level: 25 km covering the 
entire southeastern region of Brazil
City-level: Different grids with 2km  
of spatial resolution
Atmospheric boundary condition T343L42 by CPTEC/INPE Global Forecasting System
Validation with observed meteorological data Not performed Performed for temperature  
and wind intensity
Distribution of PM emissions Distributed homogeneously in the 
urban area of the city
Distributed by weights associated with 
the number of bus stops at each pixel
Cities evaluated Rio de Janeiro, São Paulo, Belo 
Horizonte, and Niterói São Paulo and Belo Horizonte
Table 1  |   Technical parameters of the simulations
Source: WRI authors.

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  9
The simulation that generated the PM FCMs for Linking 
function 2.1 includes some limitations that were later 
improved. The simulation was conducted considering a 
widely spatial resolution at the regional level of 25 km, 
using a methodology proposed by Alonso et al. (2010), 
native in PREP-CHEM-SRC. During the performance of 
this first simulation, although the model had adequate 
statistical adjustments, no quantitative validation was 
performed to assess the sensitivity of the model using 
observed meteorological data, due to limitations such as 
budget and time.
For the new simulation (Linking function 2.2), the main 
limitations of the first simulation have been improved. 
A higher resolution was used: 5 and 2 km. This new 
approach led to the development of a more accurate 
methodology for the spatial distribution of emissions 
given that PM concentrations are measured by their 
density. Regarding the simulation period, observed 
meteorological data from the two cities were evaluated 
separately. With that, it was possible to identify a period 
that was suitable for the simulations considering the 
meteorological characteristics of each of the cities, 
unlike Linking function 2.1, in which the period was 
selected to suit the climatic characteristics of the entire 
Southeast region of Brazil. The data predicted by the 
model present adequate forecasts and satisfactory 
statistical adjustments with the observed data. 
Spatially, it is assumed that the PM concentration in 
Linking function 2.2 shows improvements and better 
reliability, since emissions were distributed in PREP-
CHEM, using GTFS data with greater precision. This 
assumption is also based on the hypothesis that regions 
near bus stops—and with more bus stops deployed—
have a higher concentration of particulate matter from 
fleets of urban buses. 
Regarding atmospheric boundary conditions, in Linking 
function 2.1, for a 25 km domain, a downscaling was 
chosen with the outputs of the Global model provided 
by CPTEC/INPE, with approximately 60 km of spatial 
resolution. For Linking function 2.2, in which it was 
decided to work with city level (2 km), Global Forecast 
Model was chosen, with 25 km of spatial resolution, 
to provide the atmospheric boundary conditions. 
This ensures an acceptable nesting ratio between the 
boundary conditions and the domains. Table 2 shows 
the PM FCM obtained in the two simulations.
The variation observed in the results is mainly due 
to two factors: the distribution of PM emissions and 
the period evaluated. The distribution methodology 
significantly changes the results of the model and, 
consequently, the PM FCMs. The weather conditions 
(related to the period) can increase or decrease the 
variation. A period with drier weather conditions (such 
as the range of June up to August) results in higher 
concentrations, and a wetter period results in lower 
concentrations due to the dispersion of pollutants.
Data point 2, annual variation on concentration 
levels: This is the difference between annual 
concentrations of PM2.5 and PM10 for the current/
baseline fleet and the projected/scenario 1 fleet. This 
represents the total annual variation in concentration 
levels that the technical solution would bring, if 
implemented (represented as ΔCPM2.5 and ΔCPM10 in 
Equations 4 and 5). 
2.3.3 Epidemiological Stage
Linking function 3, from annual variations in 
concentration levels to annual variations in the 
number of fatal and nonfatal diseases: Linking 
function 3 consists of the conversion of the total annual 
variation in concentration levels of PM10 and PM2.5 into 
annual variations in the number of hospitalizations 
(nonfatal cases) and deaths (fatal cases) attributable to 
air pollution.17
Given the specificities of the state-of-the-art Brazilian 
epidemiological studies that measure air pollution 
health impacts, 18 exponential functions were applied 
to measure health impacts in the ImpactAr tool. 
Such types of functions are widely used to measure 
air pollution impacts because they are able to account 
PARAMETERS LINKING FUNCTION 2.1 LINKING FUNCTION 2.2 VARIATION
São Paulo 0.0014 0.0011 -23%
Belo Horizonte 0.0008 0.0015 +92%
Table 2  |   Particulate matter fixed conversion measures obtained
Source: WRI authors.

10  |  
for nonlinear relations among variations in pollutant 
concentrations and their health impacts, seasonality 
trends, and lags between the increase in pollution 
and the occurrence of the health event, among others 
(Conceição et al. 2001). The following epidemiological 
equation is used (André, Vormittag, and Saldiva 2017; 
Rothman and Greenland 1998)
AE = [EXP(ß*ΔCPMx)  -1] × TE (6)
where AE is the annual attributed events of fatal 
and nonfatal diseases due to the annual variation in 
concentration levels of PM10 and PM2.5, β represents 
the C-R, ΔCPMx represents the total annual variation in 
PM2.5 or PM10 concentration levels due to the technical 
solution implemented, and TE is the total annual events 
of fatal and nonfatal diseases from all causes, covered by 
the public and private health systems.19 In this work, we 
consider respiratory and cardiovascular diseases.
To capture the relation between the mean increase 
(or decrease) in pollutant concentration and the 
corresponding mean increase (or decrease) in the 
number of health events, epidemiologists make 
use of C-Rs (β). In the Brazilian literature on air 
pollution impact assessment, several ecological time-
series studies provide such coefficients for different 
populations, pollutants, health impacts, and age ranges. 
The C-Rs (β) retrieved to build the ImpactAr tool come 
from the Brazilian empirical literature, specifically 
from seven articles, which are listed in Table 3. All 
the attributable events measured in the tool follow 
exactly the criteria of age range, health endpoint, and 
pollutant of each C-R, defined by the authors of the 
epidemiological studies. 
ß AGE RANGE AREA HEALTH 
ENDPOINT POLLUTANT C-R SOURCE
ß1 Children (<5) Mortality Respiratory 
diseases PM10 0.0011821980 Marcilio and 
Gouveia 2007
ß2 Children (<5) Morbidity Respiratory 
diseases PM10 0.0010138430 Gouveia et. al. 
2017
ß3 Elderly (≥60) Mortality Respiratory 
diseases PM10 0.0013212330 Costa et al. 2017
ß4 Elderly (≥60) Mortality Cardiovascular 
diseases PM10 0.000010000 Costa et al. 2017
ß5 Elderly (≥65) Morbidity Respiratory 
diseases PM10 0.001960024 Marcilio and 
Gouveia 2007
ß6 Elderly (>39) Morbidity Cardiovascular 
diseases PM10 0.000999983 Gouveia et al. 2017
ß7 All ages Mortality Respiratory 
diseases PM2.5 0.0010148330 Fajersztajn et al. 
2017
ß8 Children (<12) Morbidity Respiratory 
diseases PM2.5 0.008925820 Nascimento et al. 
2016
ß9 Elderly (≥45) Mortality Cardiovascular 
diseases PM2.5 0.0010544210 Rodrigues et al. 
2017
ß10 Elderly (>64) Morbidity Respiratory 
diseases PM2.5 0.0042101180 Ignotti et al. 2010
ß11 Elderly (≥45) Morbidity Cardiovascular 
diseases PM2.5 0.002254400 Rodrigues et al. 
2017
Table 3  |   Concentration-Response Coefficient (ß) Details and Sources
Source: WRI authors.

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  11
Box 1  |  The Calculus of Total Events (TE): The Number of Fatal and Nonfatal Diseases from All Causes
Exposure refers to a “pollutant concentration at a particular place 
and time, and the presence of a person at that place and time.”   a 
It can vary according to (i) the magnitude of the concentration 
level, (ii) the duration of the exposure to the pollutant, and (iii) 
the frequency of exposure to the pollutant. b This entails that, 
within a city, exposure levels, and therefore health impacts, differ 
greatly according to the person’s mobility trends and living area. 
The ImpactAr tool does not measure different levels of exposure 
among the population in each city due to the lack of data 
regarding georeferenced information on PM concentration levels 
in different areas of the analyzed cities and specific features 
of the population’s mobility in those areas. Instead, our model 
uses the total number of fatal and nonfatal cardiovascular and 
respiratory diseases from all causes in each city as a baseline. 
To obtain such numbers for a 30-year analysis, a projection of 
population, morbidity rate, and mortality rate, considering the 
concentration-response coefficient criteria of age range and 
health endpoints, was measured. 
The population projections were calculated on the basis of 
population forecast estimates from local government studies 
combined with polynomial interpolation in the years for which 
data were missing. Mortality and morbidity rates were projected 
from data retrieved from the Department of Information 
Technology of the National Public Health System (Departamento 
de Informática do Sistema Único de Saúde, DATASUS). For fatal 
disease forecasts, we used cross-sectional DATASUS data on the 
number of deaths, and for nonfatal diseases we used cross-
sectional DATASUS data on hospitalizations—both from 2000 to 
2017. To maintain the reasonableness of the behavior of fatal and 
nonfatal cases until 2050 (30-year analysis), we set the 2050 
value as the best result in these health indicators (the minimum 
value reached) in the data provided by DATASUS (2000–17). Our 
main assumption is that, over the years, the overall health of 
the population will improve, reaching the best result already 
reached—and therefore the lowest number—of fatal and nonfatal 
cardiovascular and respiratory diseases. 
The projections were made through direct linear extrapolation, 
according to the following model, c
ln(mx,t) = ax + bx t + Ex,t
where mx,t is the mortality/morbidity rate of interest, for age x , 
in year t; ax means the mortality/morbidity constant for age; b x 
denotes the age-specific multiplied by time t ; Ex,t is the residual 
error. It is fundamentally a log-linear model, with the mortality/
morbidity rate as the dependent variable and the year, as well as 
a constant, as an explanatory variable. 
In possession of the population forecasts, we applied the 
projected mortality and morbidity rates of respiratory and 
cardiovascular diseases from all causes to obtain the absolute 
number of occurrences. The number of deaths provided by 
DATASUS covered both occurrences in the public health system 
as well as in the private health system. For hospitalizations, 
however, data provided only covered hospitalizations in the public 
health system. Therefore, in order to find hospitalizations in the 
private health system, we applied the method of André et al. 
(2012) as follows,  
Nps=Npublic  (            ) -1   
where Nps is the number of hospital admissions in the private 
system, Npublic  is the number of hospital admissions in the public 
system, and PI  is the proportion of the population with access to 
private health insurance.
1
(1-PI)
Note: There are several methods for projecting mortality/morbidity. Direct linear extrapolation is not meant to be accurate but rather to point to trends. This method 
is traditionally used in this kind of study (Stoeldraijer et al. 2013). Methods that include additional information or an extra dimension to the data (e.g., cohort) “will 
automatically lead to a more subjective model. . . . Models which capture age, period, and cohort effects in mortality will provide a better model fit than age-period 
models, given that a cohort effect exists in the mortality data. . . . However, there is no guarantee that models with a better fit will produce better forecasts” (Stoeldraijer 
et al. 2013, 344–45).
Sources: a. National Research Council 1988, 208; b. National Research Council 1988; c. Booth and Tickle 2008; Stoeldraijer et al. 2013.
At first, it may seem counterintuitive to assume that 
impacts on specific age ranges are representative of the 
population’s health impacts as a whole. Nevertheless, 
due to the nonlinear nature of the relation between 
pollutant variations and health impact variations, 
children and the elderly are the segments of the 
population that experience much higher-than-average 
personal health impacts caused by air pollution. By 
assessing the impacts of this risk group, we are able to 
provide a more sensitive basis for the detection of any 
increase in disease (National Research Council 1988).
Data point 4, annual variations on the number 
of fatal and nonfatal diseases: This represents 
the health impacts linked to the technical solution 
chosen. It provides the changes in the number of 
hospitalizations and deaths due to respiratory and 
cardiovascular diseases as a consequence of the annual 
variation in PM 2.5 and PM10 concentrations. Annual 
variations in the number of fatal and nonfatal cases are 
provided for 1 year and 30 years.

12  |  
2.3.4 Financial and Economic Stage
Linking function 4, from annual variations 
on the number of fatal and nonfatal diseases 
to monetary valuation:  The monetization of the 
changes in the numbers of fatal and nonfatal diseases 
applied in the tool was divided between morbidity 
costs and mortality costs. For the former, we have 
opted to monetize the cost of nonfatal diseases 
attributable to air pollution through the financial 
approach, as the Brazilian literature used the well-
grounded COI methodology. 20 For the latter, we chose 
to use a measure of economic cost that is not often 
verified in the Brazilian literature—namely, the VSL. 
Yet however controversial the VSL may be, it aims 
to measure nonmarket costs related to suffering and 
loss of well-being, broadening the spectrum of costs 
covered by the ImpactAr tool.
a. Morbidity costs: According to the COI 
methodology, the financial impacts of hospitalizations 
consist of the sum of two types of costs:
Direct cost of disease: This represents the total 
costs of hospitalizations. It is measured using the 
average cost of hospitalizations in 2018 provided by 
the Department of Information Technology of the 
National Public Health System (Departamento de 
Informática do Sistema Único de Saúde, DATASUS) 
for each age range and health endpoint of the 
C-Rs and the annual attributed events of nonfatal 
diseases due to the variation on concentration 
levels. As DATASUS only provides the average cost 
of hospitalizations in the public health system, we 
assumed that the average cost of hospitalizations in 
the private system is three times higher in relation 
to public ones, as proposed by André et al. (2012). 
The total direct cost according to each age range and 
health endpoint is given by
TDC = AC × AD (7)
where TDC is the total annual direct cost of 
nonfatal diseases, AC is the average cost of each 
hospitalization for each age and health endpoint, 
and AD is the annual attributed nonfatal diseases 
due to the variation on concentration levels.
Indirect cost of disease: This represents the cost of 
work absences due to hospitalizations. It is measured 
for each age range and health endpoint of the C-Rs, 
and it uses the average stay of hospital admissions in 
2018 provided by DATASUS (we assumed that the 
average stay of hospitalizations in the private system 
is the same as in the public system); individual daily 
per capita earnings of all sources in 2015 (2018R$) 
per city, which were measured by dividing by 30 
the average monthly earning of all sources in 2015 
provided by Brazilian Institute of Statistics and 
Geography (Instituto Brasileiro de Geografia e 
Estatística, IBGE); and the number of the annual 
attributable events of nonfatal diseases due to the 
annual variation on concentration levels. This can be 
summarized by the formula
TIC = AS × DI × AD (8)
where TIC represents the total annual indirect 
cost of disease, AS is the average stay of hospital 
admissions for each age range and health endpoint 
of C-Rs, DI is the individual daily income per 
capita of all sources per city, and AD is the annual 
attributed nonfatal diseases due to the variation on 
concentration levels.
Besides the indirect cost of morbidity, the ImpactAr 
tool also provides the number of workdays lost due 
to hospitalizations. Although we analyze the impacts 
in non-working-age ranges, we assume that someone 
active, both in the formal and informal job market, 
will be absent from work to take care of the ill, as 
proposed by Ortiz-Durán and Rojas-Roa (2013). 
Finally, the total financial cost of morbidity impacts, 
or the COI, calculated by the tool is given by the 
equation
COI = TDC + TIC (9)
where TDC is the total annual direct cost of nonfatal 
diseases and TIC represents the total annual indirect 
cost of disease.

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  13
b. Mortality costs: Mortality costs were measured 
by multiplying the number of deaths by the VSL for 
Brazil in 2018, as presented in Equation 10. They are 
measured for each age range and health endpoint of 
the C-Rs,
MC = ND × VSL (10)
where MC is the total cost of mortality, ND is the 
annual number of deaths, and VSL is the value of 
statistical life for Brazil.
Brazil does not present an extensive literature21 
that measures the VSL for air pollution through 
revealed preference or state preference methods.22 
We have opted to adopt the unit value transfer 
method to obtain the VSL value, according to which 
we transfer data from previous studies of stated 
preference or revealed preference from one context 
to another, with adjustment for specific variables. 
The methodology applied has been widely used by 
the Organization for Economic Co-operation and 
Development (OECD) (OECD 2012, 2014; Roy 
2016; Roy and Braathen 2017; WHO/Europe and 
OECD 2015). Specifically, for the ImpactAr tool, we 
adopted the methodology proposed by an OECD 
study (Roy and Braathen 2017) that targeted the 
countries of Brazil, Russia, Indonesia, India, China, 
and South Africa (BRIICS). The value transferred 
was the 2005 VSL for OECD countries, US$3 million 
(2005$) (OECD 2012). According to the formula we 
applied, we adjusted the value for the difference in 
per capita income, income per capita growth from 
2005 and 2018, and inflation from 2005 and 2018 
(Roy and Braathen 2017):
VSLBRASIL,2018 = VSLOECD,2005 x (                 )
b x (1+%ΔP+%ΔY) b (11)
where VSLBRASIL,2018 is the value of statistical life 
for Brazil in 2018; VSLOECD,2005 is the base value for 
OECD countries in 2005; YBRASIL,2005 is the GDP per 
capita in terms of purchasing power parity at 2018 
prices for Brazil in 2005; YOECD,2005 is the per capita 
GDP in terms of purchasing power parity at 2018 
prices for OECD countries in 2005; b is the income 
elasticity of VSL (considered to be 1, as proposed by 
Roy and Braathen [2017, 17]); %ΔP represents the 
price inflation in Brazil between 2005 and 2018, 
as estimated by the consumer price rate; and %ΔY 
is the real income growth between 2005 and 2018 
for the country. All the economic indicators were 
retrieved from the OECD online database.
Data point 5, monetary valuation: This 
represents the monetization of the variations 
in health impacts found in the Epidemiological 
Stage. For costs related to changes in morbidity 
impacts—namely, variations in the number of 
hospitalizations—we used the COI methodology, 
which can be interpreted as the financial savings/
costs of health treatment and income avoided/
generated due to the total decrease/increase on 
PM2.5 and PM10 annual concentration levels. For 
costs associated with mortality, in their turn, the 
VSL was used. In simple terms, the VSL is an 
estimate of how much people are willing to pay to 
reduce their risk of death, taking into account issues 
such as suffering and discomfort. Therefore, this 
cost represents more than the financial impacts of 
mortality, aiming to evaluate the impact on welfare 
losses due to a fatality.
Monetary values are measured in Brazilian reals 
(R$) at 2018 prices and a discount rate of 6.75 
percent per year was used for the 30-year analysis 
(February 2018, Brazilian basic interest rate, called 
the Special System for Settlement and Custody 
Sistema Especial de Liquidação e de Custódia 
(SELIC) rate). The concept behind the use of the 
discount rate for projections is intended to deal with 
future inflation, making future costs comparable to 
current 2018 Brazilian prices (2018R$).
YBRASIL,2005
YOECD,2005

14  |  
Source: ImpactAr tool.
3. IMPACTAR TOOL STRUCTURE
The presented methodology was used to build an 
interactive spreadsheet tool using Microsoft Excel 2013. 
The tool presents a cover, with a brief model description 
and menu, and a user guide, with details on each 
spreadsheet’s functions (Figures 3 and 4).
Figure 3  |  Interface of the ImpactAr Tool Cover

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  15
Figure 4  |  Interface of the ImpactAr Tool User Guide
Source: ImpactAr tool.

16  |  
After these two first sections, the tool presents another 
seven spreadsheets. The first corresponds to an optional 
input section, the second to a required input section, 
and the following five spreadsheets consist of sections 
for reports and results. Each one contains specific types 
of data; Table 4 provides a summary.
As specified, the sixth and seventh spreadsheets 
(Main Results and Long-Run Analysis) are not part 
of the stages presented in Figure 2, but they provide a 
summary of main results and economic comparisons. 
The interfaces of all the other spreadsheets mentioned 
in Table 2 are presented in Appendix A.
Besides the 9 spreadsheets presented above (Cover, User 
Guide, Optional Inputs, Project, Environmental Stage, 
Epidemiological Stage, Financial and Economic Stage, Main 
Results, and Long-Run Analysis), the tool has 10 additional 
support spreadsheets that cannot be visualized or modified 
by the user. These sections contain all default data used as 
well as the calculations and databases of health, financial, 
and economic impacts measured by the tool. 
ORDERING SHEET 
REFERENCE NAME MAIN CONTENTS
Sheet 1 Optional Inputs
This is an optional input sheet that enables users to change the PM emissions factor and average fuel 
efficiency per technology of buses. The values available in the model by default are provided in the only 
table of the spreadsheet, in the white cells. Note that users should only fill the optional value in the green 
cells of the table if they have the data required. Otherwise, the user should keep the green cells with N/A 
value, as the model will provide data by default.
Sheet 2 Project
The user enters the data for the fleet’s renewal project, including data on the city’s current bus fleet or 
any baseline fleet (scenario 0) and data on the city’s projected bus fleet (scenario 1). If the user does not 
possess fleet data to enter, she/he can input any value of annual emissions or concentration levels of 
PM2.5 or PM10 in the “Environmental Input Data” subsection and the tool will measure the epidemiological, 
financial, and economic impacts in the following spreadsheets. In this case, the values entered will 
represent annual variations on air pollution levels linked to the transport sector. This means that the tool 
will assume that air pollution levels for scenario 1 represent the values inputted by the user, and the air 
pollution levels for scenario 0 will be equal to zero.
Sheet 3 Environmental 
Stage
It provides the annual emissions and concentration levels of PM 2.5 and PM10 both for the current and the 
projected fleet. If the user provides data directly through the in the Environmental Input Data subsection 
of the “Project Stage,” he or she can go directly to the next spreadsheet, “Epidemiological Stage.”
Sheet 4 Epidemiological 
Stage
It provides the numbers of epidemiological cases (hospitalizations and deaths) attributable to the difference 
between the annual concentration levels of PM2.5 and PM10 linked to the current fleet (scenario 0) and the 
annual concentration levels of PM2.5 and PM10 linked to the projected fleet (scenario 1). It also offers the 
number of work absences due to hospitalizations. Values are provided for 1 year (short-run analysis) and 30 
years (long-run analysis). If the user provides data directly through the Environmental Input Data subsection 
of the Project Stage, the number of fatal and nonfatal diseases provided by ImpactAr represents an 
estimation of health endpoints due to the annual variation on emissions and concentration levels inputted.
Sheet 5 Financial and 
Economic Stage
Morbidity costs (nonfatal diseases) and mortality costs (fatal diseases) are provided as a consequence of 
the changes in the annual concentration levels of PM 2.5 and PM10 caused by the fleet’s renewal. Values are 
provided for 1 year (short-run analysis) and 30 years (long-run analysis). If the user provides data directly 
through the Environmental Input Data subsection of the Project Stage, the financial and economic costs 
of fatal and nonfatal diseases represent an estimation of the costs associated with the epidemiological 
cases due to the annual variation in emissions and concentration levels inputted.
Sheet 6 Main Results
It provides the main results—environmental, epidemiological, and financial-economic—that the changes 
in PM10 and PM2.5 annual concentration levels originated by the fleet’s renewal or by the direct air quality 
inputs of the user (in the Environmental Input Data subsection of the Project Stage) would produce. It also 
offers a comparative analysis between economic and financial results and economic indicators of the 
municipality, such as the municipal GDP , municipal annual health expenditure, municipal annual hospital 
expenditure, and average cost of hospitalizations in the municipality. Values are provided for 1 year (short-
run analysis) and 30 years (long-run analysis).
Sheet 7 Long-Run 
Analysis
It provides graphics with the evolution of morbidity and mortality cases and their respective costs over 
the period of 30 years, with data numbers provided every 5 years.
Table 4  |  ImpactAr: Tool Contents and Structure
Notes: GDP = gross domestic product; PM = particulate matter.
Source: WRI authors.

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  17
4. DATA SOURCES
All external data sources used to build the ImpactAr 
tool are summarized in Table 5, with specifications 
on their locations.
DATA SOURCES SPREADSHEET
Emissions factor per 
technology (g/L)
Ministry of the Environment (Ministério do Meio Ambiente) a
São Paulo Transportation (São Paulo Transporte) b DEFAULT_DATA_ENVIRONMENTAL
Average fuel efficiency per 
technology (L or kWh/100 km)
Operation experience—reported to the World Resources Institute—
from a large Brazilian city. The name of the city will not be provided as 
to avoid relevant information disclosure.
For average electric consumption, we added the average of the 
operation data of nine Padron electric buses of a pilot carried out in 
Santiago, Chile.
DEFAULT_DATA_ENVIRONMENTAL
Broad National Consumer 
Price Index (Índice Nacional de 
Preços ao Consumidor Amplo, 
IPCA)
Brazilian Institute of Statistics and Geography (Instituto Brasileiro de 
Geografia e Estatística; IBGE) c DEFAULT_DATA_ENVIRONMENTAL
Particulate matter fixed 
conversion measures (FCM) 
for emissions concentration
Obtained through simulations in the Coupled Chemistry Aerosol-
Tracer Transport model to the Brazilian Developments on the Regional 
Atmospheric Modeling System (CCATT-BRAMS) model.
DEFAULT_DATA_ENVIRONMENTAL
Municipal gross domestic 
product—2015 (2018R$) IBGEd DEFAULT_DATA_ENVIRONMENTAL
Annual municipal health 
expenditure in 2018 (R$)
São Paulo: 2018 data from the Municipal City Hall (Prefeitura do 
Município de São Paulo) e
Rio de Janeiro: 2018 data from the Municipal City Hall (Prefeitura da 
Cidade do Rio de Janeiro) f
Belo Horizonte: 2018 data from Municipal City Hall (Prefeitura 
Municipal de Belo Horizonte) g
Niterói: 2018 data from the Municipal City Hall (Prefeitura Municipal de 
Niterói)
DEFAULT_DATA_ENVIRONMENTAL
Average cost of 
hospitalizations from all 
causes in 2018 (R$)
Department of Information Technology of the National Public Health 
System (Departamento de Informática do Sistema Único de Saúde; 
DATASUS)
DEFAULT_DATA_ENVIRONMENTAL
Average hospital expenditure 
in 2018 from all causes per 
city (R$)
DATASUS DEFAULT_DATA_ENVIRONMENTAL
Resident population per city 
and age ranges (table) 
DATASUS (2011–12: IBGE population estimates submitted to the Federal 
Audit Court (Tribunal de Contas da União, TCU), stratified by age and 
sex by MS/SGEP/DATASUS)h
DEFAULT_DATA_EPIDEMIOLOGICAL
Private health insurance 
coverage per city in August 
2018 (%) (table)
National Agency of Supplementary Health (Agência Nacional de 
Saúde Suplementar, ANS) DEFAULT_DATA_EPIDEMIOLOGICAL
Average stay of 
hospitalizations in 2018 (table) DATASUS DEFAULT_DATA_FIN_ AND_ECO
Value of statistical life for 
Brazil in 2018 (R$)
Value obtained by transferring the value of statistical life to OECD 
countries in 2005, as proposed by Roy and Braathen (2017) DEFAULT_DATA_ FIN_ AND_ECO
Discount rate Brazilian basic interest rate in February 2018 (SELIC rate) per the 
Brazilian Central Bank (Banco Central do Brasil) i DEFAULT_DATA_ FIN_ AND_ECO
Table 5  |  Data Source Specifications

18  |  
DATA SOURCES SPREADSHEET
Average individual monthly 
income of all sources per city 
in 2015 (2018R$)
IBGE Automatic Recovery System (Sistema IBGE de Recuperação 
Automática, SIDRA)j DEFAULT_DATA_ FIN_ AND_ECO
Average cost of PUBLIC 
hospitalization in 2018 (R$) DATASUS DEFAULT_DATA_ FIN_ AND_ECO
Average cost of PRIVATE 
hospitalization in 2018 (R$)
The average cost of hospitalizations in the private system was 
considered to be three times higher in relation to public ones, as 
proposed by André et. al (2012)
DEFAULT_DATA_ FIN_ AND_ECO
Population forecasts  
for São Paulo
Foundation for the State System of Statistical Data Analysis (Fundação 
Sistema Estadual de Análise de Dados Estatísticos, SEADE) k DEFAULT_DATA_POPPROJ
Population forecasts  
for Belo Horizonte João Pinheiro Foundation (Fundação João Pinheiro) population studies DEFAULT_DATA_POPPROJ
Population forecasts  
for Rio de Janeiro Pereira Passos Institute (Instituto Pereira Passos) DEFAULT_DATA_POPPROJ
Population forecasts  
for Niterói
Municipal Secretary of Urbanism and Mobility (Secretário Municipal de 
Urbanismo e Mobilidade) l DEFAULT_DATA_POPPROJ
Notes: g/L = grams of pollutant per liter of diesel; L or kWh/100 km = liters or kilowatt-hours per 100 kilometers; SELIC = Sistema Especial de Liquidação 
e de Custódia.
Sources: a. MMA 2011; b. SPTrans 2012; c. IBGE, n.d.b; d. IBGE 2017; e. Prefeitura do Município de São Paulo 2018a; f. Prefeitura da Cidade do Rio de Janeiro 
2018; g. Prefeitura Municipal de Belo Horizonte 2018; h. IBGE, n.d.a; i. BCB 2018; j. IBGE 2015; k. Fundação SEADE 2017; l. SMU 2015.
5. LIMITATIONS AND UNCERTAINTIES
Although the ImpactAr tool offers a robust model 
to measure air pollution impacts, limitations and 
uncertainties are inexorable, but identifying them 
will help users better interpret the results. We have 
segregated the main limitations according to the stages 
presented in Section 2, Methodology, additionally 
including an overall limitations analysis. 
Environmental Stage limitations: The main issue 
that may raise controversy in this stage is related to 
the methodology applied to convert PM emissions 
into PM concentration levels. This conversion is 
based on a fixed conversion factor for each city, which 
may mislead the user to believe that the different 
variables that influence concentration levels were 
not considered. The PM FCMs, however, incorporate 
aspects inherent to the atmospheric simulation for 
the period and region analyzed in the BRAMS 5.2 
modeling system, such as wind influence, atmospheric 
boundary layer behavior, soil-atmosphere interaction, 
and mesoscale and synoptic scale phenomena. In this 
study, due to scope limitations, the period considered 
for atmospheric modeling is one month of the year 
for each Linking function (June and August), which is 
representative in meteorological conditions.
For the first simulation (Linking function 2.1), the 
emissions scenarios for each city were interpolated 
on a gridded domain (25 km) over an urban area of 
the cities, using a methodology proposed by Alonso 
et al. (2010), native in PREP-CHEM-SRC. The 
emissions preprocessing tool (Freitas et al. 2011) is 
a comprehensive tool for preparing emissions fields 
of trace gases and aerosols for use in atmospheric 
chemistry transport models. For the second simulation 
(Linking function 2.2), to mitigate the limitations of 
the domain and spatial distribution, 2 km of spatial 
resolution and the GTFS data were combined for each 
city. For both simulations, the 80 m of thickness in the 
first vertical layer was chosen due to the computational 
resource associated with the timetable for the delivery of 
the tool.
Another limitation is the use of two different 
simulations (Linking functions 2.1 and 2.2) to obtain the 
FCMs of the four cities. The different methodological 
paths taken do not allow direct comparisons among the 
four cities.

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  19
Although FCMs carry limitations—such as 
meteorological boundary conditions of one month, 
coarse-grid resolution, and some model limitations 
like atmospheric parameterization—they are a 
useful option for ImpactAr tool users because this 
methodology does not require expertise in atmospheric 
modeling. Furthermore, the FCMs are sensitive only 
to bus fleet emissions scenarios, and the inclusion 
of additional meteorological boundary conditions 
like Representative Concentration Pathway (RCP) 
scenarios,23 for example, would bring more uncertainty 
to the simulations of PM concentration. 
Epidemiological Stage limitations : All dose-
response coefficients retrieved measure the short-term 
effect of PM on health (usually on the same day of the 
exposure, up to seven days past). The epidemiological 
evidence indicates that the long-term effects of air 
pollution also negatively affect people’s health (Beelen et 
al. 2014; Pope 2007). The Brazilian literature, however, 
does not present an extensive list of such studies. In 
order to consider a long-term analysis, the ImpactAr 
tool sums the impacts of air pollution measured by 
short-run dose-response coefficients for the 30-year 
analysis. Furthermore, we have retrieved the coefficients 
from specific studies. In the future, we intend to carry 
out averaging estimates by metanalytic approaches 
to obtain the dose-response coefficients from a larger 
number of studies.
Among the epidemiological field, we analyze only a 
small yet significant portion of consequences caused 
by air pollution. Studies already suggest the impacts of 
air pollution on birth gender (Lichtenfels et al. 2007) 
and fetal development (Hettfleisch et al. 2017). Another 
limitation is related to the fact that the ImpactAr tool 
does not consider different sets of exposure among 
the population in each city. Air pollution does not 
affect the population evenly, and there is evidence that 
suggests that low-income groups tend to experience 
higher exposures to pollutants due to less favorable 
environmental living conditions compared to more 
affluent population groups or areas (Fairburn et al. 
2019; Martins et al. 2004; Rivas, Kumar, and Hagen-
Zanger 2017) and, therefore, higher impacts on health. 
Financial and Economic Stage limitations: As 
previously mentioned, we have obtained the VSL for 
Brazil, which measures mortality costs, through the 
unit transfer methodology. Unfortunately, the unit 
transfer methodology only acknowledges income and 
inflation differences between OECD countries (original 
value transferred) and Brazil. Other differences, which 
significantly affect the VSL value, include life expectancy 
and income elasticity, among others.24 
Furthermore, the tool acknowledges future inflation for 
the long-run analysis (30 years) through a discount rate, 
but income growth is not included in the analysis, as we 
believed the different methodologies used to calculate it 
could raise strong controversy. This has the potential to 
underestimate the financial and economic results, as the 
income is kept at 2018 levels. 
Overall limitations:  Our tool only fits four Brazilian 
cities: São Paulo, Rio de Janeiro, Belo Horizonte, and 
Niterói. Due to the methodology used and the size of the 
input data required to add more cities, such as new PM 
FCMs and the number of deaths and hospitalizations 
recommended. Also, the adoption of ImpactAr for 
non-Brazilian cities is particularly discouraged because 
almost all epidemiological parameters embedded in it 
were retrieved from Brazilian studies.25
At last, we acknowledge the need for caution when 
using ImpactAr tool results. It is important to note that 
we use a chain process of calculus to measure PM10 
and PM2.5 impacts, meaning that we can assert that the 
final results carry the aggregate errors of each stage’s 
calculation—namely, environmental, epidemiological, 
and financial and economic. Unfortunately, we are 
unable to evaluate whether these uncertainties would 
potentially increase or diminish the results provided by 
the tool. Hence, the quantitative outputs provided by 
the ImpactAr tool must be interpreted as estimates that 
indicate the existence of the impacts, costs, and their 
respective magnitude in the analyzed cities; they are 
not an expression of the exact values of epidemiological 
cases and costs related to the fleet’s renewal in terms of 
PM2.5 and PM10 variations.
Bearing the previous limitations and uncertainties 
in mind, however, the ImpactAr tool comprises a 
robust model for measuring air pollution impacts, 
developed using the state-of-the-art methodologies 
and most credible databases currently applied among 
the academic field. The consequences of changes in air 
pollution levels on health and economy are continuously 
addressed by empirical studies, and, in this sense, the 
ImpactAr tool provides an important insight to address 
such matters in the context of these Brazilian cities.

20  |  
6. PILOT TEST ANALYSIS
The aim of this section is to provide the readers with a 
better understanding of the tool’s outputs by performing 
a simulation of an urban bus fleet renewal project for 
the city of São Paulo. This city is the largest city in Brazil 
in terms of population and economic activity. With 12.2 
million inhabitants, São Paulo accounts for 5.8 percent 
of Brazil’s population, and it is responsible for 11 percent 
of the national GDP.26 It also has the biggest vehicle fleet 
of the country, reaching 8 percent of total national fleet27  
with around 9 million vehicles (Detran SP 2019). In this 
scenario, air pollution is an evident externality in the 
city, and transport is its main cause. 
In January 2018, the municipality implemented a 
long-term target to reduce the greenhouse gas (GHG) 
emissions and air pollutants generated by its collective 
transport fleet in 20 years.28 The law settled specific 
targets of reduction for different air pollutants and 
GHGs, for instance, PM, carbon dioxide (CO2), and 
nitrogen oxides (NOx). Particularly for PM, the law 
stipulates a minimum decrease of 95 percent in 20 
years from the validity of the law (2038) compared to 
the 2016 levels (Prefeitura do Município de São Paulo 
2018b, subsection IV of article 50).
The simulation in the ImpactAr tool is based on the 
described target for PM reductions in São Paulo. As 
the target is based on the percentage of emissions 
reduction, rather than on a profile change in the fleet 
technology, WRI Brasil determined ad hoc the number 
of buses of each technology that achieves the 95 percent 
of reduction in PM emissions, maintaining the total 
number of buses. The constructed scenario focused 
on a large increase in the electric fleet, a modest rise 
in the trolleybus fleet,29 and a large reduction in the 
most pollutant type of technology, Euro III and Euro 
V. The current fleet (scenario 0) and the projected fleet 
(scenario 1) data inputs for the test are described in 
Tables 6 and 7.
It is worth noting that the simulation used the values 
of the emissions factor and the average fuel efficiency 
provided in the tool by default.
CURRENT FLEET
TYPE OF 
BUS TECHNOLOGY NUMBER 
OF BUSES
ANNUAL 
TRAVELED 
DISTANCE (KM)
Bus 1 Euro III 7,739 63,102
Bus 2 Euro V 6,756 63,102
Bus 3 Trolleybus 201 63,102
Bus 4 Euro VI 0 0
Bus 5 Euro VI 0 0
PROJECTED FLEET
TYPE OF 
BUS TECHNOLOGY NUMBER 
OF BUSES
ANNUAL 
TRAVELED 
DISTANCE (KM)
Bus 1 Euro III 330 63,102
Bus 2 Euro V 566 63,102
Bus 3 Trolleybus 250 63,102
Bus 4 Electric 13,550 63,102
Bus 5 Euro VI 0 0
Table 6  |  Scenario 0 (Current Fleet) Inputs: Location in 
the ImpactAr tool—Project Stage Spreadsheet
Table 7  |  Scenario 1 (Projected Fleet) Inputs: Location in 
the ImpactAr Tool—Project Stage Spreadsheet
Source: WRI authors. Source: WRI authors.

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  21
6.1 Test Results
Considering only the impacts of PM2.5, the pollutant 
with the largest impacts on human health, the 
implementation of the 95 percent of PM reduction target 
in São Paulo has the potential to avoid approximately 
95 cases of illness and 4 deaths in the first year, 
reaching around 3,171 cases of illnesses and 141 deaths 
in 30 years.30 In terms of working days lost due to 
hospitalizations, in one year, about 647 work absences 
would be avoided, whereas in 30 years this number 
rises to 22,601 work absences avoided. These impacts 
collectively represent a potential savings of about R$5 
million regarding the morbidity costs and R$300 million 
regarding the mortality costs, both in the long run.
These and other estimates are presented in Table 8 and 
are analyzed in more detail in the following subsections.
6.1.1 Environmental Results
Table 9 and Figures 5 and 6 show the reduction in 
emissions and concentration levels in one year due to 
the technical solution implemented. Units are measured 
in tons for emissions levels and µg/m3 for concentration 
levels. The proposed fleet’s renewal would result in a 
drop in emissions of about 140 tons of PM10 and 98 
tons of PM2.5 compared to the levels of 2016, which 
represents approximately a 95 percent reduction as 
proposed in municipal law 16.802/2018. Changes in 
concentration levels would reduce around 0.1535µg/m3 
and 0.1075 µg/m3, for PM10 and PM2.5, respectively.
STAGE SUBSTAGE
PM2.5 PM10
1 YEAR 30 YEARS 1 YEAR 30 YEARS
ENVIRONMENTAL
Emissions (tons/year) -97.7 -139.6 
Concentration  (µg/m³) -0.1075 -0.1535 
EPIDEMIOLOGICAL
Morbidity cases  
Number of disease 
cases
-95 -3,171 -40 -1,443 
Mortality cases  
Number of fatalities -4 - 141 -2 -89 
Working days lost due 
to hospitalization stays -647 -22,601 -315 -11,544 
FINANCIAL AND 
ECONOMIC
Morbidity costs  
Cost of illness (R$) -296,528.95 -5,394,473.45 -157,494.47 -2,901,726.76 
Mortality costs 
Value of statistical life (R$) -16,741,814.29 -300,947,149.42 -8,764,888.26 -175,814,062.86 
Table 8  |  Main Results of the Second Simulation: Location in the ImpactAr Tool — Main Results Spreadsheet
Source: WRI authors.
POLLUTANT CURRENT FLEET 
(SCENARIO 0)
PROJECTED FLEET 
(SCENARIO 1) VARIATION VARIATION (%)
EMISSIONS  
(TONS/YEAR)
PM2.5 102.84 5.1 -97.69 -95
PM10 146.91 7.4 -139.55 -95
CONCENTRATION  
(µ G/M³)
PM2.5 0.1131 0.0057 -0.1075 -95
PM10 0.1616 0.0081 -0.1535 -95
Table 9  |  Main Environmental Results: Location in the ImpactAr Tool—Environmental Stage Spreadsheet
Source: WRI authors.

22  |  
Figure 5  |  Emissions Reductions: Location in the 
ImpactAr Tool—Environmental Stage 
Spreadsheet 
Figure 6  |  Concentration Reduction: Location in 
the ImpactAr Tool—Environmental Stage 
Spreadsheet
Source: ImpactAr tool. Source: ImpactAr tool.
6.1.2 Epidemiological Results
Table 10 and Figures 7, 8, 9, and 10 present the numbers 
of morbidity and mortality cases avoided according to 
the long-run and short-run analyses of the ImpactAr 
tool, measured for each pollutant and type of disease. 
The reductions in PM10 and PM2.5 emissions are reflected 
in the number of mortality and morbidity cases related 
to air pollution. For total cumulative effects provided 
Annual emissions variations (tons/year)
-97 .69
-139.55
PM2.5 PM10
Annual concentration variation (/uni00B5g/m/three.sups)
-0.107
-0.154
PM2.5 PM10
Table 10  |  Main Epidemiological Results: Location in the ImpactAr Tool—Epidemiological Stage Spreadsheet
Source: WRI authors.
VARIATION OF FATAL AND NONFATAL CASES
TYPE OF HEALTH 
IMPACT POLLUTANT CURRENT FLEET 
(SCENARIO 0)
PROJECTED FLEET 
(SCENARIO 1) VARIATION VARIATION (%)
MORBIDITY
PM2.5
1 -35 -60 -95
30 -1,296 -1,875 -3,171
PM10
1 -23 -17 -40
30 -821 -622 -1,443
MORTALITY
PM2.5
1 -3 -1 -4
30 -108 -33 -141
PM10
1 0 -2 -2
30 -1 -87 -88
by the long-run analysis (30 years), reductions in 
PM2.5 concentration levels would avoid approximately 
3,171 hospitalizations, whereas reductions in PM10 
concentration levels would avoid about 1,443. As for 
mortality outcomes, 141 cases would be avoided due to 
the drops in PM2.5 levels and 89 cases due to the drops 
in PM10 levels, both for the 30-year analysis.

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  23
Figure 7  |  Avoided Morbidity in One Year: Location in 
the ImpactAr Tool—Epidemiological Stage 
Spreadsheet
Figure 8  |  Avoided Morbidity in 30 years: Location in 
the ImpactAr Tool—Epidemiological Stage 
Spreadsheet
Source: ImpactAr tool. Source: ImpactAr tool.
Variation on morbidity cases - 1 year
Cardiovascular disease
-35
Respiratory disease
-23
-60
-17
PM2.5 PM10
Variation on morbidity cases - 30 years
Cardiovascular disease
-1,296
Respiratory disease
-821
-1,875
-622
PM2.5 PM10
Figure 9  |  Avoided Mortality Cases in One Year: Location 
in the ImpactAr Tool—Epidemiological Stage 
Spreadsheet
Figure 10  |  Avoided Mortality Cases in 30 Years: 
Location in the ImpactAr Tool—
Epidemiological Stage Spreadsheet
Source: ImpactAr tool. Source: ImpactAr tool.
Variation on mortality cases - 1 year
Cardiovascular disease
-3
Respiratory disease
0
-1
-2
PM2.5 PM10
Variation on mortality cases - 30 years
Cardiovascular disease
-108
Respiratory disease
-1
-33
-87
PM2.5 PM10
The numbers of avoided fatalities were significantly 
lower than those for avoided hospitalizations. This 
result was already expected because C-Rs had already 
shown that the impact of changes in concentration 
levels was much higher for nonfatal diseases than for 
fatal diseases. For both mortality and morbidity, PM2.5 
impacts were significantly larger when compared to 
PM10 figures.

24  |  
6.1.3 Financial and Economic Results
Tables 11 and 12 show the costs avoided related to the 
variation in the numbers of mortality and morbidity 
cases linked to the fleet’s renewal. It is worth noting 
that mortality costs are of economic nature, whereas 
morbidity costs are of financial nature. This happens 
due to the different methodology of measuring each 
health impact type: mortality costs are calculated 
through the VSL, and morbidity costs are measured 
through the COI methodology.
Figures 11 and 12 summarize savings in terms of 
hospitalization costs and income losses as a result of 
the decrease in the number of nonfatal diseases. Again, 
analysis cover the impacts of PM10 and PM2.5, short-run 
and long-run analyses for each health endpoint. As 
expected, cardiovascular diseases presented the larger 
share of the costs avoided. The cumulative effects of 
avoided costs in 30 years totaled R$5,394,473 for PM2.5 
and R$2,901,726. for PM10. According to the short-run 
analysis (1 year), PM2.5 reductions would avoid costs of 
around R$296,528, and PM10 reductions would avoid 
costs of around R$157,494.
Table 11  |  Total Cost of Morbidity: Location in the ImpactAr Tool—Financial and Economic Stage Spreadsheet
Table 12  |  Total Cost of Mortality: Location in the ImpactAr Tool—Financial and Economic Stage Spreadsheet
Source: WRI authors.
Source: WRI authors.
VARIATION ON TOTAL MORBIDITY COSTS
POLLUTANT PERIOD
(YEARS)
CARDIOVASCULAR 
DISEASES (R$)
RESPIRATORY 
DISEASES (R$) TOTAL (R$)
MORBIDITY
PM2.5
1 -178,277 -118,251 -296,528
30 -3,337,702 -2,056,771 -5,394,473
PM10
1 -114,573 -42,921 -157,494
30 -2,091,155 -810,571 -2,901,726
VARIATION ON TOTAL MORTALITY COSTS
POLLUTANT PERIOD
(YEARS)
CARDIOVASCULAR 
DISEASES (R$)
RESPIRATORY 
DISEASES (R$) TOTAL (R$)
MORTALITY
PM2.5
1 -12,521,006 -4,220,807 -16,741,814
30 -228,191,287 -72,755,862 -300,947,149
PM10
1 -152,874 -8,612,014 -8,764,888
30 -2,944,259 -172,869,803 -175,814,062

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  25
Figure 11  |  Avoided Morbidity Costs in One Year: 
Location in the ImpactAr Tool—Financial and 
Economic Stage Spreadsheet
Figure 12  |  Avoided Morbidity Costs in 30 Years: 
Location in the ImpactAr Tool—Financial and 
Economic Stage Spreadsheet
Source: ImpactAr tool. Source: ImpactAr tool.
Variation on total morbidity costs - 1 year (R$)
Cardiovascular disease Respiratory disease
-118,251
-178,278
-114,573
-42,921
PM2.5 PM10
Variation on total morbidity costs - 30 years (R$)
Cardiovascular disease Respiratory disease
-2,056,771
-3,337 ,702
-2,091,155
-810,572
PM2.5 PM10
Figure 13  |  Avoided Mortality Costs in One Year: 
Location in the ImpactAr Tool—Financial and 
Economic Spreadsheet
Figure 14  |  Avoided Mortality Costs in 30 Years: 
Location in the ImpactAr Tool—Financial and 
Economic Spreadsheet
The mortality economic costs avoided represented the 
largest figures in the Financial and Economic Stage 
of the results provided by the ImpactAr tool. This can 
be explained by the intended variables covered by the 
methodology. The idea is to provide a measure, in terms 
of Brazilian reals, of the welfare losses avoided due to 
variations in air pollution levels. The values, however, 
do not have an accountant nature and therefore cannot 
be addressed as financial costs. 
Figures 13 and 14 illustrate the mortality costs 
avoided as a result of the technical solution adopted 
for São Paulo’s urban bus fleet. The total avoided 
economic/welfare losses related to mortality reached 
R$300,947,149 for PM2.5 reductions and R$175,814,062 
for PM10 reductions in 30 years. 
Source: ImpactAr tool. Source: ImpactAr tool.
Variation on mortality costs - 1 year (R$)
Cardiovascular disease
-12,521,007
Respiratory disease
-4,220,807
-152,874
-8,612,014
PM2.5 PM10
Variation on mortality costs - 30 years (R$)
Cardiovascular disease
-228,191,287
Respiratory disease
-72,755,862
-2,944,260
-172,869,803
PM2.5 PM10

26  |  
6.1.4 Comparative Analysis 
Considering the costs that would be avoided due to the 
reduction of PM2.5 and PM10 emissions, the ImpactAr 
tool provided a comparative analysis with selected 
economic indicators for the municipality of São Paulo. 
It analyzed how much the monetary outcomes, as a 
consequence of the proposed change in the bus fleet, 
would represent in terms of the municipal GDP, 
municipal health, and hospitalization expenditures in 
2018, and how many public hospitalizations could be 
provided to the population, according to the financial 
savings. This information is presented in Table 13. 
In one year, the total avoided COI (direct and indirect 
costs summed) is almost zero compared to the annual 
GDP and total health expenditure of São Paulo. 
However, the savings due to nonfatal diseases could 
provide São Paulo’s population with an additional 107 
hospitalizations surplus, in the case of PM2.5 reductions, 
and 57 in the case of PM10 reductions, considering the 
average unit price of public and private hospitalizations 
in 2018 from all causes in São Paulo. Mortality costs, in 
turn, would represent around 0.012 percent and 0.006 
percent of the municipal GDP, for PM2.5 and PM10 in one 
year, respectively. 
If we consider the cumulative impact of avoided costs 
for 30 years and compare it with the same annual 
indicators, the 30-year avoided cost of mortality could 
reach about 0.23 percent and 0.13 percent of São Paulo’s 
GDP, for PM2.5 and PM10, respectively. 
Summing up the COI for 30 years, the values remain 
low, being about 0.004 percent for PM2.5 and 0.002 
percent for PM10 of municipal GDP. As for the relation 
of morbidity avoided costs and the municipal health and 
hospitalization expenditures of 2018, PM2.5 associated 
costs represented, respectively, 0.05 percent and 0.64 
percent, and PM10 associated costs around 0.03 percent 
and 0.34 percent. In terms of additional hospitalizations 
due to morbidity savings, the numbers reach 1,943 for 
PM2.5 and 1,045 hospitalizations that could be provided 
to the population.
PERIOD SUBSTAGE
TOTAL COSTS 
VARIATION (R$)
TOTAL COSTS 
VARIATION/GDPm 
(%)
TOTAL COSTS 
VARIATION /
ANNUAL HEALTH 
EXPENDITURE (%)
TOTAL COSTS 
VARIATION /
ANNUAL HOSPITAL 
EXPENDITURE (%)
NUMBER OF 
HOSPITALIZATIONS 
DUE TO SAVING/
COSTS OF THE FLEET 
CHANGES (%)
PM2.5 PM10 PM2.5 PM10 PM2.5 PM10 PM2.5 PM10 PM2.5 PM10
1 YEAR
Morbidity -296,528.95 -157,494.47   0.00022947   0.0001219   0.00300284   0.00159489   0.03547773   0.01884317       107         57 
Mortality -16,741,814.29 -8,764,888.26   0.01295592   0.0067828 *  * *  *  *  *
30 YEARS
Morbidity -5,394,473.45 -2,901,726.76     0.0041746   0.0022455   0.05462784   0.02938471   0.64541308   0.34717242    1,943    1,045 
Mortality -300,947,149.42 -175,814,062.86   0.23289267   0.1360565 * * *  *  * * 
Table 13  |  Comparative Analysis: Main Results Spreadsheet
Notes: GDPm = municipal gross domestic product.
*For the costs associated with mortality, the value of statistical life (VSL) methodology was used. VSL is an estimate of how much people are willing to pay 
to reduce the risk of death, taking into account issues such as suffering and discomfort. Therefore, this cost represents more than the financial impacts of 
mortality and cannot be compared with financial variables such as health expenditures.
Source: WRI authors.

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  27
Table 14  |  Comparative Analysis: Main Results for PM2.5 estimated using Linking functions 2.1 and 2.2
6.1.5 Comparative Analysis using Linking function 2.1 
and Linking function 2.2
The results presented above were developed based on 
the PM FCM obtained through the Linking function 
2.2. In this section, for illustrative and comparative 
purposes, it is also shown the results obtained through 
Linking function 2.1 (Table 14). The same data inputs, 
previously described, were considered for the current 
fleet and the projected fleet.
For the city of São Paulo, the simulation performed 
using the methodology described in Linking function 
2.2 resulted in a 23% reduction in the PM FCM. 
It is possible to verify that, after the substage of 
concentration estimation, the indicators observed show 
the same percentage reduction as the PM FCM, since 
there is a linear relationship between this variable and 
the results. This pattern is verified for PM10.
With this, it is possible to conclude that when using 
the Linking function 2.2, there is a reduction in the 
absolute number of cases of morbidity and mortality 
and, consequently, in costs. It is important to note that 
this reduction in the absolute number is valid for the 
cities analyzed and considering the technical parameters 
described in the simulation, but not for all cases. Also, 
since they are econometric models that have aggregated 
errors in each step, which are not measured (see section 
5. Limitations and uncertainties), it can be considered 
that the results of two different linking functions are 
relatively close. As mentioned in the Methodology 
section, the variation observed in the results can be due 
to differences in the distribution of PM emissions and 
due to the period evaluated for each simulation.
STAGE SUBSTAGE
PM2.5 PM10 ∆  (absolute value)
1 YEAR 30 YEARS 1 YEAR 30 YEARS 1 YEAR 30 YEARS
ENVIRONMENTAL
Emissions (tons/year) -97.7 -97.7 0
Concentration  (µg/m³) -0.1397 -0.1075 0.0322
EPIDEMIOLOGICAL
Morbidity cases   
Number of disease cases -124         4,122.00 -95 -3,171.00 29 952 
Mortality cases  
Number of fatalities -5 -184 -4 -141 1 42
Working days lost due to 
hospitalization stays -841 -29,383.00 -647 -22,601.00 194 6,782 
FINANCIAL AND 
ECONOMIC
Morbidity costs  
Cost of illness (R$) -385,513.51 -7,013,262.75 -296,528.95 -5,394,473.45 88,985 1,618,789 
Mortality costs 
Value of statistical life (R$) 21,764,725 -391,237,883 -16,741,814 -300,947,149 5,022,911 90,290,734 
Source: WRI authors.

28  |  
7. FINAL REMARKS AND CONCLUSION
Air pollution currently imposes one of the most serious 
threats to a variety of dimensions of human life. 
Fighting against air pollution requires the engagement 
of decision-makers from different sectors and the use 
of epidemiological, economic, and financial evidence 
provides a common ground for it (WHO/Europe and 
OECD 2015). As mentioned before, however, estimating 
the unobservable costs of air pollution impacts is 
not a trivial task, as it requires the use of several 
methodologies that are capable of both isolating the 
effects of pollutants on health and estimating the costs 
associated with these diseases.
Through the systematic organization of several existing 
methodologies applied in national empirical studies, 
the ImpactAr tool conveys the different stages of the 
chain process that pollutants go through in one tool. By 
allying scientific integrity and practicality, the tool is an 
attempt to provide Brazilian public municipal decision-
makers, as well as politicians, private sector operators, 
academics, researchers. and the public in general, with 
(i) a robust tool that models air pollution impacts, 
(ii) easy access to the advanced methodologies, (iii) 
maximum ease of use and understanding of the results, 
and (iv) transparency about the methodology and data 
used in the process. 
By using the ImpactAr tool, estimates on the existence 
and magnitude of the impacts on health and its related 
costs of PM caused by changes in the bus fleet can be 
measured for the cities of São Paulo, Rio de Janeiro, Belo 
Horizonte, and Niterói. The tool is a first step toward 
making observable the implicit costs of air pollution in 
Brazilian cities, after which a deeper research on a case-
by-case basis should be carried out. The tool’s results can 
broaden the benefit-cost analysis of transport projects 
made by their proponents by adding the potential non 
observable costs of air pollution. 
It is important to bear in mind that, although the 
impacts related to human health are considered the 
most significant consequences of air pollution, the 
literature on the matter has strongly suggested that 
air pollution affects other areas of human life, such 
as urban vegetation (Amato-Lourenço et al. 2016), 
real estate values (Carriazo Osorio 2001), and cultural 
heritage (Watt et al. 2009). Furthermore, air pollution, 
and, more specifically, the short-lived climate forcers 
(SLCFs),31 are also important contributors to climate 
change and key challenges because their reduction 
would have the potential to slow the climate change in 
the near term (UNEP 2011). Due to limited data and the 
incipient Brazilian empirical studies on these subjects, 
we opted not to include such areas, as we would 
significantly raise the uncertainty of the model, though 
it is important not to forget that, by broadening the 
areas of impact, the costs/benefits of a fleet’s renewal 
would certainly increase.
Despite focusing on four Brazilian cities, the aim of 
the tool is not to be confined to them. In this sense, 
both ImpactAr and its technical note should be used as 
a blueprint for other cities to learn and develop their 
own version of the ImpactAr tool. In the future, more 
Brazilian cities are expected to be included, depending 
on the availability of open data. The authors encourage 
users to provide feedback and recommendations so 
they can advance both the applicability as well as the 
accuracy of their results.

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  29
APPENDIX A. IMPACTAR TOOL USER GUIDE 
AND SPREADSHEET INTERFACES
This section presents a short user guide (along with the interfaces of 
specific spreadsheets in the ImpactAr tool32) to help users enter the 
required and/or optional data and to navigate the main outcomes of the 
tool. It is worth remembering that ImpactAr was built to maintain maximum 
ease of use and understanding of the results for users. By following the 
instructions below, users will be able to fully operate the tool.
A.1 Inserting Optional Data
After the first two spreadsheets—“Cover” and “User Guide” (presented 
in Section 3, ImpactAr Tool Structure)—the tool presents the “Optional 
Inputs” (OPT_INPUTS) spreadsheet (Figure A1). This optional input sheet 
contains a table that enables users to change the PM emissions factors 
(g/L) and average fuel effiency (L or kWh/100 km) per the technology of 
the buses. The values available in the model by default are provided in the 
white cells of the table. The optional value can be filled in the green cells 
of the table only if the user possesses such data; otherwise, green cells 
must be kept with N/A value, as the model will provide data by default.
Figure A1  |  Interface of the Optional Input Spreadsheet—OPT_INPUTS
Source: ImpactAr tool.
A.2 Inserting Required Data
After the Optional Inputs spreadsheet is the “Project” (1_PROJECT) 
spreadsheet. This is the only required input section. To start the 
simulation, the user should follow the steps provided in this spreadsheet. 
Step 1: Choose your city. The user must first select the city of interest: 
São Paulo, Rio de Janeiro, Belo Horizonte, or Niteroi—by filtering the cell. 
Please note that entering the correct city is paramount to getting the 
correct results because the databases used to calculate the impacts for 
each city vary significantly and, therefore, the outcomes as well.
Step 2: Do you have information regarding your current and 
projected fleet of buses and/or trucks? Before users are required to 
input information about the current and projected bus fleets, there is a 
cell asking whether they possess such data. If users possess the data, 
they are instructed to remain in the same spreadsheet and complete 
the following two tables with the data (see Step 3 below). If users do 
not possess the required information, they are instructed to press a cell, 
which leads them directly to the additional step in the same spreadsheet 
(see Additional Step).
Step 3: Fill in the data regarding your current and your projected 
fleet.  Fleet data must be entered in the input worksheet (Project 
spreadsheet) twice: once for the city’s current bus fleet and once for the 
city’s projected (future) bus fleet. Data required include the
 ▪ number of buses (current and projected fleet); 
 ▪ type of technology (current and projected fleet); and
 ▪ average annual travel distance (km) per bus (current and projected fleet).
Additional Step: Fill in environmental data. Note you should only 
fill these cells if you haven’t filled the data required in Step 3, 
otherwise, keep the annual value of the table “Input Data” as “0.”  
This step is only required for users who have not filled in the data about 
the urban bus fleet (both current and projected). Here, any value of annual 
emissions or concentration levels of PM 2.5 or PM10 can be inputted, and the 
tool will measure the epidemiological, financial, and economic impacts in 
the following spreadsheets. In this case, the values entered will represent 
annual variations on air pollution levels linked to the transport sector. 
This means that the tool will assume that air pollution levels for scenario 
1 represent the values inputted by the user, and the air pollution levels for 
scenario 0 will be equal to zero.

30  |  
It should be noted that if users enter the data in the Additional Step 
section, the inputs inserted for the measurement of the impacts of fleet 
renewal will not be considered. In this sense, users should always keep 
the annual value of the Input Data table in the Additional Step as “0” if 
they want to measure the impacts of fleet renewal.
In order to present the interface of the Project Stage, we have broken 
the spreadsheet into Figure A2, which presents the section of the 
spreadsheet with Steps 1, 2, and 3; and Figure A3, which presents the 
section of the spreadsheet with the Additional Step.
Figure A2  |  Interface of the Project Stage Spreadsheet: Steps 1, 2, and 3—1_PROJECT
Figure A3  |  Interface of Project Stage Spreadsheet: Additional Step—1_PROJECT
Source: ImpactAr tool.
Source: ImpactAr tool.

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  31
A.3 Analyzing the Results
After filling in either the information required for the fleet renewal or 
the environmental data, no new data will be required and the user can 
navigate the results of the simulation’s in the following five spreadsheets. 
Each spreadsheet or section contains a summary analysis of the 
main results per stage (environmental, epidemiological, and financial-
economic) and a detailed section with specific outcomes. Different tables 
and different graphs that can be filtered are provided in each section 
and all analyses cover 1-year impacts (short-run analysis) and 30-year 
impacts (long-run analysis) of the variation of PM 10 and PM2.5 levels. If 
the level of PM 2.5  and PM10 emissions or concentration decrease 
(increase) as a result of the differences between the current and 
the projected fleet, all results will be given as negative (positive), 
meaning a reduction (growth) in emissions and concentration 
levels, epidemiological cases, and financial and economic costs. 
All the results will be given as negative if the user provided 
input information in the Additional Step section of the Project 
spreadsheet, as the tool will assume that air pollution levels for 
scenario 1 represent the values inputted by the user, and the air 
pollution levels for scenario 0 will be equal to zero. Below you can 
find details on each spreadsheet’s results section.
Analysis of the environmental results spreadsheet (2_
ENVIRONMENTAL_STAGE).  In the first part of this section, the user 
can analyze the main environmental results in terms of variations 
in concentration and emissions levels of PM 2.5 and PM10. This data is 
presented in a table and two graphs that can be filtered. The spreadsheet 
also provides a second part with detailed results, showing total emissions 
and concentration levels by type of technology for both the current and 
projected fleets. This second part provides six tables and four graphs that 
can be filtered. 
In order to present the interface of the Environmental Stage, we have 
broken the spreadsheet into Figure A4, which presents the section 
with the main environmental results, and Figure A5, which presents the 
section with the detailed environmental results. 
Figure A4  |  Interface of the Environmental Stage Spreadsheet: Main Environmental Results—2_ENVIRONMENTAL_STAGE

32  |  
Figure A5  |  Interface of the Environmental Stage Spreadsheet: Detailed Environmental Results—2_ENVIRONMENTAL_STAGE
Analysis of the epidemiological results spreadsheet (3_
EPIDEMIOLOGICAL_STAGE).  In the first part of this section, the user can 
analyze the main epidemiological results as a function of variations in 
PM2.5 and PM10 concentration levels. These results are separated by fatal 
and nonfatal cases of respiratory disease and cardiovascular disease, 
and by 1-year and 30-year analyses. This data is presented in a table and 
4 graphs that can be filtered. The worksheet also provides a second part 
with detailed results, presenting the above epidemiological findings by 
age group and type of financial coverage of cases (public or private). This 
part also includes two tables with the total numbers of workdays lost due 
to hospitalizations and the total number of workdays lost per age range. 
We have not provided a table of work absences per type of financial 
coverage because we assumed the average stay to be the same for public 
and private hospitalizations. This part provides four tables and 14 graphs 
that can be filtered. 
In order to present the interface of the Epidemiological Stage, we have 
broken the spreadsheet into Figure A6, which presents with the main 
epidemiological results; Figure A7, which shows the first part of the 
detailed epidemiological results sections; Figure A8, which presents the 
second part; and Figure A9, which shows the third and final part of the 
detailed epidemiological results section. 
Source: ImpactAr tool.

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  33
Figure A6  |  Interface of the Epidemiological Stage Spreadsheet: Main Epidemiological Results—3_EPIDEMIOLOGICAL_STAGE 
Figure A7  |  Interface of the Epidemiological Stage Spreadsheet: First Part of the Detailed Epidemiological Results 
Section—3_EPIDEMIOLOGICAL_STAGE

34  |  
Figure A9  |  Interface of the Epidemiological Stage Spreadsheet: Third Part of the Detailed Epidemiological Results 
Section—3_EPIDEMIOLOGICAL_STAGE
Figure A8  |  Interface of the Epidemiological Stage Spreadsheet: Second Part of the Detailed Epidemiological Results 
Section—3_EPIDEMIOLOGICAL_STAGE
Source: ImpactAr tool.
Source: ImpactAr tool.

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  35
Analysis of the financial and economic results spreadsheet 
(4_FINANCE AND ECONOMIC_STAGE). In the first part of this section, 
the user can analyze the main financial and economic results according 
to the cases of mortality and morbidity linked to variations in PM 2.5 and 
PM10 concentration levels. These results are separated by fatal and 
nonfatal cases of respiratory and cardiovascular diseases, and by 1-year 
and 30-year analyses. This data is presented in two tables and four 
graphs that can be filtered. The spreadsheet also provides a second 
part with the detailed results of morbidity-related costs. These costs are 
separated into the total cost of morbidity, the direct cost of morbidity 
(cost of hospitalization), and the indirect cost of morbidity (cost of income 
loss due to absences at work caused by hospitalization). The analyses are 
made by age group and by type of financial coverage of the cases (public 
or private). This part provides 6 tables and 24 graphs that can be filtered. 
We have not provided the analysis of the mortality costs by age group 
because one of the C-Rs for mortality does not offer this differentiation. 
Furthermore, we also have not included the analysis of the financial 
coverage of the mortality cases because the methodology used to 
measure the mortality costs (VSL) does not allow such classification (for 
further information, please see Section 2.1, Key Concepts). 
In order to present the interface of the Financial and Economic Stage, we 
have broken the spreadsheet into Figure A10, which presents the main 
financial and economic results; Figure A11, which shows the first part of 
the detailed financial and economic results sections; Figure A12, which 
presents the second part of the detailed financial and economic results 
section; Figure A13, which presents the third part of the detailed financial 
and economic results section; and A14, which presents the fourth and 
final part of the detailed financial and economic results section.
Figure A10  |  Interface of the Financial and Economic Stage Spreadsheet: Main Financial and Economic Results–4_
FINANCIAL AND ECONOMIC_STAGE

36  |  
Figure A12  |  Interface of the Financial and Economic Stage Spreadsheet: Part 2, Detailed Financial and Economic Results 
Section, Tables with Total and Direct Costs of Morbidity per Age Range—4_FINANCIAL AND ECONOMIC_STAGE
Figure A11  |  Interface of the Financial and Economic Stage Spreadsheet: Part 1, Detailed Financial and Economic 
Results Section—4_FINANCIAL AND ECONOMIC_STAGE
Source: ImpactAr tool.
Source: ImpactAr tool.

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  37
Source: ImpactAr tool.
Source: ImpactAr tool.
Figure A13  |  Interface of the Financial and Economic Stage Spreadsheet: Part 3, Detailed Financial and Economic 
Results Section, Tables with Indirect Costs of Morbidity per Age Range and Total Costs of Morbidity per 
Type of Health Insurance Coverage—4_FINANCIAL AND ECONOMIC_STAGE
Figure A14  |   Interface of the Financial and Economic Stage Spreadsheet: Part 4, Detailed Financial and Economic 
Results Section, Tables with Direct and Indirect Costs of Morbidity per Type of Health Insurance 
Coverage—4_FINANCIAL AND ECONOMIC_STAGE

38  |  
Figure A15  |  Interface of the Main Results Spreadsheet: Sheet 5, Section 1
Analysis of the main results spreadsheet (5_MAIN RESULTS). In the 
first part of this section, a table is provided with the main environmental, 
epidemiological, financial, and economic results of the simulation for the 
1-year and 30-year periods. After it, in the second part, the spreadsheet 
presents a table with a comparative analysis between the financial and 
economic results for the 1-year and 30-year periods and the municipal 
GDP , the 2018 annual municipal health expenditure, the 2018 annual 
municipal hospitalization expenditure, and the number of medical 
Source: ImpactAr tool.
appointments “saved” or “spent” as a function of the financial savings/
losses caused by the bus fleet change or by the environmental input data. 
In order to present the interface of the Main Results, we have broken 
the spreadsheet into Figure A15, which presents the first section of the 
spreadsheet, and Figure A16, which presents the second and final section 
of the spreadsheet.
Source: ImpactAr tool.
Figure A16  |  Interface of the Main Results Spreadsheet: Sheet 5, Section 2

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  39
The long-term analysis spreadsheet (6_LONG-RUN ANALYSIS).  
In this spreadsheet, the user can filter eight types of graphs with 
information regarding the evolution of morbidity and mortality cases 
per year as well as the associated costs per year. Charts provide 
quantitative values every five years (Figure A16).
Source: ImpactAr tool.
Figure A17  |  Interface of the Long-Run Analysis: Sheet 6

40  |  
APPENDIX B. BRAZILIAN LITERATURE 
REVIEW ON HEALTH AND ECONOMIC 
IMPACTS OF AIR POLLUTION—
METHODOLOGY DESCRIPTION, MAIN 
FINDINGS, AND CONTRIBUTIONS TO BUILD 
THE IMPACTAR TOOL
The methodologies and data applied to build the ImpactAr tool was based 
on the most recent and well-grounded Brazilian empirical literature on 
the measurement of air pollution impacts on health and economy in the 
country. During the first stages of the ImpactAr tool project, WRI Brasil 
carried out a survey on the state-of-the-art studies that analyzed air 
pollution impacts in Brazilian cities to understand how the impacts linked 
to pollutants are manifested and measured in the Brazilian context. To 
that end, a literature review was conducted with the following research 
question: What are the economic and health impacts of urban air 
pollution in Brazil?
The review was stratified in a three-stage process (Table B1). In Stage 1, 
the WRI team carried out searches on the main academic search 
platforms with predefined keywords. Stage 2 consisted of researching 
publications from the key researchers and institutions identified in 
Stage 1. Finally, in Stage 3, the WRI team held a workshop with the key 
researchers and institutions for validation of the literature review. This 
process was carried out over a period of approximately six months and 
mapped 67 studies from which the main choices of health impacts and 
methodologies applied in the ImpactAr tool were retrieved.
Among the main features within these 67 studies, we were able to identify 
that the most commonly researched pollutant was PM10, followed by ozone 
(O3), but PM2.5 was studied less frequently. Furthermore, we learned that, 
besides the fact that PM is strongly linked to bus emissions and is also 
considered the most harmful pollutant (WHO 2018), PM10 and PM2.5 present 
different emissions sources from road transport activities (Hooftman et. al 
2016) and different health impact incidence (Abe and Miraglia 2016; Silva et 
al. 2017). In this sense, although it is not possible to total the impacts of PM10 
and PM2.5, as PM10 particles circumscribe PM2.5 particles, the WRI team has 
opted to include both pollutants in the scope of the ImpactAr tool. 
In relation to the analysis of the studied health endpoints in the 
publications, a significant predominance of fatal respiratory (41.8 percent), 
fatal cardiovascular (28.3 percent), nonfatal respiratory (50.7 percent), and 
nonfatal cardiovascular (32.8 percent) diseases was verified. Therefore, 
the WRI team included these health impacts in the ImpactAr tool analysis 
and retrieved the C-Rs used to measure the epidemiological impacts from 
7 articles among the 67 publications. 
Finally, regarding the financial and economic aspects addressed 
in the publications, a minor share of the studies, 22 out 67 (33 
percent), monetized the health impacts of air pollution. Amid the 
main methodologies, we can list the COI to measure financial impacts 
of hospitalizations, which was added to this tool. In relation to the 
monetization of deaths, the WRI team opted to use the VSL method, which 
was presented in some publications. The literature did not present recent 
primary data on the VSL, nor did it provide a standard value for Brazil. 
Therefore, to obtain the VSL, we have transferred the reference value 
provided by the 2012 OECD study with adjustment to income and inflation 
(Roy and Braathen 2017). 
STAGE 1 | KEYWORDS ON ACADEMIC SEARCH PLATFORMS
 ▪ Platforms: Scielo, Google Scholar, Capes, and Science Direct
 ▪ Keywords: air quality, economic impacts, brazil, urban air 
pollution, impacts, valuation, urban, air pollution, urban, 
monuments, restoration, leisure
 ▪ Around 1.200 studies analyzed
 ▪ Number of studies retrieved: 52
STAGE 2 | SEARCH OF KEY ACTOR PUBLICATIONS
 ▪ Names found on actors mapping (platform search)
 ▪ Number of studies retrieved: 9
STAGE 3 | SPECIALIST SUGGESTIONS FROM WORKSHOP AND 
INSTITUTE PLATFORMS
 ▪ Workshop took place on the June 22, 2018
 ▪ Platforms of institutes searched: Institute of Health and 
Sustainability (Instituto Saúde e Sustentabilidade, ISS); 
Institute for Energy and Environment (Instituto Energia e Meio 
Ambiente, IEMA)
 ▪ Number of studies retrieved: 6
Table B1  |   Description of the Literature Review Stages 
Source: WRI authors.

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  41
ABBREVIATIONS
ANS Agência Nacional de Saúde Suplementar (National Agency 
for Supplementary Health)
BRAMS Brazilian Developments on the Regional Atmospheric 
Modeling System
BRIICS Brazil, Russia, Indonesia, India, China and South Africa
CCATT Coupled Chemistry Aerosol-Tracer Transport 
CIFF Children’s Investment Fund Foundation
COI cost of illness
CO2 carbon dioxide
CPTEC Centro de Previsão do Tempo e Estudos Climáticos (Center 
for Weather Forecast and Climatic Studies)
C-R concentration-response coefficient
DALY disability-adjusted life years 
DATASUS Departamento de Informática do Sistema Único de Saúde 
(Brazilian Health Informatics Department)
EPA U.S. Environmental Protection Agency
ExternE  external costs of energy
FCM fixed conversion measure
GDP gross domestic product
GDPm municipal gross domestic product
GHG greenhouse gas
GIS Geographic Information System
GTFS General Transit Feed Specification
IBGE Instituto Brasileiro de Geografia e Estatística (Brazilian 
Institute of Geography and Statistics)
ICD-10 10 th revision of the International Statistical Classification of 
Diseases and Related Health Problems
IEMA Instituto Energia e Meio Ambiente (Institute for Energy and 
the Environment)
ImpactAr  valuation tool for health impacts of air pollution
INPE Instituto Nacional de Pesquisas Espaciais (National Institute 
for Space Research)
IPA impact pathway approach
IPCA Índice Nacional de Preços ao Consumidor Amplo (Broad 
National Consumer Price Index)
IPCC Intergovernmental Panel on Climate Change 
ISS Instituto Saúde e Sustentabilidade (Institute of Health and 
Sustainability)
NOx nitrogen oxides
OECD Organisation for Economic Co-operation and Development
O3 ozone
PM particulate matter
RCP Representative Concentration Pathway 
SIDRA Sistema IBGE de Recuperação Automática (IBGE Automatic 
Recovery System) 
SLCF short-lived climate forcer
VSL value of statistical life
WRI World Resources Institute
WTP willingness to pay
ENDNOTES
1. Anthropogenic sources are caused by human activities. 
2. In terms of PM share of transport emissions from exhaust and wear/
combustion, buses account for 17 percent and 14 percent, and trucks 
account for 75 percent and 64 percent, respectively (MMA 2014).
3. Information retrieved from literature review of the state-of-the-art 
Brazilian empirical studies on the issue of health and economic 
impacts of air pollution. For further information, please see Appendix B. 
4. It is important to note that the ImpactAr tool does not aim to provide 
users with a benefit-cost analysis of projects to renew a bus fleet but 
rather to point to the existence and magnitude of the implicit costs of 
air pollution embedded in such plans.
5. To see the list of all data and variables used in the model, please see 
Section 4, Data Sources.
6. The BRAMS 5.2 modeling system is an online model with an Eulerian 
approach and basically solves the mass conservation equation for any 
tracer. It has an extensive network of collaborators in the world and 
has been developed and adjusted to the South American continent, 
which makes it an integrated environmental model tuned for tropical 
and extratropical areas. BRAMS also includes a surface scheme to 
simulate the energy, water, carbon, and other biogeochemical cycles 
(Moreira et al. 2013) and soil moisture initialization using real-time 
cycling estimation from an offline hydrological model (Gevaerd and 
Freitas 2006). In Brazil, BRAMS has been applied for numerical studies 
in several universities and research centers addressing local storms, 
urban heat islands, urban and remote air pollution, aerosol-cloud-
radiation interactions, and so forth.
7. ExternE is the abbreviation for “external costs of energy.” Between 
the 1990s and 2005, the European Union initiated a series of ExternE 
projects. The “ExternE Methodology” is an approach of calculating 
environmental external costs developed during the ExternE Project 
series called the IPA (ExternE, n.d.).
8. For further information, please see Appendix B. 
9. Whereas PM2.5 emissions are linked to exhaust sources, such as 
fuel combustion, PM 10 emissions are linked to both exhaust and 
nonexhaust sources such as fuel combustion, brakes, tires, and road 
surface wear (Hooftman et al. 2016, 7).
10. Although both types of pollutants are linked to respiratory and 
cardiovascular diseases, PM 2.5 emissions present a greater risk for the 
development of cardiovascular diseases, and PM 10 emissions are more 
strongly linked to respiratory diseases. 
11. See the National Traffic Department (Departamento Nacional 
de Trânsito), https://www.denatran.gov.br/component/content/
article/115-portal-denatran/8558-frota-de-veiculos-2018.html.
12. Technology categories contemplated in the tool are Technology 1—
Euro V, Technology 2—Euro III, Technology 3—Electric, Technology 4—
Hybrid, Technology 5—Trolleybus, Technology 6—Biodiesel B20 (20% 
biodiesel), and Technology 7—Euro VI.
13. Emissions factors (g PM/L diesel) and fuel efficiency (L or kWh/100 
km) by default per technology are Euro V, 0.07 and 59.3; Euro III, 0.30 
and 57; electric, 0 and 1.3; hybrid, 0.04 and 41.5; trolleybus, 0 and 2.29; 
biodiesel B20 (20% biodiesel), 0.06 and 57; and Euro VI, 0.03 and 
59.3. For further information on emissions factors and average fuel 
efficiency by default, please see Table 4, Data Sources Specifications. 
14. The Handbook Emission Factors for Road Transport, version 3.3, 
is published as an online software program by the German 
Environment Agency (Berlin); the Federal Office for the Environment 
(Bern, Switzerland); the Environment Agency Austria (Vienna); the 
Austrian Federal Ministry of Agriculture, Forestry, Environment and 
Water Management (Vienna); and the Austrian Ministry of Transport, 
Innovation and Technology (Vienna); the Swedish Transport 
Administration (Borlänge); the French Environment & Energy 
Management Agency (Angers); the Joint Research Centre of the

42  |  
European Commission (Ispra, Italy); and INFRAS (Bern, Switzerland). 
For more information, see https://www.hbefa.net.
15. For further information, please see linking function 2, from annual 
variations on emissions levels to annual variations on concentration 
levels, in this technical note.
16. The coefficient of determination obtained by the applied dispersion/
chemical transport models was about one for all four Brazilian 
cities. Even though this relation does not seem common for these 
metropolises, the model uses an Eulerian approach, solving the 
mass conservation equation for any tracer. The main aspect is the 
homogeneity of meteorological initial and boundary conditions for 
all scenarios and the existence of only emissions associated with the 
public transport in the chosen cities, with other emissions information 
not being used in the simulations. In addition, only primary PM 
dispersion was studied (transport, sedimentation, wet and dry 
deposition), without chemical transformations.
17. As we are unable to obtain the specific age of deaths and diseases 
(due to the predefined age ranges provided by the Department 
of Information Technology of the National Public Health System 
(Departamento de Informática do Sistema Único de Saúde, DATASUS), 
we preferred not to use the disability-adjusted life years (DALY) 
methodology. 
18. For this tool, nonfatal and fatal diseases cover respiratory and 
cardiovascular events (Chapters I and J of the ICD-10, respectively) 
because these are the most studied impacts when it comes to air 
pollution among Brazilian empirical literature. 
19. For further information on the total annual number of fatal and 
nonfatal diseases for each city’s population, covered by the public 
health system and private health system, please see Box 1.
20. It is important to note that morbidity costs can also be measured in 
terms of welfare losses, such as pain and suffering. We opted to use 
a financial measure, however, as we intended to compare such costs 
with the municipal health expenditure. For further discussion on the 
economic costs of air pollution morbidity impacts in Brazil, please see 
Ortiz et al. (2011).
21. For further discussion on national contingent valuation to assess the 
economic costs of air pollution mortality, please see Ortiz, Markandya, 
and Hunt (2009).
22. Revealed preference methods consist of the analysis of individual 
preferences based on the observation of individual behaviors in the 
market. In turn, stated preference methods consist of the analysis of 
individual preferences through interviews and questionnaires.
23. The Intergovernmental Panel on Climate Change (IPCC) projections 
for greenhouse gas (GHG) concentrations commonly used in regional 
climate models for impact projection.
24. For further discussion of the factors affecting the VSL, please see 
Alberini et al. (2016), OECD (2012), and Urvashi and Sall (2016).
25. The only epidemiological parameter obtained outside of the Brazilian 
context was retrieved from Fajersztajn et al. (2017).
26. Population data consist of an estimate of 2018 values and GDP data 
consist of an estimate of 2016 values (2018 prices), according to the 
IBGE.
27. For more information, see the National Traffic Department 
(Departamento Nacional de Trânsito), https://www.denatran.gov.
br/component/content/article/115-portal-denatran/8558-frota-de-
veiculos-2018.html.
28. According to municipal law 16.802/2018, article 50, “From the date 
of publication of this Law, the operators of collective transportation 
services by bus, members of the Urban Passenger Transportation 
System of the Municipality of São Paulo, as well as the companies that 
render services for the collection of Urban and Hospital Solid Waste 
in the Municipality of São Paulo should promote the progressive 
reduction of emissions of carbon dioxide (CO2) of fossil origin and 
of toxic pollutants emitted in the operation of their respective fleets 
through the gradual use of cleaner and more sustainable fuels and 
technologies” (Prefeitura do Município de São Paulo 2018b, article 50).
29. After meeting with the city representative of the transit department, 
SPTrans, we learned that the city intended to increase the trolleybus 
fleet by 49 buses.
30. We note once more that PM 2.5 and PM10 emissions and concentration 
variations and impacts cannot be summed because PM 2.5 is contained 
in PM10. 
31. According to the 2011 United Nations Environment Programme report, 
“Short-lived climate forcers (SLCFs): substances such as methane, 
black carbon, tropospheric ozone and many hydrofluorocarbons 
(HFCs) which have a significant impact on near-term climate change 
and a relatively short lifespan in the atmosphere compared to carbon 
dioxide and other longer-lived gases” (UNEP 2011, 7).
32. Please note that the size of the figures varied greatly in comparison 
with the actual size of the Excel sheet in order to make the 
information legible. Furthermore, the arrows in the figure are not 
in the tool and were added in the technical note to improve the 
understanding of the user.

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  43
REFERENCES
Abe, K., and S. Miraglia. 2016. “Health Impact Assessment of Air Pollution 
in São Paulo, Brazil.” International Journal of Environmental Research and 
Public Health  13 (7): 694. https://doi.org/10.3390/ijerph13070694. 
Alberini, A., A. Bigano, J. Post, and E. Lanzi. 2016. “Approaches and 
Issues in Valuing the Costs of Inaction of Air Pollution on Human 
Health.” OECD Environment Working Paper 108, OECD, Paris. https://doi.
org/10.1787/5jlww02k83r0-en.
Alonso, M.F., K.M. Longo, S.R. Freitas, R.M. da Fonseca, V. Marécal, M. Pirre, 
and L.G. Klenner. 2010. “An Urban Emissions Inventory for South America 
and Its Application in Numerical Modeling of Atmospheric Chemical 
Composition at Local and Regional Scales.” Atmospheric Environment  44 
(39): 5072–83. https://doi.org/10.1016/j.atmosenv.2010.09.013. 
Amato-Lourenço, L.F., T.C.L. Moreira, V.C. de Oliveira Souza, F. Barbosa Jr., 
M. Saiki, P .H.N. Saldiva, and T. Mauad. 2016. “The Influence of Atmospheric 
Particles on the Elemental Content of Vegetables in Urban Gardens of Sao 
Paulo, Brazil.” Environmental Pollution 216 (September): 125–34. https://doi.
org/10.1016/j.envpol.2016.05.036.
André, P .A. de, M.M. Veras, S.G.E.K. Miraglia, and P .H.N. Saldiva. 2012. “Lean 
Diesel Technology and Human Health: A Case Study in Six Brazilian 
Metropolitan Regions.” Clinics  67 (6): 639–46. https://doi.org/10.6061/
clinics/2012(06)15.
André, P .A. de, E. Vormittag, and P .H.N. Saldiva. 2017. Avaliação e valoração 
dos impactos da poluição do ar na saúde da população decorrente da 
substituição da matriz energética do transporte público na cidade de 
São Paulo. São Paulo: Instituto Saúde e Sustentabilidade. https://www.
saudeesustentabilidade.org.br/wp-content/uploads/2017/05/GP_ISS_
Relatorio_ImpactosOnibusSP-1.pdf.
BCB (Banco Central do Brasil). 2018. “Taxas de juros.” https://www.bcb.
gov.br/estatisticas/txjuros.
Beelen, R., Raaschou-Nielsen, O., M. Stafoggia, Z.J. Andersen, G. Weinmayr, 
B. Hoffmann, K. Wolf, et al., 2014. “Effects of Long-Term Exposure to Air 
Pollution on Natural-Cause Mortality: An Analysis of 22 European Cohorts 
within the Multicentre ESCAPE Project.” Lancet  383 (9919): 785–95. https://
doi.org/10.1016/S0140-6736.
Booth, H., and L. Tickle. 2008. “Mortality Modelling and Forecasting: A 
Review of Methods.” Annals of Actuarial Sciences  3 (1–2): 3–43. https://doi.
org/10.1017/S1748499500000440.
Carriazo Osorio, F. 2001. “Impacts of Air Pollution on Property Values: An 
Economic Valuation for Bogotá, Colombia.” Paper presented at the second 
workshop on Population, Economy and the Environment: Modeling and 
Simulating their Complex Interaction, Max Plant Institute for Demographic 
Research, Rostock, Germany, May 18–19. https://www.researchgate.
net/publication/255659723_Impacts_of_Air_Pollution_on_Property_
Values_an_Economic_Valuation_for_Bogota_Colombia.
Cohen, A., M. Brauer, R. Burnett, R. Anderson, J. Frostad, K. Estep, K. 
Balakrishnan, B. Brunekreef, L. Dandona, R. Dandona, V. Feigin, G. 
Freedman, B. Hubbell, A. Jobling, H. Kan, L. Knibbs, Y. Liu, R. Martin, L. 
Morawska, C. Pope, H. Shin, K. Straif, G. Shaddick, M. Thomas, R. Van 
Dingenen, A. Van Donkelaar, T. Vos, C. Murray, and M. Forouzanfar. 
2017. “Estimates and 25-Year Trends of the Global Burden of Disease 
Attributable to Ambient Air Pollution: An Analysis of Data from the Global 
Burden of Diseases Study 2015.” Lancet  389 (10082): 1907–18. https://doi.
org/10.1016/S0140-6736(17)30505-6.
Conceição, G.M. de Souza, P .H.N. Saldiva, and J. da Motta Singer. 2001. 
“Modelos MLG e MAG para análise da associação entre poluição 
atmosférica e marcadores de morbi-mortalidade: Uma introdução 
baseada em dados da cidade de São Paulo.” Revista Brasileira 
de Epidemiologia  4 (3): 206–19. http://dx.doi.org/10.1590/S1415-
790X2001000300007.
Costa, A.F., G. Hoek, B. Brunekreef, and A.C.M. Ponce de Leon. 2017. “Air 
Pollution and Deaths among Elderly Residents of São Paulo, Brazil: An 
Analysis of Mortality Displacement.” Environmental Health Perspectives  125 
(3): 349–54. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5332200/.
Detran SP (Departamento Estadual de Trânsito de São Paulo). 2019. “Frota 
de veículos em SP—por tipo de veículo.” https://www.detran.sp.gov.br/
wps/wcm/connect/portaldetran/detran/detran/EstatisticasTransito/sa-
frotaVeiculos/d28760f7-8f21-429f-b039-0547c8c46ed1?presentationtempl
ate=portaldetran%2FAT-detranPaginaODetranImpressao.
EPA (U.S. Environmental Protection Agency). n.d. “Basic Information of 
Air Emissions Factors and Quantification.” https://www.epa.gov/air-
emissions-factors-and-quantification/basic-information-air-emissions-
factors-and-quantification.
ExternE (External Costs of Energy). n.d. “The Impact Pathway Approach.” 
http://www.externe.info/externe_d7/?q=node/46. Accessed December 
2018. 
Fairburn, J., S.A. Schüle, S. Dreger, L.K. Hilz, and G. Bolte. 2019. “Social 
Inequalities in Exposure to Ambient Air Pollution: A Systematic Review 
in the WHO European Region.” International Journal of Environmental 
Research and Public Health  16 (17): E3127. https://doi.org/10.3390/
ijerph16173127.
Fajersztajn, L., P . Saldiva, L.A.A. Pereira, V.F. Leite, and A.M. Buehler. 
2017. “Short-Term Effects of Fine Particulate Matter Pollution on Daily 
Health Events in Latin America: A Systematic Review and Metaanalysis.” 
International Journal of Public Health  62 (7): 729–38. https://doi.
org/10.1007/s00038-017-0960-y.
Freitas, S.R., K.M. Longo, M.F. Alonso, M. Pirre, V. Marecal, G. Grell, R. 
Stockler, R.F. Mello, and M. Sánchez Gácita. 2011. “PREP-CHEM-SRC—1.0: A 
Preprocessor of Trace Gas and Aerosol Emission Fields for Regional and 
Global Atmospheric Chemistry Models.” Geoscientific Model Development  
4 (2): 419–33. https://doi.org/10.5194/gmd-4-419-2011.
Fundação SEADE (Sistema Estadual de Análise de Dados Estatísticos). 
2017. “Projeções demográficas 2050.”June 26. http://visualizesp.seade.gov.
br/tag/projecao-populacional/.
Fortin, P ., C. Morency, M., Trépanier. “Innovative GTFS Data Application 
for Transit Network Analysis Using a Graph-Oriented Method. Journal of 
Public Transportation.” 2016. https://scholarcommons.usf.edu/jpt/vol19/
iss4/2
Gevaerd, R., and S.R. Freitas. 2006. “Estimativa operacional da umidade do 
solo para inicialização de modelos de previsão numérica da atmosfera. 
Parte I: Descrição da metodologia e validação.” Revista Brasileira de 
Meteorologia 21 (3): 1–15.

44  |  
Gouveia, N., F.P . Corrallo, A.C.P . de Leon, W. Junger, and C.U. de Freitas. 2017. 
“Air Pollution and Hospitalizations in the Largest Brazilian Metropolis.” 
Revista de Saúde Pública  51 (December): 117. https://doi.org/10.11606/
S1518-8787.2017051000223.
Hettfleisch, K., L. Bernardes, M. Carvalho, L. Pastro, S. Vieira, S. Saldiva, 
P . Saldiva, and R. Francisco. 2017. “Short-Term Exposure to Urban 
Air Pollution and Influences on Placental Vascularization Indexes.” 
Environmental Health Perspective  125 (4): 753–59. https://doi.org/10.1289/
EHP300.
Hooftman, N., L. Oliveira, M. Maarten, T. Coosemans, and J. Van Mierlo. 2016. 
“Environmental Analysis of Petrol, Diesel and Electric Passenger Cars 
in a Belgian Urban Setting.” Energies  9 (2): 84. https://doi.org/10.3390/
en9020084.
IBGE (Instituto Brasileiro de Geografia e Estatística). 2010. “População 
residente por situação de domicílio, 2010.” https://www.ibge.gov.
br/estatisticas/sociais/saude/9662-censo-demografico-2010.
html?=&t=destaques.
IBGE. 2015. “Tabela 5795—Rendimento médio mensal nominal das 
pessoas de 15 anos ou mais de idade, com rendimento, por cor ou raça.” 
Sistema IBGE de Recuperação Automática. https://sidra.ibge.gov.br/
tabela/5795.
IBGE. 2017. “Produto interno bruto dos municípios.” https://www.ibge.gov.
br/estatisticas/economicas/contas-nacionais/9088-produto-interno-
bruto-dos-municipios.html?=&t=resultados.
IBGE. n.d.a. “Estimativas da População.” https://www.ibge.gov.br/
estatisticas/sociais/populacao/9103-estimativas-de-populacao.
html?=&t=o-que-e.
IBGE. n.d.b. “Índice Nacional de Preços ao Consumidor Amplo—IPCA.” 
https://www.ibge.gov.br/estatisticas/economicas/precos-e-custos/9256-
indice-nacional-de-precos-ao-consumidor-amplo.html?=&t=o-que-e.
Ignotti, E., S. de Souza Hacon, W.L. Junger, D. Mourão, K. Longo, S. Freitas, P . 
Artaxo, and A.C.M.P . de Leon. 2010. “Air Pollution and Hospital Admissions 
for Respiratory Diseases in the Subequatorial Amazon: A Time Series 
Approach.” Cadernos de Saúde Pública  26 (4): 747–61. http://dx.doi.
org/10.1590/S0102-311X2010000400017.
Karagulian, F., C. Belis, C. Dora, A. Prüss-Ustün, S. Bonjour, H. Adair-Rohani, 
and M. Amann. 2015. “Contributions to Cities’ Ambient Particulate Matter 
(PM): A Systematic Review of Local Source Contributions at Global 
Level.” Atmospheric Environment 120 (November): 475–83. https://doi.
org/10.1016/j.atmosenv.2015.08.087.
Lichtenfels, A.J., J.B. Gomes, P .C. Pieri, S.G.E.K. Miraglia, J. Hallak, and P .H. 
Saldiva. 2007. “Increased levels of Air Pollution and a Decrease in the 
Human and Mouse Male-to-Female Ratio in Sao Paulo, Brazil.” Fertility and 
Sterility 87: 230–40. https://doi.org/10.1016/j.fertnstert.2006.06.023.
Marcilio, I., and N. Gouveia. 2007. “Quantifying the Impact of Air Pollution 
on the Urban Population of Brazil.” Cadernos de Saúde Pública  23 (4): 
S529–36. http://dx.doi.org/10.1590/S0102-311X2007001600013. 
Martins, M.C.H., F.L. Fatigati, T.C. Véspoli, L.C. Martins, L.A.A. Pereira, M.A. 
Martins, P .H.N. Saldiva, and A.L.F. Braga. 2004. “Influence of Socioeconomic 
Conditions on Air Pollution Adverse Health Effects in Elderly People: An 
Analysis of Six Regions in São Paulo, Brazil.” Journal of Epidemiology & 
Community Health 58 (1): 41–6. https://doi.org/10.1136/jech.58.1.41.
Miraglia, S., N. Gouveia. 2014. “Costs of air pollution in Brazilian 
metropolitan regions.” Ciência e saúde coletiva , 19 (10), 4141-4147.
Miraglia, S.G.E.K., M.M. Veras, L.F. Amato-Lourenço, F. Rodrigues-Silva, 
and P .H.N. Saldiva. 2013. “Follow-Up of the Air Pollution and the Human 
Male-to- Female Ratio Analysis in Sao Paulo, Brazil: A Times Series Study.” 
British Medical Journal Open 3 (7): e002552. https://doi.org/10.1136/
bmjopen-2013-002552.
Miranda, R.M. de, M. de Fatima Andrade, A. Fornaro, R. Astolfo, P .A. 
de Andre, and P . Saldiva. 2012. “Urban Air Pollution: A Representative 
Survey of PM 2.5 Mass Concentrations in Six Brazilian Cities.” Air Quality, 
Atmosphere & Health  5 (1): 63–77. https://doi.org/10.1007/s11869-010-0124-1.
MMA (Ministério do Meio Ambiente). 2011. Inventário nacional de 
emissões atmosféricas por veículos automotores rodoviários . Brasília: 
MMA. https://www.mma.gov.br/estruturas/163/_publicacao/163_
publicacao27072011055200.pdf.
MMA. 2014. Inventário nacional de emissões atmosféricas por veículos 
automotores rodoviários . Brasília: MMA. http://www.mma.gov.br/
images/arquivo/80060/Inventario_de_Emissoes_por_Veiculos_
Rodoviarios_2013.pdf.
Moreira, D.S., S.R. Freitas, J.P . Bonatti, L.M. Mercado, N.M.É. Rosário, K.M. 
Longo, J.B. Miller, M. Gloor, and L.V. Gatti. 2013. “Coupling between the JULES 
Land-Surface Scheme and the CCATT-BRAMS Atmospheric Chemistry 
Model (JULES-CCATT-BRAMS1.0): Applications to Numerical Weather 
Forecasting and the CO2 Budget in South America.” Geoscientific Model 
Development 6 (4): 1243–59. https://doi.org/10.5194/gmd-6-1243-2013.
Nascimento, A.P ., J.M. Santos, J.G. Mill, J.B. de Souza, N.C. Reis Júnior, and 
V.A. Reisen. 2016. “Association between the Concentration of Fine Particles 
in the Atmosphere and Acute Respiratory Diseases in Children.” Revista de 
Saúde Pública 51:3. http://dx.doi.org/10.1590/s1518-8787.2017051006523.
National Research Council. 1988. Air Pollution, the Automobile, and 
Public Health . Washington, DC: National Academies Press. https://doi.
org/10.17226/1033. 
NTU (Associação Nacional das Empresas de Transportes Urbanos). 2020. 
“O transporte público por ônibus em números: Cenário nacional.” http://
www.ntu.org.br/novo/AreasInternas.aspx?idArea=7&idSegundoNivel=107. 
OECD (Organisation for Economic Co-operation and Development). 2012. 
Mortality Risk Valuation in Environment, Health and Transport Policies . 
Paris: OECD. http://dx.doi.org/10.1787/9789264130807-en.
OECD. 2014. The Cost of Air Pollution: Health Impacts of Road Transport . 
Paris: OECD. 
Ortiz, R., A. Markandya, and A. Hunt. 2009. “Willingness to Pay for Mortality 
Risk Reduction Associated with Air Pollution in Sao Paulo.” Revista 
Brasileira de Economia  63 (1): 3–22. http://dx.doi.org/10.1590/S0034-
71402009000100001.
Ortiz, R.A., A. Hunt, R. Seroa da Motta, and V. MacKnight. 2011. “Morbidity 
Costs Associated with Ambient Air Pollution Exposure in Sao Paulo, Brazil.” 
Atmospheric Pollution Research  2 (4): 520–29. https://doi.org/10.5094/
APR.2011.059.

ImpactAr Tool: Valuing Air Quality Health Impacts of Urban Bus Fleet Changes in Brazil
TECHNICAL NOTE   | November 2021  |  45
Ortiz-Durán, E.Y., and N.Y. Rojas-Roa. 2013. “Estimación de los beneficios 
económicos en salud asociados a la reducción de PM 10 en Bogotá.” 
Revista de Salud Pública 15 (1): 90–102. https://revistas.unal.edu.co/index.
php/revsaludpublica/article/view/38444/62074.
Pope, C., III. 2007. “Mortality Effects of Longer Term Exposures to 
Fine Particulate Air Pollution: Review of Recent Epidemiological 
Evidence.” Journal of Inhalation Toxicology  19 (1): 133–38. https://doi.
org/10.1080/08958370701492961.
Pope, C.A., III; and D. Dockery. 2006. “Health Effects of Fine Particulate Air 
Pollution: Lines that Connect.” Journal of the Air & Waste Management 
Association 56 (6): 709–42. https://doi.org/10.1080/10473289.2006.10464485.
Prefeitura da Cidade do Rio de Janeiro. 2018. “Balanço orçamentário.” 
http://www.rio.rj.gov.br/dlstatic/10112/9568115/4236451/
BalancoOrcamentario.pdf. 
Prefeitura do Município de São Paulo. 2018a. Demonstrativos consolidados 
(comparativos) e notas explicativas.  São Paulo: Departamento de 
Contadoria, Prefeitura do Município de São Paulo. https://www.
prefeitura.sp.gov.br/cidade/upload/02-demconsol-comparativos-notas_
explicativas-balanco2018_1552077569.pdf. 
Prefeitura do Município de São Paulo. 2018b. “Lei No. 16.802, de 17 de 
Janeiro de 2018.” LeisMunicipais, January 19. https://leismunicipais.com.
br/a/sp/s/sao-paulo/lei-ordinaria/2018/1680/16802/lei-ordinaria-n-16802-
2018-da-nova-redacao-ao-art-50-da-lei-n-14933-2009-que-dispoe-
sobre-o-uso-de-fontes-motrizes-de-energia-menos-poluentes-e-menos-
geradoras-de-gases-do-efeito-estufa-na-frota-de-transporte-coletivo-
urbano-do-municipio-de-sao-paulo-e-da-outras-providencias.
Prefeitura Municipal de Belo Horizonte. 2018. “Demonstrativo da 
aplicação de recursos em ações e serviços públicos de saúde.” 
https://prefeitura.pbh.gov.br/sites/default/files/estrutura-de-governo/
fazenda/Balan%C3%A7os/2018/12%20-%20Demonstrativo%20
da%20Aplica%C3%A7%C3%A3o%20de%20Recursos%20em%20
A%C3%A7%C3%B5es%20e%20Servi%C3%A7os%20de%20
Sa%C3%BAde.pdf.
Rivas, I., P . Kumar, and A. Hagen-Zanker. 2017. “Exposure to Air Pollutants 
During Commuting in London: Are There Inequalities among Different 
Socio-Economic Groups?” Environment International 101 (April): 143–57. 
https://doi.org/10.1016/j.envint.2017.01.019.
Rodrigues, P .C.O., S.I. Pinheiro, W. Junger, E. Ignotti, and S.S. Hacon. 
2017. “Climatic Variability and Morbidity and Mortality Associated 
with Particulate Matter.” Revista de Saúde Pública 51: 91. https://doi.
org/10.11606/S1518-8787.2017051006952.
Rodrigues-Silva, F., U. de Paula Santos, P .H.N. Saldiva, L.F. Amato-
Lourenço, and S.G.E.K. Miraglia. 2012. “Health Risks and Economic Costs 
of Absenteeism Due to Air Pollution in São Paulo, Brazil.” Aerosol and Air 
Quality Research  12: 826–33. https://doi.org/10.4209/aaqr.2011.12.0235.
Rosen, S., and T. Gayer. 2008. Public Finance . 8th ed. Boston: McGraw-Hill 
Irwin.
Roy, R. 2016. “The Cost of Air Pollution in Africa.” OECD Development Centre 
Working Paper 333, OECD, Paris. http://dx.doi.org/10.1787/5jlqzq77x6f8-en.
Roy, R., and N. Braathen. 2017. “The Rising Cost of Ambient Air Pollution 
thus far in the 21st Century: Results from the BRIICS and the OECD 
Countries.” OECD Environment Working Paper 124, OECD, Paris. https://doi.
org/10.1787/d1b2b844-en.
Sclar, R., C. Gorguinpour, S. Castellanos, and X. Li. 2019. Barriers to Adopting 
Electric Buses.  Washington, DC: World Resources Institute. https://www.
wri.org/publication/barriers-adopting-electric-buses.
Silva, L.T. da, K.C. Abe, and S.G.E.K Miraglia. 2017. “Avaliação de impacto 
à saúde da poluição do ar no município de Diadema, Brasil.” Revista 
Brasileira de Ciências Ambientais 46: 117–29. https://doi.org/10.5327/Z2176-
947820170258.
SMU (Secretário Municipal de Urbanismo e Mobilidade). 2015. Revisão do 
Plano Diretor de Niterói. Niterói: Prefeiture Niterói Urbanismo e Mobilidade. 
http://urbanismo.niteroi.rj.gov.br/wp-content/uploads/2015/09/PDDU_
CENARIOS_APRESENTACAO-AUDIENCIAS-PUBLICAS.pdf.
SPTrans (São Paulo Transporte). 2012. “Livo ecofrota.” https://www.
slideshare.net/trans_smt/livro-ecofrota?from_action=save.
Stoeldraijer, L., C. van Duin, L. van Wissen, and F. Janssen. 2013 “Impact 
of Different Mortality Forecasting Methods and Explicit Assumptions 
on Projected Future Life Expectancy: The Case of the Netherlands.” 
Demographic Research 29 (13): 323–54. https://doi.org/10.4054/
DemRes.2013.29.13.
UNEP (United Nations Environment Programme). 2011. Near-Term Climate 
Protection and Clean Air Benefits: Actions for Controlling Short-Lived 
Climate Forcers: A UNEP Synthesis Report . Nairobi: UNEP. http://hdl.handle.
net/20.500.11822/8048.
Urvashi, N., and C. Sall. 2016. Methodology for Valuing the Health Impacts 
of Air Pollution: Discussion of Challenges and Proposed Solutions.  
Washington DC: World Bank Group. http://documents.worldbank.org/
curated/en/832141466999681767/Methodology-for-valuing-the-health-
impacts-of-air-pollution-discussion-of-challenges-and-proposed-
solutions.
Watt, J., J. Tidblad, V. Kucera, and R. Hamilton. eds. 2009. The Effects of Air 
Pollution on Cultural Heritage.  Boston: Springer. 
WHO (World Health Organization). 2016. Ambient Air Pollution: A Global 
Assessment of Exposure and Burden of Disease. Geneva: WHO. https://
apps.who.int/iris/handle/10665/250141.
WHO. 2018. “Ambient (Outdoor) Air Quality and Health.” May 2. https://
www.who.int/news-room/fact-sheets/detail/ambient-(outdoor)-air-
quality-and-health. 
WHO/Europe (World Health Organization Regional Office for Europe) and 
OECD (Organisation for Economic Co-operation and Development). 2015. 
Economic Cost of the Health Impact of Air Pollution in Europe: Clean Air, 
Health and Wealth.  Copenhagen: WHO/Europe.
World Bank and IHME (Institute for Health Metrics and Evaluation). 2016. 
The Cost of Air Pollution: Strengthening the Economic Case for Action. 
Washington, DC: World Bank . http://documents.worldbank.org/curated/
en/781521473177013155/The-cost-of-air-pollution-strengthening-the-
economic-case-for-action. 
Yanagi, Y., J.V. Assunção, and L.V. Barrozo. 2012. “The Impact of Atmospheric 
Particulate Matter on Cancer Incidence and Mortality in the City of São 
Paulo, Brazil.” Cadernos de Saúde Pública 28 (9): 1737–48. https://doi.
org/10.1590/s0102-311x2012000900012.

46  | 
ACKNOWLEDGMENTS  
WRI Brasil developed the Valuation Tool for Health Impacts of Air Pollution 
(ImpactAr) with the financial support of the Children’s Investment Fund 
Foundation (CIFF).
We express our sincere gratitude to the following individuals for the 
technical expertise they provided: Marcelo Félix Alonso (UFPel), Ely José de 
Mattos (PUCRS), and Jonas da Costa Carvalho (UFPel).
Our acknowledgments to those who contributed directly or indirectly to 
the implementation of this project: Rachel Biderman, Luís Antônio Lindau, 
Rafael Barbieri, Talita Esturba, and Luiza de Oliveira Schmidt.
Thanks also to the internal and external reviewers: Ajay Singh Nagpure, 
Anne Dorothée Slovic, Arya Harsono, Guillermo Petzhold, Heloant Souza, 
Matt Whitney, Ronaldo Serôa da Motta, Seth Contreras, Washington Junger, 
and Walter de Simoni. 
ABOUT THE AUTHORS
Luana Priscila Betti is the Urban Economics Coordinator at WRI Brasil.
Contact: luana.betti@wri.org
Marina Caregnato Garcia  is an Urban Economics Analyst at WRI Brasil.
Contact: marina.garcia@wri.org
Eduardo Siqueira is an Urban Mobility Analyst at WRI Brasil.
Contact: eduardo.siqueira@wri.org
Henrique Evers is the Urban Development Manager at WRI Brasil.
Contact: henrique.evers@wri.org
Copyright 2021 World Resources Institute. This work is licensed under the Creative Commons Attribution 4.0 International License.
To view a copy of the license, visit http://creativecommons.org/licenses/by/4.0/.
ABOUT WRI BRASIL  
WRI Brasil is a research institute that transforms big ideas into actions 
to protect the environment and foster Brazil’s prosperity in an inclusive 
and sustainable fashion. It is focused on research and applications of 
sustainable solutions oriented towards climate, forests, and cities. WRI 
Brasil combines technical excellence with political articulation and works 
in close collaboration with governments, private companies, universities 
and civil society.
WRI Brasil is part of World Resources Institute (WRI), a global research 
organization whose work extends to over 50 countries. WRI encompasses 
the work of almost 1000 professionals in off  ices in Brazil, China, the United 
States, Mexico, India, Indonesia, Europe, Turkey and Africa.
ABOUT CIFF
The Children’s Investment Fund Foundation (CIFF) is an independent 
philanthropic organization with off  ices in Addis Ababa, Beijing, London, 
Nairobi, and New Delhi. Established in 2003, CIFF works with a wide 
range of partners seeking to transform the lives of children and 
adolescents across the world. CIFF’s areas of work include maternal and 
child health, adolescent sexual health, nutrition, education and income 
generation, child protection, and supporting smart ways to slow down 
and stop climate change.
