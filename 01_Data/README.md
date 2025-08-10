# 01_Data

This folder contains all the datasets used in the JEE Dropout ML Project, organized by their processing stage.

## Structure
```
01_Data/
├── 01_raw/
│   └── JEE_Dropout_After_Class_12.csv
├── 02_Cleaned and Engineered/
│   ├── Feature_Engineered.csv
│   └── JEE_Dropout_Cleaned.csv
└── 03_final/
    └── JEE_Dropout_Final.csv
```

## Folder Descriptions
- **01_raw/**  
  Contains the original, unprocessed data collected for the project.
- **02_Cleaned and Engineered/**  
  Contains datasets that have been cleaned and feature engineered for analysis and modeling.
- **03_final/**  
  Contains the final dataset used for model training and evaluation.

## Notes
- All data files are in CSV format.
- For details on data cleaning and feature engineering, refer to the notebooks in `02_Data Analysis`.
- If you add new data files, please update this README accordingly.