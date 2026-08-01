---
doc_id: 2024_open-e-bus-blueprint_4307
source_pdf: kp-docs/askwri-kps/2024_open-e-bus-blueprint_4307.pdf
extraction_method: cache-plaintext
char_count: 99099
title: Open E-Bus Blueprint
authors: Mulukutla, Pawan; Pai, Madhav; Bhat, Rajit K.; Bachu, Prashant; Dubedi, Avinash; Varma, Dr Pramod; Nair, Sujith; Sinha, Anirban
date_published: 10/30/2024
article_type: Working Paper
sub_tag: Transport decarbonization
wri_primary_office: WRI India
wri_programs: Cities
language: English
url: "https://wri-india.org/research/open-e-bus-blueprint"
doi: "https://doi.org/10.46830/wriwp.24.00042"
summary: "The \"Open E-Bus Blueprint\" outlines a framework for electrifying India's bus fleet, aiming to transition 800,000 buses to electric by 2030. It emphasizes leveraging Digital Public Infrastructure (DPI) principles to create a standardized, vendor-agnostic system that enhances communication and integration among stakeholders, thereby reducing costs and improving operational efficiency. The paper identifies challenges such as fragmented operations and the need for clear information standards, proposing a collaborative approach to address these issues. By fostering innovation and scalability, the blueprint aims to facilitate a smoother transition to electric buses and associated infrastructure."
---

# Open E-Bus Blueprint

WORKING PAPER  |  Version 1.0  |  October 2024  |  1
TABLE OF CONTENTS
Executive summary ....................... 2
Introduction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .3
Pressing reasons for action ............... 5
Digital public infrastructure—  
An approach to population-  
scale complex problems ................. 10
Use cases for open e-bus  
blueprint in the DPI ecosystem ........... 19
Implementing open e-bus blueprint. . . . . 22
Conclusion .............................. 23
Glossary ................................ 24
Abbreviations ........................... 25
Endnotes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
References ............................... 27
Acknowledgments ...................... 32
About the authors. . . . . . . . . . . . . . . . . . . . . . . 32
Working Papers contain preliminary research, analysis, 
findings, and recommendations. They are circulated to 
stimulate timely discussion and critical feedback, and 
to influence ongoing debate on emerging issues.
Suggested Citation: Bhat, R.K., A. Sinha, P . Bachu, 
S. Nair, R. Prakash, P . Mulukutla, A. Dubedi, M. Pai 
and P . Varma.,2024. “Open e-bus blueprint” Working 
Paper. WRI India and FIDE.  
https://doi.org/10.46830/wriwp.24.00042
HIGHLIGHTS
 ▪ With the unprecedented success of bus electrification in India and our 
broader goal of 30 percent electric vehicle (EV) penetration by 2030, we 
have an opportunity to electrify over 8 lakh buses.
 ▪ Given the different dynamics of operating electric buses – along with 
legacy communication issues in India’s bus sector – a digitalized system of 
managing bus operations is a potential game changer in this transition.
 ▪ India has been a pioneer in using Digital Public Infrastructure (DPI) to 
resolve systemic problems at scale. This paper frames the concept of the 
open e-bus blueprint for e-bus service platforms based on successful 
DPI principles.
 ▪ Key benefits include shifting from specific technologies to foundational 
building blocks, allowing scalable e-bus infrastructure while empower-
ing innovators and stakeholders to contribute and benefit from the 
e-bus transition.
 ▪ The paper curates the principles, key elements, and potential use-cases 
of the open e-bus blueprint, offering a framework for wider stake-
holder discussion. 
WORKING PAPER
Open e-bus blueprint
WRI India - Rajit K Bhat, Pawan Mulukutla, Prashanth Bachu, Avinash Dubedi, and Madhav Pai  
FIDE - Dr. Pramod Varma, Sujith Nair, and Anirban Sinha

WORKING PAPER  |  October 2024  |  3
Open e-bus blueprint
2  |  
  
EXECUTIVE SUMMARY
Context
Buses play a vital role in India’s transportation system, serving 
millions of passengers daily across urban and rural areas. As 
part of a broader strategy to reduce emissions and improve pas-
senger services, India plans to electrify up to 800,000 buses over 
the next seven years, a transition involving public, private and 
institutional fleet operators. The government is creating policies 
and partnerships that aim to reimagine contracting and operat-
ing models for buses. 
The transition from internal combustion engines (ICE) to 
EVs poses both opportunities and challenges in the complex 
bus transportation system. It will require an approach that 
can manage the added complexities of batteries replacing ICE, 
charging stations replacing fuel pumps, and renewable energy 
replacing conventional fuels. In addition, current bus opera-
tions and maintenance systems were designed in isolation 
from one another. They are not integrated in ways that support 
communication across stakeholders—passengers, operators, 
manufacturers, financiers, and regulators. This disjointed setup 
results in delays and higher operational costs and hinders the 
cost-effective and sustainable deployment of EV buses at scale. 
Two key challenges impede progress: The absence of standards 
for exchanging information limits seamless communication and 
integration, and persistent information silos limit visibility and 
stakeholders’ ability to fully understand the system and take 
informed action. A more connected and unified digital ecosys-
tem could help overcome these challenges. 
India’s experience deploying Digital Public Infrastructure 
(DPI) in other sectors reveals why this approach holds so 
much promise. It combines open technology standards, gov-
ernance frameworks, and a stakeholder ecosystem to drive 
innovation. The DPI approach has demonstrably reduced costs 
and improved accessibility to services across sectors like bank-
ing, payments, e-commerce, and healthcare. Whether it could 
help address the unique challenges of transitioning to e-buses 
remains an open question, but one that should be explored.
About this working paper
In this working paper, WRI India and FIDE seek to frame 
and contextualize the challenges the bus transport system will 
confront amid the complexities of a large-scale digital transi-
tion. It finds that, despite the technological solutions available, 
the absence of standards and limited observability- the ability of 
stakeholders to access, monitor, and analyze information - can 
drive up costs and hinder scalability. Proprietary systems from 
various vendors are tough to integrate and upgrade, making it 
harder to effectively find and use limited resources, improve 
operations, and increase transparency and accountability. 
The paper proposes a novel approach that leverages DPI 
principles to guide bus electrification and a roadmap for 
translating this blueprint into reality. To ensure effective 
implementation, the “open e-bus blueprint” requires interaction 
across a wide range of stakeholders, including passengers, e-bus 
operators, original equipment manufacturers (OEMs), charge 
point operators (CPOs), financial institutions, government 
agencies, and technology-energy-mobility service providers. 
We invite and seek to enable wider stakeholder comments and 
consultation on strategic and functional considerations to 
design an “open e-bus blueprint” for e-bus service platforms 
based on DPI principles. The goal is to cater to the diverse 
needs of key groups involved and prepare a smooth roll-out of 
e-buses at scale with the associated infrastructure and services.
Key findings
Business-as-usual approaches based on proprietary vendor 
technologies, lock in inefficiencies and make integrating and 
upgrading systems harder. Traditional bus operations depend 
on various systems, such as those for Vehicle Location and 
Tracking (VL T), Automatic Fare Collection (AFC), and fleet 
management. E-buses require new services for energy manage-
ment, battery health, charging schedules, and power purchase 
contracts. If standards for exchanging information are not clear, 
if each vendor must develop its own proprietary solutions, with 
no opportunity to share, and integrate these, costs for technol-
ogy and upgrades will be far higher than necessary. 
Transformative outcomes seen in India’s DPI efforts come from 
careful planning. In identity, banking, payments, e-commerce, 
and healthcare, these outcomes were not simply the result of 
isolated technological solutions but stemmed from a systemic 
approach that focused on creating foundational digital building 
blocks that were available to the ecosystem. In this case, ecosys-
tem refers to a complex network of actors and their services that 
interact with and rely upon others to function effectively. The 
small interventions that created these building blocks allowed 
different actors in the ecosystem, both public and private, to 
innovate and create scalable solutions, proving that doing 
less can, in fact, achieve more. By rethinking the bus sector 
through the DPI model, we can envision a core framework that 
integrates technology architecture, governance, and market-
driven innovation.
The open e-bus blueprint, based on DPI principles, presents 
a vendor-agnostic and specification-driven architecture that 
enables observability (the ability to monitor and understand 
a system’s state by analyzing its outputs, performance metrics, 
and logs) as well as easier integration of solutions from various 
providers. This reduces costs, simplifies system-wide integration, 
and ensures smoother operations while allowing flexibility for 
future technological upgrades. 
The paper analyzes real-world use cases (descriptions of how 
ecosystem actors interact with services, systems, or business in a 
real-world scenarios) for various stakeholders. It showcases the 
blueprint’s versatility in achieving goals such as using market 
demand to guide infrastructure development, mobilizing finance, 
building capacity, to name a few. 
INTRODUCTION 
Setting the stage
Buses are the backbone of public transportation in India, serving 
around 39.9 Crores (399 million) passengers daily and account-
ing for over 90 percent of all public transport trips1 (see Figure 
1). As the primary mode of public transportation nationwide, 
they provide millions of Indians with affordable and acces-
sible mobility. However, the sector is highly fragmented, with 
numerous small operators and a lack of coordination, leading to 
inefficiencies that hinder its ability to scale and meet growing 
demand. Their central role underscores the need to strengthen 
and modernize the bus sector to enhance India’s public 
transport system.
Figure 1  |  Role of buses in India’s public transport
Source: Based on information collated from Gadepalli et al. 2024; TOI Education 2023; 
Press Information Bureau, GoI 2024; Ministry of Civil Aviation 2024; De et al. 2017.
The Government of India is increasingly recognizing the role 
of enhanced bus systems in reducing emissions and improving 
passenger experiences. Central to India’s sustainable transporta-
tion strategy is the rapid adoption of electric buses (e-buses). 
India is aspiring to electrify a significant portion of its 23 lakh 
(2.3 million) bus fleet, with up to 800,000 buses estimated to be 
electrified by 2030 (Mukherjee and Mishra 2023). This aligns 
with the country’s broader goal of achieving a 30 percent EV 
market share, a transition involving public, private and institu-
tional fleet operators (Press Information Bureau, GoI 2024a). 
The government is supporting this transition through various 
policies and partnerships (Press Information Bureau, GoI 2023; 
Press Information Bureau, GoI 2024b).
The transition is not just about adopting new technology but 
also about rethinking contracting and operating models to 
run these buses cost-effectively. It shifts from the traditional 
approach where the government procures and operates buses, 
towards greater involvement of the private sector through 
public-private partnerships (PPPs). By leveraging the private 
sector’s strengths in financing and operational efficiency, this 
approach seeks to reduce the burden on government resources 
and enables many small and medium-sized cities to initiate and 
expand bus services, thus accelerating the transition to sustain-
able transportation.
While the transition to electric buses offers significant envi-
ronmental benefits, the legacy structure of India’s bus system 
presents several challenges that hinder progress. Ninety-three 
percent of buses are privately owned (for rural, intercity, and 
fleet operations—school, employee, tourist transport, and other 
use cases) and over 90 percent of operators manage fewer 
than five buses. So, the sector is highly fragmented, leading 
to inefficiencies and a lack of scale (Mulukutla and Rajagopal 
2024). This fragmentation creates a low-growth environment 
where operators have little leeway or incentive to expand. Their 
small size constrains the types of investments and technology 
upgrades they can afford. For small operators, transitioning to 
e-buses is particularly challenging because, in addition to the 
already high cost of the buses, they must also invest in expensive 
charging infrastructure. The lack of a widespread public charg-
ing network forces them to set up their own charging stations, 
which can add 10-15 percent to the cost of each e-bus, making 
adoption economically unsustainable (CSTEP 2021). 
In addition, integrating digital technology into traditional bus 
operations requires combining various information technology 
(IT) systems, including vehicle location and tracking, ticket-
ing, passenger information, contracts, and fleet management. 
The current reliance on proprietary solutions not based on open 
technology and data standards limits IT’s potential to improve 
1%  Air
2%  Metro
6%  Train
91% BusesDaily passenger trips

