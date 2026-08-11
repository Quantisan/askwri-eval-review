Goal: 

Build eval query sets for a cross-lingual RAG system
* 207-doc corpus
* 169 en, rest zh/es/pt). 
* Queries always written in English regardless of source doc language. 


Method: 
Working one document (or twin-pair) at a time: 
* read doc. 
* manually generate high-level English queries whose expected answer is this
document 
* This document's `document_id` is useful for `Cite` mode.
* Write draft answers to the questions as well. 
    * This will be useful in the future for evaluation of `Answer` mode. 
* Do not attempt to capture chunks or excerpts at this stage. 

--

### doc review 1

```
document_id: 00be4a1d-33cc-4b56-a4d5-d15af0a5cc27
external_id: 2025_zero-emission-heavy-duty-trucks_00015
title: 驶向2035: 中国新能源重卡在区域与长途运输场景中的推广潜力研究
language: zh
```

Possible English twin: 
7c2e200e-9c01-4acd-b5ef-a18041a7f258
"Charging toward 2035: Policies to accelerate zero-emission heavy-duty trucks in China's regional and long-haul freight" (en)

Query: "What is the projected market penetration rate of new energy heavy-duty trucks in China through 2035?"
* There are three scenarios -- no policy, current policy, and enhanced policy. 
* No-policy scenario: regional transport reaches 2%–17% penetration by MY2030; long-haul stays at a nascent, low level all the way through MY2035.
* Current-policy scenario: the trade-in subsidy lifts long-range BEV semi-tractor penetration in regional transport to ~10% by MY2027.
* Enhanced-policy scenario (current + enhanced combined): regional transport penetration exceeds 50% during MY2027–2030; long-haul growth stays slow until a sharp acceleration in MY2032–2035, implying sustained policy support is needed through 2035 for long-haul to reach meaningful levels.

Query: "How does total cost of ownership compare between battery electric and diesel heavy-duty trucks in China?"
* BEVs are more cost-competitive than diesel in regional transport and are projected to dominate there.
* The TCO/capex gap is larger for heavy cargo trucks (载货汽车) than for semi-tractors, because cargo trucks suffer bigger payload losses and diesel cargo trucks already have lower baseline purchase/energy costs.
* Concrete capex gap (short-range BEV vs. diesel heavy truck): CNY 150k–260k (MY2027) narrows to CNY 35k–120k with the trade-in subsidy, then widens back above CNY 130k once that subsidy ends in 2028, not dropping below CNY 100k again until MY2030.

Query: "What is the difference in zero-emission truck adoption potential between regional transport and long-haul transport scenarios?"
* Regional transport moves much faster toward competitiveness: BEV semis hit a 5-year payback by MY2027 with subsidies, and penetration crosses 50% by MY2027–2030 under enhanced policy.
* Long-haul lags substantially: nascent under no-policy through MY2035; even with enhanced policy, real growth only emerges MY2032–2035.
* Technology split also differs: BEVs dominate regional transport; in long-haul, BEVs work best for shorter-daily-mileage, low-time-sensitivity, light-cargo routes, while fuel-cell trucks (FCEVs) are more competitive for long-daily-mileage, time-sensitive, heavy-cargo routes.

Query: "What are the payback periods for battery electric semi-trucks compared to diesel trucks in China?"
* The study defines competitiveness thresholds as ≤5-year payback for regional transport and ≤4-year payback for long-haul. 
* With the trade-in subsidy, long-range BEV semi-tractors reach the 5-year payback threshold by MY2027 — three years earlier than the no-policy case.
* The vehicle purchase-tax exemption alone is not enough to make BEV semis competitive during MY2025–2027.
* In long-haul, by MY2035 both BEV and FCEV heavy cargo trucks on shorter-daily-mileage routes approach roughly a 5-year payback. 


### doc review 2

98cc253e — "How Dockless Bike Sharing Affects Cities"

```
document_id: 98cc253e-8d96-4499-b67a-38baffe2f3f2
external_id: 2020_dockless-bike-sharing_00124
title: 共享单车如何影响城市
language: zh
```

possible english twin: 
416a01af-1c79-4db1-a356-182f0577f844 
"How Dockless Bike Sharing Changes Lives: An Analysis of Chinese Cities" (en)

Queries
* "What share of bike-share trips replace private car, taxi, or ride-hailing trips in China?"
* "How much CO2 emissions reduction is attributed to bike-sharing in China?"
* "How does dockless bike-sharing affect travel behavior in Chinese cities?"

