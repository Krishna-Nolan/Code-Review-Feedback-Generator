import numpy as np
import pandas as pd
import seaborn as sns
import random
import matplotlib.pyplot as plt
import streamlit as st

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from sklearn.model_selection import train_test_split
from sklearn.utils._testing import ignore_warnings

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def load_df(opt):
    if opt == 2:
        df = pd.read_csv('Data/fn.csv')
    elif opt == 3:
        df = pd.read_csv('Data/la.csv')
    elif opt == 1:
        df = pd.read_csv('Data/ss.csv')
    else:
        df = pd.read_csv('Data/uc.csv')
    return df


@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def remove_unwanted_cols(df):
    cols = ['new_upload','return', 'break', 'continue', 'pass', 'assign','arith', 'comp', 'log','#fun', '#fcall','globals','cond', 'loop', '#lst', '#lines', '#var_uses', '#var']
    x = df[cols]
    y = df['score']
    nunique = x.nunique()
    cols_to_drop = nunique[nunique == 1].index
    x = x.drop(cols_to_drop, axis=1)
    return x,y

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def golden_vect(opt,df):
    if opt == 2:
        t_df = df[df['score']==10]
        gv = dict(t_df.mean().round())
    elif opt == 3:
        t_df = df[df['score']==10]
        gv = dict(t_df.mean().round())
    elif opt == 1:
        t_df = df[df['score']==10]
        gv = dict(t_df.mean().round())
    else:
        t_df = df[df['score']==10]
        gv = dict(t_df.mean().round())
    return gv

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def select_subset_features(df):
    x,y = remove_unwanted_cols(df)
    x = x.drop(['new_upload'],axis=1)
    cols=list(x.columns)
    fs = SelectKBest(score_func=f_regression, k='all')
    fs.fit(x,y)
    dct_fr={}
    scores=list(fs.scores_)
    for i in range(len(scores)):
        dct_fr[cols[i]]=scores[i]
    dct_fr = dict(sorted(dct_fr.items(), key = lambda x: x[1], reverse = True))
    cols_fr=[]
    df_fr = pd.DataFrame(dict(sorted(dct_fr.items(), key = lambda x: x[1], reverse = True)).items(), columns=['Feature', 'f_reg score'])
    for k,v in dict(sorted(dct_fr.items(), key = lambda x: x[1], reverse = True)).items():
        cols_fr.append(k)
    print(df_fr)
    return cols_fr

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def train_model(df,cols_fr):
    x,y = remove_unwanted_cols(df)
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3,random_state=24)
    model = RandomForestRegressor(random_state=0)
    model.fit(x_train[cols_fr],y_train)
    y_pred = model.predict(x_test[cols_fr])
    print("MAE : ",mean_absolute_error(y_test,y_pred))
    print("MSE : ",mean_squared_error(y_test,y_pred,squared=False))
    return model