WORKING PAPER  |  October 2024  |  5
Open e-bus blueprint
4  |  
  
operations (Bachu, Roy, and Roychowdhury 2024). This can lead 
to higher costs, increased vendor dependency, and difficulties in 
integration and future upgrades, for instance, forcing operators 
to switch between hardware vendors for bus tracking or upgrad-
ing the ticketing system to Bharat Bill Pay Standards.2 These 
challenges hinder operations and service quality. With e-buses 
come new challenges in several key areas: planning for e-bus 
deployment and charging infrastructure, establishing financing 
and procurement mechanisms, and monitoring and evaluating 
operations. Managing charging infrastructure, navigating power 
contracts, ensuring effective energy management, and addressing 
battery health and degradation all pose challenges (Sclar et al. 
2019). Together, these complexities underscore the need for a 
standardized, alternative approach to digital technology that can 
efficiently accommodate emerging needs. 
Lastly, the fragmented bus sector limits multi-sectoral align-
ment: the ability for multiple sectors and stakeholders to 
collaborate to reach common goals. Fragmented and/or miss-
ing information can prevent secondary stakeholders—beyond 
bus operators—from participating. This includes experts in 
energy, finance, insurance, and mobile phone applications. These 
stakeholders could play a crucial role in the large-scale rollout 
of e-buses and the associated infrastructure and services while 
benefiting from the opportunities this transition presents.
Achieving India’s e-bus transition targets will require a con-
certed effort across the entire stakeholder ecosystem, and at 
the same time, this transition offers an opportunity for these 
stakeholders to rethink buses and ways this sector can tap the 
potential of something it has missed out on so far: the signifi-
cant digital innovations taking place in India. 
India’s experience in deploying Digital Public Infrastructure 
(DPI) demonstrates its promise. DPI is an approach that shifts 
focus from providing technology solutions to providing founda-
tional digital building blocks to enable broader, more inclusive 
innovation (CDPI 2024a). These building blocks include shared 
specifications and frameworks that support multiple use cases 
and stakeholders in the ecosystem. DPI fosters vibrant market 
innovation and has demonstrably reduced costs and improved 
accessibility to services across sectors like banking, payments, 
e-commerce, and healthcare in India (Gupta et al. 2024; 
Mohanty 2023). 
While the bus sector poses specific challenges, could DPI hold 
the key to unlocking sustainable mobility through the large-
scale deployment of e-buses in India? There are reasons to 
suggest it could. Creating a high-trust, low-cost ecosystem for 
key stakeholders—commuters, bus operators, original equip-
ment manufacturers (OEMs), financial institutions, government 
agencies, and technology service providers3—could enable them 
to co-develop and implement cost-effective, market-driven 
strategies for deploying e-buses along with the necessary infra-
structure and services.
Objective
The primary objective of this working paper is to identify key 
challenges and opportunities in extending DPI principles to 
e-bus transition and adoption.
It proposes a new blueprint for designing e-bus service plat-
forms based on DPI principles and referred to as the open e-bus 
blueprint (see Digital Public Infrastructure—An Approach to 
Population-Scale Complex Problems) that addresses major chal-
lenges in transit operations and service. 
We invite stakeholder comments and consultations on strategic 
and functional considerations for designing this technology 
blueprint. Its implementation roadmap are designed to stimu-
late discussion rather than present final recommendations. 
WRI India and the Foundation for Interoperability in Digital 
Economy (FIDE) understand that there might still be gaps with 
respect to practical implementation. 
Approach for developing this working 
paper
This working paper employs a qualitative research methodology, 
combining unstructured interviews with a comprehensive review 
of secondary literature. 
A review of the academic literature, government consultation 
papers, think-tank reports, articles, and blogs were conducted 
with focus on the following:
1. Technology implementation challenges in public transport 
and corresponding policy recommendations.
2. Systemic issues with current technology deployments in 
Indian public transport agencies.
3. DPI implementation experiences in other sectors.
4. DPI principles and architectural considerations derived from 
diverse sectoral applications.
To ensure data reliability and credibility, we focused primarily 
on English national dailies and reputable think-tank blogs to 
illustrate real-world examples of challenges and successes.
We conducted unstructured interviews with key stakehold-
ers involved in public transportation, IT , and policymaking to 
gather qualitative data on their perspectives and experiences. 
We applied thematic analysis to the secondary literature to 
identify recurring themes, patterns, and critical insights related 
to DPI implementation challenges, policy implications, and 
potential solutions.
We combined these methods to provide a comprehensive 
understanding of the potential and challenges associated with 
extending DPI principles to e-bus transition and adoption.
Scope of the paper
This paper outlines WRI India and FIDE’s current thinking on 
how a proposed open e-bus blueprint could create an ecosystem 
for software applications that accelerate the adoption of e-buses 
and related infrastructure services. The blueprint is designed 
to be versatile, not only supporting e-buses but also extending 
seamlessly to non-electric buses, thereby broadening its scope 
and applicability across the entire bus sector. 
The Introduction describes the current fragmented vendor-led, 
non-interoperable approach to bus operations and service deliv-
ery which cannot handle the complexities and scale required for 
the transition. 
The second section, “Pressing reasons for action”, highlights 
legacy and emergent issues in the current bus ecosystem. It 
explains the need for a digital technology blueprint for devel-
oping applications for e-bus and related services based on 
DPI principles. 
The third section, “Digital Public Infrastructure,” discusses the 
DPI principles and India’s experience with DPI. It explains how 
interoperability with open standards and protocols catalyze the 
innovation in and leverage the power of digital infrastructure to 
build scalable solutions. It discusses the design principles and 
key digital functionalities that highlight the essential capabilities 
for the blueprint. 
The fourth section, “Potential use cases for various stakehold-
ers,” showcases the versatility of the blueprint and its ability to 
integrate with existing digital public infrastructure to enable a 
dynamic ecosystem of solution providers.
The last section, “Rolling out the open e-bus blueprint—A 
tactical roadmap,” discusses a series of strategic actions needed 
to bring the open e-bus blueprint from idea to reality.
PRESSING REASONS FOR 
ACTION
The bus transport ecosystem is a complex network involving a 
wide range of stakeholders, each with unique needs and require-
ments, as laid out in Table 1:
Table 1  |  Key stakeholders and their needs in the bus transport ecosystem
STAKEHOLDER DESCRIPTION BROAD NEEDS
Bus operators
70+ public bus companies operating about 150,000 buses a
With over 26,000 small and large private operators, the market is 
largely fragmentedb
Maximize bus utilization by efficiently managing fleet 
operations, maintaining cost-effective practices, and 
integrating new technologies
Device manufacturers (buses)
Vehicles are equipped with devices such as tracking units, 
electronic ticketing machines, cameras, ticket validators, onboard 
units, and wi-fi systems, either pre-installed or retrofitted
Ensure seamless communication and interoperability 
between onboard systems for reliable information 
broadcasting
Financial institutions Banks, insurance companies, and non-banking financial institutions 
providing financing for buses and their operations
Assurance of financial stability, risk management, and 
return on investment through reliable operations
Government ministries
Multiple ministries (MoRTH, MoHUA, MHI, MoP) and government 
bodies (ASRTU, CESL CMVR-TSC, BEE) involved in regulating and 
supporting the sector
Regulatory compliance, safety standards, and 
the promotion of sustainable and efficient public 
transport systems

WORKING PAPER  |  October 2024  |  7
Open e-bus blueprint
6  |  
  
Each stakeholder has distinct needs, ranging from operational 
efficiency and financial returns to passenger satisfaction and 
regulatory compliance, as depicted by Figure 2. However, cur-
rent bus operation systems have historically been designed as 
standalone solutions, lacking the integration and communica-
tion necessary to meet these diverse requirements effectively.
These isolated systems weren’t designed for broader communica-
tion between various information sources as shown in Figure 
3. They rely on separate IT services, create bottlenecks, and 
highlight the following two challenges:
Standards: The absence of a consistent and interoperable frame-
work for bus operations across different information systems and 
organizations impedes seamless communication and integration 
within the transport network.
Observability: Limited access to relevant information sustains 
silos, preventing stakeholders from gaining full system visibility 
and making informed decisions.
This fragmented landscape hampers not only efficiency 
but innovation. 
Figure 2  |  Fragmented bus ecosystem
/gid00017/gid00028/gid00046/gid00046/gid00032/gid00041/gid00034/gid00032/gid00045/gid00046
/gid00016/gid00017/gid00006/gid00019/gid00002/gid00021/gid00016/gid00019/gid00001/gid00132
/gid00021/gid00020/gid00017/gid00046
/gid00020/gid00021/gid00002/gid00012/gid00006/gid00009/gid00016/gid00013/gid00005/gid00006/gid00019
/gid00006/gid00004/gid00016/gid00020/gid00026/gid00020/gid00021/gid00006/gid00014
/gid00007/gid00036/gid00041/gid00028/gid00041/gid00030/gid00036/gid00041/gid00034
/gid00016/gid00006/gid00014/gid00046
/gid00004/gid00017/gid00016/gid00046
/gid00006/gid00041/gid00032/gid00045/gid00034/gid00052/gid00001/gid00043/gid00045/gid00042/gid00049/gid00036/gid00031/gid00032/gid00045/gid00046
/gid00163/gid00163/gid00163
/gid00163/gid00163/gid00163
/gid00163/gid00163/gid00163
/gid00163/gid00163/gid00163
/gid00016/gid00017/gid00006/gid00019/gid00002/gid00021/gid00016/gid00019/gid00001/gid00133/gid00016/gid00017/gid00006/gid00019/gid00002/gid00021/gid00016/gid00019/gid00001/gid00134
/gid00022/gid00046/gid00032/gid00045/gid00001/gid00008/gid00045/gid00042/gid00048/gid00043/gid00001/gid00134/gid00022/gid00046/gid00032/gid00045/gid00001/gid00008/gid00045/gid00042/gid00048/gid00043/gid00001/gid00133/gid00022/gid00046/gid00032/gid00045/gid00001/gid00008/gid00045/gid00042/gid00048/gid00043/gid00001/gid00132
Source: Authors’ analysis.
Note: TSPs is Technology Service Providers. OEMs is Original Equipment Manufacturers. 
CPOs is Charge Point Operators.
Problem of standards 
Standardizing information flow for bus operations has not 
been a priority in India. Traditionally, bus systems have come 
up with a patchwork of solutions to manage operational data 
(route network, passenger count, schedules, stops) and passenger 
information (Real-time data, PIS boards, timetable, etc.) This 
fragmented landscape creates the following problems: 
Larger bus agencies or fleet owners: These often rely on 
proprietary systems tailored to specific needs, where hardware 
and software are bundled together, allowing vendors to impose 
proprietary protocols and operations and management contracts. 
The absence of standards leads to a lack of interoperability 
within and outside the agency, resulting in vendor lock-in 
(Bachu, Roy, and Roychowdhury 2024). This limits opera-
tors’ ability to choose optimal solutions and complicates the 
Figure 3  |  Information sources and existing technology 
gaps in bus operations
INFRASTRUCTURE
VEHICLE 
HEALTH 
MONITORING
ABSENCE OF 
DATA STANDARDS
LIMITED 
OBSERVABILITY 
OF INFORMATION
+
TICKETING 
& VALIDATION
FLEET 
TRACKING
TRANSIT 
SERVICE 
PLAN
Source: Authors’ analysis.
Other players
App developers, Intelligent Transport System (ITS) providers, 
advertisers, charge point operators, and energy and mobility 
service providers
Access to accurate and timely data for service 
enhancement, innovation, and revenue generation 
through advertising, apps, and energy services
Passengers The end-users who rely on accurate and timely information for their 
journeys
Access to accurate, real-time trip information, safety, 
and a reliable, user-friendly travel experience
Original equipment manufacturers 
(OEMS) and components 
manufacturers
Bus, bus components – sensors, software and system providers
Fulfill operator requirements by ensuring compatibility 
with various operational systems, feedback on 
product performance, and the ability to integrate their 
equipment seamlessly into diverse fleet environments
 Sources: (a) ASRTU 2024, (b) Banerjee 2022.
