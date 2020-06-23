import sys
import os
import pandas as pd
import argparse 
import src.functions as func


parser = argparse.ArgumentParser(description="Introduce the type of house and the number of rooms and the program will return its average price and maximum number of car parks")
parser.add_argument("-o", "--home", type=str, help="Introduce your preferred type of home")
parser.add_argument("-r", "--rooms", type=int, default=3, help="And now the number of rooms you would like")
parser.add_argument("-c", "--curr", type=str, default="EUR", help="And finally your currency of choice")
args = parser.parse_args()
print(args)


def main():
    func.check_home(args.home) #check 1st input is correct
    func.check_room(args.rooms) #check 2nd input is correct
    func.check_curr(args.curr) #check 3rd input is correct

    func.openDataSet() #open up the dataset
    func.openDataSetApi() #open up the API dataset
    
    func.drawMax(args.home, args.rooms) #draw most expensive for type of home and number of rooms 
    func.drawAvg(args.home, args.rooms) #draw average price for type of home and number of rooms 
    """
    func.changeCurr(args.curr) #change currency from € to the one asked for
    """

    """
    functions.plot_chart(home, rooms) #plot a graph 
    """

if __name__ == '__main__':
    main()