def feedbacks(dct):
    lst = []
    for key in dct.keys():
        if key =='return':
            if dct[key][1]>0:
                lst.append("Increase the number of return statements.")
            elif dct[key][1]<0:
                lst.append("Decrease the number of return statements.")

        elif key == 'break':
            if dct[key][1]>0:
                lst.append("Increase the number of break statements.")
            elif dct[key][1]<0:
                lst.append("Decrease the number of break statements.")

        elif key == 'continue':
            if dct[key][1]>0:
                lst.append("Increase the number of continue statements.")
            elif dct[key][1]<0:
                lst.append("Decrease the number of continue statements.")

        elif key == 'pass':
            if dct[key][1]>0:
                lst.append("Increase the number of pass statements.")
            elif dct[key][1]<0:
                lst.append("Decrease the number of pass statements.")

        elif key == 'assign':
            if dct[key][1]>0:
                lst.append("The number of assignment statements can be increased.")
            elif dct[key][1]<0:
                lst.append("The number of assignment statements can be decreased.")

        elif key == 'arith':
            if dct[key][1]>0:
                lst.append("The number of arithmetic operators in the program can be increased.")
            elif dct[key][1]<0:
                lst.append("The number of arithmetic operators in the program can be decreased.")

        elif key == 'comp':
            if dct[key][1]>0:
                lst.append("The number of comparison operators in the program can be increased.")
            elif dct[key][1]<0:
                lst.append("The number of comparison operators in the program can be decreased.")

        elif key == 'log':
            if dct[key][1]>0:
                lst.append("The number of logical operators in the program can be increased.")
            elif dct[key][1]<0:
                lst.append("The number of logical operators in the program can be decreased.")

        elif key == '#fun':
            if dct[key][1]>0:
                lst.append("Define more functions.")
            elif dct[key][1]<0:
                lst.append("There are too many functions defined.")

        elif key == '#fcall':
            if dct[key][1]>0:
                lst.append("Function calls in the program can be increased.")
            elif dct[key][1]<0:
                lst.append("Function calls in the program can be decreased.")

        elif key == 'globals':
            if dct[key][1]>0:
                lst.append("Define more global variables.")
            elif dct[key][1]<0:
                lst.append("Reduce the number of global variables defined.")

        elif key == 'cond':
            if dct[key][1]>0:
                lst.append("Increase the number of conditional statements(if,elif,else).")
            elif dct[key][1]<0:
                lst.append("Decrease the number of conditional statements(if,elif,else).")

        elif key == 'loop':
            if dct[key][1]>0:
                lst.append("Increase the number of loops(for,while).")
            elif dct[key][1]<0:
                lst.append("Decrease the number of loops(for,while).")

        elif key == '#lst':
            if dct[key][1]>0:
                lst.append("Increase the number of lists or/and tuples used in the program.")
            elif dct[key][1]<0:
                lst.append("Decrease the number of lists or/and tuples used in the program.")

        elif key == '#lines':
            if dct[key][1]<0:
                lst.append("Reduce the number of lines in the program.")

        elif key == '#var_uses':
            if dct[key][1]>0:
                lst.append("Increase the number of times variables are used.")
            elif dct[key][1]<0:
                lst.append("Reduce the number of times variables are used.")

        elif key == '#var':
            if dct[key][1]>0:
                lst.append("Increase the number of variables defined.")
            elif dct[key][1]<0:
                lst.append("Reduce the number of variables defined.")

    return lst

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def feedbackgen(model,cols_fr,gv,feat_vect):
    check = feat_vect[cols_fr].iloc[[0]]
    sc_sub = int(model.predict(check)[0].round())
    print("Predicted Score:", sc_sub)
    dct={}
    old_score = model.predict(check)[0]
    for col in cols_fr:
      temp = check.copy()
      temp[col] = gv[col]
      new_score = model.predict(temp)[0]
      if new_score > old_score:
        dct[col]=(new_score-old_score,int(gv[col].round())-int(check[col].round()))
    dct = dict(sorted(dct.items(), key=lambda item: item[1], reverse=True))
    print()
    lst = feedbacks(dct)
    return lst,sc_sub

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def Feedback_Generation(feat_vect,opt):
    df = load_df(opt)
    if opt == 1:
        gv = golden_vect(opt,df)
        cols = select_subset_features(df)
        model = train_model(df,cols[:13])
        lst,sc_sub = feedbackgen(model,cols[:13],gv,feat_vect)
    if opt == 2:
        gv = golden_vect(opt,df)
        cols = select_subset_features(df)
        model = train_model(df,cols[:10])
        lst,sc_sub = feedbackgen(model,cols[:10],gv,feat_vect)
    if opt == 3:
        gv = golden_vect(opt,df)
        cols = select_subset_features(df)
        model = train_model(df,cols[:8])
        lst,sc_sub = feedbackgen(model,cols[:8],gv,feat_vect)
    if opt == 4:
        gv = golden_vect(opt,df)
        cols = select_subset_features(df)
        model = train_model(df,cols[:8])
        lst,sc_sub = feedbackgen(model,cols[:8],gv,feat_vect)
    return lst,sc_sub