Box 1  |  Learnings from previous experience
The Intelligent Transport System (ITS) initially emerged as a 
promising solution for public transit agencies seeking improved 
operational efficiency and reliability. ITS encompasses a range of 
technologies offering real-time tracking, smart ticketing, and inte -
grated information systems for planning and scheduling. It prom -
ised a future of empowered commuters and data-driven operations. 
However, these deployments faced challenges.
Despite investments exceeding Rs 1,000 crore ($120 million) across 
multiple Indian cities, achieving value addition and capturing 
essential operational data proved difficult. These systems struggled 
to consistently generate usable data. Consequently, bus operators 
continued relying on manual methods.
Existing ITS implementation faces the following challenges that 
hinder their effectiveness and investment potential:
Flawed procurement model
 ▪ One-time purchase model : Funds are often spent on single-
time technology purchases rather than continuous services 
that include maintenance and updates. This is like buying a 
smartphone you can never upgrade, leading to outdated tech 
over time.
 ▪ All-in-one vendor bundling : Hardware, software, and 
services are often bundled with one vendor, creating conflicts 
of interest—like hiring a builder who’s responsible for design, 
construction, and inspection. This setup reduces quality control 
and flexibility.
Siloed systems
 ▪ Isolated data limits functionality : Each ITS system (tracking, 
ticketing, etc.) operates separately, preventing them from 
working together. For example, if real-time tracking isn’t 
connected to ticketing, users can’t get live schedule updates.
 ▪ Vendor lock-in : Proprietary solutions mean only the original 
vendor can service or update the system, which drives up costs 
and reduces flexibility over time.
Limited oversight and management
 ▪ Lack of monitoring and reporting : Often, there’s little 
tracking of whether the technology is performing well, which 
makes it hard to identify issues. For instance, without regular 
reports, agencies may not know if GPS trackers on buses are 
faulty or if ticketing systems are creating bottlenecks, leaving 
them with an incomplete picture of service quality.
 ▪ No transition planning for technology end-of-life : Without 
planning for when systems become outdated, agencies face 
service interruptions when technology fails. 
 ▪ Restricted data access : Limited ability to access or share 
data makes it harder for agencies to use data in decision-
making. For example, without comprehensive access to tracking 
and ticketing data, agencies struggle to make informed choices 
about adding routes or adjusting schedules to meet demand.
Source: Bachu, Roy, and Roychowdhury 2024.
Table 1  |  Key stakeholders and their needs in the bus transport ecosystem (continued)

WORKING PAPER  |  October 2024  |  9
Open e-bus blueprint
8  |  
  
networks, applications, and platforms, while policies ensure 
data gathering aligns with specific needs of the stakeholder, is 
securely managed, and is retained appropriately. 
The purpose of observability is to ensure that all relevant infor-
mation about the bus is available to stakeholders for informed 
decision-making. This leads to the following benefits:
 ▪ Improved service delivery: Operators can provide timely 
service and updates to passengers, reducing downtime, and 
enhancing the overall experience.
 ▪ Reduced risk: End-to-end visibility minimizes exposure 
to avoidable risks, such as equipment failure, operational 
inefficiencies, and revenue leakage for operators, financial 
institutions, and OEMs.
 ▪ Lower operational costs: Observability helps organizations 
identify and address inefficiencies quickly and reduce 
operational costs, such as reducing downtime and avoiding 
costly repairs with predictive maintenance. It also helps with 
optimizing route planning, forecasting revenue, and budget 
management and cost control.
The lack of observability harms passengers, operators, and other 
stakeholders alike. 
Implications
Discovery issues for passengers 
Inconsistent standards and poor observability make it difficult 
for passengers to search and discover bus services, as follows:
 ▪ Public buses often suffer from unreliability in their services. 
Non-standardized data on bus schedules, limited options 
with ticketing and payments, and long wait times make it 
difficult for passengers to plan trips effectively. 
 ▪ The lack of integration with other modes of transport and 
shared mobility services creates a fragmented network. This 
limits the effectiveness of bus-based public transport, making 
it less attractive than private vehicles despite potentially 
lower fares (Rollison, Caitlin, and Matthew Coombes. 2023). 
 ▪ These issues discourage ridership, particularly on less-
frequented routes and consequently weaken the cause for the 
operator to expand services with additional buses.
Utilization challenges for operators
Poor observability and lack of data standards limits the efficient 
utilization of bus as a resource. This can manifest the following:
 ▪ Planning inefficiencies: Due to limited observability of 
bus performance, bus operators cannot estimate charging 
infrastructure requirements. This constrains service coverage 
and route planning, leading to inefficient resource allocation 
and underutilization of e-buses. In Nagpur, for example, 34 
percent of the electric bus fleet remained idle due to a lack of 
charging stations (Chakraborty 2024).
 ▪ Scheduling inefficiencies: Without consistent information 
exchange on bus tracking, crew and bus schedules, passenger 
counts and network information, route planning and 
scheduling becomes cumbersome and potentially inefficient. 
 ▪ Gaps in passenger information: Inconsistent data formats 
block a unified view of bus operations, hindering resource 
allocation and smooth service. Passengers experience this 
in Delhi, where one of the operators, DIMTS’ proprietary 
application Poocho (offering real-time information for 
cluster buses) is unable to integrate with another operator, 
Delhi Transport Corporation’s systems, leaving most buses 
with static route and schedule data that may not be up to 
date (Abisla 2019).
 ▪ Stifling of innovative models and sustainability: 
Observability extends beyond data—it’s about fostering 
innovation and sustainability by enabling policy interventions 
that leverage digital infrastructure within the transportation 
network. For instance, in Telangana, repurposing school 
buses for passenger transport faced roadblocks as there 
was no system in place to assess and adjust risk for such a 
unique use case, which made it challenging for insurers to 
justify lower insurance premiums for buses used as passenger 
vehicles during off-hours (The Times of India 2019).
Poor visibility in public-private partnerships in bus opera-
tions such as leasing buses on a gross cost contract (GCC)6 or 
net cost contract (NCC)7—where agencies partner with private 
operators to manage and maintain buses—causes friction 
between public agencies, operators, and other stakeholders in the 
following (Kharwal and Khandelwal 2021):
 ▪ Managing contracts and service levels. This requires 
strong contract management and performance monitoring 
systems in place to ensure timely payments, service quality, 
and compliance with contractual obligations. Poor visibility 
and data validation have led to significant friction between 
bus operators and agencies, resulting in disputes and 
service disruptions.
 ▪ Bankability. Lack of clear, real-time data on bus operations, 
payment statuses, and contract compliance prevents creditors 
from accurately assessing performance and risks, which 
diminishes investor confidence in bus operators, limiting the 
flow of capital into the bus sector.
 ▪ Financing challenges in e-buses. Without accurate 
data, the financial viability of e-bus investments remains 
uncertain, deterring potential investors and slowing the 
adoption of e-buses. Investors require reliable data on asset 
quality, particularly battery performance and degradation, 
to assess risk and make informed decisions. This data gap 
hinders understanding of total cost of ownership (TCO), 
operational efficiency, and repayment ability. For instance, 
research points out that a 20 percent reduction in battery life 
can increase TCO by 2.2 percent. This effect is magnified 
as reduced battery range (10-30 percent decrease) leads to 
further TCO increases of 13-30 percent. These figures can 
vary significantly across geographies due to differences in 
climate, terrain, and usage patterns. However, without real-
world data on battery performance, investors can’t predict 
future maintenance costs or battery lifespan. This uncertainty 
discourages investment, even when it might be financially 
viable, because the risk of unexpected costs remains too high 
(Vijaykumar et al. 2020). 
 ▪ Estimating demand. Limited real-world data on e-bus 
operations, particularly in India, hampers understanding of 
factors like battery degradation and operational efficiency 
(Kumar, Mulukutla, and Doshi 2023). For example, slower 
charging times for e-buses reduces their hours of service each 
day, meaning that a larger fleet may be needed to match daily 
service hours of a diesel fleet and avoid disrupting city-wide 
replacement plans.
Future impacts of low observability 
Limited observability in bus operations poses significant chal-
lenges as fleet sizes and passenger demand grow. The absence 
of comprehensive visibility restricts operational scalability and 
hinders the full potential of buses within a broader transport 
ecosystem, leading to trust issues and aligning stakeholder 
incentives to contribute and benefit from increased bus adop-
tion. Several instances have highlighted this.
Ultimately, these inefficiencies not only affect bus operators but 
also have ripple effects across the entire ecosystem, hindering 
the development of a connected, efficient, and sustainable bus 
transport system.
How to confront these problems  
Implementing isolated technological solutions will not solve 
these looming problems. An alternative paradigm that looks at 
creating a robust, foundational digital infrastructure could be 
helpful for achieving sustainable and scalable outcomes.
integration of new technologies. For example, in Bengaluru, a 
crisis forced the public bus operator BMTC to revert to paper 
tickets from electronic ticketing machines (ETMs) because the 
intelligent transport systems (ITS) provider refused to repair or 
replace failing ETMs. Locked into a proprietary system, BMTC 
had no other options (Philip 2019). 
Smaller agencies or fleet owners: These struggle with manual 
methods like handwritten logs and spreadsheets (Ministry of 
Housing And Urban Affairs, GoI 2020).
Standardization ensures that bus operation data remain con-
sistent and accessible for passengers, operators, and other 
intermediaries. Aligning different systems enables various 
applications to work seamlessly together. Here’s how stan-
dardization helps:
 ▪ Provides a common structure and format: By adopting 
a universal format (like Network Timetable Exchange 
[NeTEx]4 or General Transit Feed Specification [GTFS]5), 
data from different systems, like GPS trackers and ticketing 
apps, becomes easier to integrate. For instance, when arrival 
times and ticketing systems use the same format, it’s possible 
to book and track live location accurately for passengers 
across apps/or platforms.
 ▪ Maintains data usability over time: Standardized data 
ensures that historical information remains readable and 
compatible, even as technologies evolve. For example, 
route performance data from a decade ago can still inform 
planning if the format hasn’t changed, helping operators see 
trends and adjust future schedules.
 ▪ Enhances data quality: Consistent formats reduce errors and 
