import streamlit as st
import hashlib
import sys
from features import FE
from feedback import Feedback_Generation,load_df

sys.tracebacklimit=0
st.set_page_config(page_title="FYP",layout="wide")

widget_values = {}
def make_recording_widget(f):
    """Return a function that wraps a streamlit widget and records the
    widget's values to a global dictionary.
    """
    def wrapper(label, *args, **kwargs):
        widget_value = f(label, *args, **kwargs)
        widget_values[label] = widget_value
        return widget_value

    return wrapper

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()
def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False
# DB Management
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_userdata(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data


def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

def post_login():

    c1,c2 = st.columns([2,2])
    opt = 0
    inst=[]
    option = c1.selectbox('Select the task you want to solve',('Selection sort','First negative element in List','Largest element in list','Unique characters count'))
    ques = ""
    if option == 'Selection sort':
        opt=1
        ques = "Write a program which performs selection sort on a list."
        inst.append("Define a function to perform swapping of elements.")
        inst.append("Define a function to find the position of the smallest element from a given index.")
        inst.append("Define a function to perform sorting.")

    elif option == 'First negative element in List':
        opt=2
        ques = "Write a program which returns the index of first negative element in the list."
        inst.append("Traverse through list and find the first negative element in the list.")
        inst.append("Use a method to stop the traversal once first negative element is encountered.")
        inst.append("Print the position of the first negative element.")
    elif option == 'Largest element in list':
        opt=3
        ques = "Write a program which returns the index of largest element in the list."
        inst.append("Traverse through list and find the largest element in the list.")
        inst.append("Traverse entire list till the end.")
        inst.append("Print the position of the largest element.")
    else:
        opt=4
        ques = "Write a program which returns the count of unique characters in a set of lines."
        inst.append("Ignore special characters like punctuation characters.")
        inst.append("Ignore case of character.")
        inst.append("Return the count of unique characters in the string.(Only count the first occurence)")

    text = c1.text_area('Enter code',height=500,placeholder=ques)
    button = make_recording_widget(st.button)
    submit = button('Submit')

    c1.subheader("Hints/Suggestions")
    for ins in inst:
        c1.write(ins)
    if submit:
        feature_vector = FE(str(text))
        if type(feature_vector)==type(-1):
            codeObejct = compile(text, 'Submission', 'exec')
            exec(codeObejct)
        else:
            lst,sc_sub= Feedback_Generation(feature_vector,opt)
            c2.header("Score: "+ str(sc_sub) + " / " +str(10))
            c2.subheader("Feedback: ")
            for com in lst:
                c2.write(com)
            if len(lst) == 0:
                c2.write("No feedbacks. The code is perfect.")

    btn = button('View Best Code?')
    if btn:
        df = load_df(opt)
        c2.write()
        c2.write()
        c2.subheader('Best Code')
        c2.code(df.iloc[0,3],language='python')



st.header("STUDENT CODE SUBMISSION PORTAL")

username = st.sidebar.text_input('Username')
password = st.sidebar.text_input('Password',type = 'password')
c1,c2 = st.sidebar.columns(2)
login = c1.button('Login')
signup = c2.button('Sign Up')

flag = True
if signup:
    flag = False
    create_usertable()
    add_userdata(username,make_hashes(password))
    st.sidebar.success("You have successfully created a valid Account")

if flag:
    create_usertable()
    hashed_pswd = make_hashes(password)
    result = login_user(username,check_hashes(password,hashed_pswd))
    if result:
        st.sidebar.success("Logged In as {}".format(username))
        post_login()
