import pandas as pd

def clean_dataset(df):
    # Make a Copy
    df = df.copy()

   # Rename Attributes
    df.rename(columns={'LTE_CSSR RATE without VOLTE_REC':'CSSR wo VoLTE',
                       '4G/LTE Drop Call Rate (without VoLTE)_V7':'DRC wo VoLTE',
                       'Ave 4G/LTE DL User Thrput (ALL) (kbit/s)(kbit/s)':'Avg DL User Thrput kbps',
                       '4G/LTE UL Traffic Volume_REC (GBytes)':'UL Traffic Volume GBytes',
                       '4G/LTE UL User Thrput (ALL) (kbps)_REC':'Avg UL User Thrput kbps',
                       'LTE DL Traffic Volume_REC (GBytes)':'DL Traffic Volume GBytes',
                       'L.Traffic.ActiveUser.Dl.Avg':'Avg DL Traffic Active User',
                       'L.Traffic.ActiveUser.Ul.Avg':'Avg UL Traffic Active User',
                       '4GHW_ Average PRB Usage DL':'Avg DL PRB Usage',
                       '4GHW_ Average PRB Usage UL':'Avg UL PRB Usage',
                       'L.Traffic.User.Avg':'Avg Traffic User'}, inplace=True)

    # Normalize Columns Names
    df.columns = df.columns.str.strip().str.replace(r'[^\w]', '_', regex=True)

    # Remove /
    df['CSSR_wo_VoLTE'] = df['CSSR_wo_VoLTE'].str.replace('/', '', regex=False)

    # Remove NIL
    df.replace('NIL', pd.NA, inplace=True)

   # Create Missing Flags
    df['DRC_wo_VoLTE_missing'] = df['DRC_wo_VoLTE'].isnull().astype(int)
    df['Avg_DL_User_Thrput_kbps_missing'] = df['Avg_DL_User_Thrput_kbps'].isnull().astype(int)
    df['Avg_UL_User_Thrput_kbps_missing'] = df['Avg_UL_User_Thrput_kbps'].isnull().astype(int)
    df['Avg_DL_Traffic_Active_User_missing'] = df['Avg_DL_Traffic_Active_User'].isnull().astype(int)
    df['Avg_UL_Traffic_Active_User_missing'] = df['Avg_UL_Traffic_Active_User'].isnull().astype(int)
    df['Avg_DL_PRB_Usage_missing'] = df['Avg_DL_PRB_Usage'].isnull().astype(int)
    df['Avg_UL_PRB_Usage_missing'] = df['Avg_UL_PRB_Usage'].isnull().astype(int)

    # Replace Missing Values with 0
    df['DRC_wo_VoLTE'] = df['DRC_wo_VoLTE'].fillna(0)
    df['Avg_DL_User_Thrput_kbps'] = df['Avg_DL_User_Thrput_kbps'].fillna(0)
    df['Avg_UL_User_Thrput_kbps'] = df['Avg_UL_User_Thrput_kbps'].fillna(0)
    df['Avg_DL_Traffic_Active_User'] = df['Avg_DL_Traffic_Active_User'].fillna(0)
    df['Avg_UL_Traffic_Active_User'] = df['Avg_UL_Traffic_Active_User'].fillna(0)
    df['Avg_UL_PRB_Usage'] = df['Avg_UL_PRB_Usage'].fillna(0)
    df['Avg_DL_PRB_Usage'] = df['Avg_DL_PRB_Usage'].fillna(0)

     # Drop Duplicates
    df.drop_duplicates()

    # Convert Object to String and Normalizing text fields
    df['eNodeB_Name'] = df['eNodeB_Name'].astype('string')
    df['eNodeB_Name'] = df['eNodeB_Name'].str.strip().str.replace(r'\s+', '', regex=True)
    df['Cell_Name'] = df['Cell_Name'].astype('string')
    df['Cell_Name'] = df['Cell_Name'].str.strip().str.replace(r'\s+', '', regex=True)
    df['eNodeB_Function_Name'] = df['eNodeB_Function_Name'].astype('string')
    df['eNodeB_Function_Name'] = df['eNodeB_Function_Name'].str.strip().str.replace(r'\s+', '', regex=True)
    df['LocalCell_Id'] = df['LocalCell_Id'].astype('string')
    df['LocalCell_Id'] = df['LocalCell_Id'].str.strip().str.replace(r'\s+', '', regex=True)

    # Convert Object to Numeric
    df['CSSR_wo_VoLTE'] = pd.to_numeric(df['CSSR_wo_VoLTE'])
    df['DRC_wo_VoLTE'] = pd.to_numeric(df['DRC_wo_VoLTE'])
    df['Avg_DL_User_Thrput_kbps'] = pd.to_numeric(df['Avg_DL_User_Thrput_kbps'])
    df['UL_Traffic_Volume_GBytes'] = pd.to_numeric(df['UL_Traffic_Volume_GBytes'])
    df['Avg_UL_User_Thrput_kbps'] = pd.to_numeric(df['Avg_UL_User_Thrput_kbps'])
    df['DL_Traffic_Volume_GBytes'] = pd.to_numeric(df['DL_Traffic_Volume_GBytes'])
    df['Avg_DL_Traffic_Active_User'] = pd.to_numeric(df['Avg_DL_Traffic_Active_User'])
    df['Avg_UL_Traffic_Active_User'] = pd.to_numeric(df['Avg_UL_Traffic_Active_User'])
    df['Avg_DL_PRB_Usage'] = pd.to_numeric(df['Avg_DL_PRB_Usage'])
    df['Avg_UL_PRB_Usage'] = pd.to_numeric(df['Avg_UL_PRB_Usage'])
    df['Avg_Traffic_User'] = pd.to_numeric(df['Avg_Traffic_User'])

    # Convert Object to Category
    df['Frequency_band'] = df['Frequency_band'].astype('category')
    df['Cell_FDD_TDD_Indication'] = df['Cell_FDD_TDD_Indication'].astype('category')
    df['Integrity'] = df['Integrity'].astype('category')

    # Convert Object to Bool
    df['DRC_wo_VoLTE_missing'] = df['DRC_wo_VoLTE_missing'].astype(bool)
    df['Avg_DL_User_Thrput_kbps_missing'] = df['Avg_DL_User_Thrput_kbps_missing'].astype(bool)
    df['Avg_UL_User_Thrput_kbps_missing'] = df['Avg_UL_User_Thrput_kbps_missing'].astype(bool)
    df['Avg_DL_Traffic_Active_User_missing'] = df['Avg_DL_Traffic_Active_User_missing'].astype(bool)
    df['Avg_UL_Traffic_Active_User_missing'] = df['Avg_UL_Traffic_Active_User_missing'].astype(bool)
    df['Avg_UL_PRB_Usage_missing'] = df['Avg_UL_PRB_Usage_missing'].astype(bool)
    df['Avg_DL_PRB_Usage_missing'] = df['Avg_DL_PRB_Usage_missing'].astype(bool)

    # Converting Object to Date
    df['Date'] = pd.to_datetime(df['Date'])

    return df