remove duplicates, improving the accuracy of each data point. 
For example, standardizing how GPS coordinates are logged 
across buses ensures that location updates aren’t conflicting 
or missed, resulting in reliable real-time information.
Problem of observability 
Observability helps various stakeholders in the bus ecosystem 
to monitor and understand the performance of bus opera-
tions, infrastructure, and services by examining critical data 
points—such as vehicle location, ticketing transactions, charger 
utilization, battery health, and schedule adherence, etc.—
through outputs, logs, and other performance metrics. 
Observability is achieved through a combination of tools and 
policies: Application programming interfaces (APIs) or software 
applications gather and aggregate data from different systems,

WORKING PAPER  |  October 2024  |  11
Open e-bus blueprint
10  |  
  
DIGITAL PUBLIC 
INFRASTRUCTURE—AN 
APPROACH TO POPULATION- 
SCALE COMPLEX PROBLEMS
The DPI model
In the realm of national development, the significance of DPI is 
comparable to that of physical infrastructure like roads and rail-
ways. Just as roads and railways form the backbone of physical 
connectivity and drive socio-economic activities, DPI provides 
the foundational digital building blocks that fuel sustainable 
innovation in the digital space. 
The DPI movement is inspired by the open standards and speci-
fications that created the Internet and mobile networks, which 
operated as the original digital infrastructure of the late 20th 
century, catalyzing a wave of public and private innovation that 
drove inclusion (CDPI 2024a). The DPI model illustrates an 
approach to solving socio-economic problems at scale. (See Box 
2 for more details on how the Internet became an early example 
of the DPI model.) 
At its core, a DPI integrates three key elements: 1) minimalist 
technology interventions, including the right technology archi-
tecture and standards for information exchange, 2) governance 
frameworks that are transparent, accountable, and participatory, 
and 3) a robust environment for both public and private sector 
innovation (CDPI 2024a). 
Over the last decade, India has championed the development 
and deployment of several DPIs. Guided by certain key prin-
ciples they ensure that the minimalist technology interventions 
are effective, inclusive, and scalable.
DPI principles
The development of DPIs in India is grounded in the 
philosophy of collaboration among three key sectors: the gov-
ernment—“Sarkar,” the market—“Bazaar,” and society—“Samaj” 
(Nilekani 2022). This tripartite model emphasizes the impor-
tance of each sector working in harmony to achieve common 
goals. It champions the idea that public infrastructure should 
be open, accessible, and governed by principles that ensure it 
serves the public interest first and foremost. For instance, the 
United Payments Interface (UPI) protocol developed by the 
National Payments Corporation of India (NPCI) for instant 
real-time payments to facilitate inter-bank transactions through 
mobile phones ensured that technology service providers gave 
citizens an affordable and secure means of digital payment for 
all types of transactions—whether between people, businesses, 
or government—all powered by the same protocol that allows 
for interoperable payments. The protocol is agnostic to payment 
devices, currency, or type of transaction (CDPI 2024b).
Systems designed to facilitate the substantial expansion of such 
design principles across sectors can promote inclusivity. Figure 4 
gives a brief description of the general principles for a DPI-led 
approach (CDPI 2023). 
Thus, rather than building bespoke solutions for each use 
case, DPIs employ reusable building blocks that can be com-
bined to serve multiple purposes. These principles enable 
DPIs to achieve societal outcomes such as fostering inclusive 
innovation, enhancing user choice, scaling service delivery, 
accelerating speed, building public trust, and promoting com-
petition—all while prioritizing data sovereignty and ensuring 
cost effectiveness.
Box 2  |  Case: Internet architecture and “the hourglass design”– achieving more with less 
The hourglass model is a powerful analogy for minimalist technology 
interventions, exemplified by the design of the Internet. At its core 
is the Internet Protocol (IP), an algorithm which acts as a universal 
intermediary, as depicted in Figure B2. IP connects a wide range of 
software applications on one end with diverse underlying services for 
information transfer on the other, facilitating efficient communication 
across networks.
Pre-internet era: Complexity in communication. Before the Inter -
net, applications like email were network specific in design, requiring 
dedicated connections between computers within a network. Each 
network required the applications to be configured uniquely, making 
cross-network communication complex and inefficient.
Post-internet: Communication simplified. With the IP as the 
common core, applications and physical services now only need to 
interface with IP, streamlining communication and significantly reduc -
ing complexity.
This model illustrates how a strong, central, and interoperable core, 
exemplified by the IP, can support a wide range of software and hard -
ware systems. It shows how a principle-based minimalist intervention 
not only addresses current challenges but also establishes a flexible 
core that can adapt to future needs.
FIGURE B2  |  Hourglass model: Rethinking technology
GAMES
VOICE 
OVER IPWEB EMAIL
BROADBAND WIFI ETHERNET WIDE/hyphen.capAREA
NETWORK
CELLULAR 
NETWORK
CHAT
VIDEO
STREAMING
THE INTERNET AS 
EXPERIENCE
INTERNET PROTOCOL
AS A COMMON STANDARD
THE SUPPORTING 
TECHNOLOGIES
Source: Georgia Institute of Technology 2011.
Figure 4  |  Distinguishing DPI from regular digitization 
efforts: Key principles
 
Designed to foster high trust and low 
costs for both public and private entities. 
MINIMALIST, REUSABLE 
BUILDING BLOCKS 
T o promote and ensure value derived 
by the participants is not locked in a 
particular platform/system liberates 
the members.
INTEROPERABILITY
Open access enables innovation by both 
“challenger”market players and 
incumbents, focusing on solutions for 
diverse problems and requirements. 
DIVERSE, INCLUSIVE INNOVATION  
T echnology should be a catalyst to 
the ecosystem and not a gatekeeper. 
Instead of concentrating power 
within one particular or a handful of 
participants.
FEDERATED & DECENTRALIZED 
Design systems with optimal 
ignorance—each system should know 
as little as possible, ensuring high 
auditability and traceability through 
digitally signed data, non-repudiable 
change logs, and authenticated 
transaction trails.
SECURITY & PRIVACY 
Source: CDPI 2023.

WORKING PAPER  |  October 2024  |  13
Open e-bus blueprint
12  |  
  
global leader in digital transactions, accounting for 46 percent of 
the world’s total (Press Information Bureau, GoI 2024b). With 
over 500 million users, UPI now processes more than 14 billion 
transactions monthly, worth over INR 20 trillion, all while 
maintaining secure and vendor-neutral operations (Business 
Standard 2024). 
Building block for sharing financial data 
The Account Aggregator framework launched by the Reserve 
Bank of India (RBI) streamlines the secure sharing of financial 
data between service providers and users and is expanding access 
to a wide range of financial services for consumers and busi-
nesses. By allowing users to consolidate and securely share their 
financial data, the framework offers several benefits: faster loan 
approvals, personalized financial services, and improved financial 
planning. It also reduces paperwork and eliminates the need for 
repeated KYC processes by making use of other building blocks, 
such as Aadhaar for identification and UPI for secure payments. 
Designed based on the principles of interoperability, consent-
based sharing, security, and privacy at its core, the framework 
has simplified financial processes, lowered costs, and enhanced 
consumer security, integrating over 2.2 billion financial accounts 
and creating new socio-economic opportunities (DoFS 2024).
The contrast between India before and after DPIs is a compel-
ling story of transformation, as depicted in Figure 5. 
These transformative outcomes were not simply the result of 
technological solutions but stemmed from a systemic approach 
that prioritized foundational digital infrastructure on which the 
solutions could operate. By focusing on minimalist but robust 
and flexible digital building blocks for identity, payments, and 
sharing financial data, India empowered its ecosystem actors 
to innovate and develop scalable solutions, driving widespread 
socio-economic progress—demonstrating that by doing less, 
more can be achieved.
Figure 5  |  India’s DPI story 
AADHAAR IDS ISSUED
/one.cap/three.cap/eight.capCR /parenleft.cap/one.cap./three.cap/eight.cap BN/parenright.cap
TRANSFERRED ON UPI IN FY/two.cap/zero.cap/two.cap/three.cap
INR
/one.cap/four.cap/two.cap./nine.capLAKH CR
/parenleft.cap/dollar.cap/one.cap./seven.cap TN/parenright.cap
DIRECT BENEFIT TRANSFER
/three.cap/two.cap./seven.capLAKH CR
INR
/parenleft.cap/dollar.cap/three.cap/eight.cap/nine.cap BN/parenright.cap
eKYC DONE
/one.cap/seven.cap/zero.cap/zero.capCR /parenleft.cap/one.cap/seven.cap BN/parenright.cap
/one.cap/two.cap/zero.cap/zero.cap
MONTHLY UPI TRANSACTIONS
CR
~
/parenleft.cap/one.cap/two.cap BN/parenright.cap
AADHAAR AUTHENTICATIONS
OVER
/one.cap/zero.cap,/zero.cap/zero.cap/zero.cap CR /parenleft.cap/one.cap/zero.cap/zero.cap BN/parenright.cap
INDIA
STACK
Immediate 
Payment 
Service
eKYC
Aadhaar Pay
Aadhaar 
Enabled 
Payment 
System
Unified 
Payment 
Interface
Sources: Based on data retrieved from official dashboards  (DBT Bharat 2024; NPCI 2024; Aadhaar 2024; D’Silva et al. 2019).
India’s digital public ecosystem—  
The story so far
India has effectively utilized these principles and scaled up the 
use of DPIs in fields such as identification (ID), payments, 
data exchange systems, and transactions to deliver vital services 
to its citizens. 
Building block for identity
Aadhaar, India’s national identification system, assigns a 12-digit 
unique ID to each resident based on their demographic and 
biometric information and has issued credentials to over 1.36 
billion individuals, providing low-cost authentication and 
electronic know your customer (eKYC) services (Aadhaar 2024). 
Aadhaar’s design provides inclusion with minimal data (collect-
ing only essential details to avoid exclusion errors), a federated 
model with one-way linkage (ability to link to other systems and 
not collect data from them), an ecosystem approach (stan-
dardized interfaces for authentication with public and private 
partners), and privacy by design. 
These core principles have significantly expanded its impact 
(UIDAI, GoI 2014). Beyond its government applications, 
these principles have unleashed a wide range of private sector 
innovations, accelerating access to formal financial systems and 
affordable services in health, education, and consumer services. 
The combination and synergies between the trinity of JanDhan 
(bank accounts), Aadhaar, and mobile phones, made it possible 
for a huge swath of India’s population to access its financial 
system for the first time. It allowed the government to target 
delivery of government subsidies to identified beneficiaries. 
Between 2011 and 2017 nearly half a billion adults opened bank 
accounts. A study by the Bank for International Settlements 
notes that this progress, which took 9 years since Aadhaar’s 
launch, would have taken 47 years using traditional methods 
(D’Silva et al. 2019). 
Aadhaar’s architecture empowers government departments 
and entrepreneurs to innovate and scale digital applications 
and services efficiently. By employing secure data storage and 
consent mechanisms, Aadhaar supports ecosystem growth while 
ensuring security and cost effectiveness.
Building block for payments
The United Payments Interface (UPI) has revolutionized 
digital payments in India with its open, mobile-first system 
that is modular, secure, and interoperable across banks. The 
participation of private players to build solutions using UPI has 
accelerated the adoption of digital payments, making India the 
Note: 1 USD = INR 84

WORKING PAPER  |  October 2024  |  15
Open e-bus blueprint
14  |  
  
