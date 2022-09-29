import pandas as pd
import ast
import re
from collections import deque
import inspect
import importlib


def FE(code):

    df = pd.DataFrame()
    while_c = []
    for_c= []
    if_c= []
    elif_c=[]
    else_c=[]
    return_c=[]
    break_c=[]
    continue_c=[]
    pass_c=[]

    assign_c=[]
    arith_c=[]
    comp_c=[]
    log_c=[]
    bit_c=[]
    iden_c=[]
    mem_c=[]
    s = str(code)
    dct={
        'if':0,
        'elif':0,
        'else':0,
        'while':0,
        'for':0,
        'return':0,
        'break':0,
        'continue':0,
        'pass':0,

        '=':0,
        '+=':0,
        '-=':0,
        '*=':0,
        '/=':0,
        '//=':0,
        '**=':0,
        '%=':0,
        '&=':0,
        '|=':0,
        '^=':0,
        '>>=':0,
        '<<=':0,

        '==':0,
        '!=':0,
        '>':0,
        '>=':0,
        '<':0,
        '<=':0,

        'and':0,
        'or':0,
        'not':0,

        '+':0,
        '-':0,
        '*':0,
        '/':0,
        '//':0,
        '**':0,
        '%':0,

        '&':0,
        '|':0,
        '^':0,
        '~':0,
        '<<':0,
        '>>':0,

        'is':0,
        'is not':0,

        'in':0,
        'not in':0

        }

    for i in (re.split(' |\t|\n',s)):
        dct[i] = dct.get(i,0)+1

    for i in dct.keys():

        if len(i)>5 and i[:5] == 'while' and i[5]=='(':
            dct['while']+=dct.get(i,0)
        elif len(i)>3 and i[:3] == 'for' and i[3]=='(':
            dct['for']+=dct.get(i,0)
        elif len(i)>2 and i[:2]=='if' and i[2]=='(':
            dct['if']+=dct.get(i,0)
        elif len(i)>4 and i[:4]=='elif' and i[4]=='(':
            dct['elif']+=dct.get(i,0)
        elif len(i)>4 and i[:4]=='else' and i[4]==':':
            dct['else']+=dct.get(i,0)


        elif len(i)>2 and '==' in i:
            dct['==']+=dct.get(i,0)
        elif len(i)>2 and '!=' in i:
            dct['!=']+=dct.get(i,0)
        elif len(i)>2 and '>=' in i:
            dct['>=']+=dct.get(i,0)
        elif len(i)>2 and '<=' in i:
            dct['<=']+=dct.get(i,0)

        elif len(i)>2 and '+=' in i:
            dct['+=']+=dct.get(i,0)
        elif len(i)>2 and '-=' in i:
            dct['-=']+=dct.get(i,0)
        elif len(i)>2 and '*=' in i:
            dct['*=']+=dct.get(i,0)
        elif len(i)>2 and '/=' in i:
            dct['/=']+=dct.get(i,0)
        elif len(i)>2 and '%=' in i:
            dct['%=']+=dct.get(i,0)
        elif len(i)>3 and '//=' in i:
            dct['//=']+=dct.get(i,0)
        elif len(i)>3 and '**=' in i:
            dct['**=']+=dct.get(i,0)

        elif len(i)>3 and '>>=' in i:
            dct['>>=']+=dct.get(i,0)
        elif len(i)>3 and '<<=' in i:
            dct['<<=']+=dct.get(i,0)
        elif len(i)>2 and '&=' in i:
            dct['&=']+=dct.get(i,0)
        elif len(i)>2 and '|=' in i:
            dct['|=']+=dct.get(i,0)
        elif len(i)>2 and '^=' in i:
            dct['^=']+=dct.get(i,0)


        elif len(i)>2 and '//' in i:
            dct['//']+=dct.get(i,0)
        elif len(i)>2 and '**' in i:
            dct['**']+=dct.get(i,0)
        elif len(i)>1 and '+' in i:
            dct['+']+=dct.get(i,0)
        elif len(i)>1 and '-' in i:
            dct['-']+=dct.get(i,0)
        elif len(i)>1 and '*' in i:
            dct['*']+=dct.get(i,0)
        elif len(i)>1 and '/' in i:
            dct['/']+=dct.get(i,0)
        elif len(i)>1 and '%' in i:
            dct['%']+=dct.get(i,0)

        elif len(i)>1 and '&' in i:
            dct['&']+=dct.get(i,0)
        elif len(i)>1 and '|' in i:
            dct['|']+=dct.get(i,0)
        elif len(i)>1 and '^' in i:
            dct['^']+=dct.get(i,0)
        elif len(i)>1 and '~' in i:
            dct['~']+=dct.get(i,0)
        elif len(i)>2 and '>>' in i:
            dct['>>']+=dct.get(i,0)
        elif len(i)>2 and '<<' in i:
            dct['<<']+=dct.get(i,0)



        elif len(i)>1 and '=' in i:
            dct['=']+=dct.get(i,0)
        elif len(i)>1 and '<' in i:
            dct['<']+=dct.get(i,0)
        elif len(i)>1 and '>' in i:
            dct['>']+=dct.get(i,0)



    dct['is not'] = s.count('is not')
    dct['is']-=dct['is not']
    dct['not']-=dct['is not']

    dct['not in'] = s.count('not in')
    dct['in']-=dct['not in']
    dct['not']-=dct['not in']

    while_c.append(dct['while'])
    for_c.append(dct['for'])
    if_c.append(dct['if'])
    elif_c.append(dct['elif'])
    else_c.append(dct['else'])
    return_c.append(dct['return'])
    break_c.append(dct['break'])
    continue_c.append(dct['continue'])
    pass_c.append(dct['pass'])

    assign_c.append(dct['=']+dct['+=']+dct['-=']+dct['*=']+dct['/=']+dct['%=']+dct['//=']+dct['**=']+dct['&=']+dct['|=']+dct['^=']+dct['>>=']+dct['<<='])
    arith_c.append(dct['+=']+dct['-=']+dct['*=']+dct['/=']+dct['%=']+dct['//=']+dct['**=']+dct['+']+dct['-']+dct['*']+dct['/']+dct['//']+dct['%']+dct['**'])
    comp_c.append(dct['==']+dct['!=']+dct['>']+dct['<']+dct['<=']+dct['>='])
    log_c.append(dct['and']+dct['not']+dct['or'])
    bit_c.append(dct['&=']+dct['|=']+dct['^=']+dct['>>=']+dct['<<=']+dct['&']+dct['|']+dct['^']+dct['~']+dct['<<']+dct['>>'])
    iden_c.append(dct['is']+dct['is not'])
    mem_c.append(dct['in']+dct['not in'])

    df['while'] = while_c
    df['for'] = for_c
    df['if'] = if_c
    df['elif'] = elif_c
    df['else'] = else_c
    df['return'] = return_c
    df['break'] = break_c
    df['continue'] = continue_c
    df['pass'] = pass_c

    df['assign'] = assign_c
    df['arith'] = arith_c
    df['comp'] = comp_c
    df['log'] = log_c
    df['bit'] = bit_c
    df['iden'] = iden_c
    df['mem'] = mem_c

    func_lst = []
    func_calls = []
    fn = []
    fc = []
    gc = []

    class CountFunc(ast.NodeVisitor):
      func_count = 0
      def visit_FunctionDef(self, node):
        self.func_count += 1
        func_lst.append(node.name)

    class FuncCallVisitor(ast.NodeVisitor):
      def __init__(self):
        self._name = deque()

      @property
      def name(self):
        return '.'.join(self._name)
      @name.deleter
      def name(self):
        self._name.clear()

      def visit_Name(self, node):
        self._name.appendleft(node.id)

      def visit_Attribute(self, node):
        try:
          self._name.appendleft(node.attr)
          self._name.appendleft(node.value.id)
        except AttributeError:
          self.generic_visit(node)

    def get_func_calls(tree):
      for node in ast.walk(tree):
          if isinstance(node, ast.Call):
            callvisitor = FuncCallVisitor()
            callvisitor.visit(node.func)
            if callvisitor.name in func_lst:
              func_calls.append(callvisitor.name)
    try:
        p = ast.parse(s)
    except:
        return -1
    f = CountFunc()
    f.visit(p)
    get_func_calls(p)
    fn.append(len(func_lst))
    fc.append(len(func_calls))
    gc.append(str(p.body).count('Assign'))
    df['#fun']=fn
    df['#fcall']=fc
    df['globals']=gc

    l=[]
    temp = str(ast.dump(p))
    l.append(temp.count('List')+temp.count('Tuple'))
    df['#lst'] = l
    df['cond'] = df['if']+df['elif']+df['else']
    df['loop'] = df['for']+df['while']

    line_c=[]
    f = open("temp.py", "w")
    f.write(s)
    f.close()
    f = open("temp.py","r")
    lines = f.readlines()
    line_c.append(len(lines))
    line_temp = 0
    el_c=[]
    com_c=[]
    for line in lines:
      if '#' in line and line.index('#')+1<len(line) and line[line.index('#')+1]!='!':
        line_temp+=1
    el_c.append(lines.count('\n'))
    com_c.append(line_temp)
    f.close()
    df['#lines'] = line_c
    df['#emptylines'] = el_c
    df['#comments'] = com_c

    class_c=[]
    count = 0
    for j in ast.walk(p):
      if isinstance(j,ast.ClassDef):
        count+=1
    class_c.append(count)
    df['#class'] = class_c


    avg_lines=[]
    count = 0
    sum_line = 0
    for j in ast.walk(p):
      if isinstance(j,ast.FunctionDef):
        count+=1
        sum_line+=j.end_lineno - j.lineno + 1
    if(count==0):
      avg_lines.append(0)
    else:
      avg_lines.append(sum_line/count)
    df['avg_lines_per_func'] = avg_lines

    var_c=[]
    con_c=[]
    vars=[]
    count1 = 0
    count2 = 0
    m=[]
    t=[]
    for j in ast.walk(p):
      if isinstance(j,ast.Call):
        try:
          m.append(j.func.id)
        except:
          continue
    for j in ast.walk(p):
      if isinstance(j,ast.Name) and j.id not in m:
        count1+=1
        t.append(j.id)
      if isinstance(j,ast.Constant):
        count2+=1
    var_c.append(count1)
    con_c.append(count2)
    vars.append(len(set(t)))
    df['#var_uses']=var_c
    df['#con_uses']=con_c
    df['#var']=vars




    return df