def clean_dataset_hour(df):
    # Make a Copy
    df = df.copy()

   # Rename Attributes
    df.rename(columns={'LTE_CSSR RATE without VOLTE_REC':'CSSR wo VoLTE',
                       '4G/LTE Drop Call Rate (without VoLTE)_V7':'DRC wo VoLTE',
                       'Ave 4G/LTE DL User Thrput (ALL) (kbit/s)(kbit/s)':'Avg DL User Thrput kbps',
                       '4G/LTE UL Traffic Volume_REC (GBytes)':'UL Traffic Volume GBytes',
                       '4G/LTE UL User Thrput (ALL) (kbps)_REC':'Avg UL User Thrput kbps',
                       'LTE DL Traffic Volume_REC (GBytes)':'DL Traffic Volume GBytes',
                       'L.Traffic.ActiveUser.Dl.Avg':'Avg DL Traffic Active User',
                       'L.Traffic.ActiveUser.Ul.Avg':'Avg UL Traffic Active User',
                       '4GHW_ Average PRB Usage DL':'Avg DL PRB Usage',
                       '4GHW_ Average PRB Usage UL':'Avg UL PRB Usage',
                       'L.Traffic.User.Avg':'Avg Traffic User'}, inplace=True)

    # Normalize Columns Names
    df.columns = df.columns.str.strip().str.replace(r'[^\w]', '_', regex=True)

    # Remove /
    df['CSSR_wo_VoLTE'] = df['CSSR_wo_VoLTE'].str.replace('/', '', regex=False)

    # Remove NIL
    df.replace('NIL', pd.NA, inplace=True)

   # Create Missing Flags
    df['DRC_wo_VoLTE_missing'] = df['DRC_wo_VoLTE'].isnull().astype(int)
    df['Avg_DL_User_Thrput_kbps_missing'] = df['Avg_DL_User_Thrput_kbps'].isnull().astype(int)
    df['Avg_UL_User_Thrput_kbps_missing'] = df['Avg_UL_User_Thrput_kbps'].isnull().astype(int)
    df['Avg_DL_Traffic_Active_User_missing'] = df['Avg_DL_Traffic_Active_User'].isnull().astype(int)
    df['Avg_UL_Traffic_Active_User_missing'] = df['Avg_UL_Traffic_Active_User'].isnull().astype(int)
    df['Avg_DL_PRB_Usage_missing'] = df['Avg_DL_PRB_Usage'].isnull().astype(int)
    df['Avg_UL_PRB_Usage_missing'] = df['Avg_UL_PRB_Usage'].isnull().astype(int)

    # Replace Missing Values with 0
    df['DRC_wo_VoLTE'] = df['DRC_wo_VoLTE'].fillna(0)
    df['Avg_DL_User_Thrput_kbps'] = df['Avg_DL_User_Thrput_kbps'].fillna(0)
    df['Avg_UL_User_Thrput_kbps'] = df['Avg_UL_User_Thrput_kbps'].fillna(0)
    df['Avg_DL_Traffic_Active_User'] = df['Avg_DL_Traffic_Active_User'].fillna(0)
    df['Avg_UL_Traffic_Active_User'] = df['Avg_UL_Traffic_Active_User'].fillna(0)
    df['Avg_UL_PRB_Usage'] = df['Avg_UL_PRB_Usage'].fillna(0)
    df['Avg_DL_PRB_Usage'] = df['Avg_DL_PRB_Usage'].fillna(0)

     # Drop Duplicates
    df.drop_duplicates()

    # Convert Object to String and Normalizing text fields
    df['eNodeB_Name'] = df['eNodeB_Name'].astype('string')
    df['eNodeB_Name'] = df['eNodeB_Name'].str.strip().str.replace(r'\s+', '', regex=True)
    df['Cell_Name'] = df['Cell_Name'].astype('string')
    df['Cell_Name'] = df['Cell_Name'].str.strip().str.replace(r'\s+', '', regex=True)
    df['eNodeB_Function_Name'] = df['eNodeB_Function_Name'].astype('string')
    df['eNodeB_Function_Name'] = df['eNodeB_Function_Name'].str.strip().str.replace(r'\s+', '', regex=True)
    df['LocalCell_Id'] = df['LocalCell_Id'].astype('string')
    df['LocalCell_Id'] = df['LocalCell_Id'].str.strip().str.replace(r'\s+', '', regex=True)

    # Convert Object to Numeric
    df['CSSR_wo_VoLTE'] = pd.to_numeric(df['CSSR_wo_VoLTE'])
    df['DRC_wo_VoLTE'] = pd.to_numeric(df['DRC_wo_VoLTE'])
    df['Avg_DL_User_Thrput_kbps'] = pd.to_numeric(df['Avg_DL_User_Thrput_kbps'])
    df['UL_Traffic_Volume_GBytes'] = pd.to_numeric(df['UL_Traffic_Volume_GBytes'])
    df['Avg_UL_User_Thrput_kbps'] = pd.to_numeric(df['Avg_UL_User_Thrput_kbps'])
    df['DL_Traffic_Volume_GBytes'] = pd.to_numeric(df['DL_Traffic_Volume_GBytes'])
    df['Avg_DL_Traffic_Active_User'] = pd.to_numeric(df['Avg_DL_Traffic_Active_User'])
    df['Avg_UL_Traffic_Active_User'] = pd.to_numeric(df['Avg_UL_Traffic_Active_User'])
    df['Avg_DL_PRB_Usage'] = pd.to_numeric(df['Avg_DL_PRB_Usage'])
    df['Avg_UL_PRB_Usage'] = pd.to_numeric(df['Avg_UL_PRB_Usage'])
    df['Avg_Traffic_User'] = pd.to_numeric(df['Avg_Traffic_User'])

    # Convert Object to Category
    df['Frequency_band'] = df['Frequency_band'].astype('category')
    df['Cell_FDD_TDD_Indication'] = df['Cell_FDD_TDD_Indication'].astype('category')
    df['Integrity'] = df['Integrity'].astype('category')

    # Convert Object to Bool
    df['DRC_wo_VoLTE_missing'] = df['DRC_wo_VoLTE_missing'].astype(bool)
    df['Avg_DL_User_Thrput_kbps_missing'] = df['Avg_DL_User_Thrput_kbps_missing'].astype(bool)
    df['Avg_UL_User_Thrput_kbps_missing'] = df['Avg_UL_User_Thrput_kbps_missing'].astype(bool)
    df['Avg_DL_Traffic_Active_User_missing'] = df['Avg_DL_Traffic_Active_User_missing'].astype(bool)
    df['Avg_UL_Traffic_Active_User_missing'] = df['Avg_UL_Traffic_Active_User_missing'].astype(bool)
    df['Avg_UL_PRB_Usage_missing'] = df['Avg_UL_PRB_Usage_missing'].astype(bool)
    df['Avg_DL_PRB_Usage_missing'] = df['Avg_DL_PRB_Usage_missing'].astype(bool)

    # Converting Object to Date
    df['Time'] = pd.to_datetime(df['Time'])

    return df