Figure 6  |  Underlying elements of DPI model
GOVERNANCE 
FRAMEWORK
COMPOSABILITY
INTEROPERABILITY
INNOVATORS BUILD SOLUTIONS WITH THE 
BLOCKS UPON A SOLID FOUNDATION LAID BY 
GOVERNANCE FRAMEWORKS
Each independent block, 
when put together, creates 
bigger blocks that allow 
innovators to build upon a 
common base
Diﬀerent blocks /f_it together 
seamlessly, enabling smooth 
connections and operations 
despite diﬀerent designs/builders
INNOVATORS
 
Source: Authors’ analysis.
Open e-bus blueprint: DPI approach to 
bus ecosystem  
The transformative potential of the DPI model, with its 
emphasis on minimalist technology interventions and systemic 
approaches in the form of building blocks, offers a compelling 
case for reimagining the bus ecosystem. These interventions are 
minimalist because they focus on core functions—such as data 
exchange standards and specifications, simple protocols, and 
lightweight architectures—that can be extended or built upon 
without over-specifying or locking in particular technologies. 
The current fragmented and isolated systems in bus operations 
resemble the pre-Internet era’s communication challenges—
complex, inefficient, and limiting. By rethinking the bus sector 
through the DPI model, we can envision a core framework that 
integrates technology architecture, governance, and market-
driven innovation, as illustrated by Figure 6. Much like the 
Internet’s hourglass design, or other DPIs like Aadhaar and 
UPI, which provide basic frameworks that are adaptable and 
interoperable, the bus sector can benefit from establishing a 
foundational infrastructure that supports its diverse stakehold-
ers and their needs, allowing future innovations and evolving 
technologies to integrate seamlessly. 
This blueprint has the potential to address current inefficiencies 
and create a flexible, scalable foundation for the e-bus transi-
tion and future growth. This would enable the bus sector to 
enhance stakeholder collaboration, align incentives, and drive 
the transition to a cleaner, more efficient system while creating 
a conducive environment for deploying the infrastructure for 
800,000 e-buses.
Box 3  |  Case: Regulatory intent and India’s banking transformation—Lessons for the public bus system
In the late 1980s, with the rise of personal computers and the Internet, 
the RBI recognized the need to modernize banking operations for 
greater efficiency and economic growth. Banks began adopting 
various technology systems to digitize and automate their processes, 
leading to the installation of multiple, often incompatible, software 
applications across branches, sometimes even within the same bank.
This fragmented approach resulted in high costs and complexity, as 
vendors provided proprietary solutions to bank branches; for instance, 
previously, transactions took a day to reflect because each branch 
had its own server, sending data to the central system only at the end 
of the day. This approach led to high costs and complexity, as propri -
etary systems were challenging to integrate or upgrade. Recognizing 
these issues, the RBI stepped in with a clear regulatory mandate: the 
implementation of a unified Core Banking Solution (CBS) across all 
commercial banks. This regulatory intent not only streamlined opera -
tions but also enabled a wave of financial innovation, demonstrating 
how proactive governance can shape the success of digital infrastruc -
ture initiatives.
Source: Hariharan and Reeshma 2015; Fathima 2015.
In rethinking the bus ecosystem through the lens of a DPI, 
we can envision a blueprint built using a series of modular 
building blocks, as illustrated in Figure 7. These building 
blocks—whether platforms, protocols, pieces of code, or 
applications—are like Lego pieces: each one is independently 
functional, but when connected, they create a strong and adapt-
able foundation. Just as different Lego pieces snap together 
to build countless structures, these digital blocks interconnect 
seamlessly with other DPIs, supporting the essential services the 
bus ecosystem relies on. 
For example, core building blocks like scheduling, ticketing, and 
tracking specifications can seamlessly integrate with other DPIs, 
such as the Open Network for Digital Commerce (ONDC)8 
and UPI for payments, as seen in Figure 8. Imagine a passenger 
being able to search, book, and pay for bus rides directly from 
any app on the ONDC network, using their familiar UPI app 
to complete payments. This integration enables passengers to 
plan trips across multiple modes of transport, view real-time bus 
tracking, and buy tickets—all in one place. With standardized 
protocols, providers can develop Mobility-as-a-Service (MaaS) 
Figure 7  |  Reimagining India’s bus ecosystem with the DPI model
FLEET TRACKING 
SPECIFICATIONS
ENERGY 
MANAGEMENT
SCHEDULING 
SPECIFICATIONS
TRANSPORT WORKFORCE 
REGISTRIES
TICKETING 
SPECIFICATIONS
ALL THE BUILDING BLOCKS 
/parenleft.capLIKE VEHICLE HEALTH, 
BATTERY INFORMATION/parenright.cap FIT 
TOGETHER SEAMLESSLY , 
EMPOWERING INNOVATORS TO 
BUILD SCALABLE SOLUTIONS
VEHICLE HEALTH 
SPECIFICATIONS
BATTERY 
INFORMATION
Source: Authors’ analysis.
©LEGO Group. This graphic is not authorized or sponsored by the LEGO Group.

WORKING PAPER  |  October 2024  |  17
Open e-bus blueprint
16  |  
  
Figure 8  |  Open e-bus blueprint: The DPI for bus ecosystem
TRANSPORT WORKFORCE 
REGISTRIES
TRACKING 
SPECIFICATIONS
BATTERY 
INFORMATION
TICKETING 
SPECIFICATIONS
SCHEDULING 
SPECIFICATIONS
 VEHICLE HEALTH 
SPECIFICATIONS
BUILDING 
BLOCKS
ACTORS
APPLICATION 
L AYER
CHARGE POINT 
OPERATORS
ENERGY
PROVIDERS
TECHNOLOGY/hyphen.capENERGY/hyphen.cap
MOBILITY SERVICE 
PROVIDERS
GOVT MINISTRIES/ 
CITY AGENCIES/ 
REGULATORS
BUS OPERATORS OTHER EQUIPMENT 
MANUFACTURERS
PASSENGERSFINANCIAL 
INSTITUTIONS
Diverse stakeholders 
needing collaboration and 
multisectoral alignment to 
bene/f_it from building blocks
Speci/f_ications for 
common ground in 
software code, registries, 
platforms, and 
applications that 
are composable, 
interoperable, and 
scalable
Private sector innovating by 
leveraging /f_inancial strength, tech 
expertise, and service delivery
CHARGING 
MANAGEMENT 
APPLICATION
MOBILITY 
AS A 
SERVICE
DRIVER
 PERFORMANCE 
TRACKING
Source: Authors’ analysis.

WORKING PAPER  |  October 2024  |  19
Open e-bus blueprint
18  |  
  
apps that connect to the ONDC network, making it easier for 
users to find and book transport options, get real-time travel 
updates relayed by bus, and switch seamlessly between transit 
types. For bus operators, such apps can provide data to help 
adjust bus routes and schedules to meet demand efficiently, 
without extra overhead. As we develop this infrastructure, 
keeping the guiding principles for these building blocks in mind 
is essential to ensure flexibility, interoperability, and accessibil-
ity for all users.
Open e-bus blueprint: Core design 
principles 
For a DPI approach to succeed in the bus ecosystem in India, it 
must be robust, adaptable, and scalable. While the foundational 
DPI principles discussed earlier still apply, the following core 
design principles are additional and specific to the unique needs 
of the bus ecosystem. These include the following: 
 ▪ Vendor-agnostic, specification-driven architecture. The 
architecture of the solutions should be based on well-defined, 
comprehensive specifications that vendors of different 
scales can adhere to. This prevents lock-in to proprietary, 
incompatible systems and vendors. For example, the highly 
successful Unified Payments Interface, which focused on 
specifications, allowed a wide array of app developers to 
create payment apps, providing users an opportunity to move 
away from convoluted banking apps.   
 ▪ T echnology-agnostic architecture. The architecture of 
the solutions should be not tied to any specific technology, 
allowing for the adoption of new and emerging technologies. 
This approach ensures far-longer-term viability and 
adaptability.  
 ▪ Open data and observability. The DPI should emphasize 
open data and observability. Making data accessible and 
enabling the bus system’s performance to be monitored 
fosters transparency and continuous improvement. This 
principle is particularly important in the transport space – 
for example, TfL, the transport authority in London, opened 
62 transit datasets to app developers. This prompted over 
5,000 developers to use and combine this data in numerous 
ways to create passenger information applications, in ways 
no one had thought of before. The apps did everything 
from mapping locations to showing passengers where 
to stand on a train station platform to avoid boarding 
overcrowded coaches. By sparing TfL from needing to 
develop all types of in-house apps itself, and attracting more 
ridership through better information, TfL estimates that 
the experiment brought in an additional GBP 6.8 billion. 
In India’s (significantly more) complicated bus operating 
environment, such an approach is likely to yield considerable 
innovation at scale. 
 ▪ Federated governance. The architecture should promote 
a federated governance model, emphasizing the autonomy 
of each geographical stakeholder. This principle allows each 
stakeholder to operate independently, making decisions and 
managing operations in a way that best serves their specific 
regional and local needs. Such a decentralized approach 
allows for greater flexibility and responsiveness, catering to 
diverse operational environments while still maintaining 
overall system coherence and standards.  
 ▪ Composability. Composability is a design principle 
that allows systems to be assembled from smaller, 
independent components. This makes it easier to create new 
systems by combining existing components. Composability 
is what will allow various players to unlock true innovation 
in the system. In the bus space, there are several data-
emitting “fundamental” blocks of the system (for example, 
passenger ticketing, vehicle tracking, battery’s state of 
charge). The ability to combine these diverse blocks (as 
shown in Figure 7) can yield rich insights and applications. 
For example, data from these three blocks can be combined 
to create applications yielding rich insights on the type of 
batteries and charging schedules to deploy on different types 
of bus routes. 
With the foundational principles outlined, we can now explore 
specific use cases that demonstrate the versatility and potential 
impact of the open e-bus blueprint. These examples will illus-
trate how the blueprint can be applied to address real-world 
challenges in the bus ecosystem.
USE CASES FOR OPEN E-BUS 
BLUEPRINT IN THE DPI 
ECOSYSTEM 
The concept of modular building blocks is essential for the open 
e-bus blueprint to function effectively. Figure 9 illustrates how 
these blocks provide the missing piece that makes it possible 
to leverage other DPI components that fit together to create a 
cohesive and scalable infrastructure for mobility.
Developing and adopting the building block approach offers the 
following advantages: 
 ▪ Encourages widespread participation, especially from 
smaller or less prominent actors. By establishing data 
standards, specifications and protocols, the approach reduces 
technical and financial barriers to build and deploy solutions. 
This helps level the playing field and enables diverse 
contributors to engage in value creation, fostering a more 
inclusive ecosystem where innovation can thrive. 
 ▪ Encourages flow of value, enabling a decentralized 
network of interconnected actors to collaborate 
harmoniously. The decentralization promotes resilience 
and adaptability and ensures value moves freely across the 
ecosystem, incentivizing innovation, and partnerships. 
Interconnected actors collaborate in open-source 
communities, where developers, companies, and users 
contribute code, funding, and feedback to co-create solutions 
without central control. 
 ▪ Addressing observability and trust by creating a platform-
agnostic environment. Allows applications built on these 
building blocks to be easily discovered, accessed, and trusted 
across various platforms, contributing to a more equitable 
digital landscape in the bus ecosystem.
Figure 9  |  The missing puzzle in DPI for mobility
OPEN E/hyphen.capBUS BLUEPRINT
DIGI LOCKER
OPEN NETWORK FOR 
DIGITAL COMMERCE
UNIFIED ENERGY 
INTERFACE
OPEN NETWORK FOR EDUCATION
AND SKILLING TRANSFORMATIONS
UNIFIED PAYMENT
INTERFACE
BHARAT BILL PAYMENT SYSTEM
OTHER DIGITAL
PUBLIC GOODS
BATTERY PASSPORT
Source: Authors’ analysis.

