# ECON6083 Final Project: Empirical Replication and Extension

**Due:** One week after the final lecture (see course schedule for exact date)

---

## Overview

The final project is a capstone assignment that requires you to replicate and extend the main empirical results of a landmark paper in the causal machine learning literature. This project is more substantial than the regular assignments and is designed to give you experience with the full empirical research workflow: from data acquisition and cleaning, to model estimation and interpretation, to presenting your findings in a professional academic format.

You will work individually or in groups of two.

---

## Paper Options

Please choose **one** of the following six papers to replicate. Each paper connects to a specific set of methods covered in the course.

### Option 1: DML for 401(k) Eligibility and Wealth

**Paper:** Chernozhukov, V., Chetverikov, D., Demirer, M., Duflo, E., Hansen, C., Newey, W., & Robins, J. (2018). Double/debiased machine learning for treatment and structural parameters. *The Econometrics Journal*, 21(1), C1-C68.

**Research Question:** What is the causal effect of 401(k) eligibility on net financial assets?

**Data:** The 401(k) dataset is available in the `econml` Python library (`econml.datasets.fetch_401k`).

**Methods:** Double/Debiased Machine Learning (DML) with various nuisance function estimators (Lasso, Random Forest, Gradient Boosting).

**Connection to Course:** Lectures 4 and 5 (Cross-Validation, DML).

### Option 2: Causal Forests for Job Training Effects

**Paper:** Athey, S., & Imbens, G. (2016). Recursive partitioning for heterogeneous causal effects. *Proceedings of the National Academy of Sciences*, 113(27), 7353-7360.

**Research Question:** Are the effects of the National Supported Work (NSW) job training program heterogeneous across individuals? Who benefits the most?

**Data:** The LaLonde (1986) dataset is available in the `econml` Python library (`econml.datasets.fetch_lalonde_observational`).

**Methods:** Causal Trees and Causal Forests for estimating Conditional Average Treatment Effects (CATEs).

**Connection to Course:** Lecture 6 (Heterogeneous Treatment Effects).

### Option 3: Modern DiD for Minimum Wage Effects

**Paper:** Cengiz, D., Dube, A., Lindner, A., & Zipperer, B. (2019). The effect of minimum wages on low-wage jobs. *The Quarterly Journal of Economics*, 134(3), 1405-1454.

**Research Question:** What is the effect of minimum wage increases on employment? Does the effect differ by industry or region?

**Data:** The replication data for this paper is publicly available on the Harvard Dataverse (doi:10.7910/DVN/EQZFZM).

**Methods:** Modern Difference-in-Differences (DiD) with staggered treatment adoption, using the Callaway and Sant'Anna (2021) estimator.

**Connection to Course:** Lecture 9 (Difference-in-Differences and RDD).

### Option 4: Synthetic Control for California Tobacco Control

**Paper:** Abadie, A., Diamond, A., & Hainmueller, J. (2010). Synthetic control methods for comparative case studies: Estimating the effect of California's tobacco control program. *Journal of the American Statistical Association*, 105(490), 493-505.

**Research Question:** Did California's Proposition 99 (a tobacco tax increase passed in 1988) reduce cigarette consumption?

**Data:** The California Proposition 99 dataset is available in the `synthdid` R package or can be accessed via `econml` examples. The data contains per-capita cigarette sales for 50 US states from 1970-2000.

**Methods:** Synthetic Control Method (SCM), Placebo Tests, Leave-one-out Robustness Checks. Optionally: Augmented SCM (Ben-Michael et al., 2021) or Synthetic Difference-in-Differences (Arkhangelsky et al., 2021).

**Connection to Course:** Lecture 9 (Difference-in-Differences and RDD - Synthetic Control is closely related to DiD as a comparative case study method).

