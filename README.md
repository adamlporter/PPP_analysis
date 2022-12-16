# PPP Analysis
The PPP program distributed an enormous amount of money. Who received it? The SBA has released the data files here: __[https://data.sba.gov/dataset/ppp-foia/resource/6dd520ff-c211-404f-b7eb-29784cd4dbda]__

There is information about the businesses that borrowed money, the lenders that provided the funds, the number of jobs reported by the employer, the NAICS code, and demographic information about race, ethnicity, gender, and veteran status. Unfortunately, for the majority of the records, the demographic information isn't recorded:
* Race - "Unanswered" 75% (White 13.7%, Black 7.1%, Asian 2.6%)
* Ethnicity - "Unknown" 71% (Not Hispanic: 25%; Hispanic 3.2%)
* Gender - "Unanswered" 61% (Male owned: 25%, Female owned 13%)
* Veteran - "Unanswered" 67% (Non-V: 31%, V:1.8%)

I am particulary interested in how the PPP funds were allocated to different religious groups. There is a specific __[NAICS code (813110)](https://www.census.gov/naics/?input=813110&year=2022&details=813110)__:

> This industry comprises (1) establishments primarily engaged in operating religious organizations, such as churches, religious temples, mosques, and monasteries, and/or  (2) establishments primarily engaged in administering an organized religion or promoting religious activities.

The "AddFIPSandMakeCountMap" jupyter notebook combines the PPP data with the US cenesus' county data and explores different ways of visualizing the PPP data at a county level (N loans, N loans as a ratio to county population, Cost of loans per person in a county, etc.)

The "MapALL_PPP_data" notebook provides a state-level visualization of the the whole PPP dataset vs the "religious group" subset. This includes the total cost of loans to businesses / religious groups in a state; and the cost per state resident.