def clean_dataset_bh(df):
    # Make a Copy
    df = df.copy()

   # Rename Attributes
    df.rename(columns={'LTE_CSSR RATE without VOLTE_REC':'CSSR wo VoLTE',
                       '4G/LTE Drop Call Rate (without VoLTE)_V7':'DRC wo VoLTE',
                       'Ave 4G/LTE DL User Thrput (ALL) (kbit/s)(kbit/s)':'Avg DL User Thrput kbps',
                       '4G/LTE UL Traffic Volume_REC (GBytes)':'UL Traffic Volume GBytes',
                       '4G/LTE UL User Thrput (ALL) (kbps)_REC':'Avg UL User Thrput kbps',
                       'LTE DL Traffic Volume_REC (GBytes)':'DL Traffic Volume GBytes',
                       'L.Traffic.ActiveUser.Dl.Avg':'Avg DL Traffic Active User',
                       'L.Traffic.ActiveUser.Ul.Avg':'Avg UL Traffic Active User',
                       '4GHW_ Average PRB Usage DL':'Avg DL PRB Usage',
                       '4GHW_ Average PRB Usage UL':'Avg UL PRB Usage',
                       'L.Traffic.User.Avg':'Avg Traffic User'}, inplace=True)

    # Normalize Columns Names
    df.columns = df.columns.str.strip().str.replace(r'[^\w]', '_', regex=True)

    # Remove /
    df['CSSR_wo_VoLTE'] = df['CSSR_wo_VoLTE'].str.replace('/', '', regex=False)

    # Remove NIL
    df.replace('NIL', pd.NA, inplace=True)

   # Create Missing Flags
    df['DRC_wo_VoLTE_missing'] = df['DRC_wo_VoLTE'].isnull().astype(int)
    df['Avg_DL_User_Thrput_kbps_missing'] = df['Avg_DL_User_Thrput_kbps'].isnull().astype(int)
    df['Avg_UL_User_Thrput_kbps_missing'] = df['Avg_UL_User_Thrput_kbps'].isnull().astype(int)
    df['Avg_DL_Traffic_Active_User_missing'] = df['Avg_DL_Traffic_Active_User'].isnull().astype(int)
    df['Avg_UL_Traffic_Active_User_missing'] = df['Avg_UL_Traffic_Active_User'].isnull().astype(int)
    df['Avg_DL_PRB_Usage_missing'] = df['Avg_DL_PRB_Usage'].isnull().astype(int)
    df['Avg_UL_PRB_Usage_missing'] = df['Avg_UL_PRB_Usage'].isnull().astype(int)

    # Replace Missing Values with 0
    df['DRC_wo_VoLTE'] = df['DRC_wo_VoLTE'].fillna(0)
    df['Avg_DL_User_Thrput_kbps'] = df['Avg_DL_User_Thrput_kbps'].fillna(0)
    df['Avg_UL_User_Thrput_kbps'] = df['Avg_UL_User_Thrput_kbps'].fillna(0)
    df['Avg_DL_Traffic_Active_User'] = df['Avg_DL_Traffic_Active_User'].fillna(0)
    df['Avg_UL_Traffic_Active_User'] = df['Avg_UL_Traffic_Active_User'].fillna(0)
    df['Avg_UL_PRB_Usage'] = df['Avg_UL_PRB_Usage'].fillna(0)
    df['Avg_DL_PRB_Usage'] = df['Avg_DL_PRB_Usage'].fillna(0)

     # Drop Duplicates
    df.drop_duplicates()

    # Convert Object to String and Normalizing text fields
    df['eNodeB_Name'] = df['eNodeB_Name'].astype('string')
    df['eNodeB_Name'] = df['eNodeB_Name'].str.strip().str.replace(r'\s+', '', regex=True)
    df['Cell_Name'] = df['Cell_Name'].astype('string')
    df['Cell_Name'] = df['Cell_Name'].str.strip().str.replace(r'\s+', '', regex=True)
    df['eNodeB_Function_Name'] = df['eNodeB_Function_Name'].astype('string')
    df['eNodeB_Function_Name'] = df['eNodeB_Function_Name'].str.strip().str.replace(r'\s+', '', regex=True)
    df['LocalCell_Id'] = df['LocalCell_Id'].astype('string')
    df['LocalCell_Id'] = df['LocalCell_Id'].str.strip().str.replace(r'\s+', '', regex=True)

    # Convert Object to Numeric
    df['CSSR_wo_VoLTE'] = pd.to_numeric(df['CSSR_wo_VoLTE'])
    df['DRC_wo_VoLTE'] = pd.to_numeric(df['DRC_wo_VoLTE'])
    df['Avg_DL_User_Thrput_kbps'] = pd.to_numeric(df['Avg_DL_User_Thrput_kbps'])
    df['UL_Traffic_Volume_GBytes'] = pd.to_numeric(df['UL_Traffic_Volume_GBytes'])
    df['Avg_UL_User_Thrput_kbps'] = pd.to_numeric(df['Avg_UL_User_Thrput_kbps'])
    df['DL_Traffic_Volume_GBytes'] = pd.to_numeric(df['DL_Traffic_Volume_GBytes'])
    df['Avg_DL_Traffic_Active_User'] = pd.to_numeric(df['Avg_DL_Traffic_Active_User'])
    df['Avg_UL_Traffic_Active_User'] = pd.to_numeric(df['Avg_UL_Traffic_Active_User'])
    df['Avg_DL_PRB_Usage'] = pd.to_numeric(df['Avg_DL_PRB_Usage'])
    df['Avg_UL_PRB_Usage'] = pd.to_numeric(df['Avg_UL_PRB_Usage'])
    df['Avg_Traffic_User'] = pd.to_numeric(df['Avg_Traffic_User'])

    # Convert Object to Category
    df['Frequency_band'] = df['Frequency_band'].astype('category')
    df['Cell_FDD_TDD_Indication'] = df['Cell_FDD_TDD_Indication'].astype('category')
    df['Integrity'] = df['Integrity'].astype('category')

    # Convert Object to Bool
    df['DRC_wo_VoLTE_missing'] = df['DRC_wo_VoLTE_missing'].astype(bool)
    df['Avg_DL_User_Thrput_kbps_missing'] = df['Avg_DL_User_Thrput_kbps_missing'].astype(bool)
    df['Avg_UL_User_Thrput_kbps_missing'] = df['Avg_UL_User_Thrput_kbps_missing'].astype(bool)
    df['Avg_DL_Traffic_Active_User_missing'] = df['Avg_DL_Traffic_Active_User_missing'].astype(bool)
    df['Avg_UL_Traffic_Active_User_missing'] = df['Avg_UL_Traffic_Active_User_missing'].astype(bool)
    df['Avg_UL_PRB_Usage_missing'] = df['Avg_UL_PRB_Usage_missing'].astype(bool)
    df['Avg_DL_PRB_Usage_missing'] = df['Avg_DL_PRB_Usage_missing'].astype(bool)

    # Converting Object to Date
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d', errors='coerce')
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M', errors='coerce').dt.time
    
    df['DateTime'] = pd.to_datetime(df['Date'].astype(str) + ' ' + df['Time'].astype(str), errors='coerce')

    df['Hour'] = df['DateTime'].dt.hour

    return df