WORKING PAPER  |  October 2024  |  21
Open e-bus blueprint
20  |  
  
The solutions built using a building block approach are demon-
strated through the following use cases: 
Public-transport-as-a-service (PTaaS)— 
Optimizing bus utilization with federated 
governance 
By adopting open e-bus blueprint, public bus transport systems 
can improve overall service quality and ridership, optimize bus 
utilization, and create a more sustainable, responsive, and profit-
able transit network.
For example, with appropriate policies enabling standardized 
data exchange across all bus operators and systems, open e-bus 
blueprint could allow fleet operators to seamlessly integrate their 
idle buses into a city or region’s transit network during peak 
times. This integration would be managed via application pro-
gramming interfaces (APIs) that facilitate flexible agreements.
Benefits of this approach include the following for:
 ▪ Fleet operators: They can generate additional revenue by 
utilizing their idle buses during periods of high demand.
 ▪ Transit agencies: They can meet passenger demand that 
exceeds their capacity without incurring substantial expenses.
Stakeholders benefited: Commuters, bus operators (both 
private and public) and transport authority.
Public-transport-as-a-service (PTaaS)— 
Unbundling of contracts and change in business 
models
Current model: Public entities that procure e-buses have 
OEMs handle procurement and operation (including setting 
up charging infrastructure and covering energy costs), as well as 
maintenance of the buses according to predefined SLAs. OEMs 
are reimbursed on a per-kilometer basis for operations. This 
model places the entire management responsibility on OEMs, 
whose core competency is bus manufacturing. Conversely, 
in the private sector, bus operators typically own the buses, 
financed through banks, and assume responsibility for mainte-
nance and operation.
Challenge: This is done because the initial cost of e-buses is 
approximately three times that of ICE buses. Because of the 
high upfront capital expenditure, accelerating e-bus adoption 
requires getting the private sector involved. Additionally, bus 
operators and financiers are generally not equipped to handle 
technology risk, which is better managed by bus OEMs.
Proposed solution: The DPI approach allows for unbundling 
existing contracts by providing a transparent, interoperable 
framework that standardizes communication between differ-
ent actors. Through standards, specifications, and protocols 
for information exchange, the blueprint allows contract com-
ponents—such as asset ownership, operations, and energy 
management—to be separated, while ensuring seamless infor-
mation flow. This transparency enables clearer roles, reduces 
information asymmetry, and fosters trust, making it easier to 
distribute responsibilities according to each actor’s expertise, 
and adopting an open e-bus blueprint allows for a more effec-
tive distribution of risk and responsibility, tailored to each 
participant’s expertise. This approach facilitates the separation of 
various contract components—such as asset ownership, opera-
tions, energy, and batteries—but strengthening transparency and 
trust. This is done by ensuring a seamless flow of information 
among them. Ultimately, this leads to a more flexible and effec-
tive business model.
Benefits of this approach include the following for:
 ▪ Bus OEMs: Focusing on bus manufacturing and assuming 
product guarantee risk without involvement in financing or 
operating the buses.
 ▪ Bus operators: Concentrating on bus operation without 
bearing the product guarantee risk.
 ▪ Charging point operators (CPOs): Focusing on providing 
charging services.
 ▪ Financiers: Investing without taking on the product and 
operational risks.
 ▪ State transport undertakings (STUs): Securing services 
with minimal upfront investments and increasing 
participation of private suppliers during procurement.
Stakeholders benefited: OEMs, CPOs, bus operators, finan-
ciers, STUs, transport authority.
Charging up the future: Interoperability 
allows market demand to guide infrastructure 
development with unified energy interface (UEI)9 
and open e-bus blueprint
Current model and challenge: Currently, the responsibility for 
setting up charging infrastructure lies with OEMs and opera-
tors. Each plans and deploys charging facilities based on their 
specific needs and capabilities, as system-wide bus operational 
data is not accessible to individual operators. The success 
of large-scale electric bus deployment depends on strategi-
cally designed charging infrastructure. A major challenge is 
identifying the most efficient and profitable locations for new 
charging stations. Without accurate data on bus movement and 
energy consumption, there is a risk of either over-investing or 
under-investing in charging infrastructure.
Proposed solution: Leveraging standardized operational data 
across electric bus operators by adopting an open e-bus blueprint 
integrated with the UEI allows energy providers to identify 
the most strategic locations for new charging stations. This 
interoperable data-driven approach ensures that investments are 
directed towards areas with the highest demand, minimizing 
risk and maximizing return on investment.
Benefits of this approach include the following for:
 ▪ Operators: Reduces the costs associated with 
setting up charging infrastructure and increasing the 
operational coverage area 
 ▪ CPOs: Accurate and timely data, allowing them to efficiently 
establish charging facilities, increase charger utilization, 
and boost revenue
 ▪ Energy providers: Enables better management of power 
demand based on precise operational data
Stakeholders benefited: Operators, CPOs, energy providers, 
transport authority.
Mobilizing finance: Enabling affordable 
financing and unlocking carbon markets with 
composability, open data and observability
Challenge: Securing financing for electric bus projects is not 
easy. Traditional financial institutions struggle to assess customer 
risk, technology risk, operational details, and the environmental 
benefits and impacts of electric buses. This lack of clear data 
hinders access to sustainable and affordable green financing, 
thereby slowing the transition to clean transportation.
Proposed solution: A DPI-driven ecosystem enables financiers 
to better assess technology and operational risks by accessing 
necessary information, including capturing credit histories 
to understand bus operator risk over time. Standardized 
operational data from e-buses also enhances transparency in 
estimating emission reductions and tracking carbon credits, 
making them easier to trade.
This approach helps oversee the generation and verification of 
carbon credits with transparency and accountability mecha-
nisms. It also reduces costs and increases the likelihood of 
securing affordable funding for sustainable e-bus projects. This 
supports a smooth transition to clean transportation, making 
e-bus projects more attractive to financiers and operators alike.
Benefits of the DPI approach for:
 ▪ OEMs/operators: Enables access to affordable financing 
and provides an additional revenue source through 
carbon credit trading
 ▪ Financiers: Helps mitigate customer and technology risks 
and, with transparent emission reduction estimates, facilitates 
the provision of affordable green financing to e-bus operators
Stakeholders benefited: OEMs/operators, financiers, 
transport authority.
Powering up the workforce: E-buses, skills, and 
the future
Challenge: India’s 10 million-strong bus workforce faces 
challenges in training, safety, and efficiency. With the planned 
expansion of e-buses, finding skilled drivers is crucial. How-
ever, without proper documentation of skills and performance, 
operators struggle to identify qualified drivers and incentivize 
good practices.
Proposed solution: Integrating and sharing verifiable creden-
tials with platforms like Digilocker10 brings transparency to 
driver skill assessment across operators. This would enable the 
creation of a transparent, structured job market by document-
ing driver credentials, tracking, motivating skill improvement, 
and incentivizing performance in areas such as safety and fuel 
efficiency. It can also connect operators with skilled drivers 
through standardized registries across geographies. Additionally, 
operators can upskill their workforce by integrating with other 
DPI initiatives like Open Network for Education and Skilling 
Transactions (ONEST).11 This approach fosters trust, reduces 
skill development costs, and aligns incentives for a more skilled 
and efficient workforce.
Benefits of the DPI approach for:
 ▪ The workforce: Drivers and staff can share verified training 
and employment credentials across operators, enhancing 
employability, pay, and incentivizing safe driving practices.
 ▪ Training institutes: Standardized training modules facilitate 
effective knowledge transfer.
 ▪ Operators: Access to a pool of trained staff aids in safer and 
more efficient bus operations.   
Stakeholders benefited: Workforce, operators, 
training institutes.

WORKING PAPER  |  October 2024  |  23
Open e-bus blueprint
22  |  
  
Inclusive circular economies: Sustainable 
battery management
Challenge: The success of large-scale electric bus adoption 
depends on sustainable battery practices. A lack of transparency 
in the battery life cycle hinders financing for e-buses and limits 
efforts towards responsible sourcing and recycling. This creates 
logistical challenges in managing and maintaining information 
across the battery supply chain. 
Proposed solution: Exchanging real-world operational data 
from e-buses, including transparent battery performance data, 
enhances trust and supports financing for electric buses. Com-
bining this with the UEI, offers a multi-stakeholder approach to 
sustainable battery practices. The UEI enables the implementa-
tion of digitally verifiable battery passports, providing a secure 
record of key information, such as the following:
 ▪ Material provenance: Tracking the origin of battery 
materials to ensure responsible sourcing practices
 ▪ Battery chemistry and manufacturing: Gaining insights 
into battery composition and production history for 
informed decision-making
 ▪ Battery health management: Monitoring battery health 
data to optimize performance, extend lifespan, and facilitate 
responsible recycling
Such a multi-stakeholder approach, connecting and engaging 
businesses, financial institutions, IT solution providers, regula-
tors, auditors, public and international organizations, can help 
foster trust and bring high levels of transparency to the global 
battery value chain. 
Benefits of the DPI approach for:
 ▪ Operators: Reliable operational data will help secure 
affordable financing and enable the deployment of efficient 
and cost-effective charging strategies. It supports the 
adoption of sustainable battery management practices and 
ensures battery circularity.
 ▪ CPOs: Planning and optimizing charging infrastructure 
improves service offerings by utilizing transparent battery 
performance data.
 ▪ Financiers: Reduces perceived technology risks due to 
greater transparency in battery life cycle data.
 ▪ Transport authorities: Enforces regulatory compliance 
and implement policies that promote sustainable sourcing 
practices for batteries.
Stakeholders benefited: Operators, OEMs, CPOs, financiers, 
transport authority.
IMPLEMENTING OPEN E-BUS 
BLUEPRINT 
Bringing the open e-bus blueprint from concept to opera-
tion will require deliberate, strategic action. We present our 
roadmap here, inviting constructive criticism, collaboration, 
and engagement.
The process begins with forming a multidisciplinary team to ini-
tiate the design and to further develop and refine the blueprint, 
balancing ambition with practicality. Deliberation with broader 
stakeholder groups will be essential to fully realize its potential. 
Once the blueprint is designed, the next step involves creating 
reference open-source software for adoption and customization 
by bus operators—including State Transport Units (STUs), 
public, private, and other fleet operators—for various use cases. 
A detailed implementation schedule will outline immediate 
goals and long-term ambitions, while early engagement with 
pioneering stakeholders will provide invaluable insights for 
broader rollout. Finally, a robust governance framework for will 
guide this progression, ensuring each innovation is purposeful 
and measurable.
With this strategic roadmap in place, the open e-bus blueprint 
would assume three key roles in its journey from concept to 
implementation:
Developmental role: The blueprint would adopt and adapt 
necessary building blocks for the bus ecosystem taking into 
consideration all the stakeholders. This includes the design, 
development, maintenance, and continuous upgrade of the 
required technological infrastructure. Additionally, it would 
work to enlist participants from various sectors, providing 
them with the necessary support to ensure widespread volun-
tary participation.
Ecosystem facilitation: The blueprint could help establish 
policies and rules for the ecosystem in collaboration with partic-
ipants. These policies will be machine-readable and, to the extent 
possible, enforceable through software within the ecosystem.
Service delivery: The blueprint would help develop, maintain, 
and continuously upgrade foundational services for managing 
the buses, such as registries, certifications, and specifications. It 
would also develop reference or sample applications to guide 
new participants (such as bus operators or service providers), 
especially in the early stages to facilitate onboarding.
Design initiation 
Securing government endorsement is vital for the legitimacy 
and success of the blueprint. Official recognition from Min-
istries (MoRTH, MoHUA, MHI, MoP), government bodies 
(ASRTU, CESL CMVR-TSC, BEE), and transport agencies 
involved in regulating and supporting the sector is needed to 
validate the blueprint and enable smoother integration with 
existing infrastructure and regulations. Recommended actions 
include the following:
 ▪ Forming the design council: This is a carefully selected 
