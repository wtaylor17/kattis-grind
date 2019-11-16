#!/usr/bin/env python3
import os
import sys
import shutil
import pathlib
import requests
import argparse

ISON_WINDOWS = sys.platform == 'win32'
EXE_NAME = 'a' if ISON_WINDOWS else './a.out'
WRITER_NAME = 'type' if ISON_WINDOWS else 'cat'
parser = argparse.ArgumentParser(description='Runs Kattis problem through their test cases')
parser.add_argument('--id', type=str, default='_NONE_', help='id of problem to fetch')
parser.add_argument('--precision',type=float,default=0,help='numeric precision of answers (default 0)')
args = parser.parse_args()
qid = args.id
precision = abs(args.precision)

if qid == '_NONE_':
    qid = input('Enter ID: ')
qdir = os.path.join(os.getcwd(),qid)

qext = 'z'
while qext != 'cpp' and qext[0] != 'p':
    qext = input('Which language (python/cpp) (if python, specify interpreter name e.g. python3): ').lower()

if qext[0] == 'p':
    if ISON_WINDOWS:
        EXE_NAME = '%s "%s"'%(qext,os.path.join(qdir,'_%s.py'%qid))

isinfile_inqdir = lambda name: name.startswith("input") and os.path.isfile(os.path.join(qdir,name))
input_files = list(filter(isinfile_inqdir, os.listdir(qdir)))
ilen = len(input_files)

if qext[0]=='c':
    os.system('g++ \"' + qdir + '/_' + qid + '.cpp\"')

for i in range(ilen):
    print('TEST CASE ' + str(i+1))
    output = os.popen('%s \"'%WRITER_NAME + os.path.join(qdir,'input' + str(i+1)) + '\" | %s'%EXE_NAME).read().rstrip()
    print('OUTPUT:')
    print(output)
    tokens = output.split()
    with open(qdir + '/output' + str(i+1)) as expected:
        content = expected.read().rstrip()
        ctokens = content.split()
        print('EXPECTED OUTPUT:')
        print(content)
        if content==output:
            print('PASSED')
        elif precision>0:
            if len(ctokens) != len(tokens):
                print('FAILED: incorrect number of tokens.')
            else:
                good=True
                for t,ct in zip(tokens,ctokens):
                    try:
                        tf = float(t)
                        ctf = float(ct)
                        if abs(tf-ctf)>precision:
                            good=False
                            print('FAILED')
                            break
                    except:
                        if t!=ct:
                            print('FAILED')
                            good=False
                            break
                if good:
                    print('PASSED')
        else:
            print('FAILED')