def clean_dataset2(df):
    # Make a Copy
    df = df.copy()

    # Renaming Attributes
    df.rename(columns={'AVG_DL_USER_THROUGHPUT':'Avg DL User Thrput kbps',
                       'L.Traffic.ActiveUser.DL.Avg':'Avg DL Traffic Active User'}, inplace=True)
    
    df.head()

    # Normalize Columns Names
    df.columns = df.columns.str.strip().str.replace(r'[^\w]', '_', regex=True)

     # Drop Duplicates
    df.drop_duplicates()

    # Convert Object to String and Normalizing text fields
    df['eNodeB_Function_Name'] = df['eNodeB_Function_Name'].astype('string')
    df['eNodeB_Function_Name'] = df['eNodeB_Function_Name'].str.strip().str.replace(r'\s+', '', regex=True)
    df['Cell_Name'] = df['Cell_Name'].astype('string')
    df['Cell_Name'] = df['Cell_Name'].str.strip().str.replace(r'\s+', '', regex=True)

    # Convert Object to Numeric
    df['Avg_DL_User_Thrput_kbps'] = pd.to_numeric(df['Avg_DL_User_Thrput_kbps'])
    df['Avg_DL_Traffic_Active_User'] = pd.to_numeric(df['Avg_DL_Traffic_Active_User'])

    # Convert Object to Category
    df['Frequency_band'] = df['Frequency_band'].astype('category')

    # Converting Object to Date
    df['Time'] = pd.to_datetime(df['Time'])
    df['Date'] = pd.to_datetime(df['Date'])
    df['Hour'] = df['Hour'].astype(int)

    return df