group of experts, especially those with a background in 
establishing or working with large digital infrastructures, 
standards bodies, free and open-source software (FOSS) 
communities, and volunteers. They can contribute to 
the architectural design, draft standards, and ensure 
system scalability.
 ▪ Establishing an advisory board: This would comprise 
experts and stakeholders from various fields and guide 
the project’s long-term success, focusing on regulatory 
alignment, technological updates, and seamless integration 
with existing systems.
Implementation strategy
The long-term plan would be to implement the blueprint as a 
foundational digital public infrastructure for buses to making it 
an ecosystem-wide utility serving the diverse use cases and play-
ers in the bus ecosystem. The blueprint could transform how the 
bus sector operates today and address challenges like building 
trust among operators, managing multi-sectoral alignment, and 
addressing stakeholder concerns. The initial phase of the blue-
print needs to be rolled out quickly with e-bus deployment to 
gain acceptance and assess scalability. The implementation strat-
egy would largely need to focus on three key aspects: technology, 
business, and institution building, including the following:
 ▪ Pilot projects: Identifying cities or regions for testing the 
components of blueprint in diverse environments.
 ▪ Value demonstration: Highlighting immediate benefits to 
users and stakeholders, such as improved service reliability 
through early blueprint features like standardizing schedules, 
vehicle health and battery health specifications.
 ▪ Scalability plans: Developing strategies to scale the 
blueprint from pilot regions to national coverage.
CONCLUSION
The transition to e-buses presents a pivotal opportunity to 
transform India’s public transportation. As the country targets 
electrifying 800,000 buses over the next decade, the current 
fragmented bus ecosystem creates inefficiencies and increases 
operational costs, limiting the scalability of e-bus deployment 
and infrastructure. Addressing these challenges will require more 
than isolated technological fixes.
Our proposed alternative is a robust, foundational digital infra-
structure. The open e-bus blueprint, rooted in Digital Public 
Infrastructure (DPI) principles, provides a sustainable approach 
to technology integration and scalable solutions. Inspired by 
India’s DPI successes, this blueprint emphasizes reusable digital 
building blocks that reduce core infrastructure investment while 
enabling significant improvements in efficiency and cost reduc-
tion. By “doing less,” we can achieve a large-scale impact, driving 
reach and inclusivity across the bus ecosystem. This approach 
allows bus operators, OEMs, CPOs, financial institutions, and 
technology service providers to innovate collaboratively, offering 
choice and flexibility for future solutions while minimizing the 
risks tied to proprietary systems.
We invite policymakers, industry leaders, and all stakeholders to 
engage with these ideas and work collectively toward a sustain-
able, resilient public transportation system that supports both 
economic growth and environmental goals.

WORKING PAPER  |  October 2024  |  25
Open e-bus blueprint
24  |  
  
ABBREVIATIONS
AFC  Automatic Fare Collection
API  Application Programming Interface
ASRTU  Association of State Road Transport Undertaking
BEE  Bureau of Energy Efficiency
BMTC  Bengaluru Metropolitan Transport Corporation
BN  Billion
CBS  Core Banking Solution
CESL  Convergence Energy Services Limited
CMVR-TSC TSC Central Motor Vehicles Rules—Technical   
  Standing Committee
CPO  Charge Point Operator
CR  Crore
DIMTS  Delhi Integrated Multi-modal Transit System
DTC  Delhi Transport Corporation
DPI  Digital Public Infrastructure
ETM  Electronic Ticketing Machine
FOSS  Free and Open Source Software
GCC  Gross Cost Contract
GoI  Government of India
GTFS  General Transit Feed Specification
ITS  Intelligent Transportation System
IT  Information Technology
IP  Internet Protocol
MaaS  Mobility-as-a-Service 
MHI  Ministry of Heavy Industries
MoHUA  Ministry of Housing and Urban Affairs
MoP  Ministry of Power
MoRTH   Ministry of Road Transport and Highways
NeTEx  Network Timetable Exchange
NPCI  National Payments Corporation of India
OEM  Original Equipment Manufacturer
ONDC  Open Network for Digital Commerce
ONEST  Open Network for Education and    
  Skilling Transformation
PPP  Public-Private Partnership 
PIS  Passenger Information System
RBI  Reserve Bank of India
SoC  State of Charge
STU  State Transport Undertaking
TCO  Total Cost of Ownership
TN  Trillion
UEI  Unified Energy Interface
UPI  Unified Payments Interface
VLT  Vehicle Location and Tracking
BUS A motor vehicle carrying passengers by road, either on a stage-carriage or contract-carriage permit. For 
the purposes of this document, a bus refers only to services having a predefined schedule.
STAGE CARRIAGE
A stage carriage means a motor vehicle carrying or adapted to carry more than six persons, excluding the 
driver, which carries passengers for hire or reward at separate fares paid by or for individual passengers, 
either for the whole journey or for stages of the journey.
CONTRACT CARRIAGE A motor vehicle that carries passenger(s) for hire or reward under a contract, whether expressed or 
implied for the use of the vehicle as a whole, for a period at agreed-upon rate or sum.
(BUS) STOP A place (with specified geo-coordinates and a geo-fence) where a bus regularly stops, usually 
marked by a sign.
BUS STATION (OR) 
TERMINAL A place where buses arrive and depart and serves passenger boarding and alighting.
BUS DEPOT A facility where buses are stored/parked and maintained.
ROUTE
A specified path for movement of a bus from origin to destination along predefined road segments 
passing through a series of bus stops and/or waypoints. A route is usually represented by a unique num-
ber, name, or ID.
TRIP An instance of a route with specific arrival/departure timings at each of the stops along the route.
TIMETABLE A passenger-facing chart showing the arrival/departure timings at a single or multiple stops. Timetables 
at a given stop are usually listed by routes serving the bus stop and color coded by service type.
SCHEDULE
A bus operator–or crew-facing chart indicating the series of trips to be undertaken by them during their 
work shift. Schedules can be of two types – bus schedule and crew schedule. In most Indian bus opera-
tions, the crew is fixed to a bus throughout their work shift on a specific day. Thus, in such cases, the bus 
schedule and the crew schedule is one and the same for that period.
TRANSIT AGENCY/
AUTHORITY
The agency responsible for planning and monitoring of transit services. This is usually a government entity 
or a government owned company/corporation.
TRANSIT OPERATOR The agency or individual, either public or private, responsible for operating the bus fleet as per the sched-
ules planned/prepared by the transit authority.
GLOSSARY

WORKING PAPER  |  October 2024  |  27
Open e-bus blueprint
26  |  
  
9. UEI, is a DPI built on the Beckn protocol; the same protocol 
powers India’s Open Network for Digital Commerce (ONDC). 
It enables interoperability between charging networks, 
energy providers for easy charger discovery, and streamlined 
payments for energy transactions. It offers a homegrown 
alternative, inspired by successful Indian models like UPI, 
compared to global standards like Open Charge Point Inter -
face (OCPI).
10. DigiLocker, an initiative by the Ministry of Electronics and 
Information Technology, GoI, under the Digital India pro -
gramme, is a secure, cloud-based platform for storing, 
sharing, and verifying digital documents. It enables citizens 
to store government-issued IDs, KYC documents, healthcare 
records, and more, supporting use cases across sectors like 
financial services, healthcare, HR, legal, and government 
agencies.
11. ONEST is an open, decentralized network designed to break 
silos in education and employment, fostering collaboration 
between content providers, learners, and job seekers. Its goal 
is to enhance access to equitable education, skills develop -
ment, and sustainable livelihood opportunities.
ENDNOTES
1. This estimate is based on data collated from multiple sources 
for the same time period (Gadepalli et al. 2024; TOI Education 
2023; Press Information Bureau, GoI 2024; Ministry of Civil 
Aviation 2024; De et al. 2017)
2. The Bharat Bill Payment System (BBPS), developed by the 
Reserve Bank of India (RBI) and managed by NPCI, offers 
a unified, interoperable platform for secure and reliable bill 
payments across India. It supports use cases like mobility 
payments, loan repayments, and utility bills, to name a few.
3. Technology service providers are entities that provide tech -
nology solutions or technology services (usually categorized 
as Mobility-tech, Energy-tech, Fin-tech, Travel-tech, etc.) 
4. Network Timetable Exchange is a CEN Technical Standard 
for exchanging Public Transport schedules and related 
data. It provides a means to exchange data for passenger 
information among different computer systems, together with 
related operational data. 
5. General Transit Feed Specification is a community-driven 
open standard for rider-facing transit information.
6. Gross Cost Contract (GCC) model, the operator/supplier 
contracts with the transport corporation and is paid on a 
fixed cost per km basis. The supplier is responsible for pro -
curement of e-buses and related operations and monitoring 
infrastructure.
7. Net Cost Contract (NCC) model is an agreement between a 
transport authority and operator/ supplier of contracts that 
gives the operator the right to provide bus services on a 
specific route. The bus operator keeps all the revenue from 
the services, and the transport authority pays the operator 
a subsidy or royalty depending on whether the services are 
profitable.
8. Open Network for Digital Commerce’ (ONDC), is a Govern -
ment of India (GoI) backed technology infrastructure. It is 
a network-centric model, based on Beckn protocol wherein 
buyers and sellers can transact irrespective of the platforms/
applications they use as long as they are connected to this 
open network. The protocol enables local commerce across 
segments, such as mobility, grocery, food order and delivery, 
hotel booking and travel, among others, to be discovered and 
engaged by any network-enabled application.
REFERENCES
Aadhaar. 2024. “Aadhaar Dashboard.” Accessed September 27. 
https://uidai.gov.in/aadhaar_dashboard/india.php.
Abisla, Richard. 2019. “Open Transit Data in India”. In The Promise of 
Public Interest Technology: In India and the United States. Washington, 
DC: New America. http://www.jstor.org/stable/resrep19980.8.
ASRTU (Association of State Road Transport Undertakings). 2024. 
“ASRTU at a Glance”. https://www.asrtu.org/page/about.
Bachu, Prashanth, Sayan Roy, and Anumita Roychowdhury. 2024. 
What Ails Intelligent Transport Systems? Roadmap for Modernizing Bus 
Services. Centre for Science and Environment.
Banerjee, Amber. 2022. “India’s Outstation Bus Market to Grow Up 
to USD 48 Billion by 2025: Here’s How.” The Times of India, June 14. 
https://timesofindia.indiatimes.com/auto/indias-outstation-bus-
market-to-grow-up-to-usd-48-billion-by-2025-heres-how/article -
show/92200042.cms.
Business Standard. 2023. “FAME III: India to Replace 800k Diesel 
Buses with Electric over 7 Years.” https://www.business-standard.
com/industry/auto/fame-iii-india-to-replace-800k-diesel-buses-with-
electric-over-7-years-123122900244_1.html.
CDPI (Centre for Digital Public Infrastructure). 2023. “DPI Tech Archi -
tecture Principles”.Bengaluru. https://docs.cdpi.dev/the-dpi-wiki/dpi-
tech-architecture-principles.
CDPI. 2024a. “DPI Overview.” https://docs.cdpi.dev/the-dpi-wikipe -
dia/dpi-overview.
CDPI. 2024b. “Payments.” https://docs.cdpi.dev/technical-notes/
digital-payment-networks.
CSTEP (Charging Technology Options for E-buses in Bengaluru). 
2021. CSTEP-RR-2021-08.
DBT (Direct Benefit Transfer) Bharat. 2024. “DBT Bharat.” Accessed 
September 27. https://dbtbharat.gov.in/.
De, Anish, Richard Threlfall, Sameer Bhatnagar, Rajaji Meshram, 
Umang Jain, Nisha Fernandes, Shveta Pednekar, and Rasesh Gajjar. 
2017. “Reimagining Public Transport in India.” KPMG. https://assets.
kpmg.com/content/dam/kpmg/in/pdf/2017/10/Reimagining-pub -
lic-transport.pdf.
DoFS, Ministry of Finance. 2024. “Account Aggregator Framework | 
Department of Financial Services | Ministry of Finance | Government 
of India.” https://financialservices.gov.in/beta/en/account-aggre -
gator-framework.
D’Silva, Derryl, Zuzana Filkova, Frank Packer, and Siddharth Tiwari. 
2019. “The Design of Digital Financial Infrastructure: Lessons from 
India,” December. https://www.bis.org/publ/bppdf/bispap106.htm.
Fathima, J Shifa. 2015. “Implementation of Core Banking Sys -
tems (CBS) in the Banks in India—With Special Reference to Ur -
ban Co-Operative Banks (UCB).” Shanlax International Journal of 
Commerce 3. https://www.shanlaxjournals.in/pdf/COM/V3N1/
COM_V3_N1_007.pdf.
Gadepalli, Ravi, Aishwarya Kachhal, Tanay Dandekar, and Mad -
humitha V. 2024. Market Assessment for Intercity Electric Buses in 
India. Bengaluru: Transit Intelligence.
Georgia Institute of Technology. 2011. “How the Internet Archi -
tecture Got Its Hourglass Shape and What That Means for the 
Future.” https://phys.org/news/2011-08-internet-architecture-hour -
glass-future.html.
Gupta, Sangeeta, Achyuta Ghosh, Kalyan Mangalapalli, Nirmala 
Balakrishnan, Vandhna Babu, Satya Easwaran, Brajesh Singh, Pankaj 
Mann, Shubhang Kandoi, and Apar Sharma. 2024. India’s Digital 
Public Infrastructure — Accelerating India’s Digital Inclusion. NASSCOM, 
Arthur D. Little. https://community.nasscom.in/sites/default/files/
publicreport/Digital%20Public%20Infrastructure%2022-2-2024_
compressed.pdf.
Hariharan, N.P., and K.J Reeshma. 2015. “Challenges of Core Banking 
Systems.” Mediterranean Journal of Social Sciences 6 (September). 
doi:10.5901/mjss.2015.v6n5p24.
Kharwal, Shilpa, and Udit Khandelwal. 2021. “Public-Private Partner -
ships (PPP) in City Bus Services in India: NCC and GCC.”WRI INDIA.
https://wri-india.org/blog/public-private-partnerships-ppp-city-bus-
services-india-ncc-and-gcc.
Kumar, Dr. Parveen, Pawan Mulukutla, and Priyansh Doshi. 2023. 
“Real-World Electric Bus Operation: Trend in Technology, Perfor -
mance, Degradation, and Lifespan of Batteries.” WRI India. https://
wri-india.org/publication/real-world-electric-bus-operation-trend-
technology-performance-degradation-and-lifespan.
Ministry of Civil Aviation. 2024. “Ministry of Civil Aviation- Dashboard.” 
https://www.civilaviation.gov.in/.
Ministry of Housing And Urban Affairs, GoI. 2020. “Bus Operations for 
Middle Managers.” December