expected_documents: {98cc253e-8d96-4499-b67a-38baffe2f3f2, 416a01af-1c79-4db1-a356-182f0577f844}

Query: "What share of bike-share trips replace private car, taxi, or ride-hailing trips in China?"
* Based on survey data from 8,218 bike-share users across 12 Chinese cities.
* 54% of bike-share users use bike-sharing to connect with other transport modes; of those, 91% of that connecting use is to link with public transit.
* Across the 12 cities, 17%–45% of bike-share trips replaced private motorized trips — including private cars, taxis, ride-hailing, and motorcycles.

Query: "How much CO2 emissions reduction is attributed to bike-sharing in China?"
* Most bike-share trips substitute for walking or public transit trips (not emissions-reducing), but the portion that substitutes for private motorized trips does reduce emissions.
* That substitution effect reduces CO2 emissions by approximately 4.8 million tonnes per year.
* The report frames this as equivalent to the annual CO2 absorption of about 6.8 million acres of forest.

Query: "How does dockless bike-sharing affect travel behavior in Chinese cities?"
* The study found high consistency in travel-behavior effects across all 12 cities, despite differing economic/social development levels.
* 54% of users ride to connect with other transport modes, primarily public transit (91% of connecting trips).
* 17%–45% of bike-share trips (varying by city) displace private motorized trips (cars, taxis, ride-hailing, motorcycles).
* Overall, the report frames bike-sharing as a "last-mile" solution that both strengthens public transit connectivity and substitutes for short private-vehicle trips — changing the broader urban mobility ecosystem, not just individual trip choices.

### doc review 3 

```
document_id: e36cae4c-c6fb-441b-adf0-f43e2aec9ad9
external_id: 2024_optimizing-container-ports-transportation-and_9894
filename: 2024_shenzhen-port-low-carbon-transport_00130.pdf
title: 优化集装箱港口运输与配送系统迈向低碳未来：深圳港案例研究
language: zh
```

Queries: 
* Can Yantian Port realistically meet the mode-shift targets set in Shenzhen's Master Plan (2035), or would it require more aggressive measures than a "stated policy" trajectory?
* What are the barriers to expanding rail-water intermodal transport (road-to-rail) at Yantian Port?
* How much would well-to-wheel CO2 emissions decline if drayage truck electrification reached 95% by 2035 at Yantian Port, and how does that compare to rail and water mode-shift measures?

expected_documents: {e36cae4c-c6fb-441b-adf0-f43e2aec9ad9}

Query 1: "Can Yantian Port realistically meet the mode-shift targets set in Shenzhen's Master Plan (2035)...?"
* The scenario analysis found it would be very difficult for Yantian Port to reach the Master Plan (2035) mode-shift targets without aggressive measures.
* Under the "Stated_policy" (realistic/conservative) scenario, the port cannot reach the targets by either 2025 or 2035; roadways would still account for the majority of throughput.
* Only the "Enhanced_policy" scenario assumes the targets are met: by 2035, railways and waterways combined account for over 50% of port throughput (roadway share drops to 35%, waterway to 45%, railway to 20%).
* Even in the Stated_policy scenario, 2025 shows almost no progress — WTW CO2 emissions fall only 1% versus 2022, and road throughput actually rises 5% above 2022 levels.
* Conclusion: achieving the Enhanced_policy targets requires aggressive short-term action (e.g., accelerating the Yantian-Pinghunan railway retrofit), since the Stated_policy trajectory alone is insufficient.

Query 2: "What are the barriers to expanding rail-water intermodal transport (road-to-rail) at Yantian Port?"
* Rail infrastructure capacity: the Yantian-Pinghunan railway (built 1994) is a single non-electrified track with low capacity, handling only ~1% of Yantian Port's container throughput as of 2022.
* The parallel Pingnan railway serving the western port area was actually demolished to make way for Qianhai district road network construction.
* Unstable/limited cargo sources: rail freight volumes are inconsistent, so railways don't prioritize container shipments, causing unreliable empty-container allocation, scheduling, and delivery times.
* Cost: rail "door-to-door" pricing (~3,290 RMB, Yantian to Qingyuan) is higher than trucking (~2,200 RMB) under current pricing mechanisms, though trunk-line rail discounts (50–60%) and subsidies (200 RMB/TEU) can nearly close the gap.
* Time competitiveness: rail transport takes nearly 3 days (container pickup to return) versus 1 day for trucking, due to marshalling/decoupling steps and dependency on train scheduling, empty wagons, and loading slots.
* Retrofitting is underway: the Yantian-Pinghunan railway upgrade (to double-track, electrified, 120 km/h) began construction in December 2022, targeting completion around 2027.

