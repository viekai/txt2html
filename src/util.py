#!/usr/bin/env python

def lines(file):
    for line in file:
            yield line
    yield '\n'

def newBlock(block):
    if(block):
        ret = ''.join(block).strip()
    else:
        ret = '' 
    return ret

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            if line.strip()[0] == "-":
                yield newBlock(block);
                block = []
            block.append(line);
        else:
            yield newBlock(block)
            block = []