WORKING PAPER  |  October 2024  |  29
Open e-bus blueprint
28  |  
  
Mohanty, Amlan. 2023. “The Business Case for DPI - Carnegie En -
dowment for International Peace.” Carnegie Endowment for Interna -
tional Peace. https://carnegieendowment.org/posts/2023/06/the-bu-
siness-case-for-dpi?lang=en.
Mulukutla, Pawan, and Srickant Rajagopal. 2024. “Empowering India’s 
Electric Bus Revolution: The Role of Blended Finance.” ETEnergy -
world.com. Accessed October 5. https://energy.economictimes.india -
times.com/news/power/empowering-indias-electric-bus-revolution-
the-role-of-blended-finance/110139495.
Nilekani, Rohini. 2022. Samaaj, Sarkaar, Bazaar: A Citizen-First Ap -
proach. Notion Press.
NPCI (National Payments Corporation of India). 2024. “Enabling 
Digital Payments in India.” Accessed September 27. https://
www.npci.org.in/.
Philip, Christin Mathew. 2019. “Trimax Financial Crisis Forces BMTC 
to Switch to Manual Paper Tickets on 15% Routes.” The Times 
of India, April 9. https://timesofindia.indiatimes.com/city/benga -
luru/bmtc-manually-issuing-tickets-on-15-of-its-routes/article -
show/68785147.cms.
Press Information Bureau, GoI. 2023. “Decarbonization of Transport 
Sector Essential to Reduce GHG Emissions, Achieve Net-Zero Emis -
sions by 2070: Union Environment Minister Shri Bhupender Yadav.” 
https://pib.gov.in/pib.gov.in/Pressreleaseshare.aspx?PRID=1984578.
Press Information Bureau, GoI. 2024a. “Cabinet Approves ‘PM-eBus 
Sewa’ for Augmenting City Bus Operations; Priority to Cities Having 
No Organized Bus Service.” Accessed October 7. https://pib.gov.in/
pib.gov.in/Pressreleaseshare.aspx?PRID=1949430.
Press Information Bureau, GoI. 2024b. “India’s UPI: A Global Front-
Runner in Digital Payment Systems.” Accessed October 17. https://pib.
gov.in/pib.gov.in/Pressreleaseshare.aspx?PRID=1973082.
Press Information Bureau, GoI. 2024c. “Growth of Metro Rail in India 
Is Underlined by Rising Ridership Figures.” https://pib.gov.in/pib.gov.
in/Pressreleaseshare.aspx?PRID=1993703.
Rollison, Caitlin, and Matthew Coombes. 2023. “Gear Shift: Interna -
tional Lessons for Increasing Public Transport Ridership.” Centre for 
Cities. https://www.centreforcities.org/reader/gear-shift/how-to-
increase-public-transport-use/.
Sclar, Ryan, Camron Gorguinpour, Sebastian Castellanos, and Xiangyi 
Li. 2019. Barriers to Adopting E Buses. World Resources Institute. 
https://www.wri.org/research/barriers-adopting-electric-buses.
Shakti Sustainable Energy Foundation. 2021. Public Private Partner -
ships in Bus Operations in Indian Cities—Engaging Private Sector in Im -
proving Public Transport. https://shaktifoundation.in/wp-content/up -
loads/2022/01/Annex-5-PPP-in-Bus-Operations-in-Indian-cities.pdf.
The Times of India. 2019. “Telangana: Use of School Buses for Passen -
ger Transport an Insurance Nightmare,” October 13. https://timesofin -
dia.indiatimes.com/city/hyderabad/use-of-school-buses-for-passen -
ger-transport-an-insurance-nightmare/articleshow/71560557.cms.
TOI Education. 2023. “Indian Railways: 10 Surprising Facts That 
Every Student Should Know About.” The Times of India , November 
23. https://timesofindia.indiatimes.com/education/learning-with-toi/
indian-railways-10-surprising-facts-that-every-student-should-know-
about/articleshow/105430676.cms.
UIDAI, GoI. 2014. AADHAAR Technology & Architecture—Principles, 
Design, Best Practices, & Key Lessons .
Vijaykumar, Aparna, Dr. Parveen Kumar, Pawan Mulukutla, and Dr. OP 
Agarwal. 2020. Procurement of Electric Buses: Insights from Total Cost 
of Ownership (TCO) Analysis . WRI India. 
THIS PAGE IS INTENTIONALLY KEPT BLANK

WORKING PAPER  |  October 2024  |  31
Open e-bus blueprint
30  |  
  
THIS PAGE IS INTENTIONALLY KEPT BLANKTHIS PAGE IS INTENTIONALLY KEPT BLANK

Copyright 2024 World Resources Institute. This work is licensed under the Creative Commons Attribution 4.0 International License.  
To view a copy of the license, visit http://creativecommons.org/licenses/by/4.0/
  
LGF, AADI, 2 Balbir Saxena Marg, Hauz Khas, New Delhi 110016, India  |  WRI-INDIA.ORG
ACKNOWLEDGMENTS
The authors thank their WRI India colleagues—Aloke Mukherjee, 
Chintan Daftardar, and Bina Shetty—for their valuable insights 
and suggestions. Special thanks to external reviewers Rathish 
Balakrishnan (Sattva Consulting), Vivek Ogra (Ernst and Young), 
Samir Sharma (National Capital Region Transport Corporation), and 
Dr. Gitakrishnan Ramadurai (Indian Institute of Technology, Madras) 
for their feedback. The authors also appreciate Ms. Ankita Rajeshwari 
and Ms. Rama Thoopal for their administrative, editorial, and design 
support, along with Mr. Venkatesh Bilvam for the infographics and 
Ms. Tulika Patel for the layout.
ABOUT THE AUTHORS
Rajit Kumar Bhat  is a Program Associate, Integrated Transport, 
Sustainable Cities Program, WRI India.
Dr. Pramod Varma is the chief architect and technology advisor for 
India’s ID project – “Aadhaar.” He is also the architect of UPI, digital 
locker, and e-sign. He is currently the CTO of EkStep Foundation.
Pawan Mulukutla  is Executive Program Director, Integrated 
Transport, Clean Air and Hydrogen, WRI India.
Anirban Sinha is a Senior Associate, FIDE.
Prashanth Bachu  is a transport planner and a consultant for WRI 
India on this paper.
Sujith Nair is the CEO and Co-founder of FIDE.
Avinash Dubedi  is the Program Head, Integrated Transport, 
Sustainable Cities Program, WRI India.
Madhav Pai is the CEO, WRI India.
ABOUT WRI INDIA
WRI India, an independent charity legally registered as the India 
Resources Trust, provides objective information and practical 
proposals to foster environmentally sound and socially equitable 
development. Our work focuses on building sustainable and liveable 
cities and working towards a low carbon economy. Through research, 
analysis, and recommendations, WRI India puts ideas into action 
to build transformative solutions to protect the earth, promote 
livelihoods, and enhance human well-being. We are inspired by 
and associated with World Resources Institute (WRI), a global 
research organization.
Know more: www.wri-india.org.
ABOUT FOUNDATION FOR 
INTEROPERABILITY IN DIGITAL 
ECONOMY (FIDE)
FIDE is a not-for-profit organization that fosters innovation and co-
creation among ecosystem participants, by building interoperable 
open protocol specifications as a public good. FIDE is the genesis 
author of Beckn Protocol specification and the angel donor for 
its evolution. FIDE continues to foster an open community–led 
movement for Beckn.
