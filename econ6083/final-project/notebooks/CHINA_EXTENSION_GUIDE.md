# Chinese Counterpart Research Extensions - Data Guide

This document provides **verified data sources** and **runnable code frameworks** for Chinese counterpart extensions of each Final Project option.

---

## ✅ Option 6: China EPU (FULLY PUBLIC - Ready to Run)

**Research Question**: How does economic policy uncertainty affect China's macro economy?

**Data Status**: ✅ ALL data directly downloadable, no registration required.

| Data | Source | Access |
|------|--------|--------|
| China EPU Index | policyuncertainty.com | Direct CSV download |
| China CPI / PMI / LPR | akshare (Python package) | `pip install akshare` |
| US EPU (for comparison) | policyuncertainty.com | Direct CSV download |

**Starter Code**: [`option6_china_epu_extension.ipynb`](./option6_china_epu_extension.ipynb)
- **Verified**: ✅ Runs end-to-end in Colab
- Overlap period: 2008-2019 (136 months)
- Includes US vs China EPU comparison

**Key Papers**:
- Baker, Bloom & Davis (2016) - original EPU paper
- 王义中, 朱东明 (2018) - China EPU and firm investment

---

## 🟡 Option 3: DiD - China Carbon Trading Pilot (Registration Required)

**Research Question**: Did China's carbon emission trading pilots reduce CO2 emissions?

**Policy Background**: 7 pilot provinces/cities launched ETS at different times (2013-2014):
- **Shenzhen**: June 2013
- **Shanghai**: November 2013
- **Beijing**: November 2013
- **Guangdong**: December 2013
- **Tianjin**: December 2013
- **Hubei**: April 2014
- **Chongqing**: June 2014

**Data Sources**:

| Data | Source | Access |
|------|--------|--------|
| Provincial CO2 emissions | CEADs | Free registration at ceacs.net |
| Provincial GDP / population | National Bureau of Statistics | Annual Statistical Yearbook |
| Alternative: OWID national CO2 | Our World in Data | Direct download (but only national level) |

**Data Structure Needed**:
```
Panel data: Province × Year (2005-2020)
- treat: 1 if province has ETS
- post: 1 if year >= treatment year
- y: CO2 emissions / CO2 per capita
- controls: GDP, population, industrial structure
```

**Starter Code Framework**:
```python
import pandas as pd
import numpy as np

# Load your data (after downloading from CEADs / Statistical Yearbook)
# df = pd.read_csv('china_province_co2_panel.csv')

# Define treatment timing
treat_timing = {
    'Shenzhen': 2013, 'Shanghai': 2013, 'Beijing': 2013,
    'Guangdong': 2013, 'Tianjin': 2013, 'Hubei': 2014, 'Chongqing': 2014
}

# Create treatment indicators
# df['treat_year'] = df['province'].map(treat_timing).fillna(0)
# df['post'] = (df['year'] >= df['treat_year']).astype(int)
# df['treat'] = (df['treat_year'] > 0).astype(int)

# Run TWFE
# import statsmodels.formula.api as smf
# model = smf.ols('co2 ~ treat*post + C(province) + C(year)', data=df).fit()

# Run Callaway-Sant'Anna (use did package or manual implementation)
```

**Feasibility**: ⭐⭐⭐⭐ (Data requires registration but freely available)

**Key Papers**:
- 张希良, 段鹏霞 (2021) - China carbon trading pilots
- Calel & Dechezleprêtre (2016) - environmental policy evaluation

---

## 🟡 Option 4: SCM - China Carbon Trading or Property Tax Pilot

**Research Question**: What would have happened to Guangdong's CO2 without the ETS pilot?

**Treatment**: Guangdong ETS (Dec 2013) OR Shanghai/Chongqing property tax (2011)

**Data**: Same as Option 3 (CEADs + Statistical Yearbook)

**Advantage**: Only need **one treated unit** (e.g., Guangdong) + donor pool (other provinces)

**Starter Code**: Same SCM code as the main notebook, just replace:
- `treat_state = 'Guangdong'`
- `treat_year = 2013`
- `outcome = 'co2_per_capita'`

**Feasibility**: ⭐⭐⭐⭐

---

## 🟡 Option 1: DML - Housing Provident Fund and Consumption

**Research Question**: What is the causal effect of Housing Provident Fund (HPF) participation on household consumption?

**Data Source**: CHFS (中国家庭金融调查)

| Data | Source | Access |
|------|--------|--------|
| CHFS | Southwestern University of Finance and Economics | Purchase via Taobao (~50-100 RMB) OR apply online |

**Key Variables**:
- `Y`: Household consumption expenditure
- `D`: HPF participation (1 = has HPF)
- `X`: Income, education, age, city, household size

**Method**: Same DML code as Option 1, just replace variables

**Feasibility**: ⭐⭐⭐ (Requires purchasing data)

**Key Papers**:
- 周绍杰 et al. - Housing provident fund and household consumption

---

## 🟡 Option 2: Causal Forests - Poverty Alleviation Heterogeneity

**Research Question**: Which types of households benefit most from targeted poverty alleviation?

**Data Source**: CFPS (中国家庭追踪调查)

| Data | Source | Access |
|------|--------|--------|
| CFPS | Peking University | Free registration at isss.pku.edu.cn/cfps |

**Key Variables**:
- `Y`: Household income / consumption
- `D`: Poverty alleviation participation (from survey questions)
- `X`: Education, health, location (rural/urban), family size, assets

**Method**: Same CausalTree code as Option 2

**Feasibility**: ⭐⭐⭐⭐ (Free but requires registration)

**Alternative**: Use CFPS public data extract (some waves have simplified public versions)

---

## 🟡 Option 5: Policy Learning - Targeted Poverty Alleviation

**Research Question**: How to optimally allocate poverty alleviation resources given a budget?

**Data**: Same as Option 2 (CFPS)

**Method**: Same policy learning code as Option 5
- Estimate CATE using DR scores
- Learn optimal treatment assignment rule
- Compare welfare under different budget constraints

**Feasibility**: ⭐⭐⭐⭐

---

## Summary: Which is Easiest?

| Option | Chinese Topic | Data Cost | Registration | Difficulty |
|--------|--------------|-----------|--------------|------------|
| **6** | China EPU + Macro | FREE | None | 🌟 Easiest |
| **3** | Carbon Trading DiD | FREE | CEADs | 🌟🌟 |
| **4** | Carbon Trading SCM | FREE | CEADs | 🌟🌟 |
| **2** | Poverty Alleviation CF | FREE | CFPS | 🌟🌟 |
| **5** | Poverty Alleviation Policy | FREE | CFPS | 🌟🌟 |
| **1** | HPF + Consumption | ~50-100 RMB | None (buy) | 🌟🌟🌟 |

---

## Recommendations

1. **If you want a fully runnable extension with ZERO data hassle**: Choose **Option 6 (China EPU)**. The notebook is already written and verified.

2. **If you want a policy evaluation topic**: Choose **Option 3 (Carbon Trading DiD)** or **Option 4 (Carbon Trading SCM)**. The policy is real, economically important, and the data is free (just requires CEADs registration).

3. **If you have access to CFPS or are willing to register**: Choose **Option 2 or 5 (Poverty Alleviation)**. Very topical and policy-relevant.

4. **If you are willing to buy data**: Choose **Option 1 (HPF + Consumption)**. CHFS is high-quality household financial data.