**Extension Ideas:** 
- Implement the Augmented Synthetic Control Method (ASCM) to address bias in small samples
- Compare SCM results with modern DiD estimators (Callaway-Sant'Anna) on the same data
- Test sensitivity to donor pool composition

### Option 5: Policy Learning for Optimal Treatment Assignment

**Papers:** 
- Kitagawa, T., & Tetenov, A. (2018). Who should be treated? Empirical welfare maximization methods for treatment choice. *Econometrica*, 86(2), 591-616.
- Athey, S., & Wager, S. (2021). Policy learning with observational data. *Econometrica*, 89(1), 133-161.

**Research Question:** How can we learn optimal treatment assignment rules from data to maximize social welfare? Who should receive job training to maximize employment outcomes?

**Data:** The LaLonde/Job Training Partnership Act (JTPA) dataset is available in `econml.datasets.fetch_lalonde()` or similar observational datasets with treatment assignment and covariates.

**Methods:** 
- Empirical Welfare Maximization (EWM)
- Policy Trees and Policy Forests
- Doubly Robust Policy Learning (using doubly robust scores to maximize welfare)
- Budget-constrained policy optimization

**Connection to Course:** Lecture 10 (Optimal Policy Learning & Text-as-Data).

**Extension Ideas:**
- Compare different policy classes (linear rules vs. tree-based rules vs. budget-constrained rules)
- Implement fairness constraints in policy learning (e.g., demographic parity)
- Use Deep Learning (neural networks) as policy class instead of trees
- Apply Thompson Sampling for robust policy selection under uncertainty

### Option 6: Text as Data - Economic Policy Uncertainty

**Paper:** Baker, S. R., Bloom, N., & Davis, S. J. (2016). Measuring economic policy uncertainty. *The Quarterly Journal of Economics*, 131(4), 1593-1636.

**Research Question:** How can we measure economic policy uncertainty from text data? How does policy uncertainty affect economic outcomes like investment and employment?

**Data:** 
- EPU index data freely available at [www.policyuncertainty.com](http://www.policyuncertainty.com)
- Newspaper text data (NYT Annotated Corpus, or other news archives)
- Economic outcome data (FRED, World Bank, etc.)

**Methods:** 
- Text analysis (bag-of-words, keyword counting)
- Sentiment analysis (dictionary-based: Loughran-McDonald; or ML-based: BERT)
- VAR/SVAR models to analyze macroeconomic effects
- Optional: Topic modeling (LDA) to identify specific policy uncertainty types

**Connection to Course:** Lecture 10 (Optimal Policy Learning & Text-as-Data).

**Extension Ideas:**
- Compare keyword-based EPU measures with modern ML-based measures (fine-tuned BERT classifiers)
- Build a China-specific EPU index using Chinese newspapers (e.g., 人民日报) and Jieba for text segmentation
- Analyze heterogeneity: construct separate uncertainty indices for fiscal, monetary, and trade policy
- Use EPU as a confounder in causal models (e.g., DML with text-based controls)

---

## Deliverables

### 1. Replication Code (`code/`)

A clean, well-commented Python script or Jupyter notebook that replicates the main results of the chosen paper. The code should be reproducible, meaning that anyone should be able to run it and obtain the same results.

### 2. Replication Report (`report.tex`, `report.pdf`)

A short academic paper (5-7 pages, excluding references and appendices) written in LaTeX using the provided template. The report should include:

*   **Introduction (1 page):** Introduce the research question and the paper you are replicating. Explain why the question is important.
*   **Data and Methodology (1-2 pages):** Describe the data and the empirical methodology. Explain the key assumptions required for the causal interpretation of the results.
*   **Replication Results (1-2 pages):** Present your replication results. Compare them to the original paper's results. Discuss any discrepancies.
*   **Extension (1-2 pages):** Describe and present a novel extension to the original analysis. This could involve using a different ML model, exploring different subgroups, or testing the robustness of the results.
*   **Conclusion (0.5 page):** Summarize your findings and discuss their policy implications.



---

## Submission Instructions

Please submit a `.zip` file containing:

1.  `code/` (your replication code)
2.  `report.pdf` (the compiled PDF of your report)


---

## Grading

| Component | Weight | Description |
| :--- | :--- | :--- |
| Replication Code | 20% | Correctness, clarity, and reproducibility of the code. |
| Replication Results | 25% | How closely your results match the original paper. |
| Extension | 30% | Quality and novelty of the extension. |
| Report | 25% | Quality of the written analysis, including clarity, rigor, and interpretation. |
| **Total** | **100%** | |

---

## LaTeX Report Template

Please use the `report.tex` file in this directory as the template for your report.