Query 3: "How much would WTW CO2 emissions decline if drayage electrification reached 95% by 2035...?"
* In the Enhanced_policy scenario with only 15% battery-electric truck penetration (the base assumption), WTW CO2 emissions fall 50% versus 2022.
* If drayage truck electrification is pushed to 95% fleet penetration by 2035 (assuming truck energy consumption also improves to 100 kWh/100km and Greater Bay Area grid emission factors drop to 0.36 tonnes CO2/MWh), WTW CO2 emissions would fall 71% versus 2022.
* Contribution breakdown to the 2035 Enhanced_policy reduction (from a 2035 BAU baseline of 392 million tonnes... actually in 10,000-tonne units: baseline 392, ~10,000t):
    * Road-to-rail: −195 (10,000 tonnes) — the single largest contributor
    * Road-to-water: −66 (10,000 tonnes)
    * Zero-emission drayage (95% scenario): −71 (10,000 tonnes) — becomes the second-largest measure, surpassing road-to-water
    * Net result: 95 (10,000 tonnes) remaining in 2035, i.e., a 71% cut from 2022's 332 (10,000 tonnes)
* At the more conservative 15% electrification assumption, the drayage measure only cuts ~1 (10,000 tonnes) — negligible — because so few trucks are converted and the electric truck's per-km WTW advantage over diesel is only ~7% under 2022 grid/efficiency assumptions.

### doc review 4

```
document_id: 987353ab-9454-473f-8f00-eb767750dd24
external_id: 2022_impactos-economicos-pandemia-covid19-transporte-publico_0070
filename: 2022_impactos-economicos-pandemia-covid19-transporte-publico_0070.pdf
title: IMPACTOS ECONÓMICOS DE LA PANDEMIA DE COVID-19 EN EL TRANSPORTE PÚBLICO URBANO EN CIUDADES MEXICANAS
language: es
```
queries: 
* "How did public transport demand in Mexican cities change during the COVID-19 pandemic?"
* "What methodology was used to estimate COVID-19 financial impacts on Mexican urban public transport operators?"
* "How many jobs depend on the public transport sector in Mexico?"

expected_documents: {987353ab-9454-473f-8f00-eb767750dd24    } 

**Query: "What methodology was used to estimate COVID-19 financial impacts on Mexican urban public transport operators?"**
* Three methodological approaches: surveys of AMAM mobility authorities (15 member states, surveys in March and May 2020); interviews and workshops with 10 operating companies (20 key informants, plus follow-up workshops in September, November and December 2021); and financial estimates for the 76 cities/metropolitan zones with over 100,000 inhabitants.
* Operators classified three ways — public vs. private, company vs. individual concession, and fleet condition — with fleet renewal percentage used as a proxy for financial resilience, yielding categories of renewal above 50%, below 50%, and ECI.
* Data sources varied by mode: public financial statements for trains, cable cars and trolleybuses; published cost-benefit analyses for BRT; INEGI (2021) for passenger figures; interview-based extrapolation across 75 metropolitan zones for buses and ECI, generating IKB (bus-kilometer) and IPB (passengers-per-bus) indices.
* Key assumptions: average fare of 7 and 7.5 Mexican pesos nationally, all buses diesel-powered, and — for ECI — supply falling in the same proportion as demand. Research ran June–December 2020 with World Bank support, covering April 2020–September 2021.

**Query: "How many jobs depend on the public transport sector in Mexico?"**
* More than 410,000 direct jobs depend on the sector, principally drivers of transport units (WRI México estimate based on interviews with mobility authorities; AMAM 2020).
* Significant indirect employment comes from individuals, small and medium enterprises, and cooperatives, which make up around 75 percent of the sector's organization.
* Before the pandemic, roughly 50 million people used collective public transport as their first mobility option — 87 percent of Mexico's economically active population (SEDATU 2016).
* Secondary pandemic impacts included loss of purchasing power for thousands of drivers and auxiliary personnel; private companies negotiated salary reductions of 20–30 percent, with cuts reaching 50 percent in some cases.

### Doc review 5

```
document_id: 2e5d79b9-7077-43a2-bc48-3661e7d3fd36
external_id: 2023_analisis-de-los-mecanismos-financieros-para-la_3765
filename: 2023_analisis-mecanismos-financieros-sostenibilidad-transporte_0087
title: Análisis de los mecanismos financieros para la sostenibilidad del transporte público en ciudades mexicanas
language: es
```

