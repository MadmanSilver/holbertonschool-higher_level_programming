#!/usr/bin/python3
def multiple_returns(sentance):
    if len(sentance) < 1:
        return (len(sentance), None)
    return (len(sentance), sentance[0])