Queries
* What barriers limit fondeo and financiamiento for urban public transport in Mexico?
* Why is revenue from Mexico's carbon tax not currently available for public transport, and how could that change?
* How much revenue do parking meters generate in Mexican cities, and where does that money go?

**Query: "What barriers limit *fondeo* and *financiamiento* for urban public transport in Mexico?"**
* The document distinguishes the two: *fondeo* refers to potential revenues generated by the government entity's own action (its source is public administration itself), while *financiamiento* refers to the capital structure underpinning a project — resources captured externally to the government body.
* Barriers to *fondeo*: scarcity of budget resources; public transport projects are not always treated as a priority; and a lack of integration in defining transport public policy across planning, design, strategy, actions and budget.
* Barriers to *financiamiento*: limited access due to numerous requirements or rigorous selectivity; inflexible credit conditions in terms and rates; and financing mechanisms that are little known or used in Mexico.
* A cross-cutting constraint: public transport is not, and has not been, legally considered a priority for budget allocation (SHCP 2020); adopting new mechanisms requires political will and cross-sector support. Fare revenue and complementary subsidies remain the most important financing source in Mexico, leaving supply vulnerable to demand shifts.

**Query: "Why is revenue from Mexico's carbon tax not currently available for public transport, and how could that change?"**
* Mexico's carbon tax has applied since January 2014 under the Special Tax on Production and Services law (IEPS), incorporated in 2013; each fossil fuel carries a different rate according to its carbon dioxide content, determined by the annual CO2 emission potential released on combustion.
* All revenue collected goes into the country's general budget and is not earmarked for any specific use. Through February 2020 cumulative collection reached 41,336 million pesos, an amount that has declined annually since 2014, which could limit project development from this source.
* At the private sector's request, the tax does not apply to natural gas or jet fuel (turbosina). SHCP frames the tax as serving two central objectives: reducing emissions and increasing federal revenue.
* The document proposes assigning these revenues to finance a National Public Transport Financing Program, linking revenue from a polluting source to projects that help mitigate greenhouse gases. More generally, specific earmarking of any contribution requires provision in tax law or in the sector-specific (mobility or transport) law — absent such provision, contributions flow by default into the general collection pool.
* 2020 carbon tax rates ranged from 7.48 centavos per liter for propane to 16.99 for fuel oil, and from 19.72 pesos per tonne for petroleum coke to 50.32 for other fossil fuels.

**Query: "How much revenue do parking meters generate in Mexican cities, and where does that money go?"**
* In Mexico City, approximately 30 percent of the amount collected through parking meters is directed to executing improvement works, with the remainder distributed to the companies carrying out collection. Ecoparq revenues are tracked from 2012 onward.
* In the municipality of Guadalajara, collection shifted from physical meters to a virtual process via a technological application: in 2017, the last year of traditional meters, total collection was 12 million pesos across 6,000 devices; in 2018 virtual meters brought in 15 million pesos across 2,665 parking spaces.
* Parking charges are classified as revenue from the use of public goods, applied at the local (state/municipal) level. Collection capacity is inherently limited by the number of regulated spaces available. Reference cases include CDMX, Guadalajara, Zapopan and Tonalá.
* Revenues captured under these concepts can be concentrated in local public finances and, by law, assigned to a specific purpose such as public transport projects. The document notes implementation and maintenance costs must not exceed revenues received, and that transparent application and distribution schemes are needed.
* By contrast, urban road pricing or congestion charging does not exist in Mexico as a revenue source for public transport, though the document identifies it as an opportunity to explore.

### doc review 6 

expected_documents: {987353ab-9454-473f-8f00-eb767750dd24, 2e5d79b9-7077-43a2-bc48-3661e7d3fd36 } 

**Query: "How did public transport demand in Mexican cities change during the COVID-19 pandemic?"**
* Demand fell by up to 70 percent in April–June 2020, the period of greatest national restrictions; the most significant shifts in mobility patterns occurred in those months.
* Reduction factors by mode (share of pre-pandemic demand) in April–June 2020: BRT 29%, trains 33%, trolleybuses/companies 45%, ECI 45% — recovering by June–September 2021 to 69%, 56%, 65% and 65% respectively.
* Trains cut supply far less than demand (97% of 2019 kilometers offered in April–June 2020), maintaining coverage to reduce vehicle occupancy; BRT supply fell to 61% in the same period.
* By September 2021, systems had still not recovered: BRT demand at 71 percent and buses/trolleybuses at 68 percent of 2019 ridership.